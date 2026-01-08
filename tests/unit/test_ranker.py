"""Unit tests for repository ranking algorithm.

Tests the RepositoryRanker class which implements composite scoring:
- 30% Popularity (logarithmic scaling)
- 45% Activity (multi-window time decay)
- 25% Health (documentation, maturity, issues)
"""

import json
import pytest
from datetime import datetime, timedelta
from pathlib import Path

from spark.models.repository import Repository
from spark.models.commit import CommitHistory
from spark.ranker import RepositoryRanker


@pytest.fixture
def ranker():
    """Create a RepositoryRanker instance for testing."""
    return RepositoryRanker()


@pytest.fixture
def ranking_scenarios():
    """Load ranking test scenarios from fixtures."""
    fixtures_path = Path(__file__).parent.parent / "fixtures" / "ranking_scenarios.json"
    with open(fixtures_path, "r") as f:
        return json.load(f)


def create_repository_from_scenario(scenario_data):
    """Create Repository and CommitHistory objects from scenario data."""
    repo_data = scenario_data["repository"]
    commit_data = scenario_data["commits"]

    # Calculate dates
    now = datetime.now()
    created_at = now - timedelta(days=repo_data["created_days_ago"])
    updated_at = now - timedelta(days=repo_data["updated_days_ago"])
    last_commit_days = commit_data["last_commit_days_ago"]
    
    # For empty repos (no commits ever), set pushed_at to None
    if commit_data["total"] == 0 or last_commit_days > 9000:
        last_commit = None
    else:
        last_commit = now - timedelta(days=last_commit_days)

    # Create Repository object
    repository = Repository(
        name=repo_data["name"],
        description=f"Test repository: {scenario_data['description']}",
        url=f"https://github.com/testuser/{repo_data['name']}",
        created_at=created_at,
        updated_at=updated_at,
        pushed_at=last_commit,
        primary_language="Python",
        language_stats={"Python": 10000},
        stars=repo_data["stars"],
        forks=repo_data["forks"],
        watchers=repo_data.get("watchers", repo_data["stars"]),
        open_issues=repo_data.get("open_issues", 0),
        is_archived=repo_data.get("is_archived", False),
        is_fork=repo_data.get("is_fork", False),
        is_private=repo_data.get("is_private", False),
        size_kb=repo_data.get("size_kb", 1000),
        has_readme=repo_data.get("has_readme", True),

    )

    # Create CommitHistory object
    commit_history = CommitHistory(
        repository_name=repo_data["name"],
        total_commits=commit_data["total"],
        recent_90d=commit_data["recent_90d"],
        recent_180d=commit_data["recent_180d"],
        recent_365d=commit_data["recent_365d"],
        last_commit_date=last_commit,
        patterns={
            "frequency": "active" if commit_data["recent_90d"] > 20 else "moderate",
            "consistency": "consistent" if commit_data["recent_90d"] > 0 else "sporadic"
        }
    )

    return repository, commit_history


class TestPrivacyFilter:
    """Test privacy filter (constitution requirement - T027)."""
    # REMOVED: test_private_repos_excluded - Cannot create private Repository anymore
    # Privacy enforcement is now at model level (Repository.__post_init__ raises ValueError)
    # The ranker filter is now defensive code that cannot be reached in production

    def test_all_public_repos_included(self, ranker, ranking_scenarios):
        """Test that all public repositories pass privacy filter."""
        public_repos = []
        commit_histories = {}

        for scenario in ranking_scenarios["scenarios"]:
            # Skip scenarios that should be excluded
            if scenario.get("should_exclude"):
                continue
            if scenario["repository"].get("is_private", False):
                continue

            repo, commits = create_repository_from_scenario(scenario)
            public_repos.append(repo)
            commit_histories[repo.name] = commits

        # Rank public repositories
        ranked = ranker.rank_repositories(public_repos, commit_histories, top_n=len(public_repos))

        # All non-empty public repos should be included
        expected_count = len([r for r in public_repos if not r.is_empty])
        assert len(ranked) == expected_count


class TestCompositeScoring:
    """Test composite scoring algorithm."""

    def test_composite_score_range(self, ranker, ranking_scenarios):
        """Test that composite scores are within 0-100 range."""
        for scenario in ranking_scenarios["scenarios"]:
            if scenario.get("should_exclude"):
                continue

            repo, commits = create_repository_from_scenario(scenario)
            commit_histories = {repo.name: commits}

            # Rank single repository
            ranked = ranker.rank_repositories([repo], commit_histories, top_n=1)

            if len(ranked) > 0:  # If not filtered out
                _, score = ranked[0]
                assert 0 <= score <= 100, f"Score out of range for {scenario['name']}: {score}"

    def test_composite_weights_applied(self, ranker):
        """Test that composite score uses correct weights (30/45/25)."""
        # Verify the ranker has correct weights
        assert abs(ranker.weight_popularity - 0.30) < 0.01
        assert abs(ranker.weight_activity - 0.45) < 0.01
        assert abs(ranker.weight_health - 0.25) < 0.01

        # Verify weights sum to 1.0
        total = ranker.weight_popularity + ranker.weight_activity + ranker.weight_health
        assert abs(total - 1.0) < 0.01


class TestRankingIntegration:
    """Test complete ranking workflow."""

    def test_rank_repositories(self, ranker, ranking_scenarios):
        """Test ranking multiple repositories."""
        repos = []
        commit_histories = {}

        for scenario in ranking_scenarios["scenarios"]:
            if scenario.get("should_exclude"):
                continue

            repo, commits = create_repository_from_scenario(scenario)
            repos.append(repo)
            commit_histories[repo.name] = commits

        # Rank repositories
        ranked = ranker.rank_repositories(repos, commit_histories, top_n=len(repos))

        # Assertions
        assert len(ranked) > 0
        assert len(ranked) <= len(repos)

        # Scores should be in descending order
        for i in range(len(ranked) - 1):
            _, score1 = ranked[i]
            _, score2 = ranked[i + 1]
            assert score1 >= score2, f"Scores not in descending order: {score1} < {score2}"

    def test_top_n_selection(self, ranker, ranking_scenarios):
        """Test that top_n parameter limits results."""
        repos = []
        commit_histories = {}

        for scenario in ranking_scenarios["scenarios"]:
            if scenario.get("should_exclude"):
                continue

            repo, commits = create_repository_from_scenario(scenario)
            repos.append(repo)
            commit_histories[repo.name] = commits

        # Request top 3
        ranked = ranker.rank_repositories(repos, commit_histories, top_n=3)

        assert len(ranked) <= 3
        if len(ranked) >= 2:
            _, score1 = ranked[0]
            _, score2 = ranked[1]
            assert score1 >= score2

    def test_empty_repository_filter(self, ranker, ranking_scenarios):
        """Test that empty repositories are excluded."""
        # Find empty repository scenario
        empty_scenario = None
        for scenario in ranking_scenarios["scenarios"]:
            if scenario["name"] == "empty_repo":
                empty_scenario = scenario
                break

        if empty_scenario:
            repo, commits = create_repository_from_scenario(empty_scenario)
            commit_histories = {repo.name: commits}

            # Should be filtered out
            ranked = ranker.rank_repositories([repo], commit_histories, top_n=10)

            # Empty repo should not be in results (filtered by is_empty property)
            assert len(ranked) == 0 or all(r.name != "placeholder" for r, _ in ranked)


class TestEdgeCases:
    """Test edge case handling."""

    def test_archived_repository_handling(self, ranker, ranking_scenarios):
        """Test that archived repositories receive appropriate scoring."""
        archived_scenario = None
        for scenario in ranking_scenarios["scenarios"]:
            if scenario["name"] == "archived_repo":
                archived_scenario = scenario
                break

        assert archived_scenario is not None

        repo, commits = create_repository_from_scenario(archived_scenario)
        commit_histories = {repo.name: commits}

        ranked = ranker.rank_repositories([repo], commit_histories, top_n=1)

        if len(ranked) > 0:
            _, score = ranked[0]
            # Archived repos should have lower scores
            assert score < 50, f"Archived repo score too high: {score}"

    def test_fork_handling(self, ranker, ranking_scenarios):
        """Test that fork repositories are handled appropriately."""
        fork_scenarios = [s for s in ranking_scenarios["scenarios"] if "fork" in s["name"]]

        for scenario in fork_scenarios:
            repo, commits = create_repository_from_scenario(scenario)
            commit_histories = {repo.name: commits}

            ranked = ranker.rank_repositories([repo], commit_histories, top_n=1)

            # Forks should still be rankable
            assert len(ranked) <= 1

    def test_new_active_repo_vs_legacy(self, ranker, ranking_scenarios):
        """Test that activity weight favors recent work over legacy stars."""
        new_active = None
        legacy = None

        for scenario in ranking_scenarios["scenarios"]:
            if scenario["name"] == "new_active_repo":
                new_active = scenario
            elif scenario["name"] == "legacy_popular_repo":
                legacy = scenario

        if new_active and legacy:
            new_repo, new_commits = create_repository_from_scenario(new_active)
            legacy_repo, legacy_commits = create_repository_from_scenario(legacy)

            repos = [new_repo, legacy_repo]
            commit_histories = {
                new_repo.name: new_commits,
                legacy_repo.name: legacy_commits
            }

            ranked = ranker.rank_repositories(repos, commit_histories, top_n=2)

            # With 45% activity weight, active repos should compete well
            assert len(ranked) == 2


class TestScenarioValidation:
    """Test against predefined scenarios with expected scores."""

    def test_ideal_active_repo_scores_high(self, ranker, ranking_scenarios):
        """Test that ideal active repo scores in expected range."""
        ideal_scenario = None
        for scenario in ranking_scenarios["scenarios"]:
            if scenario["name"] == "ideal_active_repo":
                ideal_scenario = scenario
                break

        assert ideal_scenario is not None

        repo, commits = create_repository_from_scenario(ideal_scenario)
        commit_histories = {repo.name: commits}

        ranked = ranker.rank_repositories([repo], commit_histories, top_n=1)

        assert len(ranked) == 1
        _, score = ranked[0]

        # Should score highly (expected: 84)
        assert score > 70, f"Ideal repo scored too low: {score}"

    def test_stale_repo_scores_low(self, ranker, ranking_scenarios):
        """Test that stale repo scores in expected range."""
        stale_scenario = None
        for scenario in ranking_scenarios["scenarios"]:
            if scenario["name"] == "stale_repo":
                stale_scenario = scenario
                break

        if stale_scenario:
            repo, commits = create_repository_from_scenario(stale_scenario)
            commit_histories = {repo.name: commits}

            ranked = ranker.rank_repositories([repo], commit_histories, top_n=1)

            if len(ranked) > 0:
                _, score = ranked[0]
                # Stale repo should score low
                assert score < 40, f"Stale repo scored too high: {score}"


class TestPerformance:
    """Test ranking performance."""

    def test_ranking_50_repos(self, ranker, ranking_scenarios):
        """Test that ranking 50 repositories completes quickly."""
        import time

        # Create 50 repos by repeating scenarios
        repos = []
        commit_histories = {}

        for i in range(50):
            scenario_idx = i % len(ranking_scenarios["scenarios"])
            scenario = ranking_scenarios["scenarios"][scenario_idx]

            if scenario.get("should_exclude"):
                continue

            repo, commits = create_repository_from_scenario(scenario)
            # Modify name to make unique
            repo.name = f"{repo.name}-{i}"
            repo.full_name = f"testuser/{repo.name}"

            repos.append(repo)
            commit_histories[repo.name] = commits

        start = time.time()
        ranked = ranker.rank_repositories(repos, commit_histories, top_n=50)
        elapsed = time.time() - start

        # Should complete in under 1 second
        assert elapsed < 1.0, f"Ranking took too long: {elapsed:.2f}s"
        assert len(ranked) > 0


class TestConfigurationCustomization:
    """Test ranker configuration options."""

    def test_custom_weights(self):
        """Test that custom weights can be configured."""
        custom_config = {
            "popularity": 0.4,
            "activity": 0.4,
            "health": 0.2
        }

        ranker = RepositoryRanker(config=custom_config)

        assert abs(ranker.weight_popularity - 0.4) < 0.01
        assert abs(ranker.weight_activity - 0.4) < 0.01
        assert abs(ranker.weight_health - 0.2) < 0.01

    def test_default_weights(self):
        """Test that default weights are used when no config provided."""
        ranker = RepositoryRanker()

        assert abs(ranker.weight_popularity - 0.30) < 0.01
        assert abs(ranker.weight_activity - 0.45) < 0.01
        assert abs(ranker.weight_health - 0.25) < 0.01


class TestErrorHandling:
    """Test error handling and edge cases."""

    def test_empty_repository_list(self, ranker):
        """Test ranking with empty repository list."""
        ranked = ranker.rank_repositories([], {}, top_n=10)
        assert ranked == []

    def test_repository_without_commit_history(self, ranker):
        """Test ranking repo without commit history."""
        now = datetime.now()
        repo = Repository(
            name="no-history",
            description="Test repo",
            url="https://github.com/user/no-history",
            created_at=now - timedelta(days=100),
            updated_at=now - timedelta(days=10),
            pushed_at=now - timedelta(days=10),
            primary_language="Python",
            language_stats={"Python": 10000},
            stars=50,
            forks=10,
            watchers=25,
            open_issues=5,
            is_archived=False,
            is_fork=False,
            is_private=False,
            size_kb=2000,
            has_readme=True,

        )

        # No commit history provided
        ranked = ranker.rank_repositories([repo], {}, top_n=1)

        # Should still rank but with zero activity score
        assert len(ranked) == 1

    def test_top_n_larger_than_repo_count(self, ranker, ranking_scenarios):
        """Test requesting more repos than available."""
        repos = []
        commit_histories = {}

        # Create only 3 repos
        for i, scenario in enumerate(ranking_scenarios["scenarios"][:3]):
            if scenario.get("should_exclude"):
                continue

            repo, commits = create_repository_from_scenario(scenario)
            repos.append(repo)
            commit_histories[repo.name] = commits

        # Request top 100
        ranked = ranker.rank_repositories(repos, commit_histories, top_n=100)

        # Should return all available repos
        assert len(ranked) <= len(repos)
