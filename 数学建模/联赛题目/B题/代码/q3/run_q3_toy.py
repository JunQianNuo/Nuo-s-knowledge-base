from __future__ import annotations

import tempfile
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from common.config import AIRPORTS, OFFSHORE_FACILITIES
from q3.algorithms.timed_pool import TimedColumn, propagate_timed_column, turnaround_compatible
from q3.io.csv_validator import validate_q3_csv
from q3.io.csv_writer import write_q3_csv


@dataclass(frozen=True)
class ToyFlight:
    aircraft_id: str
    column: TimedColumn


@dataclass(frozen=True)
class ToyAssignment:
    person_id: str
    aircraft_id: str
    flight_no: int
    pickup_stop_order: int
    delivery_stop_order: int


def _toy_data():
    people = []
    for i in range(12):
        people.append(
            (f"O{i:02d}", "LAND", "F001", "2026-08-03 06:00", "2026-08-03 08:00", "shift")
        )
    for i in range(11):
        people.append(
            (f"S{i:02d}", "F001", "F002", "2026-08-03 06:00", "2026-08-03 09:00", "shift")
        )
    people.extend(
        [
            ("R00", "F001", "LAND", "2026-08-03 06:00", "2026-08-03 10:00", "production"),
            ("E00", "LAND", "F003", "2026-08-03 07:00", "2026-08-03 11:00", "emergency"),
            ("T00", "LAND", "F003", "2026-08-03 07:00", "2026-08-03 11:00", "temporary"),
        ]
    )
    frame = pd.DataFrame(
        people,
        columns=[
            "person_id",
            "origin_id",
            "destination_id",
            "earliest_pickup_time",
            "latest_arrival_time",
            "task_type",
        ],
    )
    locations = sorted(AIRPORTS | OFFSHORE_FACILITIES)
    matrix = pd.DataFrame(
        [
            [origin, *(0.0 if origin == destination else 20.0 for destination in locations)]
            for origin in locations
        ],
        columns=["from_id", *locations],
    )
    distances = {
        (origin, destination): 0.0 if origin == destination else 20.0
        for origin in locations
        for destination in locations
    }
    return frame, matrix, distances


def main() -> int:
    people, matrix, distances = _toy_data()
    first = propagate_timed_column(
        column_id="TOY1",
        day=0,
        base_airport="A01",
        aircraft_type="T1",
        route=("A01", "F001", "F002", "A01"),
        refuel_decisions=(False, False, False, False),
        start_minute=360,
        distances=distances,
    )
    second = propagate_timed_column(
        column_id="TOY2",
        day=0,
        base_airport="A01",
        aircraft_type="T1",
        route=("A01", "F003", "A01"),
        refuel_decisions=(False, False, False),
        start_minute=first.return_time + 30,
        distances=distances,
    )
    assert turnaround_compatible(first, second)
    aircraft_id = "A01-T1-H01"
    flights = [ToyFlight(aircraft_id, first), ToyFlight(aircraft_id, second)]
    assignments = [
        *(ToyAssignment(f"O{i:02d}", aircraft_id, 1, 0, 1) for i in range(12)),
        *(ToyAssignment(f"S{i:02d}", aircraft_id, 1, 1, 2) for i in range(11)),
        ToyAssignment("R00", aircraft_id, 1, 1, 3),
        ToyAssignment("E00", aircraft_id, 2, 0, 1),
    ]
    with tempfile.TemporaryDirectory(prefix="q3-toy-") as directory:
        root = Path(directory)
        people_path, distance_path = root / "peopleQ3.csv", root / "distances.csv"
        people.to_csv(people_path, index=False)
        matrix.to_csv(distance_path, index=False)
        routes_path, assignments_path = write_q3_csv(root, people, flights, assignments)
        report = validate_q3_csv(
            routes_path=routes_path,
            assignments_path=assignments_path,
            people_path=people_path,
            distances_path=distance_path,
        )
    if not report.valid:
        raise RuntimeError("toy validator failed: " + "; ".join(report.violations))
    assert report.metrics.mandatory_served == 25
    assert report.metrics.temporary_served == 0
    print("Q3 toy PASS: 1 aircraft, 2 flights, exact 30-minute turnaround")
    print("outbound + return + shuttle, time windows, blank temporary, same-stop reuse PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
