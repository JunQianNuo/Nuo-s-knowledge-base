# Reproducibility

All mutable output belongs under one resolved `PROJECT_ROOT/results/<run_id>/`. Inputs and skill references remain read-only.

## Fixed layout

```text
results/<run_id>/
├── inputs/
├── domain/
├── evidence/
├── selection/
├── solve/
├── validation/
├── figures/
├── paper-handoff/
└── manifest.json
```

Resolve every path and verify containment before opening. Write structured files atomically. Large user inputs may remain external read-only references, but record absolute resolved path, size, and hash.

## Manifest contents

Record skill/API/schema versions, run ID/time, resolved input locations and hashes, `ProblemSpec`, variable/domain revisions, model requirements, accepted and rejected candidates with gate reasons, plugin ID/version/hash and solver guarantee, dependencies/environment, solve config, seeds/tolerances, evaluation protocol, validation state, evidence queries/budget/provider versions/snapshot hashes/revision/claim states, artifact paths and hashes, and one replay command. Selection, P1, evidence, solve, and diagnostic details may live in dedicated artifacts, but their hashes must be bound into the manifest.

Use canonical JSON and SHA-256. Identical declared inputs and timestamps must produce a byte-stable manifest hash. Never overwrite an algorithm version, evidence revision, or prior run to create the appearance of reproducibility.

## Replay rules

- replay evidence snapshots unless refresh is explicit;
- use the recorded plugin version and parameters;
- verify input hashes before solving;
- surface environment/version differences;
- preserve all rejected candidates and warnings;
- create a new run for refreshed evidence or changed assumptions.
- never reuse an existing run directory; replay commands omit `--output` so they create a new immutable run instead of replacing the source run.

Review mode recomputes `manifest_hash` after removing the declared hash field. A changed status, artifact reference, input, or environment declaration therefore fails review instead of being accepted as prose.

`doctor.py` reports dependency state only. It must not install packages. A missing dependency is a reproducible `BLOCKED` result, not permission to change the mathematical model.
