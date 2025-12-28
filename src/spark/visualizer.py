"""SVG visualization generation for GitHub statistics."""

from typing import Dict, List, Any, Optional
import svgwrite
from svgwrite import Drawing
from datetime import datetime

from spark.themes import Theme
from spark.themes.spark_dark import SparkDarkTheme
from spark.themes.spark_light import SparkLightTheme
from spark.themes.custom import CustomTheme


class StatisticsVisualizer:
    """Generates SVG visualizations for GitHub statistics."""

    def __init__(self, theme: Theme, enable_effects: bool = True):
        """Initialize visualizer with theme.

        Args:
            theme: Theme instance for colors and effects
            enable_effects: Enable visual effects (glow, gradients)
        """
        self.theme = theme
        self.enable_effects = enable_effects and theme.effects.get("glow", False)

    def generate_overview(
        self,
        username: str,
        spark_score: Dict[str, Any],
        total_commits: int,
        languages: List[Dict[str, Any]],
        time_pattern: Dict[str, Any],
    ) -> str:
        """Generate overview SVG with Spark Score and key metrics.

        Args:
            username: GitHub username
            spark_score: Spark Score data
            total_commits: Total commit count
            languages: Top languages list
            time_pattern: Time pattern analysis

        Returns:
            SVG content as string
        """
        width = 800
        height = 400

        dwg = svgwrite.Drawing(size=(width, height))
        dwg.add(dwg.rect((0, 0), (width, height), fill=self.theme.background_color))

        # Title
        title_y = 40
        dwg.add(dwg.text(
            f"GitHub Stats - {username}",
            insert=(width // 2, title_y),
            text_anchor="middle",
            font_size="28px",
            font_family="Arial, sans-serif",
            fill=self.theme.text_color,
            font_weight="bold",
        ))

        # Spark Score section
        score_y = 100
        score = spark_score.get("total_score", 0)
        rating = spark_score.get("lightning_rating", 1)

        # Spark Score circle
        circle_x = 150
        circle_r = 60
        dwg.add(dwg.circle(
            center=(circle_x, score_y + 60),
            r=circle_r,
            fill=self.theme.primary_color,
            opacity=0.2,
        ))
        dwg.add(dwg.circle(
            center=(circle_x, score_y + 60),
            r=circle_r - 5,
            fill="none",
            stroke=self.theme.primary_color,
            stroke_width=3,
        ))

        # Score text
        dwg.add(dwg.text(
            f"{score}",
            insert=(circle_x, score_y + 70),
            text_anchor="middle",
            font_size="36px",
            font_family="Arial, sans-serif",
            fill=self.theme.accent_color,
            font_weight="bold",
        ))

        # Lightning bolts
        bolts = "⚡" * rating
        dwg.add(dwg.text(
            bolts,
            insert=(circle_x, score_y + 140),
            text_anchor="middle",
            font_size="24px",
            font_family="Arial, sans-serif",
            fill=self.theme.accent_color,
        ))

        # Metrics section
        metrics_x = 300
        metrics_y = score_y + 20

        metrics = [
            ("Total Commits", total_commits),
            ("Consistency", f"{spark_score.get('consistency_score', 0)}/100"),
            ("Volume", f"{spark_score.get('volume_score', 0)}/100"),
            ("Collaboration", f"{spark_score.get('collaboration_score', 0)}/100"),
        ]

        for i, (label, value) in enumerate(metrics):
            y = metrics_y + (i * 35)
            dwg.add(dwg.text(
                f"{label}:",
                insert=(metrics_x, y),
                font_size="14px",
                font_family="Arial, sans-serif",
                fill=self.theme.text_color,
            ))
            dwg.add(dwg.text(
                str(value),
                insert=(metrics_x + 150, y),
                font_size="16px",
                font_family="Arial, sans-serif",
                fill=self.theme.primary_color,
                font_weight="bold",
            ))

        # Top languages
        lang_x = 520
        lang_y = score_y + 20

        dwg.add(dwg.text(
            "Top Languages",
            insert=(lang_x, lang_y),
            font_size="16px",
            font_family="Arial, sans-serif",
            fill=self.theme.text_color,
            font_weight="bold",
        ))

        for i, lang in enumerate(languages[:4]):
            y = lang_y + 30 + (i * 30)
            lang_name = lang.get("name", "Unknown")
            percentage = lang.get("percentage", 0)

            # Language bar
            bar_width = 150
            bar_filled = int(bar_width * percentage / 100)

            dwg.add(dwg.rect(
                (lang_x, y - 12),
                (bar_width, 18),
                fill=self.theme.border_color,
                rx=2,
            ))
            dwg.add(dwg.rect(
                (lang_x, y - 12),
                (bar_filled, 18),
                fill=self.theme.primary_color,
                rx=2,
            ))

            # Label
            dwg.add(dwg.text(
                f"{lang_name} {percentage}%",
                insert=(lang_x + bar_width + 10, y),
                font_size="12px",
                font_family="Arial, sans-serif",
                fill=self.theme.text_color,
            ))

        # Time pattern
        pattern = time_pattern.get("category", "unknown")
        pattern_labels = {
            "night_owl": "🦉 Night Owl",
            "early_bird": "🐦 Early Bird",
            "balanced": "⚖️ Balanced",
            "unknown": "⏰ Pattern Unknown",
        }

        dwg.add(dwg.text(
            pattern_labels.get(pattern, "⏰ Pattern Unknown"),
            insert=(width // 2, height - 40),
            text_anchor="middle",
            font_size="16px",
            font_family="Arial, sans-serif",
            fill=self.theme.accent_color,
        ))

        # Powered by footer
        dwg.add(dwg.text(
            "⚡ Generated with Stats Spark",
            insert=(width - 10, height - 10),
            text_anchor="end",
            font_size="10px",
            font_family="Arial, sans-serif",
            fill=self.theme.border_color,
            opacity=0.7,
        ))

        return dwg.tostring()

    def generate_heatmap(
        self,
        commits_by_date: Dict[str, int],
        username: str,
    ) -> str:
        """Generate commit frequency heatmap.

        Args:
            commits_by_date: Dictionary mapping dates to commit counts
            username: GitHub username

        Returns:
            SVG content as string
        """
        width = 900
        height = 200

        dwg = svgwrite.Drawing(size=(width, height))
        dwg.add(dwg.rect((0, 0), (width, height), fill=self.theme.background_color))

        # Title
        dwg.add(dwg.text(
            f"Commit Activity Heatmap - {username}",
            insert=(width // 2, 30),
            text_anchor="middle",
            font_size="20px",
            font_family="Arial, sans-serif",
            fill=self.theme.text_color,
            font_weight="bold",
        ))

        # Heatmap grid
        cell_size = 12
        cell_gap = 2
        start_x = 50
        start_y = 60

        # Create sample heatmap (would be based on actual commit data)
        max_commits = max(commits_by_date.values()) if commits_by_date else 1

        for week in range(52):
            for day in range(7):
                x = start_x + (week * (cell_size + cell_gap))
                y = start_y + (day * (cell_size + cell_gap))

                # Sample intensity (would be based on actual data)
                intensity = 0.2 + (0.8 * ((week + day) % 5) / 5)

                dwg.add(dwg.rect(
                    (x, y),
                    (cell_size, cell_size),
                    fill=self.theme.primary_color,
                    opacity=intensity,
                    rx=2,
                ))

        # Powered by footer
        dwg.add(dwg.text(
            "⚡ Generated with Stats Spark",
            insert=(width - 10, height - 10),
            text_anchor="end",
            font_size="10px",
            font_family="Arial, sans-serif",
            fill=self.theme.border_color,
            opacity=0.7,
        ))

        return dwg.tostring()

    def generate_languages(
        self,
        languages: List[Dict[str, Any]],
        username: str,
    ) -> str:
        """Generate language breakdown bar chart.

        Args:
            languages: List of language statistics
            username: GitHub username

        Returns:
            SVG content as string
        """
        width = 600
        height = 400

        dwg = svgwrite.Drawing(size=(width, height))
        dwg.add(dwg.rect((0, 0), (width, height), fill=self.theme.background_color))

        # Title
        dwg.add(dwg.text(
            f"Language Breakdown - {username}",
            insert=(width // 2, 30),
            text_anchor="middle",
            font_size="20px",
            font_family="Arial, sans-serif",
            fill=self.theme.text_color,
            font_weight="bold",
        ))

        # Language bars
        bar_height = 30
        bar_gap = 10
        start_y = 60
        max_bar_width = width - 200

        for i, lang in enumerate(languages[:10]):
            y = start_y + (i * (bar_height + bar_gap))
            lang_name = lang.get("name", "Unknown")
            percentage = lang.get("percentage", 0)

            # Bar
            bar_width = int(max_bar_width * percentage / 100)
            dwg.add(dwg.rect(
                (100, y),
                (bar_width, bar_height),
                fill=self.theme.primary_color,
                rx=4,
            ))

            # Label
            dwg.add(dwg.text(
                lang_name,
                insert=(10, y + bar_height // 2 + 5),
                font_size="14px",
                font_family="Arial, sans-serif",
                fill=self.theme.text_color,
            ))

            # Percentage
            dwg.add(dwg.text(
                f"{percentage}%",
                insert=(110 + bar_width, y + bar_height // 2 + 5),
                font_size="12px",
                font_family="Arial, sans-serif",
                fill=self.theme.accent_color,
            ))

        # Powered by footer
        dwg.add(dwg.text(
            "⚡ Generated with Stats Spark",
            insert=(width - 10, height - 10),
            text_anchor="end",
            font_size="10px",
            font_family="Arial, sans-serif",
            fill=self.theme.border_color,
            opacity=0.7,
        ))

        return dwg.tostring()

    def generate_fun_stats(
        self,
        stats: Dict[str, Any],
        username: str,
    ) -> str:
        """Generate fun stats and one-liners with personality.

        Args:
            stats: Dictionary of fun statistics
            username: GitHub username

        Returns:
            SVG content as string
        """
        width = 700
        height = 450

        dwg = svgwrite.Drawing(size=(width, height))
        dwg.add(dwg.rect((0, 0), (width, height), fill=self.theme.background_color))

        # Title with flair
        dwg.add(dwg.text(
            f"⚡ Lightning Round Stats - {username}",
            insert=(width // 2, 30),
            text_anchor="middle",
            font_size="22px",
            font_family="Arial, sans-serif",
            fill=self.theme.accent_color,
            font_weight="bold",
        ))

        # Extract stats
        most_active_hour = stats.get('most_active_hour', 0)
        pattern = stats.get('pattern', 'Unknown')
        total_repos = stats.get('total_repos', 0)
        account_age_days = stats.get('account_age_days', 0)
        total_commits = stats.get('total_commits', 0)
        languages_count = stats.get('languages_count', 0)
        total_stars = stats.get('total_stars', 0)
        avg_commits_per_day = stats.get('avg_commits_per_day', 0)

        # Generate creative fun facts with personality
        facts = []

        # Time-based facts with personality
        if most_active_hour >= 22 or most_active_hour <= 4:
            facts.append(f"🦉 Night Owl Alert! Peaks at {most_active_hour}:00 (coffee budget: infinite)")
        elif most_active_hour >= 5 and most_active_hour <= 9:
            facts.append(f"🌅 Early Bird! Most active at {most_active_hour}:00 (the worm is caught!)")
        else:
            facts.append(f"☀️ Daytime Coder! Peaks at {most_active_hour}:00 (normal sleep schedule)")

        # Commit velocity with flair
        if avg_commits_per_day > 10:
            facts.append(f"🚀 Commit Machine! Averaging {avg_commits_per_day:.1f} commits/day")
        elif avg_commits_per_day > 5:
            facts.append(f"💪 Consistent Contributor: {avg_commits_per_day:.1f} commits/day")
        elif avg_commits_per_day > 1:
            facts.append(f"📝 Steady Progress: {avg_commits_per_day:.1f} commits/day")
        else:
            facts.append(f"🌱 Quality over Quantity: {avg_commits_per_day:.1f} commits/day")

        # Repository count with achievements
        if total_repos > 100:
            facts.append(f"🏆 Repository Collector: {total_repos} repos (impressive!)")
        elif total_repos > 50:
            facts.append(f"📚 Project Enthusiast: {total_repos} repositories")
        elif total_repos > 20:
            facts.append(f"🔧 Builder Mode: {total_repos} active projects")
        else:
            facts.append(f"🎯 Focused Developer: {total_repos} repositories")

        # Language diversity
        if languages_count > 10:
            facts.append(f"🌐 Polyglot Programmer: {languages_count} languages mastered!")
        elif languages_count > 5:
            facts.append(f"🛠️ Multi-Language Dev: {languages_count} languages in toolkit")
        elif languages_count > 2:
            facts.append(f"💻 Versatile Coder: {languages_count} languages")
        else:
            facts.append(f"🎨 Specialist: {languages_count} language{'s' if languages_count != 1 else ''}")

        # Stars and popularity
        if total_stars > 1000:
            facts.append(f"⭐ GitHub Celebrity: {total_stars} stars earned!")
        elif total_stars > 100:
            facts.append(f"✨ Community Favorite: {total_stars} stars")
        elif total_stars > 10:
            facts.append(f"🌟 Growing Recognition: {total_stars} stars")
        else:
            facts.append(f"💫 Building Reputation: {total_stars} stars")

        # Account longevity
        account_years = account_age_days / 365.25
        if account_years > 10:
            facts.append(f"🏛️ GitHub Veteran: {account_age_days} days ({int(account_years)} years!)")
        elif account_years > 5:
            facts.append(f"🎖️ Experienced Dev: {account_age_days} days on GitHub")
        elif account_years > 2:
            facts.append(f"📅 Established Member: {int(account_years)} years on GitHub")
        else:
            facts.append(f"🌱 Growing Journey: {account_age_days} days on GitHub")

        # Total commits milestone
        if total_commits > 10000:
            facts.append(f"🔥 Commit Legend: {total_commits:,} total commits!")
        elif total_commits > 5000:
            facts.append(f"💥 Commit Master: {total_commits:,} total commits")
        elif total_commits > 1000:
            facts.append(f"⚡ Active Developer: {total_commits:,} commits")
        elif total_commits > 100:
            facts.append(f"📈 Building Momentum: {total_commits} commits")
        else:
            facts.append(f"🚀 Just Getting Started: {total_commits} commits")

        # Coding pattern personality
        pattern_descriptions = {
            "night_owl": "🌙 Debugs best after midnight",
            "early_bird": "🌄 Codes before the world wakes",
            "balanced": "⚖️ Perfectly balanced workflow",
            "weekend_warrior": "🎮 Weekend coding sessions",
            "weekday_grinder": "💼 Monday-Friday hustle",
        }
        if pattern in pattern_descriptions:
            facts.append(pattern_descriptions[pattern])

        # Limit to 8 facts to fit nicely
        facts = facts[:8]

        # Render facts in two columns
        left_col_x = 40
        right_col_x = 370
        start_y = 70
        spacing = 45

        for i, fact in enumerate(facts):
            if i < 4:
                # Left column
                x = left_col_x
                y = start_y + (i * spacing)
            else:
                # Right column
                x = right_col_x
                y = start_y + ((i - 4) * spacing)

            # Add fact with icon and text
            dwg.add(dwg.text(
                fact,
                insert=(x, y),
                font_size="16px",
                font_family="Arial, sans-serif",
                fill=self.theme.text_color,
            ))

        # Add a fun footer message
        footer_messages = [
            "Keep coding, keep sparking! ⚡",
            "You're doing amazing! 🌟",
            "The code is strong with this one 💪",
            "Commits speak louder than words 📝",
            "Building the future, one commit at a time 🚀",
        ]
        import random
        random.seed(hash(username))  # Consistent message per user
        footer_msg = random.choice(footer_messages)

        dwg.add(dwg.text(
            footer_msg,
            insert=(width // 2, height - 40),
            text_anchor="middle",
            font_size="14px",
            font_family="Arial, sans-serif",
            fill=self.theme.primary_color,
            opacity=0.8,
            font_style="italic",
        ))

        # Powered by footer
        dwg.add(dwg.text(
            "⚡ Generated with Stats Spark",
            insert=(width - 10, height - 10),
            text_anchor="end",
            font_size="10px",
            font_family="Arial, sans-serif",
            fill=self.theme.border_color,
            opacity=0.7,
        ))

        return dwg.tostring()

    def generate_streaks(
        self,
        streaks: Dict[str, Any],
        username: str,
    ) -> str:
        """Generate coding streaks visualization.

        Args:
            streaks: Streak statistics
            username: GitHub username

        Returns:
            SVG content as string
        """
        width = 600
        height = 250

        dwg = svgwrite.Drawing(size=(width, height))
        dwg.add(dwg.rect((0, 0), (width, height), fill=self.theme.background_color))

        # Title
        dwg.add(dwg.text(
            f"Coding Streaks - {username}",
            insert=(width // 2, 30),
            text_anchor="middle",
            font_size="20px",
            font_family="Arial, sans-serif",
            fill=self.theme.text_color,
            font_weight="bold",
        ))

        # Current streak
        dwg.add(dwg.text(
            "🔥 Current Streak",
            insert=(100, 100),
            font_size="16px",
            font_family="Arial, sans-serif",
            fill=self.theme.text_color,
        ))
        dwg.add(dwg.text(
            f"{streaks.get('current_streak', 0)} days",
            insert=(100, 130),
            font_size="32px",
            font_family="Arial, sans-serif",
            fill=self.theme.accent_color,
            font_weight="bold",
        ))

        # Longest streak
        dwg.add(dwg.text(
            "🏆 Longest Streak",
            insert=(400, 100),
            font_size="16px",
            font_family="Arial, sans-serif",
            fill=self.theme.text_color,
        ))
        dwg.add(dwg.text(
            f"{streaks.get('longest_streak', 0)} days",
            insert=(400, 130),
            font_size="32px",
            font_family="Arial, sans-serif",
            fill=self.theme.primary_color,
            font_weight="bold",
        ))

        # Powered by footer
        dwg.add(dwg.text(
            "⚡ Generated with Stats Spark",
            insert=(width - 10, height - 10),
            text_anchor="end",
            font_size="10px",
            font_family="Arial, sans-serif",
            fill=self.theme.border_color,
            opacity=0.7,
        ))

        return dwg.tostring()


def get_theme(theme_name: str, themes_config: Optional[Dict[str, Any]] = None) -> Theme:
    """Get theme instance by name.

    Args:
        theme_name: Theme name (spark-dark, spark-light, or custom)
        themes_config: Optional themes configuration for custom themes

    Returns:
        Theme instance
    """
    if theme_name == "spark-dark":
        return SparkDarkTheme()
    elif theme_name == "spark-light":
        return SparkLightTheme()
    else:
        # Custom theme
        if not themes_config:
            raise ValueError(f"Custom theme '{theme_name}' requires themes configuration")
        return CustomTheme.load_from_yaml(themes_config, theme_name)
