"""
Unified Data Generator - Clean 4-Phase Architecture

Phase 1: Fetch repository list from GitHub
Phase 2: Validate & refresh caches (via CacheManager)
Phase 3: Assemble data from cache (read-only)
Phase 4: Write outputs (handled by caller)

Constitutional Requirements:
- NO time-based TTL logic
- Cache ONLY invalidated when repo pushed_at changes
- Clear separation: fetch -> refresh -> assemble -> output
- Zero API calls on second run if no repos changed
"""

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from spark.cache import APICache
from spark.calculator import StatsCalculator
from spark.cache_manager import CacheManager
from spark.config import SparkConfig
from spark.dependencies.analyzer import RepositoryDependencyAnalyzer
from spark.fetcher import GitHubFetcher
from spark.logger import get_logger
from spark.models import (
    CommitHistory,
    Repository,
    UserProfile,
)
from spark.models.tech_stack import TechnologyStack, DependencyInfo
from spark.ranker import RepositoryRanker
from spark.summarizer import RepositorySummarizer
from spark.time_utils import sanitize_timestamp_for_filename

# Initialize logger
logger = get_logger(__name__)


class UnifiedDataGenerator:
    """Generates unified repository data using clean 4-phase architecture.
    
    Clean Architecture:
    1. Fetch: Get current repository list from GitHub
    2. Refresh: Update caches for repos with changes
    3. Assemble: Read all data from cache (no writes)
    4. Output: Write JSON/SVG files (no cache operations)
    """

    def __init__(
        self,
        username: str,
        config: SparkConfig,
        output_dir: Path,
        force_refresh: bool = False,
        max_repos_override: Optional[int] = None,
        cache: Optional[APICache] = None,
        include_ai_summaries: bool = False,
    ):
        """Initialize unified data generator.
        
        Args:
            username: GitHub username
            config: SparkConfig instance
            output_dir: Directory for output files
            force_refresh: Force refresh all caches
            max_repos_override: Override max repositories from config
            cache: Optional shared cache instance
            include_ai_summaries: Whether to generate AI summaries
        """
        self.username = username
        self.config = config
        self.output_dir = Path(output_dir)
        self.force_refresh = force_refresh
        
        # Get max_repositories from config or override
        dashboard_config = config.config.get("dashboard", {})
        data_gen_config = dashboard_config.get("data_generation", {})
        self.max_repositories = max_repos_override or data_gen_config.get("max_repositories", 50)
        self.top_n_repos = data_gen_config.get("top_n_repos", 50)
        self.include_ai_summaries = include_ai_summaries or data_gen_config.get("include_ai_summaries", False)
        
        # Initialize components
        self.cache = cache if cache is not None else APICache()
        self.fetcher = GitHubFetcher(cache=self.cache, max_repos=self.max_repositories)
        self.ranker = RepositoryRanker(config=config)
        
        logger.info(f"UnifiedDataGenerator initialized for user: {username}")
        logger.info(f"Max repositories: {self.max_repositories}")
        logger.info(f"Include AI summaries: {self.include_ai_summaries}")
        
        # Initialize cache manager for Phase 2
        self.cache_manager = CacheManager(self.fetcher.github, self.cache)

    def generate(self) -> Dict[str, Any]:
        """Generate unified data using clean 4-phase architecture.
        
        Phase 1: Fetch repository list
        Phase 2: Validate & refresh caches
        Phase 3: Assemble data from cache
        Phase 4: (handled by caller - output generation)
        
        Returns:
            Dict with profile, repositories, and metadata
        """
        from time import time
        
        logger.info("="*70)
        logger.info("Starting Unified Data Generation")
        logger.info("="*70)
        logger.info(f"Force refresh mode: {self.force_refresh}")
        logger.info(f"AI summaries: {self.include_ai_summaries}")
        logger.info(f"Max repositories: {self.max_repositories}")
        
        total_start = time()
        
        # PHASE 1: Fetch repository list from GitHub
        logger.info("\n[Phase 1] Fetching Repository List")
        phase1_start = time()
        raw_repos = self._fetch_repository_list()
        phase1_time = time() - phase1_start
        logger.info(f"Found {len(raw_repos)} repositories ({phase1_time:.2f}s)")
        
        # PHASE 2: Validate & refresh caches
        logger.info("\n[Phase 2] Cache Validation & Refresh")
        phase2_start = time()
        refresh_summary = self.cache_manager.refresh_user_data(
            username=self.username,
            repo_list=raw_repos,
            force_refresh=self.force_refresh,
            include_ai_summaries=self.include_ai_summaries,
        )
        phase2_time = time() - phase2_start
        logger.info(f"Refreshed: {refresh_summary.repos_refreshed}, " 
                   f"Unchanged: {refresh_summary.repos_unchanged}, "
                   f"API calls: {refresh_summary.api_calls_made} ({phase2_time:.2f}s)")
        
        # PHASE 3: Assemble data from cache
        logger.info("\n[Phase 3] Assembling Data from Cache")
        phase3_start = time()
        unified_data = self._assemble_data(raw_repos)
        phase3_time = time() - phase3_start
        logger.info(f"Assembled data for {len(unified_data['repositories'])} repositories ({phase3_time:.2f}s)")
        
        total_time = time() - total_start
        logger.info("\n" + "="*70)
        logger.info(f"Data Generation Complete: {total_time:.2f}s total")
        logger.info(f"  Phase 1 (Fetch): {phase1_time:.2f}s")
        logger.info(f"  Phase 2 (Refresh): {phase2_time:.2f}s")
        logger.info(f"  Phase 3 (Assemble): {phase3_time:.2f}s")
        logger.info("="*70)
        
        return unified_data
    
    def _fetch_repository_list(self) -> List[Dict]:
        """Phase 1: Fetch current repository list from GitHub.
        
        Returns:
            List of repository dicts with metadata
        """
        repos_config = self.config.config.get("repositories", {})
        exclude_forks = repos_config.get("exclude_forks", True)
        exclude_archived = repos_config.get("exclude_archived", True)
        return self.fetcher.fetch_repositories(
            username=self.username,
            exclude_private=True,
            exclude_forks=exclude_forks,
            exclude_archived=exclude_archived,
        )
    
    def _assemble_data(self, raw_repos: List[Dict]) -> Dict[str, Any]:
        """Phase 3: Assemble unified data by reading from cache.
        
        This phase ONLY reads from cache, never writes.
        
        Args:
            raw_repos: List of repository dicts from Phase 1
            
        Returns:
            Dict with 'profile', 'repositories', 'metadata' keys
        """
        repositories = []
        commit_histories = {}
        repo_cache = {}
        dependency_analyzer = RepositoryDependencyAnalyzer()
        summarizer = RepositorySummarizer(cache=self.cache, enable_ai=False)
        
        for i, repo_data in enumerate(raw_repos[:self.max_repositories], 1):
            repo_name = repo_data["name"]
            logger.debug(f"[{i}/{min(len(raw_repos), self.max_repositories)}] Assembling {repo_name}")
            
            try:
                # Parse pushed_at
                pushed_at_str = repo_data.get("pushed_at")
                if pushed_at_str:
                    pushed_at = datetime.fromisoformat(pushed_at_str.replace('Z', '+00:00'))
                    if pushed_at.tzinfo is None:
                        pushed_at = pushed_at.replace(tzinfo=timezone.utc)
                else:
                    pushed_at = None
                
                cache_key = sanitize_timestamp_for_filename(pushed_at) if pushed_at else None

                # Read commit counts from cache
                commit_data = self.fetcher.fetch_commit_counts(
                    self.username,
                    repo_name,
                    repo_pushed_at=pushed_at
                )
                
                if commit_data:
                    commit_histories[repo_name] = CommitHistory(
                        repository_name=repo_name,
                        total_commits=commit_data.get("total", 0),
                        recent_90d=commit_data.get("recent_90d", 0),
                        recent_180d=commit_data.get("recent_180d", 0),
                        recent_365d=commit_data.get("recent_365d", 0),
                        last_commit_date=(
                            datetime.fromisoformat(commit_data["last_commit_date"])
                            if commit_data.get("last_commit_date")
                            else None
                        ),
                    )
                
                # Read language stats from cache
                language_stats = self.fetcher.fetch_languages(
                    self.username,
                    repo_name,
                    repo_pushed_at=pushed_at
                ) or {}

                # Read cached AI summary, README, dependency files, and commit stats
                readme_content = ""
                dependency_files = {}
                commit_stats = None
                cached_summary = None

                if cache_key:
                    readme_content = self.cache.get(
                        "readme", self.username, repo=repo_name, week=cache_key
                    ) or ""
                    dependency_files = self.cache.get(
                        "dependency_files", self.username, repo=repo_name, week=cache_key
                    ) or {}
                    commit_stats = self.cache.get(
                        "commits_stats", self.username, repo=repo_name, week=cache_key
                    )
                    cached_summary = self.cache.get(
                        "ai_summary", self.username, repo=repo_name, week=cache_key
                    )
                    # Read quality indicators from cache
                    quality_indicators = self.cache.get(
                        "quality_indicators", self.username, repo=repo_name, week=cache_key
                    )
                    if quality_indicators:
                        repo_data["has_license"] = quality_indicators.get("has_license", False)
                        repo_data["has_ci_cd"] = quality_indicators.get("has_ci_cd", False)
                        repo_data["has_tests"] = quality_indicators.get("has_tests", False)
                        repo_data["has_docs"] = quality_indicators.get("has_docs", False)

                if cached_summary is None:
                    cached_summary = self.cache.get("ai_summary", self.username, repo=repo_name)

                # Create Repository object
                repo_data["language_stats"] = language_stats
                repo_data["language_count"] = len(language_stats)
                repo = Repository.from_dict(repo_data)
                repo.has_readme = bool(readme_content)
                repositories.append(repo)
                repo_cache[repo_name] = {
                    "readme_content": readme_content,
                    "dependency_files": dependency_files,
                    "commit_stats": commit_stats,
                    "cached_summary": cached_summary,
                }

            except Exception as e:
                logger.warn(f"Failed to assemble {repo_name}: {e}")
                continue
        
        # Rank repositories
        logger.info(f"Ranking {len(repositories)} repositories...")
        ranked_repos = self.ranker.rank_repositories(repositories, commit_histories, top_n=self.top_n_repos)
        
        # Create repository dicts
        unified_repos = []
        for rank, (repo, score) in enumerate(ranked_repos, 1):
            commit_history = commit_histories.get(repo.name)
            repo_extras = repo_cache.get(repo.name, {})
            readme_content = repo_extras.get("readme_content", "")
            dependency_files = repo_extras.get("dependency_files", {})
            commit_stats = repo_extras.get("commit_stats")
            cached_summary = repo_extras.get("cached_summary")
            commit_history_dict = commit_history.to_dict() if commit_history else None
            commit_metrics = None
            avg_commit_size = None
            largest_commit = None
            smallest_commit = None
            first_commit_date = repo.created_at

            if commit_stats:
                metrics = StatsCalculator.calculate_repository_commit_metrics(commit_stats)
                commit_metrics = {
                    "avg_size": metrics.get("avg_commit_size", 0.0),
                    "largest_commit": metrics.get("largest_commit"),
                    "smallest_commit": metrics.get("smallest_commit"),
                    "total_commits": metrics.get("total_commits", 0),
                    "commit_size_distribution": metrics.get("commit_size_distribution"),
                }
                avg_commit_size = commit_metrics["avg_size"]
                largest_commit = commit_metrics["largest_commit"]
                smallest_commit = commit_metrics["smallest_commit"]

                commit_dates = []
                for commit in commit_stats:
                    date_str = commit.get("commit", {}).get("author", {}).get("date")
                    if not date_str:
                        continue
                    try:
                        commit_dates.append(datetime.fromisoformat(date_str.replace("Z", "+00:00")))
                    except ValueError:
                        continue
                if commit_dates:
                    first_commit_date = min(commit_dates)

            if commit_history_dict is not None:
                commit_history_dict["first_commit_date"] = (
                    first_commit_date.isoformat() if first_commit_date else None
                )

            tech_stack = None
            if dependency_files:
                dep_report = dependency_analyzer.analyze_repository(dependency_files)
                if dep_report.total_dependencies > 0:
                    tech_stack = TechnologyStack(
                        repository_name=repo.name,
                        dependencies=[
                            DependencyInfo(
                                name=detail.name,
                                current_version=detail.current_version,
                                ecosystem=detail.ecosystem,
                            )
                            for detail in dep_report.details
                        ],
                        dependency_file_type=next(iter(dependency_files.keys()), None),
                        languages=repo.language_stats or {},
                    )

            summary_payload = None
            if cached_summary and cached_summary.get("ai_summary"):
                summary_payload = {
                    "text": cached_summary.get("ai_summary"),
                    "ai_generated": True,
                    "generation_method": cached_summary.get("generation_method"),
                    "generated_at": cached_summary.get("generation_timestamp"),
                    "model_used": cached_summary.get("model_used"),
                    "tokens_used": cached_summary.get("tokens_used"),
                    "confidence_score": cached_summary.get("confidence_score"),
                }
            else:
                fallback_summary = summarizer.summarize_repository(
                    repo=repo,
                    readme_content=readme_content or None,
                    commit_history=commit_history,
                    language_stats=repo.language_stats,
                    tech_stack=tech_stack,
                    repository_owner=self.username,
                    repo_pushed_at=repo.pushed_at,
                    write_cache=False,
                    allow_ai=False,
                )
                summary_payload = {
                    "text": fallback_summary.summary,
                    "ai_generated": fallback_summary.is_ai_generated,
                    "generation_method": fallback_summary.generation_method,
                    "generated_at": (
                        fallback_summary.generation_timestamp.isoformat()
                        if fallback_summary.generation_timestamp
                        else None
                    ),
                    "model_used": fallback_summary.model_used,
                    "tokens_used": fallback_summary.tokens_used,
                    "confidence_score": fallback_summary.confidence_score,
                }

            ai_summary_text = (
                summary_payload.get("text")
                if summary_payload and summary_payload.get("ai_generated")
                else None
            )

            repo_dict = {
                "name": repo.name,
                "description": repo.description,
                "summary": summary_payload,
                "url": repo.url,
                "homepage": repo.homepage,  # Custom website URL from repo settings
                "has_pages": repo.has_pages,  # GitHub Pages enabled
                "pages_url": repo.pages_url,  # Constructed GitHub Pages URL
                "website_url": repo.website_url,  # Best available website (homepage or pages_url)
                "stars": repo.stars,
                "forks": repo.forks,
                "watchers": repo.watchers,
                "language": repo.primary_language,
                "language_stats": repo.language_stats,
                "languages": repo.language_stats,
                "created_at": repo.created_at.isoformat() if repo.created_at else None,
                "updated_at": repo.updated_at.isoformat() if repo.updated_at else None,
                "pushed_at": repo.pushed_at.isoformat() if repo.pushed_at else None,
                "total_commits": commit_history.total_commits if commit_history else 0,
                "recent_commits_90d": commit_history.recent_90d if commit_history else 0,
                "first_commit_date": (
                    first_commit_date.isoformat() if first_commit_date else None
                ),
                "last_commit_date": (
                    commit_history.last_commit_date.isoformat()
                    if commit_history and commit_history.last_commit_date
                    else (repo.pushed_at.isoformat() if repo.pushed_at else None)
                ),
                "commit_history": commit_history_dict,
                "commit_metrics": commit_metrics,
                "avg_commit_size": avg_commit_size,
                "largest_commit": largest_commit,
                "smallest_commit": smallest_commit,
                "commit_velocity": commit_history.commit_frequency if commit_history else None,
                "tech_stack": tech_stack.to_dict() if tech_stack else None,
                "has_readme": repo.has_readme,
                "has_license": repo.has_license,
                "has_ci_cd": repo.has_ci_cd,
                "has_tests": repo.has_tests,
                "has_docs": repo.has_docs,
                "language_count": repo.language_count,
                "size_kb": repo.size_kb,
                "is_fork": repo.is_fork,
                "is_private": repo.is_private,
                "is_archived": repo.is_archived,
                "age_days": repo.age_days,
                "days_since_last_push": repo.days_since_last_push,
                "ai_summary": ai_summary_text,
                "rank": rank,
                "composite_score": score,
            }
            unified_repos.append(repo_dict)
        
        # Create user profile
        profile = {
            "username": self.username,
            "total_repositories": len(repositories),
            "total_stars": sum(r.stars for r in repositories),
            "total_forks": sum(r.forks for r in repositories),
            "total_commits": sum(ch.total_commits for ch in commit_histories.values()),
        }
        
        # Create metadata
        metadata = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "schema_version": "2.0.0",
            "generator": "unified_data_generator"
        }
        
        return {
            "profile": profile,
            "repositories": unified_repos,
            "metadata": metadata
        }

    def save(self, unified_data: Optional[Dict[str, Any]] = None) -> tuple[Path, bool]:
        """Generate and save unified data to repositories.json file.
        
        Phase 4: Output generation (no cache operations).
        
        Args:
            unified_data: Optional pre-generated data dict.
                         If None, will call generate().
                         
        Returns:
            Tuple of (Path to saved JSON file, generation skipped flag)
        """
        if unified_data is None:
            unified_data = self.generate()

        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Write JSON file
        output_path = self.output_dir / "repositories.json"
        logger.info(f"Writing unified data to {output_path}...")

        try:
            import json
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(unified_data, f, indent=2, ensure_ascii=False)
            
            file_size = output_path.stat().st_size
            file_size_kb = file_size / 1024
            logger.info(f"Unified data written successfully ({file_size_kb:.2f} KB)")
            
            return output_path, False
            
        except Exception as e:
            logger.error(f"Failed to write unified data: {e}")
            raise


