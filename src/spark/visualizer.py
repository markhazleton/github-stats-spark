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
        """Generate fun stats and one-liners.

        Args:
            stats: Dictionary of fun statistics
            username: GitHub username

        Returns:
            SVG content as string
        """
        width = 600
        height = 300

        dwg = svgwrite.Drawing(size=(width, height))
        dwg.add(dwg.rect((0, 0), (width, height), fill=self.theme.background_color))

        # Title
        dwg.add(dwg.text(
            f"⚡ Lightning Round Stats - {username}",
            insert=(width // 2, 30),
            text_anchor="middle",
            font_size="20px",
            font_family="Arial, sans-serif",
            fill=self.theme.accent_color,
            font_weight="bold",
        ))

        # Fun facts
        facts = [
            f"Most active hour: {stats.get('most_active_hour', 'Unknown')}:00",
            f"Coding pattern: {stats.get('pattern', 'Unknown')}",
            f"Total repositories: {stats.get('total_repos', 0)}",
            f"Account age: {stats.get('account_age_days', 0)} days",
        ]

        start_y = 80
        for i, fact in enumerate(facts):
            y = start_y + (i * 50)
            dwg.add(dwg.text(
                f"• {fact}",
                insert=(50, y),
                font_size="18px",
                font_family="Arial, sans-serif",
                fill=self.theme.text_color,
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
