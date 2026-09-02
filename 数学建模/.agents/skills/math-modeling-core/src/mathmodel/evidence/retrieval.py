from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import date
import hashlib
import json
from typing import Any, Mapping

from .records import (
    EvidenceBundle,
    EvidenceClaim,
    EvidenceRecord,
    NetworkEvent,
    ProviderResponse,
    SearchRequest,
    VerificationStatus,
    normalize_doi,
    normalize_title,
)


class BudgetExceeded(RuntimeError):
    pass


@dataclass(frozen=True, slots=True)
class BudgetEvent:
    request: SearchRequest
    counted: bool
    reason: str


@dataclass(slots=True)
class SearchBudget:
    initial_limit: int = 5
    hard_cap: int = 8
    approved_limit: int | None = None
    used: int = 0
    events: list[BudgetEvent] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.initial_limit <= 0 or self.hard_cap < self.initial_limit:
            raise ValueError("invalid search budget limits")
        if self.approved_limit is not None and self.approved_limit < self.hard_cap:
            raise ValueError("approved limit cannot be below the hard cap")

    @property
    def effective_cap(self) -> int:
        return self.approved_limit or self.hard_cap

    def consume(
        self,
        request: SearchRequest,
        *,
        retry: bool = False,
        metadata_fetch: bool = False,
        unresolved_critical: bool = False,
    ) -> None:
        if retry or metadata_fetch:
            reason = "retry" if retry else "metadata_fetch"
            self.events.append(BudgetEvent(request, False, reason))
            return
        if self.used >= self.effective_cap:
            raise BudgetExceeded(f"search hard cap {self.effective_cap} exceeded")
        if self.used >= self.initial_limit and not unresolved_critical:
            raise BudgetExceeded(
                f"initial search budget {self.initial_limit} exhausted; "
                "unresolved critical claim required for automatic expansion"
            )
        self.used += 1
        self.events.append(BudgetEvent(request, True, "search_request"))


@dataclass(frozen=True, slots=True)
class EvidenceSnapshot:
    provider: str
    provider_version: str
    request: SearchRequest
    response: ProviderResponse
    accessed_at: str
    snapshot_hash: str

    @classmethod
    def create(
        cls,
        *,
        provider: str,
        provider_version: str,
        request: SearchRequest,
        response: ProviderResponse,
        accessed_at: str,
    ) -> EvidenceSnapshot:
        payload = _snapshot_payload(
            provider, provider_version, request, response, accessed_at
        )
        return cls(
            provider=provider,
            provider_version=provider_version,
            request=request,
            response=response,
            accessed_at=accessed_at,
            snapshot_hash=_sha256(payload),
        )

    def to_json(self) -> str:
        value = _snapshot_payload(
            self.provider,
            self.provider_version,
            self.request,
            self.response,
            self.accessed_at,
        )
        value["snapshot_hash"] = self.snapshot_hash
        return _canonical_json(value)

    @classmethod
    def from_json(cls, value: str) -> EvidenceSnapshot:
        decoded = json.loads(value)
        snapshot_hash = str(decoded.pop("snapshot_hash"))
        expected = _sha256(decoded)
        if snapshot_hash != expected:
            raise ValueError("snapshot hash mismatch")
        return cls(
            provider=str(decoded["provider"]),
            provider_version=str(decoded["provider_version"]),
            request=SearchRequest.from_dict(decoded["request"]),
            response=ProviderResponse.from_dict(decoded["response"]),
            accessed_at=str(decoded["accessed_at"]),
            snapshot_hash=snapshot_hash,
        )


def retrieve_evidence(
    requests: tuple[SearchRequest, ...] | list[SearchRequest],
    providers: Mapping[str, Any],
    budget: SearchBudget,
    *,
    accessed_on: date,
    unresolved_critical: bool = False,
) -> EvidenceBundle:
    accepted_requests: list[SearchRequest] = []
    records: list[EvidenceRecord] = []
    claims: list[EvidenceClaim] = []
    record_indexes: dict[str, int] = {}
    snapshots: list[EvidenceSnapshot] = []
    events: list[NetworkEvent] = []

    for search_request in requests:
        budget.consume(search_request, unresolved_critical=unresolved_critical)
        accepted_requests.append(search_request)
        provider = providers.get(search_request.provider)
        if provider is None:
            events.append(
                NetworkEvent(
                    search_request.provider,
                    search_request,
                    "offline",
                    "provider_not_configured",
                )
            )
            continue
        try:
            response = provider.search(search_request)
        except TimeoutError as exc:
            events.append(
                NetworkEvent(provider.name, search_request, "timeout", str(exc))
            )
            continue
        except (ConnectionError, OSError) as exc:
            events.append(
                NetworkEvent(provider.name, search_request, "offline", str(exc))
            )
            continue

        event_status = "empty" if not response.records else "ok"
        events.append(
            NetworkEvent(provider.name, search_request, event_status, response.detail)
        )
        accessed_at = f"{accessed_on.isoformat()}T00:00:00Z"
        snapshots.append(
            EvidenceSnapshot.create(
                provider=provider.name,
                provider_version=provider.version,
                request=search_request,
                response=response,
                accessed_at=accessed_at,
            )
        )
        for raw in response.records:
            incoming = _record_from_raw(raw, provider.name, accessed_on)
            doi_key = f"doi:{incoming.doi}" if incoming.doi else None
            title_key = f"title:{normalize_title(incoming.title)}"
            existing_index = record_indexes.get(doi_key) if doi_key else None
            title_index = record_indexes.get(title_key)
            if existing_index is None and title_index is not None:
                title_match = records[title_index]
                if incoming.doi is None or title_match.doi is None:
                    existing_index = title_index
            if existing_index is None:
                existing_index = len(records)
                records.append(incoming)
            else:
                records[existing_index] = _merge_records(records[existing_index], incoming)
            current = records[existing_index]
            record_indexes.setdefault(
                f"title:{normalize_title(current.title)}", existing_index
            )
            if current.doi:
                record_indexes[f"doi:{current.doi}"] = existing_index
            for raw_claim in raw.get("claims", ()):
                claims.append(_claim_from_raw(raw_claim, current.record_key))

    revision_payload = _revision_payload(snapshots, records, claims)
    return EvidenceBundle(
        requests=tuple(accepted_requests),
        records=tuple(records),
        claims=tuple(claims),
        snapshots=tuple(snapshots),
        network_events=tuple(events),
        evidence_revision=_sha256(revision_payload),
    )


def _record_from_raw(
    raw: Mapping[str, Any], provider: str, accessed_on: date
) -> EvidenceRecord:
    doi = normalize_doi(_optional_str(raw.get("doi")))
    stable_id = _optional_str(raw.get("stable_id"))
    complete = bool(
        raw.get("title") and raw.get("authors") and raw.get("year") and (doi or stable_id)
    )
    return EvidenceRecord(
        title=str(raw.get("title", "")).strip(),
        authors=tuple(str(item) for item in raw.get("authors", ())),
        year=int(raw["year"]) if raw.get("year") is not None else None,
        venue=_optional_str(raw.get("venue")),
        doi=doi,
        stable_id=stable_id,
        stable_identifiers=(f"{provider}:{stable_id}",) if stable_id else (),
        sources=(provider,),
        model=_optional_str(raw.get("model")),
        applicability=tuple(str(item) for item in raw.get("applicability", ())),
        parameter_basis=tuple(str(item) for item in raw.get("parameter_basis", ())),
        validation_methods=tuple(
            str(item) for item in raw.get("validation_methods", ())
        ),
        limitations=tuple(str(item) for item in raw.get("limitations", ())),
        accessed_on=accessed_on,
        metadata_status=(
            VerificationStatus.PARTIAL if complete else VerificationStatus.UNVERIFIED
        ),
    )


def _merge_records(first: EvidenceRecord, second: EvidenceRecord) -> EvidenceRecord:
    conflicts = list(first.conflicts)
    if normalize_title(first.title) != normalize_title(second.title):
        conflicts.append(f"conflicting_title:{second.title}")
    for name in ("doi", "year", "venue"):
        left, right = getattr(first, name), getattr(second, name)
        if left is not None and right is not None and left != right:
            conflicts.append(f"conflicting_{name}:{right}")
    sources = _unique((*first.sources, *second.sources))
    metadata_status = first.metadata_status
    if len(sources) >= 2 and not conflicts:
        metadata_status = VerificationStatus.VERIFIED
    elif first.metadata_status is not VerificationStatus.UNVERIFIED or second.metadata_status is not VerificationStatus.UNVERIFIED:
        metadata_status = VerificationStatus.PARTIAL
    return replace(
        first,
        authors=_unique((*first.authors, *second.authors)),
        sources=sources,
        doi=first.doi or second.doi,
        stable_id=first.stable_id or second.stable_id,
        stable_identifiers=_unique(
            (*first.stable_identifiers, *second.stable_identifiers)
        ),
        applicability=_unique((*first.applicability, *second.applicability)),
        parameter_basis=_unique((*first.parameter_basis, *second.parameter_basis)),
        validation_methods=_unique(
            (*first.validation_methods, *second.validation_methods)
        ),
        limitations=_unique((*first.limitations, *second.limitations)),
        metadata_status=metadata_status,
        conflicts=_unique(conflicts),
    )


def _claim_from_raw(raw: Mapping[str, Any], record_key: str) -> EvidenceClaim:
    return EvidenceClaim(
        claim_id=str(raw["claim_id"]),
        claim_type=str(raw["claim_type"]),
        text=str(raw["text"]),
        record_key=record_key,
        locator=_optional_str(raw.get("locator")),
        applicability=tuple(str(item) for item in raw.get("applicability", ())),
        status=VerificationStatus(
            str(raw.get("status", VerificationStatus.UNVERIFIED.value))
        ),
        contradiction=_optional_str(raw.get("contradiction")),
    )


def _revision_payload(
    snapshots: list[EvidenceSnapshot],
    records: list[EvidenceRecord],
    claims: list[EvidenceClaim],
) -> dict[str, Any]:
    normalized_snapshots = []
    for snapshot in snapshots:
        identities = []
        for raw in snapshot.response.records:
            doi = normalize_doi(_optional_str(raw.get("doi")))
            identity = (
                f"doi:{doi}"
                if doi
                else f"title:{normalize_title(str(raw.get('title', '')))}"
            )
            identities.append(identity)
        normalized_snapshots.append(
            {
                "provider": snapshot.provider,
                "provider_version": snapshot.provider_version,
                "request": snapshot.request.to_dict(),
                "accessed_at": snapshot.accessed_at,
                "record_identities": sorted(identities),
            }
        )
    normalized_snapshots.sort(
        key=lambda item: _canonical_json(item)
    )
    return {
        "snapshots": normalized_snapshots,
        "record_keys": sorted(record.record_key for record in records),
        "claims": sorted(
            (claim.claim_id, claim.record_key, claim.status.value) for claim in claims
        ),
    }


def _unique(values: tuple[str, ...] | list[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(values))


def _optional_str(value: Any) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip()
    return normalized or None


def _snapshot_payload(
    provider: str,
    provider_version: str,
    request: SearchRequest,
    response: ProviderResponse,
    accessed_at: str,
) -> dict[str, Any]:
    return {
        "provider": provider,
        "provider_version": provider_version,
        "request": request.to_dict(),
        "response": response.to_dict(),
        "accessed_at": accessed_at,
    }


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()
