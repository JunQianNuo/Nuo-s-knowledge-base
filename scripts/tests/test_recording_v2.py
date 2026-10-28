"""Offline fixtures for recording paths, source evidence and polish status."""
import datetime as dt
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

from scripts import pull_tmeet_recordings as recordings


def metadata(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8").split("---", 2)[1])


class RecordingV2Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        previous = recordings.VAULT
        recordings.set_vault(self.root)
        self.addCleanup(recordings.set_vault, previous)
        self.notes = self.root / "03_Sources/Courses/统计/课堂笔记"
        (self.notes / "raw").mkdir(parents=True)

    def material(self, name):
        (self.notes / "raw" / name).write_text("实际素材", encoding="utf-8")
        return "raw/" + name

    def placeholder(self, transcript="raw/缺失逐字稿.md", minutes="raw/缺失纪要.md"):
        return Path(recordings.write_placeholder(
            str(self.notes), "2026-10-23", 4, "统计", "充分统计量", "001234567",
            transcript, minutes, "2026-10-23T14:30:00+08:00"))

    def test_new_lecture_uses_creation_time_real_sources_and_independent_states(self):
        transcript = self.material("第一段-逐字稿.md")
        before = dt.datetime.now(dt.timezone(dt.timedelta(hours=8)))
        note = self.placeholder(transcript)
        after = dt.datetime.now(dt.timezone(dt.timedelta(hours=8)))
        data = metadata(note)
        self.assertEqual(data.get("schema_version"), 2)
        self.assertEqual(data.get("type"), "lecture")
        self.assertNotIn("title", data)
        self.assertEqual(data["subject"], ["统计"])
        self.assertEqual(str(data["lecture_date"]), "2026-10-23")
        created = dt.datetime.fromisoformat(data["time"])
        self.assertLessEqual(before, created)
        self.assertLessEqual(created, after)
        self.assertEqual(created.utcoffset(), dt.timedelta(hours=8))
        self.assertEqual(data["status"], "not done")
        self.assertEqual(data["polish_status"], "not done")
        self.assertEqual(data["source"], [
            "[[03_Sources/Courses/统计/课堂笔记/raw/第一段-逐字稿.md]]"])
        self.assertEqual(str(data["meeting_code"]), "001234567")
        self.assertNotIn("缺失纪要", note.read_text(encoding="utf-8"))

    def test_append_segment_updates_yaml_sources_and_preserves_custom_metadata(self):
        note = self.placeholder(self.material("第一段.md"))
        original = note.read_text(encoding="utf-8").replace(
            "\nclass_no:", '\nrecord_file_ids: ["original-id"]\ncustom: {keep: true}\nclass_no:')
        note.write_text(original, encoding="utf-8")
        old_time = metadata(note).get("time")
        self.placeholder(self.material("第二段.md"), self.material("第二段纪要.md"))
        data = metadata(note)
        self.assertIn("[[03_Sources/Courses/统计/课堂笔记/raw/第二段.md]]", data["source"])
        self.assertIn("[[03_Sources/Courses/统计/课堂笔记/raw/第二段纪要.md]]", data["source"])
        self.assertEqual(data["record_file_ids"], ["original-id"])
        self.assertEqual(data["custom"], {"keep": True})
        self.assertEqual(data.get("time"), old_time)
        once = note.read_bytes()
        self.placeholder("raw/第二段.md", "raw/第二段纪要.md")
        self.assertEqual(note.read_bytes(), once)

    def test_legacy_note_keeps_status_title_body_and_sources_when_appending(self):
        note = self.notes / "2026-10-23-第4节-旧主题.md"
        note.write_text('---\ntitle: 历史标题\nsubject: 统计\nstatus: 已完成\n'
                        'record_file_id: old-id\ncustom: 保留\nsource: 原始来源说明\n---\n'
                        '# 手工正文 ^block\n\n## 课堂内容梳理\n\n已整理内容\n', encoding="utf-8")
        self.placeholder(self.material("补充.md"))
        data = metadata(note)
        self.assertEqual(data["title"], "历史标题")
        self.assertEqual(data["status"], "已完成")
        self.assertEqual(data["record_file_id"], "old-id")
        self.assertIn("原始来源说明", data["source"])
        self.assertIn("[[03_Sources/Courses/统计/课堂笔记/raw/补充.md]]", data["source"])
        self.assertIn("# 手工正文 ^block", note.read_text(encoding="utf-8"))
        self.assertNotIn("schema_version", data)

    def test_append_supports_legacy_unindented_yaml_list_and_retains_body_bytes(self):
        note = self.notes / "2026-10-23-第4节-旧主题.md"
        note.write_bytes(('---\r\nstatus: 待润色\r\nsource:\r\n- "原始来源"\r\n'
                          'custom: {keep: true}\r\n---\r\n# 手写\r\n'
                          '公式 $x$ ^anchor  \r\n\r\n\r\n').encode("utf-8"))
        self.placeholder(self.material("补充.md"))
        data = metadata(note)
        self.assertEqual(data["source"], ["原始来源", "[[03_Sources/Courses/统计/课堂笔记/raw/补充.md]]"])
        self.assertEqual(data["custom"], {"keep": True})
        self.assertIn("# 手写\r\n公式 $x$ ^anchor  \r\n\r\n\r\n".encode("utf-8"), note.read_bytes())

    def test_new_material_reopens_v2_polishing_and_extraction_without_changing_time(self):
        note = self.placeholder(self.material("a.md"))
        note.write_text(note.read_text(encoding="utf-8").replace("status: not done", "status: done"), encoding="utf-8")
        created = metadata(note)["time"]
        before = note.read_bytes()
        self.placeholder("raw/a.md")
        self.assertEqual(note.read_bytes(), before)
        self.placeholder(self.material("b.md"))
        self.assertEqual(metadata(note)["status"], "not done")
        self.assertEqual(metadata(note)["polish_status"], "not done")
        self.assertEqual(metadata(note)["time"], created)

    def test_consolidation_keeps_manual_body_in_duplicate_placeholder(self):
        a = self.placeholder(self.material("a.md"))
        b = self.notes / "2026-10-23-第4节-录音文件.md"
        b.write_text(a.read_text(encoding="utf-8") + "\n用户批注 ^user\n", encoding="utf-8")
        before = {p: p.read_bytes() for p in (a, b)}
        self.assertFalse(recordings.consolidate_placeholders(str(self.notes)))
        self.assertEqual({p: p.read_bytes() for p in (a, b)}, before)

    def test_duplicate_yaml_source_fields_are_rejected_without_overwrite(self):
        note = self.notes / "2026-10-23-第4节-旧主题.md"
        note.write_text('---\nstatus: 待润色\nsource: 第一来源\nsource: 第二来源\n---\n正文\n', encoding="utf-8")
        before = note.read_bytes()
        with self.assertRaises(ValueError):
            self.placeholder(self.material("补充.md"))
        self.assertEqual(note.read_bytes(), before)

    def test_readme_uses_polish_state_and_never_body_or_extraction_status(self):
        for index, (fields, expected) in enumerate([
            ('schema_version: 2\nstatus: done\npolish_status: "not done"', "待润色"),
            ('schema_version: 2\nstatus: not done\npolish_status: done', "已润色"),
            ('schema_version: 2\nstatus: done', "待润色"),
            ('status: 已完成', "已完成"),
        ], start=1):
            note = self.notes / f"2026-10-23-第{index}节-测试.md"
            note.write_text(f"---\n{fields}\n---\nstatus: body-value\n", encoding="utf-8")
        entries = recordings.rebuild_readme(str(self.notes), "统计")
        self.assertEqual([item[3] for item in entries], ["待润色", "已润色", "待润色", "已完成"])
        self.assertIn("polish_status", (self.notes / "README.md").read_text(encoding="utf-8"))

    def test_readme_refresh_preserves_manual_subject_status_and_surrounding_notes(self):
        self.placeholder(self.material("a.md"))
        readme = self.notes / "README.md"
        manual = ("# 统计 课堂笔记\n\n用户说明 ^manual\n\n## 课程记录\n\n"
                  "| 日期 | 节次 | 主题 | 状态 |\n|:--|:--|:--|:--|\n"
                  "| 2026-10-23 | 第4节 | [[讲评\\|人工题注]] | 已完成（原表待核） |\n"
                  "| 2026-10-24 | 第5节 | 手工补充 | 等待录入 |\n\n## 补充\n用户结论\n")
        readme.write_text(manual, encoding="utf-8")
        recordings.rebuild_readme(str(self.notes), "统计")
        actual = readme.read_text(encoding="utf-8")
        for text in ("用户说明 ^manual", "[[讲评\\|人工题注]]", "已完成（原表待核）", "手工补充", "## 补充\n用户结论"):
            self.assertIn(text, actual)
        self.assertIn("润色状态", actual)
        recordings.rebuild_readme(str(self.notes), "统计")
        self.assertEqual(readme.read_text(encoding="utf-8"), actual)

    def test_consolidation_preserves_all_sources_but_skips_polished_or_custom_conflicts(self):
        a = self.placeholder(self.material("a.md"))
        b = self.notes / "2026-10-23-第4节-录音文件.md"
        other = a.read_text(encoding="utf-8").replace("raw/a.md", "raw/b.md")
        self.material("b.md")
        b.write_text(other, encoding="utf-8")
        self.assertTrue(recordings.consolidate_placeholders(str(self.notes)))
        self.assertFalse(b.exists())
        self.assertIn("[[03_Sources/Courses/统计/课堂笔记/raw/b.md]]", metadata(a)["source"])
        b.write_text(other.replace("polish_status: not done", "polish_status: done"), encoding="utf-8")
        before = {p: p.read_bytes() for p in (a, b)}
        self.assertFalse(recordings.consolidate_placeholders(str(self.notes)))
        self.assertEqual({p: p.read_bytes() for p in (a, b)}, before)
        b.write_text(other.replace("\nclass_no:", "\nrecord_file_id: distinct-id\nclass_no:"), encoding="utf-8")
        before = {p: p.read_bytes() for p in (a, b)}
        self.assertFalse(recordings.consolidate_placeholders(str(self.notes)))
        self.assertEqual({p: p.read_bytes() for p in (a, b)}, before)

    def run_archive(self, course):
        record = {"media_start_time": "2026-10-23T14:30:00+08:00", "subject": "统计录音",
                  "record_files": [{"record_file_id": "record-123456", "record_start_time": "start", "record_end_time": "end"}],
                  "meeting_record_id": "recording-id", "meeting_id": "meeting-id", "meeting_code": "001234567"}
        with patch.object(recordings, "load_timetable", return_value=None), \
             patch.object(recordings, "match_course", return_value=(course, 4) if course else (None, None)), \
             patch.object(recordings, "tmeet", return_value={"data": {"record_meetings": [record]}}), \
             patch.object(recordings, "fetch_minutes", return_value=""), \
             patch.object(recordings, "build_transcript", return_value=("实际逐字稿", 1)), \
             patch.object(recordings, "Tee", side_effect=lambda stream, log: (log.close(), stream)[1]), \
             patch("sys.argv", ["recordings", "--start", "2026-10-23"]), \
             patch("sys.stdout", new_callable=io.StringIO):
            recordings.main()

    def test_archive_writes_new_course_root_and_preserves_archival_context(self):
        self.run_archive("归档/统计")
        notes = self.root / "03_Sources/Courses/归档/统计/课堂笔记"
        self.assertTrue((notes / "raw/2026-10-23-统计录音-123456-逐字稿.md").exists())
        note = notes / "2026-10-23-第4节-统计录音.md"
        self.assertEqual(metadata(note)["subject"], ["统计"])
        self.assertEqual(metadata(note)["record_file_ids"], ["record-123456"])
        self.assertFalse((self.root / "课程").exists())

    def test_unmatched_recording_remains_raw_resource_in_inbox(self):
        self.run_archive(None)
        raw = self.root / "00_Inbox/课堂录音/raw/2026-10-23-统计录音-123456-逐字稿.md"
        self.assertTrue(raw.exists())
        self.assertNotIn("type: lecture", raw.read_text(encoding="utf-8"))
        self.assertIn("record-123456", raw.read_text(encoding="utf-8"))
        self.assertFalse((self.root / "未命名").exists())

    def test_course_name_reuses_existing_archived_course_directory(self):
        archived = self.root / "03_Sources/Courses/归档/旧课程/课堂笔记"
        archived.mkdir(parents=True)
        self.run_archive("旧课程")
        self.assertTrue((archived / "raw/2026-10-23-统计录音-123456-逐字稿.md").exists())
        self.assertFalse((self.root / "03_Sources/Courses/旧课程").exists())

    def test_partial_archive_does_not_delete_unmatched_material_that_was_not_written(self):
        raw = self.root / "00_Inbox/课堂录音/raw"
        raw.mkdir(parents=True)
        pending_minutes = raw / "2026-10-23-统计录音-123456-纪要.md"
        pending_minutes.write_text("仅有的历史纪要", encoding="utf-8")
        self.run_archive("统计")
        self.assertTrue(pending_minutes.exists())
        self.assertEqual(pending_minutes.read_text(encoding="utf-8"), "仅有的历史纪要")

    def test_importer_keeps_even_byte_identical_inbox_raw_copies(self):
        self.run_archive("统计")
        archived = self.notes / "raw/2026-10-23-统计录音-123456-逐字稿.md"
        inbox = self.root / "00_Inbox/课堂录音/raw"
        inbox.mkdir(parents=True)
        duplicate = inbox / archived.name
        original = archived.read_bytes()
        duplicate.write_bytes(original)
        self.run_archive("统计")
        self.assertTrue(duplicate.exists())
        self.assertEqual(duplicate.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
