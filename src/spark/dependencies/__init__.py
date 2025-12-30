"""Dependency analysis modules for technology stack currency assessment.

This package provides:
- DependencyParser: Parse dependency files (package.json, requirements.txt, etc.)
- VersionChecker: Check latest versions from package registries
- RepositoryDependencyAnalyzer: Analyze repository dependencies for currency
"""

from spark.dependencies.parser import DependencyParser
from spark.dependencies.version_checker import VersionChecker
from spark.dependencies.analyzer import RepositoryDependencyAnalyzer

__all__ = ["DependencyParser", "VersionChecker", "RepositoryDependencyAnalyzer"]
