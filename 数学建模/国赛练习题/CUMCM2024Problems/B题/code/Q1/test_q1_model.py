"""Independent behavioral checks for the approved Q1 implementation."""
import copy
import csv
import importlib.util
import itertools
import json
import math
from pathlib import Path
import tempfile
import unittest
import numpy as np

SPEC = importlib.util.find_spec("q1_run")
if SPEC:
    import q1_run as model
else:
    model = None

def enumerate_paths(method, p, cap=12):
    """Direct factorial/binomial-tail calculation, no production masks."""
    totals = dict(P_A=0., P_R=0., P_U=0., ASN=0.)
    for path in itertools.product((0, 1), repeat=cap):
        weight = p**sum(path) * (1-p)**(cap-sum(path))
        x, stopped, outcome = 0, cap, "P_U"
        for k, y in enumerate(path, 1):
            x += y
            if method == "M1":
                ratio = (math.factorial(x)*math.factorial(k-x)
                         / math.factorial(k+1) / (.1**x * .9**(k-x)))
                a = x < .1*k and ratio > 10
                r = x > .1*k and ratio > 20
            elif k in (10, 12):
                a = sum(math.comb(k,j)*.1**j*.9**(k-j)
                        for j in range(x+1)) < .1/2
                r = sum(math.comb(k,j)*.1**j*.9**(k-j)
                        for j in range(x,k+1)) < .05/2
            else:
                a = r = False
            if a or r:
                stopped, outcome = k, "P_A" if a else "P_R"
                break
        totals[outcome] += weight
        totals["ASN"] += stopped*weight
    return totals

class Q1Tests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(model, "Formal Q1 implementation has not been created")

    def test_rejects_invalid_parameter_rows(self):
        # Catches silent fallback for missing, duplicate, NaN or invalid inputs.
        good = dict(nominal_defect_rate="0.1", reject_confidence="0.95",
                    accept_confidence="0.9")
        self.assertEqual(model.parse_parameters([good]), (.1, .05, .1))
        bad = [[], [good, good], [{}]]
        for field in good:
            for value in ("nan", "inf", "-0.1", "1.1", "0", "1"):
                row = dict(good, **{field:value})
                bad.append([row])
        for rows in bad:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                model.parse_parameters(rows)

    def test_approved_inputs_resolve_without_cwd_dependency(self):
        data = model.load_inputs(model.ROOT)
        self.assertEqual(data["decision"]["rationale"], "更加灵活")
        self.assertEqual(data["decision"]["choice"], "M1")
        self.assertEqual(len(data["theta"]), 77)

    def test_unknown_method_and_bad_budget_fail(self):
        for method, cap in (("bad", 100), ("M1", 0), ("B1", 1.2), ("M1", True)):
            with self.assertRaises(ValueError):
                model.build_rules(method, cap)

    def test_group_looks_do_not_silently_become_every_item(self):
        rules, looks = model.build_rules("B1", 1000)
        self.assertEqual(looks, [10,20,40,80,160,320,640,1000])
        self.assertFalse(np.any(rules[9][0] | rules[9][1]))
        self.assertTrue(rules[10][1][10])
        self.assertFalse(np.any(rules[999][0] | rules[999][1]))

    def test_degenerate_populations_stop_at_first_legal_time(self):
        for method, expected in (("M1", (62.,2.)), ("B1",(80.,10.))):
            rules, _ = model.build_rules(method, 1000)
            rows, _ = model.evaluate(rules, [0., 1.])
            self.assertEqual(tuple(r["ASN"] for r in rows), expected)
            self.assertEqual(rows[0]["P_A"], 1.)
            self.assertEqual(rows[1]["P_R"], 1.)

    def test_no_forced_decision_and_no_discarded_unresolved_cost(self):
        rules, _ = model.build_rules("M1", 1)
        rows, _ = model.evaluate(rules, [0.,.1,1.])
        for row in rows:
            self.assertEqual(row["ASN"], 1.)
            self.assertEqual(row["P_U"], 1.)
            self.assertEqual(row["P_A"] + row["P_R"], 0.)

    def test_absorbing_dp_matches_independent_binary_paths(self):
        max_error = 0.
        for method in ("M1", "B1"):
            rules, _ = model.build_rules(method, 12)
            ps = [0., .05, .1, .2, .9, 1.]
            rows, checks = model.evaluate(rules, ps)
            for p, row in zip(ps, rows):
                expected = enumerate_paths(method, p)
                for key in expected:
                    max_error = max(max_error, abs(expected[key]-row[key]))
            self.assertLess(checks["mass_error"], 1e-10)
        self.assertLess(max_error, 1e-10)

    def test_mixture_bounds_handle_endpoints_and_inversion(self):
        for k, x in ((1,0),(2,2),(62,0),(100,10),(1000,50)):
            lo, hi = model.mixture_interval(k, x, .1)
            self.assertLessEqual(lo, x/k)
            self.assertGreaterEqual(hi, x/k)
            if x:
                self.assertAlmostEqual(model.log_e(k,x,lo), math.log(10), places=8)
            else:
                self.assertEqual(lo, 0.)
            if x < k:
                self.assertAlmostEqual(model.log_e(k,x,hi), math.log(10), places=8)
            else:
                self.assertEqual(hi, 1.)

    def test_invalid_theta_cannot_enter_dp(self):
        rules, _ = model.build_rules("M1", 2)
        for grid in ([], [math.nan], [-.1], [1.1], [[.1]]):
            with self.assertRaises(ValueError):
                model.evaluate(rules, grid)

    def test_save_is_no_clobber_and_verification_detects_changes(self):
        # Catches overwriting user data or silently accepting stale results.
        bundle = {"table.csv": [{"count":1,"boundary":None}],
                  "metrics/check.json":{"value":.25}}
        with tempfile.TemporaryDirectory(prefix="q1_test_") as tmp:
            out = Path(tmp)/"round"
            model.persist_bundle(out, bundle)
            with (out/"table.csv").open(encoding="utf-8", newline="") as f:
                self.assertEqual(list(csv.DictReader(f))[0]["boundary"], "null")
            before = (out/"metrics/check.json").read_bytes()
            with self.assertRaises(FileExistsError):
                model.persist_bundle(out, bundle)
            self.assertEqual((out/"metrics/check.json").read_bytes(), before)
            model.persist_bundle(out, bundle, verify=True)
            changed = copy.deepcopy(bundle)
            changed["metrics/check.json"]["value"] = .5
            with self.assertRaises(ValueError):
                model.persist_bundle(out, changed, verify=True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
