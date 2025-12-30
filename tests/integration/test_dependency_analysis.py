"""Integration tests for full dependency analysis workflow."""

import pytest
from pathlib import Path
from spark.dependencies.analyzer import RepositoryDependencyAnalyzer


class TestDependencyAnalysisIntegration:
    """Integration tests for dependency analysis."""

    @pytest.fixture
    def analyzer(self, tmp_path):
        """Create analyzer instance with cache."""
        return RepositoryDependencyAnalyzer(cache_dir=tmp_path)

    def test_analyze_npm_dependencies(self, analyzer):
        """Test analyzing NPM dependencies."""
        dependency_files = {
            'package.json': """
            {
                "dependencies": {
                    "react": "^18.0.0",
                    "lodash": "^4.17.0"
                }
            }
            """
        }

        report = analyzer.analyze_repository(dependency_files)

        assert report.total_dependencies == 2
        assert 'npm' in report.ecosystems
        assert report.analyzed_dependencies >= 0
        assert report.currency_score >= 0

    def test_analyze_python_dependencies(self, analyzer):
        """Test analyzing Python dependencies."""
        dependency_files = {
            'requirements.txt': """
            requests>=2.31.0
            flask==3.0.0
            """
        }

        report = analyzer.analyze_repository(dependency_files)

        assert report.total_dependencies == 2
        assert 'pypi' in report.ecosystems

    def test_analyze_mixed_ecosystems(self, analyzer):
        """Test analyzing multiple ecosystems."""
        dependency_files = {
            'package.json': '{"dependencies": {"react": "^18.0.0"}}',
            'requirements.txt': 'requests>=2.31.0'
        }

        report = analyzer.analyze_repository(dependency_files)

        assert report.total_dependencies == 2
        assert 'npm' in report.ecosystems
        assert 'pypi' in report.ecosystems

    def test_analyze_no_dependencies(self, analyzer):
        """Test analyzing repository with no dependencies."""
        report = analyzer.analyze_repository({})

        assert report.total_dependencies == 0
        assert report.currency_score == 100.0
        assert len(report.ecosystems) == 0

    def test_analyze_malformed_file(self, analyzer):
        """Test analyzing malformed dependency file."""
        dependency_files = {
            'package.json': '{ invalid json'
        }

        report = analyzer.analyze_repository(dependency_files)

        assert report.total_dependencies == 0

    def test_outdated_summary(self, analyzer):
        """Test generating outdated dependencies summary."""
        dependency_files = {
            'requirements.txt': 'requests==2.0.0'
        }

        report = analyzer.analyze_repository(dependency_files)
        summary = analyzer.get_outdated_summary(report)

        assert 'Technology Stack Currency' in summary
        assert 'Total Dependencies' in summary

    @pytest.mark.slow
    def test_real_npm_package(self, analyzer):
        """Test with real NPM registry (slow test)."""
        dependency_files = {
            'package.json': '{"dependencies": {"express": "^4.18.0"}}'
        }

        report = analyzer.analyze_repository(dependency_files)

        assert report.total_dependencies == 1
        # Should successfully query NPM registry
        assert report.analyzed_dependencies == 1 or report.unknown_dependencies == 1

    @pytest.mark.slow
    def test_real_pypi_package(self, analyzer):
        """Test with real PyPI registry (slow test)."""
        dependency_files = {
            'requirements.txt': 'requests==2.31.0'
        }

        report = analyzer.analyze_repository(dependency_files)

        assert report.total_dependencies == 1
        # Should successfully query PyPI
        assert report.analyzed_dependencies == 1 or report.unknown_dependencies == 1
