"""Approved Q1 round1: deterministic Bernoulli design, not observed data."""
import argparse
import csv
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
import math
from pathlib import Path
import platform
import time
import tracemalloc
import traceback
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "results/Q1/experiments/round1"
PROBE = "methods/Q1/probes/"
TOL = 1e-10

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse_parameters(rows):
    fields = ("nominal_defect_rate", "reject_confidence", "accept_confidence")
    if len(rows) != 1 or set(rows[0]) != set(fields):
        raise ValueError("Expected one row with exactly the three official fields")
    try:
        values = [Decimal(rows[0][field]) for field in fields]
        if any(not v.is_finite() or not 0 < v < 1 for v in values):
            raise ValueError("All input proportions must be finite and interior")
    except (InvalidOperation, TypeError) as exc:
        raise ValueError("Invalid probability field") from exc
    return float(values[0]), float(1-values[1]), float(1-values[2])

def load_inputs(root):
    parameter_ref = "workspace/data_clean/q1_statement_parameters.csv"
    with (root / parameter_ref).open(encoding="utf-8-sig", newline="") as f:
        params = parse_parameters(list(csv.DictReader(f)))
    if params != (.1, .05, .1):
        raise ValueError("Official parameters differ from approved Q1 design")
    config = read_json(root / PROBE / "probe_config.json")
    if (config["parameter_ref"] != parameter_ref
            or config["main"] != {"id":"M1",
                "family":"uniform_beta_binomial_mixture_confidence_sequence","mixture":[1,1]}
            or config["baseline"] != {"id":"B1",
                "family":"prespecified_group_exact_binomial_bonferroni","first_look":10,"growth":2}
            or config["probe_cap"] != 1000 or config["cap_sensitivity"] != [900,1100]):
        raise ValueError("Unapproved method configuration")
    records = [json.loads(line) for line in
               (root/"methods/Q1/q1_decisions.jsonl").read_text(encoding="utf-8").splitlines()
               if line.strip()]
    choices = [r for r in records if r.get("decision_type") == "method_choice"]
    if not choices:
        raise ValueError("Missing human method choice")
    decision = choices[-1]
    if (decision.get("decision_id") != "q1_method_choice"
            or decision.get("status") != "DECIDED"
            or decision.get("decided_by") != "human"
            or decision.get("choice") != "M1"
            or decision.get("baseline_method_id") != "B1"
            or not decision.get("rationale", "").strip()
            or any(r.get("decision_type") == "decision_stale" for r in records)):
        raise ValueError("Method choice missing, changed or stale")
    refs = [parameter_ref, PROBE+"probe_config.json", PROBE+"risk_probe_summary.json",
            PROBE+"risk_probe_metrics.json", "methods/Q1/q1_decisions.jsonl",
            "methods/Q1/q1_method_card.md", "planning/model_assumptions.md",
            "planning/symbol_table.md", "workspace/data/data_profile.json",
            "code/Q1/q1_code_plan.md"]
    for ref in refs + decision["evidence_refs"]:
        if not (root/ref).is_file():
            raise ValueError("Missing required input: "+ref)
    summary = read_json(root/PROBE/"risk_probe_summary.json")
    for ref, expected in summary["input_sha256"].items():
        if sha256(root/ref) != expected:
            raise ValueError("Changed probe input: "+ref)
    if {m["id"] for m in summary["methods"]} != {"M1","B1"} or any(
            m["verdict"] not in ("PASS","CONDITIONAL") for m in summary["methods"]):
        raise ValueError("No eligible screened pair")
    profile = read_json(root/"workspace/data/data_profile.json")
    if profile["per_question_readiness"]["Q1"]["status"] != "ready_with_warnings":
        raise ValueError("Recheck changed Q1 data readiness")
    theta = sorted({round(min(1., max(0., p*f)),12)
                    for p in config["theta_base"]
                    for f in [1., *config["theta_relative_perturbations"]]})
    if len(theta) != 77:
        raise ValueError("Parameter grid changed since approved screening")
    return {"params":params, "config":config, "decision":decision, "theta":theta,
            "input_hashes":{ref:sha256(root/ref) for ref in refs},
            "probe":read_json(root/PROBE/"risk_probe_metrics.json")}

def build_rules(method, cap, p0=.1, ar=.05, aa=.1):
    if method not in ("M1","B1") or type(cap) is not int or cap < 1:
        raise ValueError("Unknown method or invalid integer budget")
    if any(not math.isfinite(v) or not 0 < v < 1 for v in (p0,ar,aa)):
        raise ValueError("Invalid probability")
    looks, k = [], 10
    while k < cap:
        looks.append(k)
        k *= 2
    looks.append(cap)
    active = set(range(1,cap+1)) if method == "M1" else set(looks)
    logs = np.zeros(cap+2)
    logs[1:] = np.cumsum(np.log(np.arange(1,cap+2)))
    rules = [None]
    for k in range(1,cap+1):
        x = np.arange(k+1)
        a = np.zeros(k+1, dtype=bool)
        r = a.copy()
        if k in active:
            ll = x*math.log(p0)+(k-x)*math.log1p(-p0)
            if method == "M1":
                le = logs[x]+logs[k-x]-logs[k+1]-ll
                a = (x < k*p0) & (le > math.log(1/aa))
                r = (x > k*p0) & (le > math.log(1/ar))
            else:
                pmf = np.exp(logs[k]-logs[x]-logs[k-x]+ll)
                a = np.cumsum(pmf) < aa/len(looks)
                r = np.cumsum(pmf[::-1])[::-1] < ar/len(looks)
        if (np.any(a&r) or np.any(np.diff(a.astype(int)) > 0)
                or np.any(np.diff(r.astype(int)) < 0)):
            raise ArithmeticError("Overlapping or noncontiguous boundaries")
        rules.append((a,r))
    return rules, sorted(active)

def evaluate(rules, theta):
    theta = np.asarray(theta, dtype=float)
    if theta.ndim != 1 or not theta.size or not np.all(np.isfinite(theta)) or np.any(
            (theta < 0) | (theta > 1)):
        raise ValueError("Expected a nonempty one-dimensional probability grid")
    cap = len(rules)-1
    alive = np.ones((len(theta),1))
    pa, pr, asn, moment1, moment2 = [np.zeros(len(theta)) for _ in range(5)]
    for k in range(1,cap+1):
        asn += alive.sum(axis=1)
        nxt = np.zeros((len(theta),k+1))
        nxt[:,:-1] += alive*(1-theta[:,None])
        nxt[:,1:] += alive*theta[:,None]
        a,r = rules[k]
        am,rm = nxt[:,a].sum(axis=1),nxt[:,r].sum(axis=1)
        pa += am
        pr += rm
        moment1 += k*(am+rm)
        moment2 += k*k*(am+rm)
        nxt[:,a|r] = 0.
        alive = nxt
    pu = alive.sum(axis=1)
    moment1 += cap*pu
    moment2 += cap*cap*pu
    checks = {"mass_error":float(np.max(np.abs(pa+pr+pu-1))),
              "ASN_dual_error":float(np.max(np.abs(asn-moment1))),
              "minimum_variance_before_roundoff_clip":float(np.min(moment2-asn*asn))}
    if (checks["mass_error"] > TOL or checks["ASN_dual_error"] > 1e-8
            or min(pa.min(),pr.min(),pu.min()) < -TOL
            or max(pa.max(),pr.max(),pu.max()) > 1+TOL
            or np.any(asn < 1-TOL) or np.any(asn > cap+TOL)
            or checks["minimum_variance_before_roundoff_clip"] < -1e-6):
        raise ArithmeticError("Probability or moment check failed")
    rows = [{"theta":float(p),"ASN":float(e),"SD_T_star":float(math.sqrt(max(0,s-e*e))),
             "P_A":float(a),"P_R":float(r),"P_U":float(u)}
            for p,e,s,a,r,u in zip(theta,asn,moment2,pa,pr,pu)]
    return rows, checks

def log_e(k,x,u):
    if u == 0:
        return -math.log(k+1) if x == 0 else math.inf
    if u == 1:
        return -math.log(k+1) if x == k else math.inf
    return (math.lgamma(x+1)+math.lgamma(k-x+1)-math.lgamma(k+2)
            -x*math.log(u)-(k-x)*math.log1p(-u))

def mixture_interval(k,x,alpha):
    mle, target = x/k, math.log(1/alpha)
    lower, upper = 0.,1.
    if x:
        left,right = 0.,mle
        for _ in range(70):
            mid = (left+right)/2
            if log_e(k,x,mid) > target:
                left = mid
            else:
                right = mid
        lower = (left+right)/2
    if x < k:
        left,right = mle,1.
        for _ in range(70):
            mid = (left+right)/2
            if log_e(k,x,mid) > target:
                right = mid
            else:
                left = mid
        upper = (left+right)/2
    return lower,upper

def check_boundary_witnesses(method, rules, looks, p0, ar, aa):
    count = 0
    for k in sorted({v for v in (1,2,10,62,80,100,320,len(rules)-1) if v < len(rules)}):
        a,r = rules[k]
        indices = {0,k}
        for mask in (a,r):
            for x in np.flatnonzero(np.diff(mask.astype(int))):
                indices.update([int(x),int(x+1)])
        for x in sorted(indices):
            if method == "M1":
                lo,_ = mixture_interval(k,x,ar)
                _,hi = mixture_interval(k,x,aa)
                want_a, want_r = hi < p0, lo > p0
            elif k in looks:
                pmf = [math.exp(math.lgamma(k+1)-math.lgamma(j+1)
                       -math.lgamma(k-j+1)+j*math.log(p0)+(k-j)*math.log1p(-p0))
                       for j in range(k+1)]
                want_a = math.fsum(pmf[:x+1]) < aa/len(looks)
                want_r = math.fsum(pmf[x:]) < ar/len(looks)
            else:
                want_a = want_r = False
            if bool(a[x]) != want_a or bool(r[x]) != want_r:
                raise ArithmeticError(f"Independent boundary mismatch: {method},{k},{x}")
            count += 1
    return count

def compute(data):
    p0,ar,aa = data["params"]
    cfg = data["config"]
    caps = sorted({cfg["probe_cap"], *cfg["cap_sensitivity"]})
    all_rows, boundary_rows, validations, method_summaries = [],[],{},[]
    by_method = {}
    for method,role in (("M1","main"),("B1","usable_baseline")):
        tracemalloc.start()
        start = time.perf_counter()
        method_rows = {}
        for cap in caps:
            rules,looks = build_rules(method,cap,p0,ar,aa)
            rows,checks = evaluate(rules,data["theta"])
            witness_count = check_boundary_witnesses(method,rules,looks,p0,ar,aa)
            for k,(a,r) in enumerate(rules[1:],1):
                boundary_rows.append({"method_id":method,"cap":cap,"k":k,
                    "is_look":k in looks,
                    "accept_max_defects":int(np.flatnonzero(a)[-1]) if np.any(a) else None,
                    "reject_min_defects":int(np.flatnonzero(r)[0]) if np.any(r) else None})
            mass_risk = max(row["P_R"] for row in rows if row["theta"] <= p0)
            accept_risk = max(row["P_A"] for row in rows if row["theta"] >= p0)
            mono = max([0.] + [max(b["P_A"]-a["P_A"],a["P_R"]-b["P_R"])
                               for a,b in zip(rows,rows[1:])])
            endpoint_u = max(rows[0]["P_U"],rows[-1]["P_U"])
            original = data["probe"]["runs"][method]["caps"][str(cap)]["rows"]
            probe_error = max(abs(row[key]-old[key]) for row,old in zip(rows,original)
                              for key in ("theta","ASN","P_A","P_R","P_U"))
            if mass_risk > ar+TOL or accept_risk > aa+TOL or mono > TOL or endpoint_u > TOL or probe_error > 1e-8:
                raise ArithmeticError("Risk or probe-reproduction check failed")
            checks.update(grid_sup_wrong_rejection=mass_risk,
                grid_sup_wrong_acceptance_including_boundary=accept_risk,
                monotonicity_violation=mono,endpoint_max_undecided=endpoint_u,
                probe_max_absolute_error=probe_error,independent_boundary_witnesses=witness_count,
                boundary_overlap_count=0)
            validations[f"{method}_{cap}"] = checks
            method_rows[cap] = rows
            all_rows.extend({"method_id":method,"cap":cap,**row} for row in rows)
        elapsed = time.perf_counter()-start
        _,peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        if elapsed > 60 or peak/2**20 > 256:
            raise RuntimeError("Predeclared per-method scale budget exceeded")
        by_method[method] = method_rows
        central = method_rows[1000]
        boundary = next(r for r in central if r["theta"] == p0)
        method_summaries.append({"method_id":method,"role":role,"script":"code/Q1/q1_run.py",
            "status":"success","execution_time_seconds":elapsed,"peak_traced_memory_mb":peak/2**20,
            "memory_scope":"tracemalloc tracked allocations, not RSS",
            "input_files":list(data["input_hashes"]),"output_files":[],"figure_files":[],
            "metrics_summary":{"at_nominal_rate":boundary,
                "output_degeneracy":{"endpoint_max_undecided":validations[f"{method}_1000"]["endpoint_max_undecided"],
                    "nonzero_outcome_types":sum(any(r[key] > TOL for r in central) for key in ("P_A","P_R","P_U")),
                    "max_single_outcome_probability":max(max(r[key] for key in ("P_A","P_R","P_U")) for r in central)}},
            "warnings":["Theory conditional on iid Bernoulli and perfect detection",
                        "Near-threshold undecided mass and sensitivity remain",
                        "Finite grid is not proof of uniform optimality or stability"],"errors":[]})
    comparison = []
    for cap in caps:
        for m,b in zip(by_method["M1"][cap],by_method["B1"][cap]):
            comparison.append({"cap":cap,"theta":m["theta"],
                "M1_ASN":m["ASN"],"B1_ASN":b["ASN"],"ASN_M1_minus_B1":m["ASN"]-b["ASN"],
                "M1_P_U":m["P_U"],"B1_P_U":b["P_U"],"P_U_M1_minus_B1":m["P_U"]-b["P_U"]})
    sensitivity = {"status":"CONDITIONAL","metric":"three_outcome_distribution_total_variation",
                   "human_threshold":None,"theta_perturbations":[],"cap_changes":[]}
    for method in ("M1","B1"):
        idx = {r["theta"]:r for r in by_method[method][1000]}
        for p in cfg["theta_base"]:
            for factor in cfg["theta_relative_perturbations"]:
                q = round(min(1.,max(0.,p*factor)),12)
                a,b = idx[p],idx[q]
                sensitivity["theta_perturbations"].append({"method_id":method,"theta":p,
                    "perturbed_theta":q,"crosses_nominal":(p-p0)*(q-p0)<0,
                    "TV":sum(abs(a[key]-b[key]) for key in ("P_A","P_R","P_U"))/2,
                    "ASN_relative_change":b["ASN"]/a["ASN"]-1})
        for cap in (900,1100):
            for row in by_method[method][cap]:
                ref = idx[row["theta"]]
                sensitivity["cap_changes"].append({"method_id":method,"theta":row["theta"],
                    "reference_cap":1000,"cap":cap,
                    "ASN_change":row["ASN"]-ref["ASN"],"P_U_change":row["P_U"]-ref["P_U"]})
    bundle = {"tables/decision_boundaries.csv":boundary_rows,
              "tables/operating_characteristics.csv":all_rows,
              "tables/comparison.csv":comparison,
              "metrics/sensitivity.json":sensitivity,
              "metrics/validation.json":{"status":"PASS","checks":validations,
                  "scope":"Deterministic numerical self-checks, not independent code review",
                  "scale":[{"method_id":m["method_id"],
                            "execution_time_seconds":m["execution_time_seconds"],
                            "peak_traced_memory_mb":m["peak_traced_memory_mb"]} for m in method_summaries]}}
    out_refs = ["results/Q1/experiments/round1/"+name for name in bundle]
    for m in method_summaries:
        m["output_files"] = out_refs
    bundle["run_summary.json"] = {"schema_version":1,"generated_by":"code/Q1/q1_run.py",
        "generated_at":datetime.now(timezone.utc).isoformat(),"question":"Q1","round":"round1",
        "implementation_target":"python","status":"success","approved_decision_id":"q1_method_choice",
        "random_seed":2026,"randomness":"none","seed_used":False,
        "data_kind":"theoretical_parameter_scenarios_no_observed_samples",
        "configuration":{"p0":p0,"alpha_R":ar,"alpha_A":aa,"caps":caps,
             "theta":data["theta"],"mixture":[1,1],"B1_first_look":10,"B1_growth":2},
        "input_sha256":data["input_hashes"],
        "code_sha256":{ref:sha256(ROOT/ref) for ref in ("code/Q1/q1_run.py","code/Q1/test_q1_model.py")},
        "methods":method_summaries,
        "comparison":{"table":out_refs[2],"direction":"M1 minus B1","uniform_superiority_claim":False,
            "max_TV_by_method":{m:max(r["TV"] for r in sensitivity["theta_perturbations"] if r["method_id"]==m)
                               for m in ("M1","B1")}},
        "fallback_trigger":{"fallback_id":None,"condition":None,"observed":False,"evidence":None},
        "risk_conditions":{"status":"CONDITIONAL","assumptions":["A1","A2"],
            "stability_verdict":"not_human_judged","global_minimum_claim":False,
            "cap_is_official_requirement":False,"force_decision_at_cap":False},
        "environment":{"python":platform.python_version(),"numpy":np.__version__,
             "platform":platform.platform(),"executable":__import__("sys").executable},
        "output_files":out_refs,"figure_files":[]}
    return bundle

def encode_file(name, value):
    if name.endswith(".csv"):
        s = io.StringIO(newline="")
        writer = csv.DictWriter(s,fieldnames=list(value[0]),lineterminator="\n")
        writer.writeheader()
        writer.writerows({k:("null" if v is None else v) for k,v in row.items()} for row in value)
        return s.getvalue()
    return json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+"\n"

def stable(value):
    """Only wall time, memory allocation and timestamp may differ on rerun."""
    volatile = {"generated_at","execution_time_seconds","peak_traced_memory_mb"}
    if isinstance(value,dict):
        return {k:stable(v) for k,v in value.items() if k not in volatile}
    if isinstance(value,list):
        return [stable(v) for v in value]
    return value

def persist_bundle(out, bundle, verify=False):
    if verify:
        for name,value in bundle.items():
            path = out/name
            if name.endswith(".csv"):
                equal = path.read_text(encoding="utf-8") == encode_file(name,value)
            else:
                equal = stable(read_json(path)) == stable(value)
            if not equal:
                raise ValueError("Rerun mismatch: "+name)
        return
    # Refuse even existing empty directories: never claim someone else's round.
    out.mkdir(parents=True,exist_ok=False)
    for name,value in bundle.items():
        path = out/name
        path.parent.mkdir(parents=True,exist_ok=True)
        with path.open("x",encoding="utf-8",newline="") as f:
            f.write(encode_file(name,value))
    (out/"figures").mkdir()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-existing", action="store_true",
                        help="Recompute without changing saved files; compare deterministic outputs")
    args = parser.parse_args()
    if OUT.exists() and not args.verify_existing:
        raise FileExistsError("round1 exists; use --verify-existing, never overwrite")
    if args.verify_existing and not (OUT/"run_summary.json").is_file():
        raise FileNotFoundError("No current workflow run to verify")
    if args.verify_existing and read_json(OUT/"run_summary.json").get("generated_by") != "code/Q1/q1_run.py":
        raise ValueError("Unrecognized existing round: do not read historical answers")
    try:
        bundle = compute(load_inputs(ROOT))
        persist_bundle(OUT,bundle,verify=args.verify_existing)
    except Exception:
        # Preserve failure evidence only in a new, task-owned directory.
        if not args.verify_existing and not OUT.exists():
            persist_bundle(OUT,{"run_summary.json":{"schema_version":1,"question":"Q1",
                "round":"round1","status":"failed","generated_by":"code/Q1/q1_run.py",
                "error":traceback.format_exc()}})
        raise
    print(json.dumps({"status":"reproduced" if args.verify_existing else "success",
        "row_counts":{k:len(v) for k,v in bundle.items() if k.endswith(".csv")},
        "summary":str(OUT/"run_summary.json")},ensure_ascii=False))

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    main()

