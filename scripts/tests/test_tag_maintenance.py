import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE = Path(__file__).resolve().parents[1] / "tag_maintenance.py"
spec = importlib.util.spec_from_file_location("tag_maintenance", MODULE)
tm = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = tm
spec.loader.exec_module(tm)


class TagMaintenanceTests(unittest.TestCase):
    def registry(self):
        return tm.Registry([
            tm.Entry("极大似然估计", ("最大似然估计", "极大似然估计法")),
            tm.Entry("控制收敛定理", ("DCT", "Lebesgue控制收敛定理"),
                     ambiguous_aliases=("DCT",), alias_context=("实变函数", "Lebesgue", "控制函数")),
            tm.Entry("KKT条件", ("KKT",)),
        ])

    def test_tag_characters_and_case_collisions(self):
        for tag in ("2026复习", "KKT条件", "统计/估计", "高斯-牛顿法"):
            self.assertTrue(tm.valid_tag(tag), tag)
        for tag in ("2026", "L^p空间", "a b", "", "#牛顿法"):
            self.assertFalse(tm.valid_tag(tag), tag)
        with self.assertRaises(ValueError):
            tm.Registry([tm.Entry("KKT"), tm.Entry("kkt")])
        with self.assertRaises(ValueError):
            tm.Registry([tm.Entry("甲", ("共同名",)), tm.Entry("乙", ("共同名",))])

    def test_exact_metadata_match_and_topics_preserved(self):
        before = "---\ntopics: [最大似然估计, KKT矩阵]\nstatus: 学习中\n---\n正文 $x$\n".encode()
        after = tm.plan_note(before, "课程/统计/笔记.md", self.registry())
        self.assertEqual(after, before)
        self.assertEqual(tm.metadata(after)["topics"], ["最大似然估计", "KKT矩阵"])
        self.assertEqual(after.split(b"---", 2)[2], before.split(b"---", 2)[2])

    def test_dct_alias_requires_context(self):
        raw = "---\ntags: [DCT]\ntopics: [DCT]\n---\nbody".encode()
        self.assertEqual(tm.plan_note(raw, "课程/深度学习/笔记.md", self.registry()), raw)
        self.assertEqual(tm.plan_note(raw, "课程/实变函数/笔记.md", self.registry()), raw)

    def test_preserves_bom_crlf_comments_and_other_properties(self):
        raw = '\ufeff---\r\n# 元数据注释\r\ntags: [极大似然估计法, 极大似然估计]\r\ntopics: [最大似然估计]\r\nsource: "[[原笔记]]"\r\n---\r\n正文 `代码`\r\n'.encode()
        after = tm.plan_note(raw, "课程/笔记.md", self.registry())
        self.assertTrue(after.startswith(b"\xef\xbb\xbf"))
        self.assertIn("# 元数据注释\r\n".encode(), after)
        self.assertEqual(tm.metadata(after)["tags"], ["极大似然估计"])
        self.assertEqual(after.split(b"---", 2)[2], raw.split(b"---", 2)[2])
        self.assertNotIn(b"\n", after.replace(b"\r\n", b""))
        old, new = tm.metadata(raw), tm.metadata(after)
        old.pop("tags"); new.pop("tags")
        self.assertEqual(old, new)

    def test_atom_title_is_explicit_metadata_and_idempotent(self):
        raw = "---\ntitle: 极大似然估计法\ntype: 方法\ntopics: []\n---\n内容".encode()
        after = tm.plan_note(raw, "方法/极大似然估计法.md", self.registry())
        self.assertEqual(after, raw)
        self.assertEqual(tm.plan_note(after, "方法/极大似然估计法.md", self.registry()), after)
        self.assertEqual(tm.plan_note(b"no frontmatter", "方法/笔记.md", self.registry()), b"no frontmatter")

    def test_existing_unrelated_tags_and_custom_fields_survive(self):
        raw = "---\ntags:\n  - 自定义概念\nknowledge_tags: [KKT]\nmethod_tags: [未登记方法]\n---\n正文".encode()
        after = tm.plan_note(raw, "课程/笔记.md", self.registry())
        self.assertEqual(tm.metadata(after)["tags"], ["自定义概念"])
        self.assertEqual(tm.metadata(after)["method_tags"], ["未登记方法"])

    def test_comment_after_block_tags_survives(self):
        raw = "---\ntags:\n  - 最大似然估计\n# subject explains source\nsubject: 统计\n---\n正文".encode()
        after = tm.plan_note(raw, "课程/统计.md", self.registry())
        self.assertIn(b"# subject explains source\nsubject:", after)
        self.assertEqual(tm.metadata(after)["tags"], ["极大似然估计"])

    def test_apply_preflight_rejects_stale_batch_and_backs_up_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "vault"; root.mkdir()
            a, b = root / "a.md", root / "b.md"
            raw = b"---\ntags: [KKT]\n---\nbody"
            after = tm.plan_note(raw, "a.md", self.registry())
            a.write_bytes(raw); b.write_bytes(raw)
            changes = [tm.Change(a, raw, after), tm.Change(b, raw, after)]
            b.write_bytes(b"new user edit")
            with self.assertRaises(RuntimeError):
                tm.apply_changes(root, changes, Path(td) / "stale", registry=self.registry())
            self.assertEqual(a.read_bytes(), raw)
            b.write_bytes(raw)
            manifest = tm.apply_changes(root, changes, Path(td) / "backup", registry=self.registry())
            self.assertEqual(a.read_bytes(), after)
            self.assertEqual((manifest.parent / "files/a.md").read_bytes(), raw)

    def test_new_and_mixed_metadata_skip_with_reasons(self):
        for marker in ("schema_version: 1", "schema_version: 99", "type: concept", "role: moc", 'topics: [旧词, "[[主题]]"]', "uses: []", "prerequisites: []", "about: []"):
            with self.subTest(marker=marker):
                raw = ("---\n" + marker + "\ntags: [KKT]\n---\nbody").encode()
                self.assertIsNotNone(tm.legacy_skip_reason(tm.metadata(raw)))
                self.assertEqual(tm.plan_note(raw, "课程/合成.md", self.registry()), raw)

    def test_old_plans_cannot_bypass_execution_policy(self):
        for raw, after in [(b'---\ntype: concept\ntags: [KKT]\n---\nbody', b'---\ntype: concept\ntags: [KKTconditions]\n---\nbody'), (b'---\ntopics: [KKT]\n---\nbody', b'---\ntopics: [KKT]\ntags: [KKTconditions]\n---\nbody')]:
            with self.subTest(raw=raw), tempfile.TemporaryDirectory() as td:
                root = Path(td); path = root / "note.md"; path.write_bytes(raw)
                backup = root / "backup"
                with self.assertRaises(RuntimeError):
                    tm.apply_changes(root, [tm.Change(path, raw, after)], backup, registry=self.registry())
                self.assertEqual(path.read_bytes(), raw)
                self.assertFalse(backup.exists())

    def test_skip_report_and_duplicate_keys(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); (root / "概念").mkdir()
            (root / "概念/v1.md").write_text('---\ntype: concept\ntags: [KKT]\n---\n', encoding="utf-8")
            skipped = []
            changes, errors = tm.plan_vault(root, self.registry(), skipped=skipped)
            self.assertFalse(changes); self.assertFalse(errors)
            self.assertEqual(len(skipped), 1); self.assertTrue(skipped[0]["reason"])
        with self.assertRaises(ValueError):tm.metadata(b'---\ntype: concept\ntype: legacy\n---\n')


if __name__ == "__main__":
    unittest.main()
