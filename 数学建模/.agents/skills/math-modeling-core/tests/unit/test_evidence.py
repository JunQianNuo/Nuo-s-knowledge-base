from __future__ import annotations

from dataclasses import replace
from datetime import date

import pytest

from mathmodel.evidence import (
    BudgetExceeded,
    EvidenceClaim,
    EvidenceRecord,
    EvidenceSnapshot,
    ProviderResponse,
    SearchBudget,
    SearchRequest,
    VerificationStatus,
    retrieve_evidence,
)


class FakeProvider:
    name = "fake"
    version = "test-1"

    def __init__(self, responses: dict[int, ProviderResponse | Exception]) -> None:
        self.responses = responses

    def search(self, request: SearchRequest) -> ProviderResponse:
        response = self.responses[request.page]
        if isinstance(response, Exception):
            raise response
        return response


def request(page: int = 1, provider: str = "fake") -> SearchRequest:
    return SearchRequest(
        phase="E0",
        query="traffic flow mechanism",
        provider=provider,
        page=page,
    )


def raw_record(
    title: str,
    *,
    doi: str | None = None,
    stable_id: str | None = None,
    year: int = 2024,
) -> dict[str, object]:
    return {
        "title": title,
        "authors": ["A. Author"],
        "year": year,
        "venue": "Journal",
        "doi": doi,
        "stable_id": stable_id,
        "model": "fundamental diagram",
        "applicability": ["uninterrupted roads"],
        "parameter_basis": ["field observations"],
        "validation_methods": ["holdout"],
        "limitations": ["not intersections"],
    }


def test_search_budget_counts_provider_pages_but_not_retries_or_metadata_fetches() -> None:
    budget = SearchBudget()

    budget.consume(request(page=1))
    budget.consume(request(page=2))
    budget.consume(request(page=1, provider="other"))
    budget.consume(request(page=1), retry=True)
    budget.consume(request(page=1), metadata_fetch=True)

    assert budget.used == 3
    assert [event.counted for event in budget.events] == [True, True, True, False, False]


def test_search_budget_initial_five_and_hard_cap_eight() -> None:
    budget = SearchBudget()
    for page in range(1, 6):
        budget.consume(request(page=page))

    with pytest.raises(BudgetExceeded, match="initial search budget"):
        budget.consume(request(page=6))

    for page in range(6, 9):
        budget.consume(request(page=page), unresolved_critical=True)

    assert budget.used == 8
    with pytest.raises(BudgetExceeded, match="hard cap"):
        budget.consume(request(page=9), unresolved_critical=True)


def test_retrieval_deduplicates_by_doi_then_normalized_title() -> None:
    provider = FakeProvider(
        {
            1: ProviderResponse(
                records=(
                    raw_record("Traffic-Flow Model", doi="10.1000/ABC", stable_id="x"),
                    raw_record("Other Model", stable_id="o1"),
                )
            ),
            2: ProviderResponse(
                records=(
                    raw_record("Renamed record", doi="https://doi.org/10.1000/abc", stable_id="y"),
                    raw_record(" other   model ", stable_id="o2"),
                )
            ),
        }
    )

    bundle = retrieve_evidence(
        (request(1), request(2)),
        {"fake": provider},
        SearchBudget(),
        accessed_on=date(2026, 9, 1),
    )

    assert len(bundle.records) == 2
    by_title = {record.title: record for record in bundle.records}
    assert by_title["Traffic-Flow Model"].sources == ("fake",)
    assert "conflicting_title:Renamed record" in by_title["Traffic-Flow Model"].conflicts
    assert "fake:o1" in by_title["Other Model"].stable_identifiers
    assert "fake:o2" in by_title["Other Model"].stable_identifiers
    assert not any("stable_id" in conflict for conflict in by_title["Other Model"].conflicts)


def test_same_title_with_two_different_dois_remains_two_records() -> None:
    provider = FakeProvider(
        {
            1: ProviderResponse(
                records=(
                    raw_record("Shared Title", doi="10.1000/one", stable_id="1"),
                    raw_record("shared-title", doi="10.1000/two", stable_id="2"),
                )
            )
        }
    )

    bundle = retrieve_evidence(
        (request(),),
        {"fake": provider},
        SearchBudget(),
        accessed_on=date(2026, 9, 1),
    )

    assert {record.doi for record in bundle.records} == {"10.1000/one", "10.1000/two"}


def test_verified_record_does_not_promote_unverified_claim() -> None:
    record = EvidenceRecord(
        title="Verified metadata",
        authors=("A. Author",),
        year=2024,
        venue="Journal",
        doi="10.1000/test",
        stable_id="openalex:1",
        sources=("openalex", "semantic-scholar"),
        accessed_on=date(2026, 9, 1),
        metadata_status=VerificationStatus.VERIFIED,
    )
    claim = EvidenceClaim(
        claim_id="c1",
        claim_type="mechanism",
        text="X causes Y",
        record_key=record.record_key,
        locator=None,
        applicability=(),
        status=VerificationStatus.UNVERIFIED,
    )

    assert record.metadata_status is VerificationStatus.VERIFIED
    assert claim.status is VerificationStatus.UNVERIFIED


def test_retrieval_extracts_claims_without_promoting_them_from_record_metadata() -> None:
    raw = raw_record("Claimed Model", doi="10.1000/claim", stable_id="c")
    raw["claims"] = [
        {
            "claim_id": "claim-1",
            "claim_type": "mechanism",
            "text": "X is associated with Y",
            "locator": None,
            "applicability": ["laboratory scale"],
            "status": "UNVERIFIED",
        }
    ]
    provider = FakeProvider({1: ProviderResponse(records=(raw,))})

    bundle = retrieve_evidence(
        (request(),), {"fake": provider}, SearchBudget(), accessed_on=date(2026, 9, 1)
    )

    assert len(bundle.claims) == 1
    assert bundle.claims[0].record_key == bundle.records[0].record_key
    assert bundle.claims[0].status is VerificationStatus.UNVERIFIED


def test_snapshot_hash_is_canonical_and_replay_preserves_response_order() -> None:
    response = ProviderResponse(
        records=(raw_record("First", stable_id="1"), raw_record("Second", stable_id="2"))
    )
    snapshot = EvidenceSnapshot.create(
        provider="fake",
        provider_version="test-1",
        request=request(),
        response=response,
        accessed_at="2026-09-01T00:00:00Z",
    )
    recreated = EvidenceSnapshot.from_json(snapshot.to_json())

    assert recreated.snapshot_hash == snapshot.snapshot_hash
    assert [item["title"] for item in recreated.response.records] == ["First", "Second"]
    changed = replace(snapshot, snapshot_hash="bad")
    with pytest.raises(ValueError, match="snapshot hash mismatch"):
        EvidenceSnapshot.from_json(changed.to_json())


def test_evidence_revision_is_stable_when_provider_order_changes() -> None:
    first = ProviderResponse(
        records=(raw_record("First", stable_id="1"), raw_record("Second", stable_id="2"))
    )
    reversed_response = ProviderResponse(records=tuple(reversed(first.records)))

    first_bundle = retrieve_evidence(
        (request(),),
        {"fake": FakeProvider({1: first})},
        SearchBudget(),
        accessed_on=date(2026, 9, 1),
    )
    second_bundle = retrieve_evidence(
        (request(),),
        {"fake": FakeProvider({1: reversed_response})},
        SearchBudget(),
        accessed_on=date(2026, 9, 1),
    )

    assert first_bundle.evidence_revision == second_bundle.evidence_revision


@pytest.mark.parametrize(
    ("response", "expected_status"),
    [
        (ConnectionError("offline"), "offline"),
        (TimeoutError("slow"), "timeout"),
        (ProviderResponse(records=()), "empty"),
    ],
)
def test_retrieval_records_offline_timeout_and_empty_provider_events(
    response: ProviderResponse | Exception, expected_status: str
) -> None:
    bundle = retrieve_evidence(
        (request(),),
        {"fake": FakeProvider({1: response})},
        SearchBudget(),
        accessed_on=date(2026, 9, 1),
    )

    assert bundle.records == ()
    assert bundle.network_events[0].status == expected_status
