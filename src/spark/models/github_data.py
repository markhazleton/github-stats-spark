"""GitHubData entity for intermediate workflow data sharing."""

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

from spark.models.profile import UserProfile
from spark.models.repository import Repository
from spark.models.commit import CommitHistory


@dataclass
class GitHubData:
    """Container for GitHub API data used across workflow stages.

    This entity encapsulates all data fetched from the GitHub API in a single
    stage, enabling efficient data sharing between SVG generation and repository
    analysis stages without re-fetching.

    Attributes:
        username: GitHub username being analyzed
        profile: User profile data including bio, stats, and metadata
        repositories: List of all fetched repositories
        commit_histories: Commit data indexed by repository name
        fetch_timestamp: When the data was fetched from GitHub API
        api_call_count: Number of GitHub API calls made to fetch this data
        cache_hit_count: Number of requests served from cache
    """

    username: str
    profile: UserProfile
    repositories: List[Repository]
    commit_histories: Dict[str, CommitHistory]
    fetch_timestamp: datetime
    api_call_count: int = 0
    cache_hit_count: int = 0

    @property
    def cache_efficiency(self) -> float:
        """Calculate percentage of requests served from cache.

        Returns:
            Float between 0.0 and 100.0 representing cache hit rate.
            Returns 0.0 if no requests were made.
        """
        total = self.api_call_count + self.cache_hit_count
        return (self.cache_hit_count / total * 100.0) if total > 0 else 0.0

    @property
    def total_repositories(self) -> int:
        """Total number of repositories fetched.

        Returns:
            Count of repositories in the repositories list.
        """
        return len(self.repositories)

    def to_dict(self) -> dict:
        """Serialize to dictionary for logging and debugging.

        Returns:
            Dictionary representation with serialized nested objects.
        """
        return {
            "username": self.username,
            "profile": self.profile.to_dict() if self.profile else None,
            "total_repositories": self.total_repositories,
            "fetch_timestamp": self.fetch_timestamp.isoformat(),
            "api_call_count": self.api_call_count,
            "cache_hit_count": self.cache_hit_count,
            "cache_efficiency": self.cache_efficiency,
        }
