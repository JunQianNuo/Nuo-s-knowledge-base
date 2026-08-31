from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from common.models import PersonAssignment

ROUTE_COLUMNS = ["aircraft_type", "flight_no", "stop_order", "facility_id", "refuel"]
ASSIGNMENT_COLUMNS = [
    "person_id",
    "aircraft_type",
    "flight_no",
    "pickup_stop_order",
    "delivery_stop_order",
]


def write_flight_csv(
    *,
    output_dir: Path,
    people: pd.DataFrame,
    flights,
    assignments: list[PersonAssignment],
) -> tuple[Path, Path]:
    """按官方模板写出 q1-routes.csv / q1-assignments.csv。

    `flights` 的枚举顺序必须与生成 `assignments` 时完全一致，否则 flight_no 会错位。
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    counters: dict[str, int] = {}
    route_rows = []
    for flight in flights:
        counters[flight.aircraft_type] = counters.get(flight.aircraft_type, 0) + 1
        flight_no = counters[flight.aircraft_type]
        for stop_order, (facility_id, refuel) in enumerate(
            zip(flight.route, flight.refuel_decisions)
        ):
            route_rows.append(
                {
                    "aircraft_type": flight.aircraft_type,
                    "flight_no": flight_no,
                    "stop_order": stop_order,
                    "facility_id": facility_id,
                    "refuel": int(refuel),
                }
            )
    routes_path = output_dir / "q1-routes.csv"
    pd.DataFrame(route_rows, columns=ROUTE_COLUMNS).to_csv(routes_path, index=False)

    assignment_index = {row.person_id: row for row in assignments}
    assignment_rows = [
        {
            "person_id": person_id,
            "aircraft_type": assignment_index[person_id].aircraft_type,
            "flight_no": assignment_index[person_id].flight_no,
            "pickup_stop_order": assignment_index[person_id].pickup_stop_order,
            "delivery_stop_order": assignment_index[person_id].delivery_stop_order,
        }
        for person_id in people["person_id"].astype(str)
    ]
    assignments_path = output_dir / "q1-assignments.csv"
    pd.DataFrame(assignment_rows, columns=ASSIGNMENT_COLUMNS).to_csv(assignments_path, index=False)
    return routes_path, assignments_path


def write_flight_plan(path: Path, flights, groups) -> None:
    """写出架次级明细，便于论文分析与人工抽查。"""
    rows = []
    counters: dict[str, int] = {}
    for flight in flights:
        counters[flight.aircraft_type] = counters.get(flight.aircraft_type, 0) + 1
        rows.append(
            {
                "aircraft_type": flight.aircraft_type,
                "flight_no": counters[flight.aircraft_type],
                "base_airport": flight.base_airport,
                "route": "|".join(flight.route),
                "refuel_stops": "|".join(
                    location
                    for location, refuel in zip(flight.route, flight.refuel_decisions)
                    if refuel
                ),
                "offshore_landings": len(flight.route) - 2,
                "passengers": flight.passengers,
                "load": "|".join(
                    f"{group_id}:{quantity}:{groups[group_id].destination_id}"
                    for group_id, quantity in flight.load
                ),
            }
        )
    pd.DataFrame(rows).to_csv(path, index=False)


def write_summary(path: Path, summary: dict[str, object]) -> None:
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
