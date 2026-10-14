"""Behavioral checks for the approved Q1 round2 role revision."""
import copy
import importlib.util
import unittest


SPEC = importlib.util.find_spec("q1_run_round2")
if SPEC:
    import q1_run_round2 as model
else:
    model = None


class Q1Round2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if model is None:
            raise AssertionError("Formal Q1 round2 implementation has not been created")
        cls.data = model.load_inputs(model.ROOT)
        cls.bundle = model.compute(cls.data)

    def test_loads_latest_human_choice_with_reversed_roles(self):
        decision = self.data["decision"]
        self.assertEqual(decision["decision_id"], "q1_method_choice_v2")
        self.assertEqual(decision["main_method_id"], "B1")
        self.assertEqual(decision["baseline_method_id"], "M1")
        self.assertEqual(decision["rationale"], "B1方案在接近10%时的未决率较小")
        self.assertEqual(len(self.data["theta"]), 77)

    def test_rejects_stale_or_wrong_role_decisions(self):
        good = self.data["decision"]
        for field, value in (("status", "PENDING"), ("decided_by", "ai"),
                             ("main_method_id", "M1"),
                             ("baseline_method_id", "B1"),
                             ("supersedes", None)):
            changed = copy.deepcopy(good)
            changed[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                model.validate_decision([changed])
        later = copy.deepcopy(good)
        later["decision_id"] = "later_method_choice"
        with self.assertRaises(ValueError):
            model.validate_decision([good, later])

    def test_bundle_uses_B1_as_main_and_M1_as_comparable_baseline(self):
        summary = self.bundle["run_summary.json"]
        self.assertEqual(summary["round"], "round2")
        self.assertEqual(summary["approved_decision_id"], "q1_method_choice_v2")
        self.assertEqual(summary["change_from_round1"], "method_roles_only")
        self.assertFalse(summary["mathematical_rule_change"])
        roles = {row["method_id"]: row["role"] for row in summary["methods"]}
        self.assertEqual(roles, {"B1": "main", "M1": "usable_baseline"})
        self.assertEqual(summary["comparison"]["direction"], "B1 minus M1")
        self.assertIsNone(summary["fallback_trigger"]["fallback_id"])
        self.assertEqual(summary["figure_files"], [])

    def test_nominal_comparison_has_current_direction_and_known_values(self):
        rows = self.bundle["tables/comparison.csv"]
        row = next(r for r in rows if r["cap"] == 1000 and r["theta"] == 0.1)
        self.assertAlmostEqual(row["B1_ASN"], 959.3274283395174, places=9)
        self.assertAlmostEqual(row["M1_ASN"], 967.7440880098518, places=9)
        self.assertAlmostEqual(row["ASN_B1_minus_M1"], -8.4166596703344, places=9)
        self.assertAlmostEqual(row["B1_P_U"], 0.936410476842364, places=12)
        self.assertAlmostEqual(row["M1_P_U"], 0.9649192733664852, places=12)
        self.assertAlmostEqual(row["P_U_B1_minus_M1"], -0.0285087965241212,
                               places=12)

    def test_near_threshold_and_risk_evidence_are_explicit(self):
        rows = self.bundle["tables/near_threshold_summary.csv"]
        self.assertEqual([row["theta"] for row in rows], [0.08, 0.1, 0.12])
        nominal = rows[1]
        self.assertEqual(
            set(nominal),
            {"cap", "theta", "B1_ASN", "M1_ASN", "ASN_B1_minus_M1",
             "B1_P_A", "M1_P_A", "P_A_B1_minus_M1",
             "B1_P_R", "M1_P_R", "P_R_B1_minus_M1",
             "B1_P_U", "M1_P_U", "P_U_B1_minus_M1"})
        self.assertAlmostEqual(nominal["B1_P_A"], 0.03854966147410365,
                               places=12)
        self.assertAlmostEqual(nominal["B1_P_R"], 0.025039861683558585,
                               places=12)
        self.assertGreater(nominal["B1_P_U"], 0.93)
        summary = self.bundle["run_summary.json"]
        risks = summary["risk_conditions"]
        self.assertAlmostEqual(risks["B1_boundary_undecided"],
                               0.936410476842364, places=12)
        self.assertFalse(risks["cap_monotonicity_assumed"])
        self.assertFalse(risks["global_minimum_claim"])
        self.assertFalse(risks["force_decision_at_cap"])

    def test_recalculation_matches_round1_by_method_not_role(self):
        validation = self.bundle["metrics/validation.json"]
        self.assertEqual(validation["status"], "PASS")
        self.assertLessEqual(validation["historical_equivalence_max_error"], 1e-10)
        self.assertLessEqual(validation["independent_path_max_error"], 1e-10)
        self.assertTrue(validation["named_checks"]["historical_equivalence"])
        rows = self.bundle["tables/operating_characteristics.csv"]
        role_pairs = {(row["method_id"], row["role"]) for row in rows}
        self.assertEqual(role_pairs,
                         {("B1", "main"), ("M1", "usable_baseline")})


if __name__ == "__main__":
    unittest.main(verbosity=2)
