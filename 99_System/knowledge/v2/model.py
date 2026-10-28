"""V2 metadata, byte-preserving note IO and read-only relationship audit."""
from __future__ import annotations

from datetime import date, datetime
import json
import os
from pathlib import Path, PurePosixPath
import re

from jsonschema import Draft202012Validator
import yaml

from validator import parse_frontmatter

ATOMIC_TYPES = ("concept", "proposition", "method")
SOURCE_TYPES = ("lecture", "review", "homework", "book", "paper", "web", "idea")
TYPES = ATOMIC_TYPES + ("moc",) + SOURCE_TYPES
CONTENT_ROOTS = ("00_Inbox", "01_Knowledge", "02_Maps", "03_Sources")
RAW_FOLDERS = {"raw", "resources", "assets", "附件", "ppt课件", "pdf课件", "课件", "原始录制", "原始转写", "转换资料"}
SCHEMA = json.loads((Path(__file__).parent / "schemas/note.schema.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA)


def read_note(raw: bytes) -> tuple[dict, bytes]:
    """Parse with the v1 strict loader while retaining the original body bytes."""
    data = parse_frontmatter(raw)
    if data is None:
        return {}, raw
    lines = raw.splitlines(keepends=True)
    for index, line in enumerate(lines[1:], 1):
        if re.fullmatch(rb"---[ \t]*(?:\r?\n)?", line):
            return data, b"".join(lines[index + 1:])
    raise ValueError("Missing closing frontmatter delimiter")


def render_note(data: dict, body: bytes) -> bytes:
    header = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=1000)
    return ("---\n" + header + "---\n").encode("utf-8") + body


def _diagnostic(code, field, message, **extra):
    return {"code": code, "field": field, "message": message, **extra}


def link_target(value: str) -> str | None:
    """Only whole-note property Wiki-links; literal filename carets are valid."""
    if not isinstance(value, str) or not re.fullmatch(r"\[\[[^\[\]\r\n]+\]\]", value):
        return None
    target = value[2:-2]
    if not target or any(c in target for c in ("#", "|", "\\")):
        return None
    path = PurePosixPath(target)
    if path.is_absolute() or any(part in (".", "..") for part in target.split("/")):
        return None
    return target if target.lower().endswith(".md") else target + ".md"


def validate(data: dict) -> list[dict]:
    diagnostics = []
    for error in VALIDATOR.iter_errors(data):
        field = "/".join(map(str, error.absolute_path))
        if error.validator == "required":
            field = error.message.split("'", 2)[1]
        diagnostics.append(_diagnostic("E_SCHEMA", field, error.message))
    if not isinstance(data, dict):
        return diagnostics
    kind = data.get("type")
    if kind == "idea":
        return diagnostics  # All idea properties remain manually maintained.
    stamp = data.get("time")
    if isinstance(stamp, str):
        try:
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})", stamp):
                raise ValueError
            if datetime.fromisoformat(stamp.replace("Z", "+00:00")).utcoffset() is None:
                raise ValueError
        except ValueError:
            diagnostics.append(_diagnostic("E_TIME", "time", "Expected a real ISO creation timestamp with timezone"))
    for name in ("lecture_date", "due_date"):
        value = data.get(name)
        if value is not None:
            try:
                if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                    raise ValueError
                date.fromisoformat(value)
            except ValueError:
                diagnostics.append(_diagnostic("E_DATE", name, "Expected a real YYYY-MM-DD date"))
    fields = ["topics", "prerequisites", "uses"]
    if kind in ATOMIC_TYPES:
        fields.append("source")
        if "subject" in data:
            diagnostics.append(_diagnostic("E_ATOMIC_SUBJECT", "subject", "Atomic notes do not have course ownership"))
    if kind in SOURCE_TYPES and "topics" in data:
        diagnostics.append(_diagnostic("E_SOURCE_TOPICS", "topics", "Source notes do not participate in the MOC hierarchy"))
    for name in fields:
        values = data.get(name)
        if isinstance(values, list):
            for value in values:
                if link_target(value) is None:
                    diagnostics.append(_diagnostic("E_LINK_SHAPE", name, "Expected a whole-note Wiki-link"))
    return diagnostics


def iter_files(root: Path, scopes=CONTENT_ROOTS, include_resources=False):
    """Never follow junctions, links, nested repositories, raw or resource trees."""
    root = Path(root)
    excluded = RAW_FOLDERS - {"ppt课件", "pdf课件", "课件"} if include_resources else RAW_FOLDERS
    for scope in scopes:
        start = root / scope
        ancestors = [start, *list(start.parents)[:len(start.relative_to(root).parts) - 1]]
        if not start.is_dir() or any(p.is_symlink() or p.is_junction() or (p / ".git").exists() for p in ancestors):
            continue
        for folder, dirs, names in os.walk(start, followlinks=False):
            parent = Path(folder)
            dirs[:] = sorted(name for name in dirs if not name.startswith(".") and name.casefold() not in excluded and not (parent / name).is_symlink() and not (parent / name).is_junction() and not (parent / name / ".git").exists())
            for name in sorted(names):
                path = parent / name
                if not path.is_symlink() and not path.is_junction() and path.is_file():
                    yield path


def scan(root: Path) -> dict[str, dict]:
    notes = {}
    root = Path(root)
    for path in iter_files(root):
        if path.suffix.lower() != ".md":
            continue
        raw = path.read_bytes()
        try:
            data, body = read_note(raw)
            if "canonical_tag" in data or data.get("role") in ("tag", "property", "system"):
                continue
            if data.get("type") not in TYPES and data.get("schema_version") != 2:
                continue  # Untyped course materials are resources, not entities.
            diagnostics = []
        except (UnicodeError, ValueError, yaml.YAMLError, RecursionError) as error:
            data, body = {}, raw
            diagnostics = [_diagnostic("E_FRONTMATTER", "", str(error))]
        notes[path.relative_to(root).as_posix()] = {"data": data, "body": body, "raw": raw, "diagnostics": diagnostics}
    return notes


def resolve(notes: dict, value: str) -> tuple[str | None, str | None]:
    target = link_target(value)
    if target is None:
        return None, "E_LINK_SHAPE"
    folded = target.casefold()
    matches = [key for key in notes if key.casefold() == folded]
    if not matches:
        matches = [key for key in notes if key.casefold().endswith("/" + folded)]
    if len(matches) > 1:
        return None, "E_LINK_AMBIGUOUS"
    return (matches[0], None) if matches else (None, "E_LINK_MISSING")


def audit(root: Path) -> dict:
    notes = scan(root)
    diagnostics = []
    counts = {kind: 0 for kind in TYPES}
    valid = {}
    for path, entry in notes.items():
        errors = entry["diagnostics"] + validate(entry["data"])
        kind = entry["data"].get("type")
        expected = "01_Knowledge/" if kind in ATOMIC_TYPES else "02_Maps/" if kind == "moc" else "03_Sources/"
        if not path.startswith(expected):
            errors.append(_diagnostic("E_LOCATION", "type", f"Typed content belongs under {expected}"))
        diagnostics.extend(dict(item, path=path) for item in errors)
        valid[path] = not errors
    for path, entry in notes.items():
        data = entry["data"]
        fields = ["topics", "uses", "prerequisites"]
        if data.get("type") in ATOMIC_TYPES:
            fields.append("source")
        for field in fields:
            if not isinstance(data.get(field), list):
                continue
            for value in data[field]:
                target, error = resolve(notes, value)
                if error:
                    diagnostics.append(_diagnostic(error, field, f"Unresolved or ambiguous note {value}", path=path))
                    if field in ("topics", "source"):
                        diagnostics.append(_diagnostic("E_TOPIC_TARGET" if field == "topics" else "E_SOURCE_TARGET", field, "A valid typed target is required", path=path))
                    continue
                target_type = notes[target]["data"].get("type")
                if field == "topics" and (target_type != "moc" or not valid[target] or not target.startswith("02_Maps/")):
                    diagnostics.append(_diagnostic("E_TOPIC_TARGET", field, f"Topic is not a valid MOC：{target}", path=path))
                if field == "source" and (target_type not in SOURCE_TYPES or not valid[target] or not target.startswith("03_Sources/")):
                    diagnostics.append(_diagnostic("E_SOURCE_TARGET", field, f"Source is not a valid Sources note：{target}", path=path))
    # Imported here to keep the model usable independently of view generation.
    from .views import descendants
    try:
        for path, entry in notes.items():
            if entry["data"].get("type") == "moc":
                descendants(notes, path)
    except ValueError as error:
        diagnostics.append(_diagnostic("E_MOC_GRAPH", "topics", str(error)))
        # A malformed hierarchy has no valid navigation interpretation.
        for path, entry in notes.items():
            if entry["data"].get("type") == "moc":
                valid[path] = False
    invalid_paths = {item.get("path") for item in diagnostics}
    for path in invalid_paths:
        if path in valid:
            valid[path] = False
    # Propagate invalid MOC/source identity through relationships. A schema-valid
    # atom is not a validated entity if its source or topic is invalid.
    changed = True
    while changed:
        changed = False
        for path, entry in notes.items():
            if not valid[path]:
                continue
            fields = ("topics", "source") if entry["data"].get("type") in ATOMIC_TYPES else ("topics",) if entry["data"].get("type") == "moc" else ()
            for field in fields:
                for value in entry["data"].get(field, []):
                    target, error = resolve(notes, value)
                    if error or not valid.get(target):
                        valid[path] = False
                        changed = True
    for path, entry in notes.items():
        if valid[path]:
            counts[entry["data"]["type"]] += 1
    counts["entities"] = sum(counts[kind] for kind in TYPES)
    counts["atomic"] = sum(counts[kind] for kind in ATOMIC_TYPES)
    return {"errors": len(diagnostics), "counts": counts, "diagnostics": diagnostics}
