from __future__ import annotations

from mathmodel.algorithms import PluginStatus, create_builtin_registry
from mathmodel.contracts import CheckStatus
from mathmodel.runtime import run_p1


EXPECTED_PLUGIN_IDS = {
    "optimization.linear-programming",
    "optimization.mixed-integer-linear-programming",
    "optimization.nonlinear",
    "graph.dijkstra",
    "graph.edmonds-karp",
    "evaluation.ahp",
    "evaluation.entropy-weight",
    "evaluation.topsis",
    "prediction.linear-regression",
    "prediction.ridge-regression",
    "prediction.arima",
    "statistics.pca",
    "prediction.random-forest",
    "mechanistic.solve-ivp",
    "simulation.monte-carlo",
}


def test_builtin_registry_contains_exactly_fifteen_stable_audited_plugins() -> None:
    registry = create_builtin_registry()

    assert {plugin.metadata.plugin_id for plugin in registry.plugins} == EXPECTED_PLUGIN_IDS
    assert len(registry.plugins) == 15
    for plugin in registry.plugins:
        metadata = plugin.metadata
        assert metadata.status is PluginStatus.STABLE
        assert metadata.content_hash
        assert metadata.capabilities
        assert metadata.model_families
        assert metadata.validation_capabilities
        assert metadata.io_contract.input_fields
        assert metadata.io_contract.output_fields
        assert metadata.io_contract.config_fields


def test_every_builtin_plugin_passes_its_known_answer_p1_case() -> None:
    reports = tuple(run_p1(plugin) for plugin in create_builtin_registry().plugins)

    failures = {
        report.plugin_id: report.reasons
        for report in reports
        if report.status is not CheckStatus.PASS
    }
    assert failures == {}
