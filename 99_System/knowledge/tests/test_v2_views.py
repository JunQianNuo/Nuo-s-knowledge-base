"""Recursive MOC and generated native Bases contracts."""
from pathlib import Path
import sys
import tempfile
import unittest

import yaml

SYSTEM = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM))
from v2 import model, views
from test_v2_model import metadata, put


class V2ViewsTests(unittest.TestCase):
    def fixture(self, root):
        put(root, "02_Maps/根.md", metadata("moc"), "\n人工路线：保留。\r\n".encode())
        put(root, "02_Maps/左.md", metadata("moc", topics=["[[02_Maps/根]]"]))
        put(root, "02_Maps/右.md", metadata("moc", topics=["[[02_Maps/根]]"]))
        put(root, "02_Maps/叶.md", metadata("moc", topics=["[[02_Maps/左]]", "[[02_Maps/右]]"]))
        put(root, "01_Knowledge/原子.md", metadata(topics=["[[02_Maps/叶]]"]))
        put(root, "03_Sources/Books/来源.md", metadata("book"))
        put(root, "03_Sources/Courses/数学/PPT课件/课件.pdf", {})
        put(root, "03_Sources/Reviews/跨课程/复习.md", metadata("review", subject=["数学", "统计"]))

    def test_diamond_descendants_and_aggregation_deduplicate(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.fixture(root)
            notes = model.scan(root)
            self.assertEqual(views.descendants(notes, "02_Maps/根.md"), {"02_Maps/左.md", "02_Maps/右.md", "02_Maps/叶.md"})
            result = views.build(root)
            bases = [yaml.safe_load(raw.decode()) for name, raw in result.items() if name.endswith(".base")]
            aggregate = next(b for b in bases if b["views"][0]["name"] == "根：递归原子知识")
            topic_filter = aggregate["filters"]["and"][-1]["or"]
            self.assertIn('topics.contains(link("02_Maps/叶"))', topic_filter)
            self.assertEqual(topic_filter.count('topics.contains(link("02_Maps/叶"))'), 1)
            self.assertNotIn("复习", str(aggregate))
            self.assertIn("人工路线：保留。\r\n".encode(), result["02_Maps/根.md"])
            self.assertEqual((root / "02_Maps/根.md").read_bytes(), model.render_note(metadata("moc"), "\n人工路线：保留。\r\n".encode()))
            (root / "02_Maps/根.md").write_bytes(result["02_Maps/根.md"])
            self.assertEqual(views.build(root)["02_Maps/根.md"], result["02_Maps/根.md"])

    def test_cycles_and_non_moc_topics_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.fixture(root)
            put(root, "02_Maps/根.md", metadata("moc", topics=["[[02_Maps/叶]]"]))
            with self.assertRaisesRegex(ValueError, "cycle|环"):
                views.descendants(model.scan(root), "02_Maps/根.md")
            with self.assertRaises(ValueError):
                views.build(root)
            put(root, "02_Maps/根.md", metadata("moc", topics=["[[03_Sources/Books/来源]]"]))
            with self.assertRaises(ValueError):
                views.build(root)

    def test_databases_and_course_material_filters_use_real_paths(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.fixture(root)
            result = views.build(root)
            self.assertIn("Home.md", result)
            self.assertTrue(any("标签数据库" in key for key in result))
            course = next(yaml.safe_load(raw.decode()) for name, raw in result.items() if name.endswith("课程资料.base"))
            self.assertIn("03_Sources/Courses", str(course["filters"]))
            self.assertIn("subject", str(course))
            for path in result:
                self.assertFalse((root / path).exists() and path.endswith(".base"))

    def test_invalid_atomic_source_is_not_published_in_recursive_view(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.fixture(root)
            put(root, "01_Knowledge/原子.md", metadata(topics=["[[02_Maps/叶]]"], source=["[[missing]]"]))
            with self.assertRaisesRegex(ValueError, "[Ss]ource|来源"):
                views.build(root)

    def test_course_view_excludes_raw_and_nested_project_materials(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.fixture(root)
            put(root, "03_Sources/Courses/数学/raw/原始.md", {})
            put(root, "03_Sources/Courses/数学/project/private.md", {})
            (root / "03_Sources/Courses/数学/project/.git").write_text("gitdir: elsewhere")
            result = views.build(root)
            course = next(yaml.safe_load(raw.decode()) for path, raw in result.items() if path.endswith("课程资料.base"))
            self.assertIn('file.inFolder("03_Sources/Courses")', str(course["filters"]))
            self.assertIn('file.inFolder("03_Sources/Courses/数学/project")', str(course["filters"]))
            self.assertIn("raw", str(course["filters"]))
            self.assertNotIn("private.md", str(course))

    def test_archived_course_materials_are_available_in_the_actual_course_view(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.fixture(root)
            put(root, "03_Sources/Courses/归档/最优化方法/PPT课件/第一章.pdf", {})
            result = views.build(root)
            course = next(yaml.safe_load(raw.decode()) for path, raw in result.items() if path.endswith("课程资料.base"))
            archived = next((view for view in course["views"] if view["name"] == "最优化方法"), None)
            self.assertIsNotNone(archived)
            self.assertIn("归档/最优化方法", str(archived["filters"]))

    def test_new_notes_are_visible_without_regenerating_database_filters(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.fixture(root)
            before = views.build(root)
            put(root, "01_Knowledge/新增原子.md", metadata(topics=["[[02_Maps/叶]]"]))
            put(root, "02_Maps/新增顶层.md", metadata("moc"))
            put(root, "03_Sources/Books/新增来源.md", metadata("book"))
            put(root, "03_Sources/Courses/数学/PPT课件/新增.pdf", {})
            after = views.build(root)
            for suffix in ("主题数据库.base", "来源管理.base", "课程资料.base"):
                key = next(path for path in before if path.endswith(suffix))
                self.assertEqual(before[key], after[key])
            key = next(path for path, raw in before.items() if path.endswith(".base") and "根：递归原子知识" in raw.decode())
            self.assertEqual(before[key], after[key])

    def test_independent_source_scope_is_disabled_in_dynamic_queries(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "03_Sources").mkdir()
            (root / "03_Sources/.git").write_text("gitdir: elsewhere")
            result = views.build(root)
            source = next(yaml.safe_load(raw.decode()) for path, raw in result.items() if path.endswith("来源管理.base"))
            self.assertIn("false", source["filters"]["and"])


if __name__ == "__main__":
    unittest.main()
