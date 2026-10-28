import importlib
from pathlib import Path
import sys
import tempfile
import unittest

SYSTEM = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM))
from v2 import model, transaction


class V2TagsTests(unittest.TestCase):
    def setUp(self):
        try:
            self.tags = importlib.import_module("v2.tags")
        except ModuleNotFoundError:
            self.fail("V2 tags helper missing")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "vault"
        self.root.mkdir()

    def record(self, name, canonical, aliases=(), **fields):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        data = {"canonical_tag": canonical, "tag_aliases": list(aliases), **fields}
        path.write_bytes(model.render_note(data, b"\r\nUser evidence ^tag\r\n"))
        return path

    def test_aliases_normalize_but_unknown_and_ambiguous_names_stay_unchanged(self):
        self.record("99_System/knowledge/tags/条目/标签-数学.md", "数学", ["math", "ambiguous"])
        self.record("99_System/knowledge/tags/条目/标签-统计.md", "统计", ["stats", "ambiguous"], ambiguous_aliases=["stats"])
        registry = self.tags.load(self.root)
        self.assertEqual(self.tags.canonicalize(registry, ["math", "数学", "unknown", "ambiguous", "stats"]), ["数学", "unknown", "ambiguous", "stats"])

    def test_legacy_vocabulary_is_read_without_moving_records(self):
        path = self.record("总览/标签库/条目/标签-数学.md", "数学", ["math"], promote=False, source_kind="legacy")
        before = path.read_bytes()
        registry = self.tags.load(self.root)
        self.assertEqual(self.tags.canonicalize(registry, ["math"]), ["数学"])
        self.assertEqual(path.read_bytes(), before)

    def test_alias_can_keep_mathematical_name_that_is_not_a_legal_tag(self):
        result=self.tags.register(self.root,'Lp空间',['L^p空间'])
        data,_=model.read_note(result['operations'][0]['content'])
        self.assertEqual(data['tag_aliases'],['L^p空间'])

    def test_registration_returns_expected_hash_operation_and_does_not_write(self):
        result = self.tags.register(self.root, "数学/分析", ["analysis"])
        self.assertEqual(result["canonical"], "数学/分析")
        self.assertFalse(result["existing"])
        self.assertEqual(len(result["operations"]), 1)
        op = result["operations"][0]
        self.assertIsNone(op["source"])
        self.assertIsNone(op["expected_sha256"])
        self.assertFalse((self.root / op["target"]).exists())
        data, _ = model.read_note(op["content"])
        self.assertEqual(data["canonical_tag"], "数学/分析")
        self.assertEqual(data["tag_aliases"], ["analysis"])
        self.assertNotIn("type", data)

    def test_alias_collision_is_rejected_and_existing_record_preserves_evidence(self):
        path = self.record("99_System/knowledge/tags/条目/标签-数学.md", "数学", ["math"], custom={"keep": True}, source_kind="manual")
        self.record("99_System/knowledge/tags/条目/标签-统计.md", "统计", ["stats"])
        with self.assertRaises(ValueError):
            self.tags.register(self.root, "新词", ["stats"])
        result = self.tags.register(self.root, "math", ["mathematics"])
        self.assertTrue(result["existing"])
        self.assertEqual(result["canonical"], "数学")
        data, body = model.read_note(result["operations"][0]["content"])
        self.assertEqual(data["custom"], {"keep": True})
        self.assertEqual(data["source_kind"], "manual")
        self.assertEqual(body, model.read_note(path.read_bytes())[1])
        self.assertIsNotNone(result["operations"][0]["expected_sha256"])
        self.assertEqual(self.tags.register(self.root, "math")["operations"], [])

    def test_explicit_normalization_changes_only_tags_and_preserves_unknowns(self):
        self.record("99_System/knowledge/tags/条目/标签-数学.md", "数学", ["math"])
        path = self.root / "03_Sources/Ideas/想法.md"
        path.parent.mkdir(parents=True)
        raw = b'---\r\ntype: idea\r\nstatus: not done\r\ntags: ["math", "unknown"] # keep\r\ncustom: true\r\n---\r\nBody ^block  \r\n'
        path.write_bytes(raw)
        operations = self.tags.normalize(self.root, ["03_Sources/Ideas/想法.md"])
        self.assertEqual(len(operations), 1)
        self.assertEqual(path.read_bytes(), raw)
        self.assertEqual(operations[0]["content"], raw.replace(b'["math", "unknown"]', '["数学", "unknown"]'.encode()))
        with self.assertRaises(ValueError):
            self.tags.normalize(self.root, ["03_Sources/Ideas/raw/not-a-note.md"])


if __name__ == "__main__":
    unittest.main()
