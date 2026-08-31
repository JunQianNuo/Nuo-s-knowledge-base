from __future__ import annotations

import tempfile
from dataclasses import replace
from datetime import datetime
from pathlib import Path

import pandas as pd
import pytest

from common.config import AIRCRAFT_SPECS, AIRPORTS, OFFSHORE_FACILITIES
from common.data_loader import load_people_q2, load_people_q3
from common.grouping import group_q3
from common.models import RequestGroup
from q2.algorithms.realize import decompose_intervals
from q2.algorithms.route_pool import best_refueled_route_for_order
from q3.algorithms.timed_pool import propagate_timed_column, service_options, turnaround_compatible
from q3.config import datetime_to_minute, minute_to_datetime
from q3.fleet import FLEET
from q3.io.csv_validator import validate_q3_csv
from q3.io.csv_writer import ASSIGNMENT_COLUMNS, ROUTE_COLUMNS
from q3.run_q3_toy import _toy_data
from q3.run_q3_toy import main as toy_main


def _distances(value=20.0):
    locations = sorted(AIRPORTS | OFFSHORE_FACILITIES)
    return {
        (origin, destination): 0.0 if origin == destination else value
        for origin in locations
        for destination in locations
    }


def _column(start=360, route=("A01", "F001", "A01"), **kwargs):
    return propagate_timed_column(
        column_id="C",
        day=start // 1440,
        base_airport="A01",
        aircraft_type="T1",
        route=route,
        refuel_decisions=(False,) * len(route),
        start_minute=start,
        distances=_distances(),
        **kwargs,
    )


def test_q3_data_contract_and_q2_identity():
    q2, q3 = load_people_q2(), load_people_q3()
    groups = group_q3(q3)
    counts = q3["task_type"].value_counts().to_dict()
    assert (len(q3), len(groups), counts) == (
        4000,
        1877,
        {"shift": 3440, "production": 360, "temporary": 160, "emergency": 40},
    )
    columns = ["person_id", "origin_id", "destination_id"]
    pd.testing.assert_frame_equal(q2[columns], q3[columns], check_dtype=False)


def test_fleet_exact_mapping():
    assert len(FLEET) == len({item.aircraft_id for item in FLEET}) == 24
    assert all(item.base_airport in AIRPORTS for item in FLEET)
    assert all(item.aircraft_type in AIRCRAFT_SPECS for item in FLEET)
    counts = pd.Series([(a.base_airport, a.aircraft_type) for a in FLEET]).value_counts().to_dict()
    assert counts[("A01", "T1")] == 3 and counts[("A02", "T2")] == 4
    assert counts[("A03", "T3")] == 3


def test_time_conversion_round_trip():
    value = datetime(2026, 8, 9, 23, 59)
    assert minute_to_datetime(datetime_to_minute(value)) == value


@pytest.mark.parametrize("minute", [360, 1080])
def test_departure_boundaries_legal(minute):
    assert _column(start=minute).departure_time == minute


def test_return_2000_boundary_and_same_day():
    route = ("A01", "F001", "F002", "F003", "F004", "F005", "A01")
    distances = _distances(40.0)
    baseline = propagate_timed_column(
        column_id="boundary",
        day=0,
        base_airport="A01",
        aircraft_type="T1",
        route=route,
        refuel_decisions=(False,) * len(route),
        start_minute=1080,
        distances=distances,
        pickup_earliest={1: 1110},
    )
    assert baseline.return_time == 1200
    assert baseline.return_time // 1440 == baseline.departure_time // 1440


@pytest.mark.parametrize("gap,legal", [(29, False), (30, True), (31, True)])
def test_turnaround_29_30_31(gap, legal):
    first = _column()
    second = _column(start=first.return_time + gap)
    assert turnaround_compatible(first, second) is legal


def test_land_concrete_airport_first_arrival_and_time_windows():
    column = _column(route=("A01", "F001", "F002", "F001", "A01"))
    land = RequestGroup(
        "G", ("P",), "LAND", "F001", datetime(2026, 8, 3, 6), datetime(2026, 8, 3, 8)
    )
    concrete_bad = replace(land, group_id="B", origin_id="A02")
    repeated_origin = replace(land, group_id="R", origin_id="F001", destination_id="A01")
    assert [(o.pickup, o.delivery) for o in service_options(land, column, _distances())] == [(0, 1)]
    assert not service_options(concrete_bad, column, _distances())
    assert [
        (o.pickup, o.delivery) for o in service_options(repeated_origin, column, _distances())
    ] == [
        (1, 4),
        (3, 4),
    ]
    too_early = replace(land, group_id="E", earliest_pickup_time=datetime(2026, 8, 3, 7))
    too_late = replace(land, group_id="L", latest_arrival_time=datetime(2026, 8, 3, 6, 1))
    assert not service_options(too_early, column, _distances())
    assert not service_options(too_late, column, _distances())


def test_waiting_propagation_is_counted():
    normal = _column(route=("A01", "F001", "F002", "A01"))
    waited = _column(
        route=("A01", "F001", "F002", "A01"), pickup_earliest={1: normal.departure_times[1] + 17}
    )
    assert waited.aircraft_time == normal.aircraft_time + 17


def test_dynamic_capacity_same_stop_and_decomposition_failure():
    intervals = [(f"A{i}", 0, 1) for i in range(12)] + [(f"B{i}", 1, 2) for i in range(12)]
    assert len(decompose_intervals(intervals, 1, 12)[0]) == 24
    with pytest.raises(RuntimeError):
        decompose_intervals([(str(i), 0, 2) for i in range(13)], 1, 12)


def test_fuel_and_post_delivery_refuel():
    distances = _distances(999.0)
    distances.update(
        {
            ("A01", "F001"): 200.0,
            ("A01", "F006"): 100.0,
            ("F006", "F001"): 100.0,
            ("F001", "F006"): 100.0,
            ("F006", "A01"): 100.0,
        }
    )
    plan = best_refueled_route_for_order("A01", AIRCRAFT_SPECS["T1"], ("F001",), distances)
    assert plan and any(
        i > plan.route.index("F001") and plan.refuel_decisions[i] for i in range(len(plan.route))
    )


def test_csv_schema_and_independent_toy_validator():
    assert ASSIGNMENT_COLUMNS == [
        "person_id",
        "aircraft_id",
        "flight_no",
        "pickup_stop_order",
        "delivery_stop_order",
    ]
    assert ROUTE_COLUMNS[-3:] == ["arrival_time", "departure_time", "refuel"]
    assert toy_main() == 0


def test_validator_rejects_dropped_mandatory_but_allows_blank_temporary():
    people, matrix, _ = _toy_data()
    assignments = pd.DataFrame(
        [
            {name: person if name == "person_id" else "" for name in ASSIGNMENT_COLUMNS}
            for person in people.person_id
        ],
        columns=ASSIGNMENT_COLUMNS,
    )
    with tempfile.TemporaryDirectory(prefix="q3-validator-") as directory:
        root = Path(directory)
        people_path, distance_path = root / "peopleQ3.csv", root / "distances.csv"
        route_path, assignment_path = root / "q3-routes.csv", root / "q3-assignments.csv"
        people.to_csv(people_path, index=False)
        matrix.to_csv(distance_path, index=False)
        pd.DataFrame(columns=ROUTE_COLUMNS).to_csv(route_path, index=False)
        assignments.to_csv(assignment_path, index=False)
        report = validate_q3_csv(
            routes_path=route_path,
            assignments_path=assignment_path,
            people_path=people_path,
            distances_path=distance_path,
        )
    assert not report.valid and report.mandatory_missing == 25 and report.invalid_temporary == 0
