"""Behavioral checks for the approved Q1 round3 dense-theta experiment."""
import copy
import importlib.util
import unittest


SPEC = importlib.util.find_spec("q1_run_round3")
if SPEC:
    import q1_run_round3 as model
else:
    model = None


class Q1Round3ImplementationTests(unittest.TestCase):
    def test_formal_round3_implementation_exists(self):
        self.assertIsNotNone(
            model, "Formal Q1 round3 implementation has not been created")


@unittest.skipIf(model is None, "round3 implementation not created yet")
class Q1Round3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = model.load_inputs(model.ROOT)
        cls.bundle = model.compute(cls.data)

    def test_dense_grid_has_requested_resolution_and_near_threshold_coverage(self):
        theta = self.data["theta"]
        self.assertEqual(len(theta), 1001)
        self.assertEqual(theta[0], 0.0)
        self.assertEqual(theta[-1], 1.0)
        self.assertTrue(all(round(b - a, 12) == 0.001
                            for a, b in zip(theta, theta[1:])))
        near = [value for value in theta if 0.08 <= value <= 0.12]
        self.assertEqual(len(near), 41)
        self.assertIn(0.1, near)

    def test_human_adjustment_keeps_B1_and_changes_only_experiment_coverage(self):
        method = self.data["method_decision"]
        adjustment = self.data["adjustment_decision"]
        self.assertEqual(method["decision_id"], "q1_method_choice_v2")
        self.assertEqual(method["main_method_id"], "B1")
        self.assertEqual(method["baseline_method_id"], "M1")
        self.assertEqual(adjustment["decision_id"], "q1_final_result_verdict")
        self.assertEqual(adjustment["decision_type"], "result_verdict")
        self.assertEqual(adjustment["choice"], "adjust_expand_theta_grid")
        self.assertEqual(adjustment["round_action"], "adjust")
        self.assertEqual(
            adjustment["rationale"],
            "真实次品率设置的组数不够多，不足以表现我们模型与方法的能力")

    def test_rejects_missing_or_ai_authored_adjustment(self):
        good = self.data["adjustment_decision"]
        for field, value in (("status", "PENDING"), ("decided_by", "ai"),
                             ("round_action", "proceed")):
            changed = copy.deepcopy(good)
            changed[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                model.validate_adjustment([changed])

    def test_bundle_contains_all_dense_method_cap_scenarios(self):
        rows = self.bundle["tables/operating_characteristics.csv"]
        self.assertEqual(len(rows), 2 * 3 * 1001)
        self.assertEqual(
            {(row["method_id"], row["role"]) for row in rows},
            {("B1", "main"), ("M1", "usable_baseline")})
        near = self.bundle["tables/near_threshold_dense.csv"]
        self.assertEqual(len(near), 41)
        self.assertEqual(near[0]["theta"], 0.08)
        self.assertEqual(near[-1]["theta"], 0.12)

    def test_superseded_report_is_provenance_not_a_computational_input(self):
        inputs = self.bundle["run_summary.json"]["input_sha256"]
        self.assertNotIn(
            "results/Q1/reports/q1_final_result_analysis.md", inputs)
        self.assertNotIn("robustness/Q1/q1_robustness_summary.json", inputs)
        self.assertIn("methods/Q1/q1_decisions.jsonl", inputs)

    def test_nominal_values_match_reviewed_round2_evidence(self):
        rows = self.bundle["tables/comparison.csv"]
        nominal = next(row for row in rows
                       if row["cap"] == 1000 and row["theta"] == 0.1)
        self.assertAlmostEqual(nominal["B1_ASN"], 959.3274283395174, places=9)
        self.assertAlmostEqual(nominal["M1_ASN"], 967.7440880098518, places=9)
        self.assertAlmostEqual(nominal["B1_P_U"], 0.936410476842364,
                               places=12)
        self.assertAlmostEqual(nominal["M1_P_U"], 0.9649192733664852,
                               places=12)
        validation = self.bundle["metrics/validation.json"]
        self.assertGreater(validation["round2_overlap_count"], 60)
        self.assertLessEqual(validation["round2_overlap_max_error"], 1e-10)

    def test_dense_validation_controls_error_and_schedule(self):
        validation = self.bundle["metrics/validation.json"]
        self.assertEqual(validation["status"], "PASS")
        self.assertTrue(all(validation["named_checks"].values()))
        self.assertLessEqual(validation["max_mass_error"], 1e-10)
        self.assertLessEqual(validation["max_ASN_dual_error"], 1e-8)
        self.assertLessEqual(validation["max_wrong_rejection"], 0.05 + 1e-10)
        self.assertLessEqual(validation["max_wrong_acceptance"], 0.10 + 1e-10)
        self.assertEqual(validation["B1_schedule"]["look_counts"],
                         {"900": 8, "1000": 8, "1100": 8})
        self.assertTrue(validation["B1_schedule"]["same_error_allocation"])
        self.assertTrue(validation["B1_schedule"]["nonnested_last_look"])

    def test_dense_summary_is_descriptive_not_an_optimality_claim(self):
        dense = self.bundle["metrics/dense_grid_summary.json"]
        self.assertEqual(dense["theta_grid"]["count"], 1001)
        self.assertEqual(dense["near_threshold"]["point_count"], 41)
        self.assertEqual(dense["comparison"]["cap"], 1000)
        self.assertEqual(dense["comparison"]["direction"], "B1 minus M1")
        self.assertFalse(dense["comparison"]["uniform_superiority_claim"])
        self.assertIsNone(dense["comparison"]["theta_weighting"])
        for method in ("B1", "M1"):
            self.assertIn("P_U_at_least_0.5", dense["concentration"][method])
            self.assertIn("P_U_at_least_0.9", dense["concentration"][method])


if __name__ == "__main__":
    unittest.main(verbosity=2)
