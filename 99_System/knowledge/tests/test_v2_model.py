"""V2 note contracts, with all fixtures outside the live vault."""
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

SYSTEM = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM))
from v2 import model


def metadata(kind="concept", **fields):
    data = {"schema_version": 2, "type": kind, "time": "2026-10-28T10:00:00+08:00"}
    if kind in ("concept", "proposition", "method"):
        data.update(topics=["[[02_Maps/数学]]"], source=["[[03_Sources/Books/来源]]"])
    elif kind == "moc":
        data.update(topics=[], aliases=[], tags=[])
    elif kind != "idea":
        data.update(status="not done", source=["真实资料"], subject=["数学"])
        if kind in ("book", "paper", "web"):
            data["source_title"] = "真实资料原题"
    data.update(fields)
    return data


def put(root, path, data, body=b"\n# synthetic\n"):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(("---\n" + yaml.safe_dump(data, allow_unicode=True, sort_keys=False) + "---\n").encode() + body)
    return target


class V2ModelTests(unittest.TestCase):
    def test_all_eleven_types_and_extensions(self):
        for kind in ("concept", "proposition", "method", "moc", "lecture", "review", "homework", "book", "paper", "web", "idea"):
            with self.subTest(kind=kind):
                self.assertEqual(model.validate(metadata(kind, custom={"保留": [1, 2]})), [])

    def test_required_atomic_links_and_timezone(self):
        for changes, field in (({"topics": []}, "topics"), ({"source": []}, "source"), ({"time": "2026-02-30T10:00:00+08:00"}, "time"), ({"time": "2026-10-28T10:00:00"}, "time"), ({"topics": ["数学"]}, "topics"), ({"source": ["[[x#heading]]"]}, "source"), ({"schema_version": 1}, "schema_version"), ({"subject": ["数学"]}, "subject")):
            with self.subTest(changes=changes):
                self.assertIn(field, {d["field"] for d in model.validate(metadata(**changes))})

    def test_literal_caret_filename_is_a_whole_note_but_aliases_are_not(self):
        self.assertEqual(model.link_target("[[01_Knowledge/L^p空间]]"), "01_Knowledge/L^p空间.md")
        self.assertIsNone(model.link_target("[[01_Knowledge/L^p空间|显示名]]"))
        self.assertIsNone(model.link_target("[[01_Knowledge/L^p空间#^block]]"))

    def test_source_note_constraints_and_manual_idea(self):
        for changes, field in (({"subject": "数学"}, "subject"), ({"status": "已整理"}, "status"), ({"polish_status": "草稿"}, "polish_status"), ({"lecture_date": "2026-02-30"}, "lecture_date")):
            self.assertIn(field, {d["field"] for d in model.validate(metadata("lecture", **changes))})
        self.assertTrue(model.validate(metadata("paper", source_title="")))
        self.assertTrue(model.validate(metadata("lecture", subject=[])))
        self.assertTrue(model.validate(metadata("review", topics=["[[数学]]"])))
        self.assertEqual(model.validate({"type": "idea", "whatever": "手工"}), [])

    def test_moc_aliases_and_tags_are_optional(self):
        self.assertEqual(model.validate({"schema_version": 2, "type": "moc", "time": "2026-10-28T10:00:00+08:00", "topics": []}), [])

    def test_roundtrip_preserves_original_body_and_extension(self):
        body = "\r\n中文 $x$ ^block\r\n".encode()
        raw = b"\xef\xbb\xbf---\r\ntype: idea\r\ncustom: [a, b]\r\n---\r\n" + body
        data, original = model.read_note(raw)
        self.assertEqual(original, body)
        data["status"] = "not done"
        self.assertEqual(model.read_note(model.render_note(data, original)), (data, body))
        with self.assertRaises((ValueError, yaml.YAMLError)):
            model.read_note(b"---\ntype: idea\ntype: concept\n---\n")

    def test_scan_and_audit_exclude_system_raw_assets_and_nested_repositories(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            put(root, "01_Knowledge/A.md", metadata())
            put(root, "02_Maps/数学.md", metadata("moc"))
            put(root, "03_Sources/Books/来源.md", metadata("book"))
            for path in ("99_System/fake.md", "04_Assets/fake.md", "03_Sources/Courses/数学/raw/fake.md", "03_Sources/Courses/数学/PPT课件/MD/fake.md", "03_Sources/Books/project/fake.md"):
                put(root, path, metadata())
            (root / "03_Sources/Books/project/.git").write_text("gitdir: elsewhere")
            self.assertEqual(set(model.scan(root)), {"01_Knowledge/A.md", "02_Maps/数学.md", "03_Sources/Books/来源.md"})
            report = model.audit(root)
            self.assertEqual(report["errors"], 0, report)
            self.assertEqual(report["counts"]["concept"], 1)

    def test_audit_rejects_non_moc_topics_and_atomic_or_raw_sources(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            put(root, "01_Knowledge/A.md", metadata(topics=["[[03_Sources/Books/来源]]"], source=["[[01_Knowledge/B]]"]))
            put(root, "01_Knowledge/B.md", metadata(source=["[[03_Sources/Books/raw]]"]))
            put(root, "02_Maps/数学.md", metadata("moc"))
            put(root, "03_Sources/Books/来源.md", metadata("book"))
            put(root, "03_Sources/Books/raw.md", {"title": "untyped converted material"})
            report = model.audit(root)
            codes = {d["code"] for d in report["diagnostics"]}
            self.assertIn("E_TOPIC_TARGET", codes)
            self.assertIn("E_SOURCE_TARGET", codes)

    def test_ambiguous_short_links_are_not_silently_resolved(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            put(root, "01_Knowledge/A.md", metadata(topics=["[[数学]]"]))
            put(root, "02_Maps/a/数学.md", metadata("moc"))
            put(root, "02_Maps/b/数学.md", metadata("moc"))
            put(root, "03_Sources/Books/来源.md", metadata("book"))
            self.assertIn("E_LINK_AMBIGUOUS", {d["code"] for d in model.audit(root)["diagnostics"]})

    def test_invalid_relationships_are_excluded_from_valid_entity_counts(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            put(root, "01_Knowledge/A.md", metadata(source=["[[missing]]"]))
            put(root, "02_Maps/数学.md", metadata("moc"))
            report = model.audit(root)
            self.assertEqual(report["counts"]["concept"], 0)
            self.assertEqual(report["counts"]["entities"], 1)

    def test_moc_cycle_is_not_counted_as_valid_navigation(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            put(root, "02_Maps/数学.md", metadata("moc", topics=["[[02_Maps/数学]]"]))
            self.assertEqual(model.audit(root)["counts"]["moc"], 0)

    def test_templates_remain_distinct_from_real_note_validation(self):
        for path in (SYSTEM / "v2/templates").glob("*.md"):
            data, _ = model.read_note(path.read_bytes())
            self.assertEqual(data["schema_version"], 2)
        self.assertEqual(len(list((SYSTEM / "v2/templates").glob("*.md"))), 11)


if __name__ == "__main__":
    unittest.main()
