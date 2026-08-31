"""每个候选簇的最短用时航线：受限加油候选集内的精确搜索。

给定起降机场 base、机型 spec 和一个待服务海上设施集合 S（|S| ≤ 5），本模块
返回"总飞机使用时间"最小的合法航线：

- 航线形如 base -> (海上停靠序列) -> base，海上着陆总数 ≤ 5；
- 每次海上停靠计 10 min，加油停靠再加 10 min，加油后油箱加满；
- 到达任一地点（含返场）时剩余油量不得低于机型最低安全余油量；
- 允许在任意位置（含最后一次投放之后的返场航段上）插入加油停靠。

算法 = "访问顺序枚举 + 顺序内加油插入标号法"：
1. 枚举 S 的全排列 π，`raw_time(π)` = 不加油时的用时，它是"按 π 顺序访问"
   的所有合法航线用时的下界；按 raw_time 升序处理并剪枝；
2. 对固定顺序 π，用 Dijkstra 式标号法（状态 = (当前位置, 已投放数, 已用额外
   加油停靠数)，标号 = (已用时, 剩余油量)，按 (时间↑, 油量↓) 做 Pareto 支配）
   在给定加油候选子集内精确求出该顺序下的最短用时航线。
"""

from __future__ import annotations

import heapq
import math
from dataclasses import dataclass
from itertools import permutations
from typing import Iterable, Mapping, Optional, Sequence

from common.config import (
    MAX_OFFSHORE_LANDINGS,
    REFUEL_EXTRA_MINUTES,
    REFUEL_FACILITIES,
    STOP_DURATION_MINUTES,
)
from common.models import AircraftSpec

DistanceMap = Mapping[tuple[str, str], float]

# 一次加油停靠至少额外增加 STOP + REFUEL_EXTRA 分钟；用作排列剪枝的安全下界。
_REFUEL_STOP_PENALTY = STOP_DURATION_MINUTES + REFUEL_EXTRA_MINUTES
_EPS = 1e-9


@dataclass(frozen=True)
class RoutePlan:
    """一条完整合法航线及其派生指标。"""

    base_airport: str
    aircraft_type: str
    route: tuple[str, ...]
    refuel_decisions: tuple[bool, ...]
    aircraft_time: int
    total_distance: float
    arrival_minutes: tuple[int, ...]
    cumulative_distance: tuple[float, ...]

    @property
    def offshore_landings(self) -> int:
        return len(self.route) - 2


def leg_minutes(distance: float, speed_kmh: int) -> int:
    """K-1：单航段飞行时间向上取整到整分钟。"""
    return math.ceil(60 * distance / speed_kmh)


def _finalize(
    base: str,
    spec: AircraftSpec,
    stops: Sequence[str],
    refuels: Sequence[bool],
    distances: DistanceMap,
) -> RoutePlan:
    """由停靠序列重建完整航线指标（不做可行性判断，调用方负责）。"""
    route = (base, *stops, base)
    decisions = (False, *refuels, False)
    arrival = [0]
    cumulative = [0.0]
    elapsed = 0
    travelled = 0.0
    for index, (origin, destination) in enumerate(zip(route, route[1:])):
        distance = distances[(origin, destination)]
        elapsed += leg_minutes(distance, spec.speed_kmh)
        travelled += distance
        arrival.append(elapsed)
        cumulative.append(travelled)
        stop_index = index + 1
        if stop_index < len(route) - 1:
            elapsed += STOP_DURATION_MINUTES
            if decisions[stop_index]:
                elapsed += REFUEL_EXTRA_MINUTES
    return RoutePlan(
        base_airport=base,
        aircraft_type=spec.aircraft_type,
        route=route,
        refuel_decisions=decisions,
        aircraft_time=elapsed,
        total_distance=travelled,
        arrival_minutes=tuple(arrival),
        cumulative_distance=tuple(cumulative),
    )


def _order_lower_bound(
    base: str, spec: AircraftSpec, order: Sequence[str], distances: DistanceMap
) -> tuple[int, float, bool]:
    """返回 (不加油用时, 总距离, 不加油是否满足油量约束)。"""
    route = (base, *order, base)
    elapsed = STOP_DURATION_MINUTES * len(order)
    travelled = 0.0
    fuel = spec.tank_capacity_kg
    feasible = True
    for origin, destination in zip(route, route[1:]):
        distance = distances[(origin, destination)]
        elapsed += leg_minutes(distance, spec.speed_kmh)
        travelled += distance
        fuel -= spec.fuel_consumption_kg_per_km * distance
        if fuel < spec.reserve_fuel_kg - _EPS:
            feasible = False
    return elapsed, travelled, feasible


def _plan_for_order(
    base: str,
    spec: AircraftSpec,
    order: tuple[str, ...],
    distances: DistanceMap,
    refuel_pool: tuple[str, ...],
    upper_bound: Optional[int],
) -> Optional[RoutePlan]:
    """固定投放顺序下，精确求最短用时航线（Dijkstra 标号法）。"""
    required = len(order)
    max_extra = MAX_OFFSHORE_LANDINGS - required
    if max_extra < 0:
        return None
    consumption = spec.fuel_consumption_kg_per_km
    reserve = spec.reserve_fuel_kg
    tank = spec.tank_capacity_kg

    # 标号：(已用时, 当前位置, 已投放数, 已用额外加油停靠数, 剩余油量, 停靠轨迹)
    start = (0, base, 0, 0, tank, ())
    queue: list[tuple] = [start]
    best_fuel: dict[tuple[str, int, int], float] = {}
    best: Optional[RoutePlan] = None
    limit = upper_bound

    while queue:
        elapsed, location, delivered, extra, fuel, trace = heapq.heappop(queue)
        if limit is not None and elapsed >= limit:
            break
        key = (location, delivered, extra)
        if fuel <= best_fuel.get(key, -1.0) + _EPS:
            continue
        best_fuel[key] = fuel

        if delivered == required:
            distance = distances[(location, base)]
            if fuel - consumption * distance >= reserve - _EPS:
                # 能直飞返场时，任何绕经加油站的返场都严格更慢，无需继续扩展。
                total = elapsed + leg_minutes(distance, spec.speed_kmh)
                if limit is None or total < limit:
                    stops = tuple(item[0] for item in trace)
                    refuels = tuple(item[1] for item in trace)
                    best = _finalize(base, spec, stops, refuels, distances)
                    limit = total
                continue

        if delivered < required:
            destination = order[delivered]
            distance = distances[(location, destination)]
            remaining = fuel - consumption * distance
            if remaining >= reserve - _EPS:
                arrival = elapsed + leg_minutes(distance, spec.speed_kmh) + STOP_DURATION_MINUTES
                heapq.heappush(
                    queue,
                    (
                        arrival,
                        destination,
                        delivered + 1,
                        extra,
                        remaining,
                        (*trace, (destination, False)),
                    ),
                )
                if destination in REFUEL_FACILITIES:
                    heapq.heappush(
                        queue,
                        (
                            arrival + REFUEL_EXTRA_MINUTES,
                            destination,
                            delivered + 1,
                            extra,
                            tank,
                            (*trace, (destination, True)),
                        ),
                    )

        if extra < max_extra:
            for station in refuel_pool:
                if station == location:
                    continue
                distance = distances[(location, station)]
                if fuel - consumption * distance < reserve - _EPS:
                    continue
                heapq.heappush(
                    queue,
                    (
                        elapsed + leg_minutes(distance, spec.speed_kmh) + _REFUEL_STOP_PENALTY,
                        station,
                        delivered,
                        extra + 1,
                        tank,
                        (*trace, (station, True)),
                    ),
                )
    return best


def refuel_candidates(
    base: str, facilities: Iterable[str], distances: DistanceMap, keep: int
) -> tuple[str, ...]:
    """只保留与本次任务地理相关的加油站，缩小标号法的状态空间。"""
    anchors = (base, *facilities)
    ranked = sorted(
        REFUEL_FACILITIES,
        key=lambda station: (
            min(distances[(anchor, station)] for anchor in anchors),
            station,
        ),
    )
    return tuple(ranked[:keep])


def best_route(
    base: str,
    spec: AircraftSpec,
    facilities: Sequence[str],
    distances: DistanceMap,
    *,
    refuel_keep: int = 4,
    weights: Optional[Mapping[str, int]] = None,
) -> Optional[RoutePlan]:
    """返回给定加油候选子集内服务 facilities 的最短用时航线。

    在用时相同的航线中按 `weights` 加权的到达时刻之和择优（默认权重为 1），
    这样次级目标"人员总在途时间"在不牺牲主目标的前提下自动取优。
    """
    unique = tuple(dict.fromkeys(facilities))
    if not unique or len(unique) > MAX_OFFSHORE_LANDINGS:
        return None
    stations = refuel_candidates(base, unique, distances, refuel_keep)

    orders = []
    for order in permutations(unique):
        raw_time, _, feasible = _order_lower_bound(base, spec, order, distances)
        orders.append((raw_time, feasible, order))
    orders.sort(key=lambda item: (item[0], item[2]))

    best: Optional[RoutePlan] = None
    for raw_time, feasible, order in orders:
        if best is not None and raw_time > best.aircraft_time:
            break
        if feasible:
            candidate = _finalize(base, spec, order, (False,) * len(order), distances)
        else:
            bound = None if best is None else best.aircraft_time
            if bound is not None and raw_time + _REFUEL_STOP_PENALTY >= bound:
                continue
            candidate = _plan_for_order(base, spec, order, distances, stations, bound)
        if candidate is None:
            continue
        if best is None or plan_key(candidate, weights) < plan_key(best, weights):
            best = candidate
    return best


def plan_key(
    plan: RoutePlan, weights: Optional[Mapping[str, int]] = None
) -> tuple[int, int, float, tuple[str, ...]]:
    if weights is None:
        weighted = sum(plan.arrival_minutes[1:-1])
    else:
        # 人员在其目的地的"首次"停靠下机，因此只按首次出现位置计到达时刻。
        weighted = sum(
            weight * plan.arrival_minutes[plan.route.index(facility)]
            for facility, weight in weights.items()
            if facility in plan.route
        )
    return (plan.aircraft_time, weighted, plan.total_distance, plan.route)
