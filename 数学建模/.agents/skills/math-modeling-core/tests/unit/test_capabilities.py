from __future__ import annotations

from pathlib import Path

from mathmodel.algorithms import PermissionSpec
from mathmodel.contracts import CheckStatus
from mathmodel.runtime.capabilities import CapabilityPolicy


def policy(tmp_path: Path) -> CapabilityPolicy:
    project_root = tmp_path / "project"
    run_root = project_root / "results" / "run-1"
    input_root = project_root / "inputs"
    run_root.mkdir(parents=True)
    input_root.mkdir(parents=True)
    return CapabilityPolicy(
        skill_root=tmp_path / "skill",
        project_root=project_root,
        run_root=run_root,
        input_roots=(input_root,),
    )


def test_write_inside_run_artifacts_is_allowed(tmp_path: Path) -> None:
    decision = policy(tmp_path).check_write(
        tmp_path / "project" / "results" / "run-1" / "solve" / "result.json"
    )

    assert decision.status is CheckStatus.PASS


def test_write_outside_run_artifacts_is_blocked(tmp_path: Path) -> None:
    decision = policy(tmp_path).check_write(tmp_path / "project" / "result.json")

    assert decision.status is CheckStatus.BLOCKED
    assert decision.reason == "write_outside_run_root"


def test_undeclared_network_and_subprocess_are_blocked(tmp_path: Path) -> None:
    permissions = PermissionSpec(network=False, subprocess=False)
    capability_policy = policy(tmp_path)

    assert capability_policy.check_network(permissions).status is CheckStatus.BLOCKED
    assert (
        capability_policy.check_subprocess(permissions, "highs").status
        is CheckStatus.BLOCKED
    )


def test_only_allowlisted_executable_is_allowed(tmp_path: Path) -> None:
    permissions = PermissionSpec(subprocess=True, executables=("highs",))
    capability_policy = policy(tmp_path)

    assert (
        capability_policy.check_subprocess(permissions, "highs").status
        is CheckStatus.PASS
    )
    assert (
        capability_policy.check_subprocess(permissions, "cmd.exe").status
        is CheckStatus.BLOCKED
    )
