from __future__ import annotations

from dataclasses import replace

from common.feasibility import evaluate_sortie, leg_flight_minutes
from common.models import AircraftSpec, PassengerAllocation, RequestGroup

AIRCRAFT = AircraftSpec("TX", 2, 100, 1.0, 100, 10)
DISTANCES = {
    (origin, destination): distance
    for origin, destination, distance in [
        ("A01", "F001", 20),
        ("F001", "A01", 20),
        ("A01", "F002", 20),
        ("F002", "A01", 20),
        ("F001", "F002", 10),
        ("F002", "F001", 10),
        ("F002", "F006", 20),
        ("F006", "A01", 70),
        ("A01", "F006", 70),
        ("F006", "F002", 20),
    ]
}


def group(group_id="G1", origin="LAND", destination="F001", quantity=2):
    return RequestGroup(group_id, tuple(f"P{i}" for i in range(quantity)), origin, destination)


def run(route, allocations, groups, refuels=None, aircraft=AIRCRAFT):
    return evaluate_sortie(
        base_airport="A01",
        aircraft=aircraft,
        route=route,
        refuel_decisions=refuels or tuple(False for _ in route),
        allocations=allocations,
        groups={item.group_id: item for item in groups},
        distances=DISTANCES,
    )


def test_legal_closed_route_and_per_leg_ceil() -> None:
    result = run(("A01", "F001", "A01"), (PassengerAllocation("G1", 2, 0, 1),), [group()])
    assert result.feasible
    assert result.aircraft_time == 12 + 10 + 12
    assert leg_flight_minutes(1, 90) == 1
    assert leg_flight_minutes(2, 90) == 2


def test_wrong_return_and_more_than_five_landings() -> None:
    wrong = run(("A01", "F001", "A02"), (), [])
    assert not wrong.feasible
    long_route = ("A01", "F001", "F002", "F001", "F002", "F001", "F002", "A01")
    assert any("着陆次数" in item for item in run(long_route, (), []).violations)


def test_pickup_delivery_and_first_arrival() -> None:
    request = group()
    invalid_order = run(
        ("A01", "F001", "A01"),
        (PassengerAllocation("G1", 1, 1, 1),),
        [request],
    )
    assert any("pickup < delivery" in item for item in invalid_order.violations)
    repeated = run(
        ("A01", "F001", "F002", "F001", "A01"),
        (PassengerAllocation("G1", 1, 0, 3),),
        [request],
    )
    assert any("首次到达" in item for item in repeated.violations)


def test_capacity_and_same_stop_seat_reuse() -> None:
    too_many = run(
        ("A01", "F001", "A01"),
        (PassengerAllocation("G1", 3, 0, 1),),
        [group(quantity=3)],
    )
    assert any("超容量" in item for item in too_many.violations)
    groups = [group("OUT", "LAND", "F001"), group("BACK", "F001", "LAND")]
    reuse = run(
        ("A01", "F001", "A01"),
        (PassengerAllocation("OUT", 2, 0, 1), PassengerAllocation("BACK", 2, 1, 2)),
        groups,
    )
    assert reuse.feasible
    assert reuse.leg_loads == (2, 2)


def test_fuel_reserve_illegal_and_legal_refuel() -> None:
    low_fuel = run(("A01", "F006", "A01"), (), [], aircraft=AIRCRAFT)
    assert any("安全余油" in item for item in low_fuel.violations)
    illegal = run(("A01", "F002", "A01"), (), [], refuels=(False, True, False))
    assert any("合法加油设施" in item for item in illegal.violations)
    legal = run(
        ("A01", "F006", "F002", "A01"),
        (),
        [],
        refuels=(False, True, False, False),
    )
    assert legal.feasible
    assert legal.arrival_fuel == (30, 80, 60)


def test_reserve_checked_at_every_arrival() -> None:
    strict = replace(AIRCRAFT, reserve_fuel_kg=31)
    result = run(("A01", "F006", "F002", "A01"), (), [], (False, True, False, False), strict)
    assert not result.feasible
