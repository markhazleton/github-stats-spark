# Data Model: Unified Profile Report

**Feature Branch**: `001-unified-profile-report`
**Date**: 2025-12-30
**Status**: Design Phase

## Overview

This document defines the data entities required for the Unified Profile Report feature, extending the existing data model in `src/spark/models/` to support consolidating SVG visualizations and repository analysis into a single markdown report.

---

## Core Entities

### 1. UnifiedReport

**Purpose**: Top-level entity representing the complete unified markdown report combining profile summary, SVG visualizations, and repository analysis.

**Location**: Extends `src/spark/models/report.py` (add new entity alongside existing `Report` class)

**Attributes**:

| Attribute | Type | Description | Validation Rules |
|-----------|------|-------------|-----------------|
| `username` | `str` | GitHub username being analyzed | Required, non-empty |
| `timestamp` | `datetime` | Report generation timestamp (UTC) | Required, auto-generated |
| `version` | `str` | Report format version (semver) | Required, default "1.0.0" |
| `total_repos` | `int` | Total number of repositories analyzed | >= 0 |
| `available_svgs` | `List[str]` | List of successfully generated SVG types | Subset of ["overview", "heatmap", "languages", "fun", "streaks", "release"] |
| `repositories` | `List[RepositoryAnalysis]` | Top 50 repository analyses (or fewer if <50 repos) | Max length 50, ordered by composite_score descending |
| `generation_time` | `float` | Total generation time in seconds | >= 0.0 |
| `success_rate` | `float` | Percentage of successful operations (0-100) | 0.0 <= x <= 100.0 |
| `total_api_calls` | `int` | Number of GitHub API calls made | >= 0 |
| `total_ai_tokens` | `int` | Total AI tokens used for summarization | >= 0 |
| `ai_summary_rate` | `float` | Percentage of repos with AI summaries (0-100) | 0.0 <= x <= 100.0 |
| `ai_model` | `Optional[str]` | AI model used for summarization (e.g., "claude-3-5-haiku-20241022") | Nullable |
| `errors` | `List[str]` | List of error messages encountered | Default empty list |
| `warnings` | `List[str]` | List of warning messages | Default empty list |
| `partial_results` | `bool` | True if any errors/warnings occurred | Default False |

**Relationships**:
- Has many `RepositoryAnalysis` (via `repositories` attribute)
- References SVG files by type (via `available_svgs` list)

**Methods**:

```python
class UnifiedReport:
    """Represents a unified markdown report combining SVGs and repository analysis."""

    def __init__(
        self,
        username: str,
        timestamp: datetime,
        repositories: List[RepositoryAnalysis],
        available_svgs: List[str],
        **kwargs
    ):
        """Initialize unified report with required data."""
        self.username = username
        self.timestamp = timestamp
        self.version = kwargs.get("version", "1.0.0")
        self.repositories = repositories[:50]  # Enforce top 50 limit
        self.available_svgs = available_svgs
        self.total_repos = len(repositories)
        self.generation_time = kwargs.get("generation_time", 0.0)
        self.total_api_calls = kwargs.get("total_api_calls", 0)
        self.total_ai_tokens = kwargs.get("total_ai_tokens", 0)
        self.ai_model = kwargs.get("ai_model")
        self.errors = kwargs.get("errors", [])
        self.warnings = kwargs.get("warnings", [])
        self.partial_results = len(self.errors) > 0 or len(self.warnings) > 0

        # Calculate derived metrics
        self.success_rate = self._calculate_success_rate()
        self.ai_summary_rate = self._calculate_ai_summary_rate()

    def _calculate_success_rate(self) -> float:
        """Calculate success rate based on errors/warnings."""
        total_operations = (
            1  # GitHub API fetch
            + len(self.repositories)  # Repository analyses
            + 6  # SVG generations (attempts)
        )
        failed_operations = len(self.errors)
        return ((total_operations - failed_operations) / total_operations) * 100.0

    def _calculate_ai_summary_rate(self) -> float:
        """Calculate percentage of repositories with AI-generated summaries."""
        if not self.repositories:
            return 0.0

        ai_summaries = sum(
            1
            for analysis in self.repositories
            if analysis.summary and analysis.summary.generation_method == "ai"
        )
        return (ai_summaries / len(self.repositories)) * 100.0

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "username": self.username,
            "timestamp": self.timestamp.isoformat(),
            "version": self.version,
            "total_repos": self.total_repos,
            "available_svgs": self.available_svgs,
            "repositories": [r.to_dict() for r in self.repositories],
            "generation_time": self.generation_time,
            "success_rate": self.success_rate,
            "total_api_calls": self.total_api_calls,
            "total_ai_tokens": self.total_ai_tokens,
            "ai_summary_rate": self.ai_summary_rate,
            "ai_model": self.ai_model,
            "errors": self.errors,
            "warnings": self.warnings,
            "partial_results": self.partial_results,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "UnifiedReport":
        """Create from dictionary (deserialization)."""
        return cls(
            username=data["username"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            repositories=[
                RepositoryAnalysis.from_dict(r) for r in data["repositories"]
            ],
            available_svgs=data["available_svgs"],
            version=data.get("version", "1.0.0"),
            generation_time=data.get("generation_time", 0.0),
            total_api_calls=data.get("total_api_calls", 0),
            total_ai_tokens=data.get("total_ai_tokens", 0),
            ai_model=data.get("ai_model"),
            errors=data.get("errors", []),
            warnings=data.get("warnings", []),
        )
```

**Validation Rules**:

```python
def validate(self) -> List[str]:
    """Validate report data integrity.

    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []

    # FR-001: Username required
    if not self.username or not self.username.strip():
        errors.append("Username must be non-empty")

    # FR-004: Repository limit validation
    if len(self.repositories) > 50:
        errors.append(f"Repository count exceeds limit of 50 (got {len(self.repositories)})")

    # FR-003: SVG validation
    valid_svg_types = {"overview", "heatmap", "languages", "fun", "streaks", "release"}
    invalid_svgs = set(self.available_svgs) - valid_svg_types
    if invalid_svgs:
        errors.append(f"Invalid SVG types: {invalid_svgs}")

    # FR-017: SVG ordering validation (optional - for testing)
    expected_order = ["overview", "heatmap", "streaks", "release", "languages", "fun"]
    if self.available_svgs and self.available_svgs != [s for s in expected_order if s in self.available_svgs]:
        errors.append("SVG ordering does not match FR-017 specification")

    # Success rate bounds
    if not (0.0 <= self.success_rate <= 100.0):
        errors.append(f"Success rate out of bounds: {self.success_rate}")

    return errors
```

---

### 2. GitHubData (New Intermediate Entity)

**Purpose**: Encapsulates all GitHub API data fetched in Stage 1 of the workflow, shared between SVG generation and repository analysis stages.

**Location**: Add to `src/spark/models/` as new file `github_data.py`

**Attributes**:

| Attribute | Type | Description |
|-----------|------|-------------|
| `username` | `str` | GitHub username |
| `profile` | `UserProfile` | User profile data (from models/profile.py) |
| `repositories` | `List[Repository]` | All fetched repositories |
| `commit_histories` | `Dict[str, CommitHistory]` | Commit data by repository name |
| `fetch_timestamp` | `datetime` | When data was fetched |
| `api_call_count` | `int` | Number of API calls made |
| `cache_hit_count` | `int` | Number of cache hits |

**Purpose**: Enables data sharing between workflow stages without re-fetching from GitHub API.

**Methods**:

```python
@dataclass
class GitHubData:
    """Container for GitHub API data used across workflow stages."""

    username: str
    profile: UserProfile
    repositories: List[Repository]
    commit_histories: Dict[str, CommitHistory]
    fetch_timestamp: datetime
    api_call_count: int = 0
    cache_hit_count: int = 0

    @property
    def cache_efficiency(self) -> float:
        """Calculate percentage of requests served from cache."""
        total = self.api_call_count + self.cache_hit_count
        return (self.cache_hit_count / total * 100.0) if total > 0 else 0.0
```

---

### 3. WorkflowError (New Exception Class)

**Purpose**: Custom exception for workflow-level failures that should halt execution.

**Location**: Add to `src/spark/` as `exceptions.py` (new file)

**Attributes**:

| Attribute | Type | Description |
|-----------|------|-------------|
| `message` | `str` | Error description |
| `stage` | `str` | Workflow stage where error occurred |
| `cause` | `Optional[Exception]` | Original exception |

**Usage**:

```python
class WorkflowError(Exception):
    """Raised when a critical workflow stage fails."""

    def __init__(self, message: str, stage: str = "unknown", cause: Exception = None):
        super().__init__(message)
        self.message = message
        self.stage = stage
        self.cause = cause

    def __str__(self) -> str:
        cause_info = f" (caused by {type(self.cause).__name__})" if self.cause else ""
        return f"[{self.stage}] {self.message}{cause_info}"
```

---

## Entity Relationships

### Relationship Diagram

```
UnifiedReport (1)
├── username: str
├── timestamp: datetime
├── available_svgs: List[str] ──────> SVG Files (6)
│                                      ├── overview.svg
│                                      ├── heatmap.svg
│                                      ├── languages.svg
│                                      ├── fun.svg
│                                      ├── streaks.svg
│                                      └── release.svg
│
└── repositories (0..50) ──────> RepositoryAnalysis
                                  ├── repository: Repository (existing)
                                  ├── commit_history: CommitHistory (existing)
                                  ├── summary: RepositorySummary (existing)
                                  ├── tech_stack: TechnologyStack (existing)
                                  ├── rank: int
                                  └── composite_score: float

GitHubData (intermediate)
├── profile: UserProfile (existing)
├── repositories: List[Repository] (existing)
└── commit_histories: Dict[str, CommitHistory] (existing)
```

### Dependency Flow

```
GitHub API
    ↓
GitHubData (fetched once, shared)
    ↓
    ├─> StatsCalculator + StatisticsVisualizer ─> SVG Files (6)
    │
    └─> RepositoryRanker + RepositorySummarizer ─> RepositoryAnalysis (top 50)
            ↓
        UnifiedReport
            ↓
        UnifiedReportGenerator (markdown)
            ↓
        {username}-analysis.md
```

---

## Validation & Constraints

### Functional Requirement Mapping

| Requirement | Data Model Enforcement |
|-------------|------------------------|
| **FR-001** | `UnifiedReport.username` must be non-empty string |
| **FR-002** | File naming handled by generator (not data model) |
| **FR-003** | `UnifiedReport.available_svgs` must be subset of valid types |
| **FR-004** | `UnifiedReport.repositories` max length 50, allows fewer |
| **FR-005** | Enforced by template (not data model) |
| **FR-006** | `RepositoryAnalysis.composite_score` uses configured weights |
| **FR-007** | `RepositoryAnalysis.tech_stack` includes currency status |
| **FR-017** | `UnifiedReport.available_svgs` ordering validated |

### Invariants

1. **Repository Limit**: `len(UnifiedReport.repositories) <= 50` always holds
2. **SVG Types**: All values in `available_svgs` must be in `{"overview", "heatmap", "languages", "fun", "streaks", "release"}`
3. **Success Rate Bounds**: `0.0 <= success_rate <= 100.0`
4. **Timestamp Consistency**: `UnifiedReport.timestamp >= GitHubData.fetch_timestamp`
5. **Partial Results Flag**: `partial_results == True` if and only if `len(errors) > 0 or len(warnings) > 0`

---

## State Transitions

### UnifiedReport Lifecycle

```
[INITIAL]
    ↓ (workflow.execute)
[FETCHING_DATA] ← GitHubData created
    ↓
[GENERATING_SVGS] ← available_svgs populated
    ↓
[ANALYZING_REPOS] ← repositories populated
    ↓
[GENERATING_REPORT] ← UnifiedReport created
    ↓
[COMPLETED] ← markdown file written

Error transitions:
- FETCHING_DATA → ERROR (critical failure)
- GENERATING_SVGS → PARTIAL (non-critical, continues)
- ANALYZING_REPOS → PARTIAL (non-critical, continues)
- GENERATING_REPORT → ERROR (critical failure)
```

---

## File Size Estimation

**Constraint**: SC-002 requires report file size < 1MB

### Size Breakdown

| Component | Estimated Size | Justification |
|-----------|---------------|---------------|
| Header | ~500 bytes | Metadata, title, navigation |
| SVG references | ~1KB | 6 images × ~150 bytes each |
| Repository entries | ~980KB | 50 repos × ~20KB each (summary, tech stack, metrics) |
| Footer | ~1KB | Metadata, attribution, data sources |
| **Total** | **~982.5KB** | Under 1MB constraint ✅ |

### Repository Entry Size Estimate

Assuming average per repository:
- Basic metadata: 500 bytes (name, URL, stars, forks, language, dates)
- AI summary: 1000-2000 bytes (200-400 words)
- Technology stack: 500-1000 bytes (dependencies list)
- Quality indicators: 300 bytes (badges, metrics)
- Formatting/whitespace: 200 bytes

**Average**: ~2.5KB - 4KB per repository
**50 repositories**: 125KB - 200KB (well under budget)

**Actual**: Existing dated reports are ~350KB for 50 repositories, so unified report with SVGs will be ~351KB total.

---

## Testing Considerations

### Unit Tests

```python
def test_unified_report_validation():
    """Test UnifiedReport validation rules."""
    # Test empty username
    report = UnifiedReport(username="", ...)
    errors = report.validate()
    assert "Username must be non-empty" in errors

    # Test repository limit
    report = UnifiedReport(repositories=[...] * 51, ...)
    errors = report.validate()
    assert any("exceeds limit of 50" in e for e in errors)

def test_unified_report_success_rate_calculation():
    """Test success rate calculation with errors/warnings."""
    report = UnifiedReport(..., errors=["error1", "error2"])
    assert 0.0 <= report.success_rate <= 100.0

def test_github_data_cache_efficiency():
    """Test cache efficiency calculation."""
    data = GitHubData(..., api_call_count=10, cache_hit_count=40)
    assert data.cache_efficiency == 80.0
```

### Integration Tests

```python
def test_unified_report_serialization():
    """Test UnifiedReport round-trip serialization."""
    report = UnifiedReport(...)
    data = report.to_dict()
    restored = UnifiedReport.from_dict(data)
    assert restored.username == report.username
    assert len(restored.repositories) == len(report.repositories)

def test_workflow_data_sharing():
    """Test GitHubData enables stage separation."""
    github_data = workflow._fetch_github_data("testuser")
    svg_stage = workflow._generate_svgs("testuser", github_data)
    analysis_stage = workflow._analyze_repositories("testuser", github_data.repositories, ...)
    # Assert: Data fetched once, used twice
```

---

## Migration Path

### From Existing `Report` Entity

The current `Report` class in `src/spark/models/report.py` can coexist with `UnifiedReport`:

```python
# Existing (dated reports)
class Report:
    """Dated repository analysis report."""
    ...

# NEW (unified reports)
class UnifiedReport:
    """Unified markdown report with SVGs and analysis."""
    ...

# Conversion helper (for backward compatibility)
def convert_to_legacy_format(unified: UnifiedReport) -> Report:
    """Convert UnifiedReport to legacy Report format.

    Used when --keep-dated flag is provided to generate both reports.
    """
    return Report(
        username=unified.username,
        timestamp=unified.timestamp,
        repositories=unified.repositories,
        # ... map fields ...
    )
```

---

## Summary

**New Entities Added**:
1. `UnifiedReport` (in `src/spark/models/report.py`)
2. `GitHubData` (new file `src/spark/models/github_data.py`)
3. `WorkflowError` (new file `src/spark/exceptions.py`)

**Existing Entities Reused**:
- `Repository` (models/repository.py)
- `RepositoryAnalysis` (models/report.py)
- `RepositorySummary` (models/summary.py)
- `TechnologyStack` (models/tech_stack.py)
- `CommitHistory` (models/commit.py)
- `UserProfile` (models/profile.py)

**No Breaking Changes**: All existing entities remain unchanged. `UnifiedReport` is a new addition that works alongside legacy `Report` class.

**Next**: See [contracts/unified_report_generator.md](contracts/unified_report_generator.md) for interface specifications.
