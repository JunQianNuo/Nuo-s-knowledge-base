# Data and solver engineering

## Data audit before modeling

Create a field inventory with type, shape, unit, role, missingness, range, source, hash, and read-only path. Check duplicate entities, time order, inconsistent units, impossible values, outliers, encoding, class balance, target leakage, sampling bias, and whether the data can identify proposed parameters.

Freeze every transformation. Fit imputers, scalers, encoders, PCA, feature selection, and hyperparameters only on the training partition. Time series split chronologically; grouped entities stay in one partition. Keep `X_predict` separate from `y`.

## Numerical audit

Check scale, conditioning, dimensional consistency, finite values, bounds, tolerances, convergence criteria, and solver status. Use stable formulations and sparse structures when appropriate. Report infeasible, unbounded, timed-out, and numerically failed states distinctly.

An objective value is not proof of feasibility or validity. Validate constraints and invariants independently. For stochastic algorithms, freeze seeds and assess multiple seeds when stability matters.

## P1 minimal equivalent instance

Before full execution, construct the smallest fixture preserving the essential structure: integer decisions, negative-edge prohibition, flow conservation, dynamic coupling, stochastic sampling, or the relevant invariant. Compare against a hand solution, analytic result, independent formulation, or mathematical property. P1 failure blocks full execution and rolls back to the contract or plugin.

## Dependencies and resources

Check only dependencies declared by the selected plugin and project contract. Report missing packages and suggested commands, but never install automatically. Do not silently replace ARIMA with regression, MILP with a heuristic, or any other model because a package is absent.

Use `python scripts/doctor.py --profile <core|optimization|forecasting|ml|all>` for diagnostics. The public runner is:

```text
python scripts/run_model.py --project-root <absolute-path> --problem <problem.yaml> [--data <data.yaml>] --mode <analyze|solve|review|evidence> [--review-artifact <manifest.json>] [--evidence-snapshot <snapshot.json>] [--output results/<run_id>] [--refresh-evidence]
```

`analyze` writes a domain-freeze audit and, when `model_requirements` plus `model_candidates` are declared, executes the seven adequacy gates and minimum-sufficient selector. `evidence` creates four E0 query tracks plus one E1 track, replays verified `--evidence-snapshot` inputs without network, and performs live retrieval only when `--refresh-evidence` is explicit. `review` requires `--review-artifact` and verifies the manifest, input hashes, and bound artifact hashes. `solve` consumes the frozen model decision, selects the algorithm through the audited registry, and records a structure-aware known-answer P1 report before touching the full instance. If no candidate set is embedded, the model decision is recorded as externally frozen/`SKIPPED`, not invented by the runtime.

Exit codes: `0` success; `2` input/schema error; `3` dependency/permission/support blocked; `4` solver or critical validation failure; `5` unexpected internal error. Persist diagnostics whenever a run directory can safely be created.
