# Implementation Plan: AI-Powered GitHub Repository Summary Report

**Branch**: `001-ai-repo-summary` | **Date**: 2025-12-28 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-ai-repo-summary/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Create an AI-powered analysis tool that generates comprehensive markdown reports of a GitHub user's top 50 public repositories. The report includes per-repository summaries (generated from README and commit history), technology stack identification with currency assessment, repository statistics, and an overall developer profile analysis. The feature extends the existing Stats Spark project with new analysis modules while maintaining the constitution's Python-first, CLI-accessible, and privacy-focused architecture.

## Technical Context

**Language/Version**: Python 3.11+ (current codebase uses 3.11-3.14)
**Primary Dependencies**: PyGithub (2.1.1+), PyYAML (6.0.1+), requests (2.31.0+), anthropic (0.40.0+), tenacity (9.0.0+), packaging (23.0+), tomli (2.0.0+ for Python <3.11)
**AI/LLM Provider**: Anthropic Claude Haiku via API with template fallback (decision: research.md §1)
**Dependency Registries**: Direct API access to NPM, PyPI, RubyGems, Go Proxy, Maven Central with 7-day file cache + in-memory cache (decision: research.md §2)
**Storage**: File-based (markdown reports, JSON cache via existing APICache)
**Testing**: pytest (existing infrastructure in constitution)
**Target Platform**: Cross-platform CLI (Windows, Linux, macOS) + GitHub Actions workflow
**Project Type**: Single project (extends existing src/spark/ module structure)
**Performance Goals**: <3 minutes for 50 repositories with standard commit histories (<1000 commits each)
**Constraints**: GitHub API rate limits (60 unauthenticated, 5000 authenticated requests/hour), report size <5MB, must work with existing 6-hour cache TTL
**Scale/Scope**: Analyze 1-200+ public repositories per user, process complete commit histories, generate reports with AI summaries for each repo

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### I. Python-First ✅ PASS
- **Requirement**: Core functionality as importable Python modules with clear separation of concerns
- **Compliance**: Feature will add new modules following existing pattern:
  - `ranker.py` - Repository ranking algorithm (composite scoring)
  - `summarizer.py` - AI-powered summary generation (repositories + user profiles)
  - `dependencies/parser.py` - Dependency file parsing (NPM, PyPI, RubyGems, Go, Maven)
  - `dependencies/version_checker.py` - Registry API clients with hybrid caching
  - `dependencies/analyzer.py` - Technology stack currency assessment
  - `report_generator.py` - Markdown report formatting
  - All modules will be independently testable and importable

### II. CLI Interface ✅ PASS
- **Requirement**: All functionality accessible via CLI
- **Compliance**: Will extend existing `src/spark/cli.py` with new commands:
  - `spark analyze --user <username> --output <path>` - Generate repository analysis report
  - `spark analyze --list-only` - Show top 50 repos without generating report (dry-run)
  - Compatible with GitHub Actions execution via `src/main.py`

### III. Data Privacy ⚠️ REQUIRES ATTENTION
- **Requirement**: ONLY process public repositories, NO private data
- **Compliance**:
  - Feature spec explicitly states "public repositories only" (FR-001, FR-015)
  - MUST implement explicit filter in analyzer.py to reject private repos
  - MUST validate in tests that private repos are never processed
  - **ACTION**: Add explicit privacy validation in Phase 1 design

### IV. Testability ✅ PASS
- **Requirement**: Unit tests for all calculation logic, integration tests with mock data
- **Compliance**:
  - Ranking algorithm (FR-002) will have deterministic test cases
  - AI summary generation will use mock responses in tests
  - Dependency currency checks will use fixture data
  - **Coverage target**: >80% for analyzer, summarizer, dependency_checker modules

### V. Observable ✅ PASS
- **Requirement**: All operations log to stdout/stderr with timestamps and context
- **Compliance**:
  - Feature spec FR-018 requires progress indicators (current repo + percentage)
  - Will use existing `spark.logger.get_logger()` infrastructure
  - Error messages will include actionable guidance (e.g., rate limit handling per FR-014, FR-019)

### Performance & Scalability Standards ⚠️ ATTENTION REQUIRED

**API Rate Limiting** ✅ PASS
- Requirement: 6-hour cache TTL, force-refresh flag, exponential backoff
- Compliance: Will reuse existing `spark.cache.APICache` and error handling

**Execution Time** ⚠️ CLARIFICATION NEEDED
- Requirement: <5 minutes for 500 repos (constitution) vs. <3 minutes for 50 repos (spec SC-001)
- Resolution: Spec SC-001 is MORE restrictive but only for 50 repos. Constitution applies to full analysis.
- **STATUS**: Compatible - 50-repo analysis is subset of 500-repo performance budget

**Accuracy** ⚠️ NEW METRIC
- Requirement: <1% discrepancy vs GitHub native insights (constitution)
- New metrics: AI summary accuracy (SC-002: 90%), tech stack identification (SC-003: 95%)
- **STATUS**: New metrics, not in conflict with existing accuracy requirements

### Configuration & Customization ✅ PASS
- **Requirement**: YAML-based configuration, theme compliance
- **Compliance**: Report generation does not require themes (text-only markdown), will use existing `config/spark.yml` for user/token settings

### GATE EVALUATION: ⚠️ CONDITIONAL PASS

**Blockers**: NONE

**Action Items Before Phase 0**:
1. ✅ Privacy validation strategy defined (explicit public-only filter)
2. ✅ **RESOLVED**: AI/LLM integration approach - Anthropic Claude Haiku with three-tier fallback (Primary: Claude API, Fallback 1: Enhanced template from README, Fallback 2: Basic template from metadata only). Cost: ~$0.20/50 repos. See research.md §1 for rationale.
3. ✅ **RESOLVED**: Dependency version checking - Direct registry APIs (NPM, PyPI, RubyGems, Go Proxy, Maven Central) with hybrid caching (7-day file cache + in-memory). No authentication required. 95% repository coverage. See research.md §2 for implementation details.

**Status**: ✅ APPROVED - All clarifications resolved via Phase 0 research

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
src/spark/
├── __init__.py
├── cache.py              # Existing - API response caching
├── calculator.py         # Existing - Statistics calculations
├── cli.py                # EXTEND - Add 'analyze' command
├── config.py             # Existing - Configuration management
├── fetcher.py            # EXTEND - Add time-windowed commit counts (90d/180d/365d)
├── logger.py             # Existing - Logging infrastructure
├── visualizer.py         # Existing - SVG generation (not used by this feature)
├── ranker.py             # NEW - Repository ranking algorithm
├── summarizer.py         # NEW - AI-powered summary generation
├── report_generator.py   # NEW - Markdown report formatting
├── models/               # NEW - Data model classes
│   ├── __init__.py
│   ├── repository.py     # Repository entity
│   ├── commit.py         # CommitHistory entity
│   ├── tech_stack.py     # TechnologyStack entity
│   ├── summary.py        # RepositorySummary entity
│   ├── profile.py        # UserProfile entity
│   └── report.py         # Report entity
├── dependencies/         # NEW - Technology stack analysis
│   ├── __init__.py
│   ├── parser.py         # Dependency file parsing
│   ├── version_checker.py # Registry API clients
│   └── analyzer.py       # Currency assessment logic
└── themes/               # Existing - Theme definitions (not used by this feature)

tests/
├── fixtures/
│   ├── sample_user_data.json          # Existing - Mock GitHub API responses
│   ├── sample_repositories.json       # NEW - Mock repository data for ranker
│   ├── sample_readmes/                # NEW - Sample README files
│   ├── sample_dependency_files/       # NEW - package.json, requirements.txt, etc.
│   └── ranking_scenarios.json         # NEW - Ranking algorithm test cases
├── unit/
│   ├── test_ranker.py                 # NEW - Repository ranking tests
│   ├── test_summarizer.py             # NEW - AI summary generation tests
│   ├── test_dependency_parser.py      # NEW - Dependency file parsing tests
│   ├── test_version_checker.py        # NEW - Registry API client tests
│   └── test_report_generator.py       # NEW - Markdown formatting tests
└── integration/
    ├── test_full_report_generation.py # NEW - End-to-end report generation
    ├── test_summarizer_fallback.py    # NEW - AI fallback scenarios
    └── test_dependency_analysis.py    # NEW - Full dependency analysis

output/
└── reports/              # NEW - Generated repository analysis reports

config/
└── spark.yml             # EXTEND - Add analyzer configuration options
```

**Structure Decision**: Single project structure (Option 1) is used. This feature extends the existing Stats Spark codebase by adding:
- **3 core modules**: `ranker.py`, `summarizer.py`, `report_generator.py`
- **1 models directory**: 6 entity classes for data structures
- **1 dependencies subdirectory**: 3 modules for technology stack analysis (parser, version_checker, analyzer)
- **Extended modules**: `fetcher.py` (time-windowed commits), `cli.py` (analyze command)

The modular structure maintains constitution compliance (single-responsibility modules) while organizing related functionality logically.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution violations detected. All gates passed or have documented action items for resolution during Phase 0 research.
