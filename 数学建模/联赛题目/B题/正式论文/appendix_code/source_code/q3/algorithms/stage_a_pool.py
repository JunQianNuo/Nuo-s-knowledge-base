from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence

import pandas as pd

from common.config import AIRCRAFT_SPECS, AIRPORTS, LAND
from common.models import RequestGroup
from q2.algorithms.route_pool import (
    PhysicalRoute,
    _make_physical,
)
from q2.algorithms.route_pool import (
    service_options as physical_options,
)
from q3.algorithms.timed_pool import (
    ServiceOption,
    TimedColumn,
    propagate_timed_column,
    service_options,
)
from q3.config import HORIZON_DAYS, datetime_to_minute
from q3.fleet import FLEET_BY_ID


@dataclass(frozen=True)
class PoolStats:
    physical_skeletons: int
    timed_columns: int
    service_options: int
    minimum_group_coverage: int


def _key(route: PhysicalRoute):
    return route.base_airport, route.aircraft_type, route.route, route.refuel_decisions


def load_q2_seeds(path: Path, distances) -> list[PhysicalRoute]:
    if not path.is_file():
        return []
    frame = pd.read_csv(path)
    result = []
    for (kind, _), rows in frame.groupby(["aircraft_type", "flight_no"], sort=False):
        rows = rows.sort_values("stop_order")
        route = tuple(rows["facility_id"].astype(str))
        plan = _make_physical(
            route[0],
            AIRCRAFT_SPECS[str(kind)],
            route[1:-1],
            tuple(bool(value) for value in rows["refuel"].astype(int).tolist()[1:-1]),
            distances,
        )
        if plan is not None:
            result.append(plan)
    return result


def load_q3_seeds(path: Path, distances) -> list[PhysicalRoute]:
    if not path.is_file():
        return []
    frame = pd.read_csv(path)
    result = []
    for (aircraft_id, _), rows in frame.groupby(["aircraft_id", "flight_no"], sort=False):
        rows = rows.sort_values("stop_order")
        aircraft = FLEET_BY_ID[str(aircraft_id)]
        route = tuple(rows["facility_id"].astype(str))
        plan = _make_physical(
            route[0],
            AIRCRAFT_SPECS[aircraft.aircraft_type],
            route[1:-1],
            tuple(bool(value) for value in rows["refuel"].astype(int).tolist()[1:-1]),
            distances,
        )
        if plan is not None:
            result.append(plan)
    return result


def build_skeletons(
    groups: Sequence[RequestGroup],
    distances,
    q2_routes_path: Optional[Path] = None,
    additional_routes_path: Optional[Path] = None,
) -> list[PhysicalRoute]:
    routes = (
        {_key(route): route for route in load_q2_seeds(q2_routes_path, distances)}
        if q2_routes_path
        else {}
    )
    if additional_routes_path:
        routes.update(
            {_key(route): route for route in load_q3_seeds(additional_routes_path, distances)}
        )
    by_od = {}
    for group in groups:
        by_od.setdefault((group.origin_id, group.destination_id), group)
    for group in by_od.values():
        candidates = []
        for base in sorted(AIRPORTS):
            if group.origin_id in AIRPORTS and group.origin_id != base:
                continue
            if group.destination_id in AIRPORTS and group.destination_id != base:
                continue
            origin = base if group.origin_id == LAND else group.origin_id
            destination = base if group.destination_id == LAND else group.destination_id
            order = tuple(value for value in (origin, destination) if value != base)
            for spec in AIRCRAFT_SPECS.values():
                plan = _make_physical(base, spec, order, (False,) * len(order), distances)
                if plan is not None:
                    candidates.append(plan)
        # Keep short alternatives without multiplying every OD by all nine base/type choices.
        for plan in sorted(candidates, key=lambda item: (item.aircraft_time, item.fuel_used))[:2]:
            routes[_key(plan)] = plan
    return sorted(routes.values(), key=lambda item: item.route_id)


TIME_SAMPLING_FRACTIONS = {
    "baseline": (0.0, 0.5, 1.0),
    "dense": (0.0, 0.25, 0.5, 0.75, 1.0),
}


def _critical_starts(
    route: PhysicalRoute,
    groups: Sequence[RequestGroup],
    time_sampling_density: str = "baseline",
) -> set[int]:
    fractions = TIME_SAMPLING_FRACTIONS[time_sampling_density]
    starts = set()
    for group in groups:
        for option in physical_options(group, route):
            lower = (
                datetime_to_minute(group.earliest_pickup_time)
                - route.departure_minutes[option.pickup]
            )
            upper = (
                datetime_to_minute(group.latest_arrival_time)
                - route.arrival_minutes[option.delivery]
            )
            for day in range(HORIZON_DAYS):
                day_start = day * 1440
                lo = max(lower, day_start + 360)
                hi = min(upper, day_start + 1080, day_start + 1200 - route.aircraft_time)
                if lo <= hi:
                    starts.update(lo + int((hi - lo) * fraction) for fraction in fractions)
    return starts


def build_timed_pool(
    groups: Sequence[RequestGroup],
    skeletons: Sequence[PhysicalRoute],
    distances,
    time_sampling_density: str = "baseline",
) -> tuple[list[TimedColumn], list[ServiceOption], PoolStats]:
    columns = {}
    for skeleton in skeletons:
        relevant = [group for group in groups if physical_options(group, skeleton)]
        baseline_starts = _critical_starts(skeleton, relevant, "baseline")
        for start in sorted(_critical_starts(skeleton, relevant, time_sampling_density)):
            signature = f"{skeleton.route_id}|{start}"
            column_id = "TC" + hashlib.sha1(signature.encode()).hexdigest()[:14]
            try:
                column = propagate_timed_column(
                    column_id=column_id,
                    day=start // 1440,
                    base_airport=skeleton.base_airport,
                    aircraft_type=skeleton.aircraft_type,
                    route=skeleton.route,
                    refuel_decisions=skeleton.refuel_decisions,
                    start_minute=start,
                    distances=distances,
                )
            except ValueError:
                continue
            options = [
                option for group in relevant for option in service_options(group, column, distances)
            ]
            if options:
                key = (
                    column.day,
                    column.base_airport,
                    column.aircraft_type,
                    column.route,
                    column.refuel_decisions,
                    column.arrival_times,
                    column.departure_times,
                )
                columns[key] = (column, options, start in baseline_starts)
    raw_timed = {value[0].column_id: value[0] for value in columns.values()}
    raw_options = [option for key in sorted(columns) for option in columns[key][1]]
    baseline_columns = {
        value[0].column_id for value in columns.values() if value[2]
    }
    by_group = {group.group_id: [] for group in groups}
    for option in raw_options:
        by_group[option.group_id].append(option)
    options = []
    for group_id in sorted(by_group):
        ordered = sorted(
            by_group[group_id],
            key=lambda option: (
                raw_timed[option.column_id].aircraft_time,
                option.passenger_time,
                option.column_id,
            ),
        )
        if time_sampling_density == "dense":
            options.extend(
                [option for option in ordered if option.column_id in baseline_columns][:60]
            )
            options.extend(
                [option for option in ordered if option.column_id not in baseline_columns][:60]
            )
        else:
            options.extend(ordered[:60])
    used_columns = {option.column_id for option in options}
    timed = sorted(
        (column for column_id, column in raw_timed.items() if column_id in used_columns),
        key=lambda item: item.column_id,
    )
    coverage = {group.group_id: 0 for group in groups}
    for option in options:
        coverage[option.group_id] += 1
    missing = [group_id for group_id, count in coverage.items() if count == 0]
    if missing:
        raise RuntimeError(f"zero-option mandatory groups: {missing[:20]}")
    stats = PoolStats(len(skeletons), len(timed), len(options), min(coverage.values()))
    return timed, options, stats
