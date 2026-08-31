from __future__ import annotations

from pathlib import Path

import pandas as pd

from q3.config import minute_to_datetime

ASSIGNMENT_COLUMNS = [
    "person_id",
    "aircraft_id",
    "flight_no",
    "pickup_stop_order",
    "delivery_stop_order",
]
ROUTE_COLUMNS = [
    "aircraft_id",
    "flight_no",
    "stop_order",
    "facility_id",
    "arrival_time",
    "departure_time",
    "refuel",
]


def _format_time(value: int | None) -> str:
    return "" if value is None else minute_to_datetime(value).strftime("%Y-%m-%d %H:%M")


def write_q3_csv(output_dir: Path, people: pd.DataFrame, flights, assignments):
    output_dir.mkdir(parents=True, exist_ok=True)
    ordered = sorted(flights, key=lambda item: (item.aircraft_id, item.column.departure_time))
    numbers: dict[str, int] = {}
    route_rows = []
    for flight in ordered:
        count = numbers.get(flight.aircraft_id, 0) + 1
        numbers[flight.aircraft_id] = count
        column = flight.column
        last = len(column.route) - 1
        for stop, location in enumerate(column.route):
            route_rows.append(
                {
                    "aircraft_id": flight.aircraft_id,
                    "flight_no": count,
                    "stop_order": stop,
                    "facility_id": location,
                    "arrival_time": _format_time(None if stop == 0 else column.arrival_times[stop]),
                    "departure_time": _format_time(
                        None if stop == last else column.departure_times[stop]
                    ),
                    "refuel": int(column.refuel_decisions[stop]),
                }
            )
    indexed = {item.person_id: item for item in assignments}
    rows = []
    for person in people["person_id"].astype(str):
        assignment = indexed.get(person)
        if assignment is None:
            rows.append(
                {name: person if name == "person_id" else "" for name in ASSIGNMENT_COLUMNS}
            )
            continue
        rows.append(
            {
                "person_id": person,
                "aircraft_id": assignment.aircraft_id,
                "flight_no": assignment.flight_no,
                "pickup_stop_order": assignment.pickup_stop_order,
                "delivery_stop_order": assignment.delivery_stop_order,
            }
        )
    routes_path = output_dir / "q3-routes.csv"
    assignments_path = output_dir / "q3-assignments.csv"
    pd.DataFrame(route_rows, columns=ROUTE_COLUMNS).to_csv(routes_path, index=False)
    pd.DataFrame(rows, columns=ASSIGNMENT_COLUMNS).to_csv(assignments_path, index=False)
    return routes_path, assignments_path
