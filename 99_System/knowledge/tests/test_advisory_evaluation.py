import copy
import importlib
import json
from pathlib import Path
import unittest
from test_advisory import AdvisoryFixture, SYSTEM


class EvaluationTests(AdvisoryFixture):
    def evaluator(self):return importlib.import_module("advisory_evaluation")

    def test_familiar_and_near_duplicate_groups_cannot_cross_partition(self):
        e = self.evaluator();bad = copy.deepcopy(self.manifest)
        bad["samples"][0].update(phase3_familiar=True, partition="holdout")
        self.assertTrue(e.audit_manifest(bad)["errors"])
        bad = copy.deepcopy(self.manifest);bad["samples"][1].update(group=bad["samples"][0]["group"], partition="holdout")
        self.assertTrue(e.audit_manifest(bad)["errors"])

    def test_real_manifest_is_30_pending_and_familiar_only_development(self):
        e = self.evaluator();manifest = json.loads((SYSTEM / "benchmarks/phase4a/sample_manifest.json").read_text(encoding="utf-8"))
        report = e.audit_manifest(manifest)
        self.assertEqual(report["sample_count"], 30)
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["partition_counts"], {"development": 12, "holdout": 18})
        self.assertEqual(manifest["scopes"]["model_visible"], [])
        self.assertFalse(manifest["real_model_tests_authorized"])
        annotations = [json.loads(line) for line in (SYSTEM / "benchmarks/phase4a/annotation_template.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(annotations), 30)
        self.assertTrue(all(row["gold"] is None and row["status"] == "pending" for row in annotations))
        result = e.evaluate(manifest, annotations)
        self.assertFalse(result["semantic_evaluated"])
        self.assertIsNone(result["metrics"])

    def test_missing_gold_or_fabricated_run_cannot_report_semantic_accuracy(self):
        e = self.evaluator()
        for gold in [[], [{"sample_id": "S", "sha256": self.manifest["samples"][0]["sha256"], "status": "pending", "gold": None}]]:
            result = e.evaluate(self.manifest, gold, run={"origin": "real_model", "model": "invented"})
            self.assertFalse(result["semantic_evaluated"])
            self.assertIsNone(result["metrics"])

    def test_scoring_math_includes_abstentions_and_empty_predictions(self):
        e = self.evaluator()
        metrics = e.classification_metrics(["concept", "proposition", "method"], ["concept", "undetermined", "concept"])
        self.assertEqual(metrics["correct"], 1)
        self.assertEqual(metrics["total"], 3)
        self.assertEqual(metrics["abstentions"], 1)
        self.assertAlmostEqual(metrics["macro_f1"], 2/9)
        self.assertEqual(e.retrieval_metrics({"S": {"A", "B"}}, {"S": ["A"]}, k=8)["known_target_recall"], 0.5)
        self.assertIsNone(e.relation_metrics(set(), set())["precision"])

    def test_exact_duplicate_content_is_reported_across_split(self):
        e = self.evaluator();groups = [{"sample_id": "a", "partition": "development", "body": "唯一长内容" * 60},
                                      {"sample_id": "b", "partition": "holdout", "body": "唯一长内容" * 60}]
        self.assertEqual(len(e.content_leakage(groups)["cross_partition"]), 1)

    def test_invalid_manifest_has_diagnostics_instead_of_an_api_crash(self):
        e=self.evaluator()
        for value in [[],{"samples":[1]},None]:
            self.assertTrue(e.audit_manifest(value)["errors"])

    def test_direct_annotation_api_cannot_bypass_schema(self):
        e=self.evaluator();row={"sample_id":"S","sha256":self.manifest["samples"][0]["sha256"],"status":"pending","gold":"fabricated"}
        with self.assertRaises(ValueError):e.evaluate(self.manifest,[row])


if __name__ == "__main__":unittest.main()
