"""贪心构造初始可行解，用作主问题的启动提示（hint）。

规则：每次选取"单位运送人数用时" T_r / min(cap_r, 该列可服务的剩余需求) 最小的
航线执行一次，把剩余需求最大的请求组优先装满，直到全部需求被覆盖。
"""

from __future__ import annotations

from typing import Mapping

from q1.algorithms.flow_master import FlowMaster, FlowSolution


def greedy_solution(master: FlowMaster) -> FlowSolution:
    remaining = {index: group.quantity for index, group in enumerate(master.groups)}
    multiplicities: dict[str, int] = {}
    flows: dict[tuple[str, str], int] = {}
    outstanding = sum(remaining.values())

    while outstanding > 0:
        best_score = None
        best_column = -1
        for column_position, column in enumerate(master.columns):
            available = 0
            for pair in master.pairs_by_column[column_position]:
                available += remaining[master.pairs[pair][0]]
                if available >= column.capacity:
                    break
            served = min(column.capacity, available)
            if served <= 0:
                continue
            score = column.aircraft_time / served
            if best_score is None or score < best_score:
                best_score = score
                best_column = column_position
        if best_column < 0:
            raise RuntimeError("贪心构造无法覆盖剩余需求，候选池不足")

        column = master.columns[best_column]
        multiplicities[column.column_id] = multiplicities.get(column.column_id, 0) + 1
        room = column.capacity
        pairs = sorted(
            master.pairs_by_column[best_column],
            key=lambda pair: (-remaining[master.pairs[pair][0]], pair),
        )
        for pair in pairs:
            group_position = master.pairs[pair][0]
            take = min(remaining[group_position], room)
            if take <= 0:
                continue
            key = (master.groups[group_position].group_id, column.column_id)
            flows[key] = flows.get(key, 0) + take
            remaining[group_position] -= take
            room -= take
            outstanding -= take
            if room == 0:
                break
    return _as_solution(master, multiplicities, flows)


def _as_solution(
    master: FlowMaster,
    multiplicities: Mapping[str, int],
    flows: Mapping[tuple[str, str], int],
) -> FlowSolution:
    aircraft_time = sum(
        master.columns[master.column_index[column_id]].aircraft_time * count
        for column_id, count in multiplicities.items()
    )
    return FlowSolution(
        status="GREEDY",
        stages=(),
        multiplicities=dict(multiplicities),
        flows=dict(flows),
        aircraft_time=aircraft_time,
        passenger_time=0,
        fuel=0.0,
        flights=sum(multiplicities.values()),
        passenger_km=0.0,
        available_seat_km=0.0,
        wall_time=0.0,
    )
