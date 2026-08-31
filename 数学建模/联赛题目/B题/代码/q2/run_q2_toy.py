from __future__ import annotations

import tempfile
import time
from pathlib import Path

import pandas as pd

from common.config import AIRCRAFT_SPECS, AIRPORTS, OFFSHORE_FACILITIES
from common.grouping import group_q2
from q2.algorithms.master import RouteFlowMaster
from q2.algorithms.realize import realize_solution
from q2.algorithms.route_pool import _make_physical, service_options
from q2.io.csv_validator import validate_q2_csv
from q2.io.csv_writer import write_q2_csv


def main() -> int:
    people = pd.DataFrame(
        [
            ("P1", "LAND", "F001"),
            ("P2", "LAND", "F001"),
            ("P3", "F001", "F002"),
            ("P4", "F002", "LAND"),
        ],
        columns=["person_id", "origin_id", "destination_id"],
    )
    locations = sorted(AIRPORTS | OFFSHORE_FACILITIES)
    distances = {(a, b): (0.0 if a == b else 20.0) for a in locations for b in locations}
    route = _make_physical("A01", AIRCRAFT_SPECS["T1"], ("F001", "F002"), (False, False), distances)
    assert route is not None
    groups = group_q2(people)
    options = [option for group in groups for option in service_options(group, route)]
    options = [
        type(o)(
            o.option_id,
            o.group_id,
            o.route_id,
            o.pickup,
            o.delivery,
            o.passenger_time,
            20.0 * (o.delivery - o.pickup),
        )
        for o in options
    ]
    master = RouteFlowMaster(groups, [route], options)
    solution = master.solve(deadline=time.perf_counter() + 20, workers=1)
    assert solution.status == "OPTIMAL" and solution.full_certified
    flights, assignments = realize_solution(groups, [route], options, solution)
    with tempfile.TemporaryDirectory(prefix="q2-toy-") as directory:
        routes_path, assignments_path = write_q2_csv(Path(directory), people, flights, assignments)
        report = validate_q2_csv(
            routes_path=routes_path,
            assignments_path=assignments_path,
            people=people,
            distances=distances,
        )
    if not report.valid:
        raise RuntimeError("toy validator failed: " + "; ".join(report.violations))
    print(
        f"toy OPTIMAL: T_air={report.metrics.total_aircraft_time}, "
        f"flights={report.metrics.number_of_flights}, "
        f"utilization={report.metrics.seat_utilization:.6f}"
    )
    print("toy validator PASS; same-stop seat reuse and dynamic capacity verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
