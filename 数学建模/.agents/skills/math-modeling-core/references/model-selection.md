# Model and algorithm selection

Keep `ModelSelector` and `AlgorithmSelector` separate. First decide what mathematical object represents the problem; only then decide how to compute it.

After classifying the subproblem, use the migrated [candidate matrix](model-selection-matrix.md) only to generate candidates. The seven gates and minimum-sufficient rule below override any matrix recommendation. Machine routing labels live in `model-taxonomy.json`.

## Seven model adequacy gates

Every candidate must pass all seven. `UNKNOWN` is not a pass.

1. **Coverage** — covers every mandatory objective, output, and subproblem.
2. **Structure** — matches continuous/discrete, static/dynamic, deterministic/stochastic, single/multiobjective, and network/spatial structure.
3. **Constraint** — represents all hard constraints within allowed approximation.
4. **Assumption** — critical assumptions are stated and not contradicted by the prompt, data, or evidence.
5. **Data** — required fields, units, scale, sample size, and quality are available or legitimately estimable.
6. **Identifiability** — parameters and latent states can be distinguished from available observations.
7. **Validation** — an oracle, invariant, benchmark, holdout, sensitivity, or other credible falsification route exists.

Reject failed candidates with machine-readable reasons. Never average away a failed gate with a score.

## Minimum-sufficient rule

Among candidates that pass every gate:

1. remove Pareto-dominated candidates;
2. minimize unverified assumptions, additional data, latent parameters, compute tier, memory tier, and dimension tier in the documented deterministic order;
3. break any remaining tie by stable candidate ID.

If a classical model fully covers the problem, it remains the main model. Do not replace it merely because a paper offers a newer, more complicated, or more “innovative” method.

## Challenger admission and promotion

Retain at most one challenger. It must be structurally independent for robustness, or provide a `GapClosureClaim` containing:

- baseline model and concrete inadequacy;
- expected practical gain;
- added variables, assumptions, data, and cost;
- validation test;
- preregistered minimum practical improvement.

The challenger is not promoted unless it passes all gates and checks, is compared under the identical `EvaluationProtocol`, achieves a stable gain whose uncertainty clears the threshold, and does not introduce a critical failure. If no practical threshold was frozen, do not promote it.

## Literature boundary

Use papers to understand the domain, define variables, identify mechanisms and rules, generate candidates, source parameters, design validation, and discover failure conditions. Paper count cannot change gate results or dominate complexity. A paper model whose scope only partially matches this problem loses to a classical model that completely matches it.

## AlgorithmSelector

Convert the chosen mathematical abstraction into required capabilities. Query the registry, then reject plugins with incompatible family/API/schema, missing capabilities or dependencies, missing fields, excessive permissions, experimental status without authorization, or `supports=UNSUPPORTED/UNKNOWN`. Rank surviving stable plugins by declared guarantee, resource tier, determinism, ID, and version. Run P1 before full data.
