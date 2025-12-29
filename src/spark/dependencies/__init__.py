"""Dependency analysis modules for technology stack currency assessment.

This package provides:
- DependencyParser: Parse dependency files (package.json, requirements.txt, etc.)
- VersionChecker: Check latest versions from package registries
- DependencyAnalyzer: Analyze repository dependencies for currency
"""

from spark.dependencies.parser import DependencyParser
from spark.dependencies.version_checker import VersionChecker
from spark.dependencies.analyzer import DependencyAnalyzer

__all__ = ["DependencyParser", "VersionChecker", "DependencyAnalyzer"]
