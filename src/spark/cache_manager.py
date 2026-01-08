"""Centralized cache management with explicit refresh operations.

This module provides a clean separation between:
1. Cache validation - determining what needs refresh
2. Cache refresh - updating stale data from GitHub API
3. Cache reading - consuming cached data (in fetcher.py)

NO cache writes happen during data reading/assembly.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, List, Optional, Set
from pathlib import Path

from spark.cache import APICache
from spark.fetcher import _sanitize_timestamp_for_filename
from spark.logger import get_logger


@dataclass
class RefreshResult:
    """Result of a cache refresh operation."""
    repo_name: str
    category: str  # e.g., "commit_counts", "languages", "readme"
    was_cached: bool
    refreshed: bool
    error: Optional[str] = None


@dataclass
class RefreshSummary:
    """Summary of cache refresh for all repositories."""
    total_repos: int
    repos_refreshed: int
    repos_unchanged: int
    repos_failed: int
    results: List[RefreshResult]
    api_calls_made: int


class CacheManager:
    """Manages cache validation and refresh operations."""
    
    def __init__(self, github_client, cache: APICache):
        """Initialize cache manager.
        
        Args:
            github_client: PyGithub client instance
            cache: APICache instance
        """
        self.github = github_client
        self.cache = cache
        self.logger = get_logger()
        self.api_calls = 0
    
    def needs_refresh(
        self,
        username: str,
        repo_name: str,
        category: str,
        current_pushed_at: datetime
    ) -> bool:
        """Check if a cache entry needs refresh based on repo's pushed_at.
        
        Args:
            username: Repository owner
            repo_name: Repository name
            category: Cache category (e.g., "commit_counts")
            current_pushed_at: Current pushed_at timestamp from GitHub
            
        Returns:
            True if cache is missing or stale
        """
        if not current_pushed_at:
            return True
        
        # Generate cache key for this repo's current state
        cache_key = _sanitize_timestamp_for_filename(current_pushed_at)
        
        # Check if cache exists for this exact pushed_at
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        
        return cached is None
    
    def refresh_commit_counts(
        self,
        username: str,
        repo_name: str,
        pushed_at: datetime
    ) -> RefreshResult:
        """Refresh commit counts cache for a repository.
        
        Args:
            username: Repository owner
            repo_name: Repository name
            pushed_at: Repository's pushed_at timestamp
            
        Returns:
            RefreshResult with status
        """
        cache_key = _sanitize_timestamp_for_filename(pushed_at)
        category = "commit_counts"
        
        # Check if already cached
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached:
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=True,
                refreshed=False
            )
        
        try:
            # Fetch from GitHub
            self.api_calls += 1
            repo = self.github.get_repo(f"{username}/{repo_name}")
            
            from datetime import timedelta
            now = datetime.now(timezone.utc)
            day_90_ago = now - timedelta(days=90)
            day_180_ago = now - timedelta(days=180)
            day_365_ago = now - timedelta(days=365)
            
            total_commits = 0
            commits_90d = 0
            commits_180d = 0
            commits_365d = 0
            last_commit_date = None
            
            for commit in repo.get_commits():
                if total_commits >= 1000:  # Limit for rate limiting
                    break
                
                total_commits += 1
                
                try:
                    commit_date = commit.commit.author.date if commit.commit and commit.commit.author else None
                except (AttributeError, IndexError):
                    continue
                
                if not commit_date:
                    continue
                
                if not last_commit_date or commit_date > last_commit_date:
                    last_commit_date = commit_date
                
                if commit_date >= day_90_ago:
                    commits_90d += 1
                if commit_date >= day_180_ago:
                    commits_180d += 1
                if commit_date >= day_365_ago:
                    commits_365d += 1
            
            result = {
                "total": total_commits,
                "recent_90d": commits_90d,
                "recent_180d": commits_180d,
                "recent_365d": commits_365d,
                "last_commit_date": last_commit_date.isoformat() if last_commit_date else None,
            }
            
            # Write to cache
            metadata = {
                "repository": {"owner": username, "name": repo_name},
                "category": category,
                "pushed_at": pushed_at.isoformat(),
                "ttl_enforced": False,
            }
            self.cache.set(category, username, result, repo=repo_name, week=cache_key, metadata=metadata)
            
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=False,
                refreshed=True
            )
            
        except Exception as e:
            self.logger.warn(f"Failed to refresh {category} for {repo_name}: {e}")
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=False,
                refreshed=False,
                error=str(e)
            )
    
    def refresh_languages(
        self,
        username: str,
        repo_name: str,
        pushed_at: datetime
    ) -> RefreshResult:
        """Refresh language stats cache for a repository."""
        cache_key = _sanitize_timestamp_for_filename(pushed_at)
        category = "languages"
        
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached:
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=True,
                refreshed=False
            )
        
        try:
            self.api_calls += 1
            repo = self.github.get_repo(f"{username}/{repo_name}")
            languages = repo.get_languages()
            
            metadata = {
                "repository": {"owner": username, "name": repo_name},
                "category": category,
                "pushed_at": pushed_at.isoformat(),
                "ttl_enforced": False,
            }
            self.cache.set(category, username, languages, repo=repo_name, week=cache_key, metadata=metadata)
            
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=False,
                refreshed=True
            )
            
        except Exception as e:
            self.logger.warn(f"Failed to refresh {category} for {repo_name}: {e}")
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=False,
                refreshed=False,
                error=str(e)
            )
    
    def refresh_repository(
        self,
        username: str,
        repo_name: str,
        pushed_at: datetime,
        categories: Optional[Set[str]] = None
    ) -> List[RefreshResult]:
        """Refresh all cache categories for a repository.
        
        Args:
            username: Repository owner
            repo_name: Repository name
            pushed_at: Repository's pushed_at timestamp
            categories: Specific categories to refresh (None = all)
            
        Returns:
            List of RefreshResult for each category
        """
        if categories is None:
            categories = {"commit_counts", "languages"}
        
        results = []
        
        if "commit_counts" in categories:
            results.append(self.refresh_commit_counts(username, repo_name, pushed_at))
        
        if "languages" in categories:
            results.append(self.refresh_languages(username, repo_name, pushed_at))
        
        return results
    
    def refresh_user_data(
        self,
        username: str,
        repo_list: List[Dict],
        force_refresh: bool = False
    ) -> RefreshSummary:
        """Refresh cache for all repositories of a user.
        
        This is the main entry point for cache refresh operations.
        
        Args:
            username: GitHub username
            repo_list: List of repository dicts with 'name' and 'pushed_at'
            force_refresh: If True, refresh all repos regardless of cache state
            
        Returns:
            RefreshSummary with results
        """
        self.logger.info(f"Starting cache refresh for {len(repo_list)} repositories")
        self.api_calls = 0
        
        all_results = []
        repos_refreshed = 0
        repos_unchanged = 0
        repos_failed = 0
        
        for i, repo_data in enumerate(repo_list, 1):
            repo_name = repo_data["name"]
            pushed_at_str = repo_data.get("pushed_at")
            
            if not pushed_at_str:
                self.logger.debug(f"[{i}/{len(repo_list)}] Skipping {repo_name} - no pushed_at")
                continue
            
            # Parse pushed_at
            try:
                pushed_at = datetime.fromisoformat(pushed_at_str.replace('Z', '+00:00'))
                if pushed_at.tzinfo is None:
                    pushed_at = pushed_at.replace(tzinfo=timezone.utc)
            except Exception as e:
                self.logger.warn(f"Failed to parse pushed_at for {repo_name}: {e}")
                continue
            
            # Check if refresh needed
            if not force_refresh:
                needs_update = self.needs_refresh(username, repo_name, "commit_counts", pushed_at)
                if not needs_update:
                    self.logger.debug(f"[{i}/{len(repo_list)}] OK {repo_name} - cache valid")
                    repos_unchanged += 1
                    continue
            
            # Refresh this repository
            self.logger.info(f"[{i}/{len(repo_list)}] Refreshing {repo_name}")
            repo_results = self.refresh_repository(username, repo_name, pushed_at)
            all_results.extend(repo_results)
            
            # Count success/failures
            if any(r.error for r in repo_results):
                repos_failed += 1
            else:
                repos_refreshed += 1
        
        self.logger.info(f"Cache refresh complete:")
        self.logger.info(f"  Refreshed: {repos_refreshed}")
        self.logger.info(f"  Unchanged: {repos_unchanged}")
        self.logger.info(f"  Failed: {repos_failed}")
        self.logger.info(f"  API calls: {self.api_calls}")
        
        return RefreshSummary(
            total_repos=len(repo_list),
            repos_refreshed=repos_refreshed,
            repos_unchanged=repos_unchanged,
            repos_failed=repos_failed,
            results=all_results,
            api_calls_made=self.api_calls
        )
