"""Filesystem contract for promoting the enhanced solver skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


VAULT_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = VAULT_ROOT / ".agents" / "skills"
ACTIVE_ROOT = SKILLS_ROOT / "math-modeling-solver"
COPY_ROOT = SKILLS_ROOT / "math-modeling-solver-copy"
DISABLED_ROOT = VAULT_ROOT / ".agents" / "disabled-skills" / "math-modeling-solver-legacy"

failures: list[str] = []


def read(path: Path) -> str:
    if not path.is_file():
        failures.append(f"missing file: {path.relative_to(VAULT_ROOT)}")
        return ""
    return path.read_text(encoding="utf-8-sig")


# The active discovery path contains only the enhanced skill under the official name.
active = read(ACTIVE_ROOT / "skill.md")
match = re.search(r"\A---\s*\nname:\s*([^\n]+)", active)
if not match or match.group(1).strip() != "math-modeling-solver":
    failures.append("active skill frontmatter name is not math-modeling-solver")
if not (ACTIVE_ROOT / "references" / "data-audit-and-baseline.md").is_file():
    failures.append("active skill is missing the training-enhanced references")
if COPY_ROOT.exists():
    failures.append("copy discovery directory still exists")

# The legacy skill remains recoverable, but outside the skills discovery directory.
legacy = read(DISABLED_ROOT / "skill.md")
if not legacy:
    failures.append("legacy skill was not preserved in the disabled archive")
try:
    DISABLED_ROOT.relative_to(SKILLS_ROOT)
except ValueError:
    pass
else:
    failures.append("disabled archive remains under .agents/skills and may be discovered")

if failures:
    print(f"FAIL: {len(failures)} promotion contract violation(s)")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("PASS: enhanced solver is active and legacy solver is archived outside discovery")
