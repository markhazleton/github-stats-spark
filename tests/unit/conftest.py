"""Shared fixtures for remediation-focused unit tests."""

from datetime import datetime, timezone

import pytest
import yaml

from spark.config import SparkConfig
from spark.models.dashboard_data import DashboardRepository


@pytest.fixture
def remediation_repo_list():
    """Repository payloads covering public, private, fork, and archived cases."""
    return [
        {"name": "public-repo", "pushed_at": "2026-03-01T12:00:00+00:00"},
        {"name": "private-repo", "private": True, "pushed_at": "2026-03-01T12:00:00+00:00"},
        {"name": "fork-repo", "fork": True, "pushed_at": "2026-03-01T12:00:00+00:00"},
        {"name": "archived-repo", "archived": True, "pushed_at": "2026-03-01T12:00:00+00:00"},
    ]


@pytest.fixture(autouse=True)
def github_token_env(monkeypatch):
    """Provide a dummy GitHub token for constructor-only unit tests."""
    monkeypatch.setenv("GITHUB_TOKEN", "test-token")


@pytest.fixture
def dashboard_repositories():
    """Dashboard repositories with deterministic totals for profile tests."""
    created_at = datetime(2024, 1, 1, tzinfo=timezone.utc)
    last_commit_date = datetime(2026, 3, 1, tzinfo=timezone.utc)
    return [
        DashboardRepository(
            name="alpha",
            language="Python",
            created_at=created_at,
            last_commit_date=last_commit_date,
            commit_count=12,
            url="https://github.com/markhazleton/alpha",
            stars=7,
            forks=3,
        ),
        DashboardRepository(
            name="beta",
            language="JavaScript",
            created_at=created_at,
            last_commit_date=last_commit_date,
            commit_count=8,
            url="https://github.com/markhazleton/beta",
            stars=5,
            forks=2,
        ),
    ]


@pytest.fixture
def spark_config_factory(tmp_path):
    """Create and load SparkConfig instances for workflow/config tests."""

    def factory(theme="spark-dark", custom_themes=None):
        config_path = tmp_path / "spark.yml"
        themes_path = tmp_path / "themes.yml"

        config_data = {
            "stats": {"enabled": ["overview", "heatmap", "languages", "fun", "streaks", "release"]},
            "visualization": {"theme": theme, "effects": {"glow": True}},
            "repositories": {"exclude_forks": True, "exclude_archived": True},
            "analyzer": {},
        }
        themes_data = {"custom_themes": custom_themes or {}}

        config_path.write_text(yaml.safe_dump(config_data), encoding="utf-8")
        themes_path.write_text(yaml.safe_dump(themes_data), encoding="utf-8")

        config = SparkConfig(str(config_path))
        config.load()
        return config

    return factory