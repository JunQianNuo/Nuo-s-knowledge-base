"""Explicitly scoped read-only audit; composes existing validators, never applies changes."""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path


SYSTEM = Path(__file__).resolve().parent


def _module(name, path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec); sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


links = _module("knowledge_links", SYSTEM / "link_validator.py")
v = links.v
tags = _module("knowledge_legacy_tags", SYSTEM.parents[1] / "scripts/tag_maintenance.py")


def _tag_report(raw, registry):
    try:
        metadata = v.parse_frontmatter(raw) or {}
    except (UnicodeError, ValueError, v.yaml.YAMLError, RecursionError):
        return {"action": "unchecked", "reason": "invalid_metadata", "explicit_tags": [], "suggestions": []}
    reason = tags.legacy_skip_reason(metadata)
    stored = metadata.get("tags", [])
    stored = stored if isinstance(stored, list) else [stored]
    explicit = [value for value in stored if isinstance(value, str)]
    report = {"action": "skip" if reason else "audit_explicit", "reason": reason,
              "explicit_tags": explicit, "suggestions": [], "registry_available": registry is not None,
              "invalid_values": len(stored) - len(explicit) + sum(not tags.valid_tag(x) for x in explicit)}
    if not reason and registry:
        for value in explicit:
            target = registry.resolve(value, "", existing=True)
            if target and target != value:
                report["suggestions"].append({"from": value, "to": target, "basis": "unambiguous_explicit_tag_only"})
    return report


def audit(root, scopes, system=None):
    root = Path(root).resolve()
    if not root.is_dir() or not scopes:
        raise v.ConfigurationError("An existing Vault root and at least one explicit scope are required")
    system = system or v.load_system(SYSTEM)
    requested = []
    for scope in scopes:
        scope = Path(scope)
        scope = scope.absolute() if scope.is_absolute() else (root / scope).absolute()
        if not scope.resolve().is_relative_to(root) or not scope.exists():
            raise v.ConfigurationError(f"Scope is missing or outside the Vault: {scope}")
        requested.append(scope.relative_to(root).as_posix())
    index = links.build_index(root, system)
    def selected(path):
        return any(scope == "." or v._in_scope(path, scope) for scope in requested)
    excluded = [item for item in index.excluded if selected(item["path"])]
    registry_path = root / "总览/标签库/条目"
    registry = tags.Registry.load(registry_path) if registry_path.is_dir() else None
    results = []; errors = []
    for path in sorted(index.files):
        if not selected(path) or not path.lower().endswith(".md"):
            continue
        if v.is_system_path(path, system):
            excluded.append({"path": path, "reason": "system_file"}); continue
        try:
            raw = (root / path).read_bytes()
        except OSError as error:
            errors.append({"path": path, "error_type": type(error).__name__}); continue
        result = {"path": path, "source_sha256": hashlib.sha256(raw).hexdigest(),
                  "attributes": v.validate_note(raw, path, system),
                  "links": links.audit_links(raw, path, index, system),
                  "tags": _tag_report(raw, registry)}
        results.append(result)
    statuses = Counter(row["status"] for item in results for row in item["links"])
    attribute_errors = sum(d["severity"] == "error" for item in results for d in item["attributes"]["diagnostics"])
    summary = {"files": len(results), "knowledge_entities": sum(item["attributes"]["is_knowledge_entity"] for item in results),
               "attribute_classifications": dict(Counter(item["attributes"]["classification"] for item in results)),
               "links": {name: statuses[name] for name in links.STATUSES},
               "tag_skipped": sum(item["tags"]["action"] == "skip" for item in results),
               "errors": attribute_errors + statuses["invalid_syntax"] + len(errors)}
    return {"ok": summary["errors"] == 0, "dry_run": True, "writes": 0, "proposed_changes": [],
            "formatter": {"status": "not_located", "integrated": False},
            "scope": {"root": str(root), "requested": requested, "audited": [item["path"] for item in results],
                      "excluded_sources": excluded, "file_errors": errors, "target_index": index.scope},
            "summary": summary, "results": results,
            "claim": "Static audit only; not an Obsidian runtime broken-link verdict"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    command = commands.add_parser("audit")
    command.add_argument("--vault-root", type=Path, required=True)
    command.add_argument("--scope", action="append", type=Path, required=True)
    command.add_argument("--format", choices=("json", "text"), default="json")
    args = parser.parse_args(argv)
    try:
        report = audit(args.vault_root, args.scope)
        print(json.dumps(report if args.format == "json" else {"summary": report["summary"], "scope": report["scope"], "claim": report["claim"]}, ensure_ascii=False, indent=2))
        return 0 if report["ok"] else 1
    except (v.ConfigurationError, OSError, ValueError, v.yaml.YAMLError) as error:
        print(json.dumps({"ok": False, "configuration_error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
