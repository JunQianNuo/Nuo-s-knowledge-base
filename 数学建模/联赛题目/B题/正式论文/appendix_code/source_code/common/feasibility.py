from __future__ import annotations

import math
from datetime import datetime, timedelta
from typing import Optional, Sequence

from .config import (
    AIRPORTS,
    LAND,
    MAX_OFFSHORE_LANDINGS,
    OFFSHORE_FACILITIES,
    Q3_FIRST_DEPARTURE_MINUTE,
    Q3_LAST_DEPARTURE_MINUTE,
    Q3_RETURN_DEADLINE_MINUTE,
    REFUEL_EXTRA_MINUTES,
    REFUEL_FACILITIES,
    STOP_DURATION_MINUTES,
)
from .models import (
    AircraftSpec,
    DistanceMap,
    FeasibilityResult,
    PassengerAllocation,
    RequestGroup,
)


def leg_flight_minutes(distance_km: float, speed_kmh: int) -> int:
    """K-1：每一航段单独向上取整。"""
    return math.ceil(60 * distance_km / speed_kmh)


def _actual_location(location: str, base_airport: str) -> str:
    return base_airport if location == LAND else location


def _validate_route(route: Sequence[str], base: str) -> list[str]:
    violations: list[str] = []
    if base not in AIRPORTS:
        violations.append(f"非法起降机场: {base}")
    if len(route) < 3:
        violations.append("路线至少需要一次海上着陆")
        return violations
    if route[0] != base or route[-1] != base:
        violations.append("路线必须从所属机场出发并返回同一机场")
    middle = route[1:-1]
    if not 1 <= len(middle) <= MAX_OFFSHORE_LANDINGS:
        violations.append(f"海上着陆次数必须为1至{MAX_OFFSHORE_LANDINGS}")
    illegal = [location for location in middle if location not in OFFSHORE_FACILITIES]
    if illegal:
        violations.append(f"中间停靠必须为海上设施: {illegal}")
    return violations


def _validate_allocations(
    route: Sequence[str],
    base: str,
    allocations: Sequence[PassengerAllocation],
    groups: dict[str, RequestGroup],
) -> list[str]:
    violations: list[str] = []
    for allocation in allocations:
        group = groups.get(allocation.group_id)
        if group is None:
            violations.append(f"未知请求组: {allocation.group_id}")
            continue
        if allocation.quantity <= 0 or allocation.quantity > group.quantity:
            violations.append(f"组 {group.group_id} 服务人数非法: {allocation.quantity}")
        origin = _actual_location(group.origin_id, base)
        destination = _actual_location(group.destination_id, base)
        if group.origin_id in AIRPORTS and group.origin_id != base:
            violations.append(f"组 {group.group_id} 起点机场与架次机场不兼容")
        if group.destination_id in AIRPORTS and group.destination_id != base:
            violations.append(f"组 {group.group_id} 终点机场与架次机场不兼容")
        pickup, delivery = allocation.pickup_stop, allocation.delivery_stop
        if not (0 <= pickup < delivery < len(route)):
            violations.append(f"组 {group.group_id} 必须满足 pickup < delivery")
            continue
        if route[pickup] != origin or route[delivery] != destination:
            violations.append(f"组 {group.group_id} 上下机位置与OD不匹配")
            continue
        first_delivery = next(
            (index for index in range(pickup + 1, len(route)) if route[index] == destination),
            None,
        )
        if delivery != first_delivery:
            violations.append(f"组 {group.group_id} 未在上机后首次到达终点时下机")
    return violations


def _leg_loads(allocations: Sequence[PassengerAllocation], route_length: int) -> tuple[int, ...]:
    # K-10：到站先下后上，释放的座位立即用于下一航段。
    return tuple(
        sum(item.quantity for item in allocations if item.pickup_stop <= leg < item.delivery_stop)
        for leg in range(route_length - 1)
    )


def evaluate_sortie(
    *,
    base_airport: str,
    aircraft: AircraftSpec,
    route: Sequence[str],
    refuel_decisions: Sequence[bool],
    allocations: Sequence[PassengerAllocation],
    groups: dict[str, RequestGroup],
    distances: DistanceMap,
    start_time: Optional[datetime] = None,
    waiting_minutes: Optional[Sequence[int]] = None,
) -> FeasibilityResult:
    violations = _validate_route(route, base_airport)
    if len(refuel_decisions) != len(route):
        violations.append("加油决策长度必须与路线长度一致")
        refuels = tuple(False for _ in route)
    else:
        refuels = tuple(bool(value) for value in refuel_decisions)
    if refuels and (refuels[0] or refuels[-1]):
        violations.append("机场行不得标记海上加油")
    for index in range(1, max(1, len(route) - 1)):
        if index < len(refuels) and refuels[index] and route[index] not in REFUEL_FACILITIES:
            violations.append(f"停靠 {index} 不是合法加油设施")
    violations.extend(_validate_allocations(route, base_airport, allocations, groups))

    waits = tuple(waiting_minutes or (0 for _ in route))
    if len(waits) != len(route):
        violations.append("等待时间长度必须与路线长度一致")
        waits = tuple(0 for _ in route)
    if any(value < 0 for value in waits):
        violations.append("等待时间不得为负")

    leg_distances: list[float] = []
    leg_minutes: list[int] = []
    for origin, destination in zip(route, route[1:]):
        try:
            distance = float(distances[(origin, destination)])
        except KeyError:
            violations.append(f"距离表缺少弧 {origin} -> {destination}")
            distance = 0.0
        if distance < 0 or not math.isfinite(distance):
            violations.append(f"弧 {origin} -> {destination} 距离非法")
            distance = 0.0
        leg_distances.append(distance)
        leg_minutes.append(leg_flight_minutes(distance, aircraft.speed_kmh))

    loads = _leg_loads(allocations, len(route))
    for leg, load in enumerate(loads):
        if load > aircraft.capacity:
            violations.append(f"航段 {leg}->{leg + 1} 超容量: {load}>{aircraft.capacity}")

    fuel = aircraft.tank_capacity_kg
    arrival_fuel: list[float] = []
    for leg, distance in enumerate(leg_distances):
        fuel -= aircraft.fuel_consumption_kg_per_km * distance
        arrival_fuel.append(fuel)
        if fuel < aircraft.reserve_fuel_kg - 1e-9:
            violations.append(f"到达停靠 {leg + 1} 后燃油低于安全余油")
        if leg + 1 < len(route) - 1 and refuels[leg + 1]:
            fuel = aircraft.tank_capacity_kg

    arrival_elapsed = [0]
    departure_elapsed = [0]
    elapsed = 0
    for leg, flight_minutes in enumerate(leg_minutes):
        elapsed += flight_minutes
        arrival_elapsed.append(elapsed)
        if leg + 1 < len(route) - 1:
            elapsed += STOP_DURATION_MINUTES
            if refuels[leg + 1]:
                elapsed += REFUEL_EXTRA_MINUTES
            elapsed += waits[leg + 1]
        departure_elapsed.append(elapsed)

    passenger_time = sum(
        item.quantity * (arrival_elapsed[item.delivery_stop] - departure_elapsed[item.pickup_stop])
        for item in allocations
        if 0 <= item.pickup_stop < item.delivery_stop < len(route)
    )
    passenger_km = sum(load * distance for load, distance in zip(loads, leg_distances))
    total_distance = sum(leg_distances)

    if start_time is not None:
        finish = start_time + timedelta(minutes=elapsed)
        start_minute = start_time.hour * 60 + start_time.minute
        finish_minute = finish.hour * 60 + finish.minute
        if not Q3_FIRST_DEPARTURE_MINUTE <= start_minute <= Q3_LAST_DEPARTURE_MINUTE:
            violations.append("Q3起飞时刻不在06:00—18:00")
        if finish.date() != start_time.date() or finish_minute > Q3_RETURN_DEADLINE_MINUTE:
            violations.append("Q3架次未在当日20:00前返场")
        for item in allocations:
            group = groups.get(item.group_id)
            if group is None or not (0 <= item.pickup_stop < item.delivery_stop < len(route)):
                continue
            pickup_time = start_time + timedelta(minutes=departure_elapsed[item.pickup_stop])
            delivery_time = start_time + timedelta(minutes=arrival_elapsed[item.delivery_stop])
            if group.earliest_pickup_time and pickup_time < group.earliest_pickup_time:
                violations.append(f"组 {group.group_id} 早于最早接人时刻离站")
            if group.latest_arrival_time and delivery_time > group.latest_arrival_time:
                violations.append(f"组 {group.group_id} 晚于最晚到达时刻")

    return FeasibilityResult(
        feasible=not violations,
        violations=tuple(violations),
        aircraft_time=elapsed,
        passenger_time=passenger_time,
        fuel_used=aircraft.fuel_consumption_kg_per_km * total_distance,
        passenger_km=passenger_km,
        available_seat_km=aircraft.capacity * total_distance,
        leg_loads=loads,
        arrival_fuel=tuple(arrival_fuel),
        arrival_minutes=tuple(arrival_elapsed),
        departure_minutes=tuple(departure_elapsed),
    )
