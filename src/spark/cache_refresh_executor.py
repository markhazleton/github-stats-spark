"""Category-specific cache refresh execution helpers."""

from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, Optional

from github import GithubException

from spark.dependencies.analyzer import RepositoryDependencyAnalyzer
from spark.logger import get_logger
from spark.models.commit import CommitHistory
from spark.models.repository import Repository
from spark.models.tech_stack import DependencyInfo, TechnologyStack
from spark.summarizer import RepositorySummarizer
from spark.time_utils import sanitize_timestamp_for_filename


@dataclass
class RefreshResult:
    """Result of a cache refresh operation."""

    repo_name: str
    category: str
    was_cached: bool
    refreshed: bool
    error: Optional[str] = None


class CacheRefreshExecutor:
    """Executes per-category cache refresh work for a repository."""

    def __init__(self, github_client, cache, summarizer: Optional[RepositorySummarizer] = None, fetcher=None, ai_model: Optional[str] = None):
        self.github = github_client
        self.cache = cache
        self.logger = get_logger()
        self.api_calls = 0
        self.summarizer = summarizer
        self.ai_model = ai_model
        self.dependency_analyzer = RepositoryDependencyAnalyzer()
        self.fetcher = fetcher

    @staticmethod
    def _sanitize_language_stats(language_stats: Any) -> Dict[str, int]:
        """Normalize language payload to numeric byte counts only."""
        if not isinstance(language_stats, dict):
            return {}

        sanitized: Dict[str, int] = {}
        for language, raw_value in language_stats.items():
            try:
                bytes_count = int(raw_value)
            except (TypeError, ValueError):
                continue

            if bytes_count >= 0:
                sanitized[language] = bytes_count

        return sanitized

    def refresh_commit_counts(self, username: str, repo_name: str, pushed_at: datetime) -> RefreshResult:
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "commit_counts"
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached:
            return RefreshResult(repo_name=repo_name, category=category, was_cached=True, refreshed=False)

        try:
            self.api_calls += 1
            repo = self.github.get_repo(f"{username}/{repo_name}")
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
                if total_commits >= 1000:
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
            metadata = {
                "repository": {"owner": username, "name": repo_name},
                "category": category,
                "pushed_at": pushed_at.isoformat(),
                "ttl_enforced": False,
            }
            self.cache.set(category, username, result, repo=repo_name, week=cache_key, metadata=metadata)
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=True)
        except Exception as error:
            self.logger.warning(f"Failed to refresh {category} for {repo_name}: {error}")
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False, error=str(error))

    def refresh_commits_stats(self, username: str, repo_name: str, pushed_at: datetime) -> RefreshResult:
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "commits_stats"
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached is not None:
            return RefreshResult(repo_name=repo_name, category=category, was_cached=True, refreshed=False)

        if self.fetcher is None:
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=False,
                refreshed=False,
                error="Fetcher is required for commit stats refresh",
            )

        try:
            self.fetcher.fetch_commits_with_stats(
                username=username,
                repo_name=repo_name,
                repo_pushed_at=pushed_at,
                force_refresh=True,
            )
            refreshed_cache = self.cache.get(category, username, repo=repo_name, week=cache_key)
            if refreshed_cache is None:
                return RefreshResult(
                    repo_name=repo_name,
                    category=category,
                    was_cached=False,
                    refreshed=False,
                    error="Commit stats were not written to cache",
                )

            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=True)
        except Exception as error:
            self.logger.warning(f"Failed to refresh {category} for {repo_name}: {error}")
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False, error=str(error))

    def refresh_languages(self, username: str, repo_name: str, pushed_at: datetime) -> RefreshResult:
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "languages"
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached:
            return RefreshResult(repo_name=repo_name, category=category, was_cached=True, refreshed=False)

        try:
            self.api_calls += 1
            repo = self.github.get_repo(f"{username}/{repo_name}")
            languages = self._sanitize_language_stats(repo.get_languages())
            metadata = {
                "repository": {"owner": username, "name": repo_name},
                "category": category,
                "pushed_at": pushed_at.isoformat(),
                "ttl_enforced": False,
            }
            self.cache.set(category, username, languages, repo=repo_name, week=cache_key, metadata=metadata)
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=True)
        except Exception as error:
            self.logger.warning(f"Failed to refresh {category} for {repo_name}: {error}")
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False, error=str(error))

    def refresh_contributor_stats(self, username: str, repo_name: str, pushed_at: datetime) -> RefreshResult:
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "contributor_stats"
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached is not None:
            return RefreshResult(repo_name=repo_name, category=category, was_cached=True, refreshed=False)

        if self.fetcher is None:
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=False,
                refreshed=False,
                error="Fetcher is required for contributor stats refresh",
            )

        try:
            result = self.fetcher.fetch_contributor_stats(
                username=username,
                repo_name=repo_name,
                repo_pushed_at=pushed_at,
            )
            if result is None:
                return RefreshResult(
                    repo_name=repo_name,
                    category=category,
                    was_cached=False,
                    refreshed=False,
                    error="Contributor stats unavailable",
                )

            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=True)
        except Exception as error:
            self.logger.warning(f"Failed to refresh {category} for {repo_name}: {error}")
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False, error=str(error))

    def refresh_code_frequency(self, username: str, repo_name: str, pushed_at: datetime) -> RefreshResult:
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "code_frequency"
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached is not None:
            return RefreshResult(repo_name=repo_name, category=category, was_cached=True, refreshed=False)

        if self.fetcher is None:
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=False,
                refreshed=False,
                error="Fetcher is required for code frequency refresh",
            )

        try:
            result = self.fetcher.fetch_code_frequency(
                username=username,
                repo_name=repo_name,
                repo_pushed_at=pushed_at,
            )
            if result is None:
                return RefreshResult(
                    repo_name=repo_name,
                    category=category,
                    was_cached=False,
                    refreshed=False,
                    error="Code frequency unavailable",
                )

            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=True)
        except Exception as error:
            self.logger.warning(f"Failed to refresh {category} for {repo_name}: {error}")
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False, error=str(error))

    def refresh_readme(self, username: str, repo_name: str, pushed_at: datetime) -> RefreshResult:
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "readme"
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached is not None:
            return RefreshResult(repo_name=repo_name, category=category, was_cached=True, refreshed=False)

        try:
            self.api_calls += 1
            repo = self.github.get_repo(f"{username}/{repo_name}")
            content = ""
            try:
                readme = repo.get_readme()
                content = readme.decoded_content.decode("utf-8")
            except GithubException as error:
                if getattr(error, "status", None) != 404:
                    raise

            metadata = {
                "repository": {"owner": username, "name": repo_name},
                "category": category,
                "pushed_at": pushed_at.isoformat(),
                "ttl_enforced": False,
            }
            self.cache.set(category, username, content, repo=repo_name, week=cache_key, metadata=metadata)
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=True)
        except Exception as error:
            self.logger.warning(f"Failed to refresh {category} for {repo_name}: {error}")
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False, error=str(error))

    def refresh_quality_indicators(self, username: str, repo_name: str, pushed_at: datetime) -> RefreshResult:
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "quality_indicators"
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached is not None:
            return RefreshResult(repo_name=repo_name, category=category, was_cached=True, refreshed=False)

        try:
            self.api_calls += 1
            repo = self.github.get_repo(f"{username}/{repo_name}")

            has_license = False
            try:
                repo.get_license()
                has_license = True
            except GithubException as error:
                if getattr(error, "status", None) != 404:
                    raise

            has_ci_cd = False
            try:
                workflows = repo.get_workflows()
                has_ci_cd = workflows.totalCount > 0
            except GithubException:
                pass

            has_tests = False
            has_docs = False
            test_dirs = {"test", "tests", "spec", "specs", "__tests__"}
            doc_dirs = {"docs", "doc", "documentation"}
            doc_files = {"contributing.md", "changelog.md"}

            try:
                contents = repo.get_contents("")
                for item in contents:
                    name_lower = item.name.lower()
                    if item.type == "dir":
                        if name_lower in test_dirs:
                            has_tests = True
                        if name_lower in doc_dirs:
                            has_docs = True
                    elif item.type == "file" and name_lower in doc_files:
                        has_docs = True
            except GithubException:
                pass

            quality_data = {
                "has_license": has_license,
                "has_ci_cd": has_ci_cd,
                "has_tests": has_tests,
                "has_docs": has_docs,
            }
            metadata = {
                "repository": {"owner": username, "name": repo_name},
                "category": category,
                "pushed_at": pushed_at.isoformat(),
                "ttl_enforced": False,
            }
            self.cache.set(category, username, quality_data, repo=repo_name, week=cache_key, metadata=metadata)
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=True)
        except Exception as error:
            self.logger.warning(f"Failed to refresh {category} for {repo_name}: {error}")
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False, error=str(error))

    def refresh_dependency_files(self, username: str, repo_name: str, pushed_at: datetime) -> RefreshResult:
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "dependency_files"
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached is not None:
            return RefreshResult(repo_name=repo_name, category=category, was_cached=True, refreshed=False)

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
                                dependency_files[item.name] = item.decoded_content.decode("utf-8")
                    else:
                        file_content = repo.get_contents(filename)
                        dependency_files[filename] = file_content.decoded_content.decode("utf-8")
                except GithubException as error:
                    if getattr(error, "status", None) == 404:
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
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=True)
        except Exception as error:
            self.logger.warning(f"Failed to refresh {category} for {repo_name}: {error}")
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False, error=str(error))

    def refresh_ai_summary(self, username: str, repo_data: Dict[str, Any], pushed_at: datetime) -> RefreshResult:
        repo_name = repo_data["name"]
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "ai_summary"
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached:
            return RefreshResult(repo_name=repo_name, category=category, was_cached=True, refreshed=False)

        if self.summarizer is None:
            if self.ai_model is None:
                from spark.exceptions import ConfigurationError
                raise ConfigurationError(
                    "CacheRefreshExecutor requires ai_model for AI summary generation. "
                    "Set analyzer.ai_model in spark.yml.",
                    field="analyzer.ai_model",
                )
            self.summarizer = RepositorySummarizer(cache=self.cache, model=self.ai_model)

        try:
            commit_data = self.cache.get("commit_counts", username, repo=repo_name, week=cache_key)
            if commit_data is None:
                self.refresh_commit_counts(username, repo_name, pushed_at)
                commit_data = self.cache.get("commit_counts", username, repo=repo_name, week=cache_key) or {}

            language_stats = self.cache.get("languages", username, repo=repo_name, week=cache_key)
            if language_stats is None:
                self.refresh_languages(username, repo_name, pushed_at)
                language_stats = self.cache.get("languages", username, repo=repo_name, week=cache_key) or {}
            language_stats = self._sanitize_language_stats(language_stats)

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
                    tech_stack = self.dependency_analyzer.build_technology_stack(
                        repository_name=repo_name,
                        report=dep_report,
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
                self.cache.set(category, username, cache_payload, repo=repo_name, week=cache_key, metadata=metadata)
                return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=True)

            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False)
        except Exception as error:
            self.logger.warning(f"Failed to refresh {category} for {repo_name}: {error}")
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False, error=str(error))

    def refresh_pull_request_summary(self, username: str, repo_name: str, pushed_at: datetime) -> RefreshResult:
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "pull_request_summary"
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached is not None:
            return RefreshResult(repo_name=repo_name, category=category, was_cached=True, refreshed=False)

        if self.fetcher is None:
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=False,
                refreshed=False,
                error="Fetcher is required for pull request enrichment refresh",
            )

        try:
            summary = self.fetcher.fetch_pull_request_summary(
                username=username,
                repo_name=repo_name,
                repo_pushed_at=pushed_at,
                force_refresh=True,
            )
            metadata = {
                "repository": {"owner": username, "name": repo_name},
                "category": category,
                "pushed_at": pushed_at.isoformat(),
                "ttl_enforced": False,
            }
            self.cache.set(category, username, summary, repo=repo_name, week=cache_key, metadata=metadata)
            self.api_calls += 1
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=True)
        except Exception as error:
            self.logger.warning(f"Failed to refresh {category} for {repo_name}: {error}")
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False, error=str(error))

    def refresh_security_summary(self, username: str, repo_name: str, pushed_at: datetime) -> RefreshResult:
        cache_key = sanitize_timestamp_for_filename(pushed_at)
        category = "security_summary"
        cached = self.cache.get(category, username, repo=repo_name, week=cache_key)
        if cached is not None:
            return RefreshResult(repo_name=repo_name, category=category, was_cached=True, refreshed=False)

        if self.fetcher is None:
            return RefreshResult(
                repo_name=repo_name,
                category=category,
                was_cached=False,
                refreshed=False,
                error="Fetcher is required for security enrichment refresh",
            )

        try:
            summary = self.fetcher.fetch_security_summary(
                username=username,
                repo_name=repo_name,
                repo_pushed_at=pushed_at,
                force_refresh=True,
            )
            metadata = {
                "repository": {"owner": username, "name": repo_name},
                "category": category,
                "pushed_at": pushed_at.isoformat(),
                "ttl_enforced": False,
            }
            self.cache.set(category, username, summary, repo=repo_name, week=cache_key, metadata=metadata)
            self.api_calls += 1
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=True)
        except Exception as error:
            self.logger.warning(f"Failed to refresh {category} for {repo_name}: {error}")
            return RefreshResult(repo_name=repo_name, category=category, was_cached=False, refreshed=False, error=str(error))