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


def write_q2_csv(
    output_dir: Path, people: pd.DataFrame, flights, assignments: list[PersonAssignment]
):
    output_dir.mkdir(parents=True, exist_ok=True)
    counters: dict[str, int] = {}
    route_rows, plan_rows = [], []
    for flight in flights:
        counters[flight.aircraft_type] = counters.get(flight.aircraft_type, 0) + 1
        number = counters[flight.aircraft_type]
        for stop, (location, refuel) in enumerate(zip(flight.route, flight.refuel_decisions)):
            route_rows.append(
                {
                    "aircraft_type": flight.aircraft_type,
                    "flight_no": number,
                    "stop_order": stop,
                    "facility_id": location,
                    "refuel": int(refuel),
                }
            )
        plan_rows.append(
            {
                "aircraft_type": flight.aircraft_type,
                "flight_no": number,
                "route_id": flight.route_id,
                "base_airport": flight.base_airport,
                "passengers": len(flight.passengers),
                "route": "->".join(flight.route),
            }
        )
    routes_path = output_dir / "q2-routes.csv"
    pd.DataFrame(route_rows, columns=ROUTE_COLUMNS).to_csv(routes_path, index=False)
    indexed = {row.person_id: row for row in assignments}
    missing = [person for person in people["person_id"].astype(str) if person not in indexed]
    if missing:
        raise RuntimeError(f"写出前发现缺失人员: {missing[:5]}")
    rows = [
        {
            "person_id": person,
            "aircraft_type": indexed[person].aircraft_type,
            "flight_no": indexed[person].flight_no,
            "pickup_stop_order": indexed[person].pickup_stop_order,
            "delivery_stop_order": indexed[person].delivery_stop_order,
        }
        for person in people["person_id"].astype(str)
    ]
    assignments_path = output_dir / "q2-assignments.csv"
    pd.DataFrame(rows, columns=ASSIGNMENT_COLUMNS).to_csv(assignments_path, index=False)
    pd.DataFrame(plan_rows).to_csv(output_dir / "q2-flight-plan.csv", index=False)
    return routes_path, assignments_path


def write_json(path: Path, payload: dict):
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
