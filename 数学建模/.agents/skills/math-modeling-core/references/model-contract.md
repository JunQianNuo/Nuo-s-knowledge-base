# Model contract

Freeze the contract before full solving. Changes after freeze create a new revision and rerun affected gates.

## ProblemSpec checklist

- stable problem and subproblem IDs;
- mathematical model family and structural features;
- mandatory outputs and required capabilities;
- objective functions and metric directions;
- hard constraints versus soft preferences;
- known/unknown parameters, uncertainty, and units;
- explicit assumptions with evidence status;
- user-defined minimum practical improvement for any challenger;
- accepted input fields and forbidden leakage fields;
- split, seeds, tolerances, resource limits, and rollback conditions.

## Variable and data contract

Every field maps to a `VariableSpec`. Use namespaced `DataBundle` containers (`arrays`, `tables`, `scalars`, `targets`, `metadata`) instead of an untyped catch-all. Keep raw inputs read-only. Record transformations, missing-value policy, units, ranges, train/validation/test boundaries, and hashes.

## Candidate contract

Each `ModelCandidate` declares equations or objective/constraints, capabilities, outputs covered, structural features, required data, assumption states, identifiability, validation path, known gaps, evidence, and `ComplexityProfile`.

Complexity is auditable, not an aesthetic label. Count additional fields, latent parameters, unverified critical assumptions, dimensional tier, time tier, and memory tier.

## EvaluationProtocol

Freeze before comparing candidates:

- identical data and chronological/group split;
- identical seeds or seed set;
- metric definitions and direction;
- numerical tolerances and confidence level;
- resource/time ceiling;
- feasibility and problem-specific invariants;
- baseline and uncertainty procedure;
- minimum practical improvement.

If the target, hard constraints, units, or evaluation protocol are still materially ambiguous, the contract is not frozen and full solving is `BLOCKED`.
