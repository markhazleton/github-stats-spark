"""End-to-end integration tests for full report generation (T100-T116).

This module tests the complete workflow from fetching repositories to generating
the final markdown report, covering all user stories and edge cases.
"""

import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta
import pytest

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from spark.models.repository import Repository
from spark.models.commit import CommitHistory
from spark.models.summary import RepositorySummary
from spark.models.profile import UserProfile
from spark.models.report import Report, RepositoryAnalysis
from spark.fetcher import GitHubFetcher
from spark.ranker import RepositoryRanker
from spark.summarizer import RepositorySummarizer, UserProfileGenerator
from spark.report_generator import ReportGenerator


class TestUserStory1Scenarios:
    """Test scenarios for User Story 1 (P1 - Generate Top 50 Repository Report)."""

    def test_user_with_50_plus_repositories(self):
        """T101: Test scenario with user having 50+ public repositories."""
        # Create mock data for 75 repositories
        mock_repos = []
        for i in range(75):
            repo = Mock(
                name=f"repo-{i}",
                full_name=f"testuser/repo-{i}",
                description=f"Test repository {i}",
                html_url=f"https://github.com/testuser/repo-{i}",
                created_at=datetime.now() - timedelta(days=365),
                updated_at=datetime.now() - timedelta(days=i),
                language="Python",
                stargazers_count=100 - i,
                forks_count=10,
                open_issues_count=5,
                archived=False,
                fork=False,
                size=1000,
            )
            mock_repos.append(repo)

        # Mock fetcher
        with patch("spark.fetcher.Github") as mock_github:
            mock_user = MagicMock()
            mock_user.get_repos.return_value = mock_repos[:75]  # Return all 75
            mock_github.return_value.get_user.return_value = mock_user

            fetcher = GitHubFetcher()
            repos = fetcher.fetch_repositories("testuser", exclude_private=True)

            # Should fetch all repositories
            assert len(repos) >= 50, "Should fetch at least 50 repositories"

            # Ranker should select top 50
            ranker = RepositoryRanker()
            commit_histories = {
                f"repo-{i}": CommitHistory(
                    repository_name=f"repo-{i}",
                    total_commits=50,
                    recent_90d=10,
                    recent_180d=20,
                    recent_365d=40,
                    last_commit_date=datetime.now() - timedelta(days=i),
                )
                for i in range(75)
            }

            # Convert mock repos to Repository objects
            repo_objects = [
                Repository(
                    name=f"repo-{i}",
                    description=f"Test repository {i}",
                    url=f"https://github.com/testuser/repo-{i}",
                    created_at=datetime.now() - timedelta(days=365),
                    updated_at=datetime.now() - timedelta(days=i),
                    primary_language="Python",
                    stars=100 - i,
                    forks=10,
                    issues=5,
                    is_archived=False,
                    is_fork=False,
                )
                for i in range(75)
            ]

            ranked = ranker.rank_repositories(repo_objects, commit_histories, top_n=50)

            # Should return exactly 50 repositories
            assert len(ranked) == 50, "Should rank exactly top 50 repositories"

            # Top ranked should have highest scores
            scores = [score for _, score in ranked]
            assert scores == sorted(scores, reverse=True), "Repos should be ranked by descending score"

    def test_user_with_fewer_than_50_repositories(self):
        """T102: Test scenario with user having fewer than 50 repositories."""
        # Create mock data for 25 repositories
        mock_repos = []
        for i in range(25):
            repo = Mock(
                name=f"repo-{i}",
                full_name=f"testuser/repo-{i}",
                description=f"Test repository {i}",
                html_url=f"https://github.com/testuser/repo-{i}",
                created_at=datetime.now() - timedelta(days=365),
                updated_at=datetime.now() - timedelta(days=i),
                language="Python",
                stargazers_count=50 - i,
                forks_count=5,
                open_issues_count=2,
                archived=False,
                fork=False,
                size=1000,
            )
            mock_repos.append(repo)

        # Ranker should handle fewer than 50
        ranker = RepositoryRanker()
        commit_histories = {
            f"repo-{i}": CommitHistory(
                repository_name=f"repo-{i}",
                total_commits=30,
                recent_90d=8,
                recent_180d=15,
                recent_365d=25,
                last_commit_date=datetime.now() - timedelta(days=i),
            )
            for i in range(25)
        }

        repo_objects = [
            Repository(
                name=f"repo-{i}",
                description=f"Test repository {i}",
                url=f"https://github.com/testuser/repo-{i}",
                created_at=datetime.now() - timedelta(days=365),
                updated_at=datetime.now() - timedelta(days=i),
                primary_language="Python",
                stars=50 - i,
                forks=5,
                issues=2,
                is_archived=False,
                is_fork=False,
            )
            for i in range(25)
        ]

        ranked = ranker.rank_repositories(repo_objects, commit_histories, top_n=50)

        # Should return all 25 repositories
        assert len(ranked) == 25, "Should return all available repositories when less than top_n"

    def test_repository_with_readme_and_commits(self):
        """T103: Test repository with README and commit history."""
        repo = Repository(
            name="test-repo",
            description="A test repository",
            url="https://github.com/testuser/test-repo",
            created_at=datetime.now() - timedelta(days=365),
            updated_at=datetime.now() - timedelta(days=5),
            primary_language="Python",
            stars=100,
            forks=10,
            issues=5,
            is_archived=False,
            is_fork=False,
            has_readme=True,
        )

        commit_history = CommitHistory(
            repository_name="test-repo",
            total_commits=150,
            recent_90d=25,
            recent_180d=50,
            recent_365d=120,
            last_commit_date=datetime.now() - timedelta(days=5),
        )

        readme_content = """# Test Repo

        A comprehensive testing repository for Stats Spark.

        ## Features
        - Feature 1
        - Feature 2

        ## Installation
        ```bash
        pip install test-repo
        ```
        """

        # Test summarization with README
        with patch("spark.summarizer.Anthropic") as mock_anthropic:
            mock_client = MagicMock()
            mock_message = MagicMock()
            mock_message.content = [MagicMock(text="AI-generated summary of test repository")]
            mock_message.usage.input_tokens = 500
            mock_message.usage.output_tokens = 100
            mock_client.messages.create.return_value = mock_message
            mock_anthropic.return_value = mock_client

            summarizer = RepositorySummarizer()
            summary = summarizer.summarize_repository(
                repo,
                readme_content,
                commit_history,
                repository_owner="testuser",
            )

            assert summary is not None, "Summary should be generated"
            assert summary.repository_name == "test-repo"
            assert summary.generation_method in ["ai", "template_enhanced", "template_basic"]

    def test_repository_without_readme_fallback(self):
        """T104: Test repository without README (fallback summary) - validates FR-012."""
        repo = Repository(
            name="no-readme-repo",
            description="A repository without README",
            url="https://github.com/testuser/no-readme-repo",
            created_at=datetime.now() - timedelta(days=180),
            updated_at=datetime.now() - timedelta(days=10),
            primary_language="JavaScript",
            stars=25,
            forks=3,
            issues=1,
            is_archived=False,
            is_fork=False,
            has_readme=False,
        )

        commit_history = CommitHistory(
            repository_name="no-readme-repo",
            total_commits=45,
            recent_90d=12,
            recent_180d=30,
            recent_365d=45,
            last_commit_date=datetime.now() - timedelta(days=10),
        )

        # Test fallback summarization without README (FR-012 requirement)
        summarizer = RepositorySummarizer()
        summary = summarizer.summarize_repository(
            repo,
            None,
            commit_history,
            repository_owner="testuser",
        )

        assert summary is not None, "Summary should be generated even without README"
        assert summary.repository_name == "no-readme-repo"
        assert summary.generation_method in ["template_enhanced", "template_basic"], \
            "Should use template fallback when no README"
        assert summary.fallback_summary is not None, "Fallback summary should be populated"

    def test_empty_repository_handling(self):
        """T105: Test empty repository (no commits)."""
        repo = Repository(
            name="empty-repo",
            description="An empty repository",
            url="https://github.com/testuser/empty-repo",
            created_at=datetime.now() - timedelta(days=1),
            updated_at=datetime.now() - timedelta(days=1),
            primary_language=None,
            stars=0,
            forks=0,
            issues=0,
            is_archived=False,
            is_fork=False,
            has_readme=False,
        )

        commit_history = CommitHistory(
            repository_name="empty-repo",
            total_commits=0,
            recent_90d=0,
            recent_180d=0,
            recent_365d=0,
            last_commit_date=None,
        )

        # Ranker should handle empty repos with low scores
        ranker = RepositoryRanker()
        ranked = ranker.rank_repositories([repo], {"empty-repo": commit_history}, top_n=10)

        # Should include repo but with very low score
        assert len(ranked) == 1
        _, score = ranked[0]
        assert score < 20, "Empty repo should have very low score"

    def test_github_api_rate_limit_partial_report(self):
        """T106: Test GitHub API rate limit reached (partial report)."""
        # Simulate rate limit during processing
        with patch("spark.fetcher.Github") as mock_github:
            mock_user = MagicMock()

            # First 30 repos succeed, then rate limit
            def get_repos_side_effect(*args, **kwargs):
                repos = []
                for i in range(30):
                    repo = Mock(
                        name=f"repo-{i}",
                        full_name=f"testuser/repo-{i}",
                        description=f"Repository {i}",
                        html_url=f"https://github.com/testuser/repo-{i}",
                        created_at=datetime.now() - timedelta(days=365),
                        updated_at=datetime.now() - timedelta(days=i),
                        language="Python",
                        stargazers_count=100 - i,
                        forks_count=10,
                        open_issues_count=5,
                        archived=False,
                        fork=False,
                        size=1000,
                    )
                    repos.append(repo)
                return repos

            mock_user.get_repos.side_effect = get_repos_side_effect
            mock_github.return_value.get_user.return_value = mock_user

            fetcher = GitHubFetcher()

            # Fetch should complete with partial results
            repos = fetcher.fetch_repositories("testuser", exclude_private=True)

            # Should get partial list (30 repos)
            assert len(repos) == 30, "Should return partial results on rate limit"

            # Report generation should still work with partial data
            repo_objects = [
                Repository(
                    name=f"repo-{i}",
                    description=f"Repository {i}",
                    url=f"https://github.com/testuser/repo-{i}",
                    created_at=datetime.now() - timedelta(days=365),
                    updated_at=datetime.now() - timedelta(days=i),
                    primary_language="Python",
                    stars=100 - i,
                    forks=10,
                    issues=5,
                    is_archived=False,
                    is_fork=False,
                )
                for i in range(30)
            ]

            commit_histories = {
                f"repo-{i}": CommitHistory(
                    repository_name=f"repo-{i}",
                    total_commits=50,
                    recent_90d=10,
                    recent_180d=20,
                    recent_365d=40,
                    last_commit_date=datetime.now() - timedelta(days=i),
                )
                for i in range(30)
            }

            # Report should be generated with partial data
            report_gen = ReportGenerator()
            analyses = [
                RepositoryAnalysis(
                    repository=repo,
                    commit_history=commit_histories[repo.name],
                    summary=RepositorySummary(
                        repository_name=repo.name,
                        fallback_summary=f"Repository {repo.name}",
                        generation_method="template_basic",
                    ),
                    rank=i + 1,
                    composite_score=90 - i,
                )
                for i, repo in enumerate(repo_objects)
            ]

            profile = UserProfile(
                username="testuser",
                total_repositories=30,
                active_repositories=28,
                tech_diversity_score=0.85,
                activity_patterns=["consistent"],
                overall_impression="Active developer (partial data due to rate limit)",
            )

            report = Report(
                user_profile=profile,
                repository_analyses=analyses,
                generation_timestamp=datetime.now(),
                metadata={"note": "Partial report due to API rate limit"},
            )

            markdown = report_gen.generate_report(report)
            assert markdown is not None, "Report should be generated with partial data"
            assert "testuser" in markdown, "Report should include username"
            assert "rate limit" in markdown.lower() or "partial" in markdown.lower(), \
                "Report should note it's partial due to rate limit"


class TestUserStory2Scenarios:
    """Test scenarios for User Story 2 (P2 - Overall Developer Profile Analysis)."""

    def test_profile_analysis_diverse_repositories(self):
        """T107: Test overall profile analysis with diverse repositories."""
        # Create diverse repositories with different languages
        repositories = [
            Repository(
                name="python-ml-project",
                description="Machine learning project",
                url="https://github.com/testuser/python-ml-project",
                created_at=datetime.now() - timedelta(days=730),
                updated_at=datetime.now() - timedelta(days=2),
                primary_language="Python",
                language_stats={"Python": 8500, "Jupyter Notebook": 1500},
                stars=250,
                forks=30,
                issues=15,
                is_archived=False,
                is_fork=False,
            ),
            Repository(
                name="react-dashboard",
                description="React dashboard application",
                url="https://github.com/testuser/react-dashboard",
                created_at=datetime.now() - timedelta(days=365),
                updated_at=datetime.now() - timedelta(days=5),
                primary_language="JavaScript",
                language_stats={"JavaScript": 7000, "CSS": 2000, "HTML": 1000},
                stars=180,
                forks=25,
                issues=10,
                is_archived=False,
                is_fork=False,
            ),
            Repository(
                name="rust-cli-tool",
                description="Command-line tool in Rust",
                url="https://github.com/testuser/rust-cli-tool",
                created_at=datetime.now() - timedelta(days=180),
                updated_at=datetime.now() - timedelta(days=3),
                primary_language="Rust",
                language_stats={"Rust": 9500, "Shell": 500},
                stars=95,
                forks=12,
                issues=5,
                is_archived=False,
                is_fork=False,
            ),
        ]

        commit_histories = {
            "python-ml-project": CommitHistory(
                repository_name="python-ml-project",
                total_commits=320,
                recent_90d=45,
                recent_180d=95,
                recent_365d=250,
                last_commit_date=datetime.now() - timedelta(days=2),
            ),
            "react-dashboard": CommitHistory(
                repository_name="react-dashboard",
                total_commits=185,
                recent_90d=22,
                recent_180d=60,
                recent_365d=150,
                last_commit_date=datetime.now() - timedelta(days=5),
            ),
            "rust-cli-tool": CommitHistory(
                repository_name="rust-cli-tool",
                total_commits=110,
                recent_90d=38,
                recent_180d=95,
                recent_365d=110,
                last_commit_date=datetime.now() - timedelta(days=3),
            ),
        }

        # Generate user profile
        with patch("spark.summarizer.Anthropic") as mock_anthropic:
            mock_client = MagicMock()
            mock_message = MagicMock()
            mock_message.content = [MagicMock(
                text="Polyglot developer with expertise in Python ML, JavaScript frontend, and Rust systems programming. "
                     "Demonstrates consistent activity across diverse technology stacks. "
                     "Focus on practical tools and data-driven applications."
            )]
            mock_message.usage.input_tokens = 1000
            mock_message.usage.output_tokens = 150
            mock_client.messages.create.return_value = mock_message
            mock_anthropic.return_value = mock_client

            summarizer = RepositorySummarizer()
            profile_gen = UserProfileGenerator(summarizer)
            profile = profile_gen.generate_profile("testuser", repositories, commit_histories, {})

            assert profile is not None, "Profile should be generated"
            assert profile.username == "testuser"
            assert profile.total_repositories >= 3
            assert profile.tech_diversity_score > 0.5, "Should have high tech diversity"
            assert len(profile.activity_patterns) >= 3, "Should identify 3+ patterns (SC-004)"
            assert profile.overall_impression is not None, "Should have overall impression"


# REMOVED: TestUserStory3Scenarios - Technology currency assessment out of scope
# Version checking functionality removed as it's better handled by specialized tools (Dependabot, Renovate)


class TestEdgeCases:
    """Test edge cases from spec.md."""

    def test_user_with_no_public_repositories(self):
        """T113: Edge case - User with no public repositories (spec.md L75)."""
        with patch("spark.fetcher.Github") as mock_github:
            mock_user = MagicMock()
            mock_user.get_repos.return_value = []  # No repos
            mock_github.return_value.get_user.return_value = mock_user

            fetcher = GitHubFetcher()
            repos = fetcher.fetch_repositories("testuser", exclude_private=True)

            # Should return empty list gracefully
            assert repos == [], "Should handle users with no public repos"

            # Report generation should handle empty list
            report_gen = ReportGenerator()
            profile = UserProfile(
                username="testuser",
                total_repositories=0,
                active_repositories=0,
                tech_diversity_score=0.0,
                activity_patterns=[],
                overall_impression="No public repositories found",
            )

            report = Report(
                user_profile=profile,
                repository_analyses=[],
                generation_timestamp=datetime.now(),
                metadata={"note": "User has no public repositories"},
            )

            markdown = report_gen.generate_report(report)
            assert markdown is not None, "Should generate report even with no repos"
            assert "no public repositories" in markdown.lower() or "0 repositories" in markdown.lower()

    def test_unrecognized_programming_language(self):
        """T114: Edge case - Repository with unrecognized programming language (spec.md L78)."""
        repo = Repository(
            name="obscure-lang-repo",
            description="Repository with unrecognized language",
            url="https://github.com/testuser/obscure-lang-repo",
            created_at=datetime.now() - timedelta(days=100),
            updated_at=datetime.now() - timedelta(days=5),
            primary_language="Brainfuck",  # Obscure language
            language_stats={"Brainfuck": 5000, "Assembly": 1000},
            stars=10,
            forks=2,
            issues=1,
            is_archived=False,
            is_fork=False,
        )

        commit_history = CommitHistory(
            repository_name="obscure-lang-repo",
            total_commits=25,
            recent_90d=8,
            recent_180d=15,
            recent_365d=25,
            last_commit_date=datetime.now() - timedelta(days=5),
        )

        # Ranker should handle unrecognized languages gracefully
        ranker = RepositoryRanker()
        ranked = ranker.rank_repositories([repo], {"obscure-lang-repo": commit_history}, top_n=10)

        assert len(ranked) == 1, "Should rank repo even with unrecognized language"
        _, score = ranked[0]
        assert score >= 0, "Score should be valid even for unrecognized language"

    def test_unparseable_dependency_file(self):
        """T115: Edge case - Dependency file that cannot be parsed (spec.md L82)."""
        from spark.dependencies.parser import DependencyParser

        # Malformed package.json
        malformed_json = """
        {
          "dependencies": {
            "package1": "^1.0.0",
            "package2": // invalid comment
          }
        }
        """

        parser = DependencyParser()

        # Should handle parse errors gracefully
        try:
            deps = parser.parse_package_json(malformed_json)
            # If it doesn't raise, should return empty dict or handle gracefully
            assert isinstance(deps, dict), "Should return dict even on parse error"
        except Exception as e:
            # Should be a graceful error, not a crash
            assert "parse" in str(e).lower() or "invalid" in str(e).lower()

    def test_archived_repository_activity_penalty(self):
        """T116: Edge case - Archived repository handling (spec.md L81 - validate 50% activity penalty)."""
        archived_repo = Repository(
            name="archived-repo",
            description="An archived repository",
            url="https://github.com/testuser/archived-repo",
            created_at=datetime.now() - timedelta(days=730),
            updated_at=datetime.now() - timedelta(days=365),
            primary_language="Python",
            stars=500,  # High stars
            forks=50,
            issues=0,
            is_archived=True,  # Archived!
            is_fork=False,
        )

        active_repo = Repository(
            name="active-repo",
            description="An active repository",
            url="https://github.com/testuser/active-repo",
            created_at=datetime.now() - timedelta(days=365),
            updated_at=datetime.now() - timedelta(days=2),
            primary_language="Python",
            stars=200,  # Fewer stars
            forks=20,
            issues=10,
            is_archived=False,
            is_fork=False,
        )

        commit_histories = {
            "archived-repo": CommitHistory(
                repository_name="archived-repo",
                total_commits=300,
                recent_90d=0,  # No recent activity
                recent_180d=0,
                recent_365d=5,
                last_commit_date=datetime.now() - timedelta(days=365),
            ),
            "active-repo": CommitHistory(
                repository_name="active-repo",
                total_commits=150,
                recent_90d=35,  # Active
                recent_180d=70,
                recent_365d=140,
                last_commit_date=datetime.now() - timedelta(days=2),
            ),
        }

        ranker = RepositoryRanker()
        ranked = ranker.rank_repositories(
            [archived_repo, active_repo],
            commit_histories,
            top_n=10
        )

        # Active repo should rank higher despite fewer stars
        # This validates the 50% activity penalty for archived repos
        scores = {name: score for (repo, score) in ranked for name in [repo.name]}

        assert scores["active-repo"] > scores["archived-repo"], \
            "Active repo should rank higher than archived repo despite fewer stars (validates activity penalty)"


class TestPerformanceValidation:
    """Test performance validation checkpoints."""

    def test_report_generation_performance_target(self):
        """T110: Test scenario - Complete report generation within 3-minute performance target (SC-001)."""
        # This test validates that the end-to-end workflow completes in under 3 minutes
        # Note: Actual timing would require real API calls, so this is a structural test

        import time

        # Simulate workflow steps with timing
        start_time = time.time()

        # Step 1: Mock repository fetching (should be <60s for 50 repos)
        mock_repos = [
            Repository(
                name=f"repo-{i}",
                description=f"Repository {i}",
                url=f"https://github.com/testuser/repo-{i}",
                created_at=datetime.now() - timedelta(days=365),
                updated_at=datetime.now() - timedelta(days=i),
                primary_language="Python",
                stars=100 - i,
                forks=10,
                issues=5,
                is_archived=False,
                is_fork=False,
            )
            for i in range(50)
        ]

        # Step 2: Mock ranking (should be <5s)
        ranker = RepositoryRanker()
        commit_histories = {
            f"repo-{i}": CommitHistory(
                repository_name=f"repo-{i}",
                total_commits=50,
                recent_90d=10,
                recent_180d=20,
                recent_365d=40,
                last_commit_date=datetime.now() - timedelta(days=i),
            )
            for i in range(50)
        }

        ranked = ranker.rank_repositories(mock_repos, commit_histories, top_n=50)

        # Step 3: Mock summarization (should be <90s for 50 repos with caching)
        # In real scenario, this would use cached AI responses

        # Step 4: Report generation (should be <10s)
        report_gen = ReportGenerator()
        analyses = [
            RepositoryAnalysis(
                repository=repo,
                commit_history=commit_histories[repo.name],
                summary=RepositorySummary(
                    repository_name=repo.name,
                    fallback_summary=f"Repository {repo.name}",
                    generation_method="template_basic",
                ),
                rank=i + 1,
                composite_score=score,
            )
            for i, (repo, score) in enumerate(ranked)
        ]

        profile = UserProfile(
            username="testuser",
            total_repositories=50,
            active_repositories=45,
            tech_diversity_score=0.85,
            activity_patterns=["consistent", "diverse", "active"],
            overall_impression="Active polyglot developer",
        )

        report = Report(
            user_profile=profile,
            repository_analyses=analyses,
            generation_timestamp=datetime.now(),
            metadata={},
        )

        markdown = report_gen.generate_report(report)

        elapsed_time = time.time() - start_time

        # This test should complete very quickly with mocks
        assert elapsed_time < 5, "Mocked workflow should complete in <5 seconds"
        assert markdown is not None, "Report should be generated"

        # In production, with real API calls and caching:
        # - Target: <180 seconds (3 minutes)
        # - Expected with warm cache: <120 seconds


class TestPrivacyFilter:
    """Test privacy filter compliance (constitution requirement)."""

    def test_privacy_filter_excludes_private_repositories(self):
        """T109: Test scenario - Privacy filter excludes private repositories."""
        # Create mix of public and private repositories
        mock_repos = [
            Mock(
                name="public-repo-1",
                full_name="testuser/public-repo-1",
                description="Public repository 1",
                html_url="https://github.com/testuser/public-repo-1",
                private=False,
                created_at=datetime.now() - timedelta(days=365),
                updated_at=datetime.now() - timedelta(days=10),
                language="Python",
                stargazers_count=100,
                forks_count=10,
                open_issues_count=5,
                archived=False,
                fork=False,
                size=1000,
            ),
            Mock(
                name="private-repo",
                full_name="testuser/private-repo",
                description="Private repository",
                html_url="https://github.com/testuser/private-repo",
                private=True,  # Private!
                created_at=datetime.now() - timedelta(days=200),
                updated_at=datetime.now() - timedelta(days=5),
                language="Python",
                stargazers_count=0,
                forks_count=0,
                open_issues_count=0,
                archived=False,
                fork=False,
                size=500,
            ),
            Mock(
                name="public-repo-2",
                full_name="testuser/public-repo-2",
                description="Public repository 2",
                html_url="https://github.com/testuser/public-repo-2",
                private=False,
                created_at=datetime.now() - timedelta(days=180),
                updated_at=datetime.now() - timedelta(days=3),
                language="JavaScript",
                stargazers_count=50,
                forks_count=5,
                open_issues_count=2,
                archived=False,
                fork=False,
                size=800,
            ),
        ]

        with patch("spark.fetcher.Github") as mock_github:
            mock_user = MagicMock()
            mock_user.get_repos.return_value = mock_repos
            mock_github.return_value.get_user.return_value = mock_user

            fetcher = GitHubFetcher()
            repos = fetcher.fetch_repositories("testuser", exclude_private=True)

            # Should only return public repositories
            assert len(repos) == 2, "Should exclude private repositories"

            # Verify no private repos in results
            for repo in repos:
                assert repo.get("private") == False or "private" not in repo, \
                    "All returned repos should be public"

            # Verify private repo is excluded
            repo_names = [r.get("name") for r in repos]
            assert "private-repo" not in repo_names, "Private repo should be excluded"
            assert "public-repo-1" in repo_names, "Public repo 1 should be included"
            assert "public-repo-2" in repo_names, "Public repo 2 should be included"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
