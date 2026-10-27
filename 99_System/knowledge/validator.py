"""Read-only Phase 1 validation. No scanning, formatting, migration or network retrieval."""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

import argparse
import copy
from dataclasses import dataclass
import json
import math
from pathlib import Path, PurePosixPath
import posixpath
import re

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource


DIALECT = "https://json-schema.org/draft/2020-12/schema"
ATOMIC_TYPES = ("concept", "proposition", "method")


class ConfigurationError(ValueError):
    """The local registry/schema/template configuration cannot be used."""


class DuplicateKeyError(yaml.YAMLError):
    pass


class FrontmatterError(ValueError):
    pass


class SafeMetadataLoader(yaml.SafeLoader):
    """Keep dates as strings and reject duplicate keys rather than discarding values."""


SafeMetadataLoader.yaml_implicit_resolvers = copy.deepcopy(yaml.SafeLoader.yaml_implicit_resolvers)
for _key, _resolvers in SafeMetadataLoader.yaml_implicit_resolvers.items():
    SafeMetadataLoader.yaml_implicit_resolvers[_key] = [item for item in _resolvers if item[0] != "tag:yaml.org,2002:timestamp"]


def _mapping(loader, node):
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if not isinstance(key, str):
            raise yaml.YAMLError("Property names must be strings")
        if key in result:
            raise DuplicateKeyError(f"Duplicate property: {key}")
        result[key] = loader.construct_object(value_node, deep=True)
    return result


SafeMetadataLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def _json_compatible(value, active=None):
    active = set() if active is None else active
    if isinstance(value, (dict, list)):
        if id(value) in active:
            raise yaml.YAMLError("Recursive YAML aliases are not supported")
        active.add(id(value))
        for item in (value.values() if isinstance(value, dict) else value):
            _json_compatible(item, active)
        active.remove(id(value))
    elif value is not None and not isinstance(value, (str, bool, int, float)):
        raise yaml.YAMLError("Metadata must use JSON-compatible values")
    elif isinstance(value, float) and not math.isfinite(value):
        raise yaml.YAMLError("Non-finite numbers are not supported")


def _yaml_mapping(text):
    try:
        value = yaml.load(text, Loader=SafeMetadataLoader)
    except (ValueError, TypeError, KeyError, AttributeError, OverflowError) as error:
        # SafeLoader scalar constructors may raise built-ins for malformed tags.
        # These are input YAML errors, not configuration failures or API crashes.
        raise yaml.YAMLError(f"Invalid YAML scalar: {error}") from error
    value = {} if value is None else value
    if not isinstance(value, dict):
        raise yaml.YAMLError("Frontmatter must be a mapping")
    _json_compatible(value)
    return value


def parse_frontmatter(raw: bytes) -> dict | None:
    text = raw.decode("utf-8-sig")
    lines = text.splitlines(keepends=True)
    if not lines or not re.fullmatch(r"---[ \t]*(?:\r?\n)?", lines[0]):
        return None
    for index, line in enumerate(lines[1:], 1):
        if re.fullmatch(r"---[ \t]*(?:\r?\n)?", line):
            return _yaml_mapping("".join(lines[1:index]))
    raise FrontmatterError("Opening frontmatter has no closing --- delimiter")


def _local_file(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ConfigurationError(f"Missing or outside local root: {relative}")
    return path


def _refs(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in ("$ref", "$dynamicRef"):
                yield item
            else:
                yield from _refs(item)
    elif isinstance(value, list):
        for item in value:
            yield from _refs(item)


def _schema_nodes(value):
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from _schema_nodes(item)
    elif isinstance(value, list):
        for item in value:
            yield from _schema_nodes(item)


def _check_local_references(schemas, references, identifiers):
    def target(ref, base):
        if not isinstance(ref, str) or (not ref.startswith("#") and ref.split("#", 1)[0] not in identifiers):
            raise ConfigurationError(f"Schema reference is not in the local registry: {ref}")
        resolved = references.resolver(base).lookup(ref).contents
        Draft202012Validator.check_schema(resolved)
        return resolved, (ref.split("#", 1)[0] or base)

    def unconditional(node, base, active):
        if not isinstance(node, dict):
            return
        key = (base, id(node))
        if key in active:
            raise ConfigurationError("Unconditional local Schema reference cycle")
        active.add(key)
        if "$ref" in node:
            child, resource = target(node["$ref"], base)
            unconditional(child, resource, active)
        # These applicators evaluate the same instance, without consuming a
        # property/item level. Their reference cycles can never terminate.
        for keyword in ("allOf", "anyOf", "oneOf"):
            for child in node.get(keyword, []):
                unconditional(child, base, active)
        for keyword in ("not", "if", "then", "else"):
            if keyword in node:
                unconditional(node[keyword], base, active)
        for child in node.get("dependentSchemas", {}).values():
            unconditional(child, base, active)
        active.remove(key)

    for schema in schemas.values():
        for node in _schema_nodes(schema):
            if node is not schema and "$id" in node:
                raise ConfigurationError("Nested Schema resource $id is not supported by this v1 family")
            if "$dynamicRef" in node:
                raise ConfigurationError("Dynamic references are not supported by this v1 family")
        for ref in _refs(schema):
            target(ref, schema["$id"])
        for node in _schema_nodes(schema):
            unconditional(node, schema["$id"], set())


@dataclass
class System:
    root: Path
    vault_root: Path
    registry: dict
    schemas: dict
    references: Registry
    validators: dict
    known_fields: set
    catalog_available: bool


def load_system(root: Path | None = None) -> System:
    root = (root or Path(__file__).resolve().parent).resolve()
    try:
        bootstrap = json.loads(_local_file(root, "schemas/registry.schema.json").read_text(encoding="utf-8-sig"))
        Draft202012Validator.check_schema(bootstrap)
        if bootstrap.get("$schema") != DIALECT or bootstrap.get("$id") != "urn:knowledge:registry:1":
            raise ConfigurationError("Registry schema dialect or identity is invalid")
        for ref in _refs(bootstrap):
            if not isinstance(ref, str) or not ref.startswith("#"):
                raise ConfigurationError(f"Bootstrap schema reference is not local: {ref}")
        registry = _yaml_mapping(_local_file(root, "registry.yaml").read_text(encoding="utf-8-sig"))
        bootstrap_references = Registry().with_resource(bootstrap["$id"], Resource.from_contents(bootstrap))
        Draft202012Validator(bootstrap, registry=bootstrap_references).validate(registry)
        schemas = {}
        identifiers = {}
        for name in registry["schema_files"]:
            schema = json.loads(_local_file(root, name).read_text(encoding="utf-8-sig"))
            if schema.get("$schema") != DIALECT or not isinstance(schema.get("$id"), str):
                raise ConfigurationError(f"Missing Draft 2020-12 dialect or $id: {name}")
            Draft202012Validator.check_schema(schema)
            if schema["$id"] in identifiers:
                raise ConfigurationError(f"Duplicate schema $id: {schema['$id']}")
            schemas[name] = schema
            identifiers[schema["$id"]] = schema
        references = Registry().with_resources((key, Resource.from_contents(value)) for key, value in identifiers.items())
        _check_local_references(schemas, references, identifiers)
        if "urn:knowledge:v1:common" not in identifiers:
            raise ConfigurationError("Shared common schema is missing")
        seen_schemas = set()
        seen_templates = set()
        validators = {}
        for kind, entry in registry["profiles"].items():
            expected = {"role": "moc"} if kind == "moc" else {"type": kind}
            if entry["selector"] != expected:
                raise ConfigurationError(f"Profile selector mismatch: {kind}")
            if entry["schema"] in seen_schemas or entry["template"] in seen_templates:
                raise ConfigurationError("Profile schema/template mappings must be unique")
            seen_schemas.add(entry["schema"]); seen_templates.add(entry["template"])
            schema = schemas[entry["schema"]]
            if schema["$id"] != f"urn:knowledge:v1:{kind}":
                raise ConfigurationError(f"Profile schema mismatch: {kind}")
            if {"$ref": "urn:knowledge:v1:common"} not in schema.get("allOf", []):
                raise ConfigurationError(f"Profile must reuse the common Schema: {kind}")
            _local_file(root, entry["template"])
            validators[kind] = Draft202012Validator(schema, registry=references)
        vault_root = root.parents[1]
        catalog = (vault_root / registry["field_catalog"]).resolve()
        if not catalog.is_relative_to(vault_root):
            raise ConfigurationError("Field catalog is outside the Vault")
        fields = set(identifiers["urn:knowledge:v1:common"]["properties"])
        if catalog.is_dir():
            fields.update(path.stem[len("属性-"):] for path in catalog.glob("属性-*.md"))
        return System(root, vault_root, registry, schemas, references, validators, fields, catalog.is_dir())
    except ConfigurationError:
        raise
    except Exception as error:
        raise ConfigurationError(str(error)) from error


def _in_scope(path: str, prefix: str) -> bool:
    path, prefix = path.casefold(), prefix.strip("/").casefold()
    return path == prefix or path.startswith(prefix + "/")


def is_system_path(path: str, system: System) -> bool:
    path = posixpath.normpath(path.replace("\\", "/"))
    parts = PurePosixPath(path).parts
    exclusions = system.registry["system_exclusions"]
    return (
        path.startswith("../") or path.startswith("/")
        or (exclusions["exclude_hidden"] and any(part.startswith(".") for part in parts))
        or any(_in_scope(path, prefix) for prefix in exclusions["prefixes"])
        or PurePosixPath(path).name.casefold() in {name.casefold() for name in exclusions["filenames"]}
    )


def _diagnostic(result, code, severity, message, field=""):
    result["diagnostics"].append({"code": code, "severity": severity, "field": field, "message": message})


def validate_note(raw: bytes, path: str, system: System, profile: str = "auto") -> dict:
    if profile not in ("auto", "v1"):
        raise ConfigurationError(f"Unknown validation profile: {profile}")
    path = path.replace("\\", "/")
    result = {
        "path": path, "classification": "unclassified", "selected_profile": None,
        "version_status": "undeclared", "validation_basis": None,
        "display_title": PurePosixPath(path).stem, "semantic_review_required": False,
        "is_system_file": is_system_path(path, system), "is_knowledge_entity": False,
        "diagnostics": [],
    }
    try:
        metadata = parse_frontmatter(raw)
    except (UnicodeError, DuplicateKeyError, FrontmatterError, yaml.YAMLError, RecursionError) as error:
        code = "E_ENCODING" if isinstance(error, UnicodeError) else "E_DUPLICATE_KEY" if isinstance(error, DuplicateKeyError) else "E_FRONTMATTER" if isinstance(error, FrontmatterError) else "E_YAML"
        _diagnostic(result, code, "error", str(error))
        result["classification"] = "invalid"
        return result
    if metadata is None:
        _diagnostic(result, "E_FRONTMATTER" if profile == "v1" else "W_UNCLASSIFIED", "error" if profile == "v1" else "warning", "No YAML frontmatter; no v1 creation history is assumed")
        result["classification"] = "invalid" if profile == "v1" else "unclassified"
        return result
    if isinstance(metadata.get("title"), str) and metadata["title"].strip():
        result["display_title"] = metadata["title"]
    declared = "schema_version" in metadata
    if declared:
        if type(metadata["schema_version"]) is not int or metadata["schema_version"] != system.registry["note_schema_version"]:
            result["version_status"] = "unsupported"
            result["classification"] = "invalid"
            _diagnostic(result, "E_VERSION", "error", "Unsupported schema_version; no fallback was performed", "schema_version")
            return result
        result["version_status"] = "explicit"
    kind = metadata.get("type")
    atomic = isinstance(kind, str) and kind in ATOMIC_TYPES
    if metadata.get("role") == "moc" and kind not in (None, "MOC"):
        result["classification"] = "invalid"
        _diagnostic(result, "E_ROLE_TYPE_CONFLICT", "error", "MOC role conflicts with the supplied type", "type")
        return result
    strict = profile == "v1" or declared or atomic or metadata.get("role") == "moc"
    if not strict:
        legacy = system.registry["legacy_types"].get(kind) if isinstance(kind, str) else None
        result["validation_basis"] = "legacy_classification"
        if legacy is not None:
            result["classification"] = "legacy"
            result["semantic_review_required"] = legacy["semantic_review_required"]
            _diagnostic(result, "I_LEGACY_TYPE", "info", "Historical type recognized; no canonical type assigned", "type")
            if result["semantic_review_required"]:
                _diagnostic(result, "I_SEMANTIC_REVIEW", "info", "知识点 requires content review; it is not mapped to proposition", "type")
        elif isinstance(kind, str) and kind in system.registry["out_of_scope_types"]:
            result["classification"] = "out_of_scope"
        else:
            _diagnostic(result, "W_UNCLASSIFIED", "warning", "Not classified; not counted as validated v1 content", "type")
    else:
        selected = "moc" if metadata.get("role") == "moc" else kind if atomic else None
        result["selected_profile"] = selected
        result["validation_basis"] = "explicit_schema_version" if declared else "requested_profile" if profile == "v1" else "compatible_shape"
        if not declared:
            _diagnostic(result, "W_VERSION_UNDECLARED", "warning", "Compatible validation only; schema version and creation provenance are not explicitly declared", "schema_version")
        if selected is None:
            _diagnostic(result, "E_TYPE", "error", "Expected atomic type concept/proposition/method, or role: moc", "type")
        else:
            try:
                errors = sorted(system.validators[selected].iter_errors(metadata), key=lambda item: tuple(str(x) for x in item.absolute_path))
                for error in errors:
                    _diagnostic(result, "E_SCHEMA", "error", error.message, "/".join(str(x) for x in error.absolute_path))
            except ValueError:
                _diagnostic(result, "E_SCHEMA", "error", "Input violates Schema; its value cannot be safely represented in a diagnostic")
            if selected == "moc" and kind == "MOC":
                _diagnostic(result, "W_LEGACY_MOC_TYPE", "warning", "type: MOC is temporarily accepted; new templates use role only", "type")
        result["classification"] = "invalid" if any(d["severity"] == "error" for d in result["diagnostics"]) else "valid"
    for name in metadata:
        if name not in system.known_fields:
            _diagnostic(result, "W_UNKNOWN_FIELD", "warning", "Field is not registered; input is preserved", name)
    topics = metadata.get("topics")
    if isinstance(topics, list) and any(isinstance(x, str) and "[[" in x for x in topics) and any(_in_scope(path, scope) for scope in system.registry["legacy_tag_scopes"]):
        _diagnostic(result, "W_LEGACY_TAG_CONTEXT", "warning", "Linked or mixed topics require tag-tool isolation; the Phase 2A tag tool skips this input and never infers tags", "topics")
    result["is_knowledge_entity"] = result["classification"] == "valid" and result["selected_profile"] in ATOMIC_TYPES and not result["is_system_file"]
    return result


def summarize(results: list[dict]) -> dict:
    return {
        "documents": len(results),
        "validation_counts": {name: sum(r["classification"] == name for r in results) for name in ("valid", "invalid", "legacy", "unclassified", "out_of_scope")},
        "knowledge_entities": sum(r["is_knowledge_entity"] for r in results),
        "system_files": sum(r["is_system_file"] for r in results),
        "errors": sum(d["severity"] == "error" for r in results for d in r["diagnostics"]),
        "warnings": sum(d["severity"] == "warning" for r in results for d in r["diagnostics"]),
    }


def check_system(system: System) -> dict:
    results = []
    for kind, entry in system.registry["profiles"].items():
        raw = _local_file(system.root, entry["template"]).read_bytes()
        result = validate_note(raw, "99_System/knowledge/" + entry["template"], system, "v1")
        try:
            metadata = parse_frontmatter(raw) or {}
            if any(metadata.get(key) != value for key, value in entry["selector"].items()):
                _diagnostic(result, "E_TEMPLATE_PROFILE", "error", f"Template must match registered profile {kind}")
            if type(metadata.get("schema_version")) is not int or metadata.get("schema_version") != 1:
                _diagnostic(result, "E_TEMPLATE_VERSION", "error", "New templates must explicitly declare schema_version: 1")
        except (UnicodeError, ValueError, yaml.YAMLError, RecursionError):
            pass  # validate_note already reports the parse failure.
        if any(d["severity"] == "error" for d in result["diagnostics"]):
            result["classification"] = "invalid"
        results.append(result)
    summary = summarize(results)
    return {"ok": summary["errors"] == 0, "schema_count": len(system.schemas), "schema_dialect": DIALECT, "field_catalog_available": system.catalog_available, "summary": summary, "results": results}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    system_command = commands.add_parser("check-system", help="Check local registry, schemas and templates")
    system_command.add_argument("--format", choices=("json", "text"), default="json")
    check = commands.add_parser("check", help="Read explicitly named files; never recursively scan")
    check.add_argument("--file", action="append", type=Path, required=True)
    check.add_argument("--vault-root", type=Path)
    check.add_argument("--profile", choices=("auto", "v1"), default="auto")
    check.add_argument("--format", choices=("json", "text"), default="json")
    args = parser.parse_args(argv)
    try:
        system = load_system()
        if args.command == "check-system":
            report = check_system(system)
        else:
            root = (args.vault_root or system.vault_root).resolve()
            results = []
            for path in args.file:
                path = path.resolve()
                relative = path.relative_to(root).as_posix()
                results.append(validate_note(path.read_bytes(), relative, system, args.profile))
            summary = summarize(results)
            report = {"ok": summary["errors"] == 0, "summary": summary, "results": results}
        if args.format == "json":
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(report["summary"], ensure_ascii=False))
            for result in report["results"]:
                print(f"{result['path']}: {result['classification']} ({result['version_status']})")
                for item in result["diagnostics"]:
                    print(f"  {item['severity']} {item['code']} {item['field']}: {item['message']}")
        return 0 if report["ok"] else 1
    except (ConfigurationError, OSError, ValueError) as error:
        print(json.dumps({"ok": False, "configuration_error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
