# Contract: Markdown Template Schema

**Feature**: Unified Profile Report
**Date**: 2025-12-30
**Status**: Design Phase

## Purpose

Defines the exact structure and formatting of the unified markdown report output, ensuring compliance with FR-005 (4-section structure), FR-017 (SVG ordering), and GitHub-Flavored Markdown best practices.

---

## Template Structure Overview

```
┌─ Section 1: Header (FR-005)
│  ├─ Title
│  ├─ Metadata (generated, version, repo count)
│  └─ Navigation links
├─ Section 2: Profile Overview (FR-005, FR-017)
│  ├─ Overview Dashboard SVG
│  ├─ Activity Visualizations (heatmap, streaks, release)
│  └─ Detail Breakdowns (languages, fun)
├─ Section 3: Repository Analysis (FR-005)
│  ├─ Top N Repositories heading
│  └─ Repository entries (ranked 1-50)
└─ Section 4: Footer (FR-005)
   ├─ Warning section (if errors)
   ├─ Report metadata
   ├─ Data sources
   └─ Attribution
```

---

## Section 1: Header

### Template

```markdown
# GitHub Profile: {username}

**Generated**: {timestamp_utc}
**Report Version**: {version}
**Repositories Analyzed**: {total_repos}
**AI Summary Rate**: {ai_summary_rate}%

> 💡 **Navigation**: [Profile Overview](#profile-overview) | [Top Repositories](#top-{N}-repositories) | [Metadata](#report-metadata)

---
```

### Field Bindings

| Field | Source | Format | Example |
|-------|--------|--------|---------|
| `{username}` | `UnifiedReport.username` | String | `markhazleton` |
| `{timestamp_utc}` | `UnifiedReport.timestamp` | `YYYY-MM-DD HH:MM:SS UTC` | `2025-12-30 12:00:00 UTC` |
| `{version}` | `UnifiedReport.version` | Semver | `1.0.0` |
| `{total_repos}` | `UnifiedReport.total_repos` | Integer | `48` |
| `{ai_summary_rate}` | `UnifiedReport.ai_summary_rate` | Float (1 decimal) | `95.8` |

### Constraints

- **Title**: Level 1 heading (`#`)
- **Metadata**: Bold labels with colon separator
- **Navigation**: Blockquote (`>`) with anchor links
- **Separator**: Three dashes (`---`)

---

## Section 2: Profile Overview

### Template

```markdown
## Profile Overview

### Activity Dashboard

![Overview Statistics](../overview.svg)

### Commit Activity

![Commit Heatmap](../heatmap.svg)

![Coding Streaks](../streaks.svg)

### Technology Breakdown

![Language Distribution](../languages.svg)

![Fun Statistics](../fun.svg)

### Release Patterns

![Release Cadence](../release.svg)

---
```

### SVG Embedding Rules (FR-017)

**Ordering** (strict):
1. Overview (dashboard)
2. Heatmap (activity)
3. Streaks (activity)
4. Release (activity)
5. Languages (breakdown)
6. Fun (breakdown)

**Syntax**:
```markdown
![{alt_text}](../{svg_filename}.svg)
```

**Fallback** (when SVG missing):
```markdown
*{name} visualization unavailable*
```

### Field Bindings

| Field | Source | Example |
|-------|--------|---------|
| SVG presence | `UnifiedReport.available_svgs` | `["overview", "languages"]` |
| SVG path | Relative from `/output/reports/` to `/output/` | `../overview.svg` |
| Alt text | SVG type capitalized | `"Overview Statistics"` |

### Constraints

- **Section heading**: Level 2 (`##`)
- **Subsection headings**: Level 3 (`###`)
- **Image syntax**: Markdown only (no HTML `<img>`)
- **Path format**: Relative (starts with `../`)
- **Blank lines**: One between subsections
- **Separator**: Three dashes after section

---

## Section 3: Repository Analysis

### Template

```markdown
## Top {N} Repositories

### #{rank}. [{repo_name}]({repo_url})

⭐ {stars} | 🔱 {forks} | 📝 {language} | 📊 {commits_90d} commits (90d)

👥 {contributors} contributors | 🌐 {language_count} languages | 💾 {size} | 🚀 {commits_per_month} commits/month

**Quality**: {quality_badges}

**Releases**: {release_count} | Latest: {latest_release_date} ({days_ago} days ago)

{ai_summary}

**Technology Stack Currency**: {tech_score}/100
**Dependencies**: {dep_total} total ({dep_current} current, {dep_outdated} outdated)

**Created**: {created_date} ({created_days_ago} days ago)
**Last Modified**: {updated_date} ({updated_relative})

---

[repeat for each repository 1-50]
```

### Field Bindings

| Field | Source | Format | Example |
|-------|--------|--------|---------|
| `{rank}` | Index in list | Integer | `1` |
| `{repo_name}` | `Repository.name` | String | `git-spark` |
| `{repo_url}` | `Repository.html_url` | URL | `https://github.com/...` |
| `{stars}` | `Repository.stargazers_count` | Integer | `42` |
| `{commits_90d}` | `CommitHistory.commits_last_90_days` | Integer | `81` |
| `{ai_summary}` | `RepositorySummary.content` | Multiline text | AI-generated paragraph |
| `{tech_score}` | `TechnologyStack.currency_score` | Integer 0-100 | `100` |

### Quality Badges Format

```markdown
✅ CI/CD | ✅ Tests | ✅ License | ✅ Docs
❌ CI/CD | ✅ Tests | ❌ License | ✅ Docs
```

### Constraints

- **Repository heading**: Level 3 with rank number
- **Inline stats**: Pipe-separated (`|`) with emoji indicators
- **Quality**: Bold label + emoji checklist
- **Separator**: Three dashes between repositories
- **Max count**: 50 repositories

---

## Section 4: Footer

### Template

```markdown
---

[Warning Section - only if errors/warnings exist]
## ⚠️ Generation Warnings

{error_list}

---

## Report Metadata

- **Generation Time**: {generation_time} seconds
- **SVGs Generated**: {svg_count}/6
- **Total API Calls**: {api_calls}
- **Total AI Tokens**: {ai_tokens}
- **Success Rate**: {success_rate}%

### Data Sources

- GitHub API (public repositories only)
- Anthropic Claude API (repository summaries)
- Dependency package registries (npm, PyPI, RubyGems, Go, Maven, NuGet)

### Report Details

- **Composite Score Weights**: Popularity 30% • Activity 45% • Health 25%
- **Technology Currency**: Calculated from latest versions in package registries
- **AI Model**: {ai_model}

---

*Generated by [Stats Spark](https://github.com/markhazleton/github-stats-spark)*
*Last updated: {timestamp_date}*
```

### Field Bindings

| Field | Source | Format |
|-------|--------|--------|
| `{error_list}` | `UnifiedReport.errors + warnings` | Markdown list |
| `{generation_time}` | `UnifiedReport.generation_time` | Float (1 decimal) |
| `{svg_count}` | `len(UnifiedReport.available_svgs)` | Integer |
| `{api_calls}` | `UnifiedReport.total_api_calls` | Integer |
| `{ai_tokens}` | `UnifiedReport.total_ai_tokens` | Integer (comma-separated) |
| `{success_rate}` | `UnifiedReport.success_rate` | Float (1 decimal) |
| `{ai_model}` | `UnifiedReport.ai_model` | String or "N/A" |
| `{timestamp_date}` | `UnifiedReport.timestamp` | `YYYY-MM-DD` |

### Warning Section Logic

```python
if report.errors or report.warnings:
    # Show warning section
    error_items = report.errors + report.warnings
    limited_errors = error_items[:5]  # Show max 5
    if len(error_items) > 5:
        limited_errors.append("... and {len(error_items) - 5} more")
```

---

## GitHub-Flavored Markdown (GFM) Compliance

### Required Features

✅ **Supported**:
- Headings (ATX-style `#`)
- Emphasis (`**bold**`, `*italic*`)
- Lists (unordered `-`, ordered `1.`)
- Links (`[text](url)`)
- Images (`![alt](path)`)
- Blockquotes (`>`)
- Horizontal rules (`---`)
- Emoji shortcodes (`:star:` → ⭐)
- Tables (pipe-separated)

❌ **Not Used** (compatibility):
- HTML tags (sanitized by GitHub)
- Task lists (`- [ ]`) - use regular lists
- Inline SVG code (stripped by GitHub)
- Custom heading IDs (`{#custom}`) - use auto-generated

### Encoding

- **File encoding**: UTF-8 with BOM optional
- **Line endings**: LF (`\n`) preferred, CRLF accepted
- **Character set**: Full Unicode support

---

## Validation Schema

### Structural Validation

```python
def validate_markdown_structure(markdown: str) -> List[str]:
    """Validate markdown structure against schema."""
    errors = []

    # Section 1: Header
    if not markdown.startswith("# GitHub Profile:"):
        errors.append("Missing header section")
    if "**Generated**:" not in markdown:
        errors.append("Missing timestamp metadata")

    # Section 2: Profile Overview
    if "## Profile Overview" not in markdown:
        errors.append("Missing profile overview section")

    # Section 3: Repository Analysis
    if not any(f"## Top {n} Repositories" in markdown for n in range(1, 51)):
        errors.append("Missing repository analysis section")

    # Section 4: Footer
    if "## Report Metadata" not in markdown:
        errors.append("Missing footer metadata section")

    # Section ordering (FR-005)
    sections = [
        markdown.index("# GitHub Profile:"),
        markdown.index("## Profile Overview"),
        markdown.index("## Top"),  # Repository heading
        markdown.index("## Report Metadata"),
    ]
    if sections != sorted(sections):
        errors.append("Sections out of order (violates FR-005)")

    return errors
```

---

## Size Estimation

| Section | Estimated Size |
|---------|---------------|
| Header | ~600 bytes |
| Profile Overview | ~1.2 KB (6 SVG refs + formatting) |
| Repository Analysis | ~200 KB (50 × ~4KB average) |
| Footer | ~1.5 KB |
| **Total Estimate** | **~203 KB** |

**Maximum**: ~400 KB with long AI summaries (well under 1MB SC-002 constraint)

---

## Example Output

See [Example Unified Report](../examples/markhazleton-analysis-example.md) (to be generated during testing).

---

## Summary

**Schema Type**: Structured markdown template with variable substitution

**Validation**: Structural (section presence + ordering) + size constraints

**Compliance**:
- FR-005 ✅ (4-section structure)
- FR-017 ✅ (SVG ordering)
- SC-002 ✅ (<1MB file size)

**Next**: See [quickstart.md](../quickstart.md) for usage guide.
