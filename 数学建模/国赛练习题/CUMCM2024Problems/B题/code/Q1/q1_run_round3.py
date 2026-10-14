"""Approved Q1 round3: dense theta evidence for B1 versus M1."""
import argparse
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import platform
import time
import tracemalloc
import traceback

import numpy as np

import q1_run as core
import q1_run_round2 as round2


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "results/Q1/experiments/round3"
TOL = 1e-10
GRID_STEP = 0.001
GRID_COUNT = 1001


def dense_theta_grid():
    return [round(index * GRID_STEP, 12) for index in range(GRID_COUNT)]


def validate_adjustment(records):
    verdicts = [row for row in records
                if row.get("decision_type") == "result_verdict"]
    if not verdicts:
        raise ValueError("Missing human result adjustment")
    decision = verdicts[-1]
    required = {
        "decision_id": "q1_final_result_verdict",
        "status": "DECIDED",
        "decided_by": "human",
        "choice": "adjust_expand_theta_grid",
        "round_action": "adjust",
    }
    if (any(decision.get(key) != value for key, value in required.items())
            or not decision.get("rationale", "").strip()):
        raise ValueError("Current human result adjustment is missing or changed")
    return decision


def load_inputs(root):
    screened = round2.load_inputs(root)
    ledger_ref = "methods/Q1/q1_decisions.jsonl"
    records = [json.loads(line) for line in
               (root / ledger_ref).read_text(encoding="utf-8").splitlines()
               if line.strip()]
    adjustment = validate_adjustment(records)

    round2_summary_ref = "results/Q1/experiments/round2/run_summary.json"
    round2_summary = core.read_json(root / round2_summary_ref)
    if (round2_summary.get("status") != "success"
            or round2_summary.get("round") != "round2"
            or round2_summary.get("mathematical_rule_change") is not False):
        raise ValueError("Unrecognized round2 evidence")

    round2_table_ref = (
        "results/Q1/experiments/round2/tables/operating_characteristics.csv")
    round2_rows = {}
    with (root / round2_table_ref).open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            key = (row["method_id"], int(row["cap"]), float(row["theta"]))
            round2_rows[key] = {field: float(row[field]) for field in
                                ("ASN", "SD_T_star", "P_A", "P_R", "P_U")}
    if len(round2_rows) != 2 * 3 * 77:
        raise ValueError("Round2 comparison table is incomplete")

    theta = dense_theta_grid()
    if (len(theta) != GRID_COUNT or theta[0] != 0 or theta[-1] != 1
            or any(round(b-a, 12) != GRID_STEP
                   for a, b in zip(theta, theta[1:]))):
        raise ValueError("Dense theta grid contract failed")

    refs = [ref for ref in screened["input_hashes"]
            if ref != "robustness/Q1/q1_robustness_summary.json"]
    refs.extend([
        round2_summary_ref,
        round2_table_ref,
        "results/Q1/experiments/round2/metrics/validation.json",
    ])
    refs = list(dict.fromkeys(refs))
    for ref in refs:
        if not (root / ref).is_file():
            raise ValueError("Missing required input: " + ref)

    return {
        "params": screened["params"],
        "config": screened["config"],
        "method_decision": screened["decision"],
        "adjustment_decision": adjustment,
        "theta": theta,
        "round2_rows": round2_rows,
        "input_hashes": {ref: core.sha256(root / ref) for ref in refs},
    }


def contiguous_ranges(rows, threshold):
    ranges = []
    start = None
    count = 0
    previous = None
    for row in rows:
        if row["P_U"] + TOL >= threshold:
            if start is None:
                start = row["theta"]
                count = 0
            count += 1
            previous = row["theta"]
        elif start is not None:
            ranges.append({"start": start, "end": previous,
                           "point_count": count})
            start = previous = None
            count = 0
    if start is not None:
        ranges.append({"start": start, "end": previous,
                       "point_count": count})
    return ranges


def largest_adjacent_change(rows):
    best = {"TV": -1.0}
    for current, changed in zip(rows, rows[1:]):
        tv = sum(abs(current[field] - changed[field])
                 for field in ("P_A", "P_R", "P_U")) / 2
        if tv > best["TV"]:
            best = {
                "theta_from": current["theta"],
                "theta_to": changed["theta"],
                "TV": tv,
                "ASN_change": changed["ASN"] - current["ASN"],
            }
    return best


def comparison_extreme(rows, field, mode):
    row = (min if mode == "min" else max)(rows, key=lambda item: item[field])
    return {"theta": row["theta"], "difference": row[field]}


def compute(data):
    p0, alpha_r, alpha_a = data["params"]
    config = data["config"]
    caps = sorted({config["probe_cap"], *config["cap_sensitivity"]})
    roles = (("B1", "main"), ("M1", "usable_baseline"))
    all_rows = []
    boundary_rows = []
    validations = {}
    method_summaries = []
    by_method = {}
    looks_by_cap = {}
    overlap_error = 0.0
    overlap_count = 0

    for method, role in roles:
        tracemalloc.start()
        started = time.perf_counter()
        method_rows = {}
        for cap in caps:
            rules, looks = core.build_rules(
                method, cap, p0, alpha_r, alpha_a)
            rows, checks = core.evaluate(rules, data["theta"])
            witnesses = core.check_boundary_witnesses(
                method, rules, looks, p0, alpha_r, alpha_a)
            if method == "B1":
                looks_by_cap[str(cap)] = looks

            for sample_size, (accept, reject) in enumerate(rules[1:], 1):
                boundary_rows.append({
                    "method_id": method,
                    "cap": cap,
                    "k": sample_size,
                    "is_look": sample_size in looks,
                    "accept_max_defects": (int(np.flatnonzero(accept)[-1])
                                           if np.any(accept) else None),
                    "reject_min_defects": (int(np.flatnonzero(reject)[0])
                                           if np.any(reject) else None),
                })

            wrong_rejection = max(row["P_R"] for row in rows
                                  if row["theta"] <= p0)
            wrong_acceptance = max(row["P_A"] for row in rows
                                   if row["theta"] >= p0)
            monotonicity = max([0.0] + [
                max(changed["P_A"] - current["P_A"],
                    current["P_R"] - changed["P_R"])
                for current, changed in zip(rows, rows[1:])])
            endpoint_undecided = max(rows[0]["P_U"], rows[-1]["P_U"])

            local_overlap_count = 0
            local_overlap_error = 0.0
            for row in rows:
                old = data["round2_rows"].get(
                    (method, cap, round(row["theta"], 12)))
                if old is None:
                    continue
                local_overlap_count += 1
                local_overlap_error = max(
                    local_overlap_error,
                    *(abs(row[field] - old[field]) for field in
                      ("ASN", "SD_T_star", "P_A", "P_R", "P_U")))
            overlap_count += local_overlap_count
            overlap_error = max(overlap_error, local_overlap_error)

            if (wrong_rejection > alpha_r + TOL
                    or wrong_acceptance > alpha_a + TOL
                    or monotonicity > TOL or endpoint_undecided > TOL
                    or local_overlap_error > TOL):
                raise ArithmeticError("Dense-grid risk check failed")
            checks.update({
                "grid_sup_wrong_rejection": wrong_rejection,
                "grid_sup_wrong_acceptance_including_boundary": wrong_acceptance,
                "monotonicity_violation": monotonicity,
                "endpoint_max_undecided": endpoint_undecided,
                "round2_overlap_count": local_overlap_count,
                "round2_overlap_max_error": local_overlap_error,
                "independent_boundary_witnesses": witnesses,
                "boundary_overlap_count": 0,
            })
            validations[f"{method}_{cap}"] = checks
            method_rows[cap] = rows
            all_rows.extend({"method_id": method, "role": role,
                             "cap": cap, **row} for row in rows)

        elapsed = time.perf_counter() - started
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        if elapsed > 60 or peak / 2**20 > 256:
            raise RuntimeError("Dense-grid per-method scale budget exceeded")
        by_method[method] = method_rows
        nominal = next(row for row in method_rows[1000]
                       if row["theta"] == p0)
        method_summaries.append({
            "method_id": method,
            "role": role,
            "script": "code/Q1/q1_run_round3.py",
            "reused_numeric_core": "code/Q1/q1_run.py",
            "status": "success",
            "execution_time_seconds": elapsed,
            "peak_traced_memory_mb": peak / 2**20,
            "memory_scope": "tracemalloc tracked allocations, not RSS",
            "input_files": list(data["input_hashes"]),
            "output_files": [],
            "figure_files": [],
            "metrics_summary": {
                "at_nominal_rate": nominal,
                "output_degeneracy": {
                    "endpoint_max_undecided": max(
                        method_rows[1000][0]["P_U"],
                        method_rows[1000][-1]["P_U"]),
                    "nonzero_outcome_types": sum(
                        any(row[field] > TOL for row in method_rows[1000])
                        for field in ("P_A", "P_R", "P_U")),
                },
            },
            "warnings": [
                "Theory conditional on iid Bernoulli and perfect detection",
                "Dense finite grid is not a proof of global optimality",
                "Near-threshold undecided concentration remains",
            ],
            "errors": [],
        })

    independent_error = 0.0
    for method, _ in roles:
        rules, _ = core.build_rules(method, 12, p0, alpha_r, alpha_a)
        probabilities = [0.0, 0.05, 0.1, 0.2, 0.9, 1.0]
        rows, _ = core.evaluate(rules, probabilities)
        for probability, row in zip(probabilities, rows):
            expected = round2.enumerate_paths(
                method, probability, 12, p0, alpha_r, alpha_a)
            independent_error = max(
                independent_error,
                *(abs(row[field] - expected[field])
                  for field in ("ASN", "P_A", "P_R", "P_U")))
    if independent_error > TOL:
        raise ArithmeticError("Independent path enumeration mismatch")

    comparison = []
    for cap in caps:
        for b1, m1 in zip(by_method["B1"][cap], by_method["M1"][cap]):
            comparison.append({
                "cap": cap,
                "theta": b1["theta"],
                "B1_ASN": b1["ASN"],
                "M1_ASN": m1["ASN"],
                "ASN_B1_minus_M1": b1["ASN"] - m1["ASN"],
                "B1_P_U": b1["P_U"],
                "M1_P_U": m1["P_U"],
                "P_U_B1_minus_M1": b1["P_U"] - m1["P_U"],
            })

    central_comparison = [row for row in comparison if row["cap"] == 1000]
    central_b1 = by_method["B1"][1000]
    central_m1 = by_method["M1"][1000]
    near_threshold = []
    for b1, m1 in zip(central_b1, central_m1):
        if 0.08 <= b1["theta"] <= 0.12:
            near_threshold.append({
                "cap": 1000,
                "theta": b1["theta"],
                "B1_ASN": b1["ASN"],
                "M1_ASN": m1["ASN"],
                "ASN_B1_minus_M1": b1["ASN"] - m1["ASN"],
                "B1_P_A": b1["P_A"],
                "M1_P_A": m1["P_A"],
                "B1_P_R": b1["P_R"],
                "M1_P_R": m1["P_R"],
                "B1_P_U": b1["P_U"],
                "M1_P_U": m1["P_U"],
                "P_U_B1_minus_M1": b1["P_U"] - m1["P_U"],
            })

    look_counts = {cap: len(looks) for cap, looks in looks_by_cap.items()}
    prefixes = [looks[:-1] for looks in looks_by_cap.values()]
    schedule = {
        "look_counts": look_counts,
        "shared_prefix": prefixes[0],
        "same_error_allocation": len(set(look_counts.values())) == 1,
        "nonnested_last_look": (
            all(prefix == prefixes[0] for prefix in prefixes)
            and len({looks[-1] for looks in looks_by_cap.values()}) == len(caps)),
        "last_looks": {cap: looks[-1]
                       for cap, looks in looks_by_cap.items()},
    }

    max_mass_error = max(row["mass_error"] for row in validations.values())
    max_asn_error = max(row["ASN_dual_error"] for row in validations.values())
    max_wrong_rejection = max(row["grid_sup_wrong_rejection"]
                              for row in validations.values())
    max_wrong_acceptance = max(
        row["grid_sup_wrong_acceptance_including_boundary"]
        for row in validations.values())
    max_monotonicity = max(row["monotonicity_violation"]
                           for row in validations.values())
    named_checks = {
        "input_contract": len(data["theta"]) == GRID_COUNT,
        "method_alignment": all(row["boundary_overlap_count"] == 0
                                for row in validations.values()),
        "probability_and_moments": (max_mass_error <= TOL
                                    and max_asn_error <= 1e-8),
        "dense_error_grid": (max_wrong_rejection <= alpha_r + TOL
                             and max_wrong_acceptance <= alpha_a + TOL),
        "directional_monotonicity": max_monotonicity <= TOL,
        "round2_overlap": overlap_count > 0 and overlap_error <= TOL,
        "schedule_check": (schedule["same_error_allocation"]
                           and schedule["nonnested_last_look"]),
        "reproducibility": independent_error <= TOL,
    }
    if not all(named_checks.values()):
        raise ArithmeticError("Named dense-grid validation failed")

    validation = {
        "status": "PASS",
        "scope": "Deterministic dense-grid generator self-checks; independent review pending",
        "named_checks": named_checks,
        "checks": validations,
        "max_mass_error": max_mass_error,
        "max_ASN_dual_error": max_asn_error,
        "max_wrong_rejection": max_wrong_rejection,
        "max_wrong_acceptance": max_wrong_acceptance,
        "max_monotonicity_violation": max_monotonicity,
        "round2_overlap_count": overlap_count,
        "round2_overlap_max_error": overlap_error,
        "independent_path_max_error": independent_error,
        "B1_schedule": schedule,
        "scale": [{"method_id": row["method_id"],
                   "execution_time_seconds": row["execution_time_seconds"],
                   "peak_traced_memory_mb": row["peak_traced_memory_mb"]}
                  for row in method_summaries],
    }

    def lower_count(field):
        return sum(row[field] < -TOL for row in central_comparison)

    dense_summary = {
        "status": "CONDITIONAL",
        "data_kind": "theoretical_parameter_grid_no_observed_samples",
        "theta_grid": {"start": 0.0, "end": 1.0,
                       "step": GRID_STEP, "count": GRID_COUNT},
        "near_threshold": {"start": 0.08, "end": 0.12,
                           "point_count": len(near_threshold)},
        "comparison": {
            "cap": 1000,
            "direction": "B1 minus M1",
            "B1_lower_ASN_points": lower_count("ASN_B1_minus_M1"),
            "B1_lower_P_U_points": lower_count("P_U_B1_minus_M1"),
            "B1_lower_both_points": sum(
                row["ASN_B1_minus_M1"] < -TOL
                and row["P_U_B1_minus_M1"] < -TOL
                for row in central_comparison),
            "largest_ASN_advantage": comparison_extreme(
                central_comparison, "ASN_B1_minus_M1", "min"),
            "largest_ASN_disadvantage": comparison_extreme(
                central_comparison, "ASN_B1_minus_M1", "max"),
            "largest_P_U_advantage": comparison_extreme(
                central_comparison, "P_U_B1_minus_M1", "min"),
            "largest_P_U_disadvantage": comparison_extreme(
                central_comparison, "P_U_B1_minus_M1", "max"),
            "theta_weighting": None,
            "uniform_superiority_claim": False,
        },
        "concentration": {
            method: {
                "P_U_at_least_0.5": contiguous_ranges(
                    by_method[method][1000], 0.5),
                "P_U_at_least_0.9": contiguous_ranges(
                    by_method[method][1000], 0.9),
                "thresholds_are_descriptive": True,
            } for method in ("B1", "M1")
        },
        "largest_adjacent_change": {
            method: largest_adjacent_change(by_method[method][1000])
            for method in ("B1", "M1")
        },
        "round2_overlap": {"point_method_cap_count": overlap_count,
                           "max_absolute_error": overlap_error},
        "limitations": [
            "Finite grid is not a full-parameter proof",
            "No theta weighting was supplied",
            "A1 and A2 remain unverified by observed samples",
        ],
    }

    bundle = {
        "tables/decision_boundaries.csv": boundary_rows,
        "tables/operating_characteristics.csv": all_rows,
        "tables/comparison.csv": comparison,
        "tables/near_threshold_dense.csv": near_threshold,
        "metrics/dense_grid_summary.json": dense_summary,
        "metrics/validation.json": validation,
    }
    output_refs = ["results/Q1/experiments/round3/" + name
                   for name in bundle]
    for row in method_summaries:
        row["output_files"] = output_refs

    b1_nominal = next(row for row in central_b1 if row["theta"] == p0)
    bundle["run_summary.json"] = {
        "schema_version": 1,
        "generated_by": "code/Q1/q1_run_round3.py",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "question": "Q1",
        "round": "round3",
        "implementation_target": "python",
        "status": "success",
        "approved_decision_id": "q1_method_choice_v2",
        "experiment_adjustment_decision_id": "q1_final_result_verdict",
        "change_from_round2": "theta_grid_density_only",
        "mathematical_rule_change": False,
        "random_seed": 2026,
        "randomness": "none",
        "seed_used": False,
        "data_kind": "theoretical_parameter_scenarios_no_observed_samples",
        "configuration": {
            "p0": p0,
            "alpha_R": alpha_r,
            "alpha_A": alpha_a,
            "caps": caps,
            "theta_grid": {"start": 0.0, "end": 1.0,
                           "step": GRID_STEP, "count": GRID_COUNT},
            "mixture": [1, 1],
            "B1_first_look": 10,
            "B1_growth": 2,
        },
        "input_sha256": data["input_hashes"],
        "code_sha256": {ref: core.sha256(ROOT / ref) for ref in (
            "code/Q1/q1_run_round3.py",
            "code/Q1/test_q1_round3.py",
            "code/Q1/q1_run.py",
            "code/Q1/q1_run_round2.py",
        )},
        "methods": method_summaries,
        "comparison": {
            "table": "results/Q1/experiments/round3/tables/comparison.csv",
            "summary": "results/Q1/experiments/round3/metrics/dense_grid_summary.json",
            "direction": "B1 minus M1",
            "uniform_superiority_claim": False,
            "theta_weighting": None,
        },
        "fallback_trigger": {"fallback_id": None, "condition": None,
                             "observed": False, "evidence": None},
        "risk_conditions": {
            "status": "CONDITIONAL",
            "assumptions": ["A1", "A2"],
            "B1_boundary_undecided": b1_nominal["P_U"],
            "dense_grid_is_uniform_proof": False,
            "cap_monotonicity_assumed": False,
            "global_minimum_claim": False,
            "force_decision_at_cap": False,
        },
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
            "executable": __import__("sys").executable,
        },
        "output_files": output_refs,
        "figure_files": [],
    }
    return bundle


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-existing", action="store_true",
                        help="Recompute without changing saved files")
    args = parser.parse_args()
    if OUT.exists() and not args.verify_existing:
        raise FileExistsError("round3 exists; use --verify-existing, never overwrite")
    if args.verify_existing:
        summary_path = OUT / "run_summary.json"
        if not summary_path.is_file():
            raise FileNotFoundError("No round3 workflow run to verify")
        if core.read_json(summary_path).get("generated_by") != (
                "code/Q1/q1_run_round3.py"):
            raise ValueError("Unrecognized existing round3 evidence")
    try:
        bundle = compute(load_inputs(ROOT))
        core.persist_bundle(OUT, bundle, verify=args.verify_existing)
    except Exception:
        if not args.verify_existing and not OUT.exists():
            core.persist_bundle(OUT, {"run_summary.json": {
                "schema_version": 1,
                "question": "Q1",
                "round": "round3",
                "status": "failed",
                "generated_by": "code/Q1/q1_run_round3.py",
                "error": traceback.format_exc(),
            }})
        raise
    print(json.dumps({
        "status": "reproduced" if args.verify_existing else "success",
        "row_counts": {name: len(value) for name, value in bundle.items()
                       if name.endswith(".csv")},
        "summary": str(OUT / "run_summary.json"),
    }, ensure_ascii=False))


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    main()
