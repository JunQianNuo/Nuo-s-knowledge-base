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

Record skill/API/schema versions, run ID/time, input hashes, `ProblemSpec`, variable/domain revisions, model requirements, accepted and rejected candidates with gate reasons, plugin ID/version/hash and solver guarantee, dependencies/environment, solve config, seeds/tolerances, evaluation protocol, validation state, evidence queries/budget/provider versions/snapshot hashes/revision/claim states, artifacts, and one replay command.

Use canonical JSON and SHA-256. Identical declared inputs and timestamps must produce a byte-stable manifest hash. Never overwrite an algorithm version, evidence revision, or prior run to create the appearance of reproducibility.

## Replay rules

- replay evidence snapshots unless refresh is explicit;
- use the recorded plugin version and parameters;
- verify input hashes before solving;
- surface environment/version differences;
- preserve all rejected candidates and warnings;
- create a new run for refreshed evidence or changed assumptions.

`doctor.py` reports dependency state only. It must not install packages. A missing dependency is a reproducible `BLOCKED` result, not permission to change the mathematical model.
