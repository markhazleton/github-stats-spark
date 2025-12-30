"""Repository entity model for GitHub repository analysis."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional


@dataclass
class Repository:
    """Represents a GitHub repository with metadata and statistics.

    This model contains all essential information about a repository needed
    for ranking, analysis, and report generation.

    Attributes:
        name: Repository name (without owner prefix)
        description: Repository description from GitHub
        url: Full HTTPS URL to the repository
        created_at: Repository creation timestamp
        updated_at: Last update timestamp (any change)
        pushed_at: Last push timestamp (code changes)
        primary_language: Primary programming language
        language_stats: Dictionary of languages to bytes of code
        stars: Star count
        forks: Fork count
        watchers: Watcher count
        open_issues: Count of open issues
        is_archived: Whether repository is archived
        is_fork: Whether repository is a fork
        fork_info: For forks, commits ahead/behind parent (optional)
        has_readme: Whether a README file exists
        size_kb: Repository size in kilobytes
        is_private: Whether repository is private (should always be False per constitution)
        contributors_count: Number of contributors (Tier 1)
        language_count: Number of distinct programming languages (Tier 1)
        has_ci_cd: Whether repository has CI/CD workflows (Quality Focus)
        has_tests: Whether repository has tests directory (Quality Focus)
        has_license: Whether repository has LICENSE file (Quality Focus)
        has_docs: Whether repository has documentation (Quality Focus)
        release_count: Total number of releases (Activity Focus)
        latest_release_date: Date of most recent release (Activity Focus)
        commit_velocity: Commits per month trend (Activity Focus)
    """

    name: str
    description: Optional[str]
    url: str
    created_at: datetime
    updated_at: datetime
    pushed_at: Optional[datetime]
    primary_language: Optional[str]
    language_stats: Dict[str, int] = field(default_factory=dict)
    stars: int = 0
    forks: int = 0
    watchers: int = 0
    open_issues: int = 0
    is_archived: bool = False
    is_fork: bool = False
    fork_info: Optional[Dict[str, int]] = None  # {"commits_ahead": X, "commits_behind": Y}
    has_readme: bool = False
    size_kb: int = 0
    is_private: bool = False
    # Tier 1 - Quick Enhancement
    contributors_count: int = 0
    language_count: int = 0
    # Quality Focus
    has_ci_cd: bool = False
    has_tests: bool = False
    has_license: bool = False
    has_docs: bool = False
    # Activity Focus
    release_count: int = 0
    latest_release_date: Optional[datetime] = None
    commit_velocity: Optional[float] = None  # commits per month

    def __post_init__(self):
        """Validate that private repositories are never processed."""
        if self.is_private:
            raise ValueError(
                f"Privacy violation: Attempted to process private repository '{self.name}'. "
                "Only public repositories are allowed per constitution III."
            )

    @property
    def age_days(self) -> int:
        """Calculate repository age in days from creation."""
        if not self.created_at:
            return 0
        from datetime import timezone
        now = datetime.now(timezone.utc)
        # Ensure both datetimes are timezone-aware
        created = self.created_at if self.created_at.tzinfo else self.created_at.replace(tzinfo=timezone.utc)
        delta = now - created
        return max(0, delta.days)

    @property
    def days_since_last_push(self) -> Optional[int]:
        """Calculate days since last push."""
        if not self.pushed_at:
            return None
        from datetime import timezone
        now = datetime.now(timezone.utc)
        # Ensure both datetimes are timezone-aware
        pushed = self.pushed_at if self.pushed_at.tzinfo else self.pushed_at.replace(tzinfo=timezone.utc)
        delta = now - pushed
        return max(0, delta.days)

    @property
    def is_empty(self) -> bool:
        """Check if repository appears empty (no commits, minimal size)."""
        return self.pushed_at is None and self.size_kb < 10

    def to_dict(self) -> dict:
        """Serialize repository to dictionary format.

        Returns:
            Dictionary with all repository fields, with datetimes as ISO strings
        """
        return {
            "name": self.name,
            "description": self.description,
            "url": self.url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "pushed_at": self.pushed_at.isoformat() if self.pushed_at else None,
            "primary_language": self.primary_language,
            "language_stats": self.language_stats,
            "stars": self.stars,
            "forks": self.forks,
            "watchers": self.watchers,
            "open_issues": self.open_issues,
            "is_archived": self.is_archived,
            "is_fork": self.is_fork,
            "fork_info": self.fork_info,
            "has_readme": self.has_readme,
            "size_kb": self.size_kb,
            "is_private": self.is_private,
            "age_days": self.age_days,
            "days_since_last_push": self.days_since_last_push,
            # Tier 1
            "contributors_count": self.contributors_count,
            "language_count": self.language_count,
            # Quality Focus
            "has_ci_cd": self.has_ci_cd,
            "has_tests": self.has_tests,
            "has_license": self.has_license,
            "has_docs": self.has_docs,
            # Activity Focus
            "release_count": self.release_count,
            "latest_release_date": self.latest_release_date.isoformat() if self.latest_release_date else None,
            "commit_velocity": self.commit_velocity,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Repository":
        """Create Repository from dictionary (e.g., from API cache).

        Args:
            data: Dictionary with repository data

        Returns:
            Repository instance

        Raises:
            ValueError: If repository is private (constitution violation)
        """
        from datetime import datetime
        
        # Parse datetime strings
        created_at = datetime.fromisoformat(data["created_at"]) if data.get("created_at") else datetime.now()
        updated_at = datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else datetime.now()
        pushed_at = datetime.fromisoformat(data["pushed_at"]) if data.get("pushed_at") else None
        
        return cls(
            name=data.get("name", ""),
            description=data.get("description"),
            url=data.get("url", f"https://github.com/{data.get('full_name', '')}"),
            created_at=created_at,
            updated_at=updated_at,
            pushed_at=pushed_at,
            primary_language=data.get("language"),
            language_stats={},  # Will be populated separately
            stars=data.get("stars", 0),
            forks=data.get("forks", 0),
            watchers=data.get("watchers", 0),
            open_issues=data.get("open_issues", 0),
            is_archived=data.get("is_archived", False),
            is_fork=data.get("is_fork", False),
            fork_info=data.get("fork_info"),
            has_readme=data.get("has_readme", False),
            size_kb=data.get("size", 0),
            is_private=data.get("is_private", False),
            contributors_count=data.get("contributors_count", 0),
            language_count=data.get("language_count", 0),
            has_ci_cd=data.get("has_ci_cd", False),
            has_tests=data.get("has_tests", False),
            has_license=data.get("has_license", False),
            has_docs=data.get("has_docs", False),
            release_count=data.get("release_count", 0),
            latest_release_date=None,
            commit_velocity=data.get("commit_velocity"),
        )

    @classmethod
    def from_github_repo(cls, github_repo) -> "Repository":
        """Create Repository from PyGithub Repository object.

        Args:
            github_repo: PyGithub Repository instance

        Returns:
            Repository instance with data extracted from GitHub API

        Raises:
            ValueError: If repository is private (constitution violation)
        """
        # Check README existence (basic check)
        has_readme = False
        try:
            github_repo.get_readme()
            has_readme = True
        except:
            pass

        # Extract fork info if applicable
        fork_info = None
        if github_repo.fork and github_repo.parent:
            # Note: commits_ahead/behind requires comparison API call
            # This will be populated by fetcher.py if needed
            fork_info = {"commits_ahead": 0, "commits_behind": 0}

        # Tier 1 - Get contributors count
        contributors_count = 0
        try:
            contributors_count = github_repo.get_contributors().totalCount
        except:
            pass

        # Quality Focus - Check for CI/CD workflows
        has_ci_cd = False
        try:
            workflows = github_repo.get_workflows()
            has_ci_cd = workflows.totalCount > 0
        except:
            pass

        # Quality Focus - Check for tests directory
        has_tests = False
        try:
            contents = github_repo.get_contents("")
            for item in contents:
                if item.type == "dir" and item.name.lower() in ["test", "tests", "spec", "specs", "__tests__"]:
                    has_tests = True
                    break
        except:
            pass

        # Quality Focus - Check for LICENSE file
        has_license = False
        try:
            github_repo.get_license()
            has_license = True
        except:
            pass

        # Quality Focus - Check for documentation
        has_docs = False
        try:
            contents = github_repo.get_contents("")
            for item in contents:
                if item.type == "dir" and item.name.lower() in ["docs", "doc", "documentation"]:
                    has_docs = True
                    break
                if item.type == "file" and item.name.upper() in ["CONTRIBUTING.md", "CHANGELOG.md"]:
                    has_docs = True
                    break
        except:
            pass

        # Activity Focus - Get release information
        release_count = 0
        latest_release_date = None
        try:
            releases = github_repo.get_releases()
            release_count = releases.totalCount
            if release_count > 0:
                latest_release = releases[0]
                latest_release_date = latest_release.created_at
        except:
            pass

        return cls(
            name=github_repo.name,
            description=github_repo.description,
            url=github_repo.html_url,
            created_at=github_repo.created_at,
            updated_at=github_repo.updated_at,
            pushed_at=github_repo.pushed_at,
            primary_language=github_repo.language,
            language_stats={},  # Will be populated by fetcher.get_languages()
            stars=github_repo.stargazers_count,
            forks=github_repo.forks_count,
            watchers=github_repo.watchers_count,
            open_issues=github_repo.open_issues_count,
            is_archived=github_repo.archived,
            is_fork=github_repo.fork,
            fork_info=fork_info,
            has_readme=has_readme,
            size_kb=github_repo.size,
            is_private=github_repo.private,
            # Tier 1
            contributors_count=contributors_count,
            language_count=0,  # Will be set after language_stats populated
            # Quality Focus
            has_ci_cd=has_ci_cd,
            has_tests=has_tests,
            has_license=has_license,
            has_docs=has_docs,
            # Activity Focus
            release_count=release_count,
            latest_release_date=latest_release_date,
            commit_velocity=None,  # Will be calculated from commit history
        )
