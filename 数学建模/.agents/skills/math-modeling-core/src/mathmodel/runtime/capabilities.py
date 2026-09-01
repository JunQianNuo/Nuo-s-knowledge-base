from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mathmodel.algorithms import PermissionSpec
from mathmodel.contracts import CheckStatus


@dataclass(frozen=True, slots=True)
class CapabilityDecision:
    status: CheckStatus
    reason: str | None = None
    resolved_path: Path | None = None


@dataclass(frozen=True, slots=True)
class CapabilityPolicy:
    skill_root: Path
    project_root: Path
    run_root: Path
    input_roots: tuple[Path, ...] = ()

    def __post_init__(self) -> None:
        for name in ("skill_root", "project_root", "run_root"):
            object.__setattr__(self, name, Path(getattr(self, name)).resolve())
        object.__setattr__(
            self,
            "input_roots",
            tuple(Path(root).resolve() for root in self.input_roots),
        )

    def check_write(self, path: Path) -> CapabilityDecision:
        resolved = Path(path).resolve()
        if resolved.is_relative_to(self.run_root):
            return CapabilityDecision(CheckStatus.PASS, resolved_path=resolved)
        return CapabilityDecision(
            CheckStatus.BLOCKED,
            reason="write_outside_run_root",
            resolved_path=resolved,
        )

    def check_read(self, path: Path) -> CapabilityDecision:
        resolved = Path(path).resolve()
        allowed_roots = (self.skill_root, self.run_root, *self.input_roots)
        if any(resolved.is_relative_to(root) for root in allowed_roots):
            return CapabilityDecision(CheckStatus.PASS, resolved_path=resolved)
        return CapabilityDecision(
            CheckStatus.BLOCKED,
            reason="read_outside_declared_roots",
            resolved_path=resolved,
        )

    @staticmethod
    def check_network(permissions: PermissionSpec) -> CapabilityDecision:
        if permissions.network:
            return CapabilityDecision(CheckStatus.PASS)
        return CapabilityDecision(CheckStatus.BLOCKED, reason="network_not_declared")

    @staticmethod
    def check_subprocess(
        permissions: PermissionSpec, executable: str
    ) -> CapabilityDecision:
        if not permissions.subprocess:
            return CapabilityDecision(
                CheckStatus.BLOCKED, reason="subprocess_not_declared"
            )
        if executable not in permissions.executables:
            return CapabilityDecision(
                CheckStatus.BLOCKED, reason="executable_not_allowlisted"
            )
        return CapabilityDecision(CheckStatus.PASS)
