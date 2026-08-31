"""把主问题的 (y, z) 解落成具体架次，并做保证不劣化的局部改进。

主问题在"航线"层面聚合决策：一条航线 r 被执行 y_r 次，共承运 z_{g,r} 人。
本模块负责

1. **拆分**：把 z_{g,r} 拆到 y_r 个架次副本上（贪心装箱，尽量让单个副本只服务
   少数设施），拆分永远可行，因为 Σ_g z_{g,r} ≤ cap_r · y_r 且人员可互换；
2. **收缩**：某个副本实际只投放到簇的一个子集时，用精确 DP 重新求该子集的最短
   航线，并允许改用"能装下本副本载客数的更快机型/更近机场"；
3. **重排**：在不改变用时的前提下，按本副本的实际载客分布最小化在途时间。

第 2、3 步只在词典序意义上严格不劣化时才接受，因此结果始终优于或等于主问题解。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from common.config import AIRCRAFT_SPECS, AIRPORTS, LAND
from common.models import PersonAssignment, RequestGroup, SolutionMetrics
from q1.algorithms.clusters import RouteColumn
from q1.algorithms.route_dp import RoutePlan, best_route

DistanceMap = Mapping[tuple[str, str], float]


@dataclass(frozen=True)
class Flight:
    """一个具体架次副本。"""

    base_airport: str
    aircraft_type: str
    route: tuple[str, ...]
    refuel_decisions: tuple[bool, ...]
    load: tuple[tuple[str, int], ...]  # (group_id, 人数)

    @property
    def passengers(self) -> int:
        return sum(quantity for _, quantity in self.load)


@dataclass(frozen=True)
class FlightMetrics:
    aircraft_time: int
    passenger_time: int
    fuel_used: float
    passenger_km: float
    available_seat_km: float


def _plan_of(flight: Flight, distances: DistanceMap) -> RoutePlan:
    spec = AIRCRAFT_SPECS[flight.aircraft_type]
    arrival = [0]
    cumulative = [0.0]
    elapsed = 0
    travelled = 0.0
    from q1.algorithms.route_dp import leg_minutes

    for index, (origin, destination) in enumerate(zip(flight.route, flight.route[1:])):
        distance = distances[(origin, destination)]
        elapsed += leg_minutes(distance, spec.speed_kmh)
        travelled += distance
        arrival.append(elapsed)
        cumulative.append(travelled)
        stop = index + 1
        if stop < len(flight.route) - 1:
            elapsed += 10 + 10 * int(flight.refuel_decisions[stop])
    return RoutePlan(
        base_airport=flight.base_airport,
        aircraft_type=flight.aircraft_type,
        route=flight.route,
        refuel_decisions=flight.refuel_decisions,
        aircraft_time=elapsed,
        total_distance=travelled,
        arrival_minutes=tuple(arrival),
        cumulative_distance=tuple(cumulative),
    )


def flight_metrics(
    flight: Flight, groups: Mapping[str, RequestGroup], distances: DistanceMap
) -> FlightMetrics:
    plan = _plan_of(flight, distances)
    spec = AIRCRAFT_SPECS[flight.aircraft_type]
    passenger_time = 0
    passenger_km = 0.0
    for group_id, quantity in flight.load:
        stop = flight.route.index(groups[group_id].destination_id)
        passenger_time += quantity * plan.arrival_minutes[stop]
        passenger_km += quantity * plan.cumulative_distance[stop]
    return FlightMetrics(
        aircraft_time=plan.aircraft_time,
        passenger_time=passenger_time,
        fuel_used=spec.fuel_consumption_kg_per_km * plan.total_distance,
        passenger_km=passenger_km,
        available_seat_km=spec.capacity * plan.total_distance,
    )


def aggregate(
    flights: Sequence[Flight], groups: Mapping[str, RequestGroup], distances: DistanceMap
) -> SolutionMetrics:
    time_total = 0
    pax_total = 0
    fuel_total = 0.0
    pk_total = 0.0
    ak_total = 0.0
    for flight in flights:
        metrics = flight_metrics(flight, groups, distances)
        time_total += metrics.aircraft_time
        pax_total += metrics.passenger_time
        fuel_total += metrics.fuel_used
        pk_total += metrics.passenger_km
        ak_total += metrics.available_seat_km
    return SolutionMetrics(
        time_total,
        pax_total,
        fuel_total,
        len(flights),
        pk_total,
        ak_total,
        pk_total / ak_total if ak_total else 0.0,
    )


# --------------------------------------------------------------------- 拆分
def split_flows(
    columns: Mapping[str, RouteColumn],
    multiplicities: Mapping[str, int],
    flows: Mapping[tuple[str, str], int],
    groups: Mapping[str, RequestGroup],
) -> list[Flight]:
    """把每条航线的人员流拆成 y_r 个架次副本。

    贪心规则：每个副本先装当前剩余人数最多的请求组，只有当"不装够就放不下剩余
    副本"时才继续拼装第二个组，从而尽量让副本只服务一个设施。
    """
    by_column: dict[str, dict[str, int]] = {}
    for (group_id, column_id), quantity in flows.items():
        if quantity:
            by_column.setdefault(column_id, {})[group_id] = quantity

    flights: list[Flight] = []
    for column_id, count in sorted(multiplicities.items()):
        column = columns[column_id]
        remaining = dict(by_column.get(column_id, {}))
        total = sum(remaining.values())
        for index in range(count):
            bins_left = count - index - 1
            required = max(0, total - column.capacity * bins_left)
            room = column.capacity
            load: dict[str, int] = {}
            placed = 0
            for group_id in sorted(remaining, key=lambda key: (-remaining[key], key)):
                if placed >= required and placed > 0:
                    break
                take = min(remaining[group_id], room - placed)
                if take <= 0:
                    continue
                load[group_id] = load.get(group_id, 0) + take
                placed += take
                remaining[group_id] -= take
                if not remaining[group_id]:
                    del remaining[group_id]
            total -= placed
            flights.append(
                Flight(
                    base_airport=column.base_airport,
                    aircraft_type=column.aircraft_type,
                    route=column.route,
                    refuel_decisions=column.refuel_decisions,
                    load=tuple(sorted(load.items())),
                )
            )
        if remaining:
            raise RuntimeError(f"航线 {column_id} 的人员流未能完整拆分: {remaining}")
    return flights


# --------------------------------------------------------------------- 改进
def _lex_key(metrics: FlightMetrics) -> tuple[int, int, float]:
    # 单架次只能安全自动比较前三级。架次数恒为 1；Stage 5 是
    # 全局 sum(PK)/sum(AK)，不能用单架次 AK 或 ratio 代替。
    return (
        metrics.aircraft_time,
        metrics.passenger_time,
        metrics.fuel_used,
    )


def improve_flight(
    flight: Flight,
    groups: Mapping[str, RequestGroup],
    distances: DistanceMap,
    *,
    allow_rebase: bool = True,
    allow_retype: bool = True,
    refuel_keep: int = 4,
) -> Flight:
    """收缩到实际投放设施集合，并在允许范围内改选机场/机型/停靠顺序。"""
    if not flight.load:
        return flight
    weights: dict[str, int] = {}
    for group_id, quantity in flight.load:
        weights[groups[group_id].destination_id] = (
            weights.get(groups[group_id].destination_id, 0) + quantity
        )
    facilities = tuple(sorted(weights))
    passengers = flight.passengers

    bases = {flight.base_airport}
    if allow_rebase:
        allowed = set(AIRPORTS)
        for group_id, _ in flight.load:
            origin = groups[group_id].origin_id
            if origin != LAND:
                allowed &= {origin}
        bases |= allowed
    types = (
        [name for name, spec in AIRCRAFT_SPECS.items() if spec.capacity >= passengers]
        if allow_retype
        else [flight.aircraft_type]
    )

    current = flight
    best_key = _lex_key(flight_metrics(flight, groups, distances))
    for base in sorted(bases):
        for aircraft_type in types:
            plan = best_route(
                base,
                AIRCRAFT_SPECS[aircraft_type],
                facilities,
                distances,
                refuel_keep=refuel_keep,
                weights=weights,
            )
            if plan is None:
                continue
            candidate = Flight(
                base_airport=base,
                aircraft_type=aircraft_type,
                route=plan.route,
                refuel_decisions=plan.refuel_decisions,
                load=flight.load,
            )
            key = _lex_key(flight_metrics(candidate, groups, distances))
            if key < best_key:
                best_key = key
                current = candidate
    return current


def improve_flights(
    flights: Sequence[Flight],
    groups: Mapping[str, RequestGroup],
    distances: DistanceMap,
    **kwargs,
) -> list[Flight]:
    return [improve_flight(flight, groups, distances, **kwargs) for flight in flights]


# --------------------------------------------------------------------- 回填
def assign_people(
    flights: Sequence[Flight],
    groups: Sequence[RequestGroup],
) -> list[PersonAssignment]:
    """按原始 person_id 顺序把人员回填到架次副本上。"""
    from collections import deque

    queues = {group.group_id: deque(group.person_ids) for group in groups}
    destinations = {group.group_id: group.destination_id for group in groups}
    counters: dict[str, int] = {}
    result: list[PersonAssignment] = []
    for flight in flights:
        counters[flight.aircraft_type] = counters.get(flight.aircraft_type, 0) + 1
        flight_no = counters[flight.aircraft_type]
        for group_id, quantity in flight.load:
            queue = queues[group_id]
            if len(queue) < quantity:
                raise ValueError(f"组 {group_id} 人员不足以回填")
            delivery = flight.route.index(destinations[group_id])
            for _ in range(quantity):
                result.append(
                    PersonAssignment(
                        person_id=queue.popleft(),
                        aircraft_type=flight.aircraft_type,
                        flight_no=flight_no,
                        pickup_stop_order=0,
                        delivery_stop_order=delivery,
                        column_id=f"{flight.aircraft_type}-{flight_no}",
                    )
                )
    leftover = {key: len(queue) for key, queue in queues.items() if queue}
    if leftover:
        raise ValueError(f"人员回填后仍有遗漏: {leftover}")
    return result


def flight_order(flights: Sequence[Flight]) -> list[Flight]:
    """稳定的输出顺序：机型 -> 机场 -> 路线，保证结果可复现。"""
    return sorted(
        flights,
        key=lambda flight: (flight.aircraft_type, flight.base_airport, flight.route, flight.load),
    )


def to_columns(
    flights: Sequence[Flight],
    groups: Mapping[str, RequestGroup],
    distances: DistanceMap,
) -> list[RouteColumn]:
    """把改进后的架次折回成候选航线列，用于回灌候选池。"""
    from q1.algorithms.clusters import column_from_plan

    columns: list[RouteColumn] = []
    seen: set[tuple[object, ...]] = set()
    for flight in flights:
        facilities = tuple(
            sorted({groups[group_id].destination_id for group_id, _ in flight.load})
        )
        key = (flight.base_airport, flight.aircraft_type, facilities)
        if key in seen or not facilities:
            continue
        seen.add(key)
        plan = _plan_of(flight, distances)
        columns.append(column_from_plan(plan, facilities))
    return columns
