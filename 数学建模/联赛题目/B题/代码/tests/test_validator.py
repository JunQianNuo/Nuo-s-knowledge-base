from __future__ import annotations

from common.models import PassengerAllocation, PersonAssignment, RequestGroup, SortieColumn
from common.validator import validate_solution


def fixture_data():
    from common.config import AIRCRAFT_SPECS
    from common.feasibility import evaluate_sortie

    group = RequestGroup("G1", ("P1", "P2"), "LAND", "F001")
    distances = {("A01", "F001"): 20.0, ("F001", "A01"): 20.0}
    allocation = PassengerAllocation("G1", 2, 0, 1)
    result = evaluate_sortie(
        base_airport="A01",
        aircraft=AIRCRAFT_SPECS["T3"],
        route=("A01", "F001", "A01"),
        refuel_decisions=(False, False, False),
        allocations=(allocation,),
        groups={"G1": group},
        distances=distances,
    )
    column = SortieColumn(
        "C1",
        "A01",
        "T3",
        ("A01", "F001", "A01"),
        (False, False, False),
        (allocation,),
        result.aircraft_time,
        result.passenger_time,
        result.fuel_used,
        result.passenger_km,
        result.available_seat_km,
    )
    assignments = [PersonAssignment(person, "T3", 1, 0, 1, "C1") for person in group.person_ids]
    return group, column, assignments, distances, AIRCRAFT_SPECS


def test_valid_solution() -> None:
    group, column, assignments, distances, specs = fixture_data()
    report = validate_solution(
        groups=[group],
        columns=[column],
        multiplicities={"C1": 1},
        aircraft_specs=specs,
        distances=distances,
        assignments=assignments,
    )
    assert report.passed
    assert str(report) == "PASS"


def test_duplicate_missing_and_illegal_route() -> None:
    group, column, assignments, distances, specs = fixture_data()
    bad_assignments = [assignments[0], assignments[0]]
    report = validate_solution(
        groups=[group],
        columns=[column],
        multiplicities={"C1": 1},
        aircraft_specs=specs,
        distances=distances,
        assignments=bad_assignments,
    )
    assert not report.passed
    assert "重复人员" in str(report)
    assert "遗漏人员" in str(report)
    bad_column = SortieColumn(**{**column.__dict__, "route": ("A01", "F001", "A02")})
    bad = validate_solution(
        groups=[group],
        columns=[bad_column],
        multiplicities={"C1": 1},
        aircraft_specs=specs,
        distances=distances,
    )
    assert "返回同一机场" in str(bad)
