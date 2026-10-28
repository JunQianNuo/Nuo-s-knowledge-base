"""Explicit standard-tag vocabulary and hash-bound, non-inventive tag proposals."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import unicodedata

import yaml
from . import model, transaction

TAG_ROOT = "99_System/knowledge/tags"


def load(root: Path) -> dict:
    root = Path(root).resolve()
    records = {}
    for scope in (TAG_ROOT, "总览/标签库"):
        for path in model.iter_files(root, (scope,)):
            if path.suffix.lower() != ".md":
                continue
            raw = path.read_bytes()
            data, body = model.read_note(raw)
            if "canonical_tag" not in data:
                continue
            canonical = data["canonical_tag"]
            if not isinstance(canonical, str) or not canonical.strip():
                raise ValueError("Invalid canonical tag record: " + str(path))
            records[path.relative_to(root).as_posix()] = {"metadata": data, "raw": raw, "body": body}
        if records:
            break
    names, canonical_paths = {}, {}
    for path, record in records.items():
        data = record["metadata"]
        canonical = data["canonical_tag"]
        aliases = data.get("tag_aliases", [])
        aliases = [aliases] if isinstance(aliases, str) else aliases
        if not isinstance(aliases, list) or any(not isinstance(name, str) for name in aliases):
            raise ValueError("Tag aliases must be strings")
        canonical_paths.setdefault(canonical.casefold(), []).append(path)
        for name in [canonical, *aliases]:
            folded = name.casefold()
            if folded in names and names[folded] != canonical:
                names[folded] = None
            else:
                names.setdefault(folded, canonical)
        for name in data.get("ambiguous_aliases", []):
            names[name.casefold()] = None
    return {"records": records, "names": names, "canonical_paths": canonical_paths}


def canonicalize(registry: dict, names: list[str]) -> list[str]:
    if not isinstance(names, list) or any(not isinstance(name, str) or not name.strip() for name in names):
        raise ValueError("Explicit tags must be a list of nonempty strings")
    result = []
    for name in names:
        canonical = registry["names"].get(name.casefold()) or name
        if canonical not in result:
            result.append(canonical)
    return result


def _replace_list(raw, key, values):
    text = raw.decode("utf-8")
    match = re.match(r"\A\ufeff?---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", text, re.DOTALL)
    if match is None:
        raise ValueError("Explicit tag maintenance requires frontmatter")
    node = yaml.compose(match.group(1), Loader=yaml.SafeLoader)
    block = json.dumps(values, ensure_ascii=False)
    for field, value in node.value:
        if field.value == key:
            start = match.start(1) + field.start_mark.index
            end = match.start(1) + value.end_mark.index
            if isinstance(value, yaml.SequenceNode) and not value.flow_style and value.value:
                end = match.start(1) + value.value[-1].end_mark.index
            return (text[:start] + key + ": " + block + text[end:]).encode("utf-8")
    newline = "\r\n" if "\r\n" in text else "\n"
    return (text[:match.end(1)] + newline + key + ": " + block + text[match.end(1):]).encode("utf-8")


def _operation(name, before, after, reason):
    return {"source": name if before is not None else None, "target": name, "content": after,
            "reason": reason, "expected_sha256": hashlib.sha256(before).hexdigest() if before is not None else None}


def _valid_name(name):
    return isinstance(name, str) and bool(name) and not name.isdecimal() and all(
        char in "_-/" or unicodedata.category(char)[0] in "LN" for char in name)


def register(root: Path, canonical: str, aliases=()) -> dict:
    root = Path(root).resolve()
    aliases = list(aliases)
    if not _valid_name(canonical) or any(not isinstance(name,str) or not name.strip() or name!=name.strip() or '\n' in name or '\r' in name for name in aliases):
        raise ValueError("Standard tags require legal tag names; aliases must be explicit nonempty names")
    registry = load(root)
    names = registry["names"]
    if canonical.casefold() in names and names[canonical.casefold()] is None:
        raise ValueError("Ambiguous tag cannot be registered or merged automatically")
    canonical = names.get(canonical.casefold(), canonical)
    for alias in aliases:
        if alias.casefold() in names and names[alias.casefold()] != canonical:
            raise ValueError("Alias collides with another or ambiguous standard name: " + alias)
    paths = registry["canonical_paths"].get(canonical.casefold(), [])
    if len(paths) > 1:
        raise ValueError("Duplicate canonical records require manual review")
    if paths:
        name = paths[0]
        transaction.safe_path(root, name)
        previous = registry["records"][name]["raw"]
        data, _ = model.read_note(previous)
        values = data.get("tag_aliases", [])
        values = [values] if isinstance(values, str) else list(values)
        for alias in aliases:
            if alias != canonical and alias not in values:
                values.append(alias)
        after = _replace_list(previous, "tag_aliases", values) if values != data.get("tag_aliases", []) else previous
    else:
        name = TAG_ROOT + "/条目/标签-" + canonical.replace("/", "／") + ".md"
        path = transaction.safe_path(root, name)
        if path.exists():
            raise ValueError("Tag target is already occupied")
        previous = None
        after = model.render_note({"canonical_tag": canonical, "tag_aliases": list(dict.fromkeys(alias for alias in aliases if alias != canonical))},
                                  ("\n# " + canonical + "\n").encode("utf-8"))
    operations = [] if previous == after else [_operation(name, previous, after, "Explicit standard tag registration")]
    return {"canonical": canonical, "existing": bool(paths), "operations": operations}


def normalize(root: Path, paths: list[str]) -> list[dict]:
    root = Path(root).resolve()
    registry, notes, operations = load(root), model.scan(root), []
    seen = set()
    for name in paths:
        transaction.safe_path(root, name)
        if name not in notes or name.casefold() in seen or model.validate(notes[name]["data"]):
            raise ValueError("Normalization needs unique valid content notes: " + name)
        seen.add(name.casefold())
        entry = notes[name]
        previous = entry["data"].get("tags", [])
        normalized = canonicalize(registry, previous)
        if normalized != previous:
            operations.append(_operation(name, entry["raw"], _replace_list(entry["raw"], "tags", normalized), "Normalize existing explicit unambiguous tags"))
    return operations
