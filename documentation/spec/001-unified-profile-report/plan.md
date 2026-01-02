# Implementation Plan: Unified Profile Report

**Branch**: `001-unified-profile-report` | **Date**: 2025-12-30 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/docs/spec/001-unified-profile-report/spec.md`

## Summary

Consolidate the dual-output system (SVG visualizations + dated markdown reports) into a single, comprehensive, non-dated profile report at `/output/reports/{username}-analysis.md`. The unified report will combine all six SVG visualizations with detailed analysis of the top 50 repositories, structured as: Header/Metadata → Profile Overview (embedded SVGs) → Repository Analysis → Footer. This consolidation eliminates manual coordination between two separate generation workflows and provides a single, linkable resource for GitHub profile pages that automatically updates weekly.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: PyGithub 2.1.1+, svgwrite 1.4.3+, anthropic 0.40.0+, tenacity 9.0.0+
**Storage**: File-based (SVG files in `/output/`, markdown reports in `/output/reports/`, API cache in `.cache/`)
**Testing**: pytest 7.4.0+ with pytest-cov for coverage, unit + integration test suites
**Target Platform**: GitHub Actions (Python 3.11, GitHub-hosted runners) + local CLI
**Project Type**: Single Python package with CLI interface
**Performance Goals**: Complete workflow within 10 minutes for users with up to 200 repositories
**Constraints**: <1MB markdown file size, 5,000 GitHub API requests/hour limit, <500KB per SVG, <5 min generation time
**Scale/Scope**: Single user per workflow execution, up to 200 repositories analyzed, top 50 included in report

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Compliance Assessment

| Principle | Status | Evidence/Notes |
|-----------|--------|----------------|
| **I. Python-First** | ✅ PASS | Feature consolidates existing Python modules (calculator.py, visualizer.py, ranker.py, report_generator.py, summarizer.py) - all business logic already modular and testable |
| **II. CLI Interface** | ✅ PASS | Will extend existing `spark` CLI with unified generation mode (leverages existing `analyze` and `generate` commands) - maintains local testability |
| **III. Data Privacy** | ✅ PASS | Explicitly limited to public repositories only (FR-001 to FR-017, spec Out of Scope) - no private repo data processing |
| **IV. Testability** | ⚠️ REVIEW | Need to add integration tests for unified report generation combining both workflows - existing unit tests cover components |
| **V. Observable** | ✅ PASS | FR-014 requires comprehensive logging for all generation steps - extends existing logger.py infrastructure |
| **API Rate Limiting** | ✅ PASS | Existing 6-hour cache + exponential backoff already implemented - FR-016 adds workflow-level retry (1 min, 5 min, 15 min) |
| **Execution Time** | ✅ PASS | SC-002 requires <10 min for 200 repos (existing system completes in <5 min for 500 repos) - consolidation expected to improve efficiency |
| **Configuration** | ✅ PASS | Will extend existing config/spark.yml - no new configuration paradigm needed |
| **Theme Requirements** | ✅ PASS | Reuses existing WCAG AA compliant SVG themes - no changes to visualization layer |

**Overall Status**: ✅ **PASS** with one REVIEW item (IV. Testability)

**Notes**:
- The ⚠️ REVIEW on Testability is not a blocker - it's a new requirement for Phase 1 (add integration test for unified workflow)
- All other principles are met by design - this is a consolidation of existing compliant systems
- No constitution violations or complexity justification needed

## Project Structure

### Documentation (this feature)

```text
docs/spec/001-unified-profile-report/
├── plan.md              # This file
├── research.md          # Phase 0: Consolidation patterns, report templating approaches
├── data-model.md        # Phase 1: UnifiedReport entity + markdown template structure
├── quickstart.md        # Phase 1: How to generate unified reports (CLI + workflow)
├── contracts/           # Phase 1: UnifiedReportGenerator interface, markdown template schemas
│   ├── unified_report_generator.md
│   └── markdown_template_schema.md
└── tasks.md             # Phase 2: NOT created by /speckit.plan
```

### Source Code (repository root)

```text
src/spark/
├── __init__.py
├── cache.py                    # Existing - API caching (6-hour TTL)
├── calculator.py               # Existing - Stats calculation
├── cli.py                      # MODIFY - Add unified report generation command
├── config.py                   # Existing - YAML configuration
├── fetcher.py                  # Existing - GitHub API client
├── logger.py                   # Existing - Logging utilities
├── ranker.py                   # Existing - Repository ranking
├── report_generator.py         # EXTEND - Add unified report templating
├── summarizer.py               # Existing - AI-powered summaries
├── visualizer.py               # Existing - SVG generation
├── unified_report_generator.py # NEW - Markdown templating and report generation
├── unified_report_workflow.py  # NEW - Orchestrates unified report workflow execution
├── dependencies/               # Existing - Dependency analysis
│   ├── __init__.py
│   ├── analyzer.py
│   ├── parser.py
│   └── version_checker.py
├── models/                     # Existing - Data entities
│   ├── __init__.py
│   ├── commit.py
│   ├── profile.py
│   ├── report.py               # EXTEND - Add UnifiedReport entity
│   ├── repository.py
│   ├── summary.py
│   └── tech_stack.py
└── themes/                     # Existing - SVG themes
    ├── __init__.py
    ├── spark_dark.py
    ├── spark_light.py
    └── custom.py

src/main.py                     # MODIFY - Add "unified" command mode

tests/
├── unit/
│   ├── test_unified_report_generator.py  # NEW
│   └── [existing unit tests]
└── integration/
    ├── test_unified_workflow.py          # NEW - End-to-end unified report generation
    └── [existing integration tests]

.github/workflows/
└── generate-stats.yml          # MODIFY - Update to run unified report generation

config/
├── spark.yml                   # MODIFY - Add unified report configuration section
└── themes.yml                  # Existing - No changes

output/
├── *.svg                       # Existing - Generated SVGs (non-dated)
└── reports/
    ├── {username}-analysis.md           # NEW - Unified report (non-dated)
    └── {username}-analysis-{YYYYMMDD}.md  # Existing - Dated reports (preserved)
```

**Structure Decision**: This is a **single Python project** (src/spark/ package) with CLI interface. The consolidation adds one new module (`unified_report_generator.py`), extends two existing modules (`report_generator.py` for templating, `cli.py` for commands), modifies the workflow entry point (`src/main.py`), updates the GitHub Actions workflow, and adds two new test modules for comprehensive validation. No architectural changes needed - leverages existing modular structure.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

**Status**: No violations to justify - all gates pass.

---

## Phase 0: Outline & Research

**Status**: ✅ Complete

### Research Tasks

1. **Markdown Report Templating Approaches**
   - **Question**: How should we structure the markdown template for the unified report to support dynamic SVG embedding and repository analysis sections?
   - **Research Focus**:
     - Jinja2-style templating vs. direct Python string formatting
     - Section ordering and modularity
     - SVG image reference patterns (relative paths, markdown syntax)
     - Fallback strategies for missing SVGs or failed analysis

2. **Workflow Orchestration Pattern**
   - **Question**: What is the optimal orchestration pattern for combining SVG generation + repository analysis into a single unified workflow?
   - **Research Focus**:
     - Sequential execution (SVGs first, then analysis) vs. parallel execution with result aggregation
     - Error handling and partial failure recovery (FR-011, FR-012)
     - Data sharing between components (shared cache, in-memory objects)
     - Retry logic integration (FR-016: exponential backoff at workflow level)

3. **Report Structure Best Practices**
   - **Question**: What are industry best practices for structured markdown reports combining visualizations and data tables?
   - **Research Focus**:
     - GitHub-flavored markdown conventions
     - SVG embedding patterns for maximum compatibility
     - Table formatting for repository analysis
     - Metadata header/footer patterns
     - Accessibility considerations for screen readers

4. **Backward Compatibility Strategy**
   - **Question**: How do we ensure existing dated reports remain functional while introducing the non-dated unified report?
   - **Research Focus**:
     - File naming conventions to prevent collisions
     - Dual-mode operation (preserve `analyze` command for dated reports, add new `unified` mode)
     - Configuration migration path
     - Testing strategy to validate both old and new outputs

**Output**: [research.md](research.md) - To be generated in next step

---

## Phase 1: Design & Contracts

**Status**: ✅ Complete

### Deliverables

1. **data-model.md**: UnifiedReport entity specification
   - Extends existing Report model
   - Includes: header metadata, SVG references, repository analysis section, footer
   - Relationships to existing entities (Repository, RepositoryAnalysis, SVG paths)
   - Validation rules for FR-001 through FR-017

2. **contracts/unified_report_generator.md**: UnifiedReportGenerator interface
   - Core method: `generate_unified_report(username: str) -> UnifiedReport`
   - Dependencies: GitHubFetcher, StatsCalculator, StatisticsVisualizer, RepositoryRanker, RepositorySummarizer, ReportGenerator
   - Error handling contracts (partial failures, retry logic)
   - Return type specifications

3. **contracts/markdown_template_schema.md**: Markdown template structure
   - Section 1: Header (metadata fields, generation timestamp)
   - Section 2: Profile Overview (SVG embedding pattern, ordering per FR-017)
   - Section 3: Repository Analysis (table structure, ranking display, metrics format)
   - Section 4: Footer (data sources, generation info)
   - Fallback content for missing/failed components

4. **quickstart.md**: User guide for unified report generation
   - CLI usage: `spark unified --user <username>`
   - GitHub Actions workflow configuration
   - Configuration options in config/spark.yml
   - Troubleshooting common issues
   - Output verification steps

### Agent Context Update

- Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType claude`
- Add new technology: "Unified markdown report templating with embedded SVGs"
- Preserve existing technologies: PyGithub, svgwrite, anthropic, pytest

---

## Phase 2: Task Generation

**Status**: Pending (requires Phase 1 completion)

**Note**: Task generation is handled by `/speckit.tasks` command, not by `/speckit.plan`.

---

## Gates & Checkpoints

### Pre-Phase 0 (Before Research)
- ✅ Constitution Check passed
- ✅ Technical Context filled (all fields resolved)
- ✅ No complexity violations to justify

### Pre-Phase 1 (Before Design)
- ✅ research.md completed with all 4 research tasks resolved
- ✅ No new NEEDS CLARIFICATION markers introduced
- ✅ Consolidation approach selected and documented

### Post-Phase 1 (After Design)
- ✅ data-model.md validates against FR-001 to FR-017
- ✅ contracts/ define testable interfaces (unified_report_generator.md, markdown_template_schema.md)
- ✅ quickstart.md provides clear user guidance
- ✅ Re-run Constitution Check - IV. Testability addressed (new integration tests specified)
- ✅ Agent context updated with new technologies (CLAUDE.md created)

### Pre-Phase 2 (Before Task Generation)
- ⏳ All Phase 1 artifacts validated
- ⏳ No unresolved design questions
- ⏳ Ready for `/speckit.tasks` command

---

## Planning Complete ✅

**Status**: All Phase 0 and Phase 1 deliverables completed

**Generated Artifacts**:
- ✅ [plan.md](plan.md) - This file (implementation plan)
- ✅ [research.md](research.md) - Research findings for 4 key decisions
- ✅ [data-model.md](data-model.md) - UnifiedReport entity + validation
- ✅ [contracts/unified_report_generator.md](contracts/unified_report_generator.md) - Generator interface contract
- ✅ [contracts/markdown_template_schema.md](contracts/markdown_template_schema.md) - Markdown structure specification
- ✅ [quickstart.md](quickstart.md) - User guide for unified report generation
- ✅ CLAUDE.md - Agent context file (technologies documented)

**Next Step**: Run `/speckit.tasks` to generate implementation tasks from this plan
