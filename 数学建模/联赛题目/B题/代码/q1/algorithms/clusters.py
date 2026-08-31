"""候选"簇"（一次架次要投放的海上设施集合）的枚举与航线列构造。

Q1 的所有人员都在机场上机、在其目的地首次停靠时下机，因此一条架次的物理成本
（用时、油耗、可用座公里）只取决于 (机场, 机型, 设施集合)，与"具体谁上这班"
无关。于是候选列不再是"路线×人员配置"的组合，而只是物理航线本身，人员配置
交由主问题精确决策（见 flow_master）。
"""

from __future__ import annotations

import time
from dataclasses import dataclass, replace
from itertools import combinations
from typing import Iterable, Mapping, Optional, Sequence

from common.config import AIRCRAFT_SPECS, AIRPORTS, LAND
from common.models import RequestGroup
from q1.algorithms.route_dp import RoutePlan, best_route

DistanceMap = Mapping[tuple[str, str], float]
Cluster = tuple[str, ...]


@dataclass(frozen=True)
class RouteColumn:
    """一条候选架次航线（物理列）。"""

    column_id: str
    base_airport: str
    aircraft_type: str
    capacity: int
    route: tuple[str, ...]
    refuel_decisions: tuple[bool, ...]
    aircraft_time: int
    total_distance: float
    fuel_used: float
    cluster: Cluster
    delivery_stop: dict[str, int]
    arrival_minutes: dict[str, int]
    cumulative_distance: dict[str, float]

    @property
    def available_seat_km(self) -> float:
        return self.capacity * self.total_distance


def column_from_plan(plan: RoutePlan, cluster: Cluster, column_id: str = "") -> RouteColumn:
    """由航线构造候选列。

    可服务设施取航线上"全部海上停靠"，而不只是生成时要求的设施集合：飞机既然
    已经在加油站着陆，就可以在那里免费投放人员。
    """
    spec = AIRCRAFT_SPECS[plan.aircraft_type]
    served = tuple(dict.fromkeys(plan.route[1:-1]))
    delivery = {facility: plan.route.index(facility) for facility in served}
    return RouteColumn(
        column_id=column_id,
        base_airport=plan.base_airport,
        aircraft_type=plan.aircraft_type,
        capacity=spec.capacity,
        route=plan.route,
        refuel_decisions=plan.refuel_decisions,
        aircraft_time=plan.aircraft_time,
        total_distance=plan.total_distance,
        fuel_used=spec.fuel_consumption_kg_per_km * plan.total_distance,
        cluster=tuple(sorted(served)),
        delivery_stop=delivery,
        arrival_minutes={f: plan.arrival_minutes[index] for f, index in delivery.items()},
        cumulative_distance={
            f: plan.cumulative_distance[index] for f, index in delivery.items()
        },
    )


def neighbour_table(
    facilities: Sequence[str], distances: DistanceMap, width: int
) -> dict[str, tuple[str, ...]]:
    return {
        facility: tuple(
            sorted(
                (other for other in facilities if other != facility),
                key=lambda other: (distances[(facility, other)], other),
            )[:width]
        )
        for facility in facilities
    }


def enumerate_clusters(
    facilities: Sequence[str],
    distances: DistanceMap,
    neighbourhood: Mapping[int, int],
) -> list[Cluster]:
    """按"种子设施 + 其近邻"枚举规模 1..5 的候选簇。

    `neighbourhood` 形如 {2: 12, 3: 8, 4: 6, 5: 6}，表示枚举规模 k 的簇时，
    只在种子设施的前 neighbourhood[k] 个最近邻中取剩下的 k-1 个成员。
    """
    tables = {
        size: neighbour_table(facilities, distances, width)
        for size, width in neighbourhood.items()
    }
    clusters: set[Cluster] = {(facility,) for facility in facilities}
    for size, width in sorted(neighbourhood.items()):
        if size < 2 or width < size - 1:
            continue
        table = tables[size]
        for seed in facilities:
            for extra in combinations(table[seed], size - 1):
                clusters.add(tuple(sorted((seed, *extra))))
    return sorted(clusters)


def expand_clusters(
    realized: Sequence[Cluster],
    distances: DistanceMap,
    facilities: Sequence[str],
    *,
    swap_width: int = 6,
    max_size: int = 5,
) -> list[Cluster]:
    """围绕当前解做大邻域扩池：子集、并集、单点替换与单点插入。

    这是"解引导的候选池扩张"，把当前解附近尚未枚举到的簇补进候选池，让下一轮
    主问题能在更大的可行域上重新优化。
    """
    table = neighbour_table(facilities, distances, swap_width)
    seen: set[Cluster] = set()
    unique = sorted({tuple(sorted(cluster)) for cluster in realized if cluster})

    for cluster in unique:
        for size in range(1, len(cluster)):
            for subset in combinations(cluster, size):
                seen.add(subset)
        for facility in cluster:
            for neighbour in table[facility]:
                if neighbour not in cluster:
                    swapped = tuple(sorted(set(cluster) - {facility} | {neighbour}))
                    seen.add(swapped)
                    if len(cluster) < max_size:
                        seen.add(tuple(sorted(set(cluster) | {neighbour})))
    for index, first in enumerate(unique):
        for second in unique[index + 1 :]:
            merged = set(first) | set(second)
            if len(merged) <= max_size:
                seen.add(tuple(sorted(merged)))
    return sorted(seen)


def servable_groups(
    column: RouteColumn, groups_by_destination: Mapping[str, Sequence[RequestGroup]]
) -> list[RequestGroup]:
    """列 r 能服务的请求组：目的地在簇内，且陆地端与本架次机场相容。"""
    result: list[RequestGroup] = []
    for facility in column.cluster:
        for group in groups_by_destination.get(facility, ()):
            if group.origin_id == LAND or group.origin_id == column.base_airport:
                result.append(group)
    return result


def build_columns(
    clusters: Iterable[Cluster],
    distances: DistanceMap,
    *,
    bases: Sequence[str] = tuple(sorted(AIRPORTS)),
    refuel_keep: int = 4,
    deadline: Optional[float] = None,
    cache: Optional[dict] = None,
) -> list[RouteColumn]:
    """为每个 (机场, 机型, 簇) 在受限加油候选集内求最短用时航线。"""
    store = cache if cache is not None else {}
    columns: list[RouteColumn] = []
    for cluster in clusters:
        if deadline is not None and time.perf_counter() >= deadline:
            break
        for base in bases:
            found: list[RouteColumn] = []
            for aircraft_type, spec in AIRCRAFT_SPECS.items():
                key = (base, aircraft_type, cluster, refuel_keep)
                if key in store:
                    plan = store[key]
                else:
                    plan = best_route(
                        base, spec, cluster, distances, refuel_keep=refuel_keep
                    )
                    store[key] = plan
                if plan is not None:
                    found.append(column_from_plan(plan, cluster))
            columns.extend(_pareto_filter(found))
    return columns


def _pareto_filter(columns: Sequence[RouteColumn]) -> list[RouteColumn]:
    """按完整词典序目标做安全机型支配剪枝。

    主目标严格更小且容量不小时，后续目标无论如何都不能挽回被支配列。
    主目标相等时，则必须逐层核对到达时间、油耗以及 Stage 5 的
    PK/AK 全部系数；容量更大或单列利用率本身不构成安全支配。
    """
    by_service: dict[tuple[str, Cluster], list[RouteColumn]] = {}
    for column in columns:
        by_service.setdefault((column.base_airport, column.cluster), []).append(column)
    kept: list[RouteColumn] = []
    for group in by_service.values():
        for column in group:
            dominated = any(_safely_dominates(other, column) for other in group)
            if not dominated:
                kept.append(column)
    return kept


def _safely_dominates(other: RouteColumn, column: RouteColumn) -> bool:
    if other is column or other.capacity < column.capacity:
        return False
    if other.aircraft_time < column.aircraft_time:
        return True
    if other.aircraft_time != column.aircraft_time:
        return False
    facilities = column.cluster
    arrivals_no_worse = all(
        other.arrival_minutes[facility] <= column.arrival_minutes[facility]
        for facility in facilities
    )
    if not arrivals_no_worse or other.fuel_used > column.fuel_used + 1e-9:
        return False
    earlier_layer_strict = (
        any(
            other.arrival_minutes[facility] < column.arrival_minutes[facility]
            for facility in facilities
        )
        or other.fuel_used < column.fuel_used - 1e-9
    )
    if earlier_layer_strict:
        return True
    # 前四级完全等价时，只有 Stage 5 的分子/分母系数也完全相同
    # 才能删除重复物理实现；否则宁可保留。
    stage5_equivalent = (
        abs(other.available_seat_km - column.available_seat_km) <= 1e-9
        and all(
            abs(
                other.cumulative_distance[facility]
                - column.cumulative_distance[facility]
            )
            <= 1e-9
            for facility in facilities
        )
    )
    if not stage5_equivalent:
        return False
    return (
        other.aircraft_type,
        other.route,
        other.refuel_decisions,
    ) < (
        column.aircraft_type,
        column.route,
        column.refuel_decisions,
    )


def select_columns(
    columns: Sequence[RouteColumn],
    groups: Sequence[RequestGroup],
    *,
    efficiency_slack: float,
    per_group: int,
    pinned: Sequence[str] = (),
) -> list[RouteColumn]:
    """按"单位座位用时"筛选候选列，并保证每个请求组的覆盖度。

    对设施 f，记 ρ_f = min{T_r / cap_r : f ∈ S_r} 为服务 f 的最好单位座位用时。
    一条列 r 若满足 T_r / cap_r ≤ (1 + slack) · max_{f∈S_r} ρ_f 则保留：它相对
    于自己所覆盖的最"贵"设施仍然是高效的。此外，对每个请求组无条件保留单位
    座位用时最小的 per_group 条列，避免机场专属组因效率低而被整体剪掉。
    """
    ratio = {column.column_id: column.aircraft_time / column.capacity for column in columns}
    best: dict[str, float] = {}
    for column in columns:
        for facility in column.cluster:
            best[facility] = min(best.get(facility, float("inf")), ratio[column.column_id])

    keep = {column_id for column_id in pinned}
    for column in columns:
        threshold = (1.0 + efficiency_slack) * max(best[f] for f in column.cluster)
        if ratio[column.column_id] <= threshold:
            keep.add(column.column_id)

    by_destination: dict[str, list[RequestGroup]] = {}
    for group in groups:
        by_destination.setdefault(group.destination_id, []).append(group)
    per_group_columns: dict[str, list[RouteColumn]] = {}
    for column in columns:
        for group in servable_groups(column, by_destination):
            per_group_columns.setdefault(group.group_id, []).append(column)
    for group_id, candidates in per_group_columns.items():
        for column in sorted(candidates, key=lambda item: (ratio[item.column_id], item.column_id))[
            :per_group
        ]:
            keep.add(column.column_id)
    return [column for column in columns if column.column_id in keep]


def number_columns(columns: Sequence[RouteColumn]) -> list[RouteColumn]:
    """只删除完全相同的物理列，保留同主目标的次级 trade-off。"""
    unique: dict[tuple[object, ...], RouteColumn] = {}
    for column in columns:
        key = (
            column.base_airport,
            column.aircraft_type,
            column.route,
            column.refuel_decisions,
        )
        unique.setdefault(key, column)
    return [
        replace(column, column_id=f"R{index:06d}")
        for index, column in enumerate(
            sorted(
                unique.values(),
                key=lambda item: (
                    item.cluster,
                    item.base_airport,
                    item.aircraft_type,
                    item.route,
                    item.refuel_decisions,
                ),
            ),
            start=1,
        )
    ]
