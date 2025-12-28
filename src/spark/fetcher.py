"""GitHub API data fetching with rate limiting and caching."""

import os
import time
from typing import List, Dict, Any, Optional
from datetime import datetime

from github import Github, GithubException, RateLimitExceededException
from github.Repository import Repository
from github.NamedUser import NamedUser

from spark.cache import APICache
from spark.logger import get_logger


class GitHubFetcher:
    """Fetches GitHub user data with rate limiting and caching."""

    def __init__(
        self,
        token: Optional[str] = None,
        cache: Optional[APICache] = None,
        max_repos: int = 500,
    ):
        """Initialize the GitHub API fetcher.

        Args:
            token: GitHub Personal Access Token (uses GITHUB_TOKEN env var if not provided)
            cache: API cache instance (creates new if not provided)
            max_repos: Maximum number of repositories to process
        """
        self.logger = get_logger()
        self.token = token or os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise ValueError("GitHub token required (GITHUB_TOKEN environment variable or token parameter)")

        self.github = Github(self.token)
        self.cache = cache or APICache()
        self.max_repos = max_repos

    def fetch_user_profile(self, username: str) -> Dict[str, Any]:
        """Fetch GitHub user profile information.

        Args:
            username: GitHub username

        Returns:
            User profile data dictionary
        """
        cache_key = f"user_profile_{username}"
        cached = self.cache.get(cache_key)
        if cached:
            self.logger.debug(f"Using cached user profile for {username}")
            return cached

        self.logger.info(f"Fetching user profile for {username}")

        try:
            user = self.github.get_user(username)

            profile_data = {
                "username": user.login,
                "name": user.name or user.login,
                "bio": user.bio,
                "company": user.company,
                "location": user.location,
                "email": user.email,
                "public_repos": user.public_repos,
                "followers": user.followers,
                "following": user.following,
                "created_at": user.created_at.isoformat() if user.created_at else None,
                "updated_at": user.updated_at.isoformat() if user.updated_at else None,
            }

            self.cache.set(cache_key, profile_data)
            return profile_data

        except GithubException as e:
            self.logger.error(f"Failed to fetch user profile for {username}", e)
            raise

    def fetch_repositories(
        self,
        username: str,
        exclude_private: bool = True,
        exclude_forks: bool = False,
    ) -> List[Dict[str, Any]]:
        """Fetch user repositories with pagination.

        Args:
            username: GitHub username
            exclude_private: Exclude private repositories
            exclude_forks: Exclude forked repositories

        Returns:
            List of repository data dictionaries
        """
        cache_key = f"repositories_{username}_{exclude_private}_{exclude_forks}"
        cached = self.cache.get(cache_key)
        if cached:
            self.logger.debug(f"Using cached repositories for {username}")
            return cached

        self.logger.info(f"Fetching repositories for {username}")

        try:
            user = self.github.get_user(username)
            repos = []

            for repo in user.get_repos():
                # Apply filters
                if exclude_private and repo.private:
                    continue
                if exclude_forks and repo.fork:
                    continue

                # Stop if we've hit the max
                if len(repos) >= self.max_repos:
                    self.logger.warn(f"Reached maximum repository limit ({self.max_repos})")
                    break

                repos.append({
                    "name": repo.name,
                    "full_name": repo.full_name,
                    "description": repo.description,
                    "language": repo.language,
                    "stars": repo.stargazers_count,
                    "forks": repo.forks_count,
                    "watchers": repo.watchers_count,
                    "size": repo.size,
                    "created_at": repo.created_at.isoformat() if repo.created_at else None,
                    "updated_at": repo.updated_at.isoformat() if repo.updated_at else None,
                    "pushed_at": repo.pushed_at.isoformat() if repo.pushed_at else None,
                    "is_fork": repo.fork,
                    "is_private": repo.private,
                })

            self.cache.set(cache_key, repos)
            self.logger.info(f"Fetched {len(repos)} repositories")
            return repos

        except GithubException as e:
            self.logger.error(f"Failed to fetch repositories for {username}", e)
            raise

    def fetch_commits(
        self,
        username: str,
        repo_name: str,
        max_commits: int = 100,
    ) -> List[Dict[str, Any]]:
        """Fetch commits for a repository.

        Args:
            username: Repository owner username
            repo_name: Repository name
            max_commits: Maximum commits to fetch per repository

        Returns:
            List of commit data dictionaries
        """
        cache_key = f"commits_{username}_{repo_name}"
        cached = self.cache.get(cache_key)
        if cached:
            return cached

        self.logger.debug(f"Fetching commits for {username}/{repo_name}")

        try:
            repo = self.github.get_repo(f"{username}/{repo_name}")
            commits = []

            for commit in repo.get_commits(author=username):
                if len(commits) >= max_commits:
                    break

                commit_data = {
                    "sha": commit.sha,
                    "message": commit.commit.message,
                    "author": commit.commit.author.name if commit.commit.author else username,
                    "date": commit.commit.author.date.isoformat() if commit.commit.author else None,
                    "repo": repo_name,
                }
                commits.append(commit_data)

            self.cache.set(cache_key, commits)
            return commits

        except GithubException as e:
            self.logger.debug(f"Could not fetch commits for {repo_name}: {e}")
            return []

    def fetch_languages(self, username: str, repo_name: str) -> Dict[str, int]:
        """Fetch language statistics for a repository.

        Args:
            username: Repository owner username
            repo_name: Repository name

        Returns:
            Dictionary mapping language names to byte counts
        """
        cache_key = f"languages_{username}_{repo_name}"
        cached = self.cache.get(cache_key)
        if cached:
            return cached

        try:
            repo = self.github.get_repo(f"{username}/{repo_name}")
            languages = repo.get_languages()

            self.cache.set(cache_key, languages)
            return languages

        except GithubException as e:
            self.logger.debug(f"Could not fetch languages for {repo_name}: {e}")
            return {}

    def handle_rate_limit(self, max_retries: int = 3) -> None:
        """Handle rate limiting with exponential backoff.

        Args:
            max_retries: Maximum number of retry attempts
        """
        rate_limit = self.github.get_rate_limit()
        core_rate = rate_limit.core

        if core_rate.remaining == 0:
            reset_time = core_rate.reset
            sleep_time = (reset_time - datetime.now()).total_seconds() + 10

            self.logger.warn(
                f"Rate limit exceeded. Sleeping for {sleep_time:.0f} seconds until reset."
            )
            time.sleep(sleep_time)

    def get_rate_limit_status(self) -> Dict[str, Any]:
        """Get current rate limit status.

        Returns:
            Dictionary with rate limit information
        """
        rate_limit = self.github.get_rate_limit()
        core_rate = rate_limit.core

        return {
            "limit": core_rate.limit,
            "remaining": core_rate.remaining,
            "reset": core_rate.reset.isoformat(),
            "used": core_rate.limit - core_rate.remaining,
        }
