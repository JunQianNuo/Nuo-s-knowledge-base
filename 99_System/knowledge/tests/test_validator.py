"""Phase 1 contracts. Fixtures and CLI inputs are synthetic and stay outside the Vault."""
import copy
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SYSTEM = Path(__file__).resolve().parents[1]
VAULT = SYSTEM.parents[1]
SPEC = importlib.util.spec_from_file_location("knowledge_validator", SYSTEM / "validator.py")
v = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = v
SPEC.loader.exec_module(v)


def note(mapping, body="\n# 合成笔记\n正文 $x^2$。\n"):
    return ("---\n" + v.yaml.safe_dump(mapping, allow_unicode=True, sort_keys=False) + "---\n" + body).encode("utf-8")


def codes(result):
    return {d["code"] for d in result["diagnostics"]}


class ValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.system = v.load_system(SYSTEM)

    def check(self, mapping, profile="v1", path="合成/笔记.md"):
        return v.validate_note(note(mapping), path, self.system, profile)

    def test_contract_cases(self):
        cases = json.loads((SYSTEM / "tests/cases.json").read_text(encoding="utf-8"))
        for case in cases:
            with self.subTest(case=case["id"]):
                raw = case.get("raw")
                raw = raw.encode("utf-8") if raw is not None else note(case["metadata"])
                result = v.validate_note(raw, case.get("path", "合成/笔记.md"), self.system, case.get("profile", "auto"))
                self.assertEqual(result["classification"], case["classification"])
                for code in case.get("codes", []):
                    self.assertIn(code, codes(result))
                if "version_status" in case:
                    self.assertEqual(result["version_status"], case["version_status"])
                if "selected_profile" in case:
                    self.assertEqual(result["selected_profile"], case["selected_profile"])

    def test_shared_schema_constraints_apply_to_all_profiles(self):
        for kind in ("concept", "proposition", "method", "moc"):
            marker = {"role": "moc"} if kind == "moc" else {"type": kind}
            for field in ("topics", "prerequisites", "about", "uses", "related"):
                for bad in ("[[对象]]", ["裸文本"], [7], ["[[]]"], ["![[对象]]"], ["[[对象|名称]]"], ["[[对象#标题]]"], ["[[对象#^块]]"], ["[[ 对象]]"], ["[[对象 ]]"], ["[[对象]]", "[[对象]]"]):
                    with self.subTest(kind=kind, field=field, bad=bad):
                        self.assertEqual(self.check({**marker, field: bad})["classification"], "invalid")
                self.assertEqual(self.check({**marker, field: ["[[对象]]", "[[概念/L^p空间]]"]})["classification"], "valid")

    def test_minimal_and_filename_title(self):
        for kind in ("concept", "proposition", "method"):
            result = self.check({"type": kind}, path="合成/默认标题.md")
            self.assertEqual(result["classification"], "valid")
            self.assertEqual(result["display_title"], "默认标题")
            self.assertEqual(result["version_status"], "undeclared")
            self.assertIn("W_VERSION_UNDECLARED", codes(result))
        self.assertEqual(self.check({"type": "concept", "title": "展示标题"})["display_title"], "展示标题")
        self.assertEqual(self.check({"type": "concept", "title": " "})["classification"], "invalid")

    def test_link_must_occupy_the_entire_string(self):
        for value in ("[[对象]]\n", "[[对象]]\r\n", "[[对象\n名称]]", "prefix[[对象]]", "[[对象]]suffix", "[[^块]]"):
            with self.subTest(value=value):
                self.assertEqual(self.check({"type": "concept", "topics": [value]})["classification"], "invalid")

    def test_version_does_not_establish_creation_provenance(self):
        for profile in ("auto", "v1"):
            result = self.check({"type": "method"}, profile)
            self.assertEqual(result["version_status"], "undeclared")
            self.assertEqual(result["validation_basis"], "requested_profile" if profile == "v1" else "compatible_shape")
        for bad in (True, "1", 2, None):
            self.assertIn("E_VERSION", codes(self.check({"type": "concept", "schema_version": bad})))

    def test_legacy_knowledge_point_is_not_mapped(self):
        result = self.check({"type": "知识点", "topics": ["控制收敛定理"]}, "auto")
        self.assertEqual(result["classification"], "legacy")
        self.assertIsNone(result["selected_profile"])
        self.assertTrue(result["semantic_review_required"])
        self.assertIn("I_SEMANTIC_REVIEW", codes(result))
        self.assertFalse(result["is_knowledge_entity"])

    def test_extensions_and_source_are_preserved(self):
        mapping = {"type": "concept", "exam": "历史字段", "my_extension": {"items": [1, 2]}, "source": ["[[课件#段落]]", "https://example.org", "教材，第3页"], "created": "2026-10-27"}
        raw = note(mapping)
        result = v.validate_note(raw, "合成/笔记.md", self.system, "v1")
        self.assertEqual(result["classification"], "valid")
        unknown = [d["field"] for d in result["diagnostics"] if d["code"] == "W_UNKNOWN_FIELD"]
        self.assertIn("my_extension", unknown)
        self.assertNotIn("exam", unknown)
        self.assertEqual(v.parse_frontmatter(raw)["my_extension"], mapping["my_extension"])
        self.assertEqual(v.parse_frontmatter(raw)["created"], "2026-10-27")

    def test_yaml_encoding_and_structure(self):
        raw = note({"type": "concept", "schema_version": 1})
        for sample in (raw, b"\xef\xbb\xbf" + raw, raw.replace(b"\n", b"\r\n")):
            self.assertEqual(v.validate_note(sample, "合成/笔记.md", self.system)["classification"], "valid")
        for raw, code in [(b"\xff", "E_ENCODING"), (b"---\n[]\n---\n", "E_YAML"), (b"---\ntype: [\n---\n", "E_YAML"), (b"---\ntype: concept\ntype: method\n---\n", "E_DUPLICATE_KEY"), (b"---\ntype: concept\n", "E_FRONTMATTER"), (b"---\nx: &x [*x]\n---\n", "E_YAML")]:
            with self.subTest(raw=raw):
                self.assertIn(code, codes(v.validate_note(raw, "合成/笔记.md", self.system, "v1")))

    def test_invalid_explicit_yaml_scalars_are_input_errors(self):
        for scalar in ("!!int nope", "!!float nope", "!!bool nope", "!!timestamp nope"):
            with self.subTest(scalar=scalar):
                raw = ("---\ntype: concept\nx: " + scalar + "\n---\n").encode()
                result = v.validate_note(raw, "合成/非法标量.md", self.system, "v1")
                self.assertEqual(result["classification"], "invalid")
                self.assertIn("E_YAML", codes(result))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "invalid.md"
            path.write_bytes(b"---\ntype: concept\nx: !!int nope\n---\n")
            result = subprocess.run([sys.executable, "-B", str(SYSTEM / "validator.py"), "check", "--file", str(path), "--vault-root", tmp, "--profile", "v1"], capture_output=True, encoding="utf-8")
            self.assertEqual(result.returncode, 1)
            self.assertIn("E_YAML", result.stdout)

    def test_large_integer_diagnostic_is_an_input_error(self):
        raw = ("---\ntype: concept\ntitle: 0x" + "f" * 4000 + "\n---\n").encode()
        limit = sys.get_int_max_str_digits()
        result = v.validate_note(raw, "合成/大整数.md", self.system, "v1")
        self.assertEqual(result["classification"], "invalid")
        self.assertIn("E_SCHEMA", codes(result))
        self.assertEqual(sys.get_int_max_str_digits(), limit)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "large.md"; path.write_bytes(raw)
            cli = subprocess.run([sys.executable, "-B", str(SYSTEM / "validator.py"), "check", "--file", str(path), "--vault-root", tmp], capture_output=True, encoding="utf-8")
            self.assertEqual(cli.returncode, 1)
            self.assertIn("E_SCHEMA", cli.stdout)

    def test_schema_reference_and_policy_invariants(self):
        for mutation in ("non_schema_target", "unconditional_cycle", "anyof_cycle", "oneof_cycle", "not_cycle", "if_cycle", "dependent_cycle", "nested_id", "common_removed", "review_disabled", "review_missing"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp) / "knowledge"; shutil.copytree(SYSTEM, target)
                sp = target / "schemas/concept.schema.json"
                schema = json.loads(sp.read_text(encoding="utf-8"))
                if mutation == "non_schema_target":
                    schema["allOf"].append({"$ref": "urn:knowledge:v1:common#/type"})
                elif mutation == "unconditional_cycle":
                    schema["allOf"].append({"$ref": "urn:knowledge:v1:concept"})
                elif mutation in ("anyof_cycle", "oneof_cycle"):
                    schema["anyOf" if mutation == "anyof_cycle" else "oneOf"] = [{"$ref": "urn:knowledge:v1:concept"}]
                elif mutation in ("not_cycle", "if_cycle"):
                    schema["not" if mutation == "not_cycle" else "if"] = {"$ref": "urn:knowledge:v1:concept"}
                elif mutation == "dependent_cycle":
                    schema["dependentSchemas"] = {"extra": {"$ref": "urn:knowledge:v1:concept"}}
                elif mutation == "nested_id":
                    schema["$defs"] = {"T": {"type": "string"}}
                    schema["properties"]["extra"] = {"$id": "urn:nested", "$ref": "#/$defs/T"}
                elif mutation == "common_removed":
                    del schema["allOf"]
                else:
                    rp = target / "registry.yaml"; registry = v.yaml.safe_load(rp.read_text(encoding="utf-8"))
                    if mutation == "review_disabled":registry["legacy_types"]["知识点"]["semantic_review_required"] = False
                    else:del registry["legacy_types"]["知识点"]
                    rp.write_text(v.yaml.safe_dump(registry, allow_unicode=True), encoding="utf-8")
                sp.write_text(json.dumps(schema), encoding="utf-8")
                with patch("socket.socket", side_effect=AssertionError("network")) as network:
                    with self.assertRaises(v.ConfigurationError):v.load_system(target)
                    network.assert_not_called()

    def test_system_files_are_excluded_even_when_metadata_is_valid(self):
        paths = ["99_System/knowledge/templates/concept.md", "99_System/knowledge/tests/example.md", "docs/KNOWLEDGE_ARCHITECTURE.md", "scripts/example.md", "模板/example.md", "总览/属性库/条目/属性-type.md", ".obsidian/example.md", "AGENTS.md"]
        for path in paths:
            with self.subTest(path=path):
                self.assertTrue(v.is_system_path(path, self.system))
                result = self.check({"type": "concept", "schema_version": 1}, path=path)
                self.assertTrue(result["is_system_file"])
                self.assertFalse(result["is_knowledge_entity"])
        self.assertFalse(v.is_system_path("99_Systematic/笔记.md", self.system))
        report = v.check_system(self.system)
        self.assertTrue(report["ok"])
        self.assertEqual(report["summary"]["knowledge_entities"], 0)
        self.assertEqual(report["summary"]["system_files"], 4)

    def test_all_templates_and_local_schema_reuse(self):
        self.assertEqual(len(self.system.schemas), 6)
        for kind, entry in self.system.registry["profiles"].items():
            schema = self.system.schemas[entry["schema"]]
            self.assertIn({"$ref": "urn:knowledge:v1:common"}, schema["allOf"])
            raw = (SYSTEM / entry["template"]).read_bytes()
            for rendered in (raw, raw.replace(b"{{title}}", "合成标题".encode())):
                result = v.validate_note(rendered, "99_System/knowledge/templates/" + kind + ".md", self.system, "v1")
                self.assertEqual(result["classification"], "valid", result)
                self.assertEqual(result["version_status"], "explicit")
                self.assertFalse(result["is_knowledge_entity"])

    def test_no_network_and_no_writes(self):
        blocked = AssertionError("Validator attempted a write or network access")
        original_open = io.open

        def read_only_open(file, mode="r", *args, **kwargs):
            if any(flag in mode for flag in "wax+"):
                raise blocked
            return original_open(file, mode, *args, **kwargs)

        with patch("builtins.open", side_effect=read_only_open), patch("io.open", side_effect=read_only_open), patch.object(Path, "write_text", side_effect=blocked), patch.object(Path, "write_bytes", side_effect=blocked), patch.object(Path, "mkdir", side_effect=blocked), patch.object(Path, "unlink", side_effect=blocked), patch("os.replace", side_effect=blocked), patch("socket.socket", side_effect=blocked):
            system = v.load_system(SYSTEM)
            self.assertTrue(v.check_system(system)["ok"])
            self.assertEqual(self.check({"type": "concept"})["classification"], "valid")

    def test_bad_registry_and_remote_refs_are_rejected(self):
        for mutation in ("remote", "bootstrap_remote", "missing", "duplicate", "wrong_schema", "invalid_template", "escape", "isolation_removed"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp) / "knowledge"
                shutil.copytree(SYSTEM, target)
                path = target / "registry.yaml"
                reg = v.yaml.safe_load(path.read_text(encoding="utf-8"))
                if mutation == "remote":
                    schema_path = target / reg["profiles"]["concept"]["schema"]
                    schema = json.loads(schema_path.read_text(encoding="utf-8"))
                    schema["allOf"].append({"$ref": "https://example.org/remote.json"})
                    schema_path.write_text(json.dumps(schema), encoding="utf-8")
                elif mutation == "bootstrap_remote":
                    schema_path = target / "schemas/registry.schema.json"
                    schema = json.loads(schema_path.read_text(encoding="utf-8"))
                    schema["allOf"] = [{"$ref": "https://example.org/remote.json"}]
                    schema_path.write_text(json.dumps(schema), encoding="utf-8")
                elif mutation == "missing":
                    reg["profiles"]["concept"]["template"] = "templates/missing.md"
                elif mutation == "duplicate":
                    reg["profiles"]["method"]["schema"] = reg["profiles"]["concept"]["schema"]
                elif mutation == "wrong_schema":
                    schema_path = target / reg["profiles"]["concept"]["schema"]
                    schema = json.loads(schema_path.read_text(encoding="utf-8")); schema["type"] = 123
                    schema_path.write_text(json.dumps(schema), encoding="utf-8")
                elif mutation == "invalid_template":
                    (target / reg["profiles"]["method"]["template"]).write_bytes(note({"type": "concept"}))
                elif mutation == "isolation_removed":
                    reg["system_exclusions"]["prefixes"].remove("99_System")
                else:
                    reg["profiles"]["concept"]["template"] = "../escape.md"
                path.write_text(v.yaml.safe_dump(reg, allow_unicode=True, sort_keys=False), encoding="utf-8")
                with patch("socket.socket", side_effect=AssertionError("network")) as network:
                    if mutation == "invalid_template":
                        self.assertFalse(v.check_system(v.load_system(target))["ok"])
                    else:
                        with self.assertRaises(v.ConfigurationError):
                            v.load_system(target)
                    network.assert_not_called()

    def test_cli_reports_and_leaves_input_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "样例.md"
            before = note({"type": "method", "topics": ["[[不存在的主题]]"]})
            path.write_bytes(before)
            command = [sys.executable, "-B", str(SYSTEM / "validator.py")]
            good = subprocess.run(command + ["check", "--file", str(path), "--vault-root", str(root), "--profile", "v1", "--format", "json"], capture_output=True, encoding="utf-8")
            self.assertEqual(good.returncode, 0, good.stderr)
            result = json.loads(good.stdout)
            self.assertEqual(result["summary"]["knowledge_entities"], 1)
            self.assertEqual(path.read_bytes(), before)
            path.write_bytes(note({"type": "invalid"}))
            bad = subprocess.run(command + ["check", "--file", str(path), "--vault-root", str(root), "--profile", "v1"], capture_output=True, encoding="utf-8")
            self.assertEqual(bad.returncode, 1)
            no_args = subprocess.run(command, capture_output=True, encoding="utf-8")
            self.assertEqual(no_args.returncode, 2)
            missing = subprocess.run(command + ["check", "--file", str(root / "missing.md")], capture_output=True, encoding="utf-8")
            self.assertEqual(missing.returncode, 2)
            system = subprocess.run(command + ["check-system", "--format", "json"], capture_output=True, encoding="utf-8")
            self.assertEqual(system.returncode, 0, system.stderr)
            self.assertTrue(json.loads(system.stdout)["ok"])


class ExistingTagIsolationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("phase1_legacy_tag_tool", VAULT / "scripts/tag_maintenance.py")
        cls.tm = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = cls.tm
        spec.loader.exec_module(cls.tm)

    def test_legacy_descriptive_topics_do_not_generate_tags(self):
        reg = self.tm.Registry([self.tm.Entry("控制收敛定理", ("DCT",))])
        raw = note({"type": "知识点", "topics": ["控制收敛定理"]})
        after = self.tm.plan_note(raw, "知识点/合成笔记.md", reg)
        self.assertEqual(after, raw)
        self.assertEqual(self.tm.metadata(raw)["topics"], ["控制收敛定理"])

    def test_wikilinks_are_not_unwrapped_or_promoted(self):
        reg = self.tm.Registry([self.tm.Entry("控制收敛定理", ("DCT",))])
        for target in ("[[控制收敛定理]]", "[[DCT]]", "[[主题/收敛|控制收敛定理]]", "[[控制收敛定理#标题]]"):
            raw = note({"type": "concept", "topics": [target]})
            self.assertEqual(self.tm.plan_note(raw, "概念/合成笔记.md", reg), raw)

    def test_legacy_context_risk_is_documented_and_warned(self):
        reg = self.tm.Registry([self.tm.Entry("控制收敛定理", ("DCT",), ambiguous_aliases=("DCT",), alias_context=("Lebesgue",))])
        plain = note({"type": "concept", "tags": ["DCT"], "topics": ["[[主题/其他]]"]})
        linked = note({"type": "concept", "tags": ["DCT"], "topics": ["[[主题/Lebesgue积分]]"]})
        self.assertEqual(self.tm.metadata(self.tm.plan_note(plain, "概念/合成笔记.md", reg))["tags"], ["DCT"])
        self.assertEqual(self.tm.plan_note(linked, "概念/合成笔记.md", reg), linked)
        result = v.validate_note(linked, "概念/合成笔记.md", v.load_system(SYSTEM))
        self.assertIn("W_LEGACY_TAG_CONTEXT", codes(result))

    def test_new_system_is_outside_legacy_scan_scopes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "99_System/knowledge/templates"
            target.mkdir(parents=True)
            (target / "concept.md").write_bytes(note({"type": "concept", "topics": ["[[DCT]]"]}))
            self.assertEqual(list(self.tm.iter_notes(root)), [])


if __name__ == "__main__":
    unittest.main()
