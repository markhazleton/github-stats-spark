"""Unit tests for GitHubFetcher enrichment and API-version behavior."""

from types import SimpleNamespace
from datetime import datetime, timedelta, timezone

import pytest

from spark.cache import APICache
from spark.fetcher import GitHubFetcher
from spark.time_utils import sanitize_timestamp_for_filename


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


def test_get_user_without_username_uses_authenticated_user(fetcher, monkeypatch):
    user = SimpleNamespace(
        login="markhazleton",
        name="Mark",
        bio="bio",
        avatar_url="https://example/avatar.png",
        html_url="https://github.com/markhazleton",
        public_repos=10,
        followers=5,
        following=2,
    )

    monkeypatch.setattr(fetcher.github, "get_user", lambda: user)

    profile = fetcher.get_user()

    assert profile["login"] == "markhazleton"
    assert profile["name"] == "Mark"


def test_get_user_with_username_delegates_to_fetch_user_profile(fetcher, monkeypatch):
    monkeypatch.setattr(fetcher, "fetch_user_profile", lambda username: {"username": username})

    profile = fetcher.get_user("markhazleton")

    assert profile == {"username": "markhazleton"}


def test_fetch_user_profile_reads_from_cache(fetcher):
    fetcher.cache.set("user_profile", "markhazleton", {"username": "cached"})

    profile = fetcher.fetch_user_profile("markhazleton")

    assert profile["username"] == "cached"


def test_fetch_user_profile_from_github(fetcher, monkeypatch):
    now = datetime.now(timezone.utc)
    user = SimpleNamespace(
        login="markhazleton",
        name=None,
        bio="bio",
        company="company",
        location="location",
        email="email@example.com",
        avatar_url="https://example/avatar.png",
        html_url="https://github.com/markhazleton",
        public_repos=3,
        followers=1,
        following=2,
        created_at=now,
        updated_at=now,
    )
    monkeypatch.setattr(fetcher.github, "get_user", lambda username: user)

    profile = fetcher.fetch_user_profile("markhazleton")

    assert profile["username"] == "markhazleton"
    assert profile["name"] == "markhazleton"
    assert profile["created_at"] is not None


def test_fetch_repositories_respects_max_repos(fetcher, monkeypatch):
    fetcher.max_repos = 1

    class Repo:
        def __init__(self, name):
            self.name = name
            self.full_name = f"markhazleton/{name}"
            self.description = "repo"
            self.language = "Python"
            self.stargazers_count = 1
            self.forks_count = 0
            self.watchers_count = 0
            self.size = 1
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)
            self.pushed_at = datetime.now(timezone.utc)
            self.fork = False
            self.private = False
            self.archived = False
            self.homepage = None
            self.has_pages = False

    class User:
        @staticmethod
        def get_repos():
            return [Repo("one"), Repo("two")]

    monkeypatch.setattr(fetcher.github, "get_user", lambda username: User())

    repos = fetcher.fetch_repositories("markhazleton", exclude_private=True)

    assert len(repos) == 1
    assert repos[0]["name"] == "one"


def test_fetch_commits_returns_data(fetcher, monkeypatch):
    commit = SimpleNamespace(
        sha="abc",
        commit=SimpleNamespace(
            message="msg",
            author=SimpleNamespace(name="markhazleton", date=datetime.now(timezone.utc)),
        ),
    )
    repo = SimpleNamespace(get_commits=lambda author=None: [commit])
    monkeypatch.setattr(fetcher.github, "get_repo", lambda full_name: repo)

    commits = fetcher.fetch_commits("markhazleton", "repo-one")

    assert commits[0]["sha"] == "abc"
    assert commits[0]["repo"] == "repo-one"


def test_fetch_readme_decodes_content(fetcher, monkeypatch):
    readme = SimpleNamespace(decoded_content=b"# title")
    repo = SimpleNamespace(get_readme=lambda: readme)
    monkeypatch.setattr(fetcher.github, "get_repo", lambda full_name: repo)

    content = fetcher.fetch_readme("markhazleton", "repo-one")

    assert content == "# title"


def test_fetch_dependency_files_supports_wildcard(fetcher, monkeypatch):
    root_contents = [SimpleNamespace(name="app.csproj", type="file", decoded_content=b"<Project />")]

    class Repo:
        @staticmethod
        def get_contents(path):
            if path == "":
                return root_contents
            raise RuntimeError("unexpected path")

    monkeypatch.setattr(fetcher.github, "get_repo", lambda full_name: Repo())

    files = fetcher.fetch_dependency_files("markhazleton", "repo-one")

    assert "app.csproj" in files


def test_fetch_commit_counts_computes_windows(fetcher, monkeypatch):
    now = datetime.now(timezone.utc)

    def make_commit(days_ago):
        return SimpleNamespace(commit=SimpleNamespace(author=SimpleNamespace(date=now.replace(day=max(1, now.day - days_ago)))))

    repo = SimpleNamespace(get_commits=lambda: [make_commit(1), make_commit(10), make_commit(40)])
    monkeypatch.setattr(fetcher.github, "get_repo", lambda full_name: repo)

    result = fetcher.fetch_commit_counts("markhazleton", "repo-one")

    assert result["total"] == 3
    assert result["recent_90d"] >= 1


def test_get_rate_limit_status_handles_core_and_resources(fetcher, monkeypatch):
    core_rate = SimpleNamespace(limit=5000, remaining=4999, reset=datetime.now(timezone.utc))
    monkeypatch.setattr(fetcher.github, "get_rate_limit", lambda: SimpleNamespace(core=core_rate))
    direct = fetcher.get_rate_limit_status()

    assert direct["limit"] == 5000

    resources_rate = SimpleNamespace(resources=SimpleNamespace(core=core_rate))
    monkeypatch.setattr(fetcher.github, "get_rate_limit", lambda: resources_rate)
    nested = fetcher.get_rate_limit_status()

    assert nested["remaining"] == 4999


def test_handle_rate_limit_sleeps_when_exhausted(fetcher, monkeypatch):
    class Rate:
        def __init__(self):
            self.remaining = 0
            self.reset = datetime.now() + timedelta(seconds=1)

    monkeypatch.setattr(fetcher.github, "get_rate_limit", lambda: SimpleNamespace(core=Rate()))
    sleep_calls = []
    monkeypatch.setattr("spark.fetcher.time.sleep", lambda seconds: sleep_calls.append(seconds))

    fetcher.handle_rate_limit()

    assert len(sleep_calls) == 1


def test_init_without_token_raises(tmp_path, monkeypatch):
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    cache = APICache(cache_dir=str(tmp_path / "cache-no-token"))

    with pytest.raises(ValueError, match="GitHub token required"):
        GitHubFetcher(token=None, cache=cache)


def test_fetch_commits_with_stats_returns_cached_when_cache_status_valid(fetcher, monkeypatch):
    fetcher.use_cache_status = True
    pushed_at = datetime.now(timezone.utc)
    cached_payload = [{"sha": "cached"}]

    fetcher.cache_status_tracker.get_repository_cache_status = lambda **kwargs: {
        "refresh_needed": False,
        "cache_age_hours": 1.0,
    }
    fetcher.cache.set(
        "commits_stats",
        "markhazleton",
        cached_payload,
        repo="repo-one",
        week=sanitize_timestamp_for_filename(pushed_at),
    )

    result = fetcher.fetch_commits_with_stats(
        "markhazleton",
        "repo-one",
        repo_pushed_at=pushed_at,
        force_refresh=False,
    )

    assert result == cached_payload


def test_fetch_commits_with_stats_builds_stats_payload(fetcher, monkeypatch):
    fetcher.use_cache_status = False

    commit = SimpleNamespace(
        sha="abc",
        commit=SimpleNamespace(
            author=SimpleNamespace(name="markhazleton", date=datetime.now(timezone.utc)),
            message="message",
        ),
        stats=SimpleNamespace(total=5, additions=3, deletions=2),
    )
    repo = SimpleNamespace(get_commits=lambda: [commit])
    monkeypatch.setattr(fetcher.github, "get_repo", lambda full_name: repo)

    result = fetcher.fetch_commits_with_stats("markhazleton", "repo-one", force_refresh=True)

    assert len(result) == 1
    assert result[0]["stats"]["additions"] == 3
    assert result[0]["stats"]["deletions"] == 2


def test_fetch_languages_returns_mapping(fetcher, monkeypatch):
    repo = SimpleNamespace(get_languages=lambda: {"Python": 123})
    monkeypatch.setattr(fetcher.github, "get_repo", lambda full_name: repo)

    languages = fetcher.fetch_languages("markhazleton", "repo-one")

    assert languages == {"Python": 123}


def test_fetch_pull_request_summary_marks_partial_after_page_cap(fetcher, monkeypatch):
    payload = [
        {
            "draft": False,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "requested_reviewers": [],
            "requested_teams": [],
        }
    ] * 100

    monkeypatch.setattr(fetcher, "_rest_get", lambda *args, **kwargs: FakeResponse(200, payload))

    summary = fetcher.fetch_pull_request_summary("markhazleton", "repo-one", force_refresh=True)

    assert summary["availability"] == "partial"
    assert summary["reason"] == "not_requested"
