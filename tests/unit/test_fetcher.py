"""Unit tests for GitHubFetcher enrichment and API-version behavior."""

from datetime import datetime, timezone

import pytest

from spark.cache import APICache
from spark.fetcher import GitHubFetcher


class FakeResponse:
    def __init__(self, status_code, payload=None):
        self.status_code = status_code
        self._payload = payload

    def json(self):
        return self._payload


@pytest.fixture
def fetcher(tmp_path, monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "test-token")
    cache = APICache(cache_dir=str(tmp_path / "cache"))
    return GitHubFetcher(cache=cache, api_version_settings={"enabled": True, "version": "2026-03-10"})


def test_fetch_pull_request_summary_available(fetcher, monkeypatch):
    now = datetime.now(timezone.utc)

    def fake_rest_get(path, params=None, include_version=True):
        assert path.endswith("/pulls")
        return FakeResponse(
            200,
            [
                {
                    "draft": True,
                    "created_at": (now.replace(day=max(1, now.day - 3))).isoformat(),
                    "requested_reviewers": [{"id": 1}],
                    "requested_teams": [],
                },
                {
                    "draft": False,
                    "created_at": (now.replace(day=max(1, now.day - 1))).isoformat(),
                    "requested_reviewers": [],
                    "requested_teams": [],
                },
            ],
        )

    monkeypatch.setattr(fetcher, "_rest_get", fake_rest_get)

    summary = fetcher.fetch_pull_request_summary("markhazleton", "github-stats-spark", force_refresh=True)

    assert summary["availability"] == "available"
    assert summary["reason"] == "none"
    assert summary["total_open"] == 2
    assert summary["draft_count"] == 1
    assert summary["review_requested_count"] == 1
    assert summary["has_open_pull_requests"] is True


def test_fetch_pull_request_summary_permission_denied(fetcher, monkeypatch):
    monkeypatch.setattr(fetcher, "_rest_get", lambda *args, **kwargs: FakeResponse(403, {"message": "forbidden"}))

    summary = fetcher.fetch_pull_request_summary("markhazleton", "github-stats-spark", force_refresh=True)

    assert summary["availability"] == "unavailable"
    assert summary["reason"] == "permission_denied"
    assert summary["total_open"] == 0


def test_fetch_security_summary_partial(fetcher, monkeypatch):
    responses = {
        "/repos/markhazleton/github-stats-spark": FakeResponse(
            200,
            {
                "security_and_analysis": {
                    "advanced_security": {"status": "enabled"},
                    "secret_scanning": {"status": "enabled"},
                    "secret_scanning_push_protection": {"status": "enabled"},
                }
            },
        ),
        "/repos/markhazleton/github-stats-spark/vulnerability-alerts": FakeResponse(200, None),
        "/repos/markhazleton/github-stats-spark/automated-security-fixes": FakeResponse(403, {"message": "forbidden"}),
        "/repos/markhazleton/github-stats-spark/dependabot/alerts": FakeResponse(
            200,
            [
                {"security_vulnerability": {"severity": "critical"}},
                {"security_vulnerability": {"severity": "medium"}},
            ],
        ),
    }

    def fake_rest_get(path, params=None, include_version=True):
        return responses[path]

    monkeypatch.setattr(fetcher, "_rest_get", fake_rest_get)

    summary = fetcher.fetch_security_summary("markhazleton", "github-stats-spark", force_refresh=True)

    assert summary["availability"] == "partial"
    assert summary["reason"] == "permission_denied"
    assert summary["overall_state"] == "warning_present"
    assert summary["active_alert_counts"]["total_open"] == 2
    assert summary["active_alert_counts"]["critical"] == 1
    assert summary["active_alert_counts"]["medium"] == 1


def test_fetch_security_summary_unavailable(fetcher, monkeypatch):
    monkeypatch.setattr(fetcher, "_rest_get", lambda *args, **kwargs: FakeResponse(403, {"message": "forbidden"}))

    summary = fetcher.fetch_security_summary("markhazleton", "github-stats-spark", force_refresh=True)

    assert summary["availability"] == "unavailable"
    assert summary["reason"] == "permission_denied"
    assert summary["overall_state"] == "unavailable"


def test_fetch_repositories_excludes_private(fetcher, monkeypatch):
    class Repo:
        def __init__(self, name, private):
            self.name = name
            self.full_name = f"markhazleton/{name}"
            self.description = "repo"
            self.language = "Python"
            self.stargazers_count = 1
            self.forks_count = 1
            self.watchers_count = 1
            self.size = 10
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)
            self.pushed_at = datetime.now(timezone.utc)
            self.fork = False
            self.private = private
            self.archived = False
            self.homepage = None
            self.has_pages = False

    class User:
        @staticmethod
        def get_repos():
            return [Repo("public-repo", False), Repo("private-repo", True)]

    monkeypatch.setattr(fetcher.github, "get_user", lambda username: User())

    repos = fetcher.fetch_repositories("markhazleton", exclude_private=True)

    assert [repo["name"] for repo in repos] == ["public-repo"]
