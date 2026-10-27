"""Integrated audit is read-only, explicitly scoped, and never a Formatter."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SYSTEM = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("knowledge_maintenance", SYSTEM / "maintenance.py")
m = importlib.util.module_from_spec(spec); sys.modules[spec.name] = m; spec.loader.exec_module(m)


class MaintenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("Notes/Source.md", '---\ntype: concept\ntags: [用户标签]\ntopics: ["[[Target]]"]\n---\n[[Target]] [[Missing]]\n')
        self.write("Target.md", "# Target\n")
        self.write("99_System/knowledge/templates/concept.md", '---\ntype: concept\n---\n')
        self.write("Project/.git", "marker")
        self.write("Project/private.md", '---\ntype: concept\n---\n')

    def write(self, name, text):
        p = self.root / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text, encoding="utf-8")

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in self.root.rglob('*') if p.is_file()}

    def test_integrated_readonly_report(self):
        before = self.snapshot()
        report = m.audit(self.root, [self.root / "Notes"])
        self.assertEqual(report["summary"]["knowledge_entities"], 1)
        self.assertEqual(report["summary"]["files"], 1)
        self.assertEqual(report["formatter"]["status"], "not_located")
        self.assertFalse(report["formatter"]["integrated"])
        self.assertEqual(report["writes"], 0)
        self.assertEqual(report["results"][0]["tags"]["explicit_tags"], ["用户标签"])
        self.assertEqual(report["results"][0]["tags"]["action"], "skip")
        self.assertEqual(report["summary"]["links"]["resolved"], 2)
        self.assertEqual(report["summary"]["links"]["unresolved"], 1)
        self.assertEqual(self.snapshot(), before)

    def test_system_and_independent_sources_excluded(self):
        report = m.audit(self.root, [self.root])
        self.assertEqual(report["summary"]["files"], 2)
        self.assertEqual(report["summary"]["knowledge_entities"], 1)
        excluded = report["scope"]["excluded_sources"]
        self.assertTrue(any("99_System" in x["path"] for x in excluded))
        self.assertTrue(any("Project" in x["path"] for x in excluded))

    def test_invalid_scope_is_configuration_error(self):
        with self.assertRaises(m.v.ConfigurationError):m.audit(self.root, [self.root.parent])
        with self.assertRaises(m.v.ConfigurationError):m.audit(self.root, [self.root / "missing"])
        with self.assertRaises(m.v.ConfigurationError):m.audit(self.root, [])

    def test_audit_does_not_call_apply_or_write(self):
        blocked = AssertionError("Unexpected write/network/apply")
        with patch.object(m.tags, "apply_changes", side_effect=blocked), patch.object(Path, "write_bytes", side_effect=blocked), patch.object(Path, "write_text", side_effect=blocked), patch("os.replace", side_effect=blocked), patch("socket.socket", side_effect=blocked):
            self.assertEqual(m.audit(self.root, [self.root / "Notes"])["writes"], 0)

    def test_cli_requires_scope_and_rejects_apply(self):
        command = [sys.executable, "-B", str(SYSTEM / "maintenance.py")]
        for extra in ([], ["audit", "--vault-root", str(self.root)], ["audit", "--vault-root", str(self.root), "--scope", str(self.root / "Notes"), "--apply"]):
            result = subprocess.run(command + extra, capture_output=True, encoding="utf-8")
            self.assertEqual(result.returncode, 2)
        before = self.snapshot()
        result = subprocess.run(command + ["audit", "--vault-root", str(self.root), "--scope", str(self.root / "Notes"), "--format", "json"], capture_output=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["summary"]["files"], 1)
        self.assertEqual(self.snapshot(), before)


if __name__ == "__main__":
    unittest.main()
