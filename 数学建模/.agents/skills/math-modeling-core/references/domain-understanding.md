# Domain understanding and variable design

E0 occurs after the first reading of the prompt and before formal decomposition or variable freeze. Its purpose is to understand what the problem means, not to decorate a predetermined model with citations.

## E0 query families

Generate only queries that can change the contract:

1. domain background and system boundary;
2. physical, biological, behavioral, or operational mechanism;
3. current business rule, standard, regulation, or institutional constraint;
4. variable definition, unit, measurement method, reasonable range, and typical scale.

Prefer reviews, standards, official current sources, authoritative data dictionaries, textbooks, and original research according to the claim type. A paper is secondary evidence for a mutable real-world rule; confirm such rules with the current official source.

## Required domain artifacts

### DomainContext

Record object, scenario boundary, stakeholders, temporal and spatial scale, terms, typical magnitudes, exclusions, and unresolved ambiguities.

### VariableSpec

For every candidate variable record:

- name and mathematical symbol;
- domain definition and role: `input`, `state`, `decision`, `output`, `latent`, or `confounder`;
- type and unit, or an explicit dimensionless declaration;
- measurement/derivation method and source field;
- reasonable range and missingness behavior;
- observability, data availability, and identifiability;
- evidence links and claim status.

Admit a variable only after evaluating relevance, mechanism evidence, data availability, measurability, identifiability, redundancy/collinearity, and decision actionability. Frequency in papers is never an admission rule.

### MechanismSpec

Record upstream/downstream variables, direction, candidate mathematical relation, scale, boundary conditions, evidence, and confidence. Label the relation as one of:

- correlation;
- empirical association;
- causal mechanism;
- conservation or physical law;
- business constraint.

Do not promote correlation to causation, or a literature mechanism to a law for this problem, without matching scale, boundary conditions, and identifiability.

### BusinessRuleSpec

Record rule text, source type, effective time, region/organization, version, hard/soft status, formal constraint candidate, and conflicts. An unverified or version-ambiguous rule cannot become a hard constraint.

## Conflict and freeze policy

Keep competing definitions, units, mechanisms, or rules side by side. Resolve by applicability, authority, recency for mutable rules, and directness of evidence. If a conflict would change the objective or feasible region, pause for authoritative evidence or a user decision. Otherwise make the conservative assumption explicit and keep its validation status visible.
