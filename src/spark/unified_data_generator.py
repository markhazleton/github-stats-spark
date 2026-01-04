"""Unified data generator that merges all CLI commands into comprehensive repositories.json.

This module combines data from generate, analyze, and dashboard commands into a single
comprehensive JSON file with all attributes needed by the frontend.
"""

import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

from spark.cache import APICache
from spark.config import SparkConfig
from spark.fetcher import GitHubFetcher
from spark.ranker import RepositoryRanker
from spark.summarizer import RepositorySummarizer
from spark.dependencies import RepositoryDependencyAnalyzer
from spark.calculator import StatsCalculator
from spark.models.repository import Repository
from spark.models.commit import CommitHistory
from spark.models.summary import RepositorySummary
from spark.models.tech_stack import TechnologyStack
from spark.models.dashboard_data import (
    DashboardData,
    DashboardRepository,
    DashboardMetadata,
    UserProfile,
    CommitMetric,
)

logger = logging.getLogger(__name__)


class UnifiedDataGenerator:
    """Generates comprehensive unified repository data combining all analysis features.
    
    This generator merges data from:
    - generate: Basic repository metadata and stats
    - analyze: Repository ranking, commit analysis, tech stack
    - dashboard: Commit metrics, user profile
    
    Attributes:
        config: SparkConfig instance
        username: GitHub username to analyze
        cache: APICache instance for caching API calls
        fetcher: GitHubFetcher for GitHub API access
        ranker: RepositoryRanker for scoring repositories
        summarizer: RepositorySummarizer for AI summaries
        dependency_analyzer: RepositoryDependencyAnalyzer for tech stack analysis
        output_dir: Output directory for JSON file
    """

    def __init__(
        self,
        config: SparkConfig,
        username: str,
        output_dir: str = "data",
        force_refresh: bool = False,
    ):
        """Initialize the UnifiedDataGenerator.
        
        Args:
            config: SparkConfig instance with all configuration
            username: GitHub username to analyze
            output_dir: Directory for output JSON file
            force_refresh: Whether to bypass cache and fetch fresh data
        """
        self.config = config
        self.username = username
        self.output_dir = Path(output_dir)
        self.force_refresh = force_refresh

        # Initialize components
        self.cache = APICache()
        if force_refresh:
            self.cache.clear()
            logger.info("Cache cleared for fresh data")

        token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise ValueError("GITHUB_TOKEN environment variable not set")

        self.fetcher = GitHubFetcher(cache=self.cache, token=token)
        
        ranking_config = config.config.get("analyzer", {}).get("ranking_weights", {})
        self.ranker = RepositoryRanker(config=ranking_config)
        
        self.summarizer = RepositorySummarizer(cache=self.cache)
        
        analyzer_config = config.config.get("analyzer", {})
        self.dependency_analyzer = RepositoryDependencyAnalyzer(
            cache=self.cache,
            config=analyzer_config
        )

        # Configuration
        dashboard_config = config.config.get("dashboard", {})
        data_gen_config = dashboard_config.get("data_generation", {})
        self.max_repositories = data_gen_config.get("max_repositories", 200)
        self.max_commits_per_repo = data_gen_config.get("max_commits_per_repo", 200)
        self.include_ai_summaries = data_gen_config.get("include_ai_summaries", False)
        self.top_n_repos = config.config.get("analyzer", {}).get("top_repositories", 50)

        logger.info(f"UnifiedDataGenerator initialized for user: {username}")
        logger.info(f"Max repositories: {self.max_repositories}")
        logger.info(f"Include AI summaries: {self.include_ai_summaries}")

    def generate(self) -> Dict[str, Any]:
        """Generate comprehensive unified repository data.
        
        This is the main entry point that orchestrates all data gathering:
        1. Fetch all repositories
        2. Analyze commits and calculate metrics
        3. Rank repositories
        4. Generate AI summaries (optional)
        5. Analyze tech stack and dependencies
        6. Combine all data into unified structure
        
        Returns:
            Dictionary with unified repository data including all attributes
        """
        start_time = datetime.now()
        logger.info("=" * 70)
        logger.info("Starting Unified Data Generation")
        logger.info("=" * 70)

        # Step 1: Fetch all repositories
        logger.info(f"Fetching repositories for {self.username}...")
        repos_config = self.config.config.get("repositories", {})
        exclude_forks = repos_config.get("exclude_forks", False)
        exclude_archived = repos_config.get("exclude_archived", True)  # Default: skip archived repos
        
        raw_repos = self.fetcher.fetch_repositories(
            username=self.username,
            exclude_private=True,
            exclude_forks=exclude_forks
        )
        
        # Filter out archived repositories if configured
        if exclude_archived:
            before_count = len(raw_repos)
            raw_repos = [r for r in raw_repos if not r.get('archived', False)]
            archived_count = before_count - len(raw_repos)
            if archived_count > 0:
                logger.info(f"Filtered out {archived_count} archived repositories")
        
        logger.info(f"Found {len(raw_repos)} repositories")

        # Apply max_repositories limit
        if len(raw_repos) > self.max_repositories:
            logger.warning(
                f"Limiting to {self.max_repositories} repositories (found {len(raw_repos)})"
            )
            raw_repos = raw_repos[:self.max_repositories]

        # Step 2: Convert to Repository objects and gather comprehensive data
        repositories = []
        commit_histories = {}
        commit_metrics = {}  # Store detailed commit metrics (avg, largest, smallest)
        tech_stacks = {}
        summaries = {}
        errors = []

        for i, raw_repo in enumerate(raw_repos, 1):
            repo_name = raw_repo.get("name", "unknown")
            progress_pct = (i / len(raw_repos)) * 100
            logger.info(f"[{i}/{len(raw_repos)}] ({progress_pct:.0f}%) Processing {repo_name}...")

            try:
                # Get full GitHub repo object
                github_repo = self.fetcher.github.get_repo(
                    f"{self.username}/{repo_name}"
                )
                repo = Repository.from_github_repo(github_repo)

                # Fetch language stats
                repo.language_stats = self.fetcher.fetch_languages(
                    self.username, 
                    repo_name
                )
                repo.language_count = len(repo.language_stats)

                # Fetch commit data and metrics
                commit_data = self.fetcher.fetch_commit_counts(self.username, repo_name)
                commit_history = CommitHistory(
                    repository_name=repo_name,
                    total_commits=commit_data["total"],
                    recent_90d=commit_data["recent_90d"],
                    recent_180d=commit_data["recent_180d"],
                    recent_365d=commit_data["recent_365d"],
                    last_commit_date=(
                        datetime.fromisoformat(commit_data["last_commit_date"])
                        if commit_data["last_commit_date"]
                        else None
                    ),
                )

                # Calculate commit velocity
                if repo.age_days > 0:
                    months = repo.age_days / 30.0
                    repo.commit_velocity = (
                        commit_data["total"] / months if months > 0 else 0
                    )

                commit_histories[repo_name] = commit_history

                # Fetch detailed commit metrics (for largest/smallest commits)
                # Optimize: Reduce max commits for repos with no recent activity
                max_commits_to_fetch = self.max_commits_per_repo
                if commit_history.recent_90d == 0:
                    # No recent activity - fetch fewer commits
                    max_commits_to_fetch = min(50, self.max_commits_per_repo)
                    logger.debug(f"  No recent activity, reducing to {max_commits_to_fetch} commits")
                
                # Pass push date for intelligent cache invalidation
                commits_with_stats = self.fetcher.fetch_commits_with_stats(
                    username=self.username,
                    repo_name=repo_name,
                    max_commits=max_commits_to_fetch,
                    repo_pushed_at=github_repo.pushed_at
                )
                
                # Calculate commit metrics from fetched commits
                if commits_with_stats:
                    try:
                        commit_sizes = []
                        largest_commit = None
                        smallest_commit = None
                        first_commit_date = None
                        
                        for commit_dict in commits_with_stats:
                            # Extract stats from the nested structure
                            stats = commit_dict.get("stats", {})
                            files_changed = stats.get("total", 0)
                            additions = stats.get("additions", 0)
                            deletions = stats.get("deletions", 0)
                            
                            # Calculate total size (files + lines changed)
                            size = files_changed + additions + deletions
                            commit_sizes.append(size)
                            
                            # Get commit date from nested author structure
                            commit_info_nested = commit_dict.get("commit", {})
                            author_info = commit_info_nested.get("author", {})
                            commit_date = author_info.get("date")
                            
                            commit_info = {
                                "size": size,
                                "files_changed": files_changed,
                                "lines_added": additions,
                                "lines_deleted": deletions,
                                "sha": commit_dict.get("sha", ""),
                                "date": commit_date,
                            }
                            
                            if largest_commit is None or size > largest_commit["size"]:
                                largest_commit = commit_info
                            
                            # For smallest, we want the smallest non-zero commit
                            # If all commits are zero, we'll still track one
                            if smallest_commit is None:
                                smallest_commit = commit_info
                            elif size > 0 and size < smallest_commit["size"]:
                                smallest_commit = commit_info
                            elif smallest_commit["size"] == 0 and size > 0:
                                smallest_commit = commit_info
                            
                            # Track first commit date (oldest commit)
                            if commit_date:
                                if first_commit_date is None:
                                    first_commit_date = commit_date
                                else:
                                    # Find the oldest date
                                    first_commit_date = min(first_commit_date, commit_date)
                        
                        if commit_sizes:
                            avg_size = sum(commit_sizes) / len(commit_sizes)
                            commit_metrics[repo_name] = {
                                "avg_size": round(avg_size, 2),
                                "largest_commit": largest_commit,
                                "smallest_commit": smallest_commit,
                                "first_commit_date": first_commit_date,
                            }
                            logger.debug(f"  Commit metrics: avg={avg_size:.1f}, largest={largest_commit['size']}, smallest={smallest_commit['size']}")
                    except Exception as e:
                        logger.debug(f"  Failed to calculate commit metrics: {e}")

                # Analyze tech stack and dependencies
                try:
                    tech_stack = self.dependency_analyzer.analyze_github_repository(
                        github_repo
                    )
                    if tech_stack and tech_stack.total_dependencies > 0:
                        tech_stacks[repo_name] = tech_stack
                        logger.debug(
                            f"  Tech stack: {tech_stack.total_dependencies} dependencies, "
                            f"{tech_stack.outdated_count} outdated"
                        )
                except Exception as e:
                    logger.debug(f"  Tech stack analysis skipped: {e}")

                # Generate AI summary (optional)
                if self.include_ai_summaries:
                    try:
                        readme_content = None
                        if repo.has_readme:
                            try:
                                readme = github_repo.get_readme()
                                readme_content = readme.decoded_content.decode('utf-8')
                            except Exception as e:
                                logger.debug(f"  Could not fetch README: {e}")

                        summary = self.summarizer.summarize_repository(
                            repo, readme_content, commit_history
                        )
                        summaries[repo_name] = summary
                        logger.debug("  AI summary generated")
                    except Exception as e:
                        logger.warning(f"  Summary generation failed: {e}")

                repositories.append(repo)

            except Exception as e:
                error_msg = str(e)
                if "rate limit" in error_msg.lower() or "403" in error_msg:
                    logger.error("GitHub API rate limit reached!")
                    errors.append(f"Rate limit at repo {i}/{len(raw_repos)}: {repo_name}")
                    break
                else:
                    logger.warning(f"Failed to process {repo_name}: {error_msg}")
                    errors.append(f"Failed: {repo_name}: {error_msg}")
                    continue

        # Step 3: Rank repositories
        logger.info(f"Ranking {len(repositories)} repositories...")
        ranked_repos = self.ranker.rank_repositories(
            repositories, commit_histories, top_n=self.top_n_repos
        )

        # Step 4: Build unified repository data structures
        logger.info("Building unified repository data...")
        unified_repos = []

        for rank, (repo, score) in enumerate(ranked_repos, 1):
            repo_data = self._build_unified_repo_data(
                repo=repo,
                rank=rank,
                score=score,
                commit_history=commit_histories.get(repo.name),
                commit_metrics=commit_metrics.get(repo.name),
                tech_stack=tech_stacks.get(repo.name),
                summary=summaries.get(repo.name),
            )
            unified_repos.append(repo_data)

        # Add unranked repositories (beyond top N)
        ranked_names = {repo.name for repo, _ in ranked_repos}
        for repo in repositories:
            if repo.name not in ranked_names:
                repo_data = self._build_unified_repo_data(
                    repo=repo,
                    rank=None,
                    score=None,
                    commit_history=commit_histories.get(repo.name),
                    commit_metrics=commit_metrics.get(repo.name),
                    tech_stack=tech_stacks.get(repo.name),
                    summary=summaries.get(repo.name),
                )
                unified_repos.append(repo_data)

        # Step 5: Generate user profile
        logger.info("Generating user profile...")
        user_data = self.fetcher.get_user(self.username)
        
        # Calculate aggregate statistics
        total_stars = sum(repo.stars for repo in repositories)
        total_forks = sum(repo.forks for repo in repositories)
        total_commits = sum(
            commit_histories[repo.name].total_commits
            for repo in repositories
            if repo.name in commit_histories
        )

        profile = {
            "username": user_data.get("login", self.username),
            "avatar_url": user_data.get("avatar_url", ""),
            "public_repos_count": user_data.get("public_repos", len(repositories)),
            "profile_url": user_data.get("html_url", ""),
            "total_commits": total_commits,
            "total_stars": total_stars,
            "total_forks": total_forks,
            "bio": user_data.get("bio"),
            "company": user_data.get("company"),
            "location": user_data.get("location"),
            "blog": user_data.get("blog"),
            "twitter_username": user_data.get("twitter_username"),
        }

        # Step 6: Create metadata
        end_time = datetime.now()
        generation_time = (end_time - start_time).total_seconds()

        metadata = {
            "generated_at": datetime.now().isoformat(),
            "schema_version": "2.0.0",
            "repository_count": len(unified_repos),
            "data_source": "GitHub API",
            "generation_time_seconds": generation_time,
            "cache_hit_rate": self._calculate_cache_hit_rate(),
            "errors": errors if errors else None,
            "partial_results": len(errors) > 0,
            "features": {
                "commit_metrics": True,
                "tech_stack_analysis": len(tech_stacks) > 0,
                "ai_summaries": self.include_ai_summaries,
                "ranking": True,
            },
        }

        # Include AI usage stats if summaries were generated
        if self.include_ai_summaries and self.summarizer.total_tokens_used > 0:
            stats = self.summarizer.get_usage_stats()
            metadata["ai_usage"] = {
                "total_tokens": stats["total_tokens"],
                "total_cost_usd": stats["total_cost_usd"],
                "cache_hits": stats["cache_hits"],
                "cache_misses": stats["cache_misses"],
                "cache_hit_rate": stats["cache_hit_rate"],
            }

        # Step 7: Build final unified data structure
        unified_data = {
            "repositories": unified_repos,
            "profile": profile,
            "metadata": metadata,
        }

        # Log summary
        logger.info("")
        logger.info("=" * 70)
        logger.info("✅ Unified Data Generation Complete")
        logger.info("=" * 70)
        logger.info(f"Repositories: {len(unified_repos)}")
        logger.info(f"Top Ranked: {len(ranked_repos)}")
        logger.info(f"Tech Stacks: {len(tech_stacks)}")
        if self.include_ai_summaries:
            logger.info(f"AI Summaries: {len(summaries)}")
        logger.info(f"Generation Time: {generation_time:.1f}s")
        if errors:
            logger.warning(f"Errors: {len(errors)}")
        logger.info("=" * 70)

        return unified_data

    def _build_unified_repo_data(
        self,
        repo: Repository,
        rank: Optional[int],
        score: Optional[float],
        commit_history: Optional[CommitHistory],
        commit_metrics: Optional[Dict[str, Any]],
        tech_stack: Optional[TechnologyStack],
        summary: Optional[RepositorySummary],
    ) -> Dict[str, Any]:
        """Build unified repository data dictionary with all attributes.
        
        Args:
            repo: Repository instance
            rank: Repository rank (1-based) or None if unranked
            score: Composite ranking score or None
            commit_history: CommitHistory instance or None
            commit_metrics: Dictionary with avg_size, largest_commit, smallest_commit or None
            tech_stack: TechnologyStack instance or None
            summary: RepositorySummary instance or None
            
        Returns:
            Dictionary with comprehensive repository data
        """
        data = {
            # Basic metadata
            "name": repo.name,
            "description": repo.description,
            "url": repo.url,
            "language": repo.primary_language or "Unknown",
            
            # Dates
            "created_at": repo.created_at.isoformat() if repo.created_at else None,
            "updated_at": repo.updated_at.isoformat() if repo.updated_at else None,
            "pushed_at": repo.pushed_at.isoformat() if repo.pushed_at else None,
            
            # Repository stats
            "stars": repo.stars,
            "forks": repo.forks,
            "watchers": repo.watchers,
            "open_issues": repo.open_issues,
            "size_kb": repo.size_kb,
            
            # Repository attributes
            "is_archived": repo.is_archived,
            "is_fork": repo.is_fork,
            "has_readme": repo.has_readme,
            "has_license": repo.has_license,
            "has_ci_cd": repo.has_ci_cd,
            "has_tests": repo.has_tests,
            "has_docs": repo.has_docs,
            
            # Languages
            "language_stats": repo.language_stats,
            "language_count": repo.language_count,
            
            # Activity metrics
            "age_days": repo.age_days,
            "days_since_last_push": repo.days_since_last_push,
            "commit_velocity": repo.commit_velocity,
            "contributors_count": repo.contributors_count,
            "release_count": repo.release_count,
            "latest_release_date": (
                repo.latest_release_date.isoformat()
                if repo.latest_release_date
                else None
            ),
            
            # Ranking (if applicable)
            "rank": rank,
            "composite_score": round(score, 2) if score else None,
        }

        # Add commit history data
        if commit_history:
            data["commit_history"] = {
                "total_commits": commit_history.total_commits,
                "recent_90d": commit_history.recent_90d,
                "recent_180d": commit_history.recent_180d,
                "recent_365d": commit_history.recent_365d,
                "last_commit_date": (
                    commit_history.last_commit_date.isoformat()
                    if commit_history.last_commit_date
                    else None
                ),
                "first_commit_date": (
                    commit_metrics["first_commit_date"]
                    if commit_metrics and commit_metrics.get("first_commit_date")
                    else None
                ),
            }
        
        # Add commit metrics data (avg size, largest, smallest)
        if commit_metrics:
            data["commit_metrics"] = {
                "avg_size": commit_metrics.get("avg_size"),
                "largest_commit": commit_metrics.get("largest_commit"),
                "smallest_commit": commit_metrics.get("smallest_commit"),
            }

        # Add tech stack data
        if tech_stack:
            data["tech_stack"] = {
                "frameworks": tech_stack.frameworks,
                "dependencies": [dep.to_dict() for dep in tech_stack.dependencies],
                "dependency_file_type": tech_stack.dependency_file_type,
                "total_dependencies": tech_stack.total_dependencies,
                "outdated_count": tech_stack.outdated_count,
                "outdated_percentage": tech_stack.outdated_percentage,
                "currency_score": tech_stack.currency_score,
            }

        # Add AI summary data
        if summary:
            data["summary"] = {
                "text": summary.summary,
                "ai_generated": summary.is_ai_generated,
                "generation_method": summary.generation_method,
                "confidence_score": summary.confidence_score,
                "model_used": summary.model_used,
            }

        return data

    def _calculate_cache_hit_rate(self) -> Optional[str]:
        """Calculate cache hit rate as a percentage string.
        
        Returns:
            String like "75% (30/40)" or None if no cache stats available
        """
        # This would require cache statistics tracking
        # For now, return None as a placeholder
        return None

    def save(self, unified_data: Optional[Dict[str, Any]] = None) -> Path:
        """Generate and save unified data to repositories.json file.
        
        Args:
            unified_data: Optional pre-generated unified data.
                         If None, will generate new data.
                         
        Returns:
            Path to saved JSON file
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
            
            return output_path
            
        except Exception as e:
            logger.error(f"Failed to write unified data: {e}")
            raise


def main():
    """Command-line entry point for unified data generation."""
    import argparse
    from spark.logger import get_logger
    
    parser = argparse.ArgumentParser(
        description="Generate unified repositories.json with all attributes"
    )
    parser.add_argument(
        "--user",
        type=str,
        required=True,
        help="GitHub username to analyze"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="config/spark.yml",
        help="Configuration file path"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="data",
        help="Output directory for repositories.json"
    )
    parser.add_argument(
        "--force-refresh",
        action="store_true",
        help="Bypass cache and fetch fresh data"
    )
    parser.add_argument(
        "--include-ai-summaries",
        action="store_true",
        help="Include AI-generated summaries (requires API key)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    logger = get_logger("unified-data-generator", verbose=args.verbose)
    
    # Check for GitHub token
    if not os.getenv("GITHUB_TOKEN"):
        logger.error("GITHUB_TOKEN environment variable not set")
        logger.info("Please set your GitHub Personal Access Token:")
        logger.info("  export GITHUB_TOKEN=your_token_here")
        return 1
    
    try:
        # Load config
        config = SparkConfig(args.config)
        config.load()
        
        # Override AI summaries setting if specified
        if args.include_ai_summaries:
            dashboard_config = config.config.get("dashboard", {})
            data_gen = dashboard_config.get("data_generation", {})
            data_gen["include_ai_summaries"] = True
        
        # Create generator
        generator = UnifiedDataGenerator(
            config=config,
            username=args.user,
            output_dir=args.output_dir,
            force_refresh=args.force_refresh,
        )
        
        # Generate and save
        output_path = generator.save()
        
        logger.info("")
        logger.info("✅ Success! Unified data saved to:")
        logger.info(f"   {output_path}")
        
        return 0
        
    except Exception as e:
        logger.error(f"Unified data generation failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
