"""Portfolio intelligence classification engine.

Assigns each public non-forked repository to a Core/Supporting/Archive tier
using deterministic rule-based thresholds. Classification does not require AI
or any external API calls — it operates purely on cached repo metadata.

Classification rules (priority-ordered, first match wins):
  Core:       pushed ≤90d AND commits_90d ≥5 AND (has_tests OR has_ci_cd)
  Supporting: pushed ≤365d OR commits_90d ≥1
  Archive:    all remaining repositories

Signal score formula (0–100, equal-weight):
  recency_score  = max(0, 100 - days_since_push / 365 * 100)
  volume_score   = min(100, commits_90d / 30 * 100)
  tier_score     = Core→100, Supporting→60, Archive→20
  signal_score   = round((recency + volume + tier) / 3)
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional

from spark.logger import get_logger

_TIER_SCORE: Dict[str, int] = {"core": 100, "supporting": 60, "archive": 20}
_RELEVANCE: Dict[str, str] = {"core": "high", "supporting": "medium", "archive": "low"}

_CORE_MAX_DAYS = 90
_CORE_MIN_COMMITS = 5
_SUPPORTING_MAX_DAYS = 365


@dataclass
class ClassificationResult:
    """Output of a single repository classification."""

    classification: str   # core | supporting | archive
    signal_score: int     # 0–100
    relevance: str        # high | medium | low
    notes: str            # human-readable context phrase


class RepositoryClassifier:
    """Classifies repositories and computes portfolio signal scores."""

    def __init__(self, overrides: Optional[Dict[str, str]] = None) -> None:
        self._overrides: Dict[str, str] = overrides or {}
        self._wildcard: Optional[str] = self._overrides.get("*")
        self.logger = get_logger()

    def classify(
        self,
        repo_name: str,
        commits_90d: int,
        days_since_push: int,
        has_tests: bool,
        has_ci_cd: bool,
        override_notes: Optional[str] = None,
    ) -> ClassificationResult:
        """Classify a single repository.

        Config overrides take priority over automated rules. Wildcard '*'
        sets the default for repos not explicitly named.
        """
        tier = self._resolve_tier(repo_name, commits_90d, days_since_push, has_tests, has_ci_cd)
        score = self.compute_signal_score(days_since_push, commits_90d, tier)
        relevance = _RELEVANCE[tier]
        notes = self.generate_notes(tier, commits_90d, override_notes)
        return ClassificationResult(
            classification=tier,
            signal_score=score,
            relevance=relevance,
            notes=notes,
        )

    def classify_repo_dict(self, repo_dict: Dict[str, Any]) -> ClassificationResult:
        """Classify using a repo_dict as produced by unified_data_generator."""
        name = repo_dict.get("name", "")
        commits_90d = repo_dict.get("recent_commits_90d") or 0
        pushed_at = repo_dict.get("pushed_at")
        days_since_push = repo_dict.get("days_since_last_push") or 0
        has_tests = bool(repo_dict.get("has_tests", False))
        has_ci_cd = bool(repo_dict.get("has_ci_cd", False))

        # Config-level notes override
        override_notes: Optional[str] = None
        raw_override = self._overrides.get(name) or self._overrides.get("*")
        if raw_override and name in self._overrides:
            override_notes = None  # tier came from config; notes auto-generated

        return self.classify(
            repo_name=name,
            commits_90d=int(commits_90d),
            days_since_push=int(days_since_push),
            has_tests=has_tests,
            has_ci_cd=has_ci_cd,
            override_notes=override_notes,
        )

    def _resolve_tier(
        self,
        repo_name: str,
        commits_90d: int,
        days_since_push: int,
        has_tests: bool,
        has_ci_cd: bool,
    ) -> str:
        """Resolve classification tier with override priority."""
        # Named override takes highest priority
        if repo_name in self._overrides:
            return self._overrides[repo_name]

        # Automated rules
        automated = self._automated_tier(commits_90d, days_since_push, has_tests, has_ci_cd)

        # Wildcard default: only applies when automated would give archive
        # and an explicit wildcard exists
        if self._wildcard is not None and automated == "archive":
            return self._wildcard

        return automated

    @staticmethod
    def _automated_tier(
        commits_90d: int,
        days_since_push: int,
        has_tests: bool,
        has_ci_cd: bool,
    ) -> str:
        """Apply three-factor priority-ordered classification rules."""
        if (
            days_since_push <= _CORE_MAX_DAYS
            and commits_90d >= _CORE_MIN_COMMITS
            and (has_tests or has_ci_cd)
        ):
            return "core"
        if days_since_push <= _SUPPORTING_MAX_DAYS or commits_90d >= 1:
            return "supporting"
        return "archive"

    @staticmethod
    def compute_signal_score(days_since_push: int, commits_90d: int, classification: str) -> int:
        """Compute 0–100 signal score using equal-weight formula.

        recency  = max(0, 100 - days_since_push / 365 * 100)
        volume   = min(100, commits_90d / 30 * 100)
        tier     = Core→100, Supporting→60, Archive→20
        score    = round((recency + volume + tier) / 3)
        """
        recency = max(0.0, 100.0 - (days_since_push / 365.0 * 100.0))
        volume = min(100.0, commits_90d / 30.0 * 100.0)
        tier_score = float(_TIER_SCORE.get(classification, 20))
        return round((recency + volume + tier_score) / 3.0)

    @staticmethod
    def generate_notes(
        classification: str,
        commits_90d: int,
        override_notes: Optional[str] = None,
    ) -> str:
        """Generate a human-readable notes phrase for the repository.

        Uses override_notes verbatim when provided; otherwise generates a
        tier-based phrase from activity signals.
        """
        if override_notes:
            return override_notes

        if classification == "core":
            if commits_90d >= 10:
                return f"Actively maintained core system with {commits_90d} commits in the last 90 days"
            return "Core system in the portfolio; maintained with focused recent activity"

        if classification == "supporting":
            if commits_90d >= 1:
                return "Supporting project with recent updates"
            return "Supporting project; periodically maintained"

        return "Historical project; no longer actively maintained"
