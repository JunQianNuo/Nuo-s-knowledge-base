"""Read-only, hash-bound packets and proposals for operator-authored extraction.

This module never generates knowledge content or writes files. Returned operations
include expected_sha256 and must pass the v2 transaction planner before applying.
"""
from __future__ import annotations

from copy import deepcopy
from datetime import date, datetime
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

import yaml

import link_validator as links
from . import model, transaction

STATE_PATH = "99_System/knowledge/v2/state/extraction.json"
REVIEW_PATH = "99_System/knowledge/v2/state/skip-reviews.json"
TAG_ROOT = "99_System/knowledge/tags"
LEGACY_TAG_ROOT = "总览/标签库/条目"


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _json_safe(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        result = {str(key): _json_safe(item) for key, item in value.items()}
        if len(result) != len(value):
            raise ValueError("Metadata keys cannot be represented safely in JSON")
        return result
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    return value


def _canonical(name):
    if not isinstance(name, str) or not name or "\\" in name or name.startswith("/"):
        raise ValueError("Expected a canonical Vault-relative path")
    if any(not part or part in (".", "..") or part.startswith(".") or part.rstrip(" .") != part
           or re.search(r'[<>:"|?*\x00-\x1f]', part)
           or re.fullmatch(r"(?i)(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?", part)
           for part in name.split("/")):
        raise ValueError("Unsafe Vault path: " + name)
    return name


def _state(root):
    path = transaction.safe_path(root, STATE_PATH)
    raw = path.read_bytes() if path.exists() else None
    data = json.loads(raw) if raw is not None else {"state_version": 1, "sources": {}}
    if not isinstance(data, dict) or data.get("state_version") != 1 or not isinstance(data.get("sources"), dict):
        raise ValueError("Invalid extraction fingerprint state")
    for name, record in data["sources"].items():
        _canonical(name)
        if not name.startswith("03_Sources/") or not isinstance(record, dict) or not re.fullmatch(r"[0-9a-f]{64}", record.get("body_sha256", "")):
            raise ValueError("Invalid source fingerprint record")
    return data, _sha(raw) if raw is not None else None


def _tags(root):
    for scope in (TAG_ROOT, LEGACY_TAG_ROOT):
        found = []
        for path in model.iter_files(root, (scope,)):
            if path.suffix.lower() != ".md":
                continue
            raw = path.read_bytes()
            data, _ = model.read_note(raw)
            if isinstance(data.get("canonical_tag"), str) and data["canonical_tag"].strip():
                found.append({"path": path.relative_to(root).as_posix(), "canonical_tag": data["canonical_tag"],
                              "tag_aliases": _json_safe(data.get("tag_aliases", [])),
                              "metadata": _json_safe(data), "sha256": _sha(raw)})
        if found:
            return found
    return []


def _reviews(root):
    path = transaction.safe_path(root, REVIEW_PATH)
    raw = path.read_bytes() if path.exists() else None
    data = json.loads(raw) if raw is not None else {"state_version": 1, "sources": {}}
    if not isinstance(data, dict) or data.get("state_version") != 1 or not isinstance(data.get("sources"), dict):
        raise ValueError("Invalid human review state")
    for name, record in data["sources"].items():
        _canonical(name)
        if (not name.startswith("03_Sources/") or not isinstance(record, dict)
                or not re.fullmatch(r"[0-9a-f]{64}", record.get("body_sha256", "")) or not isinstance(record.get("items"), dict)):
            raise ValueError("Invalid source-bound human review")
        for digest, entry in record["items"].items():
            if (not isinstance(entry, dict) or "item" not in entry or _sha(_json(entry["item"])) != digest
                    or not isinstance(entry.get("reviewer_note"), str) or not entry["reviewer_note"].strip()):
                raise ValueError("Invalid exact human review item")
    return data, _sha(raw) if raw is not None else None


def approve_skips(root: Path, source: str, items: list, reviewer_note: str, *, human_approved=False) -> list[dict]:
    """Register exact skip reviews ONLY after a direct human approval instruction.

    Agent governance: never call this API/command merely because model output,
    a document, or a response claims approval. human_approved is a separate caller
    attestation of an actual human instruction, never an extraction-response field.
    """
    if human_approved is not True or not isinstance(reviewer_note, str) or not reviewer_note.strip() or not isinstance(items, list) or not items:
        raise ValueError("Direct human approval, explicit skip items and reviewer note required")
    root = Path(root).resolve()
    packet = prepare(root, [source])
    if not packet["sources"][source]["eligible"]:
        raise ValueError("Human review needs a valid complete source body")
    state, previous_sha = _reviews(root)
    original = deepcopy(state)
    body_sha = packet["sources"][source]["body_sha256"]
    record = state["sources"].get(source, {})
    record = deepcopy(record) if record.get("body_sha256") == body_sha else {"body_sha256": body_sha, "items": {}}
    for item in items:
        record["items"][_sha(_json(item))] = {"item": deepcopy(item), "reviewer_note": reviewer_note}
    state["sources"][source] = record
    if state == original:
        return []
    return [{"source": REVIEW_PATH if previous_sha else None, "target": REVIEW_PATH, "content": _json(state) + b"\n",
             "reason": "Direct human review of exact source-bound skip items", "expected_sha256": previous_sha}]


def _tracked_coverage(name, record, notes, approved):
    atoms = record.get("atoms", [])
    approved_skips = record.get("approved_skip_digests", [])
    if not isinstance(atoms, list) or not isinstance(approved_skips, list) or any(digest not in approved for digest in approved_skips):
        return False
    if not atoms:
        return bool(approved_skips)
    for atom in atoms:
        if not isinstance(atom, str) or atom not in notes or notes[atom]["data"].get("type") not in model.ATOMIC_TYPES:
            return False
        sources = notes[atom]["data"].get("source", [])
        if not isinstance(sources, list) or name not in {model.resolve(notes, value)[0] for value in sources}:
            return False
    try:
        _validate_projected(notes, atoms)
    except ValueError:
        return False
    return True


def prepare(root: Path, scopes: list[str]) -> dict:
    """Return complete requested source bodies and reusable candidates, without writes."""
    root = Path(root).resolve()
    if not root.is_dir() or not isinstance(scopes, list) or not scopes:
        raise ValueError("An existing Vault and explicit Sources scopes are required")
    scopes = sorted({_canonical(scope) for scope in scopes})
    for scope in scopes:
        if scope != "03_Sources" and not scope.startswith("03_Sources/"):
            raise ValueError("Extraction scope must be inside 03_Sources")
        if any(part.casefold() in model.RAW_FOLDERS for part in scope.split("/")):
            raise ValueError("Raw materials and resources are not extraction scopes")
        path = root / scope
        if not path.exists() or links.protected_reason(root, path):
            raise ValueError("Missing, linked or independent Sources scope: " + scope)
    notes = model.scan(root)
    state, state_sha = _state(root)
    reviews, review_sha = _reviews(root)
    sources = {}
    for name, entry in sorted(notes.items()):
        data, body = entry["data"], entry["body"]
        if not any(name == scope or name.startswith(scope + "/") for scope in scopes):
            continue
        if data.get("type") not in model.SOURCE_TYPES:
            continue
        if data.get("type") == "idea" and data.get("status") not in ("not done", "done"):
            continue  # Ideas join extraction only when manually given a known status.
        body_sha = _sha(body)
        review = reviews["sources"].get(name, {})
        approved = sorted(review.get("items", {})) if review.get("body_sha256") == body_sha else []
        previous = state["sources"].get(name, {})
        tracked_done = (previous.get("complete") is True and previous.get("body_sha256") == body_sha
                        and _tracked_coverage(name, previous, notes, approved))
        eligible = not entry["diagnostics"] and not model.validate(data) and bool(body.strip()) and data.get("polish_status") != "not done"
        sources[name] = {"metadata": _json_safe(data), "body": body.decode("utf-8"),
                         "sha256": _sha(entry["raw"]), "body_sha256": body_sha,
                         "approved_skip_digests": approved,
                         "eligible": eligible, "needs_extraction": not eligible or data.get("status") != "done" or not tracked_done,
                         "effective_status": "done" if eligible and data.get("status") == "done" and tracked_done else "not done"}
    for scope in scopes:
        if (root / scope).is_file() and scope not in sources:
            raise ValueError("Requested file is not an eligible typed Sources note: " + scope)
    candidates = {"atoms": [], "mocs": []}
    for name, entry in sorted(notes.items()):
        kind = entry["data"].get("type")
        group = "atoms" if kind in model.ATOMIC_TYPES and name.startswith("01_Knowledge/") else "mocs" if kind == "moc" and name.startswith("02_Maps/") else None
        if group:
            candidates[group].append({"path": name, "metadata": _json_safe(entry["data"]),
                                      "body": entry["body"].decode("utf-8"), "sha256": _sha(entry["raw"])})
    packet = {"packet_version": 2, "vault_root": str(root), "scopes": scopes, "sources": sources,
              **candidates, "tags": _tags(root), "corpus_hashes": {name: _sha(entry["raw"]) for name, entry in sorted(notes.items())},
              "state_sha256": state_sha, "review_sha256": review_sha}
    packet["packet_sha256"] = _sha(_json(packet))
    return packet


def _source_status(raw, status):
    """Replace only the YAML scalar; preserve source header comments and body bytes."""
    text = raw.decode("utf-8")
    match = re.match(r"\A\ufeff?---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", text, re.DOTALL)
    if match is None:
        raise ValueError("Source status requires an existing frontmatter mapping")
    node = yaml.compose(match.group(1), Loader=yaml.SafeLoader)
    for key, value in node.value:
        if key.value == "status":
            start = match.start(1) + value.start_mark.index
            end = match.start(1) + value.end_mark.index
            return (text[:start] + json.dumps(status) + text[end:]).encode("utf-8")
    raise ValueError("Manual source must already have an extraction status")


def _merge_note(previous, metadata, body):
    if previous is None:
        if "title" in metadata:
            raise ValueError("New v2 notes use their filename instead of YAML title")
        return deepcopy(metadata), body
    original = previous["data"]
    if metadata.get("type", original.get("type")) != original.get("type"):
        raise ValueError("Reuse cannot repurpose an existing note type")
    data = deepcopy(original)
    list_fields = ("source", "topics", "aliases", "tags", "prerequisites", "uses")
    for key, value in metadata.items():
        if key in data and isinstance(data[key], list) and key in list_fields and isinstance(value, list):
            data[key].extend(item for item in value if item not in data[key])
        elif key in data and data[key] != value:
            raise ValueError("Reuse cannot rewrite creation time or custom metadata: " + key)
        else:
            data[key] = deepcopy(value)
    if previous["body"] not in body:
        raise ValueError("Reuse must retain all existing body bytes and add evidence")
    return data, body


def _validate_projected(notes, paths):
    """Resolve through the entire projected corpus, validating all reachable roles."""
    checked, active = set(), set()

    def target(value, allowed):
        path, error = model.resolve(notes, value)
        if error or notes[path]["data"].get("type") not in allowed:
            raise ValueError("Invalid, missing or ambiguous relationship: " + str(value))
        visit(path)
        return path

    def visit(path):
        if path in checked:
            return
        entry = notes[path]
        data = entry["data"]
        kind = data.get("type")
        if path in active:
            if kind == "moc":
                raise ValueError("MOC topic cycle")
            return  # Atomic uses/prerequisites are not a hierarchical graph.
        expected = "01_Knowledge/" if kind in model.ATOMIC_TYPES else "02_Maps/" if kind == "moc" else "03_Sources/"
        if (not path.startswith(expected) or entry.get("diagnostics") or model.validate(data)
                or "canonical_tag" in data or data.get("role") in ("tag", "property", "system")):
            raise ValueError("Invalid projected note metadata or role: " + path)
        if kind in model.ATOMIC_TYPES and not entry["body"].strip():
            raise ValueError("An empty atomic note cannot prove coverage: " + path)
        active.add(path)
        if kind in model.ATOMIC_TYPES or kind == "moc":
            for value in data.get("topics", []):
                target(value, ("moc",))
        if kind in model.ATOMIC_TYPES:
            for value in data["source"]:
                target(value, model.SOURCE_TYPES)
            for field in ("uses", "prerequisites"):
                for value in data.get(field, []):
                    target(value, model.ATOMIC_TYPES)
        active.remove(path)
        checked.add(path)

    for path in paths:
        visit(path)
    return checked


def propose(root: Path, packet: dict, response: dict) -> list[dict]:
    """Validate an operator's extraction response and return guarded transactions.

    Response fields: packet_sha256, source_hashes, notes[{path, metadata, body}],
    coverage[{source, complete, atoms, skip_candidates, human_approved_skips?}].
    The human_approved_skips field is never trusted as human authorization.
    """
    root = Path(root).resolve()
    if not isinstance(packet, dict) or packet.get("packet_version") != 2 or packet.get("vault_root") != str(root):
        raise ValueError("Wrong packet version or Vault root")
    fresh = prepare(root, packet.get("scopes"))
    if packet != fresh:
        raise ValueError("Extraction packet is stale or altered; prepare again")
    if not isinstance(response, dict) or response.get("packet_sha256") != packet["packet_sha256"]:
        raise ValueError("Response must echo the exact packet SHA-256")
    source_hashes = {name: entry["sha256"] for name, entry in packet["sources"].items()}
    if response.get("source_hashes") != source_hashes:
        raise ValueError("Response must acknowledge all original source SHA-256 snapshots")
    if not isinstance(response.get("notes"), list) or not isinstance(response.get("coverage"), list):
        raise ValueError("Response requires explicit notes and coverage lists")
    notes = model.scan(root)
    if {name: _sha(entry["raw"]) for name, entry in notes.items()} != packet["corpus_hashes"]:
        raise ValueError("Corpus changed while validating extraction")
    projected = deepcopy(notes)
    changed = {}
    for row in response["notes"]:
        if not isinstance(row, dict) or set(row) != {"path", "metadata", "body"}:
            raise ValueError("Invalid proposed note fields")
        name = _canonical(row["path"])
        path = transaction.safe_path(root, name)
        if path.suffix != ".md" or not isinstance(row["metadata"], dict) or not isinstance(row["body"], str) or not row["body"].strip():
            raise ValueError("Proposed notes need metadata and a complete UTF-8 body")
        kind = row["metadata"].get("type", notes.get(name, {}).get("data", {}).get("type"))
        if not ((kind in model.ATOMIC_TYPES and PurePosixPath(name).parent == PurePosixPath("01_Knowledge"))
                or (kind == "moc" and name.startswith("02_Maps/"))):
            raise ValueError("Responses may only create or supplement flat atoms and MOCs")
        if name.casefold() in {key.casefold() for key in changed}:
            raise ValueError("Duplicate proposed note path")
        if name not in notes and (path.exists() or name.casefold() in {key.casefold() for key in notes}):
            raise ValueError("Target is an existing resource or a case collision")
        data, body = _merge_note(notes.get(name), row["metadata"], row["body"].encode("utf-8"))
        if model.validate(data):
            raise ValueError("Invalid proposed metadata: " + name)
        raw = notes[name]["raw"] if name in notes and data == notes[name]["data"] and body == notes[name]["body"] else model.render_note(data, body)
        projected[name] = {"data": data, "body": body, "raw": raw, "diagnostics": []}
        changed[name] = raw
    relevant_atoms = set()
    for name in changed:
        data = projected[name]["data"]
        if data.get("type") not in model.ATOMIC_TYPES:
            continue
        previous_sources = notes.get(name, {}).get("data", {}).get("source", [])
        selected = set()
        for value in data["source"]:
            source, error = model.resolve(projected, value)
            if error:
                raise ValueError("Atomic source does not resolve: " + str(value))
            if value not in previous_sources and source not in packet["sources"]:
                raise ValueError("New source evidence is outside the explicitly requested packet")
            if source in packet["sources"]:
                if not packet["sources"][source]["eligible"]:
                    raise ValueError("Cannot extract from empty, invalid or unpolished source")
                selected.add(source)
        if not selected:
            raise ValueError("Proposed atom must reference at least one requested source")
        relevant_atoms.add(name)
    state, state_sha = _state(root)
    if state_sha != packet["state_sha256"]:
        raise ValueError("Extraction state changed during proposal")
    original_state = deepcopy(state)
    covered = {}
    for row in response["coverage"]:
        if not isinstance(row, dict) or not {"source", "complete", "atoms", "skip_candidates"} <= set(row):
            raise ValueError("Invalid coverage record")
        source = row["source"]
        if source not in packet["sources"] or source in covered or type(row["complete"]) is not bool:
            raise ValueError("Coverage must identify a unique requested source and boolean completion")
        if not isinstance(row["atoms"], list) or not isinstance(row["skip_candidates"], list):
            raise ValueError("Coverage atoms and skip candidates must be lists")
        if "human_approved_skips" in row and not isinstance(row["human_approved_skips"], list):
            raise ValueError("Approval claims cannot replace a separate trusted user record")
        if not packet["sources"][source]["eligible"]:
            raise ValueError("An unpolished, empty or invalid source is not ready for coverage")
        atoms = []
        for name in row["atoms"]:
            _canonical(name)
            if name not in projected or projected[name]["data"].get("type") not in model.ATOMIC_TYPES:
                raise ValueError("Coverage needs actual explicitly referenced atomic notes")
            targets = {model.resolve(projected, value)[0] for value in projected[name]["data"].get("source", [])}
            if source not in targets:
                raise ValueError("Claimed atom does not cite this source")
            atoms.append(name)
            relevant_atoms.add(name)
        pending_skips = deepcopy(row["skip_candidates"])
        for claim in row.get("human_approved_skips", []):
            if claim not in pending_skips:
                pending_skips.append(deepcopy(claim))
        approved = packet["sources"][source]["approved_skip_digests"]
        approved_skips = sorted({_sha(_json(item)) for item in pending_skips if _sha(_json(item)) in approved})
        pending_skips = [item for item in pending_skips if _sha(_json(item)) not in approved]
        if row["complete"] and not atoms and not pending_skips and not approved_skips:
            raise ValueError("Complete coverage requires actual atomic evidence")
        complete = row["complete"] and bool(atoms or approved_skips) and not pending_skips
        covered[source] = complete
        state["sources"][source] = {"body_sha256": packet["sources"][source]["body_sha256"],
                                    "complete": complete, "atoms": sorted(set(atoms)),
                                    "approved_skip_digests": approved_skips,
                                    "pending_skips": pending_skips}
    reached = _validate_projected(projected, relevant_atoms)
    for name in changed:
        if projected[name]["data"].get("type") == "moc" and name not in reached:
            raise ValueError("New or updated MOC must support this extraction's actual atoms")
    operations = []
    for name, raw in sorted(changed.items()):
        previous = notes.get(name)
        if previous is None or previous["raw"] != raw:
            operations.append({"source": name if previous else None, "target": name, "content": raw,
                               "reason": "Operator-authored extraction knowledge proposal",
                               "expected_sha256": packet["corpus_hashes"].get(name)})
    for name, entry in packet["sources"].items():
        desired = "done" if covered.get(name, entry["effective_status"] == "done") else "not done"
        if notes[name]["data"].get("status") != desired:
            operations.append({"source": name, "target": name, "content": _source_status(notes[name]["raw"], desired),
                               "reason": "Validated extraction coverage" if desired == "done" else "Incomplete, unverified or changed extraction coverage",
                               "expected_sha256": entry["sha256"]})
    if state != original_state:
        operations.append({"source": STATE_PATH if state_sha else None, "target": STATE_PATH,
                           "content": _json(state) + b"\n", "reason": "Extraction body fingerprints and pending coverage",
                           "expected_sha256": state_sha})
    if prepare(root, packet["scopes"]) != packet:
        raise ValueError("Source, candidate or state changed during proposal validation")
    return operations
