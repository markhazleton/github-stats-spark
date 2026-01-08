"""Configuration management for Stats Spark."""

import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


class SparkConfig:
    """Manages Stats Spark configuration from YAML files."""

    VALID_STATS_CATEGORIES = ["overview", "heatmap", "languages", "fun", "streaks", "release"]
    BUILT_IN_THEMES = ["spark-dark", "spark-light"]

    def __init__(self, config_path: str = "config/spark.yml"):
        """Initialize configuration.

        Args:
            config_path: Path to main configuration file
        """
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = {}
        self.themes_config: Dict[str, Any] = {}

    def load(self) -> None:
        """Load configuration from YAML file."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        with open(self.config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

        # Load themes configuration
        themes_path = self.config_path.parent / "themes.yml"
        if themes_path.exists():
            with open(themes_path, "r", encoding="utf-8") as f:
                self.themes_config = yaml.safe_load(f)

    def validate(self) -> List[str]:
        """Validate configuration and return list of errors.

        Returns:
            List of validation error messages (empty if valid)
        """
        errors = []

        # Validate required fields
        if "stats" not in self.config:
            errors.append("Missing required 'stats' section")
            return errors

        # Validate stats.enabled
        enabled = self.config.get("stats", {}).get("enabled", [])
        if not isinstance(enabled, list):
            errors.append("stats.enabled must be a list")
        else:
            invalid_categories = [
                cat for cat in enabled if cat not in self.VALID_STATS_CATEGORIES
            ]
            if invalid_categories:
                errors.append(
                    f"Invalid statistics categories: {', '.join(invalid_categories)}. "
                    f"Valid options: {', '.join(self.VALID_STATS_CATEGORIES)}"
                )

        # Validate theme
        theme = self.config.get("visualization", {}).get("theme")
        if theme:
            if theme not in self.BUILT_IN_THEMES and theme != "custom":
                if "custom_themes" not in self.themes_config:
                    errors.append(
                        f"Theme '{theme}' not found. Must be one of: "
                        f"{', '.join(self.BUILT_IN_THEMES + ['custom'])}"
                    )

        return errors

    def get_theme(self) -> str:
        """Get the configured theme name.

        Returns:
            Theme name (default: spark-dark)
        """
        return self.config.get("visualization", {}).get("theme", "spark-dark")

    def get_enabled_stats(self) -> List[str]:
        """Get list of enabled statistics categories.

        Returns:
            List of enabled category names
        """
        return self.config.get("stats", {}).get("enabled", self.VALID_STATS_CATEGORIES)

    def get_user(self) -> str:
        """Get the configured username.

        Returns:
            Username or 'auto' to detect from environment
        """
        user = self.config.get("user", "auto")
        if user == "auto":
            # Auto-detect from GITHUB_REPOSITORY environment variable
            repo = os.getenv("GITHUB_REPOSITORY", "")
            if repo:
                return repo.split("/")[0]
        return user

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value by key.

        Args:
            key: Configuration key (supports dot notation, e.g., 'stats.enabled')
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        keys = key.split(".")
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
            if value is None:
                return default
        return value
