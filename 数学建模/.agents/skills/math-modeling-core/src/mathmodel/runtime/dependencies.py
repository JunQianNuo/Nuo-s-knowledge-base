from __future__ import annotations

from dataclasses import dataclass
from importlib import metadata, util


IMPORT_NAMES = {
    "scikit-learn": "sklearn",
    "pyyaml": "yaml",
}


@dataclass(frozen=True, slots=True)
class DependencyReport:
    installed: tuple[str, ...]
    missing: tuple[str, ...]
    versions: dict[str, str]


def check_dependencies(dependencies: set[str] | frozenset[str]) -> DependencyReport:
    installed: list[str] = []
    missing: list[str] = []
    versions: dict[str, str] = {}
    for dependency in sorted(dependencies):
        import_name = IMPORT_NAMES.get(dependency.casefold(), dependency)
        if util.find_spec(import_name) is None:
            missing.append(dependency)
            continue
        installed.append(dependency)
        try:
            versions[dependency] = metadata.version(dependency)
        except metadata.PackageNotFoundError:
            try:
                module = __import__(import_name)
                versions[dependency] = str(getattr(module, "__version__", "unknown"))
            except Exception:
                versions[dependency] = "unknown"
    return DependencyReport(tuple(installed), tuple(missing), versions)
