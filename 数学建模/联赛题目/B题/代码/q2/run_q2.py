from __future__ import annotations

import argparse
import math
import time
from pathlib import Path

import pandas as pd

from common.data_loader import load_distances, load_people_q2
from common.grouping import group_q2
from common.paths import CODE_ROOT, resolve_data_dir
from q2.algorithms.master import RouteFlowMaster
from q2.algorithms.realize import realize_solution
from q2.algorithms.route_pool import build_route_pool
from q2.config import Q2Config
from q2.io.csv_validator import validate_q2_csv
from q2.io.csv_writer import write_json, write_q2_csv


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Q2 physical-route + passenger-flow solver")
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--seed", type=int, default=20260815)
    parser.add_argument("--time-budget", type=float)
    return parser.parse_args(argv)


def _counts(people):
    outbound = int(people["origin_id"].isin(["LAND", "A01", "A02", "A03"]).sum())
    returns = int(people["destination_id"].isin(["LAND", "A01", "A02", "A03"]).sum())
    shuttle = len(people) - outbound - returns
    return outbound, returns, shuttle


def _metric_dict(metrics):
    return {
        "T_air": metrics.total_aircraft_time,
        "T_pax": metrics.total_passenger_time,
        "fuel": metrics.total_fuel,
        "flights": metrics.number_of_flights,
        "PK": metrics.passenger_km,
        "AK": metrics.available_seat_km,
        "utilization": metrics.seat_utilization,
    }


def _separated_baseline(groups, routes, options):
    routes_by_id = {route.route_id: route for route in routes}
    by_group = {group.group_id: [] for group in groups}
    for option in options:
        by_group[option.group_id].append(option)
    total_air = total_pax = flights = 0
    fuel = passenger_km = available_seat_km = 0.0
    for group in groups:
        candidates = []
        for option in by_group[group.group_id]:
            route = routes_by_id[option.route_id]
            copies = math.ceil(group.quantity / route.capacity)
            candidates.append(
                (
                    copies * route.aircraft_time,
                    group.quantity * option.passenger_time,
                    copies * route.fuel_used,
                    copies,
                    -group.quantity * option.passenger_km / (copies * route.available_seat_km),
                    option.option_id,
                    route,
                    option,
                )
            )
        if not candidates:
            raise RuntimeError(f"separated baseline 未覆盖请求组 {group.group_id}")
        _, _, _, copies, _, _, route, option = min(candidates)
        total_air += copies * route.aircraft_time
        total_pax += group.quantity * option.passenger_time
        fuel += copies * route.fuel_used
        flights += copies
        passenger_km += group.quantity * option.passenger_km
        available_seat_km += copies * route.available_seat_km
    return {
        "T_air": total_air,
        "T_pax": total_pax,
        "fuel": fuel,
        "flights": flights,
        "PK": passenger_km,
        "AK": available_seat_km,
        "utilization": passenger_km / available_seat_km,
        "method": "deterministic independent-OD transportation",
    }


def main(argv=None) -> int:
    args = parse_args(argv)
    config = Q2Config.build(
        quick=args.quick, seed=args.seed, time_budget=args.time_budget, workers=args.workers
    )
    started = time.perf_counter()
    deadline = started + config.time_budget
    data_dir = resolve_data_dir(args.data_dir)
    output_dir = (args.output_dir or CODE_ROOT / "q2" / "outputs").resolve()
    distances = load_distances(data_dir=data_dir).distances
    people = load_people_q2(data_dir=data_dir)
    groups = group_q2(people)
    outbound, returns, shuttle = _counts(people)
    if (len(people), len(groups), outbound, returns, shuttle) != (4000, 264, 1600, 1600, 800):
        raise RuntimeError(
            f"数据规模异常: persons={len(people)}, groups={len(groups)}, "
            f"types={(outbound, returns, shuttle)}"
        )
    print(
        f"[1] data persons={len(people)} groups={len(groups)} "
        f"outbound/return/shuttle={outbound}/{returns}/{shuttle}"
    )

    route_started = time.perf_counter()
    routes, options = build_route_pool(groups, distances, pair_limit=config.pair_limit)
    route_seconds = time.perf_counter() - route_started
    coverage = {group.group_id: 0 for group in groups}
    for option in options:
        coverage[option.group_id] += 1
    print(
        f"[2] physical routes={len(routes)} service options={len(options)} "
        f"min coverage={min(coverage.values())}"
    )

    master_started = time.perf_counter()
    master = RouteFlowMaster(groups, routes, options)
    stages = (
        ("aircraft_time",)
        if config.quick
        else ("aircraft_time", "passenger_time", "fuel", "flights", "seat_utilization")
    )
    solution = master.solve(
        deadline=deadline,
        workers=config.workers,
        stages=stages,
        seed=config.seed,
        primary_time_limit_seconds=config.primary_time_limit,
        secondary_time_limit_seconds=config.secondary_time_limit,
    )
    master_seconds = time.perf_counter() - master_started
    if not solution.multiplicities:
        raise RuntimeError(f"主问题未得到可行解: {solution.status}")
    flights, assignments = realize_solution(groups, routes, options, solution)
    routes_path, assignments_path = write_q2_csv(output_dir, people, flights, assignments)
    report = validate_q2_csv(
        routes_path=routes_path,
        assignments_path=assignments_path,
        people=people,
        distances=distances,
    )
    if not report.valid:
        raise RuntimeError("独立 CSV 验证失败:\n" + "\n".join(report.violations[:20]))
    delivered = report.metrics
    tolerance = 1e-6
    solver_matches = (
        delivered.total_aircraft_time == solution.aircraft_time
        and delivered.total_passenger_time == solution.passenger_time
        and math.isclose(delivered.total_fuel, solution.fuel, abs_tol=tolerance)
        and delivered.number_of_flights == solution.flights
        and math.isclose(delivered.passenger_km, solution.passenger_km, abs_tol=tolerance)
        and math.isclose(delivered.available_seat_km, solution.available_seat_km, abs_tol=tolerance)
    )
    if not solver_matches:
        raise RuntimeError("求解器指标与 CSV 独立重算不一致")

    # Each OD is transported independently, hence no joint pickup-delivery seat reuse.
    separated = _separated_baseline(groups, routes, options)
    joint = _metric_dict(delivered)
    summary = {
        "mode": "quick" if config.quick else "formal",
        "seed": config.seed,
        "workers": config.workers,
        "time_budget": config.time_budget,
        "primary_time_limit": config.primary_time_limit,
        "secondary_time_limit": config.secondary_time_limit,
        "candidate_pool_scope": "finite physical route pool",
        "claim": "pool-optimal"
        if solution.stages and solution.stages[0].certified_optimal
        else "best validated feasible solution",
        "data": {
            "persons": 4000,
            "groups": 264,
            "outbound": outbound,
            "return": returns,
            "shuttle": shuttle,
        },
        "model": {
            "physical_routes": len(routes),
            "service_options": len(options),
            "y_variables": len(routes),
            "z_variables": len(options),
            "dynamic_capacity_constraints": sum(len(route.route) - 1 for route in routes),
            "groups_covered": len(coverage),
            "min_routes_per_group": min(coverage.values()),
        },
        "baseline_separated": separated,
        "joint_solution": joint,
        "improvement": dict(
            {name: separated[name] - joint[name] for name in ("T_air", "T_pax", "fuel", "flights")},
            utilization=joint["utilization"] - separated["utilization"],
        ),
        "certification": {
            stage.name: {
                "status": stage.status,
                "certified_optimal": stage.certified_optimal,
                "conditioned_on_uncertified_parent": stage.conditioned_on_uncertified_parent,
                "bound": stage.best_bound,
            }
            for stage in solution.stages
        },
        "full_lexicographic_certified": solution.full_certified,
        "validation": {
            "missing": report.missing,
            "duplicates": report.duplicates,
            "extra": report.extra,
            "independent_csv": report.valid,
            "solver_equals_delivery": solver_matches,
        },
        "runtime": {
            "route_generation": route_seconds,
            "master": master_seconds,
            "total": time.perf_counter() - started,
        },
    }
    write_json(output_dir / "q2-summary.json", summary)
    pd.DataFrame(
        [
            {
                "stage": stage.name,
                "status": stage.status,
                "objective": stage.objective,
                "best_bound": stage.best_bound,
                "seconds": stage.wall_time,
                "certified": stage.certified_optimal,
            }
            for stage in solution.stages
        ]
    ).to_csv(output_dir / "q2-history.csv", index=False)
    print(
        f"[3] status={solution.status} T_air={joint['T_air']} "
        f"flights={joint['flights']} utilization={joint['utilization']:.6f}"
    )
    print(f"[4] independent validator PASS; total={summary['runtime']['total']:.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
