# Contract: UnifiedReportGenerator

**Feature**: Unified Profile Report
**Date**: 2025-12-30
**Status**: Design Phase

## Purpose

Defines the interface contract for `UnifiedReportGenerator`, the core component responsible for converting a `UnifiedReport` data entity into a formatted GitHub-Flavored Markdown document.

---

## Class Interface

### UnifiedReportGenerator

**Location**: `src/spark/unified_report_generator.py` (new file)

**Responsibility**: Generate markdown reports combining SVG visualizations and repository analysis.

**Dependencies**:
- Existing: `ReportGenerator` (for repository entry formatting reuse)
- New: `UnifiedReport` entity (from data-model.md)

---

## Public Methods

### 1. `generate_report()`

**Signature**:
```python
def generate_report(self, report: UnifiedReport, output_path: str) -> None:
    """Generate unified markdown report and write to file.

    Args:
        report: UnifiedReport entity with all data
        output_path: Absolute path to output markdown file

    Raises:
        WorkflowError: If report generation fails (critical error)
        OSError: If file write operations fail
        ValidationError: If report data is invalid

    Postconditions:
        - File exists at output_path with valid markdown content
        - File size < 1MB (FR constraint)
        - Contains all sections per FR-005 structure
    """
```

**Contract**:

| Precondition | Validation |
|--------------|------------|
| `report` is valid `UnifiedReport` | `report.validate()` returns empty list |
| `output_path` is absolute path | `os.path.isabs(output_path)` is True |
| Parent directory exists | `os.path.exists(os.path.dirname(output_path))` is True |

| Postcondition | Verification |
|---------------|--------------|
| File created | `os.path.exists(output_path)` is True |
| File size < 1MB | `os.path.getsize(output_path) < 1_048_576` |
| Valid markdown | Can parse with markdown library |
| Contains required sections | Matches FR-005 structure |

**Error Handling**:
```python
# Example usage
try:
    generator = UnifiedReportGenerator()
    generator.generate_report(unified_report, "/path/to/output.md")
except ValidationError as e:
    logger.error(f"Invalid report data: {e}")
    raise
except WorkflowError as e:
    logger.error(f"Report generation failed: {e}")
    raise
except OSError as e:
    logger.error(f"File write failed: {e}")
    raise
```

---

### 2. `generate_markdown()`

**Signature**:
```python
def generate_markdown(self, report: UnifiedReport) -> str:
    """Generate markdown content without writing to file.

    Args:
        report: UnifiedReport entity with all data

    Returns:
        str: Complete markdown document content

    Raises:
        ValidationError: If report data is invalid
        WorkflowError: If markdown generation fails

    Postconditions:
        - Returns non-empty string
        - String length < 1MB (1_048_576 bytes)
        - Valid GitHub-Flavored Markdown syntax
    """
```

**Contract**:

| Precondition | Validation |
|--------------|------------|
| `report` is valid `UnifiedReport` | `report.validate()` returns empty list |

| Postcondition | Verification |
|---------------|--------------|
| Non-empty result | `len(result) > 0` |
| Size constraint | `len(result.encode('utf-8')) < 1_048_576` |
| Contains sections | All FR-005 sections present |

---

## Protected Methods (Internal Implementation)

### Section Generators

```python
def _generate_header(self, report: UnifiedReport) -> str:
    """Generate header section per FR-005 (Section 1).

    Returns:
        str: Markdown header with metadata, navigation
    """

def _generate_profile_overview(self, report: UnifiedReport) -> str:
    """Generate profile overview section per FR-005 (Section 2).

    Returns:
        str: Markdown with embedded SVG references (FR-017 ordering)
    """

def _generate_repository_analysis(self, report: UnifiedReport) -> str:
    """Generate repository analysis section per FR-005 (Section 3).

    Returns:
        str: Markdown with top 50 repository entries
    """

def _generate_footer(self, report: UnifiedReport) -> str:
    """Generate footer section per FR-005 (Section 4).

    Returns:
        str: Markdown with metadata, attribution, data sources
    """
```

### Helper Methods

```python
def _embed_svg(self, name: str, relative_path: str) -> str:
    """Generate SVG embedding markdown.

    Args:
        name: Display name for alt text
        relative_path: Relative path from report to SVG (e.g., "../overview.svg")

    Returns:
        str: Markdown image syntax or fallback text if SVG missing
    """

def _format_repository_entry(self, analysis: RepositoryAnalysis, rank: int) -> str:
    """Format single repository entry.

    Reuses existing ReportGenerator._format_repository_entry logic.

    Args:
        analysis: RepositoryAnalysis with metrics, summary, tech stack
        rank: Repository ranking position (1-50)

    Returns:
        str: Markdown-formatted repository entry
    """
```

---

## Constructor

```python
def __init__(self, config: Optional[SparkConfig] = None):
    """Initialize unified report generator.

    Args:
        config: Optional configuration override (default: load from spark.yml)
    """
```

---

## Usage Examples

### Example 1: Basic Report Generation

```python
from spark.unified_report_generator import UnifiedReportGenerator
from spark.models.report import UnifiedReport

# Assume unified_report is populated from workflow
generator = UnifiedReportGenerator()

# Generate and write to file
output_path = "output/reports/markhazleton-analysis.md"
generator.generate_report(unified_report, output_path)

print(f"✅ Unified report generated: {output_path}")
```

### Example 2: Preview Markdown Before Writing

```python
# Generate markdown content first
markdown_content = generator.generate_markdown(unified_report)

# Validate before writing
if len(markdown_content.encode('utf-8')) < 1_048_576:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
else:
    logger.warning("Report exceeds 1MB size constraint")
```

### Example 3: Handling Partial Failures

```python
# Report with warnings (FR-011, FR-012)
if unified_report.partial_results:
    logger.warning(f"Report has {len(unified_report.warnings)} warnings")

# Still generate report with available data
generator.generate_report(unified_report, output_path)

# Footer will include warning section automatically
```

---

## Testing Contract

### Unit Tests

```python
def test_generate_header_includes_metadata():
    """Verify header contains required metadata."""
    report = create_test_unified_report()
    generator = UnifiedReportGenerator()

    header = generator._generate_header(report)

    assert report.username in header
    assert report.timestamp.strftime('%Y-%m-%d') in header
    assert str(report.total_repos) in header

def test_generate_profile_overview_embeds_svgs():
    """Verify SVG embedding per FR-017 ordering."""
    report = create_test_unified_report(available_svgs=["overview", "languages"])
    generator = UnifiedReportGenerator()

    overview = generator._generate_profile_overview(report)

    # FR-017 ordering: overview first, languages before fun
    assert overview.index("overview.svg") < overview.index("languages.svg")
    assert "![Overview Statistics](../overview.svg)" in overview

def test_generate_repository_analysis_top_50():
    """Verify top 50 repository limit (FR-004)."""
    report = create_test_unified_report(repository_count=75)
    generator = UnifiedReportGenerator()

    analysis = generator._generate_repository_analysis(report)

    # Only top 50 included
    assert analysis.count("###") == 50  # 50 repository headings

def test_generate_footer_includes_errors_if_present():
    """Verify footer warning section appears when errors exist."""
    report = create_test_unified_report(errors=["SVG generation failed: heatmap"])
    generator = UnifiedReportGenerator()

    footer = generator._generate_footer(report)

    assert "⚠️ Generation Warnings" in footer
    assert "SVG generation failed: heatmap" in footer
```

### Integration Tests

```python
def test_generate_report_creates_valid_markdown_file():
    """End-to-end: generate complete report and validate file."""
    report = create_test_unified_report()
    generator = UnifiedReportGenerator()
    output_path = tmp_path / "test-analysis.md"

    generator.generate_report(report, str(output_path))

    # File exists and under size constraint
    assert output_path.exists()
    assert output_path.stat().st_size < 1_048_576

    # Valid markdown structure
    content = output_path.read_text()
    assert content.startswith("# GitHub Profile:")
    assert "## Profile Overview" in content
    assert "## Top" in content  # "Top N Repositories"
    assert "## Report Metadata" in content

def test_generate_markdown_matches_file_output():
    """Verify generate_markdown matches generate_report output."""
    report = create_test_unified_report()
    generator = UnifiedReportGenerator()

    # Generate markdown string
    markdown_str = generator.generate_markdown(report)

    # Generate to file
    output_path = tmp_path / "test-analysis.md"
    generator.generate_report(report, str(output_path))

    # Compare
    file_content = output_path.read_text()
    assert markdown_str == file_content
```

---

## Performance Contract

### Time Complexity

| Operation | Complexity | Justification |
|-----------|-----------|---------------|
| `generate_report()` | O(n) | n = number of repositories (max 50) |
| Header generation | O(1) | Fixed metadata fields |
| SVG embedding | O(1) | 6 SVGs (constant) |
| Repository formatting | O(n) | Iterate through top 50 |
| Footer generation | O(1) | Fixed metadata fields |

### Memory Usage

| Component | Memory Estimate |
|-----------|----------------|
| Input `UnifiedReport` | ~1-2 MB (50 repos with summaries) |
| Generated markdown string | ~1 MB (SC-002 constraint) |
| Peak memory | ~3 MB (input + output + overhead) |

### Execution Time Targets

- **generate_markdown()**: < 100ms for 50 repositories
- **generate_report()**: < 200ms (generation + file write)

---

## Backward Compatibility

### Coexistence with Legacy `ReportGenerator`

```python
# Legacy dated report generation (unchanged)
legacy_generator = ReportGenerator()
legacy_generator.generate_report(legacy_report, "output/reports/user-20251230.md")

# NEW unified report generation
unified_generator = UnifiedReportGenerator()
unified_generator.generate_report(unified_report, "output/reports/user-analysis.md")

# Both outputs coexist in same directory
```

### Shared Code Reuse

```python
class UnifiedReportGenerator:
    def __init__(self):
        # Reuse existing repository formatter
        self.legacy_generator = ReportGenerator()

    def _format_repository_entry(self, analysis: RepositoryAnalysis, rank: int) -> str:
        """Delegate to existing formatter for consistency."""
        return self.legacy_generator._format_repository_entry(analysis.repository, ...)
```

---

## Configuration

### Config File Extension (`config/spark.yml`)

```yaml
# Unified Report Settings (NEW)
report:
  unified:
    svg_order:  # FR-017 ordering
      - overview
      - heatmap
      - streaks
      - release
      - languages
      - fun
    include_footer_metadata: true
    fallback_on_missing_svg: true  # Show placeholder vs skip entirely
    max_file_size_mb: 1  # SC-002 constraint
```

---

## Error Scenarios

| Scenario | Exception | Recovery |
|----------|-----------|----------|
| Invalid report data | `ValidationError` | Fix data, retry |
| Missing parent directory | `OSError` | Create directory, retry |
| Disk full | `OSError` | Clear space, retry |
| File size exceeds 1MB | `WorkflowError` | Reduce content (fewer repos, shorter summaries) |
| Permission denied | `OSError` | Check file permissions |

---

## Contract Guarantees

### Invariants

1. **File Size**: Generated markdown always < 1MB (validated before write)
2. **Section Order**: Always Header → Profile → Analysis → Footer (FR-005)
3. **SVG Order**: SVGs embedded in FR-017 order (when present)
4. **Encoding**: Always UTF-8 encoded output
5. **Idempotency**: Generating same report multiple times produces identical markdown

### Assumptions

1. `UnifiedReport` data is pre-validated before passing to generator
2. File system supports UTF-8 filenames and content
3. Output directory permissions allow file creation
4. Markdown viewers support GitHub-Flavored Markdown spec

---

## Summary

**Core Responsibility**: Convert `UnifiedReport` entity → GitHub-Flavored Markdown file

**Key Methods**:
- `generate_report(report, path)` - Public API for file generation
- `generate_markdown(report)` - Public API for in-memory generation

**Guarantees**:
- File size < 1MB (SC-002)
- Structure matches FR-005 (4 sections)
- SVG ordering per FR-017
- Graceful handling of missing SVGs (FR-011)

**Next**: See [markdown_template_schema.md](markdown_template_schema.md) for detailed section structure.
