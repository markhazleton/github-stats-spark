"""Unified report workflow orchestration."""

import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from github import RateLimitExceededException

from spark.cache import APICache
from spark.config import SparkConfig
from spark.fetcher import GitHubFetcher
from spark.calculator import StatsCalculator
from spark.visualizer import StatisticsVisualizer
from spark.ranker import RepositoryRanker
from spark.summarizer import RepositorySummarizer
from spark.dependencies.analyzer import RepositoryDependencyAnalyzer
from spark.models import (
    UnifiedReport,
    GitHubData,
    RepositoryAnalysis,
    UserProfile,
    Repository,
    CommitHistory,
)
from spark.exceptions import WorkflowError
from spark.logger import get_logger
from spark.themes.spark_dark import SparkDarkTheme


class UnifiedReportWorkflow:
    """Orchestrates unified report generation with partial failure handling.

    This workflow combines SVG visualization generation with repository analysis
    into a single unified profile report, handling partial failures gracefully.

    Workflow stages:
        1. Fetch GitHub data (required - fails entire workflow if unsuccessful)
        2. Generate SVGs (optional - continues with warnings if fails)
        3. Analyze repositories (optional - continues with warnings if fails)
        4. Generate unified report (required - uses available data)
    """

    def __init__(
        self,
        config: SparkConfig,
        cache: Optional[APICache] = None,
        output_dir: str = "output",
        max_repos: Optional[int] = None,
    ):
        """Initialize unified report workflow.

        Args:
            config: Spark configuration instance
            cache: API cache instance (creates new if not provided)
            output_dir: Base output directory for SVGs and reports
            max_repos: Optional limit on number of repositories to process
        """
        self.logger = get_logger()
        self.config = config
        self.cache = cache or APICache()
        self.output_dir = Path(output_dir)

        # Initialize components
        self.fetcher = GitHubFetcher(cache=self.cache)
        self.theme = SparkDarkTheme()  # TODO: Load from config
        self.visualizer = StatisticsVisualizer(self.theme, enable_effects=True)

        analyzer_config = self.config.get("analyzer", {})
        self.ranker = RepositoryRanker(config=analyzer_config)
        self.summarizer = RepositorySummarizer(cache=self.cache)
        self.dependency_analyzer = RepositoryDependencyAnalyzer()

        # Track errors and warnings
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.start_time: float = 0.0
        self.api_calls: int = 0
        
        # Store max_repos limit
        self.max_repos = max_repos
        if max_repos is not None:
            self.logger.info(f"⚠️  Testing mode: Limited to {max_repos} repositories for SVG/report generation")
        
        # Store max_repos limit
        self.max_repos = max_repos
        if max_repos is not None:
            self.logger.info(f"⚠️  Testing mode: Limited to {max_repos} repositories for SVG/report generation")

    def execute(self, username: str) -> UnifiedReport:
        """Execute unified report workflow with partial failure handling.

        Args:
            username: GitHub username to analyze

        Returns:
            UnifiedReport with generated content and error metadata

        Raises:
            WorkflowError: If critical stages fail (data fetching, report generation)
        """
        self.start_time = time.time()
        self.logger.info(f"Starting unified report workflow for {username}")

        # Stage 1: Fetch GitHub data (REQUIRED)
        try:
            github_data = self._fetch_github_data(username)
        except Exception as e:
            self.logger.error(f"Failed to fetch GitHub data: {e}")
            raise WorkflowError(
                "Cannot proceed without GitHub data",
                stage="fetch_github_data",
                cause=e
            ) from e

        # Stage 2: Generate SVGs (OPTIONAL - FR-011)
        available_svgs = []
        try:
            available_svgs = self._generate_svgs(username, github_data)
        except Exception as e:
            self.logger.warn(f"SVG generation failed: {e}")
            self.warnings.append(f"SVG generation failed: {str(e)}")
            # Continue workflow - report will note missing visualizations

        # Stage 3: Analyze repositories (OPTIONAL - FR-012)
        repository_analyses = []
        try:
            repository_analyses = self._analyze_repositories(
                username, github_data.repositories, github_data.commit_histories
            )
        except Exception as e:
            self.logger.warn(f"Repository analysis failed: {e}")
            self.warnings.append(f"Repository analysis failed: {str(e)}")
            # Continue workflow - report will show available data only

        # Stage 4: Generate unified report (REQUIRED)
        report = self._generate_unified_report(
            username=username,
            github_data=github_data,
            available_svgs=available_svgs,
            repository_analyses=repository_analyses,
        )

        generation_time = time.time() - self.start_time
        report.generation_time = generation_time
        report.errors = self.errors
        report.warnings = self.warnings

        self.logger.info(
            f"Unified report workflow completed in {generation_time:.1f}s "
            f"(success rate: {report.success_rate}%)"
        )

        return report

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=60, min=60, max=900),  # 1min, 5min, 15min
        retry=retry_if_exception_type(RateLimitExceededException),
    )
    def _fetch_github_data(self, username: str) -> GitHubData:
        """Fetch all required GitHub data with retry logic.

        Args:
            username: GitHub username

        Returns:
            GitHubData container with profile, repositories, and commit histories

        Raises:
            WorkflowError: If data fetching fails after retries
        """
        self.logger.info(f"[fetch_github_data] Fetching data for {username}")
        fetch_start = time.time()

        try:
            # Fetch user profile
            profile_data = self.fetcher.fetch_user_profile(username)
            user_profile = UserProfile.from_dict(profile_data)

            # Fetch repositories (public only)
            repos_data = self.fetcher.fetch_repositories(username, exclude_private=True)
            repositories = [Repository.from_dict(r) for r in repos_data]
            
            # Apply max_repos limit if specified
            if self.max_repos is not None and len(repositories) > self.max_repos:
                self.logger.info(f"Limiting to first {self.max_repos} of {len(repositories)} repositories")
                repositories = repositories[:self.max_repos]

            # Fetch commit histories for all repositories
            commit_histories: Dict[str, CommitHistory] = {}
            for repo in repositories:
                try:
                    # Pass pushed_at for weekly cache invalidation
                    commits_data = self.fetcher.fetch_commit_counts(
                        username, 
                        repo.name, 
                        repo_pushed_at=repo.pushed_at
                    )
                    # Add repository_name to the data before creating CommitHistory
                    commits_data["repository_name"] = repo.name
                    commit_histories[repo.name] = CommitHistory.from_dict(commits_data)
                except Exception as e:
                    self.logger.warn(
                        f"Failed to fetch commits for {repo.name}: {e}"
                    )
                    self.errors.append(f"Commit fetch failed: {repo.name}")

            fetch_time = time.time() - fetch_start
            self.logger.info(
                f"[fetch_github_data] Fetched {len(repositories)} repos in {fetch_time:.1f}s"
            )

            return GitHubData(
                username=username,
                profile=user_profile,
                repositories=repositories,
                commit_histories=commit_histories,
                fetch_timestamp=datetime.utcnow(),
                api_call_count=self.api_calls,
                cache_hit_count=0,  # TODO: Track from cache
            )

        except Exception as e:
            raise WorkflowError(
                f"Failed to fetch GitHub data for {username}",
                stage="fetch_github_data",
                cause=e
            ) from e

    def _generate_svgs(
        self, username: str, github_data: GitHubData
    ) -> List[str]:
        """Generate SVG visualizations (FR-011: continue if fails).

        Args:
            username: GitHub username
            github_data: Fetched GitHub data

        Returns:
            List of successfully generated SVG types (ordered per FR-017)
        """
        self.logger.info("[generate_svgs] Generating SVG visualizations")
        available_svgs = []

        # FR-017 ordering
        svg_types = ["overview", "heatmap", "streaks", "release", "languages", "fun"]
        enabled_stats = self.config.get_enabled_stats()

        # Initialize calculator with fetched data
        profile_dict = github_data.profile.to_dict() if github_data.profile else {}
        repos_dict = [r.to_dict() for r in github_data.repositories]
        calculator = StatsCalculator(profile_dict, repos_dict)

        # Pre-fetch data for all repositories once
        self.logger.info(f"[generate_svgs] Pre-fetching detailed stats for {len(github_data.repositories)} repositories")
        
        for repo in github_data.repositories:
            try:
                # Fetch actual commits (needed for heatmaps, time patterns, etc.)
                # Use repo.pushed_at from existing object to avoid extra API call
                commits = self.fetcher.fetch_commits(
                    username, 
                    repo.name, 
                    max_commits=100,
                    repo_pushed_at=repo.pushed_at
                )
                if commits:
                    calculator.add_commits(commits)
                
                # Fetch language statistics
                languages = self.fetcher.fetch_languages(
                    username, 
                    repo.name,
                    repo_pushed_at=repo.pushed_at
                )
                if languages:
                    calculator.add_languages(languages)
                    
            except Exception as e:
                self.logger.debug(f"Could not fetch detailed stats for {repo.name}: {e}")

        # Calculate statistics once
        stats = calculator.calculate_statistics()

        for svg_type in svg_types:
            if svg_type not in enabled_stats:
                self.logger.debug(f"Skipping disabled SVG: {svg_type}")
                continue

            try:
                svg_content = self._generate_single_svg(
                    svg_type, username, stats
                )
                svg_path = self.output_dir / f"{svg_type}.svg"
                svg_path.parent.mkdir(parents=True, exist_ok=True)

                with open(svg_path, "w", encoding="utf-8") as f:
                    f.write(svg_content)

                available_svgs.append(svg_type)
                self.logger.info(f"Generated {svg_type}.svg")

            except Exception as e:
                self.logger.warn(f"Failed to generate {svg_type}.svg: {e}")
                self.warnings.append(f"SVG generation failed: {svg_type}")
                # Continue to next SVG (FR-011: partial failures OK)

        self.logger.info(
            f"[generate_svgs] Generated {len(available_svgs)}/{len(svg_types)} SVGs"
        )
        return available_svgs

    def _generate_single_svg(
        self, svg_type: str, username: str, stats: Dict[str, Any]
    ) -> str:
        """Generate a single SVG visualization.

        Args:
            svg_type: Type of SVG to generate
            username: GitHub username
            stats: Calculated statistics dictionary

        Returns:
            SVG content as string

        Raises:
            Exception: If SVG generation fails
        """
        # Generate appropriate SVG based on type
        if svg_type == "overview":
            return self.visualizer.generate_overview(
                username=username,
                spark_score=stats.get("spark_score", {}),
                total_commits=stats.get("total_commits", 0),
                languages=stats.get("languages", []),
                time_pattern=stats.get("time_pattern", {}),
            )
        elif svg_type == "heatmap":
            return self.visualizer.generate_heatmap(
                commits_by_date=stats.get("commits_by_day", {}),
                username=username,
            )
        elif svg_type == "streaks":
            return self.visualizer.generate_streaks(
                streaks=stats.get("streaks", {}),
                username=username,
            )
        elif svg_type == "release":
            return self.visualizer.generate_release_cadence(
                cadence=stats.get("release_cadence", {}),
                username=username,
            )
        elif svg_type == "languages":
            return self.visualizer.generate_languages(
                languages=stats.get("languages", []),
                username=username,
            )
        elif svg_type == "fun":
            return self.visualizer.generate_fun_stats(
                stats=stats.get("fun_stats", {}),
                username=username,
            )
        else:
            raise ValueError(f"Unknown SVG type: {svg_type}")

    def _analyze_repositories(
        self,
        username: str,
        repositories: List[Repository],
        commit_histories: Dict[str, CommitHistory],
    ) -> List[RepositoryAnalysis]:
        """Analyze repositories (FR-012: individual repo failures don't block report).

        Args:
            username: GitHub username
            repositories: List of repositories to analyze
            commit_histories: Commit data by repository name

        Returns:
            List of RepositoryAnalysis objects (top 50, ranked by composite score)
        """
        self.logger.info(
            f"[analyze_repositories] Analyzing {len(repositories)} repositories"
        )
        analyses = []

        # Rank repositories
        top_n = self.config.get("analyzer.top_repositories", 50)
        ranked = self.ranker.rank_repositories(
            repositories, commit_histories, top_n=top_n
        )

        for rank, (repo, score) in enumerate(ranked, 1):
            try:
                # Fetch README for AI summary (with push date for caching)
                # Use repo.pushed_at from existing object to avoid extra API call
                readme_content = self.fetcher.fetch_readme(
                    username, 
                    repo.name,
                    repo_pushed_at=repo.pushed_at
                )
                
                # Fetch language statistics (with push date for weekly caching)
                language_stats = self.fetcher.fetch_languages(
                    username, 
                    repo.name,
                    repo_pushed_at=repo.pushed_at
                )
                
                # Update repository with language stats
                if language_stats:
                    repo.language_stats = language_stats
                    repo.language_count = len(language_stats)
                
                # Analyze dependencies and tech stack (before summary)
                tech_stack = None
                try:
                    # Fetch dependency files from the repository (with push date for weekly caching)
                    dependency_files = self.fetcher.fetch_dependency_files(
                        username, 
                        repo.name, 
                        repo_pushed_at=repo.pushed_at
                    )
                    
                    if dependency_files:
                        # Analyze dependencies if files were found
                        dep_report = self.dependency_analyzer.analyze_repository(dependency_files)
                        
                        # Convert to TechnologyStack model (if needed)
                        from spark.models.tech_stack import TechnologyStack, Dependency as TechDependency
                        tech_stack = TechnologyStack(
                            repository_name=repo.name,
                            dependencies=[
                                TechDependency(
                                    name=detail.name,
                                    version=detail.installed_version,
                                    ecosystem=detail.ecosystem,
                                    category='library',  # Could be enhanced based on package type
                                )
                                for detail in dep_report.details
                            ],
                            currency_score=int(dep_report.currency_score),
                            outdated_count=dep_report.outdated_dependencies,
                        )
                except Exception as e:
                    self.logger.debug(
                        f"Dependency analysis skipped for {repo.name}: {e}"
                    )
                
                # Generate summary with all collected stats (uses AI if README available)
                summary = self.summarizer.summarize_repository(
                    repo=repo,
                    readme_content=readme_content,
                    commit_history=commit_histories.get(repo.name),
                    language_stats=language_stats,
                    tech_stack=tech_stack,
                    repository_owner=username,
                    repo_pushed_at=repo.pushed_at,
                )

                analysis = RepositoryAnalysis(
                    repository=repo,
                    commit_history=commit_histories.get(repo.name),
                    summary=summary,
                    tech_stack=tech_stack,
                    rank=rank,
                    composite_score=score,
                )
                analyses.append(analysis)

            except Exception as e:
                self.logger.warn(f"Failed to analyze {repo.name}: {e}")
                self.errors.append(f"Repository analysis failed: {repo.name}")
                # Continue to next repository (FR-012: partial results OK)

        self.logger.info(
            f"[analyze_repositories] Successfully analyzed {len(analyses)}/{len(ranked)} repositories"
        )
        return analyses

    def _generate_unified_report(
        self,
        username: str,
        github_data: GitHubData,
        available_svgs: List[str],
        repository_analyses: List[RepositoryAnalysis],
    ) -> UnifiedReport:
        """Generate UnifiedReport entity from workflow results.

        Args:
            username: GitHub username
            github_data: Fetched GitHub data
            available_svgs: List of successfully generated SVG types
            repository_analyses: List of repository analyses

        Returns:
            UnifiedReport instance ready for markdown generation
        """
        self.logger.info("[generate_unified_report] Creating UnifiedReport entity")

        report = UnifiedReport(
            username=username,
            timestamp=datetime.utcnow(),
            repositories=repository_analyses,
            available_svgs=available_svgs,
            total_api_calls=github_data.api_call_count,
            total_ai_tokens=sum(
                a.summary.tokens_used if a.summary else 0
                for a in repository_analyses
            ),
            ai_model="claude-3-5-haiku-20241022",  # TODO: Get from summarizer config
        )

        # Validate report structure
        validation_errors = report.validate()
        if validation_errors:
            self.logger.warn(
                f"Report validation warnings: {', '.join(validation_errors)}"
            )
            self.warnings.extend(validation_errors)

        return report
