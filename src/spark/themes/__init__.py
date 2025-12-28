"""Theme system for Stats Spark visualizations."""

from abc import ABC, abstractmethod
from typing import Dict, Any


class Theme(ABC):
    """Base class for all themes."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Theme name."""
        pass

    @property
    @abstractmethod
    def primary_color(self) -> str:
        """Primary color for main elements."""
        pass

    @property
    @abstractmethod
    def accent_color(self) -> str:
        """Accent color for highlights."""
        pass

    @property
    @abstractmethod
    def background_color(self) -> str:
        """Background color."""
        pass

    @property
    @abstractmethod
    def text_color(self) -> str:
        """Text color."""
        pass

    @property
    @abstractmethod
    def border_color(self) -> str:
        """Border color."""
        pass

    @property
    def effects(self) -> Dict[str, Any]:
        """Visual effects configuration.

        Returns:
            Dict with glow, gradient, animations flags
        """
        return {
            "glow": True,
            "gradient": True,
            "animations": False,
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert theme to dictionary.

        Returns:
            Theme configuration as dict
        """
        return {
            "name": self.name,
            "primary_color": self.primary_color,
            "accent_color": self.accent_color,
            "background_color": self.background_color,
            "text_color": self.text_color,
            "border_color": self.border_color,
            "effects": self.effects,
        }


__all__ = ["Theme"]
