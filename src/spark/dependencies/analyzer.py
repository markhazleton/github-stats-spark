"""Repository dependency analyzer for technology stack currency assessment."""

import logging
from typing import Dict, List, Optional
from dataclasses import dataclass
from pathlib import Path

from .parser import DependencyParser, Dependency
from .version_checker import VersionChecker


@dataclass
class DependencyStatus:
    """Status of a single dependency."""
    name: str
    current_version: str
    latest_version: Optional[str]
    versions_behind: Optional[int]
    ecosystem: str
    is_current: bool
    status: str  # 'current', 'outdated', 'unknown'


@dataclass
class RepositoryDependencyReport:
    """Dependency analysis report for a repository."""
    total_dependencies: int
    analyzed_dependencies: int
    current_dependencies: int
    outdated_dependencies: int
    unknown_dependencies: int
    ecosystems: List[str]
    currency_score: float  # 0-100
    details: List[DependencyStatus]


class RepositoryDependencyAnalyzer:
    """Analyze repository dependencies for technology stack currency."""

    def __init__(self, cache=None, config: Optional[Dict] = None):
        """Initialize analyzer.

        Args:
            cache: APICache instance for version caching
            config: Configuration dictionary with analyzer settings
        """
        self.parser = DependencyParser()
        cache_dir = Path(".cache/dependencies") if cache else None
        self.version_checker = VersionChecker(cache_dir)
        self.logger = logging.getLogger(__name__)
        self.config = config or {}

    def analyze_repository(self, dependency_files: Dict[str, str]) -> RepositoryDependencyReport:
        """Analyze dependencies from repository files.

        Args:
            dependency_files: Dict mapping filename to file content

        Returns:
            RepositoryDependencyReport with analysis results
        """
        all_dependencies: List[Dependency] = []
        ecosystems = set()

        # Parse all dependency files
        for filename, content in dependency_files.items():
            deps = self.parser.parse_file(filename, content)
            all_dependencies.extend(deps)
            ecosystems.update(dep.ecosystem for dep in deps)

        if not all_dependencies:
            return RepositoryDependencyReport(
                total_dependencies=0,
                analyzed_dependencies=0,
                current_dependencies=0,
                outdated_dependencies=0,
                unknown_dependencies=0,
                ecosystems=[],
                currency_score=100.0,  # No deps = up to date
                details=[]
            )

        # Analyze each dependency
        statuses = []
        current_count = 0
        outdated_count = 0
        unknown_count = 0

        for dep in all_dependencies:
            status = self._analyze_dependency(dep)
            statuses.append(status)

            if status.status == 'current':
                current_count += 1
            elif status.status == 'outdated':
                outdated_count += 1
            else:
                unknown_count += 1

        # Calculate currency score
        analyzed = current_count + outdated_count
        if analyzed > 0:
            currency_score = (current_count / analyzed) * 100
        else:
            currency_score = 0.0

        return RepositoryDependencyReport(
            total_dependencies=len(all_dependencies),
            analyzed_dependencies=analyzed,
            current_dependencies=current_count,
            outdated_dependencies=outdated_count,
            unknown_dependencies=unknown_count,
            ecosystems=sorted(list(ecosystems)),
            currency_score=currency_score,
            details=statuses
        )

    def _analyze_dependency(self, dep: Dependency) -> DependencyStatus:
        """Analyze a single dependency.

        Args:
            dep: Dependency to analyze

        Returns:
            DependencyStatus with analysis results
        """
        # Get latest version from registry
        latest_version = self.version_checker.get_latest_version(dep.name, dep.ecosystem)

        if not latest_version:
            return DependencyStatus(
                name=dep.name,
                current_version=dep.version_constraint,
                latest_version=None,
                versions_behind=None,
                ecosystem=dep.ecosystem,
                is_current=False,
                status='unknown'
            )

        # Compare versions
        if dep.version_constraint == 'latest':
            # No version specified, assume latest
            return DependencyStatus(
                name=dep.name,
                current_version='latest',
                latest_version=latest_version,
                versions_behind=0,
                ecosystem=dep.ecosystem,
                is_current=True,
                status='current'
            )

        versions_behind = self.version_checker.compare_versions(
            dep.version_constraint,
            latest_version
        )

        if versions_behind is None:
            # Version comparison failed
            return DependencyStatus(
                name=dep.name,
                current_version=dep.version_constraint,
                latest_version=latest_version,
                versions_behind=None,
                ecosystem=dep.ecosystem,
                is_current=False,
                status='unknown'
            )

        is_current = versions_behind == 0

        return DependencyStatus(
            name=dep.name,
            current_version=dep.version_constraint,
            latest_version=latest_version,
            versions_behind=versions_behind,
            ecosystem=dep.ecosystem,
            is_current=is_current,
            status='current' if is_current else 'outdated'
        )

    def get_outdated_summary(self, report: RepositoryDependencyReport) -> str:
        """Generate human-readable summary of outdated dependencies.

        Args:
            report: Dependency report

        Returns:
            Formatted summary string
        """
        if report.total_dependencies == 0:
            return "No dependencies found"

        lines = []
        lines.append(f"Technology Stack Currency: {report.currency_score:.1f}%")
        lines.append(f"Total Dependencies: {report.total_dependencies}")
        lines.append(f"Current: {report.current_dependencies}, Outdated: {report.outdated_dependencies}, Unknown: {report.unknown_dependencies}")

        if report.outdated_dependencies > 0:
            lines.append("\nOutdated Dependencies:")

            outdated = [d for d in report.details if d.status == 'outdated']
            for dep in sorted(outdated, key=lambda x: x.versions_behind or 0, reverse=True):
                lines.append(
                    f"  - {dep.name}: {dep.current_version} → {dep.latest_version} "
                    f"({dep.versions_behind} major versions behind)"
                )

        return "\n".join(lines)

    def analyze_github_repository(self, github_repo):
        """Analyze dependencies from a PyGithub repository object.

        Args:
            github_repo: PyGithub Repository instance

        Returns:
            TechnologyStack object with dependency analysis, or None if no dependencies
        """
        from spark.models.tech_stack import TechnologyStack, DependencyInfo

        # Known dependency files to check
        dependency_files_to_check = [
            'package.json',  # NPM
            'requirements.txt',  # PyPI
            'pyproject.toml',  # PyPI (modern)
            'Gemfile',  # RubyGems
            'go.mod',  # Go
            'pom.xml',  # Maven
        ]

        dependency_files = {}

        # Try to fetch each dependency file
        for filename in dependency_files_to_check:
            try:
                file_content = github_repo.get_contents(filename)
                if file_content and hasattr(file_content, 'decoded_content'):
                    content = file_content.decoded_content.decode('utf-8')
                    dependency_files[filename] = content
                    self.logger.debug(f"Found dependency file: {filename}")
            except Exception as e:
                # File doesn't exist or error fetching, skip
                self.logger.debug(f"Skipping {filename}: {e}")
                continue

        # Look for .csproj files (can be anywhere in root directory)
        try:
            contents = github_repo.get_contents("")
            for item in contents:
                if item.name.endswith('.csproj') and item.type == 'file':
                    try:
                        file_content = github_repo.get_contents(item.name)
                        if file_content and hasattr(file_content, 'decoded_content'):
                            content = file_content.decoded_content.decode('utf-8')
                            dependency_files[item.name] = content
                            self.logger.debug(f"Found .NET project file: {item.name}")
                            break  # Only process first .csproj found
                    except Exception as e:
                        self.logger.debug(f"Error reading {item.name}: {e}")
        except Exception as e:
            self.logger.debug(f"Error listing repository contents: {e}")

        if not dependency_files:
            self.logger.debug(f"No dependency files found in {github_repo.name}")
            return None

        # Analyze dependencies
        report = self.analyze_repository(dependency_files)

        if report.total_dependencies == 0:
            return None

        # Convert to TechnologyStack
        dependencies = []
        for dep_status in report.details:
            dep_info = DependencyInfo(
                name=dep_status.name,
                current_version=dep_status.current_version,
                latest_version=dep_status.latest_version,
                ecosystem=dep_status.ecosystem,
                versions_behind=dep_status.versions_behind or 0,
                is_outdated=dep_status.status == 'outdated',
                status='current' if dep_status.is_current else ('major_outdated' if (dep_status.versions_behind or 0) > 0 else 'unknown')
            )
            dependencies.append(dep_info)

        # Get primary dependency file type
        primary_file = list(dependency_files.keys())[0] if dependency_files else None

        tech_stack = TechnologyStack(
            repository_name=github_repo.name,
            dependencies=dependencies,
            dependency_file_type=primary_file,
        )

        return tech_stack
