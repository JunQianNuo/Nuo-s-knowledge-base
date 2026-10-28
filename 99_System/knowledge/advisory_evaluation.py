"""Mechanical benchmark checks and scorer functions; real-model evaluation is disabled."""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

from collections import Counter
import re

import advisory_retrieval as retrieval


def audit_manifest(manifest):
    errors = []
    try:retrieval.validate_manifest(manifest)
    except (ValueError, TypeError, KeyError) as error:
        return {"sample_count": 0, "partition_counts": {}, "stratum_counts": {}, "groups": {},
                "errors": [str(error)], "gold_status": "not_created", "semantic_evaluated": False}
    samples = manifest.get("samples", [])
    return {"sample_count": len(samples), "partition_counts": dict(Counter(x.get("partition") for x in samples)),
            "stratum_counts": dict(Counter(x.get("stratum") for x in samples)),
            "groups": {group: [x["sample_id"] for x in samples if x.get("group") == group] for group in sorted({x.get("group", "") for x in samples})},
            "errors": errors, "gold_status": "not_created", "semantic_evaluated": False}


def content_leakage(documents):
    normalized = {}; shingles = {}
    for doc in documents:
        # Ignore formatting-only headings/fences and existing links' markup.
        body = "\n".join(line for line in doc["body"].splitlines() if line.strip() and not re.match(r"^\s*(?:#|```|~~~)", line))
        text = re.sub(r"\s+", "", body).casefold()
        normalized[doc["sample_id"]] = text
        shingles[doc["sample_id"]] = {text[i:i + 12] for i in range(max(0, len(text) - 11))}
    pairs = []
    for i, first in enumerate(documents):
        for second in documents[i + 1:]:
            a = normalized[first["sample_id"]]; b = normalized[second["sample_id"]]
            sa = shingles[first["sample_id"]]; sb = shingles[second["sample_id"]]
            exact = bool(a) and a == b
            containment = len(sa & sb) / min(len(sa), len(sb)) if sa and sb else 0
            if exact or (min(len(sa), len(sb)) >= 80 and containment >= 0.65):
                pairs.append({"a": first["sample_id"], "b": second["sample_id"], "exact": exact,
                              "containment": round(containment, 6), "cross_partition": first["partition"] != second["partition"]})
    return {"pairs": pairs, "cross_partition": [x for x in pairs if x["cross_partition"]],
            "method": "normalized exact + 12-character shingle containment >= .65 with >=80 shingles; heuristic, not semantic deduplication"}


def classification_metrics(gold, predictions):
    if len(gold) != len(predictions) or not gold:raise ValueError("Nonempty aligned labels required")
    labels = sorted(set(gold)); confusion = Counter(zip(gold, predictions)); scores = []
    for label in labels:
        tp = confusion[label, label]
        fp = sum(n for (g, p), n in confusion.items() if p == label and g != label)
        fn = sum(n for (g, p), n in confusion.items() if g == label and p != label)
        scores.append(2 * tp / (2 * tp + fp + fn) if 2 * tp + fp + fn else 0)
    return {"total": len(gold), "correct": sum(g == p for g, p in zip(gold, predictions)),
            "abstentions": sum(x in (None, "undetermined") for x in predictions), "macro_f1": sum(scores) / len(scores),
            "confusion": [{"gold": g, "predicted": p, "count": n} for (g, p), n in confusion.items()],
            "claim": "Scoring arithmetic only; not a measured AI capability"}


def retrieval_metrics(gold, ranked, k=8):
    expected = sum(len(values) for values in gold.values())
    hits = sum(len(set(ranked.get(source, [])[:k]) & set(values)) for source, values in gold.items())
    reciprocal = []
    for source, values in gold.items():
        if values:reciprocal.append(next((1 / (i + 1) for i, x in enumerate(ranked.get(source, [])[:k]) if x in values), 0))
    return {"known_targets": expected, "hits": hits, "known_target_recall": hits / expected if expected else None,
            "mrr": sum(reciprocal) / len(reciprocal) if reciprocal else None,
            "claim": "Finite independently labeled target set only; not whole-Vault recall"}


def relation_metrics(gold, predictions):
    gold = set(gold); predictions = set(predictions); correct = len(gold & predictions)
    return {"gold_count": len(gold), "proposed_count": len(predictions), "correct": correct,
            "precision": correct / len(predictions) if predictions else None,
            "closed_set_recall": correct / len(gold) if gold else None}


def evaluate(manifest, annotations, run=None):
    report = audit_manifest(manifest)
    if report["errors"]:raise ValueError("; ".join(report["errors"]))
    samples = {x["sample_id"]: x for x in manifest["samples"]}; seen = set()
    from advisory import validate_schema
    for row in annotations:
        validate_schema("annotation", row)
        sid = row.get("sample_id")
        if sid not in samples or sid in seen or row.get("sha256") != samples[sid]["sha256"]:
            raise ValueError("Unknown, duplicate or stale annotation")
        seen.add(sid)
    report.update({"semantic_evaluated": False, "metrics": None, "status": "phase4a2_not_authorized",
                   "pending_annotations": sum(row.get("gold") is None for row in annotations),
                   "missing_annotations": len(samples) - len(seen),
                   "run_metadata_accepted_as_proof": False,
                   "reason": "Phase 4A-1 permits only mechanical/scorer tests; imported run labels do not authorize real semantic evaluation"})
    return report
