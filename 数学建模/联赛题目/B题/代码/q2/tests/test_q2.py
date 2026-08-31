from __future__ import annotations

import tempfile
import time
from pathlib import Path

import pandas as pd

from common.config import AIRCRAFT_SPECS, AIRPORTS, OFFSHORE_FACILITIES
from common.data_loader import load_distances, load_people_q2
from common.grouping import group_q2
from common.models import RequestGroup
from q2.algorithms.master import RouteFlowMaster
from q2.algorithms.realize import decompose_intervals, realize_solution
from q2.algorithms.route_pool import (
    _make_physical,
    best_refueled_route_for_order,
    service_options,
)
from q2.io.csv_validator import validate_q2_csv
from q2.io.csv_writer import ASSIGNMENT_COLUMNS, ROUTE_COLUMNS, write_q2_csv


def _uniform_distances(value=20.0):
    locations = sorted(AIRPORTS | OFFSHORE_FACILITIES)
    return {(a, b): (0.0 if a == b else value) for a in locations for b in locations}


def _route(stops=("F001", "F002", "F001"), base="A01"):
    result = _make_physical(
        base,
        AIRCRAFT_SPECS["T1"],
        stops,
        (False,) * len(stops),
        _uniform_distances(),
    )
    assert result is not None
    return result


def test_q2_data_counts():
    people = load_people_q2()
    groups = group_q2(people)
    outbound = people["origin_id"].isin(["LAND", "A01", "A02", "A03"]).sum()
    returns = people["destination_id"].isin(["LAND", "A01", "A02", "A03"]).sum()
    assert (len(people), len(groups), outbound, returns, len(people) - outbound - returns) == (
        4000,
        264,
        1600,
        1600,
        800,
    )


def test_land_outbound_and_return_options():
    route = _route(("F001", "F002"))
    outbound = service_options(RequestGroup("O", ("P",), "LAND", "F001"), route)
    returning = service_options(RequestGroup("R", ("Q",), "F002", "LAND"), route)
    assert [(o.pickup, o.delivery) for o in outbound] == [(0, 1)]
    assert [(o.pickup, o.delivery) for o in returning] == [(2, 3)]


def test_concrete_airport_compatibility():
    route = _route(("F001",))
    assert service_options(RequestGroup("G", ("P",), "A01", "F001"), route)
    assert not service_options(RequestGroup("H", ("Q",), "A02", "F001"), route)


def test_shuttle_and_first_arrival_with_repeated_destination():
    route = _route()
    options = service_options(RequestGroup("G", ("P",), "F002", "F001"), route)
    assert [(o.pickup, o.delivery) for o in options] == [(2, 3)]
    repeated_origin = service_options(RequestGroup("H", ("Q",), "F001", "A01"), route)
    assert [(o.pickup, o.delivery) for o in repeated_origin] == [(1, 4), (3, 4)]


def test_same_stop_reuse_and_dynamic_capacity_decomposition():
    intervals = [
        *(("A" + str(i), 0, 1) for i in range(12)),
        *(("B" + str(i), 1, 2) for i in range(12)),
    ]
    flights = decompose_intervals(intervals, copies=1, capacity=12)
    assert len(flights) == 1 and len(flights[0]) == 24


def test_interval_decomposition_multiple_copies_and_failure():
    intervals = [(str(i), 0, 2) for i in range(7)]
    flights = decompose_intervals(intervals, copies=2, capacity=4)
    assert sorted(map(len, flights)) == [3, 4]
    try:
        decompose_intervals(intervals, copies=1, capacity=4)
    except RuntimeError:
        pass
    else:
        raise AssertionError("over-capacity intervals must fail")


def test_route_flow_master_toy_matches_explicit_pattern_result():
    groups = [
        RequestGroup("G1", tuple(f"P{i}" for i in range(12)), "LAND", "F001"),
        RequestGroup("G2", tuple(f"Q{i}" for i in range(12)), "F001", "LAND"),
    ]
    route = _route(("F001",))
    options = [option for group in groups for option in service_options(group, route)]
    options = [
        type(o)(o.option_id, o.group_id, o.route_id, o.pickup, o.delivery, o.passenger_time, 20.0)
        for o in options
    ]
    solution = RouteFlowMaster(groups, [route], options).solve(
        deadline=time.perf_counter() + 10, workers=1, stages=("aircraft_time",)
    )
    # One explicit passenger pattern serves 12 outbound + 12 return passengers.
    assert solution.status == "OPTIMAL" and solution.flights == 1


def test_fixed_order_refuel_after_last_delivery():
    distances = _uniform_distances(999.0)
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
    assert plan is not None
    delivery = plan.route.index("F001")
    later_refuels = [
        index
        for index, location in enumerate(plan.route)
        if index > delivery and location == "F006" and plan.refuel_decisions[index]
    ]
    assert later_refuels


def test_csv_schema_independent_validator_and_metrics():
    people = pd.DataFrame(
        [("P", "LAND", "F001"), ("Q", "F001", "LAND")],
        columns=["person_id", "origin_id", "destination_id"],
    )
    groups = group_q2(people)
    route = _route(("F001",))
    options = [option for group in groups for option in service_options(group, route)]
    options = [
        type(o)(o.option_id, o.group_id, o.route_id, o.pickup, o.delivery, o.passenger_time, 20.0)
        for o in options
    ]
    solution = RouteFlowMaster(groups, [route], options).solve(
        deadline=time.perf_counter() + 10, workers=1
    )
    flights, assignments = realize_solution(groups, [route], options, solution)
    with tempfile.TemporaryDirectory(prefix="q2-test-") as directory:
        route_path, assignment_path = write_q2_csv(Path(directory), people, flights, assignments)
        assert list(pd.read_csv(route_path).columns) == ROUTE_COLUMNS
        assert list(pd.read_csv(assignment_path).columns) == ASSIGNMENT_COLUMNS
        report = validate_q2_csv(
            routes_path=route_path,
            assignments_path=assignment_path,
            people=people,
            distances=_uniform_distances(),
        )
    assert report.valid
    assert report.metrics.total_aircraft_time == solution.aircraft_time
    assert report.metrics.total_passenger_time == solution.passenger_time
    assert report.metrics.passenger_km == solution.passenger_km


def test_real_distance_interface_available():
    assert len(load_distances().locations) == 55
