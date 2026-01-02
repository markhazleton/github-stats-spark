"""Dashboard data generator for repository comparison dashboard.

This module generates JSON data files for the GitHub Stats Spark interactive
dashboard. It fetches repository data, calculates commit metrics, and exports
structured JSON for frontend consumption.
"""

import logging
from pathlib import Path
from datetime import datetime
from typing import List, Optional, Dict
import os

from spark.fetcher import GitHubFetcher
from spark.calculator import StatsCalculator
from spark.models.dashboard_data import (
    DashboardData,
    DashboardRepository,
    DashboardMetadata,
    UserProfile,
    CommitMetric,
)
from spark.config import Config

logger = logging.getLogger(__name__)


class DashboardGenerator:
    """Generates dashboard JSON data from GitHub repository analysis.

    This class coordinates the data collection, metric calculation, and JSON
    export process for the repository comparison dashboard.

    Attributes:
        config: Configuration object with dashboard settings
        fetcher: GitHub API data fetcher
        calculator: Metrics calculator for commit analysis
        output_dir: Directory path for JSON output files
    """

    def __init__(self, config: Dict[str, Any], username: str):
        """Initialize the DashboardGenerator.

        Args:
            config: Configuration dictionary containing dashboard settings
            username: GitHub username to analyze
        """
        self.config = config
        self.username = username

        # Initialize fetcher with token from environment
        token = os.getenv("GITHUB_TOKEN")
        dashboard_config = config.get("dashboard", {})
        max_repos = dashboard_config.get("data_generation", {}).get("max_repositories", 200)

        self.fetcher = GitHubFetcher(token=token, max_repos=max_repos)

        # Get dashboard configuration
        dashboard_config = config.get("dashboard", {})
        self.output_dir = Path(dashboard_config.get("output_dir", "docs"))
        self.data_dir = self.output_dir / "data"

        # Dashboard feature flags
        self.enabled = dashboard_config.get("enabled", True)
        data_gen = dashboard_config.get("data_generation", {})
        self.include_commit_metrics = data_gen.get("include_commit_metrics", True)
        self.include_language_stats = data_gen.get("include_language_stats", True)
        self.include_ai_summaries = data_gen.get("include_ai_summaries", False)
        self.max_repositories = data_gen.get("max_repositories", 200)

        logger.info(
            f"DashboardGenerator initialized (output: {self.data_dir}, "
            f"max_repos: {self.max_repositories})"
        )

    def generate(self) -> DashboardData:
        """Generate complete dashboard data.

        This is the main entry point for dashboard data generation. It orchestrates
        the entire process: fetch repositories, calculate metrics, build data structure.

        Returns:
            DashboardData object containing all dashboard information

        Raises:
            Exception: If dashboard generation is disabled or fails
        """
        if not self.enabled:
            logger.warning("Dashboard generation is disabled in configuration")
            raise ValueError("Dashboard generation is disabled in config")

        logger.info("Starting dashboard data generation...")

        # Fetch repository data
        repositories = self.generate_dashboard_data()

        # Fetch user profile
        profile = self.generate_user_profile()

        # Create metadata
        metadata = DashboardMetadata(
            generated_at=datetime.now(),
            schema_version="1.0.0",
            repository_count=len(repositories),
            data_source="GitHub API",
        )

        # Build dashboard data structure
        dashboard_data = DashboardData(
            repositories=repositories,
            profile=profile,
            metadata=metadata,
        )

        logger.info(
            f"Dashboard data generation complete: {len(repositories)} repositories"
        )
        return dashboard_data

    def generate_dashboard_data(self) -> List[DashboardRepository]:
        """Fetch all public repositories and prepare dashboard data.

        Returns:
            List of DashboardRepository objects with metrics
        """
        logger.info(f"Fetching repositories for {self.username}...")

        # Fetch all public repositories
        repos_config = self.config.get("repositories", {})
        exclude_forks = repos_config.get("exclude_forks", False)

        raw_repos = self.fetcher.fetch_repositories(
            username=self.username,
            exclude_private=True,  # Always exclude private per constitution
            exclude_forks=exclude_forks
        )

        logger.info(f"Found {len(raw_repos)} repositories")

        # Apply max_repositories limit
        if len(raw_repos) > self.max_repositories:
            logger.warning(f"Limiting to {self.max_repositories} repositories (found {len(raw_repos)})")
            raw_repos = raw_repos[:self.max_repositories]

        # Convert to DashboardRepository objects with metrics
        dashboard_repos = []
        for i, repo_data in enumerate(raw_repos, 1):
            repo_name = repo_data.get("name", "unknown")
            logger.info(f"Processing repository {i}/{len(raw_repos)}: {repo_name}")

            try:
                # Calculate commit metrics for this repository
                commit_metrics = self.calculate_commit_metrics(repo_name)

                # Extract dates
                created_at = repo_data.get("created_at")
                if isinstance(created_at, str):
                    created_at = datetime.fromisoformat(created_at.replace("Z", "+00:00"))

                updated_at = repo_data.get("updated_at")
                if isinstance(updated_at, str):
                    updated_at = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))

                pushed_at = repo_data.get("pushed_at")
                if isinstance(pushed_at, str):
                    pushed_at = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))

                # Build DashboardRepository
                dashboard_repo = DashboardRepository(
                    name=repo_name,
                    language=repo_data.get("language") or "Unknown",
                    created_at=created_at,
                    last_commit_date=pushed_at or updated_at,
                    first_commit_date=commit_metrics.get("first_commit_date"),
                    commit_count=commit_metrics.get("total_commits", 0),
                    avg_commit_size=commit_metrics.get("avg_commit_size", 0.0),
                    largest_commit=commit_metrics.get("largest_commit"),
                    smallest_commit=commit_metrics.get("smallest_commit"),
                    stars=repo_data.get("stargazers_count", 0),
                    forks=repo_data.get("forks_count", 0),
                    url=repo_data.get("html_url", ""),
                    description=repo_data.get("description"),
                    updated_at=updated_at,
                )
                dashboard_repos.append(dashboard_repo)

            except Exception as e:
                logger.error(f"Failed to process repository {repo_name}: {e}")
                continue

        return dashboard_repos

    def calculate_commit_metrics(
        self, repo_name: str, commits: List
    ) -> Dict:
        """Calculate commit size metrics for a repository.

        Args:
            repo_name: Repository name
            commits: List of commit objects from GitHub API

        Returns:
            Dictionary containing avg_commit_size, largest_commit, smallest_commit

        Note:
            This method will be implemented in T016
        """
        logger.debug(f"Calculating commit metrics for {repo_name}...")
        # TODO: Implement in T016
        # - Calculate commit size for each commit (files + lines added + lines deleted)
        # - Calculate average commit size
        # - Find largest and smallest commits
        # - Return CommitMetric objects
        return {
            "avg_commit_size": 0.0,
            "largest_commit": None,
            "smallest_commit": None,
        }

    def generate_user_profile(self) -> UserProfile:
        """Generate user profile information for dashboard header.

        Returns:
            UserProfile object with user statistics

        Note:
            Uses fetcher to get user data from GitHub API
        """
        logger.info("Generating user profile...")
        user_data = self.fetcher.get_user()

        # Calculate aggregate statistics
        total_stars = 0
        total_forks = 0
        # TODO: Calculate from repository data in future enhancement

        return UserProfile(
            username=user_data.get("login", "unknown"),
            avatar_url=user_data.get("avatar_url", ""),
            public_repos_count=user_data.get("public_repos", 0),
            profile_url=user_data.get("html_url", ""),
            total_stars=total_stars,
            total_forks=total_forks,
        )

    def write_json_output(self, dashboard_data: DashboardData, filename: str = "repositories.json") -> Path:
        """Write dashboard data to JSON file.

        Args:
            dashboard_data: DashboardData object to serialize
            filename: Output filename (default: repositories.json)

        Returns:
            Path to written JSON file

        Note:
            This method will be implemented in T017
        """
        output_path = self.data_dir / filename
        logger.info(f"Writing dashboard data to {output_path}...")

        # TODO: Implement in T017
        # - Ensure data directory exists
        # - Serialize dashboard_data to JSON
        # - Write to file with proper formatting
        # - Return path to written file

        return output_path

    def save(self, dashboard_data: Optional[DashboardData] = None) -> Path:
        """Generate and save dashboard data to JSON file.

        Args:
            dashboard_data: Optional pre-generated dashboard data.
                           If None, will generate new data.

        Returns:
            Path to saved JSON file
        """
        if dashboard_data is None:
            dashboard_data = self.generate()

        output_path = self.write_json_output(dashboard_data)
        logger.info(f"Dashboard data saved successfully to {output_path}")
        return output_path
