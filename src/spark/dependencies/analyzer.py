"""Repository dependency analyzer for technology stack identification."""

import logging
from typing import Dict, List, Optional
from dataclasses import dataclass

from .parser import DependencyParser, Dependency


@dataclass
class DependencyStatus:
    """Status of a single dependency."""
    name: str
    current_version: str
    ecosystem: str


@dataclass
class RepositoryDependencyReport:
    """Dependency analysis report for a repository."""
    total_dependencies: int
    ecosystems: List[str]
    details: List[DependencyStatus]


class RepositoryDependencyAnalyzer:
    """Analyze repository dependencies for technology stack identification."""

    def __init__(self, config: Optional[Dict] = None):
        """Initialize analyzer.

        Args:
            config: Configuration dictionary with analyzer settings
        """
        self.parser = DependencyParser()
        self.logger = logging.getLogger(__name__)
        self.config = config or {}

    def analyze_repository(self, dependency_files: Dict[str, str]) -> RepositoryDependencyReport:
        """Parse dependencies from repository files.

        Args:
            dependency_files: Dict mapping filename to file content

        Returns:
            RepositoryDependencyReport with parsed dependencies
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
                ecosystems=[],
                details=[]
            )

        # Convert to status objects
        statuses = []
        for dep in all_dependencies:
            status = DependencyStatus(
                name=dep.name,
                current_version=dep.version_constraint,
                ecosystem=dep.ecosystem
            )
            statuses.append(status)

        return RepositoryDependencyReport(
            total_dependencies=len(all_dependencies),
            ecosystems=sorted(list(ecosystems)),
            details=statuses
        )

    def get_dependency_summary(self, report: RepositoryDependencyReport) -> str:
        """Generate human-readable summary of dependencies.

        Args:
            report: Dependency report

        Returns:
            Formatted summary string
        """
        if report.total_dependencies == 0:
            return "No dependencies found"

        lines = []
        lines.append(f"Total Dependencies: {report.total_dependencies}")
        lines.append(f"Ecosystems: {', '.join(report.ecosystems)}")

        # Group by ecosystem
        by_ecosystem = {}
        for dep in report.details:
            if dep.ecosystem not in by_ecosystem:
                by_ecosystem[dep.ecosystem] = []
            by_ecosystem[dep.ecosystem].append(dep)

        for ecosystem, deps in sorted(by_ecosystem.items()):
            lines.append(f"\n{ecosystem.upper()} ({len(deps)}):")
            for dep in sorted(deps, key=lambda x: x.name):
                lines.append(f"  - {dep.name} ({dep.current_version})")

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
                latest_version=None,
                ecosystem=dep_status.ecosystem,
                versions_behind=0,
                is_outdated=False,
                status='unknown'
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
