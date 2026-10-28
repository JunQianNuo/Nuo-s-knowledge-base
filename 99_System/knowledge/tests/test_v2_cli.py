import contextlib
import importlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SYSTEM = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM))
import knowledge
from v2 import model

STAMP = "2026-10-28T10:00:00+08:00"


class V2CliTests(unittest.TestCase):
    def setUp(self):
        try:
            importlib.import_module("v2.cli")
        except ModuleNotFoundError:
            self.fail("V2 CLI missing")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.root = self.folder / "vault"
        self.root.mkdir()
        self.put("02_Maps/数学.md", {"schema_version": 2, "type": "moc", "time": STAMP, "topics": []})
        self.put("03_Sources/Ideas/来源.md", {"type": "idea", "status": "not done"})

    def put(self, name, data, body=b"\n# Real supplied content ^block\n"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(model.render_note(data, body))
        return path

    def run_cli(self, *argv, expected=0):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = knowledge.main(["v2", *map(str, argv)])
        self.assertEqual(code, expected, out.getvalue() + err.getvalue())
        return json.loads(out.getvalue() or err.getvalue())

    def files(self, data, body="# supplied definition\n"):
        metadata = self.folder / "metadata.json"
        text = self.folder / "body.md"
        metadata.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        text.write_text(body, encoding="utf-8")
        return metadata, text

    def atom(self):
        return {"schema_version": 2, "type": "concept", "time": STAMP, "topics": ["[[02_Maps/数学]]"], "source": ["[[03_Sources/Ideas/来源]]"]}

    def test_real_dispatcher_help_and_audit_are_usable_without_mutation(self):
        result = subprocess.run([sys.executable, "-B", str(SYSTEM / "knowledge.py"), "v2", "--help"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("prepare", result.stdout)
        self.assertIn("normalize-tags", result.stdout)
        result = self.run_cli("audit", "--vault-root", self.root)
        self.assertEqual(result["errors"], 0)
        self.run_cli("audit", "--vault-root", self.folder / "missing", expected=2)

    def test_new_defaults_to_dry_run_apply_refreshes_views_and_restore_is_guarded(self):
        metadata, body = self.files(self.atom())
        backup = self.folder / "new-backup"
        result = self.run_cli("new", "--vault-root", self.root, "--path", "01_Knowledge/定义.md", "--type", "concept", "--metadata", metadata, "--body", body, "--backup-dir", backup)
        self.assertFalse((self.root / "01_Knowledge/定义.md").exists())
        applied = self.run_cli("apply", "--plan", result["plan"], "--approve-plan-sha256", result["plan_sha256"])
        self.assertTrue((self.root / "01_Knowledge/定义.md").exists())
        self.assertTrue((self.root / "Home.md").exists())
        self.assertIn("views", applied)
        self.run_cli("restore", "--plan", result["plan"], "--approve-plan-sha256", result["plan_sha256"])
        self.assertFalse((self.root / "01_Knowledge/定义.md").exists())

    def test_new_rejects_invalid_topic_and_existing_time_rewrite(self):
        data = self.atom()
        data["topics"] = ["[[missing]]"]
        metadata, body = self.files(data)
        self.run_cli("new", "--vault-root", self.root, "--path", "01_Knowledge/定义.md", "--type", "concept", "--metadata", metadata, "--body", body, "--backup-dir", self.folder / "bad", expected=2)
        data = self.atom()
        self.put("01_Knowledge/定义.md", data)
        data["time"] = "2026-10-28T11:00:00+08:00"
        metadata, body = self.files(data, "\n# Real supplied content ^block\n\nAdditional evidence\n")
        self.run_cli("new", "--reuse", "--vault-root", self.root, "--path", "01_Knowledge/定义.md", "--type", "concept", "--metadata", metadata, "--body", body, "--backup-dir", self.folder / "bad-time", expected=2)

    def test_prepare_and_propose_connect_exact_json_packet_to_transaction_plan(self):
        output = self.folder / "packet.json"
        self.run_cli("prepare", "--vault-root", self.root, "--scope", "03_Sources/Ideas/来源.md", "--output", output)
        packet = json.loads(output.read_text(encoding="utf-8"))
        response = {"packet_sha256": packet["packet_sha256"], "source_hashes": {p: e["sha256"] for p, e in packet["sources"].items()},
                    "notes": [{"path": "01_Knowledge/定义.md", "metadata": self.atom(), "body": "# supplied\n"}],
                    "coverage": [{"source": "03_Sources/Ideas/来源.md", "complete": True, "atoms": ["01_Knowledge/定义.md"], "skip_candidates": []}]}
        answer = self.folder / "response.json"
        answer.write_text(json.dumps(response), encoding="utf-8")
        result = self.run_cli("propose", "--vault-root", self.root, "--packet", output, "--response", answer, "--backup-dir", self.folder / "proposal")
        self.assertGreater(result["planned"], 0)
        self.assertFalse((self.root / "01_Knowledge/定义.md").exists())

    def test_packet_output_cannot_bypass_transactions_inside_the_vault(self):
        self.run_cli("prepare", "--vault-root", self.root, "--scope", "03_Sources", "--output", self.root / "overwrite.json", expected=2)
        self.assertFalse((self.root / "overwrite.json").exists())

    def test_register_and_normalize_only_explicit_tags(self):
        registered = self.run_cli("tag-register", "--vault-root", self.root, "--canonical", "数学", "--alias", "math", "--backup-dir", self.folder / "register", "--apply")
        self.assertFalse(registered["dry_run"])
        path = self.put("03_Sources/Ideas/带标签.md", {"type": "idea", "status": "not done", "tags": ["math", "unknown"], "custom": "keep"})
        self.run_cli("normalize-tags", "--vault-root", self.root, "--path", "03_Sources/Ideas/带标签.md", "--backup-dir", self.folder / "normalize", "--apply")
        data, _ = model.read_note(path.read_bytes())
        self.assertEqual(data["tags"], ["数学", "unknown"])
        self.assertEqual(data["custom"], "keep")

    def test_migration_is_dry_run_by_default_and_preserves_unknown_tags(self):
        path = self.put("方法/旧条目.md", {"title": "旧条目", "tags": ["unknown"]})
        result = self.run_cli("migrate", "--vault-root", self.root, "--backup-dir", self.folder / "migration")
        self.assertTrue(result["dry_run"])
        self.assertTrue(path.exists())

    def test_view_failure_reports_primary_mutation_already_applied(self):
        self.put("02_Maps/坏主题.md", {"schema_version": 2, "type": "moc", "time": STAMP, "topics": ["[[missing]]"]})
        metadata, body = self.files(self.atom())
        result = self.run_cli("new", "--vault-root", self.root, "--path", "01_Knowledge/定义.md", "--type", "concept", "--metadata", metadata, "--body", body, "--backup-dir", self.folder / "with-bad-view", "--apply", expected=2)
        self.assertTrue(result["mutation_applied"])
        self.assertTrue((self.root / "01_Knowledge/定义.md").exists())
        self.assertIn("views_error", result)

    def test_skip_review_command_requires_separate_human_attestation(self):
        items = self.folder / "skip-items.json"
        items.write_text(json.dumps([{"section": "all", "reason": "Synthetic human review fixture"}]), encoding="utf-8")
        command = [sys.executable, "-B", str(SYSTEM / "knowledge.py"), "v2", "approve-skips", "--vault-root", str(self.root),
                   "--source", "03_Sources/Ideas/来源.md", "--items", str(items), "--reviewer-note", "Synthetic explicit human approval",
                   "--backup-dir", str(self.folder / "review")]
        rejected = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(rejected.returncode, 2)
        self.assertIn("human", rejected.stderr.lower())
        accepted = subprocess.run([*command, "--confirm-human-review"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(accepted.returncode, 0, accepted.stderr)
        planned = json.loads(accepted.stdout)
        record = json.loads(Path(planned["plan"]).read_text(encoding="utf-8"))
        self.assertIn("99_System/knowledge/v2/state/skip-reviews.json", {row["target"] for row in record["entries"]})
        self.assertFalse((self.root / "99_System/knowledge/v2/state/skip-reviews.json").exists())


if __name__ == "__main__":
    unittest.main()
