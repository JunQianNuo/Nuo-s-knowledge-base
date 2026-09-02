from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

import pytest

from mathmodel.algorithms import DijkstraPlugin
from mathmodel.contracts import CheckStatus, ProblemSpec, SolveConfig
from mathmodel.evidence import EvidenceSnapshot, ProviderResponse, SearchRequest
from mathmodel.runtime import PaperHandoff, RunContext, build_manifest, verify_manifest


SKILL_ROOT = Path(__file__).resolve().parents[2]
RUNNER = SKILL_ROOT / "scripts" / "run_model.py"
DOCTOR = SKILL_ROOT / "scripts" / "doctor.py"


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def run_cli(*arguments: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(RUNNER), *arguments],
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )


def test_help_is_path_independent(tmp_path: Path) -> None:
    completed = run_cli("--help", cwd=tmp_path)

    assert completed.returncode == 0
    assert "--project-root" in completed.stdout
    assert "--mode" in completed.stdout


def test_doctor_reports_missing_core_dependencies_without_importing_them() -> None:
    completed = subprocess.run(
        [sys.executable, "-S", str(DOCTOR), "--profile", "core"],
        text=True,
        capture_output=True,
        check=False,
    )

    assert completed.returncode == 3
    report = json.loads(completed.stdout)
    assert report["missing"] == ["numpy", "scipy"]
    assert completed.stderr == ""


def test_output_must_remain_inside_absolute_project_root(tmp_path: Path) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    write_json(
        problem_path,
        {
            "problem_id": "p",
            "model_family": "shortest_path",
            "mandatory_outputs": ["path"],
        },
    )
    outside = tmp_path / "outside"

    completed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--output",
        str(outside),
    )

    assert completed.returncode == 2
    assert "output must be inside project root" in completed.stderr
    assert not outside.exists()


def test_existing_run_directory_is_never_overwritten(tmp_path: Path) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    data_path = project / "data.json"
    write_json(
        problem_path,
        {
            "problem_id": "immutable-run",
            "model_family": "shortest_path",
            "mandatory_outputs": ["path"],
        },
    )
    write_json(
        data_path,
        {
            "tables": {"graph": {"A": {"B": 1}, "B": {}}},
            "scalars": {"source": "A", "target": "B"},
        },
    )
    arguments = (
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--data",
        str(data_path),
        "--output",
        "results/immutable",
    )

    first = run_cli(*arguments)
    manifest_path = project / "results/immutable/manifest.json"
    original = manifest_path.read_bytes()
    second = run_cli(*arguments)

    assert first.returncode == 0
    assert second.returncode == 2
    assert "already exists" in second.stderr
    assert manifest_path.read_bytes() == original


def test_missing_declared_dependency_returns_exit_three(tmp_path: Path) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    write_json(
        problem_path,
        {
            "problem_id": "p",
            "model_family": "shortest_path",
            "mandatory_outputs": ["path"],
            "required_dependencies": ["definitely_missing_mathmodel_dependency"],
        },
    )
    data_path = project / "data.json"
    write_json(
        data_path,
        {
            "tables": {"graph": {"A": {"B": 1}, "B": {}}},
            "scalars": {"source": "A", "target": "B"},
        },
    )

    completed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--data",
        str(data_path),
        "--output",
        "results/missing-dependency",
    )

    assert completed.returncode == 3
    diagnostics = json.loads(
        (project / "results/missing-dependency/diagnostics.json").read_text(
            encoding="utf-8"
        )
    )
    assert diagnostics["missing_dependencies"] == [
        "definitely_missing_mathmodel_dependency"
    ]


def test_evidence_mode_does_not_execute_algorithm_or_probe_solver_dependency(
    tmp_path: Path,
) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    write_json(
        problem_path,
        {
            "problem_id": "evidence-only",
            "model_family": "shortest_path",
            "mandatory_outputs": ["domain_evidence"],
            "required_dependencies": ["definitely_missing_mathmodel_dependency"],
        },
    )

    completed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--mode",
        "evidence",
        "--output",
        "results/evidence-only",
    )

    run_root = project / "results/evidence-only"
    assert completed.returncode == 0
    assert not (run_root / "solve/result.json").exists()
    diagnostics = json.loads(
        (run_root / "diagnostics.json").read_text(encoding="utf-8")
    )
    assert diagnostics["mode"] == "evidence"
    assert diagnostics["solver_executed"] is False
    assert diagnostics["evidence_action"] == "query_plan_created"
    plan = json.loads((run_root / "evidence/query-plan.json").read_text(encoding="utf-8"))
    assert [item["phase"] for item in plan["requests"]] == [
        "E0",
        "E0",
        "E0",
        "E0",
        "E1",
    ]
    planned_text = " ".join(item["query"] for item in plan["requests"])
    assert "physical mechanism" in planned_text
    assert "business rules" in planned_text
    assert "variable definition" in planned_text
    manifest = json.loads((run_root / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["validation_status"] == "SKIPPED"
    assert manifest["mode"] == "evidence"


def test_evidence_refresh_blocks_before_network_when_initial_budget_is_exceeded(
    tmp_path: Path,
) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    requests = [
        {
            "phase": "E0",
            "query": f"query {index}",
            "provider": "not-configured",
            "page": 1,
        }
        for index in range(6)
    ]
    write_json(
        problem_path,
        {
            "problem_id": "budget",
            "model_family": "shortest_path",
            "mandatory_outputs": ["domain_evidence"],
            "evidence_requests": requests,
        },
    )

    completed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--mode",
        "evidence",
        "--refresh-evidence",
        "--output",
        "results/budget",
    )

    diagnostics = json.loads(
        (project / "results/budget/diagnostics.json").read_text(encoding="utf-8")
    )
    assert completed.returncode == 3
    assert diagnostics["reasons"] == ["initial_search_budget_exceeded"]


def test_evidence_mode_replays_verified_local_snapshot_by_default(
    tmp_path: Path,
) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    snapshot_path = project / "snapshot.json"
    search = SearchRequest(
        phase="E0", query="road traffic variable definition", provider="local-fake"
    )
    snapshot = EvidenceSnapshot.create(
        provider="local-fake",
        provider_version="v1",
        request=search,
        response=ProviderResponse(
            records=(
                {
                    "title": "Traffic Definition",
                    "authors": ["A. Author"],
                    "year": 2024,
                    "doi": "10.1000/traffic",
                    "stable_id": "t1",
                    "claims": [
                        {
                            "claim_id": "definition-1",
                            "claim_type": "definition",
                            "text": "Traffic flow is vehicles per unit time.",
                            "locator": "p. 2",
                            "applicability": ["road segment"],
                            "status": "VERIFIED",
                        }
                    ],
                },
            )
        ),
        accessed_at="2026-09-01T00:00:00Z",
    )
    snapshot_path.write_text(snapshot.to_json(), encoding="utf-8")
    write_json(
        problem_path,
        {
            "problem_id": "replay",
            "model_family": "shortest_path",
            "mandatory_outputs": ["domain_evidence"],
            "evidence_requests": [search.to_dict()],
        },
    )

    completed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--mode",
        "evidence",
        "--evidence-snapshot",
        str(snapshot_path),
        "--output",
        "results/replay",
    )

    assert completed.returncode == 0
    diagnostics = json.loads(
        (project / "results/replay/diagnostics.json").read_text(encoding="utf-8")
    )
    assert diagnostics["evidence_action"] == "snapshot_replay"
    assert diagnostics["claim_count"] == 1
    manifest = json.loads(
        (project / "results/replay/manifest.json").read_text(encoding="utf-8")
    )
    assert manifest["evidence"]["revision"]
    assert manifest["inputs"]["evidence_snapshot_0"]["sha256"]
    assert "--evidence-snapshot" in manifest["reproduce_command"]


def test_analyze_mode_audits_domain_before_algorithm_lookup(tmp_path: Path) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    write_json(
        problem_path,
        {
            "problem_id": "domain-first",
            "model_family": "not-yet-selected",
            "mandatory_outputs": ["decision"],
        },
    )

    completed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--mode",
        "analyze",
        "--output",
        "results/domain-first",
    )

    audit = json.loads(
        (project / "results/domain-first/domain/audit.json").read_text(encoding="utf-8")
    )
    assert completed.returncode == 3
    assert audit["status"] == "BLOCKED"
    assert "domain_context_missing" in audit["reasons"]
    assert not (project / "results/domain-first/solve/result.json").exists()


def test_analyze_mode_runs_seven_gate_minimum_sufficient_model_selection(
    tmp_path: Path,
) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    write_json(
        problem_path,
        {
            "problem_id": "select-model",
            "model_family": "shortest_path",
            "mandatory_outputs": ["path", "distance"],
            "domain_context": {
                "object_name": "road graph",
                "system_boundary": "declared nodes and edges",
                "stakeholders": ["traveler"],
                "temporal_scale": "static",
                "spatial_scale": "network",
                "unresolved_ambiguities": [],
            },
            "model_requirements": {
                "mandatory_capabilities": ["shortest_path"],
                "mandatory_outputs": ["path", "distance"],
                "structural_features": ["static", "nonnegative_edges"],
                "available_fields": ["edges"],
            },
            "model_candidates": [
                {
                    "candidate_id": "classic.dijkstra-model",
                    "model_family": "shortest_path",
                    "capabilities": ["shortest_path"],
                    "covered_outputs": ["path", "distance"],
                    "structural_features": ["static", "nonnegative_edges"],
                    "required_data": ["edges"],
                    "constraints_supported": True,
                    "assumptions_verified": True,
                    "identifiable": True,
                    "validation_path": True,
                    "complexity": {"time_tier": 1, "memory_tier": 1},
                },
                {
                    "candidate_id": "paper.dynamic-ant-colony",
                    "model_family": "dynamic_routing",
                    "capabilities": ["shortest_path"],
                    "covered_outputs": ["path", "distance"],
                    "structural_features": ["dynamic", "nonnegative_edges"],
                    "required_data": ["edges", "traffic_stream"],
                    "constraints_supported": True,
                    "assumptions_verified": True,
                    "identifiable": True,
                    "validation_path": True,
                    "complexity": {"additional_data_fields": 1, "time_tier": 4},
                    "evidence_count": 100,
                },
            ],
        },
    )

    completed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--mode",
        "analyze",
        "--output",
        "results/select-model",
    )

    selection = json.loads(
        (project / "results/select-model/selection/model.json").read_text(
            encoding="utf-8"
        )
    )
    assert completed.returncode == 0
    assert selection["status"] == "PASS"
    assert selection["main"]["candidate_id"] == "classic.dijkstra-model"
    assert selection["challenger"] is None
    assert "paper.dynamic-ant-colony" in selection["rejected"]


def test_review_mode_without_declared_artifact_is_blocked(tmp_path: Path) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    write_json(
        problem_path,
        {
            "problem_id": "review",
            "model_family": "shortest_path",
            "mandatory_outputs": ["path"],
        },
    )

    completed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--mode",
        "review",
        "--output",
        "results/review",
    )

    report = json.loads(
        (project / "results/review/validation/review.json").read_text(encoding="utf-8")
    )
    assert completed.returncode == 3
    assert report == {"reasons": ["review_artifact_missing"], "status": "BLOCKED"}


def test_review_mode_verifies_a_hash_bound_manifest(tmp_path: Path) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    data_path = project / "data.json"
    write_json(
        problem_path,
        {
            "problem_id": "review-source",
            "model_family": "shortest_path",
            "mandatory_outputs": ["path"],
        },
    )
    write_json(
        data_path,
        {
            "tables": {"graph": {"A": {"B": 1}, "B": {}}},
            "scalars": {"source": "A", "target": "B"},
        },
    )
    source = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--data",
        str(data_path),
        "--output",
        "results/source",
    )
    source_manifest = project / "results/source/manifest.json"

    reviewed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--mode",
        "review",
        "--review-artifact",
        str(source_manifest),
        "--output",
        "results/review-valid",
    )

    assert source.returncode == 0
    assert reviewed.returncode == 0
    report = json.loads(
        (project / "results/review-valid/validation/review.json").read_text(
            encoding="utf-8"
        )
    )
    assert report["status"] == "PASS"
    review_manifest = json.loads(
        (project / "results/review-valid/manifest.json").read_text(encoding="utf-8")
    )
    assert "--review-artifact" in review_manifest["reproduce_command"]
    assert review_manifest["inputs"]["review_artifact"]["sha256"]


def test_review_mode_detects_tampered_run_artifact(tmp_path: Path) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    data_path = project / "data.json"
    write_json(
        problem_path,
        {
            "problem_id": "tamper-source",
            "model_family": "shortest_path",
            "mandatory_outputs": ["path"],
        },
    )
    write_json(
        data_path,
        {
            "tables": {"graph": {"A": {"B": 1}, "B": {}}},
            "scalars": {"source": "A", "target": "B"},
        },
    )
    source = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--data",
        str(data_path),
        "--output",
        "results/tamper-source",
    )
    source_manifest = project / "results/tamper-source/manifest.json"
    write_json(project / "results/tamper-source/solve/result.json", {"tampered": True})

    reviewed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--mode",
        "review",
        "--review-artifact",
        str(source_manifest),
        "--output",
        "results/tamper-review",
    )

    assert source.returncode == 0
    assert reviewed.returncode == 4
    report = json.loads(
        (project / "results/tamper-review/validation/review.json").read_text(
            encoding="utf-8"
        )
    )
    assert "artifact_hash_mismatch:solve/result.json" in report["reasons"]


def test_invalid_problem_schema_returns_exit_two(tmp_path: Path) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    write_json(problem_path, {"problem_id": "missing-fields"})

    completed = run_cli(
        "--project-root", str(project), "--problem", str(problem_path)
    )

    assert completed.returncode == 2
    assert "invalid problem schema" in completed.stderr


def test_problem_schema_rejects_string_booleans(tmp_path: Path) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    write_json(
        problem_path,
        {
            "problem_id": "strict-bool",
            "model_family": "shortest_path",
            "mandatory_outputs": ["path"],
            "variables": [
                {
                    "name": "edge time",
                    "symbol": "t",
                    "definition": "edge traversal time",
                    "role": "input",
                    "data_type": "continuous",
                    "unit": "min",
                    "measurement": "sensor",
                    "observable": "false",
                    "data_available": True,
                    "identifiable": True,
                    "evidence_claims": ["claim-time"],
                    "evidence_status": "VERIFIED",
                }
            ],
        },
    )

    completed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--mode",
        "evidence",
    )

    assert completed.returncode == 2
    assert "observable must be boolean" in completed.stderr


def test_solver_failure_persists_diagnostics_and_manifest(tmp_path: Path) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    write_json(
        problem_path,
        {
            "problem_id": "unreachable",
            "model_family": "shortest_path",
            "mandatory_outputs": ["path"],
            "required_capabilities": ["shortest_path"],
        },
    )
    data_path = project / "data.json"
    write_json(
        data_path,
        {
            "tables": {"graph": {"A": {}, "B": {}}},
            "scalars": {"source": "A", "target": "B"},
        },
    )

    completed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--data",
        str(data_path),
        "--output",
        "results/unreachable",
    )

    run_root = project / "results/unreachable"
    assert completed.returncode == 4
    assert json.loads((run_root / "solve/result.json").read_text(encoding="utf-8"))[
        "status"
    ] == "FAIL"
    manifest = json.loads((run_root / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["validation_status"] == "FAIL"
    assert manifest["manifest_hash"]


def test_cli_preserves_verified_domain_and_variable_contract(tmp_path: Path) -> None:
    project = (tmp_path / "project").resolve()
    project.mkdir()
    problem_path = project / "problem.json"
    write_json(
        problem_path,
        {
            "problem_id": "domain-contract",
            "model_family": "shortest_path",
            "mandatory_outputs": ["path"],
            "required_capabilities": ["shortest_path"],
            "domain_context": {
                "object_name": "road network",
                "system_boundary": "declared nodes and edges",
                "stakeholders": ["traveler"],
                "temporal_scale": "static snapshot",
                "spatial_scale": "network",
                "terminology": {"weight": "travel time"},
                "typical_magnitudes": {"travel_time_min": [0, 120]},
                "unresolved_ambiguities": [],
            },
            "variables": [
                {
                    "name": "edge travel time",
                    "symbol": "t_ij",
                    "definition": "time to traverse a directed edge",
                    "role": "input",
                    "data_type": "continuous",
                    "unit": "min",
                    "measurement": "road sensor estimate",
                    "observable": True,
                    "data_available": True,
                    "identifiable": True,
                    "evidence_claims": ["claim-travel-time"],
                    "evidence_status": "VERIFIED",
                }
            ],
        },
    )
    data_path = project / "data.json"
    write_json(
        data_path,
        {
            "tables": {"graph": {"A": {"B": 1}, "B": {}}},
            "scalars": {"source": "A", "target": "B"},
        },
    )

    completed = run_cli(
        "--project-root",
        str(project),
        "--problem",
        str(problem_path),
        "--data",
        str(data_path),
        "--output",
        "results/domain-contract",
    )

    manifest = json.loads(
        (project / "results/domain-contract/manifest.json").read_text(encoding="utf-8")
    )
    assert completed.returncode == 0
    assert manifest["problem"]["domain_context"]["object_name"] == "road network"
    assert manifest["problem"]["variables"][0]["unit"] == "min"
    assert len(manifest["artifacts"]["selection/algorithm.json"]) == 64
    assert len(manifest["artifacts"]["selection/p1.json"]) == 64
    selection = json.loads(
        (project / "results/domain-contract/selection/algorithm.json").read_text(
            encoding="utf-8"
        )
    )
    assert selection["selected_plugin"] == "graph.dijkstra"
    assert selection["selection_source"] == "audited_builtin_registry"
    p1 = json.loads(
        (project / "results/domain-contract/selection/p1.json").read_text(
            encoding="utf-8"
        )
    )
    assert p1["status"] == "PASS"
    assert "known_answer" in p1["passed_checks"]


def test_manifest_has_literal_required_keys_and_stable_hash(tmp_path: Path) -> None:
    context = RunContext.create(
        skill_root=SKILL_ROOT,
        project_root=tmp_path.resolve(),
        output="results/run-1",
    )
    problem = ProblemSpec(
        problem_id="p",
        model_family="shortest_path",
        mandatory_outputs=("path",),
        required_capabilities={"shortest_path"},
    )
    arguments = {
        "context": context,
        "problem": problem,
        "plugin": DijkstraPlugin().metadata,
        "config": SolveConfig(seed=7),
        "input_hashes": {"problem": "abc", "data": "def"},
        "validation_status": CheckStatus.PASS,
        "evidence_revision": "evidence-1",
        "created_at": "2026-09-01T00:00:00Z",
        "mode": "solve",
        "problem_path": tmp_path / "problem.json",
        "data_path": tmp_path / "data.json",
    }

    first = build_manifest(**arguments)
    second = build_manifest(**arguments)

    assert set(first) == {
        "schema_version",
        "skill_version",
        "run_id",
        "created_at",
        "mode",
        "problem",
        "plugin",
        "solve_config",
        "input_hashes",
        "validation_status",
        "evidence_revision",
        "evidence",
        "selection",
        "evaluation_protocol",
        "environment",
        "inputs",
        "artifacts",
        "reproduce_command",
        "manifest_hash",
    }
    assert first == second
    assert first["manifest_hash"] == second["manifest_hash"]
    assert first["evidence"] == {"refreshed": False, "revision": "evidence-1"}
    assert first["selection"]["algorithm_plugin_id"] == "graph.dijkstra"
    assert verify_manifest(first) is True
    tampered = dict(first)
    tampered["validation_status"] = "FAIL"
    assert verify_manifest(tampered) is False
    assert '--problem "' in first["reproduce_command"]
    assert '--data "' in first["reproduce_command"]
    assert '--mode "solve"' in first["reproduce_command"]


def test_warn_handoff_preserves_visible_warning() -> None:
    handoff = PaperHandoff.create(
        manifest_hash="manifest",
        validation_status=CheckStatus.WARN,
        payload={"result": 1},
        warnings=("sensitivity threshold is marginal",),
    )

    assert handoff.validation_status is CheckStatus.WARN
    assert handoff.warnings == ("sensitivity threshold is marginal",)
    assert handoff.final_result is True


@pytest.mark.parametrize("status", [CheckStatus.FAIL, CheckStatus.BLOCKED])
def test_failed_or_blocked_result_cannot_make_final_handoff(
    status: CheckStatus,
) -> None:
    with pytest.raises(ValueError, match="cannot create final-result handoff"):
        PaperHandoff.create(
            manifest_hash="manifest",
            validation_status=status,
            payload={"result": 1},
        )
