"""Spark Dark theme - Default dark theme with electric blue accents."""

from spark.themes import Theme


class SparkDarkTheme(Theme):
    """Dark theme with electric blue primary and gold accents."""

    @property
    def name(self) -> str:
        """Theme name."""
        return "spark-dark"

    @property
    def primary_color(self) -> str:
        """Electric blue primary color."""
        return "#0EA5E9"

    @property
    def accent_color(self) -> str:
        """Gold accent color."""
        return "#FCD34D"

    @property
    def background_color(self) -> str:
        """Dark background."""
        return "#0D1117"

    @property
    def text_color(self) -> str:
        """Light text for dark background."""
        return "#C9D1D9"

    @property
    def border_color(self) -> str:
        """Subtle border color."""
        return "#30363D"

    @property
    def effects(self):
        """Enable glow and gradient effects."""
        return {
            "glow": True,
            "gradient": True,
            "animations": False,
        }
