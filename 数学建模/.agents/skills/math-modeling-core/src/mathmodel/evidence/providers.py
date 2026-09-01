from __future__ import annotations

import json
from typing import Protocol
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .records import ProviderResponse, SearchRequest


class EvidenceProvider(Protocol):
    name: str
    version: str

    def search(self, request: SearchRequest) -> ProviderResponse: ...


class OpenAlexProvider:
    name = "openalex"
    version = "v1"

    def __init__(self, *, timeout: float = 10.0, mailto: str | None = None) -> None:
        self.timeout = timeout
        self.mailto = mailto

    def search(self, request: SearchRequest) -> ProviderResponse:
        parameters = {
            "search": request.query,
            "page": request.page,
            "per-page": int(request.parameters.get("per_page", 25)),
        }
        if self.mailto:
            parameters["mailto"] = self.mailto
        payload = _get_json(
            "https://api.openalex.org/works?" + urlencode(parameters), self.timeout
        )
        records = tuple(_openalex_record(item) for item in payload.get("results", []))
        return ProviderResponse(records=records)


class SemanticScholarProvider:
    name = "semantic-scholar"
    version = "graph-v1"

    def __init__(self, *, timeout: float = 10.0, api_key: str | None = None) -> None:
        self.timeout = timeout
        self.api_key = api_key

    def search(self, request: SearchRequest) -> ProviderResponse:
        offset = (request.page - 1) * int(request.parameters.get("limit", 20))
        parameters = {
            "query": request.query,
            "offset": offset,
            "limit": int(request.parameters.get("limit", 20)),
            "fields": "paperId,title,authors,year,venue,externalIds,abstract",
        }
        headers = {"User-Agent": "math-modeling-core/1.0"}
        if self.api_key:
            headers["x-api-key"] = self.api_key
        payload = _get_json(
            "https://api.semanticscholar.org/graph/v1/paper/search?"
            + urlencode(parameters),
            self.timeout,
            headers,
        )
        records = tuple(_semantic_record(item) for item in payload.get("data", []))
        return ProviderResponse(records=records)


def _get_json(
    url: str, timeout: float, headers: dict[str, str] | None = None
) -> dict[str, object]:
    request = Request(url, headers=headers or {"User-Agent": "math-modeling-core/1.0"})
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def _openalex_record(item: dict[str, object]) -> dict[str, object]:
    authorships = item.get("authorships") or []
    authors = [
        str(authorship.get("author", {}).get("display_name", ""))
        for authorship in authorships
        if isinstance(authorship, dict)
    ]
    primary = item.get("primary_location") or {}
    source = primary.get("source") or {} if isinstance(primary, dict) else {}
    return {
        "title": item.get("display_name") or item.get("title") or "",
        "authors": authors,
        "year": item.get("publication_year"),
        "venue": source.get("display_name") if isinstance(source, dict) else None,
        "doi": item.get("doi"),
        "stable_id": item.get("id"),
    }


def _semantic_record(item: dict[str, object]) -> dict[str, object]:
    external = item.get("externalIds") or {}
    authors = item.get("authors") or []
    return {
        "title": item.get("title") or "",
        "authors": [
            str(author.get("name", ""))
            for author in authors
            if isinstance(author, dict)
        ],
        "year": item.get("year"),
        "venue": item.get("venue"),
        "doi": external.get("DOI") if isinstance(external, dict) else None,
        "stable_id": item.get("paperId"),
    }
