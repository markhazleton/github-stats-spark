"""Integration tests for dependency parsing workflow."""

import pytest
from spark.dependencies.analyzer import RepositoryDependencyAnalyzer


class TestDependencyAnalysisIntegration:
    """Integration tests for dependency parsing."""

    @pytest.fixture
    def analyzer(self):
        """Create analyzer instance."""
        return RepositoryDependencyAnalyzer()

    def test_analyze_npm_dependencies(self, analyzer):
        """Test parsing NPM dependencies."""
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

    def test_analyze_python_dependencies(self, analyzer):
        """Test parsing Python dependencies."""
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
        """Test parsing multiple ecosystems."""
        dependency_files = {
            'package.json': '{"dependencies": {"react": "^18.0.0"}}',
            'requirements.txt': 'requests>=2.31.0'
        }

        report = analyzer.analyze_repository(dependency_files)

        assert report.total_dependencies == 2
        assert 'npm' in report.ecosystems
        assert 'pypi' in report.ecosystems

    def test_analyze_no_dependencies(self, analyzer):
        """Test parsing repository with no dependencies."""
        report = analyzer.analyze_repository({})

        assert report.total_dependencies == 0
        assert len(report.ecosystems) == 0

    def test_analyze_malformed_file(self, analyzer):
        """Test parsing malformed dependency file."""
        dependency_files = {
            'package.json': '{ invalid json'
        }

        report = analyzer.analyze_repository(dependency_files)

        assert report.total_dependencies == 0

    def test_dependency_summary(self, analyzer):
        """Test generating dependency summary."""
        dependency_files = {
            'requirements.txt': 'requests==2.0.0\nflask==3.0.0'
        }

        report = analyzer.analyze_repository(dependency_files)
        summary = analyzer.get_dependency_summary(report)

        assert 'Total Dependencies' in summary
        assert 'pypi' in summary.lower()

    # REMOVED: test_real_npm_package - Version checking removed (out of scope)
    # REMOVED: test_real_pypi_package - Version checking removed (out of scope)
