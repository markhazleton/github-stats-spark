"""Version checking against package registries with hybrid caching.

Supports:
- NPM (registry.npmjs.org)
- PyPI (pypi.org)
- RubyGems (rubygems.org)
- Go Modules (proxy.golang.org)
- NuGet (api.nuget.org) - .NET packages
"""

import json
import logging
import time
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Optional
import requests
from packaging.version import Version, InvalidVersion

logger = logging.getLogger(__name__)


class RegistryClient(ABC):
    """Base class for package registry clients."""

    def __init__(self, cache_ttl: int = 7 * 24 * 3600):
        """Initialize registry client.

        Args:
            cache_ttl: Cache time-to-live in seconds (default: 7 days)
        """
        self.cache_ttl = cache_ttl
        self.memory_cache: Dict[str, tuple] = {}
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'GitHub-Stats-Spark/1.0'
        })
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def get_latest_version(self, package_name: str) -> Optional[str]:
        """Get latest version from registry.

        Args:
            package_name: Name of the package

        Returns:
            Latest version string or None if not found
        """
        pass

    def _get_from_memory_cache(self, key: str) -> Optional[str]:
        """Get value from in-memory cache."""
        if key in self.memory_cache:
            version, timestamp = self.memory_cache[key]
            if time.time() - timestamp < self.cache_ttl:
                return version
            else:
                del self.memory_cache[key]
        return None

    def _set_memory_cache(self, key: str, value: str):
        """Set value in in-memory cache."""
        self.memory_cache[key] = (value, time.time())


class NPMRegistryClient(RegistryClient):
    """NPM registry client (registry.npmjs.org)."""

    BASE_URL = 'https://registry.npmjs.org'

    def get_latest_version(self, package_name: str) -> Optional[str]:
        """Get latest NPM package version."""
        # Check memory cache
        cached = self._get_from_memory_cache(f"npm:{package_name}")
        if cached:
            return cached

        try:
            url = f"{self.BASE_URL}/{package_name}"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                latest_version = data.get('dist-tags', {}).get('latest')

                if latest_version:
                    self._set_memory_cache(f"npm:{package_name}", latest_version)
                    return latest_version
            elif response.status_code == 404:
                self.logger.debug(f"NPM package not found: {package_name}")
            else:
                self.logger.warning(f"NPM registry error for {package_name}: {response.status_code}")

        except requests.RequestException as e:
            self.logger.error(f"NPM registry request failed for {package_name}: {e}")

        return None


class PyPIRegistryClient(RegistryClient):
    """PyPI registry client (pypi.org)."""

    BASE_URL = 'https://pypi.org/pypi'

    def get_latest_version(self, package_name: str) -> Optional[str]:
        """Get latest PyPI package version."""
        # Check memory cache
        cached = self._get_from_memory_cache(f"pypi:{package_name}")
        if cached:
            return cached

        try:
            url = f"{self.BASE_URL}/{package_name}/json"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                latest_version = data.get('info', {}).get('version')

                if latest_version:
                    self._set_memory_cache(f"pypi:{package_name}", latest_version)
                    return latest_version
            elif response.status_code == 404:
                self.logger.debug(f"PyPI package not found: {package_name}")
            else:
                self.logger.warning(f"PyPI registry error for {package_name}: {response.status_code}")

        except requests.RequestException as e:
            self.logger.error(f"PyPI registry request failed for {package_name}: {e}")

        return None


class RubyGemsRegistryClient(RegistryClient):
    """RubyGems registry client (rubygems.org)."""

    BASE_URL = 'https://rubygems.org/api/v1'

    def get_latest_version(self, package_name: str) -> Optional[str]:
        """Get latest RubyGems package version."""
        # Check memory cache
        cached = self._get_from_memory_cache(f"rubygems:{package_name}")
        if cached:
            return cached

        try:
            url = f"{self.BASE_URL}/gems/{package_name}.json"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                latest_version = data.get('version')

                if latest_version:
                    self._set_memory_cache(f"rubygems:{package_name}", latest_version)
                    return latest_version
            elif response.status_code == 404:
                self.logger.debug(f"RubyGems package not found: {package_name}")
            else:
                self.logger.warning(f"RubyGems registry error for {package_name}: {response.status_code}")

        except requests.RequestException as e:
            self.logger.error(f"RubyGems registry request failed for {package_name}: {e}")

        return None


class GoProxyClient(RegistryClient):
    """Go Proxy client (proxy.golang.org)."""

    BASE_URL = 'https://proxy.golang.org'

    def get_latest_version(self, package_name: str) -> Optional[str]:
        """Get latest Go module version."""
        # Check memory cache
        cached = self._get_from_memory_cache(f"go:{package_name}")
        if cached:
            return cached

        try:
            url = f"{self.BASE_URL}/{package_name}/@latest"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                latest_version = data.get('Version', '').lstrip('v')

                if latest_version:
                    self._set_memory_cache(f"go:{package_name}", latest_version)
                    return latest_version
            elif response.status_code == 404:
                self.logger.debug(f"Go module not found: {package_name}")
            else:
                self.logger.warning(f"Go proxy error for {package_name}: {response.status_code}")

        except requests.RequestException as e:
            self.logger.error(f"Go proxy request failed for {package_name}: {e}")

        return None


class NuGetRegistryClient(RegistryClient):
    """NuGet registry client (api.nuget.org).

    NuGet is the package manager for .NET. This client queries the official
    NuGet API v3 to get the latest version of packages.
    """

    BASE_URL = 'https://api.nuget.org/v3-flatcontainer'

    def get_latest_version(self, package_name: str) -> Optional[str]:
        """Get latest NuGet package version.

        Args:
            package_name: Name of the NuGet package (case-insensitive)

        Returns:
            Latest version string or None if not found
        """
        # Skip .NET SDK version checks - these aren't packages
        if package_name == '.NET SDK':
            # .NET SDK versions are not queryable from NuGet
            # The version is already from the project file
            return None

        # Check memory cache
        cached = self._get_from_memory_cache(f"nuget:{package_name}")
        if cached:
            return cached

        try:
            # NuGet API is case-insensitive but package IDs are lowercased in URLs
            package_id_lower = package_name.lower()

            # Get list of all versions for the package
            url = f"{self.BASE_URL}/{package_id_lower}/index.json"
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                versions = data.get('versions', [])

                if versions:
                    # Get the last version in the list (latest)
                    # Filter out prerelease versions (those with - in version)
                    stable_versions = [v for v in versions if '-' not in v]

                    if stable_versions:
                        latest_version = stable_versions[-1]
                    else:
                        # If no stable versions, use latest prerelease
                        latest_version = versions[-1]

                    self._set_memory_cache(f"nuget:{package_name}", latest_version)
                    return latest_version
            elif response.status_code == 404:
                self.logger.debug(f"NuGet package not found: {package_name}")
            else:
                self.logger.warning(f"NuGet registry error for {package_name}: {response.status_code}")

        except requests.RequestException as e:
            self.logger.error(f"NuGet registry request failed for {package_name}: {e}")
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            self.logger.error(f"NuGet response parsing failed for {package_name}: {e}")

        return None


class VersionChecker:
    """Check package versions against registries."""

    def __init__(self, cache_dir: Optional[Path] = None, cache_ttl: int = 7 * 24 * 3600):
        """Initialize version checker.

        Args:
            cache_dir: Directory for file-based cache (optional)
            cache_ttl: Cache time-to-live in seconds (default: 7 days)
        """
        self.cache_dir = cache_dir
        self.cache_ttl = cache_ttl

        # Initialize registry clients
        self.clients = {
            'npm': NPMRegistryClient(cache_ttl),
            'pypi': PyPIRegistryClient(cache_ttl),
            'rubygems': RubyGemsRegistryClient(cache_ttl),
            'go': GoProxyClient(cache_ttl),
            'nuget': NuGetRegistryClient(cache_ttl)
        }

        self.logger = logging.getLogger(__name__)

    def get_latest_version(self, package_name: str, ecosystem: str) -> Optional[str]:
        """Get latest version for a package.

        Args:
            package_name: Name of the package
            ecosystem: Package ecosystem (npm, pypi, rubygems, go)

        Returns:
            Latest version string or None
        """
        if ecosystem not in self.clients:
            self.logger.warning(f"Unsupported ecosystem: {ecosystem}")
            return None

        # Try file cache first
        if self.cache_dir:
            cached_version = self._get_from_file_cache(package_name, ecosystem)
            if cached_version:
                return cached_version

        # Fetch from registry
        client = self.clients[ecosystem]
        latest_version = client.get_latest_version(package_name)

        # Save to file cache
        if latest_version and self.cache_dir:
            self._set_file_cache(package_name, ecosystem, latest_version)

        return latest_version

    def compare_versions(self, current: str, latest: str) -> Optional[int]:
        """Compare versions and calculate major versions behind.

        Args:
            current: Current version string
            latest: Latest version string

        Returns:
            Number of major versions behind, or None if comparison fails
        """
        try:
            current_ver = Version(self._clean_version(current))
            latest_ver = Version(self._clean_version(latest))

            return max(0, latest_ver.major - current_ver.major)
        except InvalidVersion as e:
            self.logger.debug(f"Invalid version comparison: {current} vs {latest}: {e}")
            return None

    def _clean_version(self, version: str) -> str:
        """Clean version string for comparison."""
        # Remove common prefixes
        cleaned = version.lstrip('v').strip()
        # Remove build metadata
        if '+' in cleaned:
            cleaned = cleaned.split('+')[0]
        return cleaned

    def _get_from_file_cache(self, package_name: str, ecosystem: str) -> Optional[str]:
        """Get version from file cache."""
        cache_file = self.cache_dir / f"{ecosystem}_{package_name}.json"

        if cache_file.exists():
            try:
                with open(cache_file, 'r') as f:
                    data = json.load(f)

                timestamp = datetime.fromisoformat(data['timestamp'])
                if datetime.now() - timestamp < timedelta(seconds=self.cache_ttl):
                    return data['version']
            except Exception as e:
                self.logger.debug(f"Failed to read cache file {cache_file}: {e}")

        return None

    def _set_file_cache(self, package_name: str, ecosystem: str, version: str):
        """Set version in file cache."""
        try:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            cache_file = self.cache_dir / f"{ecosystem}_{package_name}.json"

            data = {
                'package': package_name,
                'ecosystem': ecosystem,
                'version': version,
                'timestamp': datetime.now().isoformat()
            }

            with open(cache_file, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            self.logger.debug(f"Failed to write cache file: {e}")
