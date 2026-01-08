"""Integration tests for end-to-end workflow."""

import pytest
import json
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from spark.config import SparkConfig
from spark.calculator import StatsCalculator
from spark.visualizer import StatisticsVisualizer
from spark.themes.spark_dark import SparkDarkTheme
from spark.cache import APICache


class TestEndToEndWorkflow:
    """Test complete workflow from data to SVG generation."""

    @pytest.fixture
    def sample_data(self):
        """Load sample user data from fixtures."""
        fixtures_path = Path(__file__).parent.parent / "fixtures" / "sample_user_data.json"
        with open(fixtures_path, "r") as f:
            return json.load(f)

    @pytest.fixture
    def temp_output_dir(self, tmp_path):
        """Create temporary output directory."""
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        return output_dir

    @pytest.fixture
    def temp_cache_dir(self, tmp_path):
        """Create temporary cache directory."""
        cache_dir = tmp_path / ".cache"
        cache_dir.mkdir()
        return cache_dir

    def test_complete_generation_workflow(self, sample_data, temp_output_dir):
        """Test complete workflow: data -> calculation -> visualization -> SVG files."""
        # Step 1: Initialize calculator with sample data
        profile = sample_data["profile"]
        repositories = sample_data["repositories"]

        calculator = StatsCalculator(profile, repositories)

        # Add commits and languages
        calculator.add_commits(sample_data["commits"])
        calculator.add_languages(sample_data["languages"])

        # Step 2: Calculate statistics
        spark_score = calculator.calculate_spark_score()
        time_patterns = calculator.analyze_time_patterns()
        languages = calculator.aggregate_languages()
        streaks = calculator.calculate_streaks()

        # Verify calculations completed
        assert "total_score" in spark_score
        assert "category" in time_patterns
        assert len(languages) > 0
        assert "current_streak" in streaks

        # Step 3: Generate SVG visualizations
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme, enable_effects=True)

        # Generate all SVG types
        overview_svg = visualizer.generate_overview(
            username=profile["username"],
            spark_score=spark_score,
            total_commits=len(sample_data["commits"]),
            languages=languages[:5],
            time_pattern=time_patterns,
        )

        languages_svg = visualizer.generate_languages(profile["username"], languages)

        streaks_svg = visualizer.generate_streaks(
            username=profile["username"],
            current_streak=streaks["current_streak"],
            longest_streak=streaks["longest_streak"],
        )

        # Step 4: Verify SVG outputs
        assert overview_svg.startswith("<?xml")
        assert languages_svg.startswith("<?xml")
        assert streaks_svg.startswith("<?xml")

        # Verify content in overview
        assert profile["username"] in overview_svg
        assert str(spark_score["lightning_rating"]) in overview_svg or "⚡" in overview_svg

        # Verify content in languages
        assert "Python" in languages_svg
        assert "JavaScript" in languages_svg

        # Step 5: Write SVG files
        (temp_output_dir / "overview.svg").write_text(overview_svg)
        (temp_output_dir / "languages.svg").write_text(languages_svg)
        (temp_output_dir / "streaks.svg").write_text(streaks_svg)

        # Verify files were created
        assert (temp_output_dir / "overview.svg").exists()
        assert (temp_output_dir / "languages.svg").exists()
        assert (temp_output_dir / "streaks.svg").exists()

        # Verify file sizes are reasonable
        assert (temp_output_dir / "overview.svg").stat().st_size > 500
        assert (temp_output_dir / "languages.svg").stat().st_size > 300
        assert (temp_output_dir / "streaks.svg").stat().st_size > 200

    def test_cache_integration(self, temp_cache_dir):
        """Test cache integration with hierarchical storage."""
        cache = APICache(cache_dir=str(temp_cache_dir))

        # Test cache set and get with new hierarchical API
        test_data = {"username": "testuser", "repos": 50}
        
        # New API: category, owner, value
        cache.set("profile", "testuser", test_data)

        # Should retrieve cached data
        cached = cache.get("profile", "testuser")
        assert cached == test_data

        # Verify cache file exists in hierarchical structure
        cache_files = list(temp_cache_dir.rglob("*.json"))
        assert len(cache_files) > 0

    def test_selective_statistics_generation(self, sample_data, temp_output_dir):
        """Test selective statistics generation based on configuration."""
        # Simulate config with selective stats enabled
        enabled_stats = ["overview", "languages"]

        profile = sample_data["profile"]
        repositories = sample_data["repositories"]

        calculator = StatsCalculator(profile, repositories)
        calculator.add_commits(sample_data["commits"])
        calculator.add_languages(sample_data["languages"])

        # Calculate all stats
        spark_score = calculator.calculate_spark_score()
        time_patterns = calculator.analyze_time_patterns()
        languages = calculator.aggregate_languages()
        streaks = calculator.calculate_streaks()

        # Generate only enabled visualizations
        theme = SparkDarkTheme()
        visualizer = StatisticsVisualizer(theme)

        generated_svgs = {}

        if "overview" in enabled_stats:
            generated_svgs["overview"] = visualizer.generate_overview(
                username=profile["username"],
                spark_score=spark_score,
                total_commits=len(sample_data["commits"]),
                languages=languages[:5],
                time_pattern=time_patterns,
            )

        if "languages" in enabled_stats:
            generated_svgs["languages"] = visualizer.generate_languages(profile["username"], languages)

        # Should only have generated 2 SVGs
        assert len(generated_svgs) == 2
        assert "overview" in generated_svgs
        assert "languages" in generated_svgs
        assert "streaks" not in generated_svgs

    def test_error_handling_no_commits(self):
        """Test graceful handling of users with no commits."""
        profile = {"username": "newuser", "public_repos": 0, "followers": 0}
        repositories = []

        calculator = StatsCalculator(profile, repositories)

        # Should not crash with no data
        spark_score = calculator.calculate_spark_score()
        time_patterns = calculator.analyze_time_patterns()
        languages = calculator.aggregate_languages()
        streaks = calculator.calculate_streaks()

        # Should return sensible defaults
        assert spark_score["total_score"] >= 0
        assert spark_score["lightning_rating"] >= 1
        assert time_patterns["category"] in ["night_owl", "early_bird", "balanced", "no_data"]
        assert languages == []
        assert streaks["current_streak"] == 0

    def test_success_rate_validation(self, sample_data):
        """Test 99% success rate requirement (SC-007)."""
        # Simulate 100 generation attempts
        successful = 0
        total_attempts = 100

        profile = sample_data["profile"]
        repositories = sample_data["repositories"]

        for i in range(total_attempts):
            try:
                calculator = StatsCalculator(profile, repositories)
                calculator.add_commits(sample_data["commits"])
                calculator.add_languages(sample_data["languages"])

                spark_score = calculator.calculate_spark_score()
                theme = SparkDarkTheme()
                visualizer = StatisticsVisualizer(theme)

                svg = visualizer.generate_overview(
                    username=profile["username"],
                    spark_score=spark_score,
                    total_commits=len(sample_data["commits"]),
                    languages=calculator.aggregate_languages()[:5],
                    time_pattern=calculator.analyze_time_patterns(),
                )

                if svg.startswith("<?xml"):
                    successful += 1

            except Exception as e:
                # Log failure but continue
                print(f"Attempt {i} failed: {e}")

        success_rate = successful / total_attempts
        assert success_rate >= 0.99, f"Success rate {success_rate*100}% is below 99% requirement"

    def test_accuracy_validation(self, sample_data):
        """Test statistics accuracy validation (SC-006)."""
        profile = sample_data["profile"]
        repositories = sample_data["repositories"]

        calculator = StatsCalculator(profile, repositories)
        calculator.add_commits(sample_data["commits"])
        calculator.add_languages(sample_data["languages"])

        # Test language aggregation accuracy
        languages = calculator.aggregate_languages()

        # Calculate expected total bytes
        expected_total = sum(sample_data["languages"].values())
        calculated_total = sum(lang["bytes"] for lang in languages)

        # Should match exactly (0% discrepancy for aggregation)
        assert calculated_total == expected_total

        # Test percentage calculations sum to 100%
        total_percentage = sum(lang["percentage"] for lang in languages)
        assert 99.9 <= total_percentage <= 100.1, "Language percentages don't sum to 100%"

    def test_repository_limit_enforcement(self):
        """Test repository limit enforcement."""
        # Create profile with many repos
        profile = {"username": "testuser", "public_repos": 1000, "followers": 100}

        # Create 600 repositories
        repositories = [
            {"name": f"repo{i}", "stars": i, "forks": i // 2, "watchers": i // 3} for i in range(600)
        ]

        calculator = StatsCalculator(profile, repositories)

        # Should handle large repository count
        # (Actual limit enforcement would be in fetcher, but calculator should handle it)
        spark_score = calculator.calculate_spark_score()

        assert spark_score is not None
        assert "total_score" in spark_score

    def test_theme_switching(self, sample_data):
        """Test theme switching produces different color schemes."""
        from spark.themes.spark_light import SparkLightTheme

        profile = sample_data["profile"]
        calculator = StatsCalculator(profile, sample_data["repositories"])
        calculator.add_commits(sample_data["commits"])
        calculator.add_languages(sample_data["languages"])

        spark_score = calculator.calculate_spark_score()
        languages = calculator.aggregate_languages()
        time_pattern = calculator.analyze_time_patterns()

        # Generate with dark theme
        dark_theme = SparkDarkTheme()
        dark_visualizer = StatisticsVisualizer(dark_theme)
        dark_svg = dark_visualizer.generate_overview(
            username=profile["username"],
            spark_score=spark_score,
            total_commits=len(sample_data["commits"]),
            languages=languages[:5],
            time_pattern=time_pattern,
        )

        # Generate with light theme
        light_theme = SparkLightTheme()
        light_visualizer = StatisticsVisualizer(light_theme)
        light_svg = light_visualizer.generate_overview(
            username=profile["username"],
            spark_score=spark_score,
            total_commits=len(sample_data["commits"]),
            languages=languages[:5],
            time_pattern=time_pattern,
        )

        # SVGs should be different (different colors)
        assert dark_svg != light_svg

        # Verify theme-specific colors are present
        assert dark_theme.background_color.lower() in dark_svg.lower()
        assert light_theme.background_color.lower() in light_svg.lower()
