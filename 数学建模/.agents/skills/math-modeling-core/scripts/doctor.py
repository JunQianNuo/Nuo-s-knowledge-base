from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "src"))

from mathmodel.runtime import check_dependencies  # noqa: E402


PROFILES = {
    "core": {"numpy", "scipy"},
    "optimization": {"numpy", "scipy"},
    "forecasting": {"numpy", "statsmodels"},
    "ml": {"numpy", "sklearn"},
    "graph": set(),
    "all": {"numpy", "scipy", "statsmodels", "sklearn", "yaml"},
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check math-modeling-core dependencies")
    parser.add_argument("--profile", choices=tuple(PROFILES), default="core")
    arguments = parser.parse_args(argv)
    report = check_dependencies(frozenset(PROFILES[arguments.profile]))
    print(
        json.dumps(
            {
                "profile": arguments.profile,
                "installed": report.installed,
                "missing": report.missing,
                "versions": report.versions,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 3 if report.missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
