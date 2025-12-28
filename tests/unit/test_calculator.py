"""Unit tests for StatsCalculator."""

import pytest
from datetime import datetime, timedelta
from spark.calculator import StatsCalculator


class TestSparkScore:
    """Test Spark Score calculation."""

    def test_calculate_spark_score_with_data(self):
        """Test Spark Score calculation with sample data."""
        profile = {
            "username": "testuser",
            "public_repos": 10,
            "followers": 50,
        }

        repositories = [
            {"name": "repo1", "stars": 100, "forks": 20, "watchers": 30},
            {"name": "repo2", "stars": 50, "forks": 10, "watchers": 15},
        ]

        calculator = StatsCalculator(profile, repositories)

        # Add some commits
        commits = [
            {"sha": "abc123", "date": datetime.now().isoformat(), "message": "Test commit"}
            for _ in range(100)
        ]
        calculator.add_commits(commits)

        spark_score = calculator.calculate_spark_score()

        assert "total_score" in spark_score
        assert "consistency_score" in spark_score
        assert "volume_score" in spark_score
        assert "collaboration_score" in spark_score
        assert "lightning_rating" in spark_score

        assert 0 <= spark_score["total_score"] <= 100
        assert 1 <= spark_score["lightning_rating"] <= 5

    def test_calculate_spark_score_no_data(self):
        """Test Spark Score calculation with no data."""
        profile = {"username": "testuser", "public_repos": 0, "followers": 0}
        repositories = []

        calculator = StatsCalculator(profile, repositories)
        spark_score = calculator.calculate_spark_score()

        assert spark_score["total_score"] >= 0
        assert spark_score["lightning_rating"] >= 1


class TestLightningRating:
    """Test lightning rating mapping."""

    def test_lightning_rating_levels(self):
        """Test all lightning rating thresholds."""
        calculator = StatsCalculator({}, [])

        assert calculator.calculate_lightning_rating(90) == 5
        assert calculator.calculate_lightning_rating(70) == 4
        assert calculator.calculate_lightning_rating(50) == 3
        assert calculator.calculate_lightning_rating(30) == 2
        assert calculator.calculate_lightning_rating(10) == 1


class TestTimePatterns:
    """Test time pattern analysis."""

    def test_night_owl_detection(self):
        """Test night owl pattern detection."""
        profile = {"username": "testuser"}
        calculator = StatsCalculator(profile, [])

        # Add commits during night hours (22:00-4:00)
        night_commits = []
        base_time = datetime.now().replace(hour=23, minute=0, second=0, microsecond=0)

        for i in range(50):
            commit_time = base_time - timedelta(days=i)
            night_commits.append({
                "sha": f"commit{i}",
                "date": commit_time.isoformat(),
                "message": "Night commit"
            })

        calculator.add_commits(night_commits)
        patterns = calculator.analyze_time_patterns()

        assert patterns["category"] == "night_owl"
        assert "hour_distribution" in patterns

    def test_early_bird_detection(self):
        """Test early bird pattern detection."""
        profile = {"username": "testuser"}
        calculator = StatsCalculator(profile, [])

        # Add commits during morning hours (6:00-9:00)
        morning_commits = []
        base_time = datetime.now().replace(hour=7, minute=0, second=0, microsecond=0)

        for i in range(50):
            commit_time = base_time - timedelta(days=i)
            morning_commits.append({
                "sha": f"commit{i}",
                "date": commit_time.isoformat(),
                "message": "Morning commit"
            })

        calculator.add_commits(morning_commits)
        patterns = calculator.analyze_time_patterns()

        assert patterns["category"] == "early_bird"

    def test_balanced_pattern(self):
        """Test balanced coding pattern."""
        profile = {"username": "testuser"}
        calculator = StatsCalculator(profile, [])

        # Add commits throughout the day
        commits = []
        base_time = datetime.now()

        for hour in range(8, 18):  # 8 AM to 6 PM
            for day in range(5):
                commit_time = base_time.replace(hour=hour, minute=0) - timedelta(days=day)
                commits.append({
                    "sha": f"commit{hour}{day}",
                    "date": commit_time.isoformat(),
                    "message": "Day commit"
                })

        calculator.add_commits(commits)
        patterns = calculator.analyze_time_patterns()

        assert patterns["category"] == "balanced"


class TestStreaks:
    """Test coding streak calculation."""

    def test_consecutive_streak(self):
        """Test calculation of consecutive coding streak."""
        profile = {"username": "testuser"}
        calculator = StatsCalculator(profile, [])

        # Add commits for consecutive 10 days
        commits = []
        base_time = datetime.now()

        for i in range(10):
            commit_time = base_time - timedelta(days=i)
            commits.append({
                "sha": f"commit{i}",
                "date": commit_time.isoformat(),
                "message": f"Day {i} commit"
            })

        calculator.add_commits(commits)
        streaks = calculator.calculate_streaks()

        assert streaks["longest_streak"] >= 10

    def test_no_streak(self):
        """Test streak calculation with no commits."""
        profile = {"username": "testuser"}
        calculator = StatsCalculator(profile, [])

        streaks = calculator.calculate_streaks()

        assert streaks["current_streak"] == 0
        assert streaks["longest_streak"] == 0


class TestLanguages:
    """Test language aggregation."""

    def test_aggregate_languages(self):
        """Test language percentage calculation."""
        profile = {"username": "testuser"}
        calculator = StatsCalculator(profile, [])

        # Add language data
        calculator.add_languages({"Python": 1000, "JavaScript": 500, "HTML": 300})

        languages = calculator.aggregate_languages()

        assert len(languages) == 3
        assert languages[0]["name"] == "Python"
        assert languages[0]["percentage"] > languages[1]["percentage"]

        # Check percentages sum to ~100
        total_percentage = sum(lang["percentage"] for lang in languages)
        assert 99.9 <= total_percentage <= 100.1

    def test_aggregate_languages_grouping(self):
        """Test 'Other' grouping for many languages."""
        profile = {"username": "testuser"}
        calculator = StatsCalculator(profile, [])

        # Add 15 languages
        languages_data = {f"Lang{i}": 100 - i * 5 for i in range(15)}
        calculator.add_languages(languages_data)

        languages = calculator.aggregate_languages()

        # Should group into top 9 + "Other"
        assert len(languages) <= 10
        if len(languages) == 10:
            assert languages[-1]["name"] == "Other"
