from __future__ import annotations

import heapq
from dataclasses import dataclass
from typing import Sequence

from common.models import PersonAssignment, RequestGroup
from q2.algorithms.master import MasterSolution
from q2.algorithms.route_pool import PhysicalRoute, ServiceOption


@dataclass(frozen=True)
class RealizedFlight:
    route_id: str
    base_airport: str
    aircraft_type: str
    route: tuple[str, ...]
    refuel_decisions: tuple[bool, ...]
    passengers: tuple[tuple[str, int, int], ...]


def decompose_intervals(
    intervals: Sequence[tuple[str, int, int]], copies: int, capacity: int
) -> list[list[tuple[str, int, int]]]:
    """Partition unit passenger intervals into copies*capacity deterministic seat channels."""
    if copies < 0 or capacity <= 0:
        raise ValueError("非法架次数或容量")
    channel_count = copies * capacity
    channels: list[list[tuple[str, int, int]]] = [[] for _ in range(channel_count)]
    available = list(range(channel_count))
    heapq.heapify(available)
    busy: list[tuple[int, int]] = []
    for interval in sorted(intervals, key=lambda item: (item[1], item[2], item[0])):
        person_id, pickup, delivery = interval
        while busy and busy[0][0] <= pickup:  # delivery == pickup: same-stop reuse
            _, channel = heapq.heappop(busy)
            heapq.heappush(available, channel)
        if not available:
            raise RuntimeError("聚合流无法分解为实际架次：区间重叠超容量")
        channel = heapq.heappop(available)
        channels[channel].append(interval)
        heapq.heappush(busy, (delivery, channel))
    flights = [[] for _ in range(copies)]
    for channel, assigned in enumerate(channels):
        flights[channel // capacity].extend(assigned)
    return [sorted(items, key=lambda item: (item[1], item[2], item[0])) for items in flights]


def realize_solution(
    groups: Sequence[RequestGroup],
    routes: Sequence[PhysicalRoute],
    options: Sequence[ServiceOption],
    solution: MasterSolution,
) -> tuple[list[RealizedFlight], list[PersonAssignment]]:
    groups_by_id = {g.group_id: g for g in groups}
    routes_by_id = {r.route_id: r for r in routes}
    options_by_id = {o.option_id: o for o in options}
    person_cursor = {g.group_id: 0 for g in groups}
    intervals_by_route: dict[str, list[tuple[str, int, int]]] = {}
    for option_id, quantity in sorted(solution.flows.items()):
        option = options_by_id[option_id]
        group = groups_by_id[option.group_id]
        start = person_cursor[group.group_id]
        selected = group.person_ids[start : start + quantity]
        if len(selected) != quantity:
            raise RuntimeError(f"请求组 {group.group_id} 人员回填越界")
        person_cursor[group.group_id] += quantity
        intervals_by_route.setdefault(option.route_id, []).extend(
            (person_id, option.pickup, option.delivery) for person_id in selected
        )
    if any(person_cursor[g.group_id] != g.quantity for g in groups):
        raise RuntimeError("人员流未完整回填")

    flights = []
    for route_id, copies in sorted(solution.multiplicities.items()):
        route = routes_by_id[route_id]
        partitions = decompose_intervals(
            intervals_by_route.get(route_id, ()), copies, route.capacity
        )
        flights.extend(
            RealizedFlight(
                route_id,
                route.base_airport,
                route.aircraft_type,
                route.route,
                route.refuel_decisions,
                tuple(partition),
            )
            for partition in partitions
        )
    counters: dict[str, int] = {}
    assignments = []
    for flight in flights:
        counters[flight.aircraft_type] = counters.get(flight.aircraft_type, 0) + 1
        number = counters[flight.aircraft_type]
        assignments.extend(
            PersonAssignment(
                person, flight.aircraft_type, number, pickup, delivery, flight.route_id
            )
            for person, pickup, delivery in flight.passengers
        )
    return flights, assignments
