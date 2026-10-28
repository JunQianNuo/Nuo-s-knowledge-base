"""Maintain Obsidian tags using the Markdown records behind 标签库.base.

Default is read-only. --apply backs up the exact current bytes before writing.
Only existing explicit tags are normalized; no tags are inferred from other fields.
New/mixed metadata is skipped both when planning and immediately before execution.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata
import uuid
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCOPES = ("课程", "概念", "知识点", "方法", "数学建模/知识体系")
FM = re.compile(r"\A\ufeff?---[ \t]*\r?\n(?P<yaml>.*?)(?P<tail>^---[ \t]*(?:\r?\n|$).*)\Z", re.S | re.M)


def valid_tag(tag: str) -> bool:
    return bool(tag) and not tag.isdecimal() and all(
        c in "_-/" or unicodedata.category(c)[0] in "LN" for c in tag
    )


def values(value) -> list[str]:
    if value is None:
        return []
    return [str(v).strip().lstrip("#") for v in (value if isinstance(value, list) else [value]) if v is not None]


def metadata(raw: bytes) -> dict:
    match = FM.match(raw.decode("utf-8"))
    if not match:
        return {}
    node = yaml.compose(match["yaml"])
    if isinstance(node, yaml.MappingNode):
        keys = [key.value for key, _ in node.value]
        if len(keys) != len(set(keys)):
            raise ValueError("Duplicate frontmatter keys")
    value = yaml.safe_load(match["yaml"])
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise ValueError("Frontmatter must be a mapping")
    return value


def legacy_skip_reason(fm: dict) -> str | None:
    if "schema_version" in fm:
        return "explicit_or_unsupported_schema_version"
    if fm.get("type") in ("concept", "proposition", "method") or fm.get("role") == "moc":
        return "new_type_or_moc_role"
    if any(key in fm for key in ("prerequisites", "about", "uses")):
        return "new_semantic_fields"
    topics = fm.get("topics", [])
    topics = topics if isinstance(topics, list) else [topics]
    if any(isinstance(text, str) and "[[" in text for text in topics):
        return "linked_or_mixed_topics"
    return None


@dataclass(frozen=True)
class Entry:
    canonical_tag: str
    tag_aliases: tuple[str, ...] = ()
    promote: bool = True
    ambiguous_aliases: tuple[str, ...] = ()
    alias_context: tuple[str, ...] = ()


class Registry:
    def __init__(self, entries):
        self.entries = {}
        self.names = {}
        for entry in entries:
            if not valid_tag(entry.canonical_tag):
                raise ValueError(f"Invalid canonical tag: {entry.canonical_tag}")
            key = entry.canonical_tag.casefold()
            if key in self.entries:
                raise ValueError(f"Duplicate canonical tag: {entry.canonical_tag}")
            self.entries[key] = entry
            for name in (entry.canonical_tag, *entry.tag_aliases):
                folded = name.casefold()
                if folded in self.names and self.names[folded].canonical_tag != entry.canonical_tag:
                    raise ValueError(f"Conflicting alias: {name}")
                self.names[folded] = entry

    @classmethod
    def load(cls, directory: Path):
        entries = []
        for path in sorted(directory.glob("标签-*.md")):
            fm = metadata(path.read_bytes())
            if "canonical_tag" not in fm and "legacy_canonical_tag" in fm and "synonym_of" in fm:
                continue
            entries.append(Entry(
                fm["canonical_tag"], tuple(values(fm.get("tag_aliases"))),
                fm.get("promote", True), tuple(values(fm.get("ambiguous_aliases"))),
                tuple(values(fm.get("alias_context"))),
            ))
        if not entries:
            raise ValueError(f"Empty registry: {directory}")
        return cls(entries)

    def resolve(self, name: str, context: str, *, existing=False):
        entry = self.names.get(name.casefold())
        if not entry or (not existing and not entry.promote):
            return None
        if name.casefold() in {a.casefold() for a in entry.ambiguous_aliases}:
            if not any(token.casefold() in context.casefold() for token in entry.alias_context):
                return None
        return entry.canonical_tag


def replace_tags(raw: bytes, tags: list[str]) -> bytes:
    text = raw.decode("utf-8")
    match = FM.match(text)
    if not match:
        return raw
    fm_text = match["yaml"]
    newline = "\r\n" if "\r\n" in text else "\n"
    block = yaml.safe_dump({"tags": tags}, allow_unicode=True, sort_keys=False).replace("\n", newline)
    node = yaml.compose(fm_text)
    tag_nodes = [(k, v) for k, v in node.value if k.value == "tags"] if isinstance(node, yaml.MappingNode) else []
    if len(tag_nodes) > 1:
        raise ValueError("Duplicate tags keys")
    if tag_nodes:
        key, value = tag_nodes[0]
        end = value.end_mark.index
        # Collection end marks can include comments before the next property.
        # A block sequence ends syntactically at its last item, not that mark.
        if isinstance(value, yaml.SequenceNode) and not value.flow_style and value.value:
            end = value.value[-1].end_mark.index
        suffix = fm_text[end:]
        if suffix.startswith(("\r", "\n", " ", "\t")):
            block = block.rstrip("\r\n")
        fm_text = fm_text[:key.start_mark.index] + block + suffix
    else:
        if fm_text and not fm_text.endswith("\n"):
            fm_text += newline
        fm_text += block
    result = (text[:match.start("yaml")] + fm_text + match["tail"]).encode("utf-8")
    old, new = metadata(raw), metadata(result)
    old.pop("tags", None); new.pop("tags", None)
    if old != new or FM.match(result.decode("utf-8"))["tail"] != match["tail"]:
        raise ValueError("Non-tag metadata or note body changed")
    return result


def plan_note(raw: bytes, relative_path: str, registry: Registry) -> bytes:
    fm = metadata(raw)
    if not fm or legacy_skip_reason(fm):
        return raw
    stored = fm.get("tags")
    if stored is None:
        return raw
    original = stored if isinstance(stored, list) else [stored]
    if any(not isinstance(tag, str) or not valid_tag(tag) for tag in original):
        raise ValueError("Invalid explicit tag; manual review required")
    candidates = []
    for tag in original:
        # Empty context intentionally prevents ambiguous aliases being resolved
        # using filenames, titles, topics or semantic relationships.
        candidates.append(registry.resolve(tag, "", existing=True) or tag)
    seen = set(); tags = []
    for tag in candidates:
        if tag.casefold() not in seen:
            seen.add(tag.casefold()); tags.append(tag)
    if not tags or (tags == original and isinstance(fm.get("tags"), list)):
        return raw
    if any(not valid_tag(tag) for tag in tags):
        raise ValueError("Invalid existing tag; manual review required")
    return replace_tags(raw, tags)


def iter_notes(root: Path):
    for scope in SCOPES:
        for path in sorted((root / scope).rglob("*.md")):
            relative = path.relative_to(root)
            if not path.resolve().is_relative_to(root.resolve()):
                continue
            if _protected_path(root, path):
                continue
            if any(part.startswith(".") or part in {"raw", "node_modules", "__pycache__"} for part in relative.parts):
                continue
            yield path


@dataclass(frozen=True)
class Change:
    path: Path
    before: bytes
    after: bytes


def plan_vault(root: Path, registry: Registry, *, skipped: list | None = None):
    changes = []; errors = []
    for path in iter_notes(root):
        before = path.read_bytes()
        try:
            reason = legacy_skip_reason(metadata(before))
            if reason:
                if skipped is not None:
                    skipped.append({"path": path.relative_to(root).as_posix(), "reason": reason})
                continue
            after = plan_note(before, path.relative_to(root).as_posix(), registry)
        except (ValueError, yaml.YAMLError, UnicodeError) as error:
            errors.append({"path": path.relative_to(root).as_posix(), "error": str(error)})
            continue
        if after != before:
            changes.append(Change(path, before, after))
    return changes, errors


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _protected_path(root: Path, path: Path) -> bool:
    root = root.resolve()
    if not path.resolve().is_relative_to(root):
        return True
    for current in (path, *path.parents):
        if current == root:
            break
        if current.is_symlink() or current.is_junction() or (current.is_dir() and (current / ".git").exists()):
            return True
    return False


def apply_changes(root: Path, changes: list[Change], backup: Path, *, registry: Registry | None = None) -> Path:
    root = root.resolve()
    if registry is None:
        registry = Registry.load(root / ("99_System/knowledge/tags/条目" if (root / "99_System/knowledge/tags/条目").is_dir() else "总览/标签库/条目"))

    def verify(change):
        if _protected_path(root, change.path):
            raise RuntimeError(f"Outside or protected path: {change.path}")
        current = change.path.read_bytes()
        if current != change.before:
            raise RuntimeError(f"File changed after scan: {change.path}")
        reason = legacy_skip_reason(metadata(current))
        if reason:
            raise RuntimeError(f"New/mixed metadata skipped at execution: {reason}: {change.path}")
        expected = plan_note(current, change.path.relative_to(root).as_posix(), registry)
        if expected != change.after:
            raise RuntimeError(f"Plan no longer matches explicit-tag-only policy: {change.path}")

    # Check the entire batch before the first write; preserve concurrent user edits.
    if len({str(c.path.resolve()).casefold() for c in changes}) != len(changes):
        raise RuntimeError("Duplicate paths in tag change plan")
    for change in changes:
        verify(change)
    backup.mkdir(parents=True, exist_ok=False)
    manifest = {"root": str(root), "state": "backed_up", "files": []}
    for change in changes:
        relative = change.path.relative_to(root)
        target = backup / "files" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(change.before)
        manifest["files"].append({"path": relative.as_posix(), "before_sha256": sha(change.before), "after_sha256": sha(change.after)})
    manifest_path = backup / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    for change in changes:
        verify(change)
        temp = change.path.with_name(change.path.name + ".tag-" + uuid.uuid4().hex + ".tmp")
        try:
            temp.write_bytes(change.after)
            os.replace(temp, change.path)
        finally:
            if temp.exists():
                temp.unlink()
    manifest["state"] = "applied"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--backup-dir", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    registry = Registry.load(root / ("99_System/knowledge/tags/条目" if (root / "99_System/knowledge/tags/条目").is_dir() else "总览/标签库/条目"))
    skipped = []
    changes, errors = plan_vault(root, registry, skipped=skipped)
    result = {"mode": "apply" if args.apply else "audit", "registry_entries": len(registry.entries),
              "changed_files": len(changes), "errors": errors, "skipped_files": len(skipped), "skipped": skipped,
              "changes": [{"path": c.path.relative_to(root).as_posix(), "tags": metadata(c.after)["tags"]} for c in changes]}
    if args.apply and errors:
        raise RuntimeError("Malformed metadata found; inspect the audit report before applying")
    if args.apply and changes:
        backup = args.backup_dir or Path.home() / ".codex/backups/knowledge-tags" / datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        result["backup_manifest"] = str(apply_changes(root, changes, backup, registry=registry))
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "changes"}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
