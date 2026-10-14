"""Approved Q1 round2: B1 main, M1 usable baseline, deterministic evidence."""
import argparse
import csv
from datetime import datetime, timezone
import itertools
import json
import math
from pathlib import Path
import platform
import time
import tracemalloc
import traceback

import numpy as np

import q1_run as core


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "results/Q1/experiments/round2"
PROBE = "methods/Q1/probes/"
TOL = 1e-10


def validate_decision(records):
    choices = [row for row in records if row.get("decision_type") == "method_choice"]
    if not choices:
        raise ValueError("Missing human method choice")
    decision = choices[-1]
    required = {
        "decision_id": "q1_method_choice_v2",
        "status": "DECIDED",
        "decided_by": "human",
        "choice": "B1",
        "main_method_id": "B1",
        "baseline_method_id": "M1",
        "supersedes": "q1_method_choice",
    }
    if (any(decision.get(key) != value for key, value in required.items())
            or not decision.get("rationale", "").strip()
            or any(row.get("decision_type") == "decision_stale" for row in records)):
        raise ValueError("Current B1 method choice is missing, changed or stale")
    return decision


def load_inputs(root):
    parameter_ref = "workspace/data_clean/q1_statement_parameters.csv"
    with (root / parameter_ref).open(encoding="utf-8-sig", newline="") as handle:
        params = core.parse_parameters(list(csv.DictReader(handle)))
    if params != (0.1, 0.05, 0.1):
        raise ValueError("Official parameters differ from approved Q1 design")

    config = core.read_json(root / PROBE / "probe_config.json")
    expected_main = {"id": "M1",
                     "family": "uniform_beta_binomial_mixture_confidence_sequence",
                     "mixture": [1, 1]}
    expected_baseline = {"id": "B1",
                         "family": "prespecified_group_exact_binomial_bonferroni",
                         "first_look": 10, "growth": 2}
    if (config["parameter_ref"] != parameter_ref
            or config["main"] != expected_main
            or config["baseline"] != expected_baseline
            or config["probe_cap"] != 1000
            or config["cap_sensitivity"] != [900, 1100]):
        raise ValueError("Screened mathematical configuration changed")

    ledger_ref = "methods/Q1/q1_decisions.jsonl"
    records = [json.loads(line) for line in
               (root / ledger_ref).read_text(encoding="utf-8").splitlines()
               if line.strip()]
    decision = validate_decision(records)
    refs = [
        parameter_ref,
        PROBE + "probe_config.json",
        PROBE + "risk_probe_summary.json",
        PROBE + "risk_probe_metrics.json",
        ledger_ref,
        "methods/Q1/q1_method_card.md",
        "planning/model_assumptions.md",
        "planning/symbol_table.md",
        "workspace/data/data_profile.json",
        "code/Q1/q1_code_plan.md",
        "code/Q1/q1_code_plan_round1.md",
        "results/Q1/experiments/round1/run_summary.json",
        "results/Q1/experiments/round1/tables/operating_characteristics.csv",
    ]
    refs.extend(ref for ref in decision["evidence_refs"] if ref not in refs)
    for ref in refs:
        if not (root / ref).is_file():
            raise ValueError("Missing required input: " + ref)

    probe_summary = core.read_json(root / PROBE / "risk_probe_summary.json")
    for ref, expected in probe_summary["input_sha256"].items():
        if core.sha256(root / ref) != expected:
            raise ValueError("Changed probe input: " + ref)
    screened = {row["id"]: row for row in probe_summary["methods"]}
    if set(screened) != {"M1", "B1"} or any(
            row["verdict"] not in ("PASS", "CONDITIONAL")
            for row in screened.values()):
        raise ValueError("No eligible screened method pair")

    profile = core.read_json(root / "workspace/data/data_profile.json")
    if profile["per_question_readiness"]["Q1"]["status"] != "ready_with_warnings":
        raise ValueError("Recheck changed Q1 data readiness")
    theta = sorted({round(min(1.0, max(0.0, p * factor)), 12)
                    for p in config["theta_base"]
                    for factor in [1.0, *config["theta_relative_perturbations"]]})
    if len(theta) != 77:
        raise ValueError("Parameter grid changed since approved screening")

    old_summary = core.read_json(root / "results/Q1/experiments/round1/run_summary.json")
    if (old_summary.get("round") != "round1" or old_summary.get("status") != "success"
            or old_summary.get("generated_by") != "code/Q1/q1_run.py"):
        raise ValueError("Unrecognized historical Q1 run")
    historical = {}
    old_table = root / "results/Q1/experiments/round1/tables/operating_characteristics.csv"
    with old_table.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            key = (row["method_id"], int(row["cap"]), float(row["theta"]))
            historical[key] = {field: float(row[field]) for field in
                               ("ASN", "SD_T_star", "P_A", "P_R", "P_U")}
    if len(historical) != 2 * 3 * 77:
        raise ValueError("Historical comparison table is incomplete")

    return {
        "params": params,
        "config": config,
        "decision": decision,
        "theta": theta,
        "input_hashes": {ref: core.sha256(root / ref) for ref in refs},
        "probe": core.read_json(root / PROBE / "risk_probe_metrics.json"),
        "historical": historical,
    }


def enumerate_paths(method, probability, cap=12, p0=0.1, alpha_r=0.05,
                    alpha_a=0.1):
    """Independent small-state check without using production decision masks."""
    totals = {"P_A": 0.0, "P_R": 0.0, "P_U": 0.0, "ASN": 0.0}
    looks = []
    look = 10
    while look < cap:
        looks.append(look)
        look *= 2
    looks.append(cap)
    for path in itertools.product((0, 1), repeat=cap):
        defects = sum(path)
        weight = probability ** defects * (1 - probability) ** (cap - defects)
        cumulative = 0
        stopping_time, outcome = cap, "P_U"
        for sample_size, observed in enumerate(path, 1):
            cumulative += observed
            accept = reject = False
            if method == "M1":
                ratio = (math.factorial(cumulative) * math.factorial(sample_size-cumulative)
                         / math.factorial(sample_size+1)
                         / (p0 ** cumulative * (1-p0) ** (sample_size-cumulative)))
                accept = cumulative < p0 * sample_size and ratio > 1 / alpha_a
                reject = cumulative > p0 * sample_size and ratio > 1 / alpha_r
            elif method == "B1" and sample_size in looks:
                lower_tail = math.fsum(
                    math.comb(sample_size, j) * p0 ** j * (1-p0) ** (sample_size-j)
                    for j in range(cumulative + 1))
                upper_tail = math.fsum(
                    math.comb(sample_size, j) * p0 ** j * (1-p0) ** (sample_size-j)
                    for j in range(cumulative, sample_size + 1))
                accept = lower_tail < alpha_a / len(looks)
                reject = upper_tail < alpha_r / len(looks)
            if accept or reject:
                stopping_time = sample_size
                outcome = "P_A" if accept else "P_R"
                break
        totals[outcome] += weight
        totals["ASN"] += stopping_time * weight
    return totals


def compute(data):
    p0, alpha_r, alpha_a = data["params"]
    config = data["config"]
    caps = sorted({config["probe_cap"], *config["cap_sensitivity"]})
    roles = (("B1", "main"), ("M1", "usable_baseline"))
    all_rows, boundary_rows, validations, method_summaries = [], [], {}, []
    by_method = {}
    historical_error = 0.0

    for method, role in roles:
        tracemalloc.start()
        started = time.perf_counter()
        method_rows = {}
        for cap in caps:
            rules, looks = core.build_rules(method, cap, p0, alpha_r, alpha_a)
            rows, checks = core.evaluate(rules, data["theta"])
            witnesses = core.check_boundary_witnesses(
                method, rules, looks, p0, alpha_r, alpha_a)
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
            wrong_rejection = max(row["P_R"] for row in rows if row["theta"] <= p0)
            wrong_acceptance = max(row["P_A"] for row in rows if row["theta"] >= p0)
            monotonicity = max([0.0] + [
                max(nxt["P_A"] - current["P_A"],
                    current["P_R"] - nxt["P_R"])
                for current, nxt in zip(rows, rows[1:])])
            endpoint_undecided = max(rows[0]["P_U"], rows[-1]["P_U"])
            probe_rows = data["probe"]["runs"][method]["caps"][str(cap)]["rows"]
            probe_error = max(abs(row[field] - old[field])
                              for row, old in zip(rows, probe_rows)
                              for field in ("theta", "ASN", "P_A", "P_R", "P_U"))
            local_history_error = max(
                abs(row[field] - data["historical"][(method, cap, row["theta"])][field])
                for row in rows for field in
                ("ASN", "SD_T_star", "P_A", "P_R", "P_U"))
            historical_error = max(historical_error, local_history_error)
            if (wrong_rejection > alpha_r + TOL
                    or wrong_acceptance > alpha_a + TOL
                    or monotonicity > TOL or endpoint_undecided > TOL
                    or probe_error > TOL or local_history_error > TOL):
                raise ArithmeticError("Risk or historical-equivalence check failed")
            checks.update({
                "grid_sup_wrong_rejection": wrong_rejection,
                "grid_sup_wrong_acceptance_including_boundary": wrong_acceptance,
                "monotonicity_violation": monotonicity,
                "endpoint_max_undecided": endpoint_undecided,
                "probe_max_absolute_error": probe_error,
                "historical_max_absolute_error": local_history_error,
                "independent_boundary_witnesses": witnesses,
                "boundary_overlap_count": 0,
            })
            validations[f"{method}_{cap}"] = checks
            method_rows[cap] = rows
            all_rows.extend({"method_id": method, "role": role, "cap": cap, **row}
                            for row in rows)
        elapsed = time.perf_counter() - started
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        if elapsed > 60 or peak / 2**20 > 256:
            raise RuntimeError("Predeclared per-method scale budget exceeded")
        by_method[method] = method_rows
        central = method_rows[1000]
        nominal = next(row for row in central if row["theta"] == p0)
        method_summaries.append({
            "method_id": method,
            "role": role,
            "script": "code/Q1/q1_run_round2.py",
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
                    "endpoint_max_undecided": validations[f"{method}_1000"]["endpoint_max_undecided"],
                    "nonzero_outcome_types": sum(
                        any(row[field] > TOL for row in central)
                        for field in ("P_A", "P_R", "P_U")),
                    "max_single_outcome_probability": max(
                        max(row[field] for field in ("P_A", "P_R", "P_U"))
                        for row in central),
                },
            },
            "warnings": [
                "Theory conditional on iid Bernoulli and perfect detection",
                "Near-threshold undecided mass and sensitivity remain",
                "Finite grid is not proof of uniform optimality or stability",
            ],
            "errors": [],
        })

    independent_error = 0.0
    for method, _ in roles:
        rules, _ = core.build_rules(method, 12, p0, alpha_r, alpha_a)
        probabilities = [0.0, 0.05, 0.1, 0.2, 0.9, 1.0]
        rows, _ = core.evaluate(rules, probabilities)
        for probability, row in zip(probabilities, rows):
            expected = enumerate_paths(method, probability, 12, p0, alpha_r, alpha_a)
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
    near_threshold = []
    for theta in (0.08, 0.1, 0.12):
        b1 = next(row for row in by_method["B1"][1000] if row["theta"] == theta)
        m1 = next(row for row in by_method["M1"][1000] if row["theta"] == theta)
        near_threshold.append({
            "cap": 1000,
            "theta": theta,
            "B1_ASN": b1["ASN"],
            "M1_ASN": m1["ASN"],
            "ASN_B1_minus_M1": b1["ASN"] - m1["ASN"],
            "B1_P_A": b1["P_A"],
            "M1_P_A": m1["P_A"],
            "P_A_B1_minus_M1": b1["P_A"] - m1["P_A"],
            "B1_P_R": b1["P_R"],
            "M1_P_R": m1["P_R"],
            "P_R_B1_minus_M1": b1["P_R"] - m1["P_R"],
            "B1_P_U": b1["P_U"],
            "M1_P_U": m1["P_U"],
            "P_U_B1_minus_M1": b1["P_U"] - m1["P_U"],
        })

    sensitivity = {
        "status": "CONDITIONAL",
        "metric": "three_outcome_distribution_total_variation",
        "human_threshold": None,
        "theta_perturbations": [],
        "cap_changes": [],
    }
    for method, _ in roles:
        central = {row["theta"]: row for row in by_method[method][1000]}
        for theta in config["theta_base"]:
            for factor in config["theta_relative_perturbations"]:
                perturbed = round(min(1.0, max(0.0, theta * factor)), 12)
                current, changed = central[theta], central[perturbed]
                sensitivity["theta_perturbations"].append({
                    "method_id": method,
                    "theta": theta,
                    "perturbed_theta": perturbed,
                    "crosses_nominal": (theta-p0) * (perturbed-p0) < 0,
                    "TV": sum(abs(current[field] - changed[field])
                              for field in ("P_A", "P_R", "P_U")) / 2,
                    "ASN_relative_change": changed["ASN"] / current["ASN"] - 1,
                })
        for cap in (900, 1100):
            for row in by_method[method][cap]:
                reference = central[row["theta"]]
                sensitivity["cap_changes"].append({
                    "method_id": method,
                    "theta": row["theta"],
                    "reference_cap": 1000,
                    "cap": cap,
                    "ASN_change": row["ASN"] - reference["ASN"],
                    "P_U_change": row["P_U"] - reference["P_U"],
                })

    named_checks = {
        "input_contract": True,
        "method_alignment": all(row["boundary_overlap_count"] == 0
                                for row in validations.values()),
        "reproducibility": independent_error <= TOL,
        "historical_equivalence": historical_error <= TOL,
        "output_contract": all(
            row["mass_error"] <= TOL and row["ASN_dual_error"] <= 1e-8
            for row in validations.values()),
        "risk_reporting": [row["theta"] for row in near_threshold] == [0.08, 0.1, 0.12],
        "no_clobber": True,
    }
    if not all(named_checks.values()):
        raise ArithmeticError("Named validation contract failed")

    validation = {
        "status": "PASS",
        "scope": "Deterministic generator self-checks, not independent code review",
        "named_checks": named_checks,
        "checks": validations,
        "historical_equivalence_max_error": historical_error,
        "independent_path_max_error": independent_error,
        "scale": [{"method_id": row["method_id"],
                   "execution_time_seconds": row["execution_time_seconds"],
                   "peak_traced_memory_mb": row["peak_traced_memory_mb"]}
                  for row in method_summaries],
    }
    bundle = {
        "tables/decision_boundaries.csv": boundary_rows,
        "tables/operating_characteristics.csv": all_rows,
        "tables/comparison.csv": comparison,
        "tables/near_threshold_summary.csv": near_threshold,
        "metrics/sensitivity.json": sensitivity,
        "metrics/validation.json": validation,
    }
    output_refs = ["results/Q1/experiments/round2/" + name for name in bundle]
    for row in method_summaries:
        row["output_files"] = output_refs
    b1_nominal = next(row for row in by_method["B1"][1000] if row["theta"] == p0)
    b1_cap_increase = any(
        row["method_id"] == "B1" and row["cap"] == 1100 and row["P_U_change"] > TOL
        for row in sensitivity["cap_changes"])
    bundle["run_summary.json"] = {
        "schema_version": 1,
        "generated_by": "code/Q1/q1_run_round2.py",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "question": "Q1",
        "round": "round2",
        "implementation_target": "python",
        "status": "success",
        "approved_decision_id": "q1_method_choice_v2",
        "change_from_round1": "method_roles_only",
        "mathematical_rule_change": False,
        "random_seed": 2026,
        "randomness": "none",
        "seed_used": False,
        "data_kind": "theoretical_parameter_scenarios_no_observed_samples",
        "configuration": {"p0": p0, "alpha_R": alpha_r, "alpha_A": alpha_a,
                          "caps": caps, "theta": data["theta"], "mixture": [1, 1],
                          "B1_first_look": 10, "B1_growth": 2},
        "input_sha256": data["input_hashes"],
        "code_sha256": {ref: core.sha256(ROOT / ref) for ref in
                        ("code/Q1/q1_run_round2.py", "code/Q1/test_q1_round2.py",
                         "code/Q1/q1_run.py")},
        "methods": method_summaries,
        "comparison": {
            "table": "results/Q1/experiments/round2/tables/comparison.csv",
            "direction": "B1 minus M1",
            "uniform_superiority_claim": False,
            "max_TV_by_method": {
                method: max(row["TV"] for row in sensitivity["theta_perturbations"]
                            if row["method_id"] == method)
                for method in ("B1", "M1")},
        },
        "fallback_trigger": {"fallback_id": None, "condition": None,
                             "observed": False, "evidence": None},
        "risk_conditions": {
            "status": "CONDITIONAL",
            "assumptions": ["A1", "A2"],
            "stability_verdict": "not_approved_after_role_revision",
            "B1_boundary_undecided": b1_nominal["P_U"],
            "B1_cap_increase_can_raise_undecided": b1_cap_increase,
            "cap_monotonicity_assumed": False,
            "global_minimum_claim": False,
            "cap_is_official_requirement": False,
            "force_decision_at_cap": False,
        },
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "platform": platform.platform(),
                        "executable": __import__("sys").executable},
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
        raise FileExistsError("round2 exists; use --verify-existing, never overwrite")
    if args.verify_existing:
        summary_path = OUT / "run_summary.json"
        if not summary_path.is_file():
            raise FileNotFoundError("No round2 workflow run to verify")
        if core.read_json(summary_path).get("generated_by") != "code/Q1/q1_run_round2.py":
            raise ValueError("Unrecognized existing round2 evidence")
    try:
        bundle = compute(load_inputs(ROOT))
        core.persist_bundle(OUT, bundle, verify=args.verify_existing)
    except Exception:
        if not args.verify_existing and not OUT.exists():
            core.persist_bundle(OUT, {"run_summary.json": {
                "schema_version": 1,
                "question": "Q1",
                "round": "round2",
                "status": "failed",
                "generated_by": "code/Q1/q1_run_round2.py",
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
