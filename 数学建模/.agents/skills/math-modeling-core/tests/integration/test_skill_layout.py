from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys

import yaml


SKILL_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = Path(
    "C:/Users/Nuo/.codex/skills/.system/skill-creator/scripts/quick_validate.py"
)


def test_skill_validator_accepts_entrypoint() -> None:
    completed = subprocess.run(
        [sys.executable, str(VALIDATOR), str(SKILL_ROOT)],
        text=True,
        capture_output=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stdout + completed.stderr


def test_skill_links_resolve_and_mode_loading_is_progressive() -> None:
    skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", skill_text)

    assert targets
    for target in targets:
        assert (SKILL_ROOT / target).is_file(), target
    assert "Always read [workflow](references/workflow.md)." in skill_text
    expected_routes = {
        "analyze": ("domain-understanding.md", "problem-decomposition.md"),
        "solve": ("model-contract.md", "data-and-solver-engineering.md"),
        "review": ("model-contract.md", "validation-runtime.md"),
        "evidence": ("literature-evidence.md", "domain-understanding.md"),
    }
    for mode, references in expected_routes.items():
        route = next(
            line for line in skill_text.splitlines() if line.startswith(f"- `{mode}`:")
        )
        assert all(reference in route for reference in references)
        assert route.count("references/") == 2


def test_openai_metadata_allows_implicit_invocation_and_names_skill() -> None:
    metadata = yaml.safe_load(
        (SKILL_ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    )

    assert metadata["policy"]["allow_implicit_invocation"] is True
    assert "$math-modeling-core" in metadata["interface"]["default_prompt"]


def test_required_references_have_no_placeholders_or_duplicate_primary_routes() -> None:
    required = (
        "workflow.md",
        "domain-understanding.md",
        "problem-decomposition.md",
        "model-contract.md",
        "model-selection.md",
        "plugin-contract.md",
        "literature-evidence.md",
        "data-and-solver-engineering.md",
        "validation-runtime.md",
        "reproducibility.md",
        "handoffs.md",
    )
    texts = []
    for filename in required:
        path = SKILL_ROOT / "references" / filename
        assert path.is_file(), filename
        text = path.read_text(encoding="utf-8")
        assert not re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", text, re.IGNORECASE)
        texts.append(text)
    entrypoint = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert "paper prose" in entrypoint
    assert "contest orchestration" in entrypoint
    assert "math-modeling-paper" in "\n".join(texts)


def test_migration_inventory_covers_frozen_knowledge_categories() -> None:
    inventory = json.loads(
        (SKILL_ROOT / "references/migration-inventory.json").read_text(
            encoding="utf-8"
        )
    )
    cookbooks = tuple((SKILL_ROOT / "references/cookbooks").glob("*.md"))
    playbooks = tuple((SKILL_ROOT / "references/playbooks").glob("*.md"))
    notes = tuple((SKILL_ROOT / "references/algorithm-notes").glob("*.md"))

    assert len(cookbooks) == 8
    assert len(playbooks) == 12
    assert len(notes) == 7
    assert inventory["counts"] == {
        "lupynow_cookbooks": 8,
        "lupynow_playbooks": 12,
        "xiaoma_algorithm_notes": 7,
    }
    assert not tuple((SKILL_ROOT / "references").rglob("*.py"))
    assert not tuple((SKILL_ROOT / "references").rglob("*.m"))


def test_candidate_matrix_and_machine_readable_taxonomy_are_migrated() -> None:
    assert (SKILL_ROOT / "references/model-selection-matrix.md").is_file()
    taxonomy = json.loads(
        (SKILL_ROOT / "references/model-taxonomy.json").read_text(encoding="utf-8")
    )

    assert taxonomy["schema_version"] == 1
    assert len(taxonomy["problem_types"]) == 12
    assert {item["id"] for item in taxonomy["problem_types"]} == {
        "prediction_regression",
        "classification",
        "evaluation_ranking",
        "optimization_decision",
        "mechanism_physics",
        "clustering_grouping",
        "association_causality",
        "game_strategy",
        "geometry_kinematics",
        "statistical_inference_design",
        "network_graph",
        "ecosystem_environment",
    }
