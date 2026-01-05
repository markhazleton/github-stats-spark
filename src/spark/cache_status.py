"""Cache status tracking and validation for repository data."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Any

from spark.cache import APICache


class CacheStatusTracker:
    """Tracks cache status for repositories and determines refresh needs."""

    def __init__(self, cache_dir: str = ".cache"):
        """Initialize cache status tracker.

        Args:
            cache_dir: Directory where cache files are stored
        """
        self.cache = APICache(cache_dir)

    def get_repository_cache_status(
        self,
        username: str,
        repo_name: str,
        pushed_at: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get comprehensive cache status for a repository."""
        
        # Determine current week for cache key validation
        current_week = datetime.now(timezone.utc).strftime("%YW%V")
        if pushed_at:
            pushed_date = datetime.fromisoformat(pushed_at.replace("+00:00", ""))
            if pushed_date.tzinfo is None:
                pushed_date = pushed_date.replace(tzinfo=timezone.utc)
            push_week = pushed_date.strftime("%YW%V")
        else:
            push_week = "unknown"
            pushed_date = None

        cache_types = [
            "commits_stats",
            "commit_counts",
            "languages",
            "dependency_files",
            "readme",
            "ai_summary",
        ]
        
        essential_types = ["commits_stats", "commit_counts", "languages"]
        
        cache_files = {}
        oldest_timestamp = None
        newest_timestamp = None
        all_caches_exist = True
        
        for cache_type in cache_types:
            entry_info = self.cache.get_entry_info(cache_type, username, repo_name)
            exists = False
            timestamp = None
            metadata = {}
            
            if entry_info:
                weeks = entry_info.get("weeks", [])
                # Check if we have a matching week
                # For ai_summary, week might be {week}_{hash}
                matching_week = None
                for w in weeks:
                    if w.startswith(push_week):
                        matching_week = w
                        break
                
                if matching_week:
                    exists = True
                    # We need to read the file to get timestamp/metadata?
                    # Or rely on manifest updated_at?
                    # Manifest updated_at is when the cache was written.
                    # That's what we want for "cache age".
                    timestamp_str = entry_info.get("updated_at")
                    if timestamp_str:
                        timestamp = datetime.fromisoformat(timestamp_str)
            
            if exists and timestamp:
                if oldest_timestamp is None or timestamp < oldest_timestamp:
                    oldest_timestamp = timestamp
                if newest_timestamp is None or timestamp > newest_timestamp:
                    newest_timestamp = timestamp
            
            cache_files[cache_type] = {
                "exists": exists,
                "timestamp": timestamp.isoformat() if timestamp else None,
                "age_hours": (
                    (datetime.now(timezone.utc) - timestamp).total_seconds() / 3600 if timestamp else None
                ),
            }
            
            if not exists and cache_type in essential_types:
                all_caches_exist = False

        # Determine if refresh is needed
        refresh_needed = False
        refresh_reasons = []

        if not all_caches_exist:
            refresh_needed = True
            refresh_reasons.append("missing_cache_files")

        # Refresh only when repository push timestamp advances beyond cached metadata
        if pushed_date and all_caches_exist and newest_timestamp:
             if pushed_date > newest_timestamp:
                 refresh_needed = True
                 refresh_reasons.append("repo_has_new_commits")

        return {
            "has_cache": all_caches_exist,
            "cache_date": newest_timestamp.isoformat() if newest_timestamp else None,
            "cache_age_hours": (
                (datetime.now(timezone.utc) - newest_timestamp).total_seconds() / 3600 if newest_timestamp else None
            ),
            "refresh_needed": refresh_needed,
            "refresh_reasons": refresh_reasons,
            "cache_files": cache_files,
            "push_week": push_week,
            "current_week": current_week,
        }

    def update_repositories_cache_with_status(
        self,
        username: str,
        exclude_private: bool = True,
        exclude_forks: bool = False,
    ) -> Dict[str, Any]:
        """Update repositories cache file with cache status for each repo."""
        # We need to read the repositories cache using APICache
        variant = f"list_{exclude_private}_{exclude_forks}"
        repos = self.cache.get("repositories", username, repo=variant)
        
        if not repos:
             raise FileNotFoundError(f"Repositories cache not found for {username}")

        # Add cache status to each repository
        for repo in repos:
            repo_name = repo["name"]
            pushed_at = repo.get("pushed_at")
            
            cache_status = self.get_repository_cache_status(
                username=username,
                repo_name=repo_name,
                pushed_at=pushed_at,
            )
            
            repo["cache_status"] = cache_status

        # Update the cache
        self.cache.set("repositories", username, repos, repo=variant)
        
        return {"value": repos}

    def get_repositories_needing_refresh(
        self,
        username: str,
        exclude_private: bool = True,
        exclude_forks: bool = False,
    ) -> List[Dict[str, Any]]:
        """Get list of repositories that need cache refresh."""
        variant = f"list_{exclude_private}_{exclude_forks}"
        repos = self.cache.get("repositories", username, repo=variant)
        
        if not repos:
            raise FileNotFoundError(f"Repositories cache not found")

        return [
            repo for repo in repos
            if repo.get("cache_status", {}).get("refresh_needed", True)
        ]

    def get_cache_statistics(
        self,
        username: str,
        exclude_private: bool = True,
        exclude_forks: bool = False,
    ) -> Dict[str, Any]:
        """Get overall cache statistics for a user's repositories."""
        variant = f"list_{exclude_private}_{exclude_forks}"
        repos = self.cache.get("repositories", username, repo=variant)
        
        if not repos:
            return {
                "total_repositories": 0,
                "cached_repositories": 0,
                "needs_refresh": 0,
                "up_to_date": 0,
                "cache_hit_rate": "0%",
                "refresh_rate": "0%",
            }

        total = len(repos)
        cached = sum(1 for repo in repos if repo.get("cache_status", {}).get("has_cache", False))
        needs_refresh = sum(1 for repo in repos if repo.get("cache_status", {}).get("refresh_needed", True))
        up_to_date = total - needs_refresh

        return {
            "total_repositories": total,
            "cached_repositories": cached,
            "needs_refresh": needs_refresh,
            "up_to_date": up_to_date,
            "cache_hit_rate": f"{(cached / total * 100):.1f}%" if total > 0 else "0%",
            "refresh_rate": f"{(needs_refresh / total * 100):.1f}%" if total > 0 else "0%",
        }
