"""Regression coverage for unified workflow theme handling."""

import pytest

from spark.cache import APICache
from spark.themes.spark_light import SparkLightTheme
from spark.unified_report_workflow import UnifiedReportWorkflow


def test_workflow_uses_configured_builtin_theme(spark_config_factory, tmp_path):
    config = spark_config_factory(theme="spark-light")

    workflow = UnifiedReportWorkflow(config, cache=APICache(cache_dir=str(tmp_path / ".cache")))

    assert isinstance(workflow.theme, SparkLightTheme)
    assert workflow.visualizer.theme is workflow.theme


def test_workflow_uses_configured_custom_theme(spark_config_factory, tmp_path):
    config = spark_config_factory(
        theme="ocean",
        custom_themes={
            "ocean": {
                "colors": {
                    "primary": "#06B6D4",
                    "accent": "#8B5CF6",
                    "background": "#0C4A6E",
                    "text": "#E0F2FE",
                    "border": "#075985",
                },
                "effects": {"glow": True, "gradient": True, "animations": False},
            }
        },
    )

    workflow = UnifiedReportWorkflow(config, cache=APICache(cache_dir=str(tmp_path / ".cache")))

    assert workflow.theme.name == "ocean"
    assert workflow.visualizer.theme.primary_color == "#06B6D4"


def test_workflow_rejects_unknown_theme(spark_config_factory, tmp_path):
    config = spark_config_factory(theme="unknown-theme", custom_themes={"ocean": {"colors": {}, "effects": {}}})

    with pytest.raises(ValueError):
        UnifiedReportWorkflow(config, cache=APICache(cache_dir=str(tmp_path / ".cache")))