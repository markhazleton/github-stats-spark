"""Helpers for coordinating cache refresh categories and decisions."""

from collections.abc import Callable
from datetime import datetime
from typing import Set


BASE_REFRESH_CATEGORIES = frozenset({
    "commit_counts",
    "commits_stats",
    "languages",
    "contributor_stats",
    "code_frequency",
    "quality_indicators",
    "pull_request_summary",
    "security_summary",
})
AI_REFRESH_CATEGORIES = frozenset({"readme", "dependency_files", "ai_summary"})


def get_refresh_categories(include_ai_summaries: bool = False) -> Set[str]:
    """Return the cache categories that participate in a refresh run."""
    categories = set(BASE_REFRESH_CATEGORIES)
    if include_ai_summaries:
        categories.update(AI_REFRESH_CATEGORIES)
    return categories


def should_refresh_repository(
    needs_refresh: Callable[[str, str, str, datetime], bool],
    username: str,
    repo_name: str,
    pushed_at: datetime,
    include_ai_summaries: bool = False,
) -> bool:
    """Determine whether any relevant category is missing or stale."""
    return any(
        needs_refresh(username, repo_name, category, pushed_at)
        for category in get_refresh_categories(include_ai_summaries)
    )