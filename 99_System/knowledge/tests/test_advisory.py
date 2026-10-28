"""Synthetic fixtures only; no real note bodies enter a model packet in this suite."""
import copy
import hashlib
import importlib
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SYSTEM = Path(__file__).resolve().parents[1]
if str(SYSTEM) not in sys.path:
    sys.path.insert(0, str(SYSTEM))


class AdvisoryFixture(unittest.TestCase):
    def setUp(self):
        self.assertTrue((SYSTEM / "advisory.py").is_file(), "Advisory implementation is not present")
        self.a = importlib.import_module("advisory")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        cases = json.loads((SYSTEM / "tests/advisory_cases.json").read_text(encoding="utf-8"))
        samples = []
        for name, text in cases["notes"].items():
            p = self.root / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text, encoding="utf-8")
            sid = {"notes/Source.md": "S", "entities/Fatou.md": "T", "entities/Hidden.md": "H"}[name]
            samples.append({"sample_id": sid, "path": name, "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
                            "stratum": "synthetic", "group": "g_" + sid, "partition": "development", "phase3_familiar": False})
        self.manifest = {"manifest_version": 1, "dataset_kind": "synthetic", "samples": samples,
                         "scopes": {"source": ["S"], "retrieval": ["T", "H"], "model_visible": ["S", "T"]},
                         "model_content_authorization": "synthetic_only", "real_model_tests_authorized": False}

    def packet(self, stage="relations"):
        return self.a.prepare(self.root, self.manifest, stage=stage, queries=["Fatou"])

    def response(self, packet=None, kind="relation"):
        p = packet or self.packet(); src = p["model_input"]["documents"][0]
        target = p["model_input"]["candidates"][0] if p["model_input"]["candidates"] else None
        def evidence(doc):
            span = doc["spans"][1]
            return {"document_id": doc["id"], "span_id": span["id"], "quote": span["text"]}
        item = {"id": "suggestion-1", "kind": kind, "source_id": src["id"], "source_evidence": [evidence(src)],
                "form": "atomic", "primary_type": None, "field": "uses", "resolution": "unique",
                "candidates": [{"target_id": target["id"], "evidence": [evidence(target)]}] if target else [],
                "selected_target": target["id"] if target else None, "new_entity": None, "segments": [],
                "rationale": "合成来源明确调用该工具，候选给出相应定义。",
                "confidence": {"level": "medium", "calibrated": False, "uncertainties": ["机械样例，不是数学结论验收"]},
                "requires_human_review": True}
        return {"protocol_version": 1, "request_id": p["request_id"], "origin": "synthetic_fixture", "suggestions": [item]}


class AdvisoryTests(AdvisoryFixture):
    def test_three_scopes_do_not_export_retrieval_body(self):
        p = self.packet(); payload = json.dumps(p["model_input"], ensure_ascii=False)
        self.assertNotIn("PRIVATE_BODY_SENTINEL", payload)
        self.assertEqual(len(p["model_input"]["documents"]), 1)
        self.assertEqual(len(p["model_input"]["candidates"]), 1)
        self.assertEqual(p["audit"]["scopes"]["source"]["requested"], ["S"])
        self.assertEqual(p["audit"]["scopes"]["retrieval"]["requested"], ["T", "H"])
        self.assertEqual(p["audit"]["scopes"]["model_visible"]["requested"], ["S", "T"])
        self.assertTrue(any(x["reason"] == "not_model_visible" for x in p["audit"]["exclusions"]))

    def test_pending_phase4a2_has_no_model_content(self):
        self.manifest["model_content_authorization"] = "pending_phase4a2"
        self.manifest["scopes"]["model_visible"] = []
        p = self.packet()
        self.assertEqual(p["model_input"]["documents"], [])
        self.assertEqual(p["model_input"]["candidates"], [])
        self.assertNotIn("先检查非负性", json.dumps(p))
        self.manifest["scopes"]["model_visible"] = ["S"]
        with self.assertRaises(ValueError): self.packet()

    def test_blind_classification_excludes_old_metadata(self):
        p = self.packet("classify"); doc = p["model_input"]["documents"][0]
        self.assertEqual(set(doc), {"id", "sha256", "coverage", "spans"})
        self.assertEqual(p["model_input"]["candidates"], [])
        self.assertNotIn("status", json.dumps(doc))
        self.assertNotIn("type: 方法", json.dumps(doc, ensure_ascii=False))

    def test_grounded_relation_reuses_existing_validators(self):
        p = self.packet(); result = self.a.check_response(self.root, self.manifest, p, self.response(p))
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["results"][0]["link_status"], "resolved")
        self.assertEqual(result["results"][0]["target_path"], "entities/Fatou.md")
        self.assertEqual(result["writes"], 0)

    def test_forged_quote_id_path_and_request_are_rejected(self):
        p = self.packet()
        for field, value in [("quote", "伪造引文"), ("span_id", "missing-span"), ("document_id", "hidden-id")]:
            response = self.response(p); response["suggestions"][0]["source_evidence"][0][field] = value
            self.assertFalse(self.a.check_response(self.root, self.manifest, p, response)["ok"])
        response = self.response(p); response["suggestions"][0]["selected_target"] = "entities/Hidden.md"
        self.assertFalse(self.a.check_response(self.root, self.manifest, p, response)["ok"])
        response = self.response(p); response["suggestions"][0]["path"] = "../../credentials.json"
        self.assertFalse(self.a.check_response(self.root, self.manifest, p, response)["ok"])
        forged = copy.deepcopy(p); forged["model_input"]["candidates"][0]["spans"][0]["text"] = "tampered"
        self.assertFalse(self.a.check_response(self.root, self.manifest, forged, self.response(p))["ok"])

    def test_target_change_invalidates_snapshot(self):
        p = self.packet(); (self.root / "entities/Fatou.md").write_text("changed", encoding="utf-8")
        self.assertFalse(self.a.check_response(self.root, self.manifest, p, self.response(p))["ok"])

    def test_mixed_and_abstain_do_not_force_atomic_type(self):
        p = self.packet("classify")
        for kind, form in [("classification", "mixed"), ("abstain", "undetermined")]:
            response = self.response(p, kind); item = response["suggestions"][0]
            item.update(form=form, field=None, resolution="not_applicable", candidates=[], selected_target=None)
            self.assertTrue(self.a.check_response(self.root, self.manifest, p, response)["ok"])
            item["primary_type"] = "proposition"
            self.assertFalse(self.a.check_response(self.root, self.manifest, p, response)["ok"])

    def test_new_entity_is_review_only_and_never_wikilink(self):
        p = self.packet(); response = self.response(p, "new_entity_review"); item = response["suggestions"][0]
        item.update(form="undetermined", field=None, resolution="propose_new", candidates=[], selected_target=None,
                    new_entity={"title": "待审新对象", "reason": "范围内未找到；不是全库不存在的结论"})
        result = self.a.check_response(self.root, self.manifest, p, response)
        self.assertTrue(result["ok"], result)
        self.assertNotIn("[[", json.dumps(result))
        item["new_entity"]["title"] = "[[Suspended]]"
        self.assertFalse(self.a.check_response(self.root, self.manifest, p, response)["ok"])

    def test_split_review_requires_real_source_spans(self):
        p = self.packet(); response = self.response(p, "split_review"); item = response["suggestions"][0]
        item.update(form="mixed", field=None, resolution="not_applicable", candidates=[], selected_target=None,
                    segments=[{"label": "保留原件，仅审阅这个单元", "proposed_type": "method", "evidence": item["source_evidence"]}])
        self.assertTrue(self.a.check_response(self.root, self.manifest, p, response)["ok"])
        item["segments"][0]["evidence"][0]["span_id"] = "invented"
        self.assertFalse(self.a.check_response(self.root, self.manifest, p, response)["ok"])

    def test_no_writes_network_credentials_or_model_process(self):
        before = {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*.md")}
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
             patch.object(subprocess, "Popen", side_effect=AssertionError("process")), \
             patch.object(Path, "write_bytes", side_effect=AssertionError("write")), \
             patch.object(Path, "write_text", side_effect=AssertionError("write")):
            p = self.packet(); self.assertTrue(self.a.check_response(self.root, self.manifest, p, self.response(p))["ok"])
        self.assertEqual(before, {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*.md")})

    def test_cli_rejects_mutating_commands_and_prepares_synthetic_only(self):
        manifest_path = self.root / "manifest.json"; manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")
        for name in ["apply", "fix", "migrate", "split"]:
            result = subprocess.run([sys.executable, "-B", str(SYSTEM / "advisory.py"), name], capture_output=True)
            self.assertEqual(result.returncode, 2)
        result = subprocess.run([sys.executable, "-B", str(SYSTEM / "advisory.py"), "prepare", "--vault-root", str(self.root), "--manifest", str(manifest_path)], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(result.stdout)["model_input"]["documents"]), 1)

    def test_large_json_is_rejected_before_reading_its_body(self):
        p = self.root / "large.json"; p.write_bytes(b" " * (4 * 1024 * 1024 + 1))
        with patch.object(Path, "read_bytes", side_effect=AssertionError("oversized read")):
            with self.assertRaises(ValueError):self.a.read_json(p)

    def test_boolean_manifest_version_is_not_integer_one(self):
        self.manifest["manifest_version"] = True
        with self.assertRaises(ValueError):self.packet()

    def test_new_entity_checks_alias_duplicates(self):
        p = self.packet();response = self.response(p, "new_entity_review");item = response["suggestions"][0]
        item.update(form="undetermined",field=None,resolution="propose_new",candidates=[],selected_target=None,
                    new_entity={"title":"Shared","reason":"需要核对已有别名"})
        self.assertFalse(self.a.check_response(self.root,self.manifest,p,response)["ok"])

    def test_existing_short_link_is_not_recommended_twice(self):
        source = self.root / "notes/Source.md"
        source.write_bytes(source.read_bytes().replace(b'type: ', b'uses: ["[[Fatou]]"]\ntype: ', 1))
        self.manifest["samples"][0]["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
        p = self.packet();result = self.a.check_response(self.root,self.manifest,p,self.response(p))
        self.assertTrue(result["ok"],result)
        self.assertEqual(result["results"][0]["status"],"already_present")

    def test_prerequisite_cycle_is_flagged_for_review(self):
        target = self.root / "entities/Fatou.md"
        target.write_bytes(target.read_bytes().replace(b'type: ', b'prerequisites: ["[[notes/Source]]"]\ntype: ', 1))
        self.manifest["samples"][1]["sha256"] = hashlib.sha256(target.read_bytes()).hexdigest()
        p = self.packet();response = self.response(p);response["suggestions"][0]["field"] = "prerequisites"
        result = self.a.check_response(self.root,self.manifest,p,response)
        self.assertTrue(result["ok"],result)
        self.assertIn("prerequisite_cycle",result["results"][0]["review_flags"])

    def test_partial_note_can_abstain_but_cannot_certify_atomic_type(self):
        source = self.root / "notes/Source.md"
        source.write_text("---\ntype: 方法\n---\n# 合成\n" + "较长片段。\n" * 20000,encoding="utf-8")
        self.manifest["samples"][0]["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
        p = self.packet("classify");self.assertEqual(p["model_input"]["documents"][0]["coverage"],"partial")
        self.assertLessEqual(len(p["model_input"]["documents"][0]["spans"]),2000)
        response = self.response(p,"classification");item = response["suggestions"][0]
        item.update(field=None,resolution="not_applicable",candidates=[],selected_target=None,primary_type="method")
        self.assertFalse(self.a.check_response(self.root,self.manifest,p,response)["ok"])
        item.update(kind="abstain",form="undetermined",primary_type=None)
        self.assertTrue(self.a.check_response(self.root,self.manifest,p,response)["ok"])

    def test_duplicate_json_keys_and_nonfinite_values_are_rejected(self):
        p = self.root / "bad.json"
        for value in ['{"id":1,"id":2}','{"value":NaN}']:
            p.write_text(value,encoding="utf-8")
            with self.assertRaises(ValueError):self.a.read_json(p)

    def test_hidden_ambiguous_candidate_cannot_be_declared_unique(self):
        p = self.a.prepare(self.root,self.manifest,stage="relations",queries=["Shared"])
        self.assertEqual(len(p["model_input"]["candidates"]),1)
        self.assertFalse(self.a.check_response(self.root,self.manifest,p,self.response(p))["ok"])

    def test_all_visible_ambiguous_candidates_can_be_reported_without_selection(self):
        self.manifest["scopes"]["model_visible"].append("H")
        p = self.a.prepare(self.root,self.manifest,stage="relations",queries=["Shared"])
        response = self.response(p);item = response["suggestions"][0];item.update(resolution="multiple",selected_target=None)
        doc=p["model_input"]["candidates"][1];span=doc["spans"][1]
        item["candidates"].append({"target_id":doc["id"],"evidence":[{"document_id":doc["id"],"span_id":span["id"],"quote":span["text"]}]})
        result = self.a.check_response(self.root,self.manifest,p,response)
        self.assertTrue(result["ok"],result)
        self.assertEqual(result["results"][0]["status"],"ambiguous_review")

    def test_remote_schema_reference_is_rejected_without_network(self):
        original = self.a.read_json
        def damaged(path):
            value=original(path)
            if Path(path).name=="response.schema.json":value["$ref"]="https://example.invalid/schema"
            return value
        with patch.object(self.a,"read_json",damaged),patch.object(socket,"socket",side_effect=AssertionError("network")):
            with self.assertRaises(ValueError):self.a.schema_validators()


if __name__ == "__main__": unittest.main()
