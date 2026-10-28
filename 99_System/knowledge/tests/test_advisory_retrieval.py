import copy
import importlib
from pathlib import Path
import unittest
from test_advisory import AdvisoryFixture


class RetrievalTests(AdvisoryFixture):
    def catalog(self):
        self.r = importlib.import_module("advisory_retrieval")
        return self.r.build_catalog(self.root, self.manifest)

    def test_unique_ambiguous_missing_are_separate(self):
        cat = self.catalog()
        self.assertEqual(self.r.retrieve(cat, "Fatou")["state"], "unique")
        shared = self.r.retrieve(cat, "Shared")
        self.assertEqual(shared["state"], "multiple")
        self.assertIsNone(shared["selected_id"])
        self.assertEqual(self.r.retrieve(cat, "不存在的词项ZZZ")["state"], "not_found")

    def test_legacy_is_not_a_canonical_proposition(self):
        cat = self.catalog(); matches = self.r.retrieve(cat, "Fatou")["candidates"]
        self.assertEqual(matches[0]["eligibility"], "legacy_candidate")
        self.assertIsNone(matches[0]["canonical_type"])
        self.assertNotIn("非负函数列", str(matches))

    def test_paths_and_scope_ids_cannot_escape_manifest(self):
        for name in ["../outside.md", "/absolute.md", "C:/secret.md", "notes/../secret.md", "notes\\Source.md"]:
            manifest = copy.deepcopy(self.manifest); manifest["samples"][0]["path"] = name
            with self.assertRaises(ValueError): self.a.prepare(self.root, manifest)
        manifest = copy.deepcopy(self.manifest); manifest["scopes"]["model_visible"].append("UNKNOWN")
        with self.assertRaises(ValueError): self.a.prepare(self.root, manifest)

    def test_system_files_are_reported_and_never_entities_or_payloads(self):
        p = self.root / "99_System/Fake.md"; p.parent.mkdir(); p.write_text("---\ntype: concept\n---\nSYSTEM_SENTINEL", encoding="utf-8")
        import hashlib
        self.manifest["samples"].append({"sample_id": "SYS", "path": "99_System/Fake.md", "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "stratum": "synthetic", "group": "system", "partition": "development", "phase3_familiar": False})
        for scope in self.manifest["scopes"].values():scope.append("SYS")
        packet = self.packet()
        self.assertNotIn("SYSTEM_SENTINEL", str(packet))
        self.assertTrue(any(e["reason"] == "system_file" for e in packet["audit"]["exclusions"]))
        self.assertEqual(packet["audit"]["knowledge_entities"], 0)

    def test_unlisted_body_is_not_read(self):
        (self.root / "unlisted.md").write_text("NOT_AUTHORIZED", encoding="utf-8")
        from unittest.mock import patch
        original = Path.read_bytes
        def guarded(path):
            if path.name == "unlisted.md":raise AssertionError("unlisted body read")
            return original(path)
        with patch.object(Path, "read_bytes", guarded):self.packet()

    def test_caret_is_filename_and_links_use_existing_parser(self):
        import hashlib
        name = "entities/L^p.md"; p = self.root / name;p.write_text("---\ntype: concept\n---\n# Lp\nLp 合成对象", encoding="utf-8")
        self.manifest["samples"][1].update(path=name, sha256=hashlib.sha256(p.read_bytes()).hexdigest())
        packet = self.a.prepare(self.root, self.manifest, stage="relations", queries=["L^p"])
        response = self.response(packet)
        result = self.a.check_response(self.root, self.manifest, packet, response)
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["results"][0]["link_status"], "resolved")

    def test_source_evidence_has_real_crlf_bom_positions(self):
        import hashlib
        p = self.root / "notes/Source.md";raw=b'\xef\xbb\xbf'+"---\r\ntype: 方法\r\n---\r\n# 合成\r\n动作一。\r\n".encode();p.write_bytes(raw)
        self.manifest["samples"][0]["sha256"] = hashlib.sha256(raw).hexdigest()
        packet = self.packet();span = packet["model_input"]["documents"][0]["spans"][-1]
        self.assertEqual((span["start_line"], span["start_column"], span["text"]), (5, 1, "动作一。"))

    def test_expanding_local_retrieval_does_not_expand_model_view(self):
        self.manifest["scopes"]["retrieval"] = ["T"]
        first = self.packet()
        self.manifest["scopes"]["retrieval"].append("H")
        second = self.packet()
        self.assertEqual(first["model_input"],second["model_input"])
        self.assertEqual(second["audit"]["scopes"]["retrieval"]["included"],["T","H"])

    def test_symlink_or_junction_is_excluded_before_body_read(self):
        from unittest.mock import patch
        r = importlib.import_module("advisory_retrieval");original=r.links.protected_reason
        def protected(root,path):
            return "symlink_or_junction" if path.name=="Hidden.md" else original(root,path)
        original_read=Path.read_bytes
        def guarded(path):
            if path.name=="Hidden.md":raise AssertionError("protected target read")
            return original_read(path)
        with patch.object(r.links,"protected_reason",protected),patch.object(Path,"read_bytes",guarded):
            packet=self.packet()
        self.assertTrue(any(x["reason"]=="symlink_or_junction" for x in packet["audit"]["exclusions"]))

    def test_navigation_target_is_topic_only(self):
        import hashlib
        p=self.root/"entities/Fatou.md";text=p.read_text(encoding="utf-8").replace("type: 知识点","schema_version: 1\nrole: moc")
        p.write_text(text,encoding="utf-8");self.manifest["samples"][1]["sha256"]=hashlib.sha256(p.read_bytes()).hexdigest()
        packet=self.packet();response=self.response(packet)
        self.assertFalse(self.a.check_response(self.root,self.manifest,packet,response)["ok"])
        response["suggestions"][0]["field"]="topics"
        self.assertTrue(self.a.check_response(self.root,self.manifest,packet,response)["ok"])

    def test_long_single_line_keeps_locatable_prefix_for_abstention(self):
        import hashlib
        p=self.root/"notes/Source.md";p.write_text("---\ntype: 方法\n---\n"+"长"*9000,encoding="utf-8")
        self.manifest["samples"][0]["sha256"]=hashlib.sha256(p.read_bytes()).hexdigest()
        packet=self.packet("classify");doc=packet["model_input"]["documents"][0]
        self.assertEqual(doc["coverage"],"partial")
        self.assertEqual(len(doc["spans"]),1)
        self.assertEqual(len(doc["spans"][0]["text"]),8192)
        self.assertEqual((doc["spans"][0]["start_line"],doc["spans"][0]["end_column"]),(4,8193))


if __name__ == "__main__":unittest.main()
