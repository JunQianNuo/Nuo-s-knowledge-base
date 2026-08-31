"""Q1 小实例交叉验证：架次—人员流模型 vs. 显式人员配置的集合划分模型。

M1 模型文档要求"用小实例枚举或紧凑 MILP 核对 (Q1-3)—(Q1-12)"。本脚本在真实
距离矩阵上取一个小规模切片，用两套**互相独立的形式化**求同一个主目标：

A. 架次—人员流模型（正式流水线所用）：每条候选航线只出现一次，人员分配由
   z 变量决策；
B. 集合划分模型（对照）：把"航线 × 每一种合法人员配置"全部显式展开成列，
   用 Σ_r a_{gr} x_r = q_g 的整数规划求解。

两者的可行域在数学上等价，因此最优 T_air 必须一致；若不一致即说明实现有误。
"""

from __future__ import annotations

import argparse
import itertools
import time

from ortools.sat.python import cp_model

from common.config import AIRPORTS
from common.data_loader import load_distances
from common.models import RequestGroup
from q1.algorithms.clusters import build_columns, number_columns
from q1.algorithms.flight_builder import aggregate, improve_flights, split_flows
from q1.algorithms.flow_master import FlowMaster
from q1.config import Q1AlgorithmConfig

TOY_FACILITIES = ("F009", "F017", "F030")
TOY_DEMANDS = {"F009": 7, "F017": 5, "F030": 9}


def toy_groups() -> list[RequestGroup]:
    groups = []
    counter = 0
    for index, facility in enumerate(TOY_FACILITIES, start=1):
        quantity = TOY_DEMANDS[facility]
        person_ids = tuple(f"P{counter + offset:04d}" for offset in range(quantity))
        counter += quantity
        groups.append(RequestGroup(f"T{index:02d}", person_ids, "LAND", facility))
    return groups


def set_partitioning_optimum(groups, columns, time_limit: float = 60.0) -> int:
    """对照模型：显式枚举每条航线上的全部合法人员配置，求最优 T_air。"""
    quantities = {group.group_id: group.quantity for group in groups}
    destination = {group.group_id: group.destination_id for group in groups}
    patterns: list[tuple[int, dict[str, int]]] = []
    for column in columns:
        servable = [
            group_id
            for group_id in quantities
            if destination[group_id] in column.cluster
        ]
        ranges = [range(quantities[group_id] + 1) for group_id in servable]
        for combination in itertools.product(*ranges):
            total = sum(combination)
            if not 0 < total <= column.capacity:
                continue
            patterns.append(
                (
                    column.aircraft_time,
                    {
                        group_id: value
                        for group_id, value in zip(servable, combination)
                        if value
                    },
                )
            )
    model = cp_model.CpModel()
    variables = [model.new_int_var(0, sum(quantities.values()), "") for _ in patterns]
    for group_id, quantity in quantities.items():
        model.add(
            sum(
                pattern.get(group_id, 0) * variable
                for (_, pattern), variable in zip(patterns, variables)
                if pattern.get(group_id, 0)
            )
            == quantity
        )
    model.minimize(
        sum(cost * variable for (cost, _), variable in zip(patterns, variables))
    )
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    status = solver.solve(model)
    if solver.status_name(status) != "OPTIMAL":
        raise RuntimeError(f"对照集合划分模型未证明最优: {solver.status_name(status)}")
    print(f"    对照模型列数 {len(patterns)}")
    return int(solver.objective_value)


def main() -> int:
    parser = argparse.ArgumentParser(description="Q1 小实例双模型交叉验证")
    parser.add_argument("--time-limit", type=float, default=60.0)
    args = parser.parse_args()
    config = Q1AlgorithmConfig()

    distances = load_distances().distances
    groups = toy_groups()
    groups_by_id = {group.group_id: group for group in groups}
    print(f"[1] 小实例：{len(groups)} 个请求组，共 {sum(TOY_DEMANDS.values())} 人")

    clusters = [
        tuple(sorted(subset))
        for size in range(1, len(TOY_FACILITIES) + 1)
        for subset in itertools.combinations(TOY_FACILITIES, size)
    ]
    columns = number_columns(
        build_columns(
            clusters,
            distances,
            bases=tuple(sorted(AIRPORTS)),
            refuel_keep=config.refuel_keep,
        )
    )
    print(
        f"[2] 候选航线列 {len(columns)} 条"
        f"（{len(clusters)} 个簇 × 机场 × 机型，机型 Pareto 剪枝后）"
    )

    started = time.perf_counter()
    master = FlowMaster(groups, columns)
    solution = master.solve(
        time_limit_seconds=args.time_limit, stages=("aircraft_time",), workers=1
    )
    flow_time = solution.aircraft_time
    print(
        f"[3] 架次—人员流模型 T_air={flow_time} 状态={solution.status} "
        f"({time.perf_counter() - started:.2f}s)"
    )

    started = time.perf_counter()
    reference = set_partitioning_optimum(groups, columns, args.time_limit)
    print(f"[4] 集合划分对照模型 T_air={reference} ({time.perf_counter() - started:.2f}s)")

    if flow_time != reference:
        raise RuntimeError(f"两套模型不一致: 流模型 {flow_time} vs 集合划分 {reference}")

    index = {column.column_id: column for column in master.columns}
    flights = split_flows(index, solution.multiplicities, solution.flows, groups_by_id)
    metrics = aggregate(
        improve_flights(
            flights, groups_by_id, distances, refuel_keep=config.refuel_keep
        ),
        groups_by_id,
        distances,
    )
    print(f"[5] 落地架次 {metrics.number_of_flights} 个，实际 T_air={metrics.total_aircraft_time}")
    if metrics.total_aircraft_time > flow_time:
        raise RuntimeError("拆分/改进后主目标劣化")
    print("Q1 toy 交叉验证：PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
