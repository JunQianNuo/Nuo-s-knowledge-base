from __future__ import annotations

import hashlib
import heapq
from dataclasses import dataclass
from itertools import combinations
from typing import Mapping, Optional, Sequence

from common.config import AIRCRAFT_SPECS, AIRPORTS, LAND, MAX_OFFSHORE_LANDINGS, REFUEL_FACILITIES
from common.feasibility import evaluate_sortie, leg_flight_minutes
from common.models import AircraftSpec, RequestGroup


@dataclass(frozen=True)
class PhysicalRoute:
    route_id: str
    base_airport: str
    aircraft_type: str
    route: tuple[str, ...]
    refuel_decisions: tuple[bool, ...]
    aircraft_time: int
    fuel_used: float
    total_distance: float
    available_seat_km: float
    arrival_minutes: tuple[int, ...]
    departure_minutes: tuple[int, ...]

    @property
    def capacity(self) -> int:
        return AIRCRAFT_SPECS[self.aircraft_type].capacity


@dataclass(frozen=True)
class ServiceOption:
    option_id: str
    group_id: str
    route_id: str
    pickup: int
    delivery: int
    passenger_time: int
    passenger_km: float


def service_options(group: RequestGroup, physical: PhysicalRoute) -> list[ServiceOption]:
    base = physical.base_airport
    if group.origin_id in AIRPORTS and group.origin_id != base:
        return []
    if group.destination_id in AIRPORTS and group.destination_id != base:
        return []
    origin = base if group.origin_id == LAND else group.origin_id
    destination = base if group.destination_id == LAND else group.destination_id
    cumulative = [0.0]
    for first, second in zip(physical.route, physical.route[1:]):
        # total_distance alone is insufficient for an option; the builder stores no distance map.
        cumulative.append(cumulative[-1])
    result = []
    for pickup, location in enumerate(physical.route[:-1]):
        if location != origin:
            continue
        delivery = next(
            (i for i in range(pickup + 1, len(physical.route)) if physical.route[i] == destination),
            None,
        )
        if delivery is None:
            continue
        result.append(
            ServiceOption(
                f"{group.group_id}@{physical.route_id}:{pickup}-{delivery}",
                group.group_id,
                physical.route_id,
                pickup,
                delivery,
                physical.arrival_minutes[delivery] - physical.departure_minutes[pickup],
                0.0,
            )
        )
    return result


def _make_physical(
    base: str,
    spec: AircraftSpec,
    stops: Sequence[str],
    refuels: Sequence[bool],
    distances: Mapping[tuple[str, str], float],
) -> Optional[PhysicalRoute]:
    route = (base, *stops, base)
    decisions = (False, *refuels, False)
    checked = evaluate_sortie(
        base_airport=base,
        aircraft=spec,
        route=route,
        refuel_decisions=decisions,
        allocations=(),
        groups={},
        distances=distances,
    )
    if not checked.feasible:
        return None
    total_distance = sum(distances[arc] for arc in zip(route, route[1:]))
    signature = (
        f"{base}|{spec.aircraft_type}|{','.join(route)}|{''.join(map(str, map(int, decisions)))}"
    )
    route_id = "R" + hashlib.sha1(signature.encode()).hexdigest()[:12]
    return PhysicalRoute(
        route_id,
        base,
        spec.aircraft_type,
        route,
        decisions,
        checked.aircraft_time,
        checked.fuel_used,
        total_distance,
        checked.available_seat_km,
        checked.arrival_minutes,
        checked.departure_minutes,
    )


def best_refueled_route_for_order(
    base: str,
    spec: AircraftSpec,
    service_order: Sequence[str],
    distances: Mapping[tuple[str, str], float],
) -> Optional[PhysicalRoute]:
    """Keep the service order fixed; optimize refuels and inserted refuel stops."""
    order = tuple(service_order)
    if not order or len(order) > MAX_OFFSHORE_LANDINGS:
        return None
    max_extra = MAX_OFFSHORE_LANDINGS - len(order)
    stations = tuple(sorted(REFUEL_FACILITIES - set(order)))
    tank, reserve, rate = (
        spec.tank_capacity_kg,
        spec.reserve_fuel_kg,
        spec.fuel_consumption_kg_per_km,
    )
    # (time, location, served-prefix, extra-stops, -fuel, trace, refuels)
    queue = [(0, base, 0, 0, -tank, (), ())]
    labels: dict[tuple[str, int, int], list[tuple[int, float]]] = {}
    best = None
    while queue:
        elapsed, location, done, extra, neg_fuel, trace, marks = heapq.heappop(queue)
        fuel = -neg_fuel
        key = (location, done, extra)
        frontier = labels.setdefault(key, [])
        if any(t <= elapsed and f >= fuel - 1e-9 for t, f in frontier):
            continue
        frontier[:] = [(t, f) for t, f in frontier if not (elapsed <= t and fuel >= f - 1e-9)]
        frontier.append((elapsed, fuel))
        if best is not None and elapsed >= best.aircraft_time:
            continue
        if done == len(order):
            distance = distances[(location, base)]
            if fuel - rate * distance >= reserve - 1e-9:
                candidate = _make_physical(base, spec, trace, marks, distances)
                if candidate and (best is None or _route_key(candidate) < _route_key(best)):
                    best = candidate
        if done < len(order):
            destination = order[done]
            distance = distances[(location, destination)]
            remaining = fuel - rate * distance
            if remaining >= reserve - 1e-9:
                base_time = elapsed + leg_flight_minutes(distance, spec.speed_kmh) + 10
                heapq.heappush(
                    queue,
                    (
                        base_time,
                        destination,
                        done + 1,
                        extra,
                        -remaining,
                        (*trace, destination),
                        (*marks, False),
                    ),
                )
                if destination in REFUEL_FACILITIES:
                    heapq.heappush(
                        queue,
                        (
                            base_time + 10,
                            destination,
                            done + 1,
                            extra,
                            -tank,
                            (*trace, destination),
                            (*marks, True),
                        ),
                    )
        if extra < max_extra:
            for station in stations:
                if station == location:
                    continue
                distance = distances[(location, station)]
                if fuel - rate * distance < reserve - 1e-9:
                    continue
                heapq.heappush(
                    queue,
                    (
                        elapsed + leg_flight_minutes(distance, spec.speed_kmh) + 20,
                        station,
                        done,
                        extra + 1,
                        -tank,
                        (*trace, station),
                        (*marks, True),
                    ),
                )
    return best


def _route_key(route: PhysicalRoute):
    return (
        route.aircraft_time,
        route.fuel_used,
        len(route.route),
        route.route,
        route.aircraft_type,
    )


def _events(group: RequestGroup, base: str) -> Optional[tuple[str, str]]:
    if group.origin_id in AIRPORTS and group.origin_id != base:
        return None
    if group.destination_id in AIRPORTS and group.destination_id != base:
        return None
    return (
        base if group.origin_id == LAND else group.origin_id,
        base if group.destination_id == LAND else group.destination_id,
    )


def _paired_orders(first: RequestGroup, second: RequestGroup, base: str) -> set[tuple[str, ...]]:
    events = []
    for label, group in enumerate((first, second)):
        pair = _events(group, base)
        if pair is None:
            return set()
        origin, destination = pair
        if origin != base:
            events.append((label, 0, origin))
        if destination != base:
            events.append((label, 1, destination))
    orders = set()
    from itertools import permutations

    for permutation in permutations(events):
        positions = {(label, kind): i for i, (label, kind, _) in enumerate(permutation)}
        if any(
            (label, 0) in positions
            and (label, 1) in positions
            and positions[(label, 0)] >= positions[(label, 1)]
            for label in (0, 1)
        ):
            continue
        stops = tuple(location for _, _, location in permutation)
        if len(stops) <= 5:
            orders.add(stops)
    return orders


def build_route_pool(
    groups: Sequence[RequestGroup],
    distances: Mapping[tuple[str, str], float],
    *,
    pair_limit: int = 500,
) -> tuple[list[PhysicalRoute], list[ServiceOption]]:
    routes: dict[tuple, PhysicalRoute] = {}
    compatible_bases = {}
    for group in groups:
        bases = [base for base in sorted(AIRPORTS) if _events(group, base)]
        compatible_bases[group.group_id] = bases
        for base in bases:
            origin, destination = _events(group, base) or (base, base)
            order = tuple(location for location in (origin, destination) if location != base)
            for spec in AIRCRAFT_SPECS.values():
                plan = best_refueled_route_for_order(base, spec, order, distances)
                if plan:
                    routes[
                        (plan.base_airport, plan.aircraft_type, plan.route, plan.refuel_decisions)
                    ] = plan

    scored = []
    for first, second in combinations(groups, 2):
        shared = len(
            {first.origin_id, first.destination_id} & {second.origin_id, second.destination_id}
        )
        chain = first.destination_id == second.origin_id or second.destination_id == first.origin_id
        complementary = (first.origin_id == LAND and second.destination_id == LAND) or (
            second.origin_id == LAND and first.destination_id == LAND
        )
        if not (shared or chain or complementary):
            continue
        scored.append(
            (
                -(3 * chain + 2 * complementary + shared),
                first.group_id,
                second.group_id,
                first,
                second,
            )
        )
    for _, _, _, first, second in sorted(scored)[:pair_limit]:
        for base in sorted(
            set(compatible_bases[first.group_id]) & set(compatible_bases[second.group_id])
        ):
            for order in sorted(_paired_orders(first, second, base))[:4]:
                for spec in AIRCRAFT_SPECS.values():
                    plan = best_refueled_route_for_order(base, spec, order, distances)
                    if plan:
                        routes[
                            (
                                plan.base_airport,
                                plan.aircraft_type,
                                plan.route,
                                plan.refuel_decisions,
                            )
                        ] = plan

    physical = sorted(routes.values(), key=lambda item: item.route_id)
    options = []
    for route in physical:
        cumulative = [0.0]
        for first, second in zip(route.route, route.route[1:]):
            cumulative.append(cumulative[-1] + distances[(first, second)])
        for group in groups:
            for option in service_options(group, route):
                options.append(
                    ServiceOption(
                        option.option_id,
                        option.group_id,
                        option.route_id,
                        option.pickup,
                        option.delivery,
                        option.passenger_time,
                        cumulative[option.delivery] - cumulative[option.pickup],
                    )
                )
    covered = {option.group_id for option in options}
    missing = [group.group_id for group in groups if group.group_id not in covered]
    if missing:
        raise RuntimeError(f"候选物理路线未覆盖请求组: {missing}")
    return physical, options
