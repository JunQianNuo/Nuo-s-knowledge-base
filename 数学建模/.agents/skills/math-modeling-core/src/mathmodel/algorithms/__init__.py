from .base import (
    AlgorithmMetadata,
    AlgorithmPlugin,
    FieldSpec,
    IOContract,
    PermissionSpec,
    PluginStatus,
    SupportDecision,
    SupportStatus,
)
from .evaluation import AHPPlugin, EntropyWeightPlugin, TOPSISPlugin
from .graph import DijkstraPlugin, MaxFlowPlugin
from .loader import PluginManifest, load_plugin_manifest
from .mechanistic import ODESolverPlugin
from .optimization import (
    LinearProgrammingPlugin,
    MixedIntegerLinearProgrammingPlugin,
    NonlinearOptimizationPlugin,
)
from .prediction import (
    ARIMAPlugin,
    LinearRegressionPlugin,
    RandomForestPlugin,
    RidgeRegressionPlugin,
)
from .registry import AlgorithmRegistry, RegistryDecision
from .simulation import MonteCarloPlugin
from .statistics import PCAPlugin


def create_builtin_registry() -> AlgorithmRegistry:
    """Return the audited, versioned built-in plugin allowlist."""
    return AlgorithmRegistry(
        (
            LinearProgrammingPlugin(),
            MixedIntegerLinearProgrammingPlugin(),
            NonlinearOptimizationPlugin(),
            DijkstraPlugin(),
            MaxFlowPlugin(),
            AHPPlugin(),
            EntropyWeightPlugin(),
            TOPSISPlugin(),
            LinearRegressionPlugin(),
            RidgeRegressionPlugin(),
            ARIMAPlugin(),
            PCAPlugin(),
            RandomForestPlugin(),
            ODESolverPlugin(),
            MonteCarloPlugin(),
        )
    )

__all__ = [
    "AlgorithmMetadata",
    "AlgorithmPlugin",
    "AlgorithmRegistry",
    "AHPPlugin",
    "ARIMAPlugin",
    "DijkstraPlugin",
    "EntropyWeightPlugin",
    "FieldSpec",
    "IOContract",
    "LinearProgrammingPlugin",
    "LinearRegressionPlugin",
    "MaxFlowPlugin",
    "MonteCarloPlugin",
    "MixedIntegerLinearProgrammingPlugin",
    "NonlinearOptimizationPlugin",
    "ODESolverPlugin",
    "PCAPlugin",
    "PermissionSpec",
    "PluginStatus",
    "PluginManifest",
    "RegistryDecision",
    "RandomForestPlugin",
    "RidgeRegressionPlugin",
    "SupportDecision",
    "SupportStatus",
    "TOPSISPlugin",
    "create_builtin_registry",
    "load_plugin_manifest",
]
