"""Integration tests for summarizer fallback scenarios.

Tests the complete fallback chain:
1. AI Summary (Primary)
2. Enhanced Template (Fallback 1 - README + metadata)
3. Basic Template (Fallback 2 - metadata only)
"""

import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta

from spark.models.repository import Repository
from spark.models.commit import CommitHistory
from spark.models.summary import RepositorySummary
from spark.summarizer import RepositorySummarizer


@pytest.fixture
def summarizer_with_api():
    """Create summarizer with valid API configuration."""
    config = {
        "anthropic_api_key": "test-key-valid",
        "model": "claude-3-5-haiku-20241022",
        "max_retries": 3,
        "timeout": 30
    }
    return RepositorySummarizer(config)


@pytest.fixture
def summarizer_without_api():
    """Create summarizer without API key (forces fallback)."""
    config = {
        "anthropic_api_key": None,
        "model": "claude-3-5-haiku-20241022"
    }
    return RepositorySummarizer(config)


@pytest.fixture
def complete_repository():
    """Repository with README and full metadata."""
    now = datetime.now()
    return Repository(
        name="complete-project",
        full_name="user/complete-project",
        description="A fully documented project with all metadata",
        url="https://github.com/user/complete-project",
        created_at=now - timedelta(days=730),
        updated_at=now - timedelta(days=3),
        primary_language="Python",
        language_stats={"Python": 75000, "JavaScript": 20000, "CSS": 5000},
        stars=850,
        forks=120,
        watchers=300,
        open_issues=18,
        is_archived=False,
        is_fork=False,
        is_private=False,
        size_kb=8000,
        has_readme=True,

    )


@pytest.fixture
def minimal_repository():
    """Repository with minimal metadata, no README."""
    now = datetime.now()
    return Repository(
        name="minimal-project",
        full_name="user/minimal-project",
        description="",
        url="https://github.com/user/minimal-project",
        created_at=now - timedelta(days=90),
        updated_at=now - timedelta(days=10),
        primary_language="Go",
        language_stats={"Go": 50000},
        stars=5,
        forks=1,
        watchers=3,
        open_issues=2,
        is_archived=False,
        is_fork=False,
        is_private=False,
        size_kb=1500,
        has_readme=False,

    )


@pytest.fixture
def active_commits():
    """Active commit history."""
    now = datetime.now()
    return CommitHistory(
        repository_name="test",
        total_commits=320,
        recent_90d=55,
        recent_180d=95,
        recent_365d=185,
        last_commit_date=now - timedelta(days=3),
        patterns={"frequency": "active", "consistency": "consistent"}
    )


@pytest.fixture
def complete_readme():
    """Complete README with all sections."""
    return """# Complete Project

A comprehensive solution for enterprise-grade applications.

## Overview

This project provides a robust framework for building scalable systems with built-in security, monitoring, and deployment automation.

## Features

- **Security**: Built-in authentication and authorization
- **Scalability**: Horizontal and vertical scaling support
- **Monitoring**: Integrated metrics and logging
- **CI/CD**: Automated testing and deployment pipelines

## Installation

```bash
npm install complete-project
```

## Quick Start

```python
from complete import App

app = App()
app.configure(security=True, monitoring=True)
app.run()
```

## Architecture

The system follows a microservices architecture with:
- API Gateway
- Service mesh
- Message queue
- Database cluster

## Contributing

See CONTRIBUTING.md for guidelines.

## License

Apache 2.0
"""


class TestTier1_AISummary:
    """Test Tier 1: Primary AI summary generation."""

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_ai_summary_success(self, mock_anthropic, summarizer_with_api, complete_repository, active_commits, complete_readme):
        """Test successful AI summary generation (happy path)."""
        # Mock successful API response
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client

        mock_response = MagicMock()
        mock_response.content = [MagicMock(
            text="An enterprise-grade framework for building scalable applications with built-in security, monitoring, and CI/CD automation. Features microservices architecture with API gateway, service mesh, and database clustering."
        )]
        mock_response.usage.input_tokens = 2200
        mock_response.usage.output_tokens = 85
        mock_client.messages.create.return_value = mock_response

        # Generate summary
        summary = summarizer_with_api.generate_summary(
            complete_repository,
            active_commits,
            complete_readme
        )

        # Assertions
        assert summary.generation_method == "claude-3-5-haiku-20241022"
        assert summary.ai_summary is not None
        assert summary.fallback_summary is None
        assert "enterprise" in summary.ai_summary.lower()
        assert "scalable" in summary.ai_summary.lower()
        assert len(summary.ai_summary) > 50

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_ai_summary_with_minimal_repo(self, mock_anthropic, summarizer_with_api, minimal_repository, active_commits):
        """Test AI summary with minimal repository (no README)."""
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client

        mock_response = MagicMock()
        mock_response.content = [MagicMock(
            text="A Go-based project with active development, showing 55 commits in the last 90 days."
        )]
        mock_response.usage.input_tokens = 800
        mock_response.usage.output_tokens = 40
        mock_client.messages.create.return_value = mock_response

        # Generate without README
        summary = summarizer_with_api.generate_summary(
            minimal_repository,
            active_commits,
            readme_content=None
        )

        # Should still use AI if available
        assert summary.generation_method == "claude-3-5-haiku-20241022"
        assert summary.ai_summary is not None


class TestTier2_EnhancedTemplate:
    """Test Tier 2: Enhanced template fallback (README + metadata)."""

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_enhanced_template_on_api_failure(self, mock_anthropic, summarizer_with_api, complete_repository, active_commits, complete_readme):
        """Test fallback to enhanced template when API fails."""
        # Mock API failure
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client
        mock_client.messages.create.side_effect = Exception("API Error: Service unavailable")

        # Generate summary
        summary = summarizer_with_api.generate_summary(
            complete_repository,
            active_commits,
            complete_readme
        )

        # Should use enhanced template
        assert summary.generation_method == "enhanced-template"
        assert summary.ai_summary is None
        assert summary.fallback_summary is not None
        assert "Python" in summary.fallback_summary
        assert any(word in summary.fallback_summary.lower() for word in ["framework", "enterprise", "scalable"])

    def test_enhanced_template_extracts_from_readme(self, summarizer_without_api, complete_repository, active_commits, complete_readme):
        """Test that enhanced template extracts key information from README."""
        summary = summarizer_without_api.generate_summary(
            complete_repository,
            active_commits,
            complete_readme
        )

        assert summary.generation_method == "enhanced-template"
        assert summary.fallback_summary is not None

        # Should extract key features
        summary_lower = summary.fallback_summary.lower()
        assert any(word in summary_lower for word in ["security", "scalability", "monitoring"])

    def test_enhanced_template_includes_metadata(self, summarizer_without_api, complete_repository, active_commits, complete_readme):
        """Test that enhanced template includes repository metadata."""
        summary = summarizer_without_api.generate_summary(
            complete_repository,
            active_commits,
            complete_readme
        )

        # Should include language and stats
        assert "Python" in summary.fallback_summary
        assert "850" in summary.fallback_summary or "stars" in summary.fallback_summary.lower()

    def test_enhanced_template_with_partial_readme(self, summarizer_without_api, complete_repository, active_commits):
        """Test enhanced template with minimal README content."""
        minimal_readme = "# Project\n\nA simple tool.\n"

        summary = summarizer_without_api.generate_summary(
            complete_repository,
            active_commits,
            minimal_readme
        )

        # Should still generate meaningful summary
        assert summary.generation_method == "enhanced-template"
        assert len(summary.fallback_summary) > 50
        assert "Python" in summary.fallback_summary


class TestTier3_BasicTemplate:
    """Test Tier 3: Basic template fallback (metadata only)."""

    def test_basic_template_no_readme(self, summarizer_without_api, complete_repository, active_commits):
        """Test basic template when README is unavailable."""
        summary = summarizer_without_api.generate_summary(
            complete_repository,
            active_commits,
            readme_content=None
        )

        # Should use basic or enhanced template
        assert summary.generation_method in [
            "basic-template",
            "enhanced-template"
        ]
        assert summary.fallback_summary is not None

        # Should include basic metadata
        assert "Python" in summary.fallback_summary
        assert str(complete_repository.stars) in summary.fallback_summary or "star" in summary.fallback_summary.lower()

    def test_basic_template_minimal_repo(self, summarizer_without_api, minimal_repository, active_commits):
        """Test basic template with minimal repository metadata."""
        summary = summarizer_without_api.generate_summary(
            minimal_repository,
            active_commits,
            readme_content=None
        )

        # Should generate summary from minimal metadata
        assert summary.fallback_summary is not None
        assert "Go" in summary.fallback_summary
        assert len(summary.fallback_summary) > 30

    def test_basic_template_includes_commit_info(self, summarizer_without_api, complete_repository, active_commits):
        """Test that basic template includes commit activity information."""
        summary = summarizer_without_api.generate_summary(
            complete_repository,
            active_commits,
            readme_content=None
        )

        # Should mention commits or activity
        summary_lower = summary.fallback_summary.lower()
        assert "commit" in summary_lower or "active" in summary_lower or str(active_commits.total_commits) in summary.fallback_summary


class TestFallbackChain:
    """Test complete fallback chain integration."""

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_fallback_chain_tier1_to_tier2(self, mock_anthropic, summarizer_with_api, complete_repository, active_commits, complete_readme):
        """Test fallback from AI to enhanced template."""
        # Simulate API failure after retries
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client
        mock_client.messages.create.side_effect = Exception("Persistent API error")

        summary = summarizer_with_api.generate_summary(
            complete_repository,
            active_commits,
            complete_readme
        )

        # Should have fallen back to enhanced template
        assert summary.generation_method == "enhanced-template"
        assert summary.ai_summary is None
        assert summary.fallback_summary is not None

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_fallback_chain_tier1_to_tier3(self, mock_anthropic, summarizer_with_api, minimal_repository, active_commits):
        """Test fallback from AI to basic template (no README)."""
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client
        mock_client.messages.create.side_effect = Exception("API error")

        summary = summarizer_with_api.generate_summary(
            minimal_repository,
            active_commits,
            readme_content=None
        )

        # Should have fallen back to basic template
        assert summary.generation_method in [
            "basic-template",
            "enhanced-template"
        ]
        assert summary.fallback_summary is not None

    def test_fallback_chain_all_tiers_available(self, summarizer_without_api, complete_repository, active_commits, complete_readme):
        """Test that fallback works even when all AI tiers are unavailable."""
        # No API key, forces fallback
        summary = summarizer_without_api.generate_summary(
            complete_repository,
            active_commits,
            complete_readme
        )

        # Should successfully generate fallback summary
        assert summary is not None
        assert isinstance(summary, RepositorySummary)
        assert summary.fallback_summary is not None
        assert len(summary.fallback_summary) > 50


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_repository_description(self, summarizer_without_api, active_commits):
        """Test handling of repository with empty description."""
        now = datetime.now()
        empty_desc_repo = Repository(
            name="no-desc",
            full_name="user/no-desc",
            description="",  # Empty description
            url="https://github.com/user/no-desc",
            created_at=now - timedelta(days=100),
            updated_at=now - timedelta(days=5),
            primary_language="Ruby",
            language_stats={"Ruby": 30000},
            stars=10,
            forks=2,
            watchers=5,
            open_issues=1,
            is_archived=False,
            is_fork=False,
            is_private=False,
            size_kb=2000,
            has_readme=False,

        )

        summary = summarizer_without_api.generate_summary(
            empty_desc_repo,
            active_commits,
            readme_content=None
        )

        # Should still generate summary
        assert summary.fallback_summary is not None
        assert "Ruby" in summary.fallback_summary

    def test_archived_repository(self, summarizer_without_api, active_commits):
        """Test handling of archived repository."""
        now = datetime.now()
        archived_repo = Repository(
            name="archived",
            full_name="user/archived",
            description="Archived project",
            url="https://github.com/user/archived",
            created_at=now - timedelta(days=1000),
            updated_at=now - timedelta(days=365),
            primary_language="Java",
            language_stats={"Java": 100000},
            stars=5000,
            forks=800,
            watchers=1500,
            open_issues=200,
            is_archived=True,
            is_fork=False,
            is_private=False,
            size_kb=25000,
            has_readme=True,

        )

        readme = "# Archived Project\n\nThis project is no longer maintained.\n"

        summary = summarizer_without_api.generate_summary(
            archived_repo,
            active_commits,
            readme
        )

        # Should mention archived status
        summary_lower = summary.fallback_summary.lower()
        assert "archived" in summary_lower or "maintained" in summary_lower

    def test_fork_repository(self, summarizer_without_api, active_commits):
        """Test handling of fork repository."""
        now = datetime.now()
        fork_repo = Repository(
            name="forked-lib",
            full_name="user/forked-lib",
            description="Fork of popular library",
            url="https://github.com/user/forked-lib",
            created_at=now - timedelta(days=200),
            updated_at=now - timedelta(days=20),
            primary_language="TypeScript",
            language_stats={"TypeScript": 60000},
            stars=3,
            forks=0,
            watchers=2,
            open_issues=1,
            is_archived=False,
            is_fork=True,
            is_private=False,
            size_kb=8000,
            has_readme=True,

        )

        summary = summarizer_without_api.generate_summary(
            fork_repo,
            active_commits,
            readme_content="# Forked Library\n\nMy fork of the library.\n"
        )

        # Should handle fork gracefully
        assert summary.fallback_summary is not None
        assert "TypeScript" in summary.fallback_summary


class TestConsistency:
    """Test consistency of fallback summaries."""

    def test_same_input_same_output(self, summarizer_without_api, complete_repository, active_commits, complete_readme):
        """Test that same inputs produce consistent outputs."""
        summary1 = summarizer_without_api.generate_summary(
            complete_repository,
            active_commits,
            complete_readme
        )

        summary2 = summarizer_without_api.generate_summary(
            complete_repository,
            active_commits,
            complete_readme
        )

        # Template summaries should be deterministic
        assert summary1.fallback_summary == summary2.fallback_summary
        assert summary1.generation_method == summary2.generation_method

    def test_different_repos_different_summaries(self, summarizer_without_api, complete_repository, minimal_repository, active_commits):
        """Test that different repositories produce different summaries."""
        summary1 = summarizer_without_api.generate_summary(
            complete_repository,
            active_commits,
            readme_content=None
        )

        summary2 = summarizer_without_api.generate_summary(
            minimal_repository,
            active_commits,
            readme_content=None
        )

        # Summaries should be different
        assert summary1.fallback_summary != summary2.fallback_summary
        assert "Python" in summary1.fallback_summary
        assert "Go" in summary2.fallback_summary


class TestPerformance:
    """Test fallback performance."""

    def test_fallback_faster_than_ai(self, summarizer_without_api, complete_repository, active_commits, complete_readme):
        """Test that template fallback is faster than AI calls."""
        import time

        start = time.time()
        summary = summarizer_without_api.generate_summary(
            complete_repository,
            active_commits,
            complete_readme
        )
        elapsed = time.time() - start

        # Template generation should be very fast
        assert elapsed < 0.5  # Less than 500ms
        assert summary.fallback_summary is not None

    def test_batch_fallback_performance(self, summarizer_without_api, active_commits):
        """Test performance of generating multiple fallback summaries."""
        import time

        # Create 10 different repositories
        repos = []
        for i in range(10):
            now = datetime.now()
            repo = Repository(
                name=f"project-{i}",
                full_name=f"user/project-{i}",
                description=f"Project {i}",
                url=f"https://github.com/user/project-{i}",
                created_at=now - timedelta(days=365 + i*10),
                updated_at=now - timedelta(days=i),
                primary_language="Python",
                language_stats={"Python": 50000 + i*1000},
                stars=100 + i*10,
                forks=20 + i*2,
                watchers=50 + i*5,
                open_issues=10 + i,
                is_archived=False,
                is_fork=False,
                is_private=False,
                size_kb=5000 + i*100,
                has_readme=True,

            )
            repos.append(repo)

        # Generate summaries
        start = time.time()
        summaries = [
            summarizer_without_api.generate_summary(repo, active_commits, f"# Project {i}\n\nDescription.")
            for i, repo in enumerate(repos)
        ]
        elapsed = time.time() - start

        # Should complete quickly
        assert elapsed < 2.0  # Less than 2 seconds for 10 repos
        assert len(summaries) == 10
        assert all(s.fallback_summary is not None for s in summaries)
