# Literature evidence pipeline

Literature participates twice: E0 helps interpret the problem and variables; E1 supports method, parameter, and validation decisions. Retrieval informs hard gates but never bypasses them.

## E0 — understand the domain

Run after first reading and before formal decomposition/variable freeze. Query background, mechanism, current rules, variable definitions, units, measurement, and typical scales. Extract claims into domain context, variables, mechanisms, rules, and conflicts.

Use source priority by claim:

- background: systematic/review literature, authoritative reports, textbooks;
- mechanism: original research, systematic review, standard, or authoritative textbook;
- mutable business/regulatory rule: current official rule, standard, regulator, or industry authority first; papers explain but do not establish current validity;
- variable/measurement: standard, data dictionary, method paper, or domain research.

## E1 — methods and validation

Run after `ProblemSpec` and before final candidate selection. Build Chinese and English queries from each subproblem, mechanism, and variable dictionary. Retrieve similar problems, actual equations/models, algorithms, parameter bases, validation methods, benchmarks, applicability, quantitative results, and known failure conditions.

Do not recommend from title or abstract keywords alone. Record what the paper actually solves and whether its scale, boundary conditions, data regime, objective, and constraints match this problem.

## Search budget

A `search_request` is one normalized query sent to one provider for one result page. Another provider or page counts again. Same-parameter retry, known-ID metadata fetch, and opening an already-hit authority do not count, but remain in the network log.

- initial limit: 5 requests shared by all subproblems;
- automatic expansion: only for unresolved critical ambiguity, up to hard cap 8;
- beyond 8: require explicit user approval of a new cap;
- local files cost zero external requests.

Stop early only when critical claims are covered, no high-severity conflict remains, and the evidence set is sufficiently relevant and verifiable. A typical 5–8 papers is a stopping signal, not a quota or rank feature.

## Records and claims

`EvidenceRecord` stores title, authors, year, venue, DOI/stable ID, sources, actual model, applicability, parameter basis, validation, limitations, access date, metadata status, and conflicts. Deduplicate by normalized DOI first and normalized title second; preserve source disagreements.

`EvidenceClaim` stores claim type, exact statement, record key, locator, applicability, contradiction, and independent status:

- `VERIFIED`: direct locatable text/formula/table/standard clause supports the claim and applicability matches;
- `PARTIAL`: source exists, but detail or applicability is only partly verified;
- `UNVERIFIED`: search snippet, secondary paraphrase, or unavailable locator only.

Metadata verification never promotes claims. Every variable definition, hard rule, parameter source, and final conclusion needs its own claim status.

## Reproducibility and fallback

Save each normalized provider response with provider/version, request, parameters, page, access time, ordered records, stable IDs, status, and SHA-256. Replay the snapshot by default; refresh creates a new evidence revision and never overwrites history.

If providers are offline, time out, or return nothing, use another configured provider or local literature. Otherwise continue with `UNVERIFIED` claims. Never fabricate a DOI, source, parameter, rule, or conclusion. An unverified rule cannot be a hard constraint; an unverified mechanism cannot be called a law.
