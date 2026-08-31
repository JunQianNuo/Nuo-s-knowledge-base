"""Offline consistency check for the frozen support-material snapshots.

No official input data or OR-Tools is required.  The script verifies that the
submitted CSV/JSON snapshots agree with the numerical claims used in the paper.
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def n_flights(frame: pd.DataFrame, cols: list[str]) -> int:
    return int(frame[cols].drop_duplicates().shape[0])


def main() -> int:
    q1 = load_json(ROOT / "q1/outputs/q1-summary.json")
    q1a = pd.read_csv(ROOT / "q1/outputs/q1-assignments.csv")
    q1r = pd.read_csv(ROOT / "q1/outputs/q1-routes.csv")
    assert len(q1a) == 1600
    assert n_flights(q1r, ["aircraft_type", "flight_no"]) == 88
    assert (q1["T_air"], q1["T_pax"], q1["flights"]) == (14759, 126288, 88)
    assert q1["validator"]["independent_csv"] == "PASS"

    q1s = pd.read_csv(ROOT / "q1/outputs/sensitivity/sensitivity_q1.csv")
    assert set(q1s["refuel_keep"]) == {4, 8}
    assert set(q1s["validator"]) == {"PASS"}

    q2 = load_json(ROOT / "q2/outputs/q2-summary.json")
    q2a = pd.read_csv(ROOT / "q2/outputs/q2-assignments.csv")
    q2r = pd.read_csv(ROOT / "q2/outputs/q2-routes.csv")
    assert len(q2a) == 4000
    assert n_flights(q2r, ["aircraft_type", "flight_no"]) == 111
    assert (q2["joint_solution"]["T_air"], q2["joint_solution"]["T_pax"]) == (18963, 241751)
    assert q2["validation"]["independent_csv"] is True
    br = pd.read_csv(ROOT / "q2/outputs/q2-tpax-aggregate.csv")
    expected_q2 = {
        "outbound": (1600, 114303, 111638, 2665),
        "return": (1600, 115939, 107816, 8123),
        "shuttle": (800, 11509, 11935, -426),
    }
    for row in br.itertuples(index=False):
        assert expected_q2[str(row.category)] == (
            int(row.count), int(row.joint_T_pax), int(row.baseline_T_pax), int(row.delta)
        )
    assert int(br["joint_T_pax"].sum()) == 241751
    assert int(br["baseline_T_pax"].sum()) == 231389
    assert int(br["delta"].sum()) == 10362
    detour = pd.read_csv(ROOT / "q2/outputs/q2-detour-summary.csv").iloc[0]
    assert int(detour["detour_persons"]) == 662 and int(detour["total_persons"]) == 4000

    a = load_json(ROOT / "q3/outputs/formal_stage_a_summary.json")
    b = load_json(ROOT / "q3/outputs/formal_stage_b_summary.json")
    c = load_json(ROOT / "q3/outputs/q3-summary.json")
    q3a = pd.read_csv(ROOT / "q3/outputs/q3-assignments.csv")
    q3r = pd.read_csv(ROOT / "q3/outputs/q3-routes.csv")
    assert len(q3a) == 4000
    assert n_flights(q3r, ["aircraft_id", "flight_no"]) == 204
    assert a["mandatory_served"] == a["mandatory_total"] == 3840
    assert a["T_air"] == 35114
    assert b["temporary_served"] == b["temporary_total"] == 160
    assert b["status"] == "OPTIMAL"
    assert b["temporary_incumbent"] == b["temporary_best_bound"] == 160
    assert b["temporary_gap"] == 0 and b["temporary_certified_optimal"] is True
    assert (c["T_air"], c["T_pax"], c["flights"], c["aircraft_used"]) == (34033, 246808, 204, 22)
    assert c["final_solution_source"] == "C4 incumbent"
    assert c["full_certified"] is False

    temp = load_json(ROOT / "q3/outputs/temporary_bottleneck_summary.json")
    assert temp["all_temporary_count"] == temp["all_temporary_served_count"] == 160
    assert temp["all_temporary_unserved_count"] == 0
    assert temp["all_temporary_aircraft_type_distribution"] == {"T1": 27, "T2": 99, "T3": 62}
    assert temp["all_temporary_compatible_airport_distribution"] == {"A01": 93, "A02": 58, "A03": 45}

    q3s = pd.read_csv(ROOT / "q3/outputs/sensitivity/time_density_sensitivity.csv")
    assert set(q3s["time_sampling_density"]) == {"baseline", "dense"}
    assert set(q3s["validator"]) == {"PASS"}

    print("PASS: frozen support snapshots are internally consistent with paper claims.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
