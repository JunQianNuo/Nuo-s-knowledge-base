# Validation runtime

Validation tries to falsify the model, implementation, and conclusion. It is not a paragraph written after optimization.

## Status semantics

- `PASS`: executed and met threshold;
- `WARN`: usable result with visible noncritical risk;
- `FAIL`: executed and violated a requirement;
- `BLOCKED`: a required check could not execute because a prerequisite is missing;
- `SKIPPED`: only an explicitly inapplicable optional check, with reason.

Aggregate deterministically: critical `FAIL` → `FAIL`; otherwise required `BLOCKED/SKIPPED` → `BLOCKED`; otherwise any `WARN` or major/minor `FAIL` → `WARN`; all required checks passing → `PASS`. Accepted risk is an annotation and never rewrites status.

## Five runtime layers

1. **Data** — schema, units, missingness, leakage, splits, ranges, sample adequacy.
2. **Mathematical** — feasibility, bounds, conservation, probability sums, path/flow integrity, equilibrium, dimensional consistency.
3. **Numerical** — conditioning, finite outputs, convergence, residuals, tolerances, alternate initialization, solver gaps.
4. **Statistical/generalization** — chronological holdout or cross-validation, residual assumptions, uncertainty, calibration, multiple seeds.
5. **Problem constraint** — every requested output and hard business/physical constraint, including the verified time/region/version of rules.

Also verify DOI/title deduplication, claim applicability, parameter provenance, and evidence conflicts when those affect the model.

## Test classes

- unit: local formula or transformation;
- oracle: hand/analytic/independent known answer;
- property: invariant such as flow conservation or probability bounds;
- benchmark: standard problem/data behavior;
- regression: fixed input/seed/tolerance stability.

Every stable plugin needs unit plus oracle/property coverage.

## Comparison

Only `PASS/WARN` results enter comparison; retain all WARN penalties and text. Use the frozen `EvaluationProtocol` for all candidates. Promote a complex challenger only if its improvement is stable, practically exceeds the preregistered threshold, and introduces no critical failure. Otherwise keep the minimum-sufficient main model.

On failure, preserve inputs, raw result, logs, checks, and rollback stage. Never describe timeout as infeasibility, best observed incumbent as an optimum without the declared guarantee, or metric gain as proof of model adequacy.
