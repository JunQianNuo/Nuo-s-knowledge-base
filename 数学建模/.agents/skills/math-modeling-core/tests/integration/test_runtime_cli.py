from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

import pytest

from mathmodel.algorithms import DijkstraPlugin
from mathmodel.contracts import CheckStatus, ProblemSpec, SolveConfig
from mathmodel.runtime import PaperHandoff, RunContext, build_manifest


SKILL_ROOT = Path(__file__).resolve().parents[2]
RUNNER = SKILL_ROOT / "scripts" / "run_model.py"


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
    }

    first = build_manifest(**arguments)
    second = build_manifest(**arguments)

    assert set(first) == {
        "schema_version",
        "skill_version",
        "run_id",
        "created_at",
        "problem",
        "plugin",
        "solve_config",
        "input_hashes",
        "validation_status",
        "evidence_revision",
        "environment",
        "reproduce_command",
        "manifest_hash",
    }
    assert first == second
    assert first["manifest_hash"] == second["manifest_hash"]


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
