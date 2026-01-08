"""Dependency analysis module for repository technology stacks.

This module provides:
- DependencyParser: Extract dependencies from various package managers
- RepositoryDependencyAnalyzer: Dependency parsing and ecosystem identification
"""

from spark.dependencies.parser import DependencyParser
from spark.dependencies.analyzer import RepositoryDependencyAnalyzer

__all__ = ["DependencyParser", "RepositoryDependencyAnalyzer"]
