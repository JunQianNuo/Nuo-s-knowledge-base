from __future__ import annotations

import argparse
from importlib import metadata, util
import json


PROFILES = {
    "core": {"numpy", "scipy"},
    "optimization": {"numpy", "scipy"},
    "forecasting": {"numpy", "statsmodels"},
    "ml": {"numpy", "sklearn"},
    "graph": set(),
    "all": {"numpy", "scipy", "statsmodels", "sklearn", "yaml"},
}
IMPORT_NAMES = {"sklearn": "sklearn", "yaml": "yaml"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check math-modeling-core dependencies")
    parser.add_argument("--profile", choices=tuple(PROFILES), default="core")
    arguments = parser.parse_args(argv)
    installed: list[str] = []
    missing: list[str] = []
    versions: dict[str, str] = {}
    for dependency in sorted(PROFILES[arguments.profile]):
        import_name = IMPORT_NAMES.get(dependency, dependency)
        if util.find_spec(import_name) is None:
            missing.append(dependency)
            continue
        installed.append(dependency)
        distribution = {"sklearn": "scikit-learn", "yaml": "PyYAML"}.get(
            dependency, dependency
        )
        try:
            versions[dependency] = metadata.version(distribution)
        except metadata.PackageNotFoundError:
            versions[dependency] = "unknown"
    print(
        json.dumps(
            {
                "profile": arguments.profile,
                "installed": installed,
                "missing": missing,
                "versions": versions,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 3 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
