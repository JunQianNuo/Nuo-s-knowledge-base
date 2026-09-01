---
name: math-modeling-core
description: Use when solving or reviewing a mathematical-modeling problem, selecting mathematical models or algorithms, auditing modeling data, or validating and reproducing a model; excludes requests solely for contest-paper prose, formatting, or end-to-end contest project orchestration.
---

# Math Modeling Core

Build the smallest adequate mathematical model, execute only compatible audited algorithms, and preserve evidence and validation state. This skill owns modeling analysis and computation. It does not own paper prose or contest orchestration.

## Select one mode

Default to `solve` unless the user clearly requests another mode. Always read [workflow](references/workflow.md).

- `analyze`: read [domain understanding](references/domain-understanding.md) and [problem decomposition](references/problem-decomposition.md).
- `solve`: read [model contract](references/model-contract.md) and [data and solver engineering](references/data-and-solver-engineering.md).
- `review`: read [model contract](references/model-contract.md) and [validation runtime](references/validation-runtime.md).
- `evidence`: read [literature evidence](references/literature-evidence.md) and [domain understanding](references/domain-understanding.md).

Do not load every reference at startup. After the taxonomy and model family are known, load only the matching cookbook, playbook, or algorithm note.

## Non-negotiable gates

1. Interpret the domain before freezing variables or equations. Use E0 evidence for unfamiliar terms, mechanisms, mutable business rules, units, and typical scales. Network failure is not permission to invent facts: continue with `UNVERIFIED` labels.
2. Select the mathematical abstraction before selecting an algorithm. A convenient library or paper cannot define the problem.
3. Apply all seven model adequacy gates. `UNKNOWN` does not pass. If a classical model fully covers the problem, prefer it over a more complex paper model unless the challenger has a concrete `GapClosureClaim` and later demonstrates a preregistered practical improvement.
4. Treat literature count as evidence coverage, never as a model-ranking score. A verified DOI does not verify every claim made about the paper.
5. Run a plugin only after its input contract, dependencies, support status, and permissions pass. Never install a dependency or substitute another model silently.
6. Write only under `PROJECT_ROOT/results/<run_id>/`. Preserve raw failure diagnostics and machine status; prose cannot convert `FAIL` or `BLOCKED` to `PASS`.
7. Compare models only under the same frozen evaluation protocol. Promote a challenger only when its stable practical gain exceeds the preregistered threshold.

## Conditional routing

- Before choosing a model, read [model selection](references/model-selection.md).
- Before adding or auditing an algorithm plugin, read [plugin contract](references/plugin-contract.md).
- Before E0/E1 retrieval or citation claims, read [literature evidence](references/literature-evidence.md).
- Before full execution, read [validation runtime](references/validation-runtime.md).
- For manifests, replay, or environment checks, read [reproducibility](references/reproducibility.md).
- For a user-requested writing handoff, read [handoffs](references/handoffs.md). Hand off to `math-modeling-paper`; do not write the paper here.

## Stop conditions

Pause only when an unresolved choice changes the mathematical objective or a hard constraint, a mutable rule cannot be verified, an experimental plugin or new dependency needs authorization, the search budget must exceed its approved cap, or the user requests a final paper handoff from `FAIL/BLOCKED` results. Otherwise proceed with explicit assumptions and preserve them in the run artifacts.
