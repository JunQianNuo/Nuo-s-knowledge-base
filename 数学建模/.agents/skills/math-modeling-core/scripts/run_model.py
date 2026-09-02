from __future__ import annotations

import argparse
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping


SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "src"))

from mathmodel.algorithms import create_builtin_registry  # noqa: E402
from mathmodel.contracts import (  # noqa: E402
    BusinessRuleSpec,
    CheckStatus,
    ConstraintKind,
    DataBundle,
    DomainContext,
    EvidenceStatus,
    MechanismKind,
    MechanismSpec,
    ProblemSpec,
    RunStatus,
    SolveConfig,
    VariableRole,
    VariableSpec,
)
from mathmodel.runtime import (  # noqa: E402
    ArtifactStore,
    CapabilityPolicy,
    RunContext,
    build_manifest,
    check_dependencies,
    execute_plugin,
    run_p1,
    verify_manifest,
)
from mathmodel.evidence import (  # noqa: E402
    OpenAlexProvider,
    SearchBudget,
    SearchRequest,
    SemanticScholarProvider,
    retrieve_evidence,
)


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(
        description="Run a validated math-modeling-core plugin"
    )
    value.add_argument("--project-root", required=True)
    value.add_argument("--problem", required=True)
    value.add_argument("--data")
    value.add_argument(
        "--mode", choices=("analyze", "solve", "review", "evidence"), default="solve"
    )
    value.add_argument("--output")
    value.add_argument("--refresh-evidence", action="store_true")
    value.add_argument("--review-artifact")
    return value


def main(argv: list[str] | None = None) -> int:
    arguments = parser().parse_args(argv)
    project_root = Path(arguments.project_root)
    if not project_root.is_absolute():
        print("project root must be absolute", file=sys.stderr)
        return 2

    problem_path = Path(arguments.problem).resolve()
    data_path = Path(arguments.data).resolve() if arguments.data else None
    review_artifact_path = (
        Path(arguments.review_artifact).resolve() if arguments.review_artifact else None
    )
    try:
        problem_raw = _load_mapping(problem_path)
        problem = _problem_spec(problem_raw)
        data = _data_bundle(_load_mapping(data_path)) if data_path else DataBundle()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"invalid problem schema: {exc}", file=sys.stderr)
        return 2

    output = arguments.output or _default_output(problem_path, data_path)
    try:
        context = RunContext.create(
            skill_root=SKILL_ROOT,
            project_root=project_root,
            output=output,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    store = ArtifactStore(context)
    store.initialize()
    created_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )
    input_hashes = {"problem": _file_hash(problem_path)}
    if data_path:
        input_hashes["data"] = _file_hash(data_path)
    if review_artifact_path and review_artifact_path.is_file():
        input_hashes["review_artifact"] = _file_hash(review_artifact_path)

    config = SolveConfig()
    try:
        if arguments.mode != "solve":
            exit_code, validation_status, evidence_revision, artifacts = (
                _run_non_solve_mode(
                    mode=arguments.mode,
                    arguments=arguments,
                    problem=problem,
                    problem_raw=problem_raw,
                    store=store,
                    context=context,
                )
            )
            manifest = build_manifest(
                context=context,
                problem=problem,
                plugin=None,
                config=config,
                input_hashes=input_hashes,
                validation_status=validation_status,
                evidence_revision=evidence_revision,
                created_at=created_at,
                mode=arguments.mode,
                problem_path=problem_path,
                data_path=data_path,
                review_artifact=review_artifact_path,
                evidence_refreshed=arguments.refresh_evidence,
                artifacts=artifacts,
            )
            store.write_json("manifest.json", manifest)
            return exit_code

        registry = create_builtin_registry()
        declared_dependencies = frozenset(
            dependency
            for plugin in registry.plugins
            for dependency in plugin.metadata.dependencies
        )
        installed_dependencies = frozenset(
            check_dependencies(declared_dependencies).installed
        )
        registry_decision = registry.match(
            problem,
            data,
            installed_dependencies=installed_dependencies,
        )
        plugin = registry_decision.matches[0] if registry_decision.matches else None
        store.write_json(
            "selection/algorithm.json",
            {
                "selection_source": "audited_builtin_registry",
                "selected_plugin": plugin.metadata.plugin_id if plugin else None,
                "selected_version": (
                    plugin.metadata.algorithm_version if plugin else None
                ),
                "rejected": registry_decision.rejected,
            },
        )
        if plugin is None:
            store.write_json(
                "diagnostics.json",
                {
                    "reason": "no_eligible_registered_plugin",
                    "rejected": registry_decision.rejected,
                },
            )
            manifest = build_manifest(
                context=context,
                problem=problem,
                plugin=None,
                config=config,
                input_hashes=input_hashes,
                validation_status=CheckStatus.BLOCKED,
                evidence_revision=None,
                created_at=created_at,
                mode="solve",
                problem_path=problem_path,
                data_path=data_path,
                artifacts=("selection/algorithm.json", "diagnostics.json"),
            )
            store.write_json("manifest.json", manifest)
            print(
                f"no eligible plugin for model family: {problem.model_family}",
                file=sys.stderr,
            )
            return 3

        p1_report = run_p1(plugin)
        store.write_json("selection/p1.json", p1_report)
        if p1_report.status is not CheckStatus.PASS:
            store.write_json(
                "diagnostics.json",
                {
                    "reason": "p1_gate_not_passed",
                    "status": p1_report.status,
                    "reasons": p1_report.reasons,
                },
            )
            manifest = build_manifest(
                context=context,
                problem=problem,
                plugin=plugin.metadata,
                config=config,
                input_hashes=input_hashes,
                validation_status=p1_report.status,
                evidence_revision=None,
                created_at=created_at,
                mode="solve",
                problem_path=problem_path,
                data_path=data_path,
                artifacts=(
                    "selection/algorithm.json",
                    "selection/p1.json",
                    "diagnostics.json",
                ),
            )
            store.write_json("manifest.json", manifest)
            return 3 if p1_report.status is CheckStatus.BLOCKED else 4

        additional_dependencies = frozenset(
            str(name) for name in problem_raw.get("required_dependencies", ())
        )
        declared_inputs = (problem_path,) + ((data_path,) if data_path else ())
        capability_policy = CapabilityPolicy(
            skill_root=SKILL_ROOT,
            project_root=context.project_root,
            run_root=context.run_root,
            input_roots=declared_inputs,
        )
        outcome = execute_plugin(
            plugin,
            problem,
            data,
            config,
            additional_dependencies=additional_dependencies,
            capability_policy=capability_policy,
            requested_reads=declared_inputs,
        )
        if outcome.result is None:
            validation_status = CheckStatus.BLOCKED
            store.write_json(
                "diagnostics.json",
                {
                    "missing_dependencies": outcome.dependencies.missing,
                    "reasons": outcome.reasons,
                },
            )
        else:
            result = outcome.result
            validation_status = (
                result.validation_report.status
                if result.validation_report
                else (
                    CheckStatus.PASS
                    if result.status is RunStatus.SUCCESS
                    else CheckStatus.FAIL
                )
            )
            store.write_json("solve/result.json", result)
            store.write_json(
                "diagnostics.json",
                {"exit_code": outcome.exit_code, "diagnostics": result.diagnostics},
            )
        manifest = build_manifest(
            context=context,
            problem=problem,
            plugin=plugin.metadata,
            config=config,
            input_hashes=input_hashes,
            validation_status=validation_status,
            evidence_revision=None,
            created_at=created_at,
            mode="solve",
            problem_path=problem_path,
            data_path=data_path,
            artifacts=(
                "selection/algorithm.json",
                "selection/p1.json",
                "solve/result.json" if outcome.result is not None else "diagnostics.json",
            ),
        )
        store.write_json("manifest.json", manifest)
        return outcome.exit_code
    except Exception as exc:
        store.write_json(
            "diagnostics.json",
            {"internal_error": type(exc).__name__, "message": str(exc)},
        )
        print(f"internal runtime error: {exc}", file=sys.stderr)
        return 5


def _run_non_solve_mode(
    *,
    mode: str,
    arguments: argparse.Namespace,
    problem: ProblemSpec,
    problem_raw: Mapping[str, Any],
    store: ArtifactStore,
    context: RunContext,
) -> tuple[int, CheckStatus, str | None, tuple[str, ...]]:
    if mode == "analyze":
        return _run_analyze(problem, store)
    if mode == "evidence":
        return _run_evidence(
            problem,
            problem_raw,
            store,
            refresh=bool(arguments.refresh_evidence),
        )
    if mode == "review":
        return _run_review(arguments.review_artifact, store, context)
    raise ValueError(f"unsupported mode: {mode}")


def _run_analyze(
    problem: ProblemSpec, store: ArtifactStore
) -> tuple[int, CheckStatus, None, tuple[str, ...]]:
    reasons: list[str] = []
    if problem.domain_context is None:
        reasons.append("domain_context_missing")
    elif not problem.domain_context.ready_to_freeze:
        reasons.extend(
            f"unresolved_ambiguity:{item}"
            for item in problem.domain_context.unresolved_ambiguities
        )
    status = CheckStatus.BLOCKED if reasons else CheckStatus.PASS
    audit = {
        "status": status.value,
        "reasons": reasons,
        "domain_context_ready": bool(
            problem.domain_context and problem.domain_context.ready_to_freeze
        ),
        "variable_count": len(problem.variables),
        "mechanism_count": len(problem.mechanisms),
        "business_rule_count": len(problem.business_rules),
        "solver_executed": False,
    }
    store.write_json("domain/audit.json", audit)
    store.write_json(
        "selection/model-readiness.json",
        {
            "model_family": problem.model_family,
            "mandatory_outputs": problem.mandatory_outputs,
            "required_capabilities": problem.required_capabilities,
            "ready_for_model_selection": status is CheckStatus.PASS,
        },
    )
    store.write_json(
        "diagnostics.json",
        {"mode": "analyze", "solver_executed": False, "status": status.value},
    )
    return (
        3 if status is CheckStatus.BLOCKED else 0,
        status,
        None,
        ("domain/audit.json", "selection/model-readiness.json", "diagnostics.json"),
    )


def _run_evidence(
    problem: ProblemSpec,
    problem_raw: Mapping[str, Any],
    store: ArtifactStore,
    *,
    refresh: bool,
) -> tuple[int, CheckStatus, str | None, tuple[str, ...]]:
    raw_requests = problem_raw.get("evidence_requests")
    if raw_requests is None:
        subject = (
            problem.domain_context.object_name
            if problem.domain_context is not None
            else problem.problem_id
        )
        provider = str(problem_raw.get("evidence_provider", "openalex"))
        requests = (
            SearchRequest(
                phase="E0",
                query=(
                    f"{subject} domain background terminology system boundary "
                    "typical scale"
                ),
                provider=provider,
            ),
            SearchRequest(
                phase="E0",
                query=(
                    f"{subject} physical mechanism causal relationship "
                    "applicable conditions"
                ),
                provider=provider,
            ),
            SearchRequest(
                phase="E0",
                query=(
                    f"{subject} current business rules standards constraints "
                    "region effective date"
                ),
                provider=provider,
            ),
            SearchRequest(
                phase="E0",
                query=(
                    f"{subject} variable definition measurement unit observable data"
                ),
                provider=provider,
            ),
            SearchRequest(
                phase="E1",
                query=(
                    f"{problem.model_family} mathematical model validation "
                    "benchmark limitations"
                ),
                provider=provider,
            ),
        )
    else:
        if not isinstance(raw_requests, (tuple, list)):
            raise ValueError("evidence_requests must be a list")
        requests = tuple(SearchRequest.from_dict(item) for item in raw_requests)

    store.write_json(
        "evidence/query-plan.json",
        {
            "requests": tuple(request.to_dict() for request in requests),
            "refresh_requested": refresh,
        },
    )
    if not refresh:
        store.write_json(
            "diagnostics.json",
            {
                "mode": "evidence",
                "solver_executed": False,
                "evidence_action": "query_plan_created",
                "refresh_required_for_network": True,
            },
        )
        return (
            0,
            CheckStatus.SKIPPED,
            None,
            ("evidence/query-plan.json", "diagnostics.json"),
        )

    unresolved_critical = bool(problem_raw.get("unresolved_critical_claim", False))
    budget_reason = None
    if len(requests) > 8:
        budget_reason = "search_hard_cap_exceeded"
    elif len(requests) > 5 and not unresolved_critical:
        budget_reason = "initial_search_budget_exceeded"
    if budget_reason is not None:
        store.write_json(
            "diagnostics.json",
            {
                "mode": "evidence",
                "solver_executed": False,
                "evidence_action": "blocked",
                "reasons": (budget_reason,),
            },
        )
        return 3, CheckStatus.BLOCKED, None, (
            "evidence/query-plan.json",
            "diagnostics.json",
        )

    providers = {
        "openalex": OpenAlexProvider(),
        "semantic-scholar": SemanticScholarProvider(),
    }
    bundle = retrieve_evidence(
        requests,
        providers,
        SearchBudget(),
        accessed_on=date.today(),
        unresolved_critical=unresolved_critical,
    )
    store.write_json("evidence/bundle.json", bundle)
    for snapshot in bundle.snapshots:
        store.write_json(
            f"evidence/snapshots/{snapshot.snapshot_hash}.json",
            json.loads(snapshot.to_json()),
        )
    event_statuses = tuple(event.status for event in bundle.network_events)
    if not bundle.records:
        status = CheckStatus.BLOCKED
        exit_code = 3
    elif any(value != "ok" for value in event_statuses):
        status = CheckStatus.WARN
        exit_code = 0
    else:
        status = CheckStatus.PASS
        exit_code = 0
    store.write_json(
        "diagnostics.json",
        {
            "mode": "evidence",
            "solver_executed": False,
            "evidence_action": "network_refresh",
            "record_count": len(bundle.records),
            "claim_count": len(bundle.claims),
            "network_statuses": event_statuses,
        },
    )
    return (
        exit_code,
        status,
        bundle.evidence_revision,
        ("evidence/query-plan.json", "evidence/bundle.json", "diagnostics.json"),
    )


def _run_review(
    artifact: str | None,
    store: ArtifactStore,
    context: RunContext,
) -> tuple[int, CheckStatus, None, tuple[str, ...]]:
    if artifact is None:
        report = {"reasons": ["review_artifact_missing"], "status": "BLOCKED"}
        store.write_json("validation/review.json", report)
        store.write_json(
            "diagnostics.json", {"mode": "review", "solver_executed": False}
        )
        return 3, CheckStatus.BLOCKED, None, (
            "validation/review.json",
            "diagnostics.json",
        )

    artifact_path = Path(artifact).resolve()
    if not artifact_path.is_relative_to(context.project_root) or not artifact_path.is_file():
        report = {"reasons": ["review_artifact_not_allowed"], "status": "BLOCKED"}
        status = CheckStatus.BLOCKED
        exit_code = 3
    else:
        reviewed = _load_mapping(artifact_path)
        valid = verify_manifest(reviewed)
        report = {
            "artifact": str(artifact_path),
            "manifest_hash_valid": valid,
            "reasons": [] if valid else ["manifest_hash_mismatch"],
            "status": "PASS" if valid else "FAIL",
        }
        status = CheckStatus.PASS if valid else CheckStatus.FAIL
        exit_code = 0 if valid else 4
    store.write_json("validation/review.json", report)
    store.write_json(
        "diagnostics.json", {"mode": "review", "solver_executed": False}
    )
    return exit_code, status, None, (
        "validation/review.json",
        "diagnostics.json",
    )


def _problem_spec(value: Mapping[str, Any]) -> ProblemSpec:
    return ProblemSpec(
        problem_id=str(value["problem_id"]),
        model_family=str(value["model_family"]),
        mandatory_outputs=tuple(str(item) for item in value["mandatory_outputs"]),
        required_capabilities=frozenset(
            str(item) for item in value.get("required_capabilities", ())
        ),
        assumptions=dict(value.get("assumptions", {})),
        preference_weights=dict(value.get("preference_weights", {})),
        minimum_practical_improvement=value.get("minimum_practical_improvement"),
        domain_context=_domain_context(value.get("domain_context")),
        variables=tuple(_variable_spec(item) for item in value.get("variables", ())),
        mechanisms=tuple(
            _mechanism_spec(item) for item in value.get("mechanisms", ())
        ),
        business_rules=tuple(
            _business_rule_spec(item) for item in value.get("business_rules", ())
        ),
    )


def _domain_context(value: Any) -> DomainContext | None:
    if value is None:
        return None
    if not isinstance(value, Mapping):
        raise ValueError("domain_context must be a mapping")
    return DomainContext(
        object_name=str(value["object_name"]),
        system_boundary=str(value["system_boundary"]),
        stakeholders=tuple(str(item) for item in value["stakeholders"]),
        temporal_scale=str(value["temporal_scale"]),
        spatial_scale=str(value["spatial_scale"]),
        terminology={str(key): str(item) for key, item in value.get("terminology", {}).items()},
        typical_magnitudes={
            str(key): (float(bounds[0]), float(bounds[1]))
            for key, bounds in value.get("typical_magnitudes", {}).items()
        },
        unresolved_ambiguities=tuple(
            str(item) for item in value.get("unresolved_ambiguities", ())
        ),
    )


def _variable_spec(value: Mapping[str, Any]) -> VariableSpec:
    reasonable_range = value.get("reasonable_range")
    return VariableSpec(
        name=str(value["name"]),
        symbol=str(value["symbol"]),
        definition=str(value["definition"]),
        role=VariableRole(str(value["role"])),
        data_type=str(value["data_type"]),
        unit=str(value["unit"]),
        measurement=str(value["measurement"]),
        observable=bool(value["observable"]),
        data_available=bool(value["data_available"]),
        identifiable=bool(value["identifiable"]),
        reasonable_range=(
            (float(reasonable_range[0]), float(reasonable_range[1]))
            if reasonable_range is not None
            else None
        ),
        evidence_claims=tuple(str(item) for item in value.get("evidence_claims", ())),
        evidence_status=EvidenceStatus(
            str(value.get("evidence_status", EvidenceStatus.UNVERIFIED.value))
        ),
    )


def _mechanism_spec(value: Mapping[str, Any]) -> MechanismSpec:
    return MechanismSpec(
        mechanism_id=str(value["mechanism_id"]),
        upstream_variables=tuple(str(item) for item in value["upstream_variables"]),
        downstream_variables=tuple(
            str(item) for item in value["downstream_variables"]
        ),
        kind=MechanismKind(str(value["kind"])),
        direction=str(value["direction"]),
        mathematical_relation=str(value["mathematical_relation"]),
        conditions=tuple(str(item) for item in value.get("conditions", ())),
        applicable_scale=str(value["applicable_scale"]),
        evidence_claims=tuple(str(item) for item in value.get("evidence_claims", ())),
        evidence_status=EvidenceStatus(
            str(value.get("evidence_status", EvidenceStatus.UNVERIFIED.value))
        ),
    )


def _business_rule_spec(value: Mapping[str, Any]) -> BusinessRuleSpec:
    return BusinessRuleSpec(
        rule_id=str(value["rule_id"]),
        text=str(value["text"]),
        source_type=str(value["source_type"]),
        effective_period=str(value["effective_period"]),
        region=str(value["region"]),
        organization=str(value["organization"]),
        version=str(value["version"]),
        constraint_kind=ConstraintKind(str(value["constraint_kind"])),
        formal_constraint=str(value["formal_constraint"]),
        evidence_claims=tuple(str(item) for item in value.get("evidence_claims", ())),
        evidence_status=EvidenceStatus(
            str(value.get("evidence_status", EvidenceStatus.UNVERIFIED.value))
        ),
        conflict_status=str(value.get("conflict_status", "none")),
    )


def _data_bundle(value: Mapping[str, Any]) -> DataBundle:
    return DataBundle(
        arrays=dict(value.get("arrays", {})),
        scalars=dict(value.get("scalars", {})),
        tables=dict(value.get("tables", {})),
        targets=dict(value.get("targets", {})),
        metadata=dict(value.get("metadata", {})),
    )


def _load_mapping(path: Path) -> Mapping[str, Any]:
    text = path.read_text(encoding="utf-8")
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        try:
            import yaml
        except ImportError as exc:
            raise ValueError("YAML input requires PyYAML") from exc
        value = yaml.safe_load(text)
    if not isinstance(value, Mapping):
        raise ValueError("document root must be a mapping")
    return value


def _default_output(problem_path: Path, data_path: Path | None) -> str:
    digest = hashlib.sha256(problem_path.read_bytes())
    if data_path:
        digest.update(data_path.read_bytes())
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"results/{stamp}-{digest.hexdigest()[:8]}"


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == "__main__":
    raise SystemExit(main())
