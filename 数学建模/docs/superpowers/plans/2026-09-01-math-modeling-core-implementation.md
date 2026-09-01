# Math Modeling Core Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a discoverable local `math-modeling-core` Skill with deterministic model/algorithm selection, 15 validated algorithm plugins, literature evidence records, runtime validation, reproducible artifacts, and a paper handoff.

**Architecture:** The Skill entrypoint is a short router into progressive references. Python code under `src/mathmodel` implements typed contracts, a two-stage selector, an allowlisted plugin registry, evidence snapshots, validation aggregation, and a path-contained runtime. Built-in algorithms implement one protocol and are accepted only through hand-derived oracle/property tests.

**Tech Stack:** Python 3.13, standard-library dataclasses/enum/pathlib/json/hashlib/urllib, NumPy, SciPy, scikit-learn, statsmodels, PyYAML, pytest.

**Spec:** `docs/superpowers/specs/2026-09-01-math-modeling-skill-merge-design.md`

## Global Constraints

- Install at `数学建模/.agents/skills/math-modeling-core/`; keep automatic discovery enabled.
- Treat `上游skills/XiaoMaColtAI-math-modeling-skill` and `上游skills/Lupynow-math-modeling-skills` as read-only inputs.
- Do not publish, push upstream, create a PR, or add license/provenance/clean-room workflows.
- Never auto-install dependencies; missing dependencies produce `BLOCKED` diagnostics.
- Read inputs and the Skill root only; write runtime artifacts only below `PROJECT_ROOT/results/<run_id>/`.
- Separate mathematical model selection from algorithm plugin selection.
- Prefer the minimum sufficient classical model; a complex challenger needs a complete `GapClosureClaim` and validated practical improvement.
- Implement exactly the 15 v1.0 stable plugins in the spec; keep NSGA-II and CVaR out of stable v1.0.
- Follow RED → verify failure → GREEN → verify pass for every production behavior.
- Preserve all unrelated worktree changes and do not modify the existing paper or contest-orchestrator Skills.

---

### Task 1: Package Bootstrap and Contract RED Tests

**Files:**
- Create: `数学建模/.agents/skills/math-modeling-core/pyproject.toml`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/__init__.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/contracts/__init__.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/contracts/core.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/conftest.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/unit/test_contracts.py`

**Interfaces:**
- Produces: `ProblemSpec`, `ModelRequirements`, `ComplexityProfile`, `GapClosureClaim`, `ModelCandidate`, `DataBundle`, `SolveConfig`, `SolveResult`, `ValidationCheck`, `ValidationReport`.
- Status enums: `CheckStatus(PASS,WARN,FAIL,BLOCKED,SKIPPED)`, `Severity(CRITICAL,MAJOR,MINOR)`, `RunStatus(SUCCESS,FAIL,BLOCKED)`.

- [ ] **Step 1: Write the failing contract tests**

```python
def test_data_bundle_separates_arrays_scalars_and_metadata():
    bundle = DataBundle(arrays={"x": np.array([1.0])}, scalars={"alpha": 2.0}, metadata={"unit": "m"})
    assert bundle.arrays["x"].tolist() == [1.0]
    assert bundle.scalars == {"alpha": 2.0}

def test_problem_spec_rejects_empty_mandatory_outputs():
    with pytest.raises(ValueError, match="mandatory_outputs"):
        ProblemSpec(problem_id="p", model_family="graph", mandatory_outputs=())

def test_solve_config_rejects_nonpositive_timeout():
    with pytest.raises(ValueError, match="timeout"):
        SolveConfig(timeout=0)
```

- [ ] **Step 2: Run `python -m pytest tests/unit/test_contracts.py -q` and verify import/contract failures**
- [ ] **Step 3: Implement frozen dataclasses, enum values, immutable tuple/frozenset normalization, and validation in `__post_init__`**
- [ ] **Step 4: Run the contract tests and verify PASS**
- [ ] **Step 5: Commit `feat: add math modeling core contracts`**

### Task 2: Validation Status Aggregation

**Files:**
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/validation/__init__.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/validation/statuses.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/unit/test_validation_statuses.py`

**Interfaces:**
- Consumes: `ValidationCheck`, `ValidationReport`, `CheckStatus`, `Severity`.
- Produces: `aggregate_report(checks: Sequence[ValidationCheck]) -> ValidationReport`.

- [ ] **Step 1: Write table-driven failing tests with literal expectations**

```python
@pytest.mark.parametrize(("checks", "expected"), [
    ([check(Severity.CRITICAL, CheckStatus.FAIL)], CheckStatus.FAIL),
    ([check(Severity.CRITICAL, CheckStatus.BLOCKED)], CheckStatus.BLOCKED),
    ([check(Severity.MAJOR, CheckStatus.FAIL)], CheckStatus.WARN),
    ([check(Severity.MINOR, CheckStatus.WARN)], CheckStatus.WARN),
    ([check(Severity.CRITICAL, CheckStatus.PASS)], CheckStatus.PASS),
])
def test_report_status_is_deterministically_aggregated(checks, expected):
    assert aggregate_report(checks).status is expected

def test_accepted_risk_does_not_rewrite_failure():
    report = aggregate_report([check(Severity.CRITICAL, CheckStatus.FAIL)], accepted_risk="user accepted")
    assert report.status is CheckStatus.FAIL
```

- [ ] **Step 2: Run the file and verify failures name missing aggregation**
- [ ] **Step 3: Implement the exact precedence `critical FAIL > required BLOCKED > WARN/major-minor FAIL > PASS`**
- [ ] **Step 4: Run tests and verify PASS**
- [ ] **Step 5: Commit `feat: add validation status aggregation`**

### Task 3: Minimum-Sufficient Model Selector

**Files:**
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/reasoning/__init__.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/reasoning/selector.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/behavior/test_model_selection.py`

**Interfaces:**
- Produces: `GateResult`, `CandidateAssessment`, `ModelSelectionDecision`, `assess_candidate(requirements, candidate)`, `select_models(requirements, candidates)`.
- `select_models` returns one main candidate and zero/one challenger; rejected candidates retain literal reasons.

- [ ] **Step 1: Write failing behavior fixtures**

```python
def test_static_nonnegative_shortest_path_prefers_dijkstra_model():
    decision = select_models(shortest_path_requirements(), [dijkstra_candidate(), dynamic_ant_colony_candidate()])
    assert decision.main.candidate_id == "classic.shortest-path"
    assert decision.challenger is None
    assert decision.rejected["paper.dynamic-ant-colony"] == ("structure_mismatch",)

def test_linear_problem_rejects_complex_candidate_without_gap_claim():
    decision = select_models(linear_program_requirements(), [lp_candidate(), ga_candidate(gap=None)])
    assert decision.main.candidate_id == "classic.linear-program"
    assert "missing_gap_closure_claim" in decision.rejected["heuristic.ga"]

def test_negative_edges_reject_dijkstra_structure():
    decision = select_models(negative_edge_requirements(), [dijkstra_candidate()])
    assert decision.main is None
    assert decision.status is CheckStatus.BLOCKED
```

- [ ] **Step 2: Run the behavior file and verify missing-selector failures**
- [ ] **Step 3: Implement seven gates, Pareto dominance, lexicographic complexity tie-break, and challenger admission**
- [ ] **Step 4: Add tests proving paper count cannot override a failed gate and an indeterminate practical threshold cannot promote a challenger**
- [ ] **Step 5: Run behavior tests and verify PASS**
- [ ] **Step 6: Commit `feat: select minimum sufficient models`**

### Task 4: Plugin Protocol, Registry, Loader, and Capability Guard

**Files:**
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/__init__.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/base.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/registry.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/loader.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/runtime/__init__.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/runtime/capabilities.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/unit/test_registry.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/unit/test_capabilities.py`

**Interfaces:**
- Produces: `FieldSpec`, `IOContract`, `AlgorithmMetadata`, `SupportDecision`, `AlgorithmPlugin` Protocol, `AlgorithmRegistry`, `CapabilityPolicy`.
- `AlgorithmRegistry.match(problem, data)` filters API/schema/status/dependency/support before deterministic ordering.

- [ ] **Step 1: Write failing tests for duplicate ID/version, `UNKNOWN` support, missing fields, and stable-before-experimental ordering**
- [ ] **Step 2: Write failing path tests proving writes outside `run_artifacts` and undeclared network/subprocess permissions return `BLOCKED`**
- [ ] **Step 3: Run both files and verify failures come from missing registry/capability behavior**
- [ ] **Step 4: Implement metadata/schema validation, allowlisted registration, JSON-compatible YAML manifest loading, and resolved-path containment**
- [ ] **Step 5: Run tests and verify PASS**
- [ ] **Step 6: Commit `feat: add secure algorithm registry`**

### Task 5: Optimization and Graph Plugins

**Files:**
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/optimization.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/graph.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/algorithms/test_optimization.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/algorithms/test_graph.py`

**Interfaces:**
- Produces built-ins: `LinearProgrammingPlugin`, `MixedIntegerLinearProgrammingPlugin`, `NonlinearOptimizationPlugin`, `DijkstraPlugin`, `MaxFlowPlugin`.
- Every plugin consumes `ProblemSpec`, namespaced `DataBundle`, and `SolveConfig`; returns `SolveResult` plus plugin checks.

- [ ] **Step 1: Write failing LP test with hand optimum `(2,2)` and objective `-10`; assert feasibility and objective literally**
- [ ] **Step 2: Write failing MILP knapsack test whose enumerated optimum is item mask `[1,0,1]` and value `8`**
- [ ] **Step 3: Write failing convex quadratic test with analytic optimum `[1,-2]`**
- [ ] **Step 4: Write failing Dijkstra hand graph test with path `A→B→C` and distance `3`; include negative-edge rejection**
- [ ] **Step 5: Write failing max-flow hand network test with flow/min-cut value `5` and conservation assertions**
- [ ] **Step 6: Run files and verify RED**
- [ ] **Step 7: Implement minimal SciPy optimization adapters and pure-Python Dijkstra/Edmonds-Karp plugins**
- [ ] **Step 8: Run files and verify PASS**
- [ ] **Step 9: Commit `feat: add optimization and graph plugins`**

### Task 6: Evaluation Plugins

**Files:**
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/evaluation.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/algorithms/test_evaluation.py`

**Interfaces:**
- Produces: `AHPPlugin`, `EntropyWeightPlugin`, `TOPSISPlugin`.

- [ ] **Step 1: Write failing AHP test for a consistent reciprocal matrix with literal normalized weights `[0.5, 0.3, 0.2]` and CR near zero**
- [ ] **Step 2: Write failing entropy test with one constant column; assert nonnegative weights summing to one and deterministic constant-column handling**
- [ ] **Step 3: Write failing TOPSIS benefit/cost fixture with literal rank `[1,0,2]` and scores in `[0,1]`**
- [ ] **Step 4: Run and verify RED**
- [ ] **Step 5: Implement NumPy algorithms with explicit zero-range/zero-entropy policies and direction validation**
- [ ] **Step 6: Run and verify PASS**
- [ ] **Step 7: Commit `feat: add evaluation plugins`**

### Task 7: Forecasting, Statistics, and ML Plugins

**Files:**
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/prediction.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/statistics.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/algorithms/test_prediction.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/algorithms/test_statistics.py`

**Interfaces:**
- Produces: `LinearRegressionPlugin`, `RidgeRegressionPlugin`, `ARIMAPlugin`, `PCAPlugin`, `RandomForestPlugin`.

- [ ] **Step 1: Write failing noiseless regression test with literal coefficients `[2,-1]`, intercept `3`, and near-zero residual**
- [ ] **Step 2: Write failing orthogonal-design ridge test using the closed-form expected coefficient vector**
- [ ] **Step 3: Write failing fixed AR(1) forecast fixture; assert forecast length, chronological split, finite output, and repeatability**
- [ ] **Step 4: Write failing diagonal-covariance PCA test; assert orthonormal components and literal explained-variance order**
- [ ] **Step 5: Write failing seeded random-forest test on a fixed separable dataset; assert repeatable predictions and legal probabilities**
- [ ] **Step 6: Run and verify RED**
- [ ] **Step 7: Implement NumPy least squares/ridge/PCA, statsmodels ARIMA, and sklearn RandomForest adapters without target leakage**
- [ ] **Step 8: Run and verify PASS**
- [ ] **Step 9: Commit `feat: add prediction and statistics plugins`**

### Task 8: Mechanistic and Simulation Plugins

**Files:**
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/mechanistic.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/simulation.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/algorithms/test_mechanistic.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/algorithms/test_simulation.py`

**Interfaces:**
- Produces: `ODESolverPlugin`, `MonteCarloPlugin`.

- [ ] **Step 1: Write failing ODE test for `dy/dt=2y`, `y(0)=1`, asserting `y(1)` within `1e-5` of `exp(2)` and monotone time**
- [ ] **Step 2: Write failing Monte Carlo test for the integral of `x^2` on `[0,1]`; assert same-seed identity and a valid confidence interval containing `1/3` under a fixed non-flaky sample size**
- [ ] **Step 3: Run and verify RED**
- [ ] **Step 4: Implement `solve_ivp` and seeded vectorized Monte Carlo adapters**
- [ ] **Step 5: Run and verify PASS**
- [ ] **Step 6: Commit `feat: add mechanistic and simulation plugins`**

### Task 9: Evidence Budget, Records, Providers, and Snapshots

**Files:**
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/evidence/__init__.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/evidence/records.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/evidence/providers.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/evidence/retrieval.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/unit/test_evidence.py`

**Interfaces:**
- Produces: `EvidenceRecord`, `EvidenceClaim`, `SearchRequest`, `SearchBudget`, `EvidenceSnapshot`, `EvidenceBundle`, `EvidenceProvider`, `OpenAlexProvider`, `SemanticScholarProvider`, `retrieve_evidence`.

- [ ] **Step 1: Write failing tests for provider-page counting, retry exclusion, initial 5/hard cap 8, DOI-first deduplication, and claim status independent of metadata status**
- [ ] **Step 2: Write failing snapshot test asserting canonical JSON SHA-256 and unchanged replay order**
- [ ] **Step 3: Run and verify RED**
- [ ] **Step 4: Implement deterministic records, canonical JSON snapshots, fake-provider-compatible retrieval, and urllib-based live providers with timeout**
- [ ] **Step 5: Add offline/timeout/empty-result tests without mocking internal code; use a complete local fake provider at the network boundary**
- [ ] **Step 6: Run and verify PASS**
- [ ] **Step 7: Commit `feat: add reproducible evidence pipeline`**

### Task 10: Runtime, Artifacts, Manifest, CLI, and Handoff

**Files:**
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/runtime/executor.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/runtime/artifacts.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/runtime/reproducibility.py`
- Create: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/runtime/dependencies.py`
- Create: `数学建模/.agents/skills/math-modeling-core/scripts/doctor.py`
- Create: `数学建模/.agents/skills/math-modeling-core/scripts/run_model.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/integration/test_runtime_cli.py`

**Interfaces:**
- Produces: `RunContext`, `ArtifactStore`, `build_manifest`, `execute_plugin`, `PaperHandoff`, documented exit codes 0/2/3/4/5.

- [ ] **Step 1: Write failing integration tests for path-independent `--help`, project-root containment, missing dependency exit 3, invalid schema exit 2, and failure diagnostics persistence**
- [ ] **Step 2: Write failing manifest test with literal required keys and stable hash under identical input**
- [ ] **Step 3: Run and verify RED**
- [ ] **Step 4: Implement resolved-path artifact directories, atomic JSON writes, dependency diagnostics, manifest serialization, and CLI dispatch**
- [ ] **Step 5: Add handoff tests proving WARN remains visible and FAIL/BLOCKED cannot produce a final-result handoff**
- [ ] **Step 6: Run integration tests and verify PASS**
- [ ] **Step 7: Commit `feat: add runtime CLI and reproducible artifacts`**

### Task 11: Skill Entry, Progressive References, and Knowledge Migration

**Files:**
- Create: `数学建模/.agents/skills/math-modeling-core/SKILL.md`
- Create: `数学建模/.agents/skills/math-modeling-core/agents/openai.yaml`
- Create: `数学建模/.agents/skills/math-modeling-core/references/workflow.md`
- Create: `数学建模/.agents/skills/math-modeling-core/references/domain-understanding.md`
- Create: `数学建模/.agents/skills/math-modeling-core/references/model-contract.md`
- Create: `数学建模/.agents/skills/math-modeling-core/references/model-selection.md`
- Create: `数学建模/.agents/skills/math-modeling-core/references/plugin-contract.md`
- Create: `数学建模/.agents/skills/math-modeling-core/references/literature-evidence.md`
- Create: `数学建模/.agents/skills/math-modeling-core/references/data-and-solver-engineering.md`
- Create: `数学建模/.agents/skills/math-modeling-core/references/validation-runtime.md`
- Create: `数学建模/.agents/skills/math-modeling-core/references/reproducibility.md`
- Create: `数学建模/.agents/skills/math-modeling-core/references/handoffs.md`
- Copy unchanged knowledge assets into: `references/cookbooks/`, `references/playbooks/`, `references/algorithm-notes/`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/integration/test_skill_layout.py`

**Interfaces:**
- `SKILL.md` routes `analyze|solve|review|evidence`, initially loading `workflow.md` plus at most two mode references.
- `openai.yaml` keeps implicit invocation enabled and names `$math-modeling-core` in `default_prompt`.

- [ ] **Step 1: Run the Skill validator against the absent directory and record RED**
- [ ] **Step 2: Write failing layout tests that execute the validator, resolve every linked reference, and reject placeholders/duplicate runtime routes**
- [ ] **Step 3: Create the concise entrypoint and mode references; migrate Lupynow taxonomy/cookbooks/playbooks and XiaoMa algorithm notes according to the frozen mapping**
- [ ] **Step 4: Validate `SKILL.md` and `agents/openai.yaml`; run layout tests and verify PASS**
- [ ] **Step 5: Manually run deterministic behavior scenarios through selector fixtures; record that fresh-agent pressure testing remains unavailable without delegation authorization**
- [ ] **Step 6: Commit `feat: add math modeling core skill`**

### Task 12: Full Registration, Acceptance, and Legacy Cutover

**Files:**
- Modify: `数学建模/.agents/skills/math-modeling-core/src/mathmodel/algorithms/__init__.py`
- Create: `数学建模/.agents/skills/math-modeling-core/tests/integration/test_builtin_registry.py`
- Move after all gates pass: `数学建模/.agents/skills/math-modeling-solver/` → `数学建模/.agents/disabled-skills/math-modeling-solver-pre-core/`
- Test existing: `数学建模/.agents/skills/math-modeling-paper/`
- Test existing: `数学建模/.agents/skills/mathmodel-skill/`

**Interfaces:**
- Produces: `create_builtin_registry() -> AlgorithmRegistry` containing exactly 15 stable plugin IDs.

- [ ] **Step 1: Write failing registry test asserting the exact 15 stable IDs and complete metadata/IO contracts**
- [ ] **Step 2: Implement built-in registration and run the test to verify PASS**
- [ ] **Step 3: Run `python -m pytest -q` from the new Skill root; require zero failures and zero warnings from project code**
- [ ] **Step 4: Run each of the 15 oracle/property tests explicitly and save the terminal summary**
- [ ] **Step 5: Run Skill validator, `python -m compileall src scripts`, CLI smoke tests, and targeted type checks available in the environment**
- [ ] **Step 6: Verify both upstream snapshots remain clean and the new Skill writes only under a temporary `PROJECT_ROOT/results/<run_id>`**
- [ ] **Step 7: Run existing `math-modeling-paper` and `mathmodel-skill` test suites**
- [ ] **Step 8: Only after Steps 3–7 pass, resolve the exact active legacy solver path, move it to the disabled directory, and verify the new Skill is the sole generic solver entry**
- [ ] **Step 9: Commit `feat: activate math modeling core skill`**

## Completion Evidence

- The implementation commit history follows the task boundaries above.
- `create_builtin_registry()` exposes exactly 15 stable plugins and zero unaudited stable templates.
- All contract, selector, algorithm, evidence, security, CLI, integration, and existing-Skill regression tests pass.
- The Skill validator and Python compilation pass.
- Upstream snapshots are byte-for-byte untouched.
- Legacy solver cutover occurs only after the complete verification command succeeds.
- Fresh-context agent behavior testing is reported separately if delegation has not been explicitly authorized.
