from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from common.config import AIRCRAFT_SPECS, AIRPORTS, LAND
from common.feasibility import evaluate_sortie
from common.models import RequestGroup
from q3.fleet import compatible_aircraft_ids


@dataclass(frozen=True)
class TimedColumn:
    column_id: str
    day: int
    base_airport: str
    aircraft_type: str
    route: tuple[str, ...]
    refuel_decisions: tuple[bool, ...]
    departure_time: int
    return_time: int
    arrival_times: tuple[int, ...]
    departure_times: tuple[int, ...]
    aircraft_time: int
    distance: float
    fuel_used: float
    compatible_aircraft_ids: tuple[str, ...]

    @property
    def capacity(self) -> int:
        return AIRCRAFT_SPECS[self.aircraft_type].capacity


@dataclass(frozen=True)
class ServiceOption:
    option_id: str
    group_id: str
    column_id: str
    pickup: int
    delivery: int
    passenger_time: int
    passenger_distance: float


def propagate_timed_column(
    *,
    column_id: str,
    day: int,
    base_airport: str,
    aircraft_type: str,
    route: Sequence[str],
    refuel_decisions: Sequence[bool],
    start_minute: int,
    distances: Mapping[tuple[str, str], float],
    pickup_earliest: Mapping[int, int] | None = None,
) -> TimedColumn:
    waits = [0] * len(route)
    baseline = evaluate_sortie(
        base_airport=base_airport,
        aircraft=AIRCRAFT_SPECS[aircraft_type],
        route=route,
        refuel_decisions=refuel_decisions,
        allocations=(),
        groups={},
        distances=distances,
    )
    if not baseline.feasible:
        raise ValueError("illegal route: " + "; ".join(baseline.violations))
    for stop, earliest in sorted((pickup_earliest or {}).items()):
        current_departure = start_minute + baseline.departure_minutes[stop] + sum(waits[: stop + 1])
        waits[stop] = max(waits[stop], earliest - current_departure)
    checked = evaluate_sortie(
        base_airport=base_airport,
        aircraft=AIRCRAFT_SPECS[aircraft_type],
        route=route,
        refuel_decisions=refuel_decisions,
        allocations=(),
        groups={},
        distances=distances,
        waiting_minutes=waits,
    )
    arrivals = tuple(start_minute + value for value in checked.arrival_minutes)
    departures = tuple(start_minute + value for value in checked.departure_minutes)
    day_start = day * 1440
    if not day_start + 360 <= start_minute <= day_start + 1080:
        raise ValueError("departure outside 06:00-18:00")
    if arrivals[-1] > day_start + 1200:
        raise ValueError("return after 20:00")
    if start_minute // 1440 != arrivals[-1] // 1440:
        raise ValueError("flight must return on departure day")
    total_distance = sum(float(distances[arc]) for arc in zip(route, route[1:]))
    return TimedColumn(
        column_id,
        day,
        base_airport,
        aircraft_type,
        tuple(route),
        tuple(refuel_decisions),
        start_minute,
        arrivals[-1],
        arrivals,
        departures,
        checked.aircraft_time,
        total_distance,
        checked.fuel_used,
        compatible_aircraft_ids(base_airport, aircraft_type),
    )


def service_options(group: RequestGroup, column: TimedColumn, distances) -> list[ServiceOption]:
    base = column.base_airport
    if group.origin_id in AIRPORTS and group.origin_id != base:
        return []
    if group.destination_id in AIRPORTS and group.destination_id != base:
        return []
    origin = base if group.origin_id == LAND else group.origin_id
    destination = base if group.destination_id == LAND else group.destination_id
    earliest = group.earliest_pickup_time
    latest = group.latest_arrival_time
    from q3.config import datetime_to_minute

    cumulative = [0.0]
    for arc in zip(column.route, column.route[1:]):
        cumulative.append(cumulative[-1] + float(distances[arc]))
    result = []
    for pickup, location in enumerate(column.route[:-1]):
        if location != origin:
            continue
        # first-arrival is relative to this pickup occurrence.
        delivery = next(
            (i for i in range(pickup + 1, len(column.route)) if column.route[i] == destination),
            None,
        )
        if delivery is None:
            continue
        if earliest and column.departure_times[pickup] < datetime_to_minute(earliest):
            continue
        if latest and column.arrival_times[delivery] > datetime_to_minute(latest):
            continue
        result.append(
            ServiceOption(
                f"{group.group_id}@{column.column_id}:{pickup}-{delivery}",
                group.group_id,
                column.column_id,
                pickup,
                delivery,
                column.arrival_times[delivery] - column.departure_times[pickup],
                cumulative[delivery] - cumulative[pickup],
            )
        )
    return result


def turnaround_compatible(first: TimedColumn, second: TimedColumn) -> bool:
    return second.departure_time >= first.return_time + 30
