# Problem decomposition

## First separate calculation from modeling

A deterministic calculation uses a supplied formula or an unambiguous arithmetic transformation and offers no meaningful modeling choice. Execute it directly and record its formula. A modeling subproblem requires assumptions, abstraction, estimation, uncertainty, or optimization. If the prompt explicitly asks to build a model, treat it as modeling even if part of it is deterministic.

## Extract the problem graph

For each requested output record its input fields, unknowns, objective, hard constraints, soft preferences, uncertainty, time/space scale, and upstream/downstream subproblems. Draw a directed data-flow graph and label every edge with the value transferred. Do not let a downstream metric leak into an upstream training or selection step.

## Twelve taxonomies

| Type | Output signal | Typical abstractions |
|---|---|---|
| prediction/regression | future or continuous estimate | regression, time series, state model |
| classification | discrete label or probability | statistical/ML classifier |
| evaluation/ranking | score, rank, selection | AHP, entropy weight, TOPSIS |
| optimization/decision | feasible best action | LP, MILP, nonlinear, stochastic/robust optimization |
| mechanism/physics | state trajectory or physical quantity | algebraic balance, ODE/PDE, conservation law |
| clustering/grouping | unlabeled groups | distance/density/probabilistic clustering |
| association/causality | relationship and uncertainty | regression, experiment, causal design |
| game/strategy | equilibrium or policy | static/dynamic/cooperative game |
| geometry/kinematics | position, path, angle, collision | analytic geometry, transforms, constrained motion |
| statistical inference/design | effect, interval, decision rule | testing, sampling, experimental design |
| networks/graphs | path, flow, matching, robustness | shortest path, flow, graph statistics |
| ecosystem/environment | population, diversity, emissions | coupled dynamics, networks, accounting |

Taxonomy only generates candidates. It does not select a model or plugin.

## Mixed problems

Split mixed requests into an ordered pipeline, for example prediction → evaluation → optimization or mechanism → simulation → policy optimization. Freeze the interface between stages: output fields, units, uncertainty, and validation status. A downstream stage must consume uncertainty or limitations, not only point estimates.

## Decomposition output

Produce a table with subproblem ID, taxonomy, deterministic/modeling flag, inputs, outputs, decision variables, constraints, assumptions, evidence gaps, and dependencies. Generate bilingual E1 queries only after E0 has corrected domain terminology. Then build the formal model contract.
