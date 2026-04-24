"""Repository summary entity model for AI-generated content."""

import json
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any


@dataclass
class RepositorySummary:
    """Represents a repository summary with AI-generated or fallback content.

    This model stores the summary text along with metadata about how it
    was generated (AI model, fallback tier, generation timestamp).

    Attributes:
        repo_id: Repository identifier (name or full_name)
        ai_summary: AI-generated summary text (if available)
        fallback_summary: Template-based fallback summary
        generation_method: How summary was generated (claude-haiku, enhanced-template, basic-template)
        generation_timestamp: When summary was generated
        model_used: AI model identifier (e.g., "claude-haiku-3.5")
        tokens_used: Number of tokens consumed (if AI-generated)
        confidence_score: 0-100 confidence in summary quality
        error_message: Error details if generation failed
    """

    repo_id: str
    ai_summary: Optional[str] = None
    fallback_summary: Optional[str] = None
    generation_method: str = "unknown"
    generation_timestamp: Optional[datetime] = None
    model_used: Optional[str] = None
    tokens_used: int = 0
    confidence_score: int = 0
    error_message: Optional[str] = None

    @property
    def portfolio_intelligence(self) -> Optional[Dict[str, Any]]:
        """Parse AI summary as portfolio intelligence JSON when available."""
        if not self.ai_summary:
            return None
        try:
            parsed = json.loads(self.ai_summary)
            if isinstance(parsed, dict) and "role" in parsed:
                return parsed
        except (json.JSONDecodeError, ValueError):
            pass
        return None

    @property
    def summary(self) -> str:
        """Get the best available summary (AI or fallback).

        When the AI summary is portfolio intelligence JSON, returns the
        positioning line — the human-readable sentence describing the repo's
        portfolio role. Falls back to the raw string for legacy summaries.
        """
        if self.ai_summary:
            pi = self.portfolio_intelligence
            if pi:
                return pi.get("positioning") or pi.get("what") or self.ai_summary
            return self.ai_summary
        elif self.fallback_summary:
            return self.fallback_summary
        elif self.error_message:
            return f"Summary generation failed: {self.error_message}"
        else:
            return "No summary available."

    @property
    def is_ai_generated(self) -> bool:
        """Check if summary was AI-generated.

        Returns:
            True if summary used AI model, False if fallback
        """
        return self.generation_method.startswith("claude") or self.generation_method.startswith("gpt")

    @property
    def summary_length(self) -> int:
        """Get character count of the summary.

        Returns:
            Number of characters in the summary text
        """
        return len(self.summary)

    def to_dict(self) -> dict:
        """Serialize summary to dictionary format."""
        result = {
            "repo_id": self.repo_id,
            "ai_summary": self.ai_summary,
            "fallback_summary": self.fallback_summary,
            "summary": self.summary,
            "generation_method": self.generation_method,
            "generation_timestamp": self.generation_timestamp.isoformat() if self.generation_timestamp else None,
            "model_used": self.model_used,
            "tokens_used": self.tokens_used,
            "confidence_score": self.confidence_score,
            "error_message": self.error_message,
            "is_ai_generated": self.is_ai_generated,
            "summary_length": self.summary_length,
        }
        pi = self.portfolio_intelligence
        if pi:
            result["portfolio_intelligence"] = pi
        return result
