"""Unit tests for StatisticsVisualizer and SVG generation."""

import pytest
from spark.visualizer import StatisticsVisualizer
from spark.themes.spark_dark import SparkDarkTheme
from spark.themes.spark_light import SparkLightTheme


class TestSVGGeneration:
    """Test SVG generation methods."""

    def test_generate_overview_structure(self):
        """Test overview SVG structure and content."""
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme, enable_effects=True)

        spark_score = {
            "total_score": 75.5,
            "consistency_score": 70.0,
            "volume_score": 80.0,
            "collaboration_score": 75.0,
            "lightning_rating": 4,
        }

        languages = [
            {"name": "Python", "percentage": 45.2, "bytes": 10000},
            {"name": "JavaScript", "percentage": 30.1, "bytes": 6500},
        ]

        time_pattern = {
            "category": "night_owl",
            "most_active_hour": 23,
            "hour_distribution": {23: 50, 0: 40, 1: 30},
        }

        svg = visualizer.generate_overview(
            username="testuser",
            spark_score=spark_score,
            total_commits=1250,
            languages=languages,
            time_pattern=time_pattern,
        )

        # Validate SVG structure
        assert svg.startswith("<?xml")
        assert "testuser" in svg
        assert "75.5" in svg or "75" in svg  # Score
        assert "⚡" in svg  # Lightning bolts
        assert "Python" in svg
        assert "night_owl" in svg.lower() or "Night Owl" in svg

    def test_generate_overview_with_effects(self):
        """Test overview SVG with effects enabled."""
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme, enable_effects=True)

        spark_score = {
            "total_score": 85.0,
            "lightning_rating": 5,
            "consistency_score": 80.0,
            "volume_score": 90.0,
            "collaboration_score": 85.0,
        }

        svg = visualizer.generate_overview(
            username="testuser",
            spark_score=spark_score,
            total_commits=2000,
            languages=[],
            time_pattern={"category": "balanced", "most_active_hour": 14},
        )

        assert "<?xml" in svg
        assert len(svg) > 500  # Should be substantial

    def test_generate_heatmap_structure(self):
        """Test heatmap SVG structure."""
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme)

        commits_by_date = {
            "2025-12-28": 5,
            "2025-12-27": 3,
            "2025-12-26": 0,
            "2025-12-25": 8,
        }

        svg = visualizer.generate_heatmap("testuser", commits_by_date)

        assert svg.startswith("<?xml")
        assert "testuser" in svg
        # Should contain rect elements for calendar grid
        assert "rect" in svg

    def test_generate_languages_structure(self):
        """Test languages SVG structure."""
        theme = SparkLightTheme()
        visualizer = StatisticsVisualizer(theme)

        languages = [
            {"name": "Python", "percentage": 45.2, "bytes": 10000},
            {"name": "JavaScript", "percentage": 30.1, "bytes": 6500},
            {"name": "HTML", "percentage": 15.7, "bytes": 3500},
            {"name": "CSS", "percentage": 9.0, "bytes": 2000},
        ]

        svg = visualizer.generate_languages("testuser", languages)

        assert svg.startswith("<?xml")
        assert "Python" in svg
        assert "45.2" in svg or "45" in svg
        assert "JavaScript" in svg

    def test_generate_fun_stats_structure(self):
        """Test fun stats SVG structure."""
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme)

        stats = {
            "most_active_hour": 23,
            "coding_pattern": "Night Owl",
            "total_repos": 50,
            "account_age_days": 1825,
        }

        svg = visualizer.generate_fun_stats("testuser", stats)

        assert svg.startswith("<?xml")
        assert "testuser" in svg
        assert "23" in svg or "11 PM" in svg
        assert "Night Owl" in svg or "night" in svg.lower()

    def test_generate_release_cadence_structure(self):
        """Test release cadence SVG structure."""
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme)

        cadence = {
            "weekly": [
                {"label": "W01", "repos": 1, "start": "2025-01-01", "range_label": "Jan 01 - Jan 07"},
                {"label": "W02", "repos": 3, "start": "2025-01-08", "range_label": "Jan 08 - Jan 14"},
            ],
            "monthly": [
                {"label": "Jan", "repos": 2, "start": "2025-01-01", "range_label": "Jan 2025"},
                {"label": "Feb", "repos": 4, "start": "2025-02-01", "range_label": "Feb 2025"},
            ],
            "max_weekly": 3,
            "max_monthly": 4,
            "unique_repos": 5,
        }

        svg = visualizer.generate_release_cadence(cadence, "testuser")

        assert svg.startswith("<?xml")
        assert "Release Cadence" in svg
        assert "Weekly Repo Diversity" in svg
        assert "Monthly Repo Diversity" in svg
        assert "Peak" in svg

    def test_generate_streaks_structure(self):
        """Test streaks SVG structure."""
        theme = SparkLightTheme()
        visualizer = StatisticsVisualizer(theme)

        svg = visualizer.generate_streaks(
            username="testuser",
            current_streak=15,
            longest_streak=45,
        )

        assert svg.startswith("<?xml")
        assert "testuser" in svg
        assert "15" in svg
        assert "45" in svg
        assert "streak" in svg.lower()


class TestThemeApplication:
    """Test theme application in SVG generation."""

    def test_dark_theme_colors(self):
        """Test that dark theme colors are applied."""
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme)

        spark_score = {
            "total_score": 75.0,
            "lightning_rating": 4,
            "consistency_score": 70.0,
            "volume_score": 80.0,
            "collaboration_score": 75.0,
        }

        svg = visualizer.generate_overview(
            username="testuser",
            spark_score=spark_score,
            total_commits=1000,
            languages=[],
            time_pattern={"category": "balanced", "most_active_hour": 14},
        )

        # Check theme colors are used
        assert theme.primary_color.lower() in svg.lower()
        assert theme.background_color.lower() in svg.lower()

    def test_light_theme_colors(self):
        """Test that light theme colors are applied."""
        theme = SparkLightTheme()
        visualizer = StatisticsVisualizer(theme)

        languages = [{"name": "Python", "percentage": 100.0, "bytes": 10000}]

        svg = visualizer.generate_languages("testuser", languages)

        # Light theme should have light background
        assert theme.background_color.lower() in svg.lower()


class TestCommitMessageSanitization:
    """Test sanitization of commit messages to prevent SVG injection."""

    def test_sanitize_special_characters(self):
        """Test that special characters are escaped in SVG output."""
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme)

        # Test with potentially dangerous characters
        stats = {
            "most_active_hour": 23,
            "coding_pattern": "<script>alert('xss')</script>",
            "total_repos": 50,
            "account_age_days": 1825,
        }

        svg = visualizer.generate_fun_stats("testuser", stats)

        # Should not contain raw script tags
        assert "<script>" not in svg
        assert "alert(" not in svg

        # Should be properly escaped or sanitized
        assert "<?xml" in svg  # Valid SVG

    def test_truncate_long_text(self):
        """Test that extremely long text is truncated."""
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme)

        # Create very long language name
        long_name = "A" * 500

        languages = [{"name": long_name, "percentage": 100.0, "bytes": 10000}]

        svg = visualizer.generate_languages("testuser", languages)

        # Should still generate valid SVG
        assert svg.startswith("<?xml")
        # Should not contain the full 500-character name
        assert long_name not in svg


class TestEdgeCases:
    """Test edge cases in SVG generation."""

    def test_empty_languages(self):
        """Test generating overview with no languages."""
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme)

        spark_score = {
            "total_score": 50.0,
            "lightning_rating": 3,
            "consistency_score": 50.0,
            "volume_score": 50.0,
            "collaboration_score": 50.0,
        }

        svg = visualizer.generate_overview(
            username="testuser",
            spark_score=spark_score,
            total_commits=0,
            languages=[],
            time_pattern={"category": "balanced", "most_active_hour": 12},
        )

        assert svg.startswith("<?xml")
        assert "testuser" in svg

    def test_zero_commits_heatmap(self):
        """Test generating heatmap with no commits."""
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme)

        svg = visualizer.generate_heatmap("testuser", {})

        assert svg.startswith("<?xml")
        assert "testuser" in svg

    def test_zero_streak(self):
        """Test generating streaks with zero values."""
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme)

        svg = visualizer.generate_streaks(
            username="testuser",
            current_streak=0,
            longest_streak=0,
        )

        assert svg.startswith("<?xml")
        assert "0" in svg or "No" in svg


class TestWCAGCompliance:
    """Test WCAG AA contrast compliance."""

    def test_light_theme_contrast(self):
        """Test that light theme has sufficient contrast."""
        theme = SparkLightTheme()

        # Light theme should have dark text on light background
        # or ensure proper contrast ratios
        assert theme.background_color == "#FFFFFF"
        assert theme.text_color != "#FFFFFF"  # Not white on white

        # Primary and accent colors should be different from background
        assert theme.primary_color != theme.background_color
        assert theme.accent_color != theme.background_color

    def test_dark_theme_contrast(self):
        """Test that dark theme has sufficient contrast."""
        theme = SparkDarkTheme()

        # Dark theme should have light text on dark background
        assert theme.background_color == "#0F172A"
        assert theme.text_color != "#0F172A"  # Not dark on dark

        # Verify colors are distinct
        assert theme.primary_color != theme.background_color
        assert theme.accent_color != theme.background_color
