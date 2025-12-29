"""Markdown report generator for repository analysis."""

from datetime import datetime
from typing import List, Optional
from spark.models.report import Report, RepositoryAnalysis
from spark.logger import get_logger


class ReportGenerator:
    """Generates markdown reports from analysis data."""

    def __init__(self):
        """Initialize report generator."""
        self.logger = get_logger()

    def generate_report(self, report: Report, output_path: str) -> None:
        """Generate and save markdown report.

        Args:
            report: Report object with all analysis data
            output_path: File path to save report
        """
        self.logger.info(f"Generating report for {report.username}")

        markdown = self._build_markdown(report)

        # Write to file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        self.logger.info(f"Report saved to {output_path}")

    def _build_markdown(self, report: Report) -> str:
        """Build complete markdown document.

        Args:
            report: Report object

        Returns:
            Markdown string
        """
        sections = []

        # Header
        sections.append(self._generate_header(report))

        # User profile
        if report.user_profile:
            sections.append(self._generate_profile_section(report))

        # Repository listings
        sections.append(self._generate_repositories_section(report))

        # Metadata
        sections.append(self._generate_metadata_section(report))

        # Errors (if any)
        if report.errors:
            sections.append(self._generate_errors_section(report))

        return "\n\n".join(sections)

    def _generate_header(self, report: Report) -> str:
        """Generate report header.

        Args:
            report: Report object

        Returns:
            Markdown header
        """
        return f"""# GitHub Repository Analysis: {report.username}

**Generated**: {report.generation_timestamp.strftime('%Y-%m-%d %H:%M:%S UTC')}
**Repositories Analyzed**: {report.total_repositories_analyzed}
**AI Summary Rate**: {report.ai_summary_rate:.1f}%

---"""

    def _generate_profile_section(self, report: Report) -> str:
        """Generate user profile section.

        Args:
            report: Report object

        Returns:
            Markdown profile section
        """
        profile = report.user_profile
        lines = ["## Developer Profile", ""]

        lines.append(f"**Username**: {profile.username}")
        lines.append(f"**Total Public Repositories**: {profile.total_repos}")
        lines.append(f"**Active Repositories (90d)**: {profile.active_repos}")
        lines.append(f"**Technology Diversity**: {profile.tech_diversity}/100")
        lines.append(f"**Contribution Style**: {profile.contribution_classification.replace('_', ' ').title()}")
        lines.append("")

        # Top languages
        if profile.top_languages:
            lines.append("### Primary Technologies")
            for lang in profile.top_languages[:5]:
                percentage = (profile.primary_languages[lang] / sum(profile.primary_languages.values()) * 100)
                lines.append(f"- **{lang}**: {percentage:.1f}% of codebase")
            lines.append("")

        # Activity patterns
        if profile.activity_patterns:
            lines.append("### Observable Patterns")
            for pattern in profile.activity_patterns:
                lines.append(f"- {pattern.description}")
            lines.append("")

        # Overall impression
        if profile.overall_impression:
            lines.append("### Overall Impression")
            lines.append(profile.overall_impression)
            lines.append("")

        return "\n".join(lines)

    def _generate_repositories_section(self, report: Report) -> str:
        """Generate repositories listing section.

        Args:
            report: Report object

        Returns:
            Markdown repositories section
        """
        lines = [f"## Top {len(report.repositories)} Repositories", ""]

        for analysis in report.repositories:
            lines.append(self._format_repository_entry(analysis))
            lines.append("")

        return "\n".join(lines)

    def _format_repository_entry(self, analysis: RepositoryAnalysis) -> str:
        """Format single repository entry.

        Args:
            analysis: RepositoryAnalysis object

        Returns:
            Markdown entry
        """
        repo = analysis.repository
        lines = []

        # Title with rank
        lines.append(f"### #{analysis.rank}. [{repo.name}]({repo.url})")
        lines.append("")

        # Stats line
        stats = [
            f"⭐ {repo.stars}",
            f"🔱 {repo.forks}",
            f"📝 {repo.primary_language or 'Unknown'}",
        ]
        if analysis.commit_history:
            stats.append(f"📊 {analysis.commit_history.recent_90d} commits (90d)")
        lines.append(" | ".join(stats))
        lines.append("")

        # Summary
        if analysis.summary:
            lines.append(analysis.summary.summary)
            lines.append("")

        # Tech stack (if available)
        if analysis.tech_stack and analysis.tech_stack.dependencies:
            lines.append(f"**Dependencies**: {analysis.tech_stack.total_dependencies} packages")
            if analysis.tech_stack.outdated_count > 0:
                lines.append(f"⚠️ {analysis.tech_stack.outdated_count} outdated")
            lines.append("")

        # Metadata
        lines.append(f"**Created**: {repo.created_at.strftime('%Y-%m-%d')}")
        if repo.is_archived:
            lines.append("⚠️ **Archived**")
        if repo.is_fork:
            lines.append("🔀 **Fork**")

        return "\n".join(lines)

    def _generate_metadata_section(self, report: Report) -> str:
        """Generate metadata section.

        Args:
            report: Report object

        Returns:
            Markdown metadata
        """
        lines = ["## Report Metadata", ""]
        lines.append(f"- **Generation Time**: {report.generation_time_seconds:.1f} seconds")
        lines.append(f"- **Total API Calls**: {report.total_api_calls}")
        lines.append(f"- **Total AI Tokens**: {report.total_ai_tokens}")
        lines.append(f"- **Success Rate**: {report.success_rate:.1f}%")
        lines.append("")
        lines.append("*Generated by [Stats Spark](https://github.com/markhazleton/github-stats-spark)*")
        return "\n".join(lines)

    def _generate_errors_section(self, report: Report) -> str:
        """Generate errors section.

        Args:
            report: Report object

        Returns:
            Markdown errors section
        """
        lines = ["## ⚠️ Errors Encountered", ""]
        for error in report.errors:
            lines.append(f"- {error}")
        return "\n".join(lines)
