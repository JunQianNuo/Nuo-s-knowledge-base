from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS_DIR))

from audit_vault import AuditResult, LinkIssue, render_report, scan_vault


class AuditVaultTests(unittest.TestCase):
    def test_scan_vault_reports_unresolved_empty_and_pending_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "existing.md").write_text("# Existing\n", encoding="utf-8")
            (root / "linked.md").write_text(
                "[[existing]]\n[[missing#section|Missing]]\n", encoding="utf-8"
            )
            (root / "empty.md").write_text(" \n\t", encoding="utf-8")
            pending_dir = root / "课程" / "未处理"
            pending_dir.mkdir(parents=True)
            (pending_dir / "source.pdf").write_bytes(b"pdf")

            result = scan_vault(root)

            self.assertEqual([issue.target for issue in result.unresolved_links], ["missing"])
            self.assertEqual(result.empty_markdown, ["empty.md"])
            self.assertEqual(result.pending_files, ["课程/未处理/source.pdf"])

    def test_render_report_limits_long_sections_to_keep_the_note_readable(self) -> None:
        result = AuditResult(
            unresolved_links=[LinkIssue(f"note-{index}.md", f"missing-{index}") for index in range(201)],
            empty_markdown=[],
            orphan_markdown=[],
            pending_files=[],
        )

        report = render_report(result, Path("D:/vault"))

        self.assertIn("仅显示前 200 项", report)
        self.assertIn("missing-199", report)
        self.assertNotIn("missing-200", report)

    def test_scan_vault_ignores_code_examples_and_generated_audit_reports(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "example.md").write_text(
                "```markdown\n[[missing-in-example]]\n```\n", encoding="utf-8"
            )
            report_dir = root / "总览" / "审查报告"
            report_dir.mkdir(parents=True)
            (report_dir / "generated.md").write_text("[[missing-in-report]]", encoding="utf-8")

            result = scan_vault(root)

            self.assertEqual(result.unresolved_links, [])


if __name__ == "__main__":
    unittest.main()
