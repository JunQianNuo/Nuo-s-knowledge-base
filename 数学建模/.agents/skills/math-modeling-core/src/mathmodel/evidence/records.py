from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any, Mapping
import re

from mathmodel.contracts import EvidenceStatus


VerificationStatus = EvidenceStatus


def normalize_doi(value: str | None) -> str | None:
    if value is None:
        return None
    normalized = value.strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if normalized.startswith(prefix):
            normalized = normalized[len(prefix) :]
            break
    return normalized or None


def normalize_title(value: str) -> str:
    return re.sub(r"[^\w]+", " ", value.casefold(), flags=re.UNICODE).strip()


@dataclass(frozen=True, slots=True)
class EvidenceRecord:
    title: str
    authors: tuple[str, ...] = ()
    year: int | None = None
    venue: str | None = None
    doi: str | None = None
    stable_id: str | None = None
    stable_identifiers: tuple[str, ...] = ()
    sources: tuple[str, ...] = ()
    model: str | None = None
    applicability: tuple[str, ...] = ()
    parameter_basis: tuple[str, ...] = ()
    validation_methods: tuple[str, ...] = ()
    limitations: tuple[str, ...] = ()
    accessed_on: date | None = None
    metadata_status: VerificationStatus = VerificationStatus.UNVERIFIED
    conflicts: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("evidence title must not be empty")
        object.__setattr__(self, "doi", normalize_doi(self.doi))
        for name in (
            "authors",
            "sources",
            "stable_identifiers",
            "applicability",
            "parameter_basis",
            "validation_methods",
            "limitations",
            "conflicts",
        ):
            object.__setattr__(self, name, tuple(getattr(self, name)))

    @property
    def record_key(self) -> str:
        if self.doi:
            return f"doi:{self.doi}"
        return f"title:{normalize_title(self.title)}"


@dataclass(frozen=True, slots=True)
class EvidenceClaim:
    claim_id: str
    claim_type: str
    text: str
    record_key: str
    locator: str | None
    applicability: tuple[str, ...]
    status: VerificationStatus
    contradiction: str | None = None

    def __post_init__(self) -> None:
        for name in ("claim_id", "claim_type", "text", "record_key"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must not be empty")
        object.__setattr__(self, "applicability", tuple(self.applicability))


@dataclass(frozen=True, slots=True)
class SearchRequest:
    phase: str
    query: str
    provider: str
    page: int = 1
    parameters: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.phase not in {"E0", "E1"}:
            raise ValueError("phase must be E0 or E1")
        normalized_query = " ".join(self.query.split())
        if not normalized_query:
            raise ValueError("query must not be empty")
        if not self.provider.strip():
            raise ValueError("provider must not be empty")
        if self.page <= 0:
            raise ValueError("page must be positive")
        object.__setattr__(self, "query", normalized_query)
        object.__setattr__(self, "parameters", dict(self.parameters))

    def to_dict(self) -> dict[str, Any]:
        return {
            "phase": self.phase,
            "query": self.query,
            "provider": self.provider,
            "page": self.page,
            "parameters": dict(self.parameters),
        }

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> SearchRequest:
        return cls(
            phase=str(value["phase"]),
            query=str(value["query"]),
            provider=str(value["provider"]),
            page=int(value["page"]),
            parameters=dict(value.get("parameters", {})),
        )


@dataclass(frozen=True, slots=True)
class ProviderResponse:
    records: tuple[Mapping[str, Any], ...]
    status_code: int | None = 200
    detail: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "records", tuple(dict(record) for record in self.records)
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "records": [dict(record) for record in self.records],
            "status_code": self.status_code,
            "detail": self.detail,
        }

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> ProviderResponse:
        return cls(
            records=tuple(dict(item) for item in value.get("records", [])),
            status_code=value.get("status_code"),
            detail=value.get("detail"),
        )


@dataclass(frozen=True, slots=True)
class NetworkEvent:
    provider: str
    request: SearchRequest
    status: str
    detail: str | None = None


@dataclass(frozen=True, slots=True)
class EvidenceBundle:
    requests: tuple[SearchRequest, ...]
    records: tuple[EvidenceRecord, ...]
    claims: tuple[EvidenceClaim, ...]
    snapshots: tuple[Any, ...]
    network_events: tuple[NetworkEvent, ...]
    evidence_revision: str

    def __post_init__(self) -> None:
        for name in (
            "requests",
            "records",
            "claims",
            "snapshots",
            "network_events",
        ):
            object.__setattr__(self, name, tuple(getattr(self, name)))
