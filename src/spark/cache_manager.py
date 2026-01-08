"""Centralized cache management with explicit refresh operations.

This module provides a clean separation between:
1. Cache validation - determining what needs refresh
2. Cache refresh - updating stale data from GitHub API
3. Cache reading - consuming cached data (in fetcher.py)

NO cache writes happen during data reading/assembly.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, List, Optional, Set, Any

from github import GithubException

from spark.cache import APICache
from spark.dependencies.analyzer import RepositoryDependencyAnalyzer
from spark.time_utils import sanitize_timestamp_for_filename
from spark.logger import get_logger
from spark.models.commit import CommitHistory
from spark.models.repository import Repository
from spark.models.tech_stack import TechnologyStack, DependencyInfo
from spark.summarizer import RepositorySummarizer


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
    
    def __init__(
        self,
        github_client,
        cache: APICache,
        summarizer: Optional[RepositorySummarizer] = None,
    ):
        """Initialize cache manager.
        
        Args:
            github_client: PyGithub client instance
            cache: APICache instance
            summarizer: Optional RepositorySummarizer for AI summary refresh
        """
        self.github = github_client
        self.cache = cache
        self.logger = get_logger()
        self.api_calls = 0
        self.summarizer = summarizer
        self.dependency_analyzer = RepositoryDependencyAnalyzer()
    
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
        cache_key = sanitize_timestamp_for_filename(current_pushed_at)
        
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
        cache_key = sanitize_timestamp_for_filename(pushed_at)
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
        cache_key = sanitize_timestamp_for_filename(pushed_at)
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

    def refresh_readme(
        self,
        username: str,
        repo_name: str,
        pushed_at: datetime
    ) -> RefreshResult:
        """Refresh README cache for a repository."""
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "readme"

        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached is not None:
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=True,
                refreshed=False
            )

        try:
            self.api_calls += 1
            repo = self.github.get_repo(f"{username}/{repo_name}")
            content = ""
            try:
                readme = repo.get_readme()
                content = readme.decoded_content.decode("utf-8")
            except GithubException as e:
                if getattr(e, "status", None) != 404:
                    raise

            metadata = {
                "repository": {"owner": username, "name": repo_name},
                "category": category,
                "pushed_at": pushed_at.isoformat(),
                "ttl_enforced": False,
            }
            self.cache.set(category, username, content, repo=repo_name, week=cache_key, metadata=metadata)

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

    def refresh_dependency_files(
        self,
        username: str,
        repo_name: str,
        pushed_at: datetime
    ) -> RefreshResult:
        """Refresh dependency files cache for a repository."""
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "dependency_files"

        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached is not None:
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=True,
                refreshed=False
            )

        dependency_files: Dict[str, str] = {}
        target_files = [
            "package.json",
            "requirements.txt",
            "pyproject.toml",
            "Gemfile",
            "go.mod",
            "pom.xml",
            "*.csproj",
            "Cargo.toml",
            "composer.json",
        ]

        try:
            self.api_calls += 1
            repo = self.github.get_repo(f"{username}/{repo_name}")

            for filename in target_files:
                try:
                    if "*" in filename:
                        contents = repo.get_contents("")
                        pattern = filename.replace("*", "")
                        for item in contents:
                            if item.name.endswith(pattern):
                                content = item.decoded_content.decode("utf-8")
                                dependency_files[item.name] = content
                    else:
                        file_content = repo.get_contents(filename)
                        content = file_content.decoded_content.decode("utf-8")
                        dependency_files[filename] = content
                except GithubException as e:
                    if getattr(e, "status", None) == 404:
                        continue
                    raise
                except Exception:
                    continue

            metadata = {
                "repository": {"owner": username, "name": repo_name},
                "category": category,
                "pushed_at": pushed_at.isoformat(),
                "ttl_enforced": False,
            }
            self.cache.set(category, username, dependency_files, repo=repo_name, week=cache_key, metadata=metadata)

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

    def refresh_ai_summary(
        self,
        username: str,
        repo_data: Dict[str, Any],
        pushed_at: datetime
    ) -> RefreshResult:
        """Refresh AI summary cache for a repository."""
        repo_name = repo_data["name"]
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "ai_summary"

        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached:
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=True,
                refreshed=False
            )

        if self.summarizer is None:
            self.summarizer = RepositorySummarizer(cache=self.cache)

        try:
            # Ensure supporting caches exist
            commit_data = self.cache.get("commit_counts", username, repo=repo_name, week=cache_key)
            if commit_data is None:
                self.refresh_commit_counts(username, repo_name, pushed_at)
                commit_data = self.cache.get("commit_counts", username, repo=repo_name, week=cache_key) or {}

            language_stats = self.cache.get("languages", username, repo=repo_name, week=cache_key)
            if language_stats is None:
                self.refresh_languages(username, repo_name, pushed_at)
                language_stats = self.cache.get("languages", username, repo=repo_name, week=cache_key) or {}

            readme_content = self.cache.get("readme", username, repo=repo_name, week=cache_key)
            if readme_content is None:
                self.refresh_readme(username, repo_name, pushed_at)
                readme_content = self.cache.get("readme", username, repo=repo_name, week=cache_key) or ""

            dependency_files = self.cache.get("dependency_files", username, repo=repo_name, week=cache_key)
            if dependency_files is None:
                self.refresh_dependency_files(username, repo_name, pushed_at)
                dependency_files = self.cache.get("dependency_files", username, repo=repo_name, week=cache_key) or {}

            tech_stack = None
            if dependency_files:
                dep_report = self.dependency_analyzer.analyze_repository(dependency_files)
                if dep_report.total_dependencies > 0:
                    tech_stack = TechnologyStack(
                        repository_name=repo_name,
                        dependencies=[
                            DependencyInfo(
                                name=detail.name,
                                current_version=detail.current_version,
                                ecosystem=detail.ecosystem,
                            )
                            for detail in dep_report.details
                        ],
                    )

            repo = Repository.from_dict(repo_data)
            repo.language_stats = language_stats or {}
            repo.language_count = len(repo.language_stats)
            repo.has_readme = bool(readme_content)

            commit_data["repository_name"] = repo_name
            commit_history = CommitHistory.from_dict(commit_data) if commit_data else None

            summary = self.summarizer.summarize_repository(
                repo=repo,
                readme_content=readme_content or None,
                commit_history=commit_history,
                language_stats=language_stats,
                tech_stack=tech_stack,
                repository_owner=username,
                repo_pushed_at=pushed_at,
                write_cache=False,
            )

            if summary.ai_summary:
                cache_payload = {
                    "ai_summary": summary.ai_summary,
                    "generation_method": summary.generation_method,
                    "generation_timestamp": summary.generation_timestamp.isoformat()
                    if summary.generation_timestamp
                    else datetime.now().isoformat(),
                    "model_used": summary.model_used,
                    "tokens_used": summary.tokens_used,
                    "confidence_score": summary.confidence_score,
                }
                metadata = self.summarizer._build_cache_metadata(
                    repo_name=repo_name,
                    repository_owner=username,
                    cache_date=pushed_at,
                )
                self.cache.set(
                    category,
                    username,
                    cache_payload,
                    repo=repo_name,
                    week=cache_key,
                    metadata=metadata,
                )

                return RefreshResult(
                    repo_name=repo_name,
                    category=category,
                    was_cached=False,
                    refreshed=True
                )

            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=False,
                refreshed=False
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
        categories: Optional[Set[str]] = None,
        repo_data: Optional[Dict[str, Any]] = None,
        include_ai_summaries: bool = False,
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

        if include_ai_summaries:
            categories = set(categories) | {"readme", "dependency_files", "ai_summary"}
        
        results = []
        
        if "commit_counts" in categories:
            results.append(self.refresh_commit_counts(username, repo_name, pushed_at))
        
        if "languages" in categories:
            results.append(self.refresh_languages(username, repo_name, pushed_at))

        if "readme" in categories:
            results.append(self.refresh_readme(username, repo_name, pushed_at))

        if "dependency_files" in categories:
            results.append(self.refresh_dependency_files(username, repo_name, pushed_at))

        if "ai_summary" in categories and repo_data:
            results.append(self.refresh_ai_summary(username, repo_data, pushed_at))
        
        return results
    
    def refresh_user_data(
        self,
        username: str,
        repo_list: List[Dict],
        force_refresh: bool = False,
        include_ai_summaries: bool = False,
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
                categories_to_check = {"commit_counts", "languages"}
                if include_ai_summaries:
                    categories_to_check |= {"readme", "dependency_files", "ai_summary"}

                needs_update = any(
                    self.needs_refresh(username, repo_name, category, pushed_at)
                    for category in categories_to_check
                )
                if not needs_update:
                    self.logger.debug(f"[{i}/{len(repo_list)}] OK {repo_name} - cache valid")
                    repos_unchanged += 1
                    continue
            
            # Refresh this repository
            self.logger.info(f"[{i}/{len(repo_list)}] Refreshing {repo_name}")
            repo_results = self.refresh_repository(
                username,
                repo_name,
                pushed_at,
                repo_data=repo_data,
                include_ai_summaries=include_ai_summaries,
            )
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
