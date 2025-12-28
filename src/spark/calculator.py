"""Statistics calculation for GitHub activity data."""

from typing import Dict, List, Any, Tuple
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import math


class StatsCalculator:
    """Calculates comprehensive statistics from GitHub activity data."""

    def __init__(self, profile: Dict[str, Any], repositories: List[Dict[str, Any]]):
        """Initialize calculator with user data.

        Args:
            profile: User profile data
            repositories: List of repository data
        """
        self.profile = profile
        self.repositories = repositories
        self.commits: List[Dict[str, Any]] = []
        self.languages: Dict[str, int] = {}

    def add_commits(self, commits: List[Dict[str, Any]]) -> None:
        """Add commits data for analysis.

        Args:
            commits: List of commit data dictionaries
        """
        self.commits.extend(commits)

    def add_languages(self, languages: Dict[str, int]) -> None:
        """Add language statistics.

        Args:
            languages: Dictionary mapping language names to byte counts
        """
        for lang, bytes_count in languages.items():
            self.languages[lang] = self.languages.get(lang, 0) + bytes_count

    def calculate_spark_score(self) -> Dict[str, Any]:
        """Calculate overall Spark Score (0-100).

        Formula: 40% consistency + 35% commit volume + 25% collaboration

        Returns:
            Dictionary with total score and component scores
        """
        consistency_score = self._calculate_consistency_score()
        volume_score = self._calculate_volume_score()
        collaboration_score = self._calculate_collaboration_score()

        # Weighted combination
        total_score = (
            consistency_score * 0.40 +
            volume_score * 0.35 +
            collaboration_score * 0.25
        )

        # Calculate lightning rating (1-5 bolts)
        lightning_rating = self.calculate_lightning_rating(total_score)

        return {
            "total_score": round(total_score, 1),
            "consistency_score": round(consistency_score, 1),
            "volume_score": round(volume_score, 1),
            "collaboration_score": round(collaboration_score, 1),
            "lightning_rating": lightning_rating,
        }

    def _calculate_consistency_score(self) -> float:
        """Calculate consistency score based on commit regularity.

        Measures how consistently you commit across weeks.
        Combines both regularity (lower variance) and activity rate.

        Returns:
            Score from 0-100
        """
        if not self.commits:
            return 0.0

        # Group commits by week
        week_commits = defaultdict(int)
        for commit in self.commits:
            if commit.get("date"):
                date = datetime.fromisoformat(commit["date"].replace("Z", "+00:00"))
                week_key = date.strftime("%Y-W%U")
                week_commits[week_key] += 1

        if not week_commits:
            return 0.0

        # Calculate weekly activity metrics
        weekly_counts = list(week_commits.values())
        total_weeks_with_commits = len(weekly_counts)
        mean = sum(weekly_counts) / len(weekly_counts)
        
        # Calculate coefficient of variation (normalized std dev)
        if mean == 0:
            return 0.0
            
        variance = sum((x - mean) ** 2 for x in weekly_counts) / len(weekly_counts)
        std_dev = math.sqrt(variance)
        cv = std_dev / mean  # Coefficient of variation
        
        # Calculate activity rate (weeks with commits / total weeks in period)
        if self.commits:
            dates = [datetime.fromisoformat(c["date"].replace("Z", "+00:00")) 
                    for c in self.commits if c.get("date")]
            if dates:
                oldest = min(dates)
                newest = max(dates)
                total_weeks = max(1, ((newest - oldest).days + 1) / 7)
                activity_rate = min(1.0, total_weeks_with_commits / total_weeks)
            else:
                activity_rate = 0.0
        else:
            activity_rate = 0.0
        
        # Score based on both regularity (lower CV = better) and activity rate
        # CV of 0 = perfect consistency, CV > 2 = very inconsistent
        regularity_score = max(0, min(100, 100 * (1 - min(cv / 2, 1))))
        activity_score = activity_rate * 100
        
        # Combine: 60% regularity, 40% activity rate
        consistency = (regularity_score * 0.6) + (activity_score * 0.4)
        
        return min(100, consistency)

    def _calculate_volume_score(self) -> float:
        """Calculate commit volume score with diminishing returns.

        Returns:
            Score from 0-100
        """
        commit_count = len(self.commits)

        # Logarithmic scale with diminishing returns
        # 100 commits = 50 points, 1000 commits = 75 points, 10000 commits = 100 points
        if commit_count == 0:
            return 0.0

        score = 20 * math.log10(commit_count + 1)
        return min(100, score)

    def _calculate_collaboration_score(self) -> float:
        """Calculate collaboration score based on stars, forks, and community engagement.

        Returns:
            Score from 0-100
        """
        total_stars = sum(repo.get("stars", 0) for repo in self.repositories)
        total_forks = sum(repo.get("forks", 0) for repo in self.repositories)
        total_watchers = sum(repo.get("watchers", 0) for repo in self.repositories)
        followers = self.profile.get("followers", 0)

        # Weighted combination with diminishing returns
        stars_score = min(50, 10 * math.log10(total_stars + 1))
        forks_score = min(30, 8 * math.log10(total_forks + 1))
        watchers_score = min(10, 5 * math.log10(total_watchers + 1))
        followers_score = min(10, 5 * math.log10(followers + 1))

        total = stars_score + forks_score + watchers_score + followers_score
        return min(100, total)

    def calculate_lightning_rating(self, spark_score: float) -> int:
        """Map Spark Score to lightning bolt rating (1-5).

        Args:
            spark_score: Total Spark Score (0-100)

        Returns:
            Lightning rating from 1 to 5
        """
        if spark_score >= 80:
            return 5
        elif spark_score >= 60:
            return 4
        elif spark_score >= 40:
            return 3
        elif spark_score >= 20:
            return 2
        else:
            return 1

    def analyze_time_patterns(self) -> Dict[str, Any]:
        """Analyze when user commits (hour distribution, night owl/early bird).

        Returns:
            Dictionary with time pattern analysis
        """
        if not self.commits:
            return {
                "category": "unknown",
                "hour_distribution": {},
                "most_active_hour": None,
            }

        # Count commits by hour
        hour_counts = defaultdict(int)
        for commit in self.commits:
            if commit.get("date"):
                date = datetime.fromisoformat(commit["date"].replace("Z", "+00:00"))
                hour_counts[date.hour] += 1

        total_commits = sum(hour_counts.values())

        # Night owl: majority commits between 22:00-4:00
        night_hours = list(range(22, 24)) + list(range(0, 5))
        night_commits = sum(hour_counts[h] for h in night_hours)

        # Early bird: majority commits between 5:00-9:00
        early_hours = list(range(5, 10))
        early_commits = sum(hour_counts[h] for h in early_hours)

        # Categorize
        if night_commits > total_commits * 0.4:
            category = "night_owl"
        elif early_commits > total_commits * 0.4:
            category = "early_bird"
        else:
            category = "balanced"

        # Find most active hour
        most_active_hour = max(hour_counts.items(), key=lambda x: x[1])[0] if hour_counts else None

        return {
            "category": category,
            "hour_distribution": dict(hour_counts),
            "most_active_hour": most_active_hour,
            "night_commits_percent": round(night_commits / total_commits * 100, 1) if total_commits > 0 else 0,
            "early_commits_percent": round(early_commits / total_commits * 100, 1) if total_commits > 0 else 0,
        }

    def aggregate_languages(self) -> List[Dict[str, Any]]:
        """Aggregate language usage with percentages.

        Returns:
            List of language dictionaries sorted by usage
        """
        if not self.languages:
            return []

        total_bytes = sum(self.languages.values())
        if total_bytes == 0:
            return []

        language_stats = []
        for lang, bytes_count in self.languages.items():
            percentage = (bytes_count / total_bytes) * 100
            language_stats.append({
                "name": lang,
                "bytes": bytes_count,
                "percentage": round(percentage, 1),
            })

        # Sort by percentage (highest first)
        language_stats.sort(key=lambda x: x["percentage"], reverse=True)

        # Group small languages as "Other" if more than 10 languages
        if len(language_stats) > 10:
            top_9 = language_stats[:9]
            other_percentage = sum(lang["percentage"] for lang in language_stats[9:])
            other_bytes = sum(lang["bytes"] for lang in language_stats[9:])

            top_9.append({
                "name": "Other",
                "bytes": other_bytes,
                "percentage": round(other_percentage, 1),
            })
            return top_9

        return language_stats

    def calculate_streaks(self) -> Dict[str, Any]:
        """Calculate coding streaks and learning streaks.

        Returns:
            Dictionary with current and longest streaks
        """
        if not self.commits:
            return {
                "current_streak": 0,
                "longest_streak": 0,
                "current_learning_streak": 0,
                "longest_learning_streak": 0,
            }

        # Extract commit dates
        commit_dates = []
        for commit in self.commits:
            if commit.get("date"):
                date = datetime.fromisoformat(commit["date"].replace("Z", "+00:00"))
                commit_dates.append(date.date())

        # Sort and deduplicate
        unique_dates = sorted(set(commit_dates))

        # Calculate coding streaks
        current_streak = 0
        longest_streak = 0
        streak = 1

        for i in range(1, len(unique_dates)):
            if (unique_dates[i] - unique_dates[i-1]).days == 1:
                streak += 1
            else:
                longest_streak = max(longest_streak, streak)
                streak = 1

        longest_streak = max(longest_streak, streak)

        # Calculate current streak (from today)
        if unique_dates:
            today = datetime.now().date()
            last_commit = unique_dates[-1]
            days_since = (today - last_commit).days

            if days_since == 0:
                # Count backwards from today
                current_streak = 1
                for i in range(len(unique_dates) - 2, -1, -1):
                    if (unique_dates[i+1] - unique_dates[i]).days == 1:
                        current_streak += 1
                    else:
                        break
            elif days_since == 1:
                # Yesterday counts
                current_streak = 1
                for i in range(len(unique_dates) - 2, -1, -1):
                    if (unique_dates[i+1] - unique_dates[i]).days == 1:
                        current_streak += 1
                    else:
                        break

        # Learning streaks (new languages over time)
        # TODO: Implement learning streak detection based on language diversity
        current_learning_streak = 0
        longest_learning_streak = 0

        return {
            "current_streak": current_streak,
            "longest_streak": longest_streak,
            "current_learning_streak": current_learning_streak,
            "longest_learning_streak": longest_learning_streak,
        }
