# Paper handoff

`math-modeling-core` owns problem interpretation, contracts, evidence, model and algorithm decisions, solving, validation, and reproducibility. `math-modeling-paper` owns paper prose, structure, formatting, and submission-facing presentation. End-to-end contest project orchestration remains with `mathmodel-skill`.

Create a `PaperHandoff` only when the user requests writing after the core run. It is a read-only reference to frozen artifacts, not a second copy that can silently change results.

## Handoff contents

- problem interpretation and unresolved ambiguities;
- variables, units, roles, definitions, and evidence;
- equations/objective/constraints and assumptions;
- model adequacy gates, rejected candidates, main/challenger decision;
- algorithm/plugin version, parameters, and solver guarantee;
- results, figures, tables, and artifact paths;
- validation checks, sensitivity, uncertainty, warnings, and limitations;
- claim-level citations and evidence applicability;
- manifest hash and reproduction command.

## Status gate

- `PASS`: final-result handoff allowed.
- `WARN`: allowed only with warnings prominently preserved; the paper skill may improve narration but cannot hide or rewrite them.
- `FAIL/BLOCKED`: no final-result handoff. On explicit user request, create only a clearly labeled diagnostic draft that cannot be presented as a validated conclusion.

The paper skill may reorganize prose and visuals. It may not change equations, parameter values, metrics, validation states, evidence status, or artifacts. Any requested mathematical change returns to a new core run and produces a new manifest revision.
