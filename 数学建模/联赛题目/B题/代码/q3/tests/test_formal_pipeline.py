from __future__ import annotations

import inspect
import json
import shutil
from types import SimpleNamespace

import pytest

from common.paths import CODE_ROOT, resolve_data_dir
from q3.algorithms.lex import StageCLexMaster
from q3.run_q3 import (
    _artifact,
    _budget,
    _publish_formal,
    _validated_baseline,
    _validated_stage_b,
)


def test_no_quick_baseline_or_temporary_hardcoding():
    sources = [
        (CODE_ROOT / "q3" / "run_q3.py").read_text(encoding="utf-8"),
        (CODE_ROOT / "q3" / "algorithms" / "lex.py").read_text(encoding="utf-8"),
    ]
    forbidden = ("40617", "40593", "149")
    assert not any(value in source for value in forbidden for source in sources)
    signature = inspect.signature(StageCLexMaster)
    assert signature.parameters["temporary_served"].default is inspect.Parameter.empty
    assert signature.parameters["budget"].default is inspect.Parameter.empty


def test_formal_quick_artifacts_and_default_budgets_are_separate(tmp_path):
    assert _artifact(tmp_path, "a", "routes", True).name == "stage_a_routes.csv"
    assert _artifact(tmp_path, "a", "routes", False).name == "formal_stage_a_routes.csv"
    quick = SimpleNamespace(
        quick=True,
        time_budget=None,
        stage_a_budget=None,
        stage_b_budget=None,
        stage_c_budget=None,
    )
    formal = SimpleNamespace(
        quick=False,
        time_budget=None,
        stage_a_budget=None,
        stage_b_budget=None,
        stage_c_budget=None,
    )
    assert [_budget(quick, stage) for stage in "abc"] == [240, 180, 240]
    assert [_budget(formal, stage) for stage in "abc"] == [600, 360, 360]


def _copy_parent(source_name, destination):
    shutil.copyfile(CODE_ROOT / "q3" / "outputs" / source_name, destination)


def test_formal_parent_resume_loads_values_dynamically_and_rejects_stale(tmp_path):
    data_dir = resolve_data_dir()
    for kind in ("routes", "assignments"):
        _copy_parent(f"stage_a_{kind}.csv", _artifact(tmp_path, "a", kind, False))
        _copy_parent(f"stage_b_{kind}.csv", _artifact(tmp_path, "b", kind, False))
    stage_a = json.loads(
        (CODE_ROOT / "q3" / "outputs" / "stage_a_summary.json").read_text(encoding="utf-8")
    )
    stage_a.update(mode="formal", baseline_kind="formal_best_validated_feasible")
    _artifact(tmp_path, "a", "summary", False).write_text(json.dumps(stage_a), encoding="utf-8")
    loaded_a = _validated_baseline(tmp_path, data_dir, False)
    stage_b = json.loads(
        (CODE_ROOT / "q3" / "outputs" / "stage_b_summary.json").read_text(encoding="utf-8")
    )
    stage_b.update(mode="formal", B0=loaded_a["T_air"])
    _artifact(tmp_path, "b", "summary", False).write_text(json.dumps(stage_b), encoding="utf-8")
    loaded_b = _validated_stage_b(tmp_path, data_dir, False, loaded_a)
    assert loaded_b["B0"] == loaded_a["T_air"]
    assert loaded_b["temporary_served"] > 0
    stage_b["B0"] += 1
    _artifact(tmp_path, "b", "summary", False).write_text(json.dumps(stage_b), encoding="utf-8")
    with pytest.raises(RuntimeError, match="stale"):
        _validated_stage_b(tmp_path, data_dir, False, loaded_a)


def test_official_files_not_published_before_formal_validation(tmp_path):
    invalid = SimpleNamespace(valid=False)
    with pytest.raises(RuntimeError, match="not publishable"):
        _publish_formal(tmp_path, tmp_path, 0, invalid, False)
    assert not (tmp_path / "q3-routes.csv").exists()
