from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from common.models import RequestGroup
from q2.algorithms.realize import decompose_intervals
from q3.algorithms.master import StageASolution
from q3.algorithms.timed_pool import ServiceOption, TimedColumn


@dataclass(frozen=True)
class RealizedFlight:
    aircraft_id: str
    column: TimedColumn
    passengers: tuple[tuple[str, int, int], ...]


@dataclass(frozen=True)
class Q3Assignment:
    person_id: str
    aircraft_id: str
    flight_no: int
    pickup_stop_order: int
    delivery_stop_order: int


def realize_stage_a(
    groups: Sequence[RequestGroup],
    columns: Sequence[TimedColumn],
    options: Sequence[ServiceOption],
    solution: StageASolution,
    optional_group_ids=(),
):
    optional_group_ids = frozenset(optional_group_ids)
    groups_by_id = {g.group_id: g for g in groups}
    columns_by_id = {r.column_id: r for r in columns}
    options_by_id = {o.option_id: o for o in options}
    cursor = {g.group_id: 0 for g in groups}
    intervals = {}
    for option_id, quantity in sorted(solution.flows.items()):
        option = options_by_id[option_id]
        group = groups_by_id[option.group_id]
        start = cursor[group.group_id]
        people = group.person_ids[start : start + quantity]
        if len(people) != quantity:
            raise RuntimeError(f"请求组 {group.group_id} 人员回填越界")
        cursor[group.group_id] += quantity
        intervals.setdefault(option.column_id, []).extend(
            (person, option.pickup, option.delivery) for person in people
        )
    if any(
        cursor[g.group_id] != g.quantity for g in groups if g.group_id not in optional_group_ids
    ):
        raise RuntimeError("mandatory 人员流未完整回填")
    flights = []
    for column_id, aircraft_ids in sorted(solution.aircraft_by_column.items()):
        column = columns_by_id[column_id]
        partitions = decompose_intervals(
            intervals.get(column_id, ()), len(aircraft_ids), column.capacity
        )
        if len(partitions) != len(aircraft_ids):
            raise RuntimeError("selected aircraft count != timed route copies")
        flights.extend(
            RealizedFlight(aircraft_id, column, tuple(partition))
            for aircraft_id, partition in zip(sorted(aircraft_ids), partitions)
        )
    number_by_flight = {}
    for aircraft_id in sorted({flight.aircraft_id for flight in flights}):
        ordered = sorted(
            (flight for flight in flights if flight.aircraft_id == aircraft_id),
            key=lambda item: item.column.departure_time,
        )
        number_by_flight.update((id(flight), number) for number, flight in enumerate(ordered, 1))
    assignments = [
        Q3Assignment(person, flight.aircraft_id, number_by_flight[id(flight)], pickup, delivery)
        for flight in flights
        for person, pickup, delivery in flight.passengers
    ]
    return flights, assignments
