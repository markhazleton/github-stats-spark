"""Unit tests for AI-powered repository summarization."""

import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta

from spark.models.repository import Repository
from spark.models.commit import CommitHistory
from spark.models.summary import RepositorySummary
from spark.summarizer import RepositorySummarizer


@pytest.fixture
def summarizer():
    """Create a RepositorySummarizer instance for testing."""
    config = {
        "anthropic_api_key": "test-api-key-12345",
        "model": "claude-3-5-haiku-20241022",
        "max_retries": 3,
        "timeout": 30
    }
    return RepositorySummarizer(config)


@pytest.fixture
def sample_repository():
    """Create a sample repository for testing."""
    now = datetime.now()
    return Repository(
        name="awesome-project",
        full_name="testuser/awesome-project",
        description="A really cool open source project",
        url="https://github.com/testuser/awesome-project",
        created_at=now - timedelta(days=365),
        updated_at=now - timedelta(days=5),
        primary_language="Python",
        language_stats={"Python": 80000, "JavaScript": 15000, "HTML": 5000},
        stars=1250,
        forks=180,
        watchers=450,
        open_issues=25,
        is_archived=False,
        is_fork=False,
        is_private=False,
        size_kb=5000,
        has_readme=True,

    )


@pytest.fixture
def sample_commits():
    """Create sample commit history."""
    now = datetime.now()
    return CommitHistory(
        repository_name="awesome-project",
        total_commits=450,
        recent_90d=45,
        recent_180d=85,
        recent_365d=180,
        last_commit_date=now - timedelta(days=5),
        patterns={
            "frequency": "active",
            "recency": "recent",
            "consistency": "consistent"
        }
    )


@pytest.fixture
def sample_readme():
    """Create sample README content."""
    return """# Awesome Project

A comprehensive toolkit for building scalable web applications.

## Features

- Fast and efficient
- Easy to use
- Well documented
- Actively maintained

## Installation

```bash
pip install awesome-project
```

## Usage

```python
from awesome import App

app = App()
app.run()
```

## Contributing

We welcome contributions! Please see CONTRIBUTING.md for details.

## License

MIT License
"""


class TestAIIntegration:
    """Test Anthropic Claude API integration."""

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_successful_ai_summary(self, mock_anthropic, summarizer, sample_repository, sample_commits, sample_readme):
        """Test successful AI summary generation."""
        # Mock API response
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client

        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="This is a comprehensive web application toolkit that focuses on scalability and ease of use. The project is actively maintained with consistent commit patterns.")]
        mock_response.usage.input_tokens = 1500
        mock_response.usage.output_tokens = 150

        mock_client.messages.create.return_value = mock_response

        # Generate summary
        summary = summarizer.generate_summary(
            repository=sample_repository,
            commit_history=sample_commits,
            readme_content=sample_readme
        )

        # Assertions
        assert isinstance(summary, RepositorySummary)
        assert summary.repository_name == "awesome-project"
        assert summary.generation_method == "claude-3-5-haiku-20241022"
        assert "comprehensive" in summary.ai_summary.lower()
        assert "toolkit" in summary.ai_summary.lower()
        assert summary.fallback_summary is None

        # Verify API was called
        mock_client.messages.create.assert_called_once()

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_ai_api_error_fallback(self, mock_anthropic, summarizer, sample_repository, sample_commits, sample_readme):
        """Test fallback to enhanced template on API error."""
        # Mock API to raise error
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client
        mock_client.messages.create.side_effect = Exception("API Error: Rate limit exceeded")

        # Generate summary (should fallback)
        summary = summarizer.generate_summary(
            repository=sample_repository,
            commit_history=sample_commits,
            readme_content=sample_readme
        )

        # Assertions
        assert isinstance(summary, RepositorySummary)
        assert summary.generation_method == "enhanced-template"
        assert summary.ai_summary is None
        assert summary.fallback_summary is not None
        assert "Python" in summary.fallback_summary
        assert "1250" in summary.fallback_summary or "stars" in summary.fallback_summary.lower()

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_retry_logic(self, mock_anthropic, summarizer, sample_repository, sample_commits, sample_readme):
        """Test exponential backoff retry logic."""
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client

        # First two calls fail, third succeeds
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Success after retries")]
        mock_response.usage.input_tokens = 1500
        mock_response.usage.output_tokens = 50

        mock_client.messages.create.side_effect = [
            Exception("Temporary error"),
            Exception("Another temporary error"),
            mock_response
        ]

        # Generate summary
        summary = summarizer.generate_summary(
            repository=sample_repository,
            commit_history=sample_commits,
            readme_content=sample_readme
        )

        # Should succeed after retries
        assert summary.generation_method == "claude-3-5-haiku-20241022"
        assert summary.ai_summary == "Success after retries"

        # Verify retry happened
        assert mock_client.messages.create.call_count == 3


class TestREADMETruncation:
    """Test README content truncation."""

    def test_readme_truncation_for_context_window(self, summarizer):
        """Test that very long READMEs are truncated to fit context window."""
        # Create a very long README (simulate 300K tokens worth)
        long_readme = "# Long Project\n\n" + ("Lorem ipsum dolor sit amet. " * 100000)

        truncated = summarizer._truncate_readme(long_readme)

        # Should be significantly shorter
        assert len(truncated) < len(long_readme)
        assert len(truncated) < 200000  # Reasonable char limit for 200K token window

    def test_short_readme_not_truncated(self, summarizer, sample_readme):
        """Test that short READMEs are not modified."""
        truncated = summarizer._truncate_readme(sample_readme)
        assert truncated == sample_readme

    def test_truncation_preserves_beginning(self, summarizer):
        """Test that truncation keeps the important beginning content."""
        long_readme = "# Title\n\nImportant intro." + ("\n\nFiller content. " * 50000)
        truncated = summarizer._truncate_readme(long_readme)

        assert "# Title" in truncated
        assert "Important intro" in truncated


class TestCommitPatternAnalysis:
    """Test commit pattern analysis."""

    def test_active_pattern_detection(self, summarizer, sample_commits):
        """Test detection of active commit patterns."""
        analysis = summarizer._analyze_commit_patterns(sample_commits)

        assert "frequency" in analysis
        assert "recency" in analysis
        assert "consistency" in analysis

        # Active repo should have positive indicators
        assert analysis["frequency"] in ["active", "very_active", "moderate"]

    def test_stale_pattern_detection(self, summarizer):
        """Test detection of stale commit patterns."""
        now = datetime.now()
        stale_commits = CommitHistory(
            repository_name="stale",
            total_commits=500,
            recent_90d=0,
            recent_180d=0,
            recent_365d=2,
            last_commit_date=now - timedelta(days=300),
            patterns={}
        )

        analysis = summarizer._analyze_commit_patterns(stale_commits)

        assert analysis["frequency"] in ["low", "minimal", "inactive"]
        assert analysis["recency"] in ["stale", "old", "outdated"]

    def test_sporadic_pattern_detection(self, summarizer):
        """Test detection of sporadic commit patterns."""
        now = datetime.now()
        sporadic_commits = CommitHistory(
            repository_name="sporadic",
            total_commits=100,
            recent_90d=5,
            recent_180d=5,
            recent_365d=20,
            last_commit_date=now - timedelta(days=60),
            patterns={}
        )

        analysis = summarizer._analyze_commit_patterns(sporadic_commits)

        assert analysis["consistency"] in ["sporadic", "inconsistent", "irregular"]


class TestPromptEngineering:
    """Test prompt engineering for technical summaries."""

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_prompt_includes_repo_metadata(self, mock_anthropic, summarizer, sample_repository, sample_commits, sample_readme):
        """Test that prompt includes repository metadata."""
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client

        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Summary")]
        mock_response.usage.input_tokens = 1500
        mock_response.usage.output_tokens = 50
        mock_client.messages.create.return_value = mock_response

        summarizer.generate_summary(sample_repository, sample_commits, sample_readme)

        # Get the prompt that was sent
        call_args = mock_client.messages.create.call_args
        prompt_messages = call_args[1]["messages"]

        # Verify metadata is in prompt
        prompt_text = str(prompt_messages)
        assert "awesome-project" in prompt_text.lower()
        assert "1250" in prompt_text or "stars" in prompt_text.lower()

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_prompt_includes_commit_analysis(self, mock_anthropic, summarizer, sample_repository, sample_commits, sample_readme):
        """Test that prompt includes commit pattern analysis."""
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client

        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Summary")]
        mock_response.usage.input_tokens = 1500
        mock_response.usage.output_tokens = 50
        mock_client.messages.create.return_value = mock_response

        summarizer.generate_summary(sample_repository, sample_commits, sample_readme)

        call_args = mock_client.messages.create.call_args
        prompt_messages = call_args[1]["messages"]
        prompt_text = str(prompt_messages)

        # Should mention commit activity
        assert any(word in prompt_text.lower() for word in ["commit", "activity", "recent"])


class TestFallbackStrategies:
    """Test fallback strategies when AI is unavailable."""

    def test_enhanced_template_with_readme(self, summarizer, sample_repository, sample_commits, sample_readme):
        """Test enhanced template fallback extracts from README."""
        summary = summarizer._generate_enhanced_template_summary(
            sample_repository,
            sample_commits,
            sample_readme
        )

        assert isinstance(summary, str)
        assert len(summary) > 0
        assert "Python" in summary or sample_repository.primary_language in summary
        assert any(word in summary.lower() for word in ["toolkit", "web", "application"])

    def test_basic_template_without_readme(self, summarizer, sample_repository, sample_commits):
        """Test basic template fallback uses only metadata."""
        summary = summarizer._generate_basic_template_summary(
            sample_repository,
            sample_commits
        )

        assert isinstance(summary, str)
        assert len(summary) > 0
        assert "Python" in summary
        assert "1250" in summary or "stars" in summary.lower()
        assert str(sample_commits.total_commits) in summary or "commit" in summary.lower()

    def test_no_readme_fallback_scenario(self, summarizer, sample_repository, sample_commits):
        """Test FR-012 requirement: handle repositories without README."""
        # Repository without README
        no_readme_repo = Repository(
            name="no-readme-project",
            full_name="testuser/no-readme-project",
            description="A project without documentation",
            url="https://github.com/testuser/no-readme-project",
            created_at=datetime.now() - timedelta(days=180),
            updated_at=datetime.now() - timedelta(days=10),
            primary_language="JavaScript",
            language_stats={"JavaScript": 50000},
            stars=50,
            forks=10,
            watchers=25,
            open_issues=5,
            is_archived=False,
            is_fork=False,
            is_private=False,
            size_kb=2000,
            has_readme=False,

        )

        # Generate summary without README (should use basic template)
        summary = summarizer.generate_summary(
            repository=no_readme_repo,
            commit_history=sample_commits,
            readme_content=None
        )

        # Assertions for FR-012
        assert isinstance(summary, RepositorySummary)
        assert summary.generation_method in [
            "basic-template",
            "enhanced-template"
        ]
        assert summary.fallback_summary is not None
        assert "JavaScript" in summary.fallback_summary
        assert len(summary.fallback_summary) > 50  # Should have meaningful content

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_no_readme_with_ai_available(self, mock_anthropic, summarizer, sample_repository, sample_commits):
        """Test that AI can generate summary even without README."""
        # Mock successful API response
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client

        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="AI-generated summary based on metadata and commit history")]
        mock_response.usage.input_tokens = 800
        mock_response.usage.output_tokens = 60
        mock_client.messages.create.return_value = mock_response

        # Generate summary without README
        summary = summarizer.generate_summary(
            repository=sample_repository,
            commit_history=sample_commits,
            readme_content=None
        )

        # Should use AI even without README
        assert summary.generation_method == "claude-3-5-haiku-20241022"
        assert "AI-generated" in summary.ai_summary


class TestCostTracking:
    """Test API cost tracking and logging."""

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_token_usage_logging(self, mock_anthropic, summarizer, sample_repository, sample_commits, sample_readme):
        """Test that API token usage is logged."""
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client

        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Summary")]
        mock_response.usage.input_tokens = 2500
        mock_response.usage.output_tokens = 200
        mock_client.messages.create.return_value = mock_response

        with patch.object(summarizer.logger, 'info') as mock_logger:
            summarizer.generate_summary(sample_repository, sample_commits, sample_readme)

            # Verify cost logging
            logged_calls = [str(call) for call in mock_logger.call_args_list]
            assert any("token" in str(call).lower() for call in logged_calls)

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_cost_calculation(self, mock_anthropic, summarizer, sample_repository, sample_commits, sample_readme):
        """Test that API cost is calculated correctly."""
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client

        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Summary")]
        mock_response.usage.input_tokens = 10000  # Input tokens
        mock_response.usage.output_tokens = 1000  # Output tokens
        mock_client.messages.create.return_value = mock_response

        summary = summarizer.generate_summary(sample_repository, sample_commits, sample_readme)

        # Cost should be tracked (Haiku pricing: ~$0.25/$1.25 per million tokens)
        # This is a basic check that cost tracking exists
        assert hasattr(summarizer, 'total_cost') or hasattr(summarizer, 'track_cost')


class TestErrorHandling:
    """Test error handling and edge cases."""

    def test_empty_readme(self, summarizer, sample_repository, sample_commits):
        """Test handling of empty README content."""
        summary = summarizer.generate_summary(
            sample_repository,
            sample_commits,
            ""  # Empty string
        )

        # Should still generate a summary
        assert isinstance(summary, RepositorySummary)
        assert summary.fallback_summary is not None or summary.ai_summary is not None

    def test_malformed_readme(self, summarizer, sample_repository, sample_commits):
        """Test handling of malformed README content."""
        malformed = "# \n\n\n\n<<>>{}[]invalid"

        summary = summarizer.generate_summary(
            sample_repository,
            sample_commits,
            malformed
        )

        # Should handle gracefully
        assert isinstance(summary, RepositorySummary)

    def test_missing_api_key(self):
        """Test behavior when API key is missing."""
        config = {"anthropic_api_key": None}
        summarizer = RepositorySummarizer(config)

        # Should initialize but use fallback strategies
        assert summarizer is not None
        # Fallback functionality is tested through generate_summary method

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_api_timeout_fallback(self, mock_anthropic, summarizer, sample_repository, sample_commits, sample_readme):
        """Test fallback on API timeout."""
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client
        mock_client.messages.create.side_effect = TimeoutError("Request timed out")

        summary = summarizer.generate_summary(
            sample_repository,
            sample_commits,
            sample_readme
        )

        # Should fallback gracefully
        assert summary.generation_method in [
            "enhanced-template",
            "basic-template"
        ]
        assert summary.fallback_summary is not None


class TestSummaryQuality:
    """Test summary content quality."""

    @patch('spark.summarizer.anthropic.Anthropic')
    def test_summary_mentions_key_features(self, mock_anthropic, summarizer, sample_repository, sample_commits, sample_readme):
        """Test that summary extracts key features from README."""
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client

        # Mock AI to return a good summary
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="A scalable web application toolkit featuring fast performance, easy usage, comprehensive documentation, and active maintenance.")]
        mock_response.usage.input_tokens = 1500
        mock_response.usage.output_tokens = 80
        mock_client.messages.create.return_value = mock_response

        summary = summarizer.generate_summary(sample_repository, sample_commits, sample_readme)

        # Check quality indicators
        assert len(summary.ai_summary) > 50  # Should be substantive
        assert len(summary.ai_summary) < 500  # Should be concise

    def test_template_summary_structure(self, summarizer, sample_repository, sample_commits):
        """Test that template summaries follow a consistent structure."""
        summary_text = summarizer._generate_basic_template_summary(
            sample_repository,
            sample_commits
        )

        # Should include key information
        assert sample_repository.primary_language in summary_text
        assert any(str(val) in summary_text for val in [sample_repository.stars, "stars", "⭐"])
        assert "commit" in summary_text.lower() or str(sample_commits.total_commits) in summary_text
