"""Q1 pre-selection risk probe, not approved production model code.
Only theoretical Bernoulli probabilities; never creates observations.
"""
import csv
import hashlib
import itertools
import json
import math
import platform
import time
import tracemalloc
from datetime import datetime, timezone
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONFIG = json.loads((HERE / "probe_config.json").read_text(encoding="utf-8"))
with (ROOT / CONFIG["parameter_ref"]).open(encoding="utf-8-sig", newline="") as f:
    PARAM = list(csv.DictReader(f))
assert len(PARAM) == 1
P0 = float(PARAM[0]["nominal_defect_rate"])
AR = 1 - float(PARAM[0]["reject_confidence"])
AA = 1 - float(PARAM[0]["accept_confidence"])
BASE = CONFIG["theta_base"]
GRID = np.array(sorted(set(round(min(1., max(0., p * factor)), 12)
                          for p in BASE
                          for factor in [1., *CONFIG["theta_relative_perturbations"]])))
TOL = CONFIG["predeclared_checks"]["probability_mass_tolerance"]

def make_rules(method, cap):
    """Masks implement strict confidence-bound separation from p0."""
    logs = np.zeros(cap + 2)
    logs[1:] = np.cumsum(np.log(np.arange(1, cap + 2)))
    looks = []
    k = CONFIG["baseline"]["first_look"]
    while k < cap:
        looks.append(k)
        k *= CONFIG["baseline"]["growth"]
    looks.append(cap)
    rules = [None]
    for k in range(1, cap + 1):
        x = np.arange(k + 1)
        loglik = x * math.log(P0) + (k - x) * math.log1p(-P0)
        if method == "M1":
            loge = logs[x] + logs[k-x] - logs[k+1] - loglik
            accept = (x < k * P0) & (loge > math.log(1 / AA))
            reject = (x > k * P0) & (loge > math.log(1 / AR))
        elif k in looks:
            pmf = np.exp(logs[k] - logs[x] - logs[k-x] + loglik)
            lower_tail = np.cumsum(pmf)
            upper_tail = np.cumsum(pmf[::-1])[::-1]
            accept = lower_tail < AA / len(looks)
            reject = upper_tail < AR / len(looks)
        else:
            accept = np.zeros(k + 1, dtype=bool)
            reject = np.zeros(k + 1, dtype=bool)
        assert not np.any(accept & reject), (method, k)
        # One lower acceptance segment, one upper rejection segment.
        assert np.all(np.diff(accept.astype(int)) <= 0)
        assert np.all(np.diff(reject.astype(int)) >= 0)
        rules.append((accept, reject))
    return rules, looks

def exact_dp(rules, theta):
    """Absorbing recursion over (k, defect count); no Monte Carlo."""
    cap = len(rules) - 1
    theta = np.asarray(theta)
    alive = np.ones((len(theta), 1))
    pa = np.zeros(len(theta))
    pr = pa.copy()
    asn = pa.copy()
    weighted_time = pa.copy()
    second_time = pa.copy()
    for k in range(1, cap + 1):
        asn += alive.sum(axis=1)
        nxt = np.zeros((len(theta), k + 1))
        nxt[:, :-1] += alive * (1 - theta[:, None])
        nxt[:, 1:] += alive * theta[:, None]
        a, r = rules[k]
        am = nxt[:, a].sum(axis=1)
        rm = nxt[:, r].sum(axis=1)
        pa += am
        pr += rm
        weighted_time += k * (am + rm)
        second_time += k*k * (am + rm)
        nxt[:, a | r] = 0
        alive = nxt
    pu = alive.sum(axis=1)
    weighted_time += cap * pu
    second_time += cap*cap * pu
    assert np.max(np.abs(asn-weighted_time)) < 1e-8
    assert np.max(np.abs(pa+pr+pu-1)) < TOL
    assert np.all((asn >= 1-TOL) & (asn <= cap+TOL))
    return [{"theta":float(p), "ASN":float(e), "P_A":float(a),
             "P_R":float(r), "P_U":float(u),
             "SD_T_star":float(math.sqrt(max(0, s-e*e)))}
            for p,e,a,r,u,s in zip(theta,asn,pa,pr,pu,second_time)]

def enumeration_error(method):
    """Independent full binary-path enumeration, including multiple looks."""
    cap = 12
    rules, _ = make_rules(method, cap)
    ps = [0., .05, .1, .2, .9, 1.]
    errors = []
    for p, ref in zip(ps, exact_dp(rules, ps)):
        total = {"P_A":0., "P_R":0., "P_U":0., "ASN":0.}
        for path in itertools.product([0,1], repeat=cap):
            probability = p**sum(path) * (1-p)**(cap-sum(path))
            x, stop, outcome = 0, cap, "P_U"
            for k,y in enumerate(path, 1):
                x += y
                # Independently evaluate formulas, not DP masks.
                if method == "M1":
                    e = (math.factorial(x)*math.factorial(k-x)
                         / math.factorial(k+1) / (P0**x*(1-P0)**(k-x)))
                    a = x < k*P0 and e > 1/AA
                    r = x > k*P0 and e > 1/AR
                elif k in (10, 12):
                    a = sum(math.comb(k,j)*P0**j*(1-P0)**(k-j)
                            for j in range(x+1)) < AA / 2
                    r = sum(math.comb(k,j)*P0**j*(1-P0)**(k-j)
                            for j in range(x,k+1)) < AR / 2
                else:
                    a = r = False
                if a or r:
                    stop, outcome = k, "P_A" if a else "P_R"
                    break
            total[outcome] += probability
            total["ASN"] += probability*stop
        errors.extend(abs(total[key]-ref[key]) for key in total)
    return max(errors)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    all_runs = {}
    summaries = []
    for method, role in [("M1","main_candidate"),("B1","usable_baseline")]:
        runs = {}
        tracemalloc.start()
        started = time.perf_counter()
        independent_error = enumeration_error(method)
        caps = sorted(set([CONFIG["probe_cap"], *CONFIG["cap_sensitivity"],
                           *CONFIG["scale_caps"]]))
        for cap in caps:
            t0 = time.perf_counter()
            rules, looks = make_rules(method, cap)
            rows = exact_dp(rules, GRID)
            runs[str(cap)] = {"rows":rows,"runtime_seconds":time.perf_counter()-t0,
                             "looks":list(range(1,cap+1)) if method=="M1" else looks,
                             "boundary_at_cap":{
                                 "accept_max_defects":int(np.where(rules[-1][0])[0][-1]) if np.any(rules[-1][0]) else None,
                                 "reject_min_defects":int(np.where(rules[-1][1])[0][0]) if np.any(rules[-1][1]) else None}}
        elapsed = time.perf_counter()-started
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        rows = runs[str(CONFIG["probe_cap"])]["rows"]
        keyed = {round(r["theta"],12):r for r in rows}
        max_bad_r = max(r["P_R"] for r in rows if r["theta"] <= P0)
        max_bad_a = max(r["P_A"] for r in rows if r["theta"] >= P0)
        mono = max([0.] + [max(rows[i+1]["P_A"]-rows[i]["P_A"],
                               rows[i]["P_R"]-rows[i+1]["P_R"])
                            for i in range(len(rows)-1)])
        shifts = []
        for p in BASE:
            original = keyed[round(p,12)]
            for factor in CONFIG["theta_relative_perturbations"]:
                q = round(min(1.,max(0.,p*factor)),12)
                moved = keyed[q]
                tv = sum(abs(original[key]-moved[key])
                         for key in ("P_A","P_R","P_U"))/2
                shifts.append({"theta":p,"perturbed_theta":q,"decision_distribution_TV":tv,
                               "ASN_relative_change":moved["ASN"]/original["ASN"]-1})
        endpoints = max(keyed[0.]["P_U"],keyed[1.]["P_U"])
        checks = {
            "mass_conservation_max_error":max(abs(r["P_A"]+r["P_R"]+r["P_U"]-1) for r in rows),
            "independent_path_enumeration_max_error":independent_error,
            "grid_sup_wrong_rejection":max_bad_r,
            "grid_sup_wrong_acceptance_including_boundary":max_bad_a,
            "monotonicity_violation":mono,
            "endpoint_max_undecided":endpoints,
            "boundary_undecided":keyed[P0]["P_U"],
            "decision_distribution_max_TV_under_10pct_theta":max(s["decision_distribution_TV"] for s in shifts)}
        hard_pass = (independent_error < CONFIG["predeclared_checks"]["independent_check_tolerance"]
                     and max_bad_r <= AR+TOL and max_bad_a <= AA+TOL
                     and mono <= TOL and endpoints <= CONFIG["predeclared_checks"]["endpoint_undecided_max"]
                     and elapsed <= CONFIG["predeclared_checks"]["runtime_seconds_per_method"]
                     and peak/2**20 <= CONFIG["predeclared_checks"]["peak_memory_mb"])
        all_runs[method] = {"caps":runs,"perturbations":shifts,"checks":checks}
        summaries.append({
            "id":method,"role":role,
            "executability":{"status":"PASS" if hard_pass else "FAIL","evidence":checks},
            "data_coverage":{"status":"PASS","evidence":{"official_parameter_rows":1,
                 "observed_sample_rows":0,"effective_sample_size":None,
                 "theta_grid_points":len(GRID),"theta_range":[0,1],
                 "selection":"Predeclared parameter grid spanning both sides, boundary and extremes, plus relative +/-10% perturbations",
                 "missingness":"No empirical observations supplied; theoretical design does not require fabricated records"}},
            "assumption_checks":[
                {"name":"iid_Bernoulli_and_perfect_detection","status":"CONDITIONAL",
                 "evidence":"Accepted simplifying assumptions A1/A2; not empirically testable from supplied inputs"},
                {"name":"repeated_looks_error_control","status":"PASS" if max_bad_r<=AR+TOL and max_bad_a<=AA+TOL else "FAIL",
                 "evidence":checks,"basis":"Ville mixture martingale" if method=="M1" else "Exact binomial tails plus Bonferroni union bound"}],
            "output_degeneracy":{"status":"PASS" if endpoints<=TOL else "FAIL",
                 "metrics":{"endpoint_max_undecided":endpoints,
                            "boundary_undecided":keyed[P0]["P_U"],
                            "max_single_outcome_probability":max(max(r["P_A"],r["P_R"],r["P_U"]) for r in rows),
                            "nonzero_outcome_types_across_grid":sum(any(r[key]>TOL for r in rows) for key in ("P_A","P_R","P_U"))},
                 "interpretation":"Near p0 undecided concentration is inherent; endpoints must decide. No universal all-undecided rule."},
            "perturbation_sensitivity":{"status":"CONDITIONAL",
                 "perturbation":"true theta +/-10%; cap 900/1000/1100, official p0 and confidence fixed",
                 "metric":"decision_distribution_total_variation_not_individual_path_flip_rate",
                 "value":checks["decision_distribution_max_TV_under_10pct_theta"],
                 "monotonicity_violation":mono,
                 "note":"No human-defined acceptable TV threshold. Changes crossing p0 are not automatically instability failures."},
            "scale_check":{"status":"PASS" if elapsed<=60 and peak/2**20<=256 else "FAIL",
                 "representative_caps":caps,"runtime_seconds":elapsed,"peak_traced_memory_mb":peak/2**20,
                 "memory_scope":"Python/NumPy allocations tracked by tracemalloc, not process RSS"},
            "verdict":"CONDITIONAL" if hard_pass else "FAIL",
            "conditions":CONFIG["conditions"]+["Human must judge reported sensitivity and undecided/ASN tradeoff before approving method."],
            "evidence_refs":["methods/Q1/probes/probe_config.json","methods/Q1/probes/risk_probe_metrics.json"]})
    hashes = {name:digest(ROOT/name) for name in [
        CONFIG["parameter_ref"],"planning/framing_decisions.jsonl","planning/model_assumptions.md",
        "methods/Q1/probes/probe_config.json","methods/Q1/probes/q1_screening_probe.py"]}
    metadata = {"generated_at":datetime.now(timezone.utc).isoformat(),"input_sha256":hashes,
                "environment":{"python":platform.python_version(),"numpy":np.__version__},
                "seed":None,"randomness":"None: exact finite-state probability propagation"}
    (HERE/"risk_probe_metrics.json").write_text(
        json.dumps({"metadata":metadata,"runs":all_runs},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    summary = {"schema_version":1,"question_id":"Q1",**metadata,
               "scope":CONFIG["scope"],"data_refs":[CONFIG["parameter_ref"],"workspace/data/data_profile.json"],
               "methods":summaries}
    (HERE/"risk_probe_summary.json").write_text(
        json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"verdicts":[[m["id"],m["verdict"]] for m in summaries],
                      "checks":{m:all_runs[m]["checks"] for m in all_runs}},indent=2))
    if any(m["verdict"]=="FAIL" for m in summaries):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
