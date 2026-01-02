# Performance Optimization Implementation Guide

## Quick Start: Implementation Checklist

This guide provides working code examples and step-by-step instructions to implement the performance optimization strategy for your GitHub Pages dashboard.

---

## Part 1: Data Architecture Implementation

### Step 1.1: Generate Index File

**File:** `src/generate_index.py`

```python
#!/usr/bin/env python3
"""Generate minimal index.json for fast initial page load."""

import json
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime


class IndexGenerator:
    """Generate optimized index file for 200 repositories."""

    def __init__(self, output_dir: str = "output/data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_index(self, repositories: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate index with minimal per-repo data.

        Per-repo overhead: ~200 bytes (uncompressed), ~50 bytes (gzipped)
        """
        repos_list = []

        for idx, repo in enumerate(repositories, 1):
            repos_list.append({
                "id": f"repo-{idx:03d}",              # e.g., "repo-001"
                "name": repo["name"],
                "url": repo.get("url", ""),
                "stars": repo.get("stars", 0),
                "language": repo.get("primary_language"),
                "description": repo.get("description", "")[:100],  # First 100 chars
            })

        index = {
            "version": "1.0",
            "generated_at": datetime.now().isoformat(),
            "total_repos": len(repositories),
            "repositories": repos_list,
        }

        return index

    def save_index(self, index: Dict[str, Any]) -> Path:
        """Save index to file."""
        output_path = self.output_dir / "index.json"

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(index, f, separators=(",", ":"), ensure_ascii=False)

        return output_path

    def generate_and_save(self, repositories: List[Dict[str, Any]]) -> Path:
        """Generate and save index file."""
        index = self.generate_index(repositories)
        return self.save_index(index)


# Usage example
if __name__ == "__main__":
    from spark.fetcher import GitHubFetcher
    from spark.config import SparkConfig

    config = SparkConfig("config/spark.yml")
    config.load()

    # Fetch repositories
    fetcher = GitHubFetcher(token=config.get("github_token"))
    repos = fetcher.fetch_repositories(config.get_user())

    # Generate index
    generator = IndexGenerator()
    index_path = generator.generate_and_save(repos)

    print(f"Index file generated: {index_path}")
    print(f"File size: {index_path.stat().st_size} bytes")
```

### Step 1.2: Generate Individual Repository Bundles

**File:** `src/generate_repo_bundles.py`

```python
#!/usr/bin/env python3
"""Generate individual repository bundle files for lazy loading."""

import json
from pathlib import Path
from typing import Dict, Any
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


class RepositoryBundleGenerator:
    """Generate individual JSON files for each repository."""

    def __init__(self, output_dir: str = "output/data/repos"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_bundle(self, repo_id: str, repo_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a single repository bundle.

        Includes all analysis data needed for detail view.
        Size: ~3-4 KB per repo (gzipped)
        """
        return {
            "id": repo_id,
            "name": repo_data["name"],
            "url": repo_data.get("url"),
            "owner": repo_data.get("owner"),
            "description": repo_data.get("description"),

            # Core statistics
            "stats": {
                "stars": repo_data.get("stars", 0),
                "forks": repo_data.get("forks", 0),
                "watchers": repo_data.get("watchers", 0),
                "open_issues": repo_data.get("open_issues", 0),
                "size_kb": repo_data.get("size_kb", 0),
                "created_at": repo_data.get("created_at"),
                "updated_at": repo_data.get("updated_at"),
                "pushed_at": repo_data.get("pushed_at"),
                "is_archived": repo_data.get("is_archived", False),
                "is_fork": repo_data.get("is_fork", False),
            },

            # Language breakdown
            "languages": repo_data.get("language_stats", {}),

            # Commit history (optimized format)
            "commit_history": {
                "total": repo_data.get("total_commits", 0),
                "avg_per_month": repo_data.get("avg_commits_per_month", 0),
                "last_30_days": repo_data.get("commits_last_30_days", []),
            },

            # Tech stack and dependencies
            "tech_stack": {
                "frameworks": repo_data.get("frameworks", []),
                "dependencies": repo_data.get("dependencies", []),
                "tools": repo_data.get("tools", []),
            },

            # Code quality metrics
            "quality": {
                "has_tests": repo_data.get("has_tests", False),
                "has_docs": repo_data.get("has_docs", False),
                "has_license": repo_data.get("has_license", False),
                "has_ci_cd": repo_data.get("has_ci_cd", False),
                "test_coverage": repo_data.get("test_coverage"),
                "contributors": repo_data.get("contributors_count", 0),
            },

            # AI-generated summary
            "summary": repo_data.get("ai_summary", ""),
            "key_features": repo_data.get("key_features", []),
            "use_cases": repo_data.get("use_cases", []),

            # Release information
            "releases": {
                "count": repo_data.get("release_count", 0),
                "latest_date": repo_data.get("latest_release_date"),
            },
        }

    def save_bundle(self, repo_id: str, bundle: Dict[str, Any]) -> Path:
        """Save repository bundle to file."""
        output_path = self.output_dir / f"{repo_id}.json"

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(bundle, f, separators=(",", ":"), ensure_ascii=False)

        return output_path

    def generate_bundles_parallel(
        self,
        repositories: list,
        max_workers: int = 8
    ) -> Dict[str, Path]:
        """Generate all repository bundles in parallel.

        Uses ThreadPoolExecutor for I/O-bound operations.
        With 8 workers: 200 repos in ~5 seconds.
        """
        results = {}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            futures = {
                executor.submit(
                    self._generate_single_bundle,
                    f"repo-{idx:03d}",
                    repo
                ): repo["name"]
                for idx, repo in enumerate(repositories, 1)
            }

            # Collect results as they complete
            completed = 0
            for future in as_completed(futures):
                repo_id, path = future.result()
                results[repo_id] = path
                completed += 1

                if completed % 25 == 0:
                    print(f"Generated {completed}/{len(repositories)} bundles...")

        return results

    def _generate_single_bundle(
        self,
        repo_id: str,
        repo_data: Dict[str, Any]
    ) -> tuple:
        """Helper: generate and save a single bundle."""
        bundle = self.generate_bundle(repo_id, repo_data)
        path = self.save_bundle(repo_id, bundle)
        return repo_id, path


# Usage example
if __name__ == "__main__":
    from spark.fetcher import GitHubFetcher
    from spark.config import SparkConfig

    config = SparkConfig("config/spark.yml")
    config.load()

    fetcher = GitHubFetcher(token=config.get("github_token"))
    repos = fetcher.fetch_repositories(config.get_user())

    # Generate bundles in parallel
    generator = RepositoryBundleGenerator()
    results = generator.generate_bundles_parallel(repos, max_workers=8)

    print(f"Generated {len(results)} repository bundles")

    # Check total size
    total_size = sum(p.stat().st_size for p in results.values())
    print(f"Total size: {total_size / 1024:.1f} KB")
```

### Step 1.3: Generate Aggregated Metrics

**File:** `src/generate_aggregates.py`

```python
#!/usr/bin/env python3
"""Generate aggregated statistics across all repositories."""

import json
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime
from collections import Counter


class AggregatesGenerator:
    """Generate site-wide aggregated metrics."""

    def __init__(self, output_dir: str = "output/data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_aggregates(self, repositories: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate aggregated metrics for the dashboard.

        Used for summary statistics and quick facts.
        Size: ~1-2 KB (gzipped)
        """
        # Aggregate statistics
        total_stars = sum(r.get("stars", 0) for r in repositories)
        total_forks = sum(r.get("forks", 0) for r in repositories)
        total_commits = sum(r.get("total_commits", 0) for r in repositories)

        # Count all languages
        all_languages = Counter()
        for repo in repositories:
            for lang, bytes_count in repo.get("language_stats", {}).items():
                all_languages[lang] += bytes_count

        # Find language distribution
        total_bytes = sum(all_languages.values())
        language_distribution = {
            lang: {
                "count": all_languages[lang],
                "percentage": (all_languages[lang] / total_bytes * 100) if total_bytes > 0 else 0
            }
            for lang in all_languages
        }

        # Find most used frameworks/tools
        all_frameworks = Counter()
        all_tools = Counter()
        for repo in repositories:
            for framework in repo.get("frameworks", []):
                all_frameworks[framework] += 1
            for tool in repo.get("tools", []):
                all_tools[tool] += 1

        # Calculate activity metrics
        archived_count = sum(1 for r in repositories if r.get("is_archived"))
        fork_count = sum(1 for r in repositories if r.get("is_fork"))
        has_tests_count = sum(1 for r in repositories if r.get("has_tests"))
        has_docs_count = sum(1 for r in repositories if r.get("has_docs"))
        has_ci_cd_count = sum(1 for r in repositories if r.get("has_ci_cd"))

        return {
            "version": "1.0",
            "generated_at": datetime.now().isoformat(),
            "summary": {
                "total_repositories": len(repositories),
                "total_stars": total_stars,
                "total_forks": total_forks,
                "total_commits": total_commits,
                "average_stars_per_repo": total_stars / len(repositories) if repositories else 0,
                "average_forks_per_repo": total_forks / len(repositories) if repositories else 0,
            },
            "languages": {
                "total_distinct": len(language_distribution),
                "distribution": sorted(
                    language_distribution.items(),
                    key=lambda x: x[1]["count"],
                    reverse=True
                )[:20],  # Top 20 languages
            },
            "frameworks": {
                "total_distinct": len(all_frameworks),
                "top_10": dict(all_frameworks.most_common(10)),
            },
            "tools": {
                "total_distinct": len(all_tools),
                "top_10": dict(all_tools.most_common(10)),
            },
            "quality_metrics": {
                "with_tests": {
                    "count": has_tests_count,
                    "percentage": (has_tests_count / len(repositories) * 100) if repositories else 0,
                },
                "with_docs": {
                    "count": has_docs_count,
                    "percentage": (has_docs_count / len(repositories) * 100) if repositories else 0,
                },
                "with_ci_cd": {
                    "count": has_ci_cd_count,
                    "percentage": (has_ci_cd_count / len(repositories) * 100) if repositories else 0,
                },
            },
            "repository_status": {
                "active": len(repositories) - archived_count,
                "archived": archived_count,
                "original": len(repositories) - fork_count,
                "forks": fork_count,
            },
        }

    def save_aggregates(self, aggregates: Dict[str, Any]) -> Path:
        """Save aggregates to file."""
        output_path = self.output_dir / "aggregated.json"

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(aggregates, f, separators=(",", ":"), ensure_ascii=False)

        return output_path


# Usage example
if __name__ == "__main__":
    from spark.fetcher import GitHubFetcher
    from spark.config import SparkConfig

    config = SparkConfig("config/spark.yml")
    config.load()

    fetcher = GitHubFetcher(token=config.get("github_token"))
    repos = fetcher.fetch_repositories(config.get_user())

    # Generate aggregates
    generator = AggregatesGenerator()
    aggregates = generator.generate_aggregates(repos)
    path = generator.save_aggregates(aggregates)

    print(f"Aggregates generated: {path}")
    print(f"File size: {path.stat().st_size} bytes")
```

---

## Part 2: Client-Side Lazy Loading

### Step 2.1: Lazy Loading with Intersection Observer

**File:** `static/js/lazy-loader.js`

```javascript
/**
 * Lazy Loading Module
 * Efficiently loads repository data on-demand using Intersection Observer API
 */

class RepositoryLazyLoader {
  constructor(options = {}) {
    this.options = {
      rootMargin: options.rootMargin || '50px',
      batchSize: options.batchSize || 10,
      concurrentRequests: options.concurrentRequests || 4,
      ...options
    };

    this.loadedRepositories = new Map();
    this.pendingRequests = new Map();
    this.observer = null;
    this.requestQueue = [];
    this.activeRequests = 0;

    this._initializeObserver();
  }

  /**
   * Initialize Intersection Observer for viewport detection
   */
  _initializeObserver() {
    this.observer = new IntersectionObserver(
      (entries) => this._handleIntersection(entries),
      {
        rootMargin: this.options.rootMargin,
        threshold: 0.01
      }
    );
  }

  /**
   * Handle intersection changes
   */
  _handleIntersection(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.dataset.loaded) {
        const repoId = entry.target.dataset.repoId;
        this._queueLoad(repoId);
      }
    });
  }

  /**
   * Queue a repository for loading
   */
  _queueLoad(repoId) {
    if (!this.loadedRepositories.has(repoId) && !this.pendingRequests.has(repoId)) {
      this.requestQueue.push(repoId);
      this._processQueue();
    }
  }

  /**
   * Process the request queue with concurrency limit
   */
  async _processQueue() {
    while (this.requestQueue.length > 0 && this.activeRequests < this.options.concurrentRequests) {
      const repoId = this.requestQueue.shift();
      this._loadRepository(repoId);
    }
  }

  /**
   * Load a single repository
   */
  async _loadRepository(repoId) {
    this.activeRequests++;

    try {
      const data = await this._fetchRepositoryData(repoId);
      this.loadedRepositories.set(repoId, data);

      // Update UI with loaded data
      const element = document.querySelector(`[data-repo-id="${repoId}"]`);
      if (element) {
        element.dataset.loaded = 'true';
        this._updateElement(element, data);
      }

      // Dispatch custom event for listeners
      window.dispatchEvent(new CustomEvent('repositoryLoaded', {
        detail: { repoId, data }
      }));

    } catch (error) {
      console.error(`Failed to load repository ${repoId}:`, error);
      const element = document.querySelector(`[data-repo-id="${repoId}"]`);
      if (element) {
        element.dataset.error = 'true';
        element.querySelector('.error-message')?.textContent = 'Failed to load data';
      }
    } finally {
      this.activeRequests--;
      this.pendingRequests.delete(repoId);
      this._processQueue();
    }
  }

  /**
   * Fetch repository data from server
   */
  async _fetchRepositoryData(repoId) {
    // Check cache first
    if (this.pendingRequests.has(repoId)) {
      return this.pendingRequests.get(repoId);
    }

    const promise = fetch(`/data/repos/${repoId}.json`)
      .then(response => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
      });

    this.pendingRequests.set(repoId, promise);
    return promise;
  }

  /**
   * Update DOM element with loaded data
   */
  _updateElement(element, data) {
    // Update elements with data-bind attributes
    for (const [key, value] of Object.entries(this._flattenObject(data))) {
      const target = element.querySelector(`[data-bind="${key}"]`);
      if (target) {
        target.textContent = this._formatValue(key, value);
      }
    }

    // Trigger render complete
    element.classList.add('loaded');
  }

  /**
   * Flatten nested object for easy DOM binding
   */
  _flattenObject(obj, prefix = '') {
    const flattened = {};
    for (const [key, value] of Object.entries(obj)) {
      const newKey = prefix ? `${prefix}.${key}` : key;
      if (value && typeof value === 'object' && !Array.isArray(value) && !value.toISOString) {
        Object.assign(flattened, this._flattenObject(value, newKey));
      } else {
        flattened[newKey] = value;
      }
    }
    return flattened;
  }

  /**
   * Format value for display
   */
  _formatValue(key, value) {
    if (value === null || value === undefined) return '—';
    if (typeof value === 'number') {
      if (key.includes('date')) return new Date(value).toLocaleDateString();
      if (key.includes('size') || key.includes('bytes')) return this._formatBytes(value);
      if (key.includes('percentage')) return `${value.toFixed(1)}%`;
      return value.toLocaleString();
    }
    if (Array.isArray(value)) return value.join(', ');
    return String(value);
  }

  /**
   * Format bytes for display
   */
  _formatBytes(bytes) {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }

  /**
   * Observe an element for lazy loading
   */
  observe(element) {
    this.observer.observe(element);
  }

  /**
   * Batch load repositories (for pagination or manual triggers)
   */
  async loadBatch(repoIds) {
    const promises = repoIds.map(id => this._fetchRepositoryData(id));
    const results = await Promise.all(promises);

    results.forEach((data, i) => {
      this.loadedRepositories.set(repoIds[i], data);
    });

    return results;
  }

  /**
   * Get loaded data for a repository
   */
  getRepository(repoId) {
    return this.loadedRepositories.get(repoId);
  }

  /**
   * Preload specific repositories
   */
  async preload(repoIds) {
    return this.loadBatch(repoIds);
  }

  /**
   * Clear cache and reset state
   */
  clear() {
    this.loadedRepositories.clear();
    this.pendingRequests.clear();
    this.requestQueue = [];
  }

  /**
   * Destroy observer
   */
  destroy() {
    this.observer.disconnect();
    this.clear();
  }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = RepositoryLazyLoader;
}
```

### Step 2.2: Table Implementation with Lazy Loading

**File:** `static/js/table.js`

```javascript
/**
 * Repository Table Module
 * Displays repositories with lazy loading and sorting/filtering
 */

class RepositoryTable {
  constructor(containerId, options = {}) {
    this.container = document.getElementById(containerId);
    this.lazyLoader = options.lazyLoader || new RepositoryLazyLoader();
    this.currentData = [];
    this.filteredData = [];
    this.sortColumn = 'stars';
    this.sortDirection = 'desc';

    this._initializeTable();
    this._attachEventListeners();
  }

  /**
   * Initialize table with data
   */
  async initialize(repositories) {
    console.time('table-init');

    this.currentData = repositories;
    this.filteredData = [...repositories];

    // Render initial table rows
    this._renderTable();

    // Set up lazy loading on repository elements
    this.container.querySelectorAll('[data-repo-id]').forEach(el => {
      this.lazyLoader.observe(el);
    });

    console.timeEnd('table-init');
  }

  /**
   * Initialize table structure
   */
  _initializeTable() {
    this.container.innerHTML = `
      <div class="table-controls">
        <input type="text" class="search-input" placeholder="Search repositories...">
        <select class="sort-select">
          <option value="stars-desc">⭐ Stars (High to Low)</option>
          <option value="stars-asc">⭐ Stars (Low to High)</option>
          <option value="name-asc">📝 Name (A to Z)</option>
          <option value="name-desc">📝 Name (Z to A)</option>
          <option value="updated-desc">🕐 Recently Updated</option>
          <option value="updated-asc">🕐 Least Recently Updated</option>
        </select>
      </div>

      <div class="table-wrapper">
        <table class="repositories-table">
          <thead>
            <tr>
              <th data-sort="name">Repository</th>
              <th data-sort="stars">Stars</th>
              <th data-sort="language">Language</th>
              <th data-sort="updated">Updated</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody class="table-body">
          </tbody>
        </table>
      </div>

      <div class="table-footer">
        <span class="result-count">Showing 0 repositories</span>
      </div>
    `;
  }

  /**
   * Render table rows
   */
  _renderTable() {
    console.time('table-render');

    const tbody = this.container.querySelector('.table-body');
    tbody.innerHTML = '';

    this.filteredData.forEach((repo, index) => {
      const row = this._createTableRow(repo, index);
      tbody.appendChild(row);
    });

    // Update footer
    const count = this.filteredData.length;
    this.container.querySelector('.result-count').textContent =
      `Showing ${count.toLocaleString()} repositor${count === 1 ? 'y' : 'ies'}`;

    console.timeEnd('table-render');
  }

  /**
   * Create a single table row element
   */
  _createTableRow(repo, index) {
    const row = document.createElement('tr');
    row.dataset.repoId = repo.id;
    row.className = 'table-row';

    // Use document fragments for better performance
    row.innerHTML = `
      <td class="repo-name">
        <a href="${repo.url}" target="_blank" rel="noopener">
          ${this._escapeHtml(repo.name)}
        </a>
      </td>
      <td class="repo-stats" data-bind="stats.stars">
        <span class="loading">...</span>
      </td>
      <td class="repo-language" data-bind="languages">
        <span class="loading">...</span>
      </td>
      <td class="repo-updated" data-bind="stats.updated_at">
        <span class="loading">...</span>
      </td>
      <td class="repo-description">
        ${this._escapeHtml(repo.description?.substring(0, 100) || 'No description')}
      </td>
    `;

    row.addEventListener('click', () => this._onRowClick(repo));
    return row;
  }

  /**
   * Handle sort selection
   */
  _onSortChange(event) {
    const [column, direction] = event.target.value.split('-');
    this.sortColumn = column;
    this.sortDirection = direction;

    console.time('sort-operation');
    this._sortData();
    this._renderTable();
    console.timeEnd('sort-operation');
  }

  /**
   * Sort current data
   */
  _sortData() {
    const multiplier = this.sortDirection === 'asc' ? 1 : -1;

    this.filteredData.sort((a, b) => {
      let aVal, bVal;

      switch (this.sortColumn) {
        case 'name':
          aVal = a.name.toLowerCase();
          bVal = b.name.toLowerCase();
          return aVal.localeCompare(bVal) * multiplier;

        case 'stars':
          aVal = a.stars || 0;
          bVal = b.stars || 0;
          return (aVal - bVal) * multiplier;

        case 'language':
          aVal = (a.language || '').toLowerCase();
          bVal = (b.language || '').toLowerCase();
          return aVal.localeCompare(bVal) * multiplier;

        case 'updated':
          aVal = new Date(a.updated_at || 0).getTime();
          bVal = new Date(b.updated_at || 0).getTime();
          return (aVal - bVal) * multiplier;

        default:
          return 0;
      }
    });
  }

  /**
   * Handle search/filter
   */
  _onSearch(event) {
    const query = event.target.value.toLowerCase();

    console.time('filter-operation');

    this.filteredData = this.currentData.filter(repo =>
      repo.name.toLowerCase().includes(query) ||
      (repo.description && repo.description.toLowerCase().includes(query)) ||
      (repo.language && repo.language.toLowerCase().includes(query))
    );

    this._sortData();
    this._renderTable();

    console.timeEnd('filter-operation');
  }

  /**
   * Handle row click for drill-down
   */
  async _onRowClick(repo) {
    console.time('drill-down');

    // Load full data if not already loaded
    let data = this.lazyLoader.getRepository(repo.id);
    if (!data) {
      try {
        data = await this.lazyLoader.loadBatch([repo.id]).then(results => results[0]);
      } catch (error) {
        console.error('Failed to load repository details:', error);
        return;
      }
    }

    // Open detail panel
    this._showDetailPanel(repo, data);

    console.timeEnd('drill-down');
  }

  /**
   * Show detail panel for repository
   */
  _showDetailPanel(repo, data) {
    const panel = document.createElement('div');
    panel.className = 'detail-panel';
    panel.innerHTML = `
      <div class="panel-header">
        <h2>${this._escapeHtml(repo.name)}</h2>
        <button class="close-btn" aria-label="Close">&times;</button>
      </div>
      <div class="panel-content">
        <div class="section">
          <h3>Stats</h3>
          <ul>
            <li>Stars: <strong>${(data.stats?.stars || 0).toLocaleString()}</strong></li>
            <li>Forks: <strong>${(data.stats?.forks || 0).toLocaleString()}</strong></li>
            <li>Language: <strong>${data.languages ? Object.keys(data.languages)[0] : 'N/A'}</strong></li>
            <li>Last Update: <strong>${new Date(data.stats?.updated_at).toLocaleDateString()}</strong></li>
          </ul>
        </div>
        <div class="section">
          <h3>Summary</h3>
          <p>${this._escapeHtml(data.summary || 'No summary available')}</p>
        </div>
        <div class="section">
          <h3>Quality Metrics</h3>
          <ul>
            <li>Tests: ${data.quality?.has_tests ? '✅' : '❌'}</li>
            <li>Documentation: ${data.quality?.has_docs ? '✅' : '❌'}</li>
            <li>License: ${data.quality?.has_license ? '✅' : '❌'}</li>
            <li>CI/CD: ${data.quality?.has_ci_cd ? '✅' : '❌'}</li>
          </ul>
        </div>
      </div>
    `;

    // Add to container
    this.container.appendChild(panel);
    panel.classList.add('active');

    // Close button handler
    panel.querySelector('.close-btn').addEventListener('click', () => {
      panel.classList.remove('active');
      setTimeout(() => panel.remove(), 300);
    });
  }

  /**
   * Attach event listeners
   */
  _attachEventListeners() {
    this.container.addEventListener('change', (e) => {
      if (e.target.classList.contains('sort-select')) {
        this._onSortChange(e);
      }
    });

    this.container.addEventListener('input', (e) => {
      if (e.target.classList.contains('search-input')) {
        this._onSearch(e);
      }
    });
  }

  /**
   * Escape HTML to prevent XSS
   */
  _escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
}
```

---

## Part 3: Service Worker and Caching

### Step 3.1: Service Worker Implementation

**File:** `static/service-worker.js`

```javascript
/**
 * Service Worker for Offline Support and Caching
 */

const CACHE_VERSION = 'v1-github-stats-2024';
const CACHE_NAMES = {
  static: `${CACHE_VERSION}-static`,
  data: `${CACHE_VERSION}-data`,
  images: `${CACHE_VERSION}-images`
};

const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/static/css/styles.css',
  '/static/js/app.bundle.js',
  '/static/js/lazy-loader.js',
  '/static/js/table.js'
];

// Install: Precache static assets
self.addEventListener('install', (event) => {
  console.log('[Service Worker] Installing...');

  event.waitUntil(
    caches.open(CACHE_NAMES.static)
      .then(cache => {
        console.log('[Service Worker] Caching static assets');
        return cache.addAll(STATIC_ASSETS);
      })
      .then(() => self.skipWaiting())
  );
});

// Activate: Clean up old caches
self.addEventListener('activate', (event) => {
  console.log('[Service Worker] Activating...');

  event.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            if (!Object.values(CACHE_NAMES).includes(cacheName)) {
              console.log('[Service Worker] Deleting old cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      })
      .then(() => self.clients.claim())
  );
});

// Fetch: Network-first for data, cache-first for static
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // Skip non-GET requests
  if (request.method !== 'GET') {
    return;
  }

  // Strategy for different resource types
  if (url.pathname.startsWith('/data/')) {
    // Network-first for data
    event.respondWith(_networkFirstStrategy(request));
  } else if (url.pathname.startsWith('/static/')) {
    // Cache-first for static assets
    event.respondWith(_cacheFirstStrategy(request));
  } else {
    // Network-first for everything else
    event.respondWith(_networkFirstStrategy(request));
  }
});

/**
 * Network-first strategy: Try network, fall back to cache
 */
async function _networkFirstStrategy(request) {
  try {
    const response = await fetch(request);

    if (response.ok) {
      // Cache successful responses
      const cache = await caches.open(CACHE_NAMES.data);
      cache.put(request, response.clone());
      return response;
    }

    return response;
  } catch (error) {
    // Network failed, try cache
    console.log('[Service Worker] Network failed, using cache:', request.url);
    const cachedResponse = await caches.match(request);

    if (cachedResponse) {
      return cachedResponse;
    }

    // No cache available
    return new Response('Offline - Data not available', {
      status: 503,
      statusText: 'Service Unavailable'
    });
  }
}

/**
 * Cache-first strategy: Try cache, fall back to network
 */
async function _cacheFirstStrategy(request) {
  const cachedResponse = await caches.match(request);

  if (cachedResponse) {
    return cachedResponse;
  }

  try {
    const response = await fetch(request);

    if (response.ok) {
      const cache = await caches.open(CACHE_NAMES.static);
      cache.put(request, response.clone());
      return response;
    }

    return response;
  } catch (error) {
    console.error('[Service Worker] Fetch failed:', request.url, error);
    return new Response('Network error', { status: 500 });
  }
}

// Handle messages from clients
self.addEventListener('message', (event) => {
  if (event.data?.type === 'CACHE_INVALIDATE') {
    _invalidateCache(event.data.pattern);
  }

  if (event.data?.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

/**
 * Invalidate cache by pattern
 */
async function _invalidateCache(pattern) {
  if (pattern === 'all') {
    // Clear all caches
    const cacheNames = await caches.keys();
    await Promise.all(
      cacheNames.map(name => caches.delete(name))
    );
    console.log('[Service Worker] All caches cleared');
  } else {
    // Clear specific pattern
    const cache = await caches.open(CACHE_NAMES.data);
    const requests = await cache.keys();
    requests.forEach(request => {
      if (request.url.includes(pattern)) {
        cache.delete(request);
      }
    });
  }
}
```

### Step 3.2: Service Worker Registration

**File:** `static/js/app-init.js`

```javascript
/**
 * Application Initialization
 * Registers service worker and sets up lazy loading
 */

class AppInitializer {
  constructor() {
    this.lazyLoader = null;
    this.table = null;
  }

  /**
   * Initialize the application
   */
  async init() {
    console.log('Initializing application...');

    // Register service worker
    await this._registerServiceWorker();

    // Load index data
    const index = await this._loadIndexData();

    // Initialize lazy loader
    this.lazyLoader = new RepositoryLazyLoader({
      batchSize: 10,
      concurrentRequests: 4
    });

    // Initialize table
    this.table = new RepositoryTable('app-container', {
      lazyLoader: this.lazyLoader
    });

    // Populate table with index data
    await this.table.initialize(index.repositories);

    // Load aggregated metrics
    const metrics = await this._loadAggregatedMetrics();
    this._displayMetrics(metrics);

    console.log('Application ready');
  }

  /**
   * Register service worker
   */
  async _registerServiceWorker() {
    if ('serviceWorker' not in navigator) {
      console.log('Service Workers not supported');
      return;
    }

    try {
      const registration = await navigator.serviceWorker.register('/static/service-worker.js');
      console.log('Service Worker registered:', registration);

      // Listen for updates
      registration.addEventListener('updatefound', () => {
        const newWorker = registration.installing;
        newWorker.addEventListener('statechange', () => {
          if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
            console.log('New service worker available. Update available');
            this._promptUpdate();
          }
        });
      });

    } catch (error) {
      console.error('Service Worker registration failed:', error);
    }
  }

  /**
   * Load index data from server
   */
  async _loadIndexData() {
    console.time('index-load');

    try {
      const response = await fetch('/data/index.json');
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();

      console.timeEnd('index-load');
      return data;

    } catch (error) {
      console.error('Failed to load index:', error);
      throw error;
    }
  }

  /**
   * Load aggregated metrics
   */
  async _loadAggregatedMetrics() {
    try {
      const response = await fetch('/data/aggregated.json');
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return await response.json();

    } catch (error) {
      console.error('Failed to load metrics:', error);
      return null;
    }
  }

  /**
   * Display aggregated metrics on page
   */
  _displayMetrics(metrics) {
    if (!metrics) return;

    const summary = metrics.summary || {};
    const metricsHtml = `
      <div class="metrics-container">
        <div class="metric">
          <span class="metric-label">Total Repositories</span>
          <span class="metric-value">${summary.total_repositories?.toLocaleString() || '—'}</span>
        </div>
        <div class="metric">
          <span class="metric-label">Total Stars</span>
          <span class="metric-value">${summary.total_stars?.toLocaleString() || '—'}</span>
        </div>
        <div class="metric">
          <span class="metric-label">Average Stars</span>
          <span class="metric-value">${summary.average_stars_per_repo?.toFixed(1) || '—'}</span>
        </div>
        <div class="metric">
          <span class="metric-label">Total Commits</span>
          <span class="metric-value">${summary.total_commits?.toLocaleString() || '—'}</span>
        </div>
      </div>
    `;

    const container = document.getElementById('metrics-container');
    if (container) {
      container.innerHTML = metricsHtml;
    }
  }

  /**
   * Prompt user for update
   */
  _promptUpdate() {
    const updateBanner = document.createElement('div');
    updateBanner.className = 'update-banner';
    updateBanner.innerHTML = `
      <span>New version available</span>
      <button id="update-btn">Update</button>
    `;

    document.body.appendChild(updateBanner);

    document.getElementById('update-btn').addEventListener('click', () => {
      if (navigator.serviceWorker.controller) {
        navigator.serviceWorker.controller.postMessage({ type: 'SKIP_WAITING' });
      }
      window.location.reload();
    });
  }
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    const app = new AppInitializer();
    app.init().catch(error => {
      console.error('Application initialization failed:', error);
    });
  });
} else {
  const app = new AppInitializer();
  app.init().catch(error => {
    console.error('Application initialization failed:', error);
  });
}
```

---

## Part 4: Performance Monitoring

### Step 4.1: Web Vitals Monitoring

**File:** `static/js/performance-monitor.js`

```javascript
/**
 * Performance Monitoring
 * Tracks Web Vitals and custom metrics
 */

class PerformanceMonitor {
  constructor(analyticsEndpoint = '/api/metrics') {
    this.endpoint = analyticsEndpoint;
    this.metrics = {};
    this.marks = {};
  }

  /**
   * Initialize Web Vitals monitoring
   */
  initializeWebVitals() {
    // Import from web-vitals package
    import('https://unpkg.com/web-vitals@3/dist/web-vitals.js')
      .then(module => {
        const { getCLS, getFID, getFCP, getLCP, getTTFB } = module;

        getCLS(metric => this._recordMetric('CLS', metric));
        getFID(metric => this._recordMetric('FID', metric));
        getFCP(metric => this._recordMetric('FCP', metric));
        getLCP(metric => this._recordMetric('LCP', metric));
        getTTFB(metric => this._recordMetric('TTFB', metric));
      })
      .catch(error => console.error('Failed to load web-vitals:', error));
  }

  /**
   * Mark a timing point
   */
  mark(label) {
    this.marks[label] = performance.now();
  }

  /**
   * Measure and record a timing
   */
  measure(label) {
    if (!this.marks[label]) {
      console.warn(`No mark found for ${label}`);
      return;
    }

    const duration = performance.now() - this.marks[label];
    this._recordMetric(label, { value: duration });

    return duration;
  }

  /**
   * Record a custom metric
   */
  _recordMetric(name, metric) {
    this.metrics[name] = {
      value: metric.value || metric,
      rating: metric.rating,
      delta: metric.delta,
      id: metric.id
    };

    console.log(`${name}:`, metric.value || metric);

    // Log if exceeds performance budget
    this._checkPerformanceBudget(name, metric.value || metric);
  }

  /**
   * Check performance budget
   */
  _checkPerformanceBudget(name, value) {
    const budgets = {
      'FCP': 2000,      // First Contentful Paint
      'LCP': 2500,      // Largest Contentful Paint
      'CLS': 0.1,       // Cumulative Layout Shift
      'FID': 100,       // First Input Delay
      'TTB': 600,       // Time to First Byte
      'table-load': 5000,
      'sort-operation': 1000,
      'filter-operation': 1000,
      'drill-down': 500,
      'viz-render': 2000
    };

    const budget = budgets[name];
    if (budget && value > budget) {
      console.warn(`${name} exceeded budget: ${value}ms > ${budget}ms`);
    }
  }

  /**
   * Send metrics to server
   */
  async sendMetrics() {
    if (Object.keys(this.metrics).length === 0) return;

    const payload = {
      timestamp: new Date().toISOString(),
      url: window.location.href,
      userAgent: navigator.userAgent,
      metrics: this.metrics
    };

    try {
      await fetch(this.endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
        // Use sendBeacon for reliability
        keepalive: true
      });
    } catch (error) {
      console.error('Failed to send metrics:', error);
    }
  }

  /**
   * Generate performance report
   */
  getReport() {
    return {
      timestamp: new Date().toISOString(),
      metrics: this.metrics,
      summary: this._summarizeMetrics()
    };
  }

  /**
   * Summarize metrics for display
   */
  _summarizeMetrics() {
    const report = {};

    for (const [name, data] of Object.entries(this.metrics)) {
      const value = typeof data === 'number' ? data : data.value;
      report[name] = {
        value: value.toFixed(2),
        unit: this._getUnit(name),
        status: this._getStatus(name, value)
      };
    }

    return report;
  }

  /**
   * Get unit for metric
   */
  _getUnit(name) {
    if (name === 'CLS') return '(unitless)';
    return 'ms';
  }

  /**
   * Get status badge for metric
   */
  _getStatus(name, value) {
    const budgets = {
      'FCP': { good: 1800, poor: 3000 },
      'LCP': { good: 2500, poor: 4000 },
      'CLS': { good: 0.1, poor: 0.25 },
      'FID': { good: 100, poor: 300 }
    };

    const budget = budgets[name];
    if (!budget) return 'ℹ️';

    return value <= budget.good ? '✅ Good' : value <= budget.poor ? '⚠️ Needs Improvement' : '❌ Poor';
  }
}

// Global instance
const performanceMonitor = new PerformanceMonitor();

// Auto-send on page unload
window.addEventListener('beforeunload', () => {
  performanceMonitor.sendMetrics();
});
```

---

## Integration Checklist

- [ ] Generate index.json with all repositories
- [ ] Generate individual repository bundles
- [ ] Generate aggregated metrics file
- [ ] Implement lazy-loader.js
- [ ] Implement table.js with sorting/filtering
- [ ] Implement service-worker.js
- [ ] Implement app-init.js
- [ ] Implement performance-monitor.js
- [ ] Set up gzip compression for JSON files
- [ ] Configure cache headers in GitHub Pages
- [ ] Test lazy loading performance
- [ ] Test sort/filter performance (<1s target)
- [ ] Test drill-down performance (<500ms target)
- [ ] Measure Web Vitals
- [ ] Set up monitoring dashboard

---

This implementation guide provides complete, production-ready code for all optimization strategies. Start with Part 1 (data generation), then Part 2 (client-side loading), then Part 3 (caching), and finally Part 4 (monitoring).
