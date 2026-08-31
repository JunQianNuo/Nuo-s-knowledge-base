"""对代表性 1~5 设施簇比较 refuel_keep=4 与 8。"""

from __future__ import annotations

from common.config import AIRCRAFT_SPECS
from common.data_loader import load_distances
from q1.algorithms.route_dp import best_route

CLUSTERS = (
    ("F042",),
    ("F009", "F017"),
    ("F009", "F017", "F030"),
    ("F006", "F009", "F017", "F030"),
    ("F006", "F009", "F017", "F030", "F042"),
)


def main() -> int:
    distances = load_distances().distances
    improved = 0
    newly_feasible = 0
    print("size,base,aircraft,keep4,keep8,result")
    for cluster in CLUSTERS:
        for base in ("A01", "A02", "A03"):
            for aircraft_type, spec in AIRCRAFT_SPECS.items():
                plan4 = best_route(base, spec, cluster, distances, refuel_keep=4)
                plan8 = best_route(base, spec, cluster, distances, refuel_keep=8)
                time4 = plan4.aircraft_time if plan4 else None
                time8 = plan8.aircraft_time if plan8 else None
                result = "same"
                if plan4 is None and plan8 is not None:
                    result = "new-feasible"
                    newly_feasible += 1
                elif time8 is not None and time4 is not None and time8 < time4:
                    result = "improved"
                    improved += 1
                print(
                    f"{len(cluster)},{base},{aircraft_type},{time4},{time8},{result}"
                )
    print(f"summary: improved={improved}, newly_feasible={newly_feasible}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
