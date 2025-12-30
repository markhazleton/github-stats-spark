"""Data models for GitHub repository analysis.

This module contains entity classes for repository analysis, including:
- Repository: Core repository metadata and statistics
- CommitHistory: Commit patterns and temporal data
- TechnologyStack: Language and dependency information
- RepositorySummary: AI-generated and fallback summaries
- UserProfile: Overall developer profile analysis
- Report: Complete analysis report structure
- UnifiedReport: Unified markdown report combining SVGs and analysis
- GitHubData: Intermediate GitHub API data container
"""

from spark.models.repository import Repository
from spark.models.commit import CommitHistory
from spark.models.tech_stack import TechnologyStack
from spark.models.summary import RepositorySummary
from spark.models.profile import UserProfile
from spark.models.report import Report, RepositoryAnalysis, UnifiedReport
from spark.models.github_data import GitHubData

__all__ = [
    "Repository",
    "CommitHistory",
    "TechnologyStack",
    "RepositorySummary",
    "UserProfile",
    "Report",
    "RepositoryAnalysis",
    "UnifiedReport",
    "GitHubData",
]
