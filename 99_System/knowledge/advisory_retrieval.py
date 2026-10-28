"""Scoped in-memory retrieval. Never walks beyond the operator's pinned manifest."""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

from collections import Counter
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re

import maintenance

v = maintenance.v
links = maintenance.links
SYSTEM = Path(__file__).resolve().parent


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def safe_relative(value):
    if not isinstance(value, str) or not value or "\\" in value or ":" in value or value.startswith("/"):
        raise ValueError("Only explicit Vault-relative Markdown paths are accepted")
    if any(part in ("", ".", "..") for part in value.split("/")) or not value.lower().endswith(".md"):
        raise ValueError("Non-canonical or non-Markdown path")
    return value


def validate_manifest(manifest, authorization=None):
    required = {"manifest_version", "dataset_kind", "samples", "scopes", "model_content_authorization", "real_model_tests_authorized"}
    if not isinstance(manifest, dict) or set(manifest) != required or type(manifest["manifest_version"]) is not int or manifest["manifest_version"] != 1:
        raise ValueError("Unsupported manifest structure")
    if manifest["dataset_kind"] not in ("synthetic", "real_candidates") or manifest["real_model_tests_authorized"] is not False:
        raise ValueError("Phase 4A-2 is not authorized by this implementation")
    scopes = manifest["scopes"]
    if not isinstance(scopes, dict) or set(scopes) != {"source", "retrieval", "model_visible"}:
        raise ValueError("Three explicit scopes are required")
    if not isinstance(manifest["samples"], list) or not 1 <= len(manifest["samples"]) <= 1000:
        raise ValueError("Invalid sample count")
    ids = set(); paths = set(); groups = {}
    for row in manifest["samples"]:
        fields = {"sample_id", "path", "sha256", "stratum", "group", "partition", "phase3_familiar"}
        if not isinstance(row, dict) or set(row) != fields:
            raise ValueError("Invalid sample record")
        if any(not isinstance(row[key], str) or not row[key] for key in fields - {"phase3_familiar"}):
            raise ValueError("Sample identifiers must be nonempty strings")
        safe_relative(row["path"])
        if row["sample_id"] in ids or row["path"].casefold() in paths or not re.fullmatch(r"[0-9a-f]{64}", row["sha256"]):
            raise ValueError("Duplicate sample identity/path or invalid SHA-256")
        ids.add(row["sample_id"]); paths.add(row["path"].casefold())
        if row["partition"] not in ("development", "holdout") or type(row["phase3_familiar"]) is not bool:
            raise ValueError("Invalid partition")
        if row["phase3_familiar"] and row["partition"] != "development":
            raise ValueError("Familiar Phase 3 samples cannot be held out")
        groups.setdefault(row["group"], set()).add(row["partition"])
    if any(len(partitions) != 1 for partitions in groups.values()):
        raise ValueError("Leakage group crosses partitions")
    for names in scopes.values():
        if not isinstance(names, list) or any(not isinstance(x, str) or x not in ids for x in names) or len(set(names)) != len(names):
            raise ValueError("Scope contains unknown or duplicate sample IDs")
    if not set(scopes["model_visible"]) <= set(scopes["source"]) | set(scopes["retrieval"]):
        raise ValueError("Model scope is not within explicit local scopes")
    approval = authorization
    authorization = manifest["model_content_authorization"]
    if manifest["dataset_kind"] == "real_candidates":
        if authorization not in ("pending_phase4a2", "explicit_scope") or (scopes["model_visible"] and authorization != "explicit_scope"):
            raise ValueError("Real model-visible content requires separate Phase 4A-2 implementation/approval")
    elif authorization not in ("synthetic_only", "pending_phase4a2"):
        raise ValueError("Unsupported model content authorization")
    if authorization == "pending_phase4a2" and scopes["model_visible"]:
        raise ValueError("Pending authorization must have an empty model-visible scope")
    if manifest["dataset_kind"] == "real_candidates" and scopes["model_visible"]:
        validate_authorization(manifest, approval)
    return manifest


def validate_authorization(manifest, approval):
    fields = {"authorization_version", "purpose", "manifest_sha256", "vault_root", "model_visible", "allowed_stages"}
    if not isinstance(approval, dict) or set(approval) != fields:
        raise ValueError("Explicit local authorization is required")
    if type(approval["authorization_version"]) is not int or approval["authorization_version"] != 1 or approval["purpose"] != "advisory_only":
        raise ValueError("Invalid authorization purpose/version")
    if approval["manifest_sha256"] != digest(canonical(manifest)) or approval["model_visible"] != manifest["scopes"]["model_visible"]:
        raise ValueError("Authorization does not match the exact manifest/model scope")
    if not isinstance(approval["vault_root"], str) or not Path(approval["vault_root"]).is_absolute():
        raise ValueError("Authorization must pin an absolute Vault root")
    stages = approval["allowed_stages"]
    if not isinstance(stages, list) or not stages or len(set(stages)) != len(stages) or any(x not in ("classify", "relations") for x in stages):
        raise ValueError("Authorization stages are invalid")


def make_manifest(root, sources, candidates, visible):
    root = Path(root).resolve(); system = v.load_system(SYSTEM)
    names = list(dict.fromkeys(sources + candidates))
    if not names or any(x not in names for x in visible):
        raise ValueError("Explicit nonempty source/retrieval scopes and visible subset required")
    rows = []
    for i, name in enumerate(names, 1):
        safe_relative(name); path = root / name
        if links.protected_reason(root, path) or v.is_system_path(name, system):
            raise ValueError("Protected/system path is not an advisory document")
        raw = path.read_bytes()
        rows.append({"sample_id": f"N{i:04d}", "path": name, "sha256": digest(raw), "stratum": "operator_scoped",
                     "group": "work", "partition": "development", "phase3_familiar": False})
    ids = {x["path"]: x["sample_id"] for x in rows}
    result = {"manifest_version": 1, "dataset_kind": "real_candidates", "samples": rows,
              "scopes": {"source": [ids[x] for x in sources], "retrieval": [ids[x] for x in candidates], "model_visible": [ids[x] for x in visible]},
              "model_content_authorization": "explicit_scope", "real_model_tests_authorized": False}
    # Validate with a local candidate record; this function exports metadata only.
    candidate = {"authorization_version": 1, "purpose": "advisory_only", "manifest_sha256": digest(canonical(result)),
                 "vault_root": str(root), "model_visible": result["scopes"]["model_visible"], "allowed_stages": ["classify", "relations"]}
    validate_manifest(result, candidate)
    return result


@dataclass
class Note:
    sample_id: str
    path: str
    sha256: str
    id: str
    raw: bytes
    metadata: dict
    validation: dict
    title: str
    body: str
    first_body_line: int

    @property
    def eligibility(self):
        if self.validation["is_knowledge_entity"]:
            return "validated_v1_atomic"
        if self.metadata.get("type") in ("概念", "知识点", "方法") and self.validation["classification"] == "legacy":
            return "legacy_candidate"
        if maintenance.topic_policy.is_moc(self.raw, self.path, maintenance.v.load_system(SYSTEM)):
            return "navigation"
        return "reference_only"

    def spans(self, limit=80000):
        output = []; used = 0; partial = False
        for line_number, line in enumerate(self.body.splitlines(), self.first_body_line):
            if not line.strip():
                continue
            if used >= limit or len(output) >= 2000:
                partial = True; break
            fragment = line[:min(8192, limit - used)]
            if len(fragment) < len(line):partial = True
            output.append({"id": f"{self.id}:L{line_number}", "text": fragment, "start_line": line_number,
                           "end_line": line_number, "start_column": 1, "end_column": len(fragment) + 1})
            used += len(fragment)
        return output, "partial" if partial else "full"


@dataclass
class Catalog:
    root: Path
    system: object
    manifest: dict
    notes: dict
    exclusions: list
    index: object


def build_catalog(root, manifest, system=None, authorization=None):
    validate_manifest(manifest, authorization)
    root = Path(root).resolve()
    if authorization is not None and Path(authorization["vault_root"]).resolve() != root:
        raise ValueError("Authorization root mismatch")
    if not root.is_dir():
        raise ValueError("Vault root does not exist")
    system = system or v.load_system(SYSTEM)
    if manifest["dataset_kind"] == "synthetic" and (root.is_relative_to(system.vault_root) or system.vault_root.is_relative_to(root)):
        raise ValueError("The real Vault cannot be relabeled as a synthetic fixture")
    selected = set(manifest["scopes"]["source"]) | set(manifest["scopes"]["retrieval"])
    notes = {}; exclusions = []; index_files = {}
    for sample in manifest["samples"]:
        sid = sample["sample_id"]; name = sample["path"]
        if sid not in selected:
            exclusions.append({"sample_id": sid, "path": name, "reason": "not_in_local_scope"}); continue
        path = root / name
        reason = links.protected_reason(root, path)
        if not reason and v.is_system_path(name, system):reason = "system_file"
        if reason:
            exclusions.append({"sample_id": sid, "path": name, "reason": reason}); continue
        raw = path.read_bytes()
        if digest(raw) != sample["sha256"]:
            raise ValueError(f"Pinned document changed: {sid}")
        metadata = v.parse_frontmatter(raw)
        lines = raw.decode("utf-8-sig").splitlines(keepends=True)
        start = 0
        if metadata is not None:
            for i, line in enumerate(lines[1:], 1):
                if re.fullmatch(r"---[ \t]*(?:\r?\n)?", line):start = i + 1; break
        metadata = metadata or {}
        validation = v.validate_note(raw, name, system)
        identifier = "d_" + digest((name + "\0" + sample["sha256"]).encode())[:24]
        note = Note(sid, name, sample["sha256"], identifier, raw, metadata, validation,
                    validation["display_title"], "".join(lines[start:]), start + 1)
        notes[sid] = note
        # Reuse the existing parser's heading/block/alias interpretation.
        index_files[name] = links._record(raw)
    return Catalog(root, system, manifest, notes, exclusions,
                   links.Index(root, index_files, [{"path": x["path"], "reason": x["reason"]} for x in exclusions], []))


def terms(text):
    words = re.findall(r"[a-z0-9_^]+", text.casefold())
    for run in re.findall(r"[\u3400-\u9fff]+", text):
        words.extend(run[i:i + 2] for i in range(max(1, len(run) - 1)))
    return Counter(words)


def retrieve(catalog, query, k=8):
    if not isinstance(query, str) or not query.strip() or len(query) > 256 or type(k) is not int or not 1 <= k <= 20:
        raise ValueError("A bounded literal query and 1..20 candidates are required")
    records = [catalog.notes[sid] for sid in catalog.manifest["scopes"]["retrieval"] if sid in catalog.notes]
    vectors = {}
    aliases = {}
    for note in records:
        names = note.metadata.get("aliases", [])
        names = names if isinstance(names, list) else []
        aliases[note.id] = [x for x in names if isinstance(x, str)]
        vectors[note.id] = terms(note.title + " " + " ".join(aliases[note.id]) + " " + note.body)
    df = Counter(word for vector in vectors.values() for word in vector)
    qterms = terms(query); matches = []
    for note in records:
        vector = vectors[note.id]
        score = sum((1 + math.log(vector[word])) * math.log(1 + len(records) / (1 + df[word])) for word in qterms if vector[word])
        exact = query.casefold() in {note.title.casefold(), PurePosixPath(note.path).stem.casefold(), *(x.casefold() for x in aliases[note.id])}
        if exact:score += 5
        if score <= 0:continue
        matches.append({"id": note.id, "sample_id": note.sample_id, "path": note.path, "title": note.title,
                        "sha256": note.sha256, "score": round(score, 6), "basis": "exact_name_or_alias_and_lexical_terms" if exact else "lexical_terms_only",
                        "eligibility": note.eligibility, "canonical_type": note.validation["selected_profile"] if note.validation["is_knowledge_entity"] else None})
    matches.sort(key=lambda x: (-x["score"], x["path"]))
    count = len(matches)
    return {"query": query, "state": "not_found" if not count else "unique" if count == 1 else "multiple",
            "selected_id": matches[0]["id"] if count == 1 else None, "candidates": matches[:k],
            "matching_count": count, "truncated_candidates": count > k,
            "scope": list(catalog.manifest["scopes"]["retrieval"]),
            "claim": "Lexical candidates in the explicit scope; not proof of a mathematical relation or global absence"}
