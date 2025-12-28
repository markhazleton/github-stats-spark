"""Spark Light theme - Light theme with bright colors and WCAG AA compliance."""

from spark.themes import Theme


class SparkLightTheme(Theme):
    """Light theme with bright backgrounds and accessible contrast."""

    @property
    def name(self) -> str:
        """Theme name."""
        return "spark-light"

    @property
    def primary_color(self) -> str:
        """Deep blue primary color (WCAG AA compliant)."""
        return "#0369A1"

    @property
    def accent_color(self) -> str:
        """Deep gold accent color (WCAG AA compliant)."""
        return "#CA8A04"

    @property
    def background_color(self) -> str:
        """Light background."""
        return "#FFFFFF"

    @property
    def text_color(self) -> str:
        """Dark text for light background."""
        return "#1F2937"

    @property
    def border_color(self) -> str:
        """Light border color."""
        return "#E5E7EB"

    @property
    def effects(self):
        """Minimal effects for light theme."""
        return {
            "glow": False,
            "gradient": True,
            "animations": False,
        }
