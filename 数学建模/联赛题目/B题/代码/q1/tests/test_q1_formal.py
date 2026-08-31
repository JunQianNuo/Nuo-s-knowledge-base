from __future__ import annotations

import itertools
import math
import random

import pandas as pd
import pytest

from common.config import AIRCRAFT_SPECS, MAX_OFFSHORE_LANDINGS, REFUEL_FACILITIES
from common.data_loader import load_distances, load_people_q1
from common.feasibility import evaluate_sortie
from common.grouping import group_q1
from common.models import PassengerAllocation, RequestGroup
from q1.algorithms.clusters import (
    RouteColumn,
    _pareto_filter,
    build_columns,
    enumerate_clusters,
    expand_clusters,
    number_columns,
    select_columns,
)
from q1.algorithms.flight_builder import (
    Flight,
    FlightMetrics,
    aggregate,
    assign_people,
    flight_metrics,
    improve_flight,
    split_flows,
)
from q1.algorithms.flow_master import FlowMaster
from q1.algorithms.greedy import greedy_solution
from q1.algorithms.route_dp import RoutePlan, best_route, refuel_candidates
from q1.config import Q1AlgorithmConfig
from q1.io.csv_validator import validate_q1_csv
from q1.io.csv_writer import ASSIGNMENT_COLUMNS, ROUTE_COLUMNS, write_flight_csv


@pytest.fixture(scope="module")
def distances():
    return load_distances().distances


@pytest.fixture(scope="module")
def real_groups():
    return group_q1(load_people_q1())


def _brute_force_best_time(base, spec, required, distances, stations):
    """穷举所有 ≤5 次海上着陆、覆盖 required 的停靠序列，返回最短用时。

    题面允许"飞机离开后再次返回同一设施"，故枚举的是可重复的停靠序列（只禁止
    连续两次停靠同一地点），而不是排列。
    """
    locations = sorted(set(required) | set(stations))
    best = None
    for length in range(len(required), MAX_OFFSHORE_LANDINGS + 1):
        for stops in itertools.product(locations, repeat=length):
            if not set(required) <= set(stops):
                continue
            if any(first == second for first, second in zip(stops, stops[1:])):
                continue
            for refuels in itertools.product(
                *[(False, True) if stop in REFUEL_FACILITIES else (False,) for stop in stops]
            ):
                route = (base, *stops, base)
                fuel = spec.tank_capacity_kg
                elapsed = 0
                feasible = True
                for index, (origin, destination) in enumerate(zip(route, route[1:])):
                    distance = distances[(origin, destination)]
                    fuel -= spec.fuel_consumption_kg_per_km * distance
                    if fuel < spec.reserve_fuel_kg - 1e-9:
                        feasible = False
                        break
                    elapsed += math.ceil(60 * distance / spec.speed_kmh)
                    stop_index = index + 1
                    if stop_index < len(route) - 1:
                        elapsed += 10
                        if refuels[stop_index - 1]:
                            elapsed += 10
                            fuel = spec.tank_capacity_kg
                if feasible and (best is None or elapsed < best):
                    best = elapsed
    return best


@pytest.mark.parametrize("facility", ["F001", "F013", "F042", "F050", "F009"])
@pytest.mark.parametrize("aircraft_type", ["T1", "T2", "T3"])
def test_route_dp_matches_brute_force_single_destination(facility, aircraft_type, distances):
    spec = AIRCRAFT_SPECS[aircraft_type]
    stations = refuel_candidates("A03", (facility,), distances, 4)
    plan = best_route("A03", spec, (facility,), distances, refuel_keep=4)
    reference = _brute_force_best_time("A03", spec, (facility,), distances, stations)
    assert (plan.aircraft_time if plan else None) == reference


def test_route_dp_inserts_refuel_after_the_last_delivery():
    """油量约束可能要求在最后一次投放之后才加油，DP 必须能找到这类航线。"""
    base, delivery, station = "A01", "F001", "F006"
    locations = {base, delivery, *REFUEL_FACILITIES}
    distances = {
        (origin, destination): (0.0 if origin == destination else 999.0)
        for origin in locations
        for destination in locations
    }
    distances.update(
        {
            (base, delivery): 200.0,
            (delivery, base): 200.0,
            (delivery, station): 100.0,
            (station, delivery): 100.0,
            (station, base): 100.0,
            (base, station): 100.0,
        }
    )
    plan = best_route(base, AIRCRAFT_SPECS["T1"], (delivery,), distances)
    assert plan is not None
    delivery_index = plan.route.index(delivery)
    assert any(
        index > delivery_index and plan.refuel_decisions[index]
        for index in range(len(plan.route))
    )


def test_refuel_keep_is_propagated(monkeypatch):
    seen = []

    def fake_best_route(*args, **kwargs):
        seen.append(kwargs["refuel_keep"])
        return None

    monkeypatch.setattr("q1.algorithms.clusters.best_route", fake_best_route)
    build_columns([("F001",)], {}, bases=("A01",), refuel_keep=8)
    assert seen == [8, 8, 8]

    seen.clear()
    monkeypatch.setattr("q1.algorithms.flight_builder.best_route", fake_best_route)
    groups = {"G": RequestGroup("G", ("P",), "LAND", "F001")}
    flight = Flight("A01", "T1", ("A01", "F001", "A01"), (False,) * 3, (("G", 1),))
    improve_flight(
        flight,
        groups,
        {("A01", "F001"): 1.0, ("F001", "A01"): 1.0},
        refuel_keep=8,
    )
    assert seen and set(seen) == {8}


def _test_column(name, *, time, capacity, arrival, fuel, distance=100.0):
    return RouteColumn(
        name,
        "A01",
        name,
        capacity,
        ("A01", "F001", "A01"),
        (False, False, False),
        time,
        distance,
        fuel,
        ("F001",),
        {"F001": 1},
        {"F001": arrival},
        {"F001": distance / 2},
    )


def test_pareto_filter_keeps_secondary_tradeoff():
    faster_arrival = _test_column("small", time=100, capacity=12, arrival=30, fuel=50)
    larger = _test_column("large", time=100, capacity=19, arrival=40, fuel=50)
    assert _pareto_filter([faster_arrival, larger]) == [faster_arrival, larger]


def test_pareto_filter_removes_strict_primary_dominance():
    dominant = _test_column("fast", time=99, capacity=19, arrival=50, fuel=100)
    dominated = _test_column("slow", time=100, capacity=12, arrival=20, fuel=10)
    assert _pareto_filter([dominant, dominated]) == [dominant]


def test_improve_flight_does_not_assume_smaller_ak_means_better_ratio(monkeypatch):
    groups = {"G": RequestGroup("G", ("P",), "LAND", "F001")}
    current = Flight("A01", "T3", ("A01", "F001", "A01"), (False,) * 3, (("G", 1),))

    def fake_route(base, spec, facilities, distances, **kwargs):
        return RoutePlan(
            base,
            spec.aircraft_type,
            (base, "F001", base),
            (False,) * 3,
            10,
            20,
            (0, 5, 10),
            (0, 10, 20),
        )

    def fake_metrics(flight, groups, distances):
        ak = 100.0 if flight.aircraft_type == "T3" else 50.0
        pk = 90.0 if flight.aircraft_type == "T3" else 10.0
        return FlightMetrics(10, 5, 2.0, pk, ak)

    monkeypatch.setattr("q1.algorithms.flight_builder.best_route", fake_route)
    monkeypatch.setattr("q1.algorithms.flight_builder.flight_metrics", fake_metrics)
    assert improve_flight(current, groups, {}) == current


def test_feedback_loop_feeds_improved_route_back_and_matches_metrics(distances):
    from q1.run_q1 import solve_realize_feedback

    groups = [RequestGroup("G", ("P",), "LAND", "F009")]
    groups_by_id = {group.group_id: group for group in groups}
    columns = number_columns(build_columns([("F009", "F030")], distances))
    config = Q1AlgorithmConfig(
        efficiency_slack=1.0,
        columns_per_group=20,
        secondary_time_limit_seconds=10,
        max_feedback_rounds=2,
    )
    result = solve_realize_feedback(
        groups, columns, groups_by_id, distances, config, workers=1,
        stages=("aircraft_time", "passenger_time", "fuel", "flights"),
    )
    assert result.columns_fed_back > 0
    assert result.solver_matches_delivery
    assert result.solution.aircraft_time == result.metrics.total_aircraft_time


def test_route_dp_plans_pass_the_shared_feasibility_core(distances):
    facilities = sorted({f"F{number:03d}" for number in range(1, 53)})
    generator = random.Random(20260815)
    checked = 0
    for _ in range(120):
        cluster = tuple(sorted(generator.sample(facilities, generator.randint(1, 4))))
        base = generator.choice(["A01", "A02", "A03"])
        aircraft_type = generator.choice(list(AIRCRAFT_SPECS))
        spec = AIRCRAFT_SPECS[aircraft_type]
        plan = best_route(base, spec, cluster, distances)
        if plan is None:
            continue
        checked += 1
        groups = {
            f"G{index}": RequestGroup(f"G{index}", ("P",), "LAND", facility)
            for index, facility in enumerate(cluster)
        }
        allocations = tuple(
            PassengerAllocation(f"G{index}", 1, 0, plan.route.index(facility))
            for index, facility in enumerate(cluster)
        )
        result = evaluate_sortie(
            base_airport=base,
            aircraft=spec,
            route=plan.route,
            refuel_decisions=plan.refuel_decisions,
            allocations=allocations,
            groups=groups,
            distances=distances,
        )
        assert result.feasible, (base, aircraft_type, cluster, result.violations)
        assert result.aircraft_time == plan.aircraft_time
    assert checked >= 60


def test_flow_master_matches_explicit_set_partitioning(distances):
    """流模型与"航线×人员配置"集合划分模型的最优主目标必须一致。"""
    groups = [
        RequestGroup("G1", tuple(f"P{i}" for i in range(7)), "LAND", "F009"),
        RequestGroup("G2", tuple(f"Q{i}" for i in range(5)), "LAND", "F017"),
    ]
    clusters = [("F009",), ("F017",), ("F009", "F017")]
    columns = number_columns(build_columns(clusters, distances))
    master = FlowMaster(groups, columns)
    flow = master.solve(time_limit_seconds=30, stages=("aircraft_time",), workers=1)

    from ortools.sat.python import cp_model

    patterns = []
    for column in columns:
        servable = [g for g in groups if g.destination_id in column.cluster]
        for combination in itertools.product(*[range(g.quantity + 1) for g in servable]):
            if 0 < sum(combination) <= column.capacity:
                patterns.append(
                    (column.aircraft_time, dict(zip((g.group_id for g in servable), combination)))
                )
    model = cp_model.CpModel()
    variables = [model.new_int_var(0, 12, "") for _ in patterns]
    for group in groups:
        model.add(
            sum(
                pattern.get(group.group_id, 0) * variable
                for (_, pattern), variable in zip(patterns, variables)
            )
            == group.quantity
        )
    model.minimize(sum(cost * v for (cost, _), v in zip(patterns, variables)))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 30
    assert solver.status_name(solver.solve(model)) == "OPTIMAL"
    assert flow.aircraft_time == int(solver.objective_value)
    assert flow.stages[0].certified_optimal


def test_column_service_set_includes_refuel_stops(distances):
    """航线在加油站着陆时也能投放人员，候选列必须体现这一点。"""
    columns = build_columns([("F042",)], distances, bases=("A03",))
    assert columns
    with_refuel = [c for c in columns if any(c.refuel_decisions)]
    assert with_refuel
    for column in with_refuel:
        assert set(column.cluster) == set(column.route[1:-1])


def test_selection_keeps_full_group_coverage(real_groups, distances):
    facilities = sorted({group.destination_id for group in real_groups})
    clusters = enumerate_clusters(facilities, distances, {2: 6, 3: 5})
    columns = number_columns(build_columns(clusters, distances))
    pool = select_columns(columns, real_groups, efficiency_slack=0.05, per_group=3)
    assert len(pool) < len(columns)
    # 构造函数在任一请求组无列可服务时会抛错，因此能构造即说明覆盖完整。
    FlowMaster(real_groups, pool)


def test_split_flows_conserves_demand_and_respects_capacity(distances):
    groups = [
        RequestGroup("G1", tuple(f"P{i}" for i in range(25)), "LAND", "F009"),
        RequestGroup("G2", tuple(f"Q{i}" for i in range(11)), "LAND", "F017"),
    ]
    columns = number_columns(build_columns([("F009", "F017")], distances))
    master = FlowMaster(groups, columns)
    solution = master.solve(time_limit_seconds=30, stages=("aircraft_time",), workers=1)
    index = {column.column_id: column for column in master.columns}
    groups_by_id = {group.group_id: group for group in groups}
    flights = split_flows(index, solution.multiplicities, solution.flows, groups_by_id)
    delivered = {"G1": 0, "G2": 0}
    for flight in flights:
        assert flight.passengers <= AIRCRAFT_SPECS[flight.aircraft_type].capacity
        for group_id, quantity in flight.load:
            delivered[group_id] += quantity
    assert delivered == {"G1": 25, "G2": 11}
    assert len(flights) == solution.flights


def test_improve_flight_never_worsens_and_can_shrink(distances):
    groups = {
        "G1": RequestGroup("G1", ("P1",), "LAND", "F009"),
        "G2": RequestGroup("G2", ("P2",), "LAND", "F030"),
    }
    plan = best_route("A01", AIRCRAFT_SPECS["T3"], ("F009", "F030"), distances)
    wasteful = Flight(
        base_airport="A01",
        aircraft_type="T3",
        route=plan.route,
        refuel_decisions=plan.refuel_decisions,
        load=(("G1", 1),),
    )
    improved = improve_flight(wasteful, groups, distances)
    before = flight_metrics(wasteful, groups, distances)
    after = flight_metrics(improved, groups, distances)
    assert after.aircraft_time < before.aircraft_time
    assert set(improved.route[1:-1]) >= {"F009"}
    assert improved.load == wasteful.load


def test_greedy_covers_every_group(real_groups, distances):
    facilities = sorted({group.destination_id for group in real_groups})
    clusters = enumerate_clusters(facilities, distances, {2: 5})
    columns = number_columns(build_columns(clusters, distances))
    master = FlowMaster(real_groups, columns)
    solution = greedy_solution(master)
    served = {group.group_id: 0 for group in real_groups}
    for (group_id, _), quantity in solution.flows.items():
        served[group_id] += quantity
    assert served == {group.group_id: group.quantity for group in real_groups}


def test_expand_clusters_stays_within_the_landing_limit(distances):
    facilities = sorted({f"F{number:03d}" for number in range(1, 53)})
    expanded = expand_clusters(
        [("F009", "F017", "F030"), ("F001", "F005")], distances, facilities
    )
    assert expanded
    assert all(1 <= len(cluster) <= MAX_OFFSHORE_LANDINGS for cluster in expanded)
    assert all(len(set(cluster)) == len(cluster) for cluster in expanded)


def test_csv_schema_and_independent_validator(tmp_path, distances):
    people = pd.DataFrame(
        [
            {"person_id": "P2", "origin_id": "LAND", "destination_id": "F009"},
            {"person_id": "P1", "origin_id": "A01", "destination_id": "F009"},
        ]
    )
    groups = [
        RequestGroup("G1", ("P2",), "LAND", "F009"),
        RequestGroup("G2", ("P1",), "A01", "F009"),
    ]
    plan = best_route("A01", AIRCRAFT_SPECS["T2"], ("F009",), distances)
    flight = Flight("A01", "T2", plan.route, plan.refuel_decisions, (("G1", 1), ("G2", 1)))
    assignments = assign_people([flight], groups)
    routes_path, assignments_path = write_flight_csv(
        output_dir=tmp_path, people=people, flights=[flight], assignments=assignments
    )
    assert list(pd.read_csv(routes_path).columns) == ROUTE_COLUMNS
    assert list(pd.read_csv(assignments_path).columns) == ASSIGNMENT_COLUMNS
    report = validate_q1_csv(routes_path, assignments_path, people, distances)
    assert report.passed, report.violations
    assert report.assignment_rows == 2
    assert report.missing == report.duplicates == 0
    metrics = aggregate([flight], {g.group_id: g for g in groups}, distances)
    assert report.metrics.total_aircraft_time == metrics.total_aircraft_time
    assert report.metrics.total_passenger_time == metrics.total_passenger_time
