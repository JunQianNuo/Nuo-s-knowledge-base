# Algorithm plugin contract

Plugins solve an already-selected mathematical abstraction. They do not reinterpret the problem or silently substitute another model.

## Required interface

Each plugin implements:

- immutable `AlgorithmMetadata`;
- `supports(problem, data) -> SupportDecision`;
- `solve(problem, data, config) -> SolveResult`;
- `validate_result(result) -> checks`.

`SupportDecision` is `SUPPORTED`, `UNSUPPORTED`, or `UNKNOWN` with explicit reasons. Only `SUPPORTED` can execute.

## Metadata and schemas

Declare unique plugin ID and algorithm version, API/schema versions, `stable|experimental` status, capabilities, model families, dependencies, solver guarantee, validation capabilities, determinism, resource tier, permissions, I/O contract, and content hash. A reused ID/version with different content is invalid.

`IOContract` names each required input, config, and output field. Validate it before invoking the solver; missing hard constraints, target meaning, units, or fields are not values a plugin may guess.

## Built-in stable plugins

| Family | Plugin |
|---|---|
| continuous optimization | linear programming, nonlinear optimization |
| integer optimization | mixed-integer linear programming |
| graphs | Dijkstra shortest path, Edmonds–Karp max flow |
| evaluation | AHP, entropy weight, TOPSIS |
| prediction | linear regression, ridge regression, ARIMA, random forest |
| statistics | PCA |
| mechanism/simulation | ODE integration, Monte Carlo integration |

Knowledge templates and unaudited upstream code are examples only. They cannot become `stable` until they implement the contract and pass unit plus mathematical oracle/property tests.

## Capability safety

Default permissions allow declared input/reference reads and writes only inside the active run artifacts. Network, secrets, arbitrary subprocesses, dynamic installation, and dynamic `eval/exec` are denied. An external solver requires `subprocess=true` and an executable allowlist; pass arguments as an array, never a shell string.

Evidence providers are separate network-capable components governed by the evidence budget. They cannot write the algorithm directory or read secrets.

## Extension policy

Load built-ins from a versioned allowlist. Load a personal extension only from an explicitly configured path or entry point with a validated manifest. Do not recursively scan the project or import unregistered Python files. Missing dependencies return `BLOCKED` with an exact list; never install them automatically.

The personal manifest is closed-schema metadata: `plugin_id`, semantic `algorithm_version`, positive `api_version`/`schema_version`, `status`, `entrypoint`, dependency list, complete permission object, input/output/config field schemas, and `sha256:<digest>` of the entrypoint module source. Resolve both manifest and source below an explicit allowed root, verify the source hash, and only then consider a separate authorized import step. Unknown fields such as install commands are rejected rather than executed.
