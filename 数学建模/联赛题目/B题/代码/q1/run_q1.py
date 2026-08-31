"""B题 Q1 正式求解入口：候选簇 + 受限加油集精确 DP + 架次—人员流规划。

流水线
    [1] 读入并校验官方数据，1600 人聚合为 104 个 OD 请求组；
    [2] 按"种子设施 + 近邻"枚举候选簇（每架次至多 5 次海上着陆）；
    [3] 对每个 (机场, 机型, 簇) 在配置的加油候选集内精确求解；
    [4] 按单位座位用时筛选候选池，并保证每组覆盖度；
    [5] 贪心构造初始解 → CP-SAT 求解主目标 T_air；
    [6] 解引导的大邻域扩池 + 重解（LNS 轮次）；
    [7] 固定 T_air 后依次优化 T_pax、油耗、架次数、座位利用率（词典序）；
    [8] 拆分、局部改进并回灌物理列，有限轮重求至指标一致；
    [9] 写出官方 CSV，并用两套独立检查器复核。
"""

from __future__ import annotations

import argparse
import math
import time
from dataclasses import asdict, dataclass, replace
from pathlib import Path

import pandas as pd

from common.data_loader import load_distances, load_people_q1
from common.grouping import group_q1
from common.models import SolutionMetrics
from common.paths import Q1_OUTPUT_DIR, resolve_data_dir
from q1.algorithms.clusters import (
    RouteColumn,
    build_columns,
    enumerate_clusters,
    expand_clusters,
    number_columns,
    select_columns,
)
from q1.algorithms.flight_builder import (
    Flight,
    aggregate,
    assign_people,
    flight_order,
    improve_flights,
    split_flows,
    to_columns,
)
from q1.algorithms.flow_master import FlowMaster, FlowSolution
from q1.algorithms.greedy import greedy_solution
from q1.config import QUICK_CONFIG, Q1AlgorithmConfig
from q1.io.csv_validator import validate_q1_csv
from q1.io.csv_writer import write_flight_csv, write_flight_plan, write_summary

_LEX_STAGES = ("aircraft_time", "passenger_time", "fuel", "flights", "seat_utilization")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="B题 Q1 正式求解")
    parser.add_argument("--quick", action="store_true", help="小预算冒烟运行")
    parser.add_argument("--workers", type=int, default=None)
    parser.add_argument("--lns-rounds", type=int, default=None)
    parser.add_argument("--primary-seconds", type=float, default=None)
    parser.add_argument("--secondary-seconds", type=float, default=None)
    parser.add_argument("--efficiency-slack", type=float, default=None)
    parser.add_argument("--data-dir", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--refuel-keep", type=int, default=None)
    return parser.parse_args()


def _config(args: argparse.Namespace) -> Q1AlgorithmConfig:
    config = QUICK_CONFIG if args.quick else Q1AlgorithmConfig()
    overrides = {
        "lns_rounds": args.lns_rounds,
        "primary_time_limit_seconds": args.primary_seconds,
        "secondary_time_limit_seconds": args.secondary_seconds,
        "efficiency_slack": args.efficiency_slack,
        "seed": args.seed,
        "refuel_keep": args.refuel_keep,
    }
    return replace(config, **{key: value for key, value in overrides.items() if value is not None})


def _metrics_row(label: str, metrics: SolutionMetrics, extra: dict) -> dict:
    row = {
        "stage": label,
        "T_air": metrics.total_aircraft_time,
        "T_pax": metrics.total_passenger_time,
        "fuel": metrics.total_fuel,
        "flights": metrics.number_of_flights,
        "PK": metrics.passenger_km,
        "AK": metrics.available_seat_km,
        "seat_utilization": metrics.seat_utilization,
    }
    row.update(extra)
    return row


def _realize(
    master: FlowMaster,
    solution: FlowSolution,
    groups_by_id: dict,
    distances: dict,
    *,
    refuel_keep: int = 4,
) -> list[Flight]:
    """(y, z) -> 具体架次副本 -> 不劣化的局部改进。"""
    index = {column.column_id: column for column in master.columns}
    flights = split_flows(index, solution.multiplicities, solution.flows, groups_by_id)
    return improve_flights(
        flights, groups_by_id, distances, refuel_keep=refuel_keep
    )


@dataclass(frozen=True)
class FeedbackResult:
    master: FlowMaster
    columns: list[RouteColumn]
    pool: list[RouteColumn]
    solution: FlowSolution
    flights: list[Flight]
    metrics: SolutionMetrics
    rounds: int
    columns_fed_back: int
    solver_matches_delivery: bool


def _physical_signature(column: RouteColumn) -> tuple[object, ...]:
    return (
        column.base_airport,
        column.aircraft_type,
        column.route,
        column.refuel_decisions,
    )


def _metrics_match(solution: FlowSolution, metrics: SolutionMetrics) -> bool:
    return (
        solution.aircraft_time == metrics.total_aircraft_time
        and solution.passenger_time == metrics.total_passenger_time
        and math.isclose(solution.fuel, metrics.total_fuel, abs_tol=1e-6)
        and solution.flights == metrics.number_of_flights
        and math.isclose(solution.passenger_km, metrics.passenger_km, abs_tol=1e-6)
        and math.isclose(
            solution.available_seat_km, metrics.available_seat_km, abs_tol=1e-6
        )
    )


def solve_realize_feedback(
    groups,
    columns: list[RouteColumn],
    groups_by_id: dict,
    distances: dict,
    config: Q1AlgorithmConfig,
    *,
    workers: int | None = None,
    incumbent_flights: list[Flight] | None = None,
    stages: tuple[str, ...] = _LEX_STAGES,
    seed: int | None = None,
) -> FeedbackResult:
    """求解—落地—物理列回灌，直到交付指标与主问题一致或达到轮次上限。"""
    working = number_columns(columns)
    incumbent = incumbent_flights
    incumbent_metrics = (
        aggregate(incumbent, groups_by_id, distances) if incumbent else None
    )
    fed = 0
    last: tuple[FlowMaster, list[RouteColumn], FlowSolution, list[Flight], SolutionMetrics]

    for round_number in range(config.max_feedback_rounds + 1):
        pinned = _incumbent_ids(working, incumbent) if incumbent else ()
        master, pool, _ = _build_master(groups, working, config, pinned=pinned)
        if incumbent_metrics is not None:
            master.upper_bounds_by_metric["aircraft_time"] = (
                incumbent_metrics.total_aircraft_time
            )
        hint = _warm_start(master, incumbent, groups_by_id) if incumbent else None
        solution = master.solve(
            time_limit_seconds=config.secondary_time_limit_seconds,
            workers=workers,
            warm_start=hint,
            stages=stages,
            dinkelbach_max_iterations=config.dinkelbach_max_iterations,
            seed=seed,
        )
        if not solution.multiplicities:
            raise RuntimeError(f"feedback 主问题未得到可行解: {solution.status}")
        flights = flight_order(
            _realize(
                master,
                solution,
                groups_by_id,
                distances,
                refuel_keep=config.refuel_keep,
            )
        )
        metrics = aggregate(flights, groups_by_id, distances)
        last = (master, pool, solution, flights, metrics)
        feedback = to_columns(flights, groups_by_id, distances)
        known = {_physical_signature(column) for column in working}
        new_columns = [
            column for column in feedback if _physical_signature(column) not in known
        ]
        if _metrics_match(solution, metrics) and not new_columns:
            return FeedbackResult(
                master, working, pool, solution, flights, metrics,
                round_number + 1, fed, True,
            )
        if round_number == config.max_feedback_rounds:
            break
        fed += len(new_columns)
        working = number_columns([*working, *feedback])
        incumbent = flights
        incumbent_metrics = metrics

    master, pool, solution, flights, metrics = last
    return FeedbackResult(
        master,
        working,
        pool,
        solution,
        flights,
        metrics,
        config.max_feedback_rounds + 1,
        fed,
        _metrics_match(solution, metrics),
    )


def _warm_start(
    master: FlowMaster, flights: list[Flight], groups_by_id: dict
) -> FlowSolution | None:
    """把架次集合折回 (y, z)，用作下一轮主问题的启动提示。"""
    by_physical = {
        (
            column.base_airport,
            column.aircraft_type,
            column.route,
            column.refuel_decisions,
        ): column.column_id
        for column in master.columns
    }
    by_service: dict[tuple[str, str, tuple[str, ...]], str] = {}
    for column in master.columns:
        by_service.setdefault(
            (column.base_airport, column.aircraft_type, column.cluster), column.column_id
        )
    multiplicities: dict[str, int] = {}
    flows: dict[tuple[str, str], int] = {}
    for flight in flights:
        facilities = tuple(
            sorted({groups_by_id[group_id].destination_id for group_id, _ in flight.load})
        )
        stops = tuple(sorted(dict.fromkeys(flight.route[1:-1])))
        column_id = by_physical.get(
            (
                flight.base_airport,
                flight.aircraft_type,
                flight.route,
                flight.refuel_decisions,
            )
        ) or by_service.get(
            (flight.base_airport, flight.aircraft_type, stops)
        ) or by_service.get((flight.base_airport, flight.aircraft_type, facilities))
        if column_id is None:
            return None
        multiplicities[column_id] = multiplicities.get(column_id, 0) + 1
        for group_id, quantity in flight.load:
            key = (group_id, column_id)
            flows[key] = flows.get(key, 0) + quantity
    aircraft_time = sum(
        master.columns[master.column_index[column_id]].aircraft_time * count
        for column_id, count in multiplicities.items()
    )
    return FlowSolution(
        "WARM", (), multiplicities, flows, aircraft_time, 0, 0.0,
        sum(multiplicities.values()), 0.0, 0.0, 0.0,
    )


def _incumbent_ids(columns: list[RouteColumn], flights: list[Flight]) -> list[str]:
    """当前解用到的列必须固定保留，避免筛选阶段把它们剪掉。"""
    index = {
        (
            column.base_airport,
            column.aircraft_type,
            column.route,
            column.refuel_decisions,
        ): column.column_id
        for column in columns
    }
    ids = []
    for flight in flights:
        key = (
            flight.base_airport,
            flight.aircraft_type,
            flight.route,
            flight.refuel_decisions,
        )
        if key in index:
            ids.append(index[key])
    return ids


def _build_master(
    groups, columns: list[RouteColumn], config: Q1AlgorithmConfig, pinned=()
) -> tuple[FlowMaster, list[RouteColumn], float]:
    pool = select_columns(
        columns,
        groups,
        efficiency_slack=config.efficiency_slack,
        per_group=config.columns_per_group,
        pinned=pinned,
    )
    master = FlowMaster(groups, pool)
    bound = master.linear_relaxation_bound() or 0.0
    master.lower_bounds["aircraft_time"] = math.ceil(bound - 1e-6)
    return master, pool, bound


def main() -> int:
    args = parse_args()
    config = _config(args)
    started = time.perf_counter()
    data_dir = resolve_data_dir(args.data_dir)
    output_dir = (args.output_dir or Q1_OUTPUT_DIR).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    print("[1] 读取数据并聚合请求组")
    distance_data = load_distances(data_dir=data_dir)
    distances = distance_data.distances
    people = load_people_q1(data_dir=data_dir)
    groups = group_q1(people)
    if len(people) != 1600 or len(groups) != 104:
        raise RuntimeError(f"数据规模异常: persons={len(people)}, groups={len(groups)}")
    groups_by_id = {group.group_id: group for group in groups}
    facilities = sorted({group.destination_id for group in groups})

    print("[2] 枚举候选簇")
    clusters = enumerate_clusters(facilities, distances, config.neighbourhood)
    print(f"    候选簇 {len(clusters)} 个")

    print("[3] 受限加油候选集内精确 DP 求最短用时航线")
    route_cache: dict = {}
    columns = number_columns(
        build_columns(
            clusters,
            distances,
            refuel_keep=config.refuel_keep,
            cache=route_cache,
        )
    )
    print(f"    候选航线列 {len(columns)} 条")

    print("[4] 候选池筛选")
    master, pool, lp_bound = _build_master(groups, columns, config)
    print(f"    入池 {len(pool)} 条，z 变量 {len(master.pairs)} 个，LP 下界 {lp_bound:.1f}")

    print("[5] 贪心初始解 + 主目标求解")
    warm = greedy_solution(master)
    print(f"    贪心 T_air={warm.aircraft_time} 架次={warm.flights}")
    history: list[dict] = []
    solution = master.solve(
        time_limit_seconds=config.primary_time_limit_seconds,
        workers=args.workers,
        warm_start=warm,
        stages=("aircraft_time",),
        seed=config.seed,
    )
    if not solution.multiplicities:
        raise RuntimeError(f"主问题未得到可行解: {solution.status}")
    flights = _realize(
        master, solution, groups_by_id, distances, refuel_keep=config.refuel_keep
    )
    best_metrics = aggregate(flights, groups_by_id, distances)
    best_flights = flight_order(flights)
    history.append(
        _metrics_row(
            "primary",
            best_metrics,
            {
                "pool": len(pool),
                "lp_bound": lp_bound,
                "cp_sat_bound": solution.stages[0].best_bound,
                "cp_sat_objective": solution.aircraft_time,
                "status": solution.status,
                "seconds": solution.wall_time,
            },
        )
    )
    print(f"    T_air={best_metrics.total_aircraft_time} 架次={best_metrics.number_of_flights}")

    print("[6] 解引导的大邻域扩池")
    known = set(clusters)
    for round_number in range(1, config.lns_rounds + 1):
        realized = [
            tuple(sorted(dict.fromkeys(flight.route[1:-1]))) for flight in best_flights
        ]
        fresh = [
            cluster
            for cluster in expand_clusters(
                realized, distances, facilities, swap_width=config.lns_swap_width
            )
            if cluster not in known
        ]
        known.update(fresh)
        columns = number_columns(
            columns
            + build_columns(
                fresh,
                distances,
                refuel_keep=config.refuel_keep,
                cache=route_cache,
            )
            + to_columns(best_flights, groups_by_id, distances)
        )
        master, pool, lp_bound = _build_master(
            groups, columns, config, pinned=_incumbent_ids(columns, best_flights)
        )
        master.upper_bounds_by_metric["aircraft_time"] = best_metrics.total_aircraft_time
        hint = _warm_start(master, best_flights, groups_by_id)
        solution = master.solve(
            time_limit_seconds=config.lns_time_limit_seconds,
            workers=args.workers,
            warm_start=hint,
            stages=("aircraft_time",),
            seed=config.seed,
        )
        if not solution.multiplicities:
            print(f"    第{round_number}轮未得到可行解，跳过")
            continue
        candidate = _realize(
            master, solution, groups_by_id, distances, refuel_keep=config.refuel_keep
        )
        metrics = aggregate(candidate, groups_by_id, distances)
        history.append(
            _metrics_row(
                f"lns-{round_number}",
                metrics,
                {
                    "pool": len(pool),
                    "lp_bound": lp_bound,
                    "cp_sat_bound": solution.stages[0].best_bound,
                    "cp_sat_objective": solution.aircraft_time,
                    "status": solution.status,
                    "seconds": solution.wall_time,
                },
            )
        )
        print(
            f"    第{round_number}轮 新增簇 {len(fresh)} 列池 {len(pool)} "
            f"T_air={metrics.total_aircraft_time}"
        )
        if metrics.total_aircraft_time < best_metrics.total_aircraft_time:
            best_metrics, best_flights = metrics, flight_order(candidate)

    print("[7] 固定主目标后的词典序次级优化")
    # 把已实现的最好架次折回候选列并固定保留，使主目标上界一定可达，
    # 从而保证次级目标是在"不劣化主目标"的前提下优化的。
    feedback = solve_realize_feedback(
        groups,
        columns + to_columns(best_flights, groups_by_id, distances),
        groups_by_id,
        distances,
        config,
        workers=args.workers,
        incumbent_flights=best_flights,
        seed=config.seed,
    )
    master, pool, columns = feedback.master, feedback.pool, feedback.columns
    lexicographic = feedback.solution
    if lexicographic.multiplicities:
        candidate, metrics = feedback.flights, feedback.metrics
        history.append(
            _metrics_row(
                "lexicographic",
                metrics,
                {
                    "pool": len(pool),
                    "lp_bound": lp_bound,
                    "cp_sat_bound": lexicographic.stages[0].best_bound,
                    "cp_sat_objective": lexicographic.aircraft_time,
                    "status": lexicographic.status,
                    "seconds": lexicographic.wall_time,
                },
            )
        )
        if _lex_key(metrics) < _lex_key(best_metrics):
            best_metrics, best_flights = metrics, candidate

    print("[8] 人员回填与正式 CSV 输出")
    assignments = assign_people(best_flights, groups)
    if len(assignments) != 1600:
        raise RuntimeError(f"人员回填行数不是 1600: {len(assignments)}")
    routes_path, assignments_path = write_flight_csv(
        output_dir=output_dir, people=people, flights=best_flights, assignments=assignments
    )
    write_flight_plan(output_dir / "q1-flight-plan.csv", best_flights, groups_by_id)
    pd.DataFrame(history).to_csv(output_dir / "q1-history.csv", index=False)

    print("[9] 独立检查器复核")
    report = validate_q1_csv(routes_path, assignments_path, people, distances)
    if not report.passed:
        raise RuntimeError(str(report))
    checked = report.metrics
    if (checked.total_aircraft_time, checked.total_passenger_time) != (
        best_metrics.total_aircraft_time,
        best_metrics.total_passenger_time,
    ):
        raise RuntimeError("独立检查器重算指标与内部指标不一致")
    delivery_matches_solver = _metrics_match(lexicographic, checked)

    summary = {
        "persons": len(people),
        "groups": len(groups),
        "candidate_clusters": len(clusters),
        "candidate_columns": len(columns),
        "pool_columns": len(pool),
        "flow_variables": len(master.pairs),
        "T_air": checked.total_aircraft_time,
        "T_pax": checked.total_passenger_time,
        "fuel": checked.total_fuel,
        "flights": checked.number_of_flights,
        "PK": checked.passenger_km,
        "AK": checked.available_seat_km,
        "seat_utilization": checked.seat_utilization,
        "greedy_T_air": warm.aircraft_time,
        "lp_lower_bound": lp_bound,
        "optimality_gap_vs_pool_lp": (
            checked.total_aircraft_time - lp_bound
        ) / checked.total_aircraft_time,
        "flight_lower_bound": math.ceil(len(people) / 19),
        "solver_metrics": {
            "T_air": lexicographic.aircraft_time,
            "T_pax": lexicographic.passenger_time,
            "fuel": lexicographic.fuel,
            "flights": lexicographic.flights,
            "PK": lexicographic.passenger_km,
            "AK": lexicographic.available_seat_km,
        },
        "delivery_metrics": _metrics_row("delivery", checked, {}),
        "feedback_rounds": feedback.rounds,
        "columns_fed_back": feedback.columns_fed_back,
        "solver_metrics_equal_delivery": delivery_matches_solver,
        "stages": [asdict(stage) for stage in lexicographic.stages],
        "full_lexicographic_certified": (
            delivery_matches_solver
            and all(stage.certified_optimal for stage in lexicographic.stages)
            and len(lexicographic.stages) == len(_LEX_STAGES)
        ),
        "delivery_solution_certified": (
            delivery_matches_solver
            and all(stage.certified_optimal for stage in lexicographic.stages)
            and len(lexicographic.stages) == len(_LEX_STAGES)
        ),
        "history": history,
        "validator": {"independent_csv": str(report)},
        "certified_scope": "restricted-pool",
        "global_optimum": False,
        "run_mode": "quick" if args.quick else "formal",
        "seed": config.seed,
        "workers": args.workers,
        "wall_time_total": time.perf_counter() - started,
    }
    write_summary(output_dir / "q1-summary.json", summary)
    print(
        f"Q1 PASS 人员={len(assignments)} 架次={checked.number_of_flights} "
        f"T_air={checked.total_aircraft_time} T_pax={checked.total_passenger_time} "
        f"油耗={checked.total_fuel:.1f} 利用率={checked.seat_utilization:.4f} "
        f"LP下界={lp_bound:.1f}"
    )
    return 0


def _lex_key(metrics: SolutionMetrics):
    return (
        metrics.total_aircraft_time,
        metrics.total_passenger_time,
        metrics.total_fuel,
        metrics.number_of_flights,
        -metrics.seat_utilization,
    )


if __name__ == "__main__":
    raise SystemExit(main())
