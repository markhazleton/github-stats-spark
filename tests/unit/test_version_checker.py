"""Unit tests for version checker with mock responses."""

import pytest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
from spark.dependencies.version_checker import (
    VersionChecker,
    NPMRegistryClient,
    PyPIRegistryClient,
    RubyGemsRegistryClient,
    GoProxyClient
)


class TestNPMRegistryClient:
    """Test cases for NPM registry client."""

    @pytest.fixture
    def client(self):
        """Create NPM client instance."""
        return NPMRegistryClient()

    @patch('requests.Session.get')
    def test_get_latest_version_success(self, mock_get, client):
        """Test successful version retrieval."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'dist-tags': {'latest': '18.2.0'}
        }
        mock_get.return_value = mock_response

        version = client.get_latest_version('react')
        assert version == '18.2.0'

    @patch('requests.Session.get')
    def test_get_latest_version_not_found(self, mock_get, client):
        """Test package not found."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        version = client.get_latest_version('nonexistent-package')
        assert version is None

    @patch('requests.Session.get')
    def test_memory_cache(self, mock_get, client):
        """Test in-memory caching."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'dist-tags': {'latest': '1.0.0'}
        }
        mock_get.return_value = mock_response

        # First call
        version1 = client.get_latest_version('test-package')
        assert version1 == '1.0.0'

        # Second call should use cache
        version2 = client.get_latest_version('test-package')
        assert version2 == '1.0.0'

        # Should only make one API call
        assert mock_get.call_count == 1


class TestPyPIRegistryClient:
    """Test cases for PyPI registry client."""

    @pytest.fixture
    def client(self):
        """Create PyPI client instance."""
        return PyPIRegistryClient()

    @patch('requests.Session.get')
    def test_get_latest_version_success(self, mock_get, client):
        """Test successful version retrieval."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'info': {'version': '2.31.0'}
        }
        mock_get.return_value = mock_response

        version = client.get_latest_version('requests')
        assert version == '2.31.0'


class TestRubyGemsRegistryClient:
    """Test cases for RubyGems registry client."""

    @pytest.fixture
    def client(self):
        """Create RubyGems client instance."""
        return RubyGemsRegistryClient()

    @patch('requests.Session.get')
    def test_get_latest_version_success(self, mock_get, client):
        """Test successful version retrieval."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'version': '7.0.8'
        }
        mock_get.return_value = mock_response

        version = client.get_latest_version('rails')
        assert version == '7.0.8'


class TestGoProxyClient:
    """Test cases for Go Proxy client."""

    @pytest.fixture
    def client(self):
        """Create Go Proxy client instance."""
        return GoProxyClient()

    @patch('requests.Session.get')
    def test_get_latest_version_success(self, mock_get, client):
        """Test successful version retrieval."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'Version': 'v1.9.1'
        }
        mock_get.return_value = mock_response

        version = client.get_latest_version('github.com/gin-gonic/gin')
        assert version == '1.9.1'


class TestVersionChecker:
    """Test cases for VersionChecker."""

    @pytest.fixture
    def checker(self, tmp_path):
        """Create version checker instance."""
        return VersionChecker(cache_dir=tmp_path)

    def test_compare_versions_equal(self, checker):
        """Test version comparison - equal versions."""
        result = checker.compare_versions('1.0.0', '1.0.0')
        assert result == 0

    def test_compare_versions_behind(self, checker):
        """Test version comparison - behind."""
        result = checker.compare_versions('1.0.0', '3.0.0')
        assert result == 2

    def test_compare_versions_ahead(self, checker):
        """Test version comparison - ahead."""
        result = checker.compare_versions('3.0.0', '1.0.0')
        assert result == 0  # max(0, ...)

    def test_compare_versions_with_prefix(self, checker):
        """Test version comparison with v prefix."""
        result = checker.compare_versions('v1.0.0', 'v2.0.0')
        assert result == 1

    def test_clean_version(self, checker):
        """Test version cleaning."""
        assert checker._clean_version('v1.2.3') == '1.2.3'
        assert checker._clean_version('1.2.3+build.123') == '1.2.3'
        assert checker._clean_version('  1.2.3  ') == '1.2.3'

    @patch('spark.dependencies.version_checker.NPMRegistryClient.get_latest_version')
    def test_get_latest_version_npm(self, mock_get, checker):
        """Test getting latest version for NPM."""
        mock_get.return_value = '18.2.0'

        version = checker.get_latest_version('react', 'npm')
        assert version == '18.2.0'

    def test_get_latest_version_unsupported_ecosystem(self, checker):
        """Test unsupported ecosystem."""
        version = checker.get_latest_version('package', 'unknown')
        assert version is None
