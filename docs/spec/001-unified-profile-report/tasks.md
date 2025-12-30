# Tasks: Unified Profile Report

**Input**: Design documents from `/docs/spec/001-unified-profile-report/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Tests are NOT explicitly requested in the specification, so test tasks are marked OPTIONAL below. Implement if desired for TDD approach.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `- [ ] [ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3, US4)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization - verify existing infrastructure is ready

- [X] T001 Verify Python 3.11+ environment and existing dependencies (PyGithub, svgwrite, anthropic, tenacity, pytest)
- [X] T002 [P] Verify existing project structure matches plan.md (src/spark/, tests/, config/, output/)
- [X] T003 [P] Review existing modules to understand integration points (calculator.py, visualizer.py, ranker.py, report_generator.py, summarizer.py)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core entities and infrastructure that ALL user stories depend on

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create WorkflowError exception class in src/spark/exceptions.py
- [X] T005 [P] Create GitHubData dataclass in src/spark/models/github_data.py
- [X] T006 [P] Create UnifiedReport entity in src/spark/models/report.py (extend existing Report)
- [X] T007 Update src/spark/models/__init__.py to export GitHubData, UnifiedReport, WorkflowError
- [X] T008 [P] Create UnifiedReportWorkflow class skeleton in src/spark/unified_report_workflow.py
- [X] T009 [P] Create UnifiedReportGenerator class skeleton in src/spark/unified_report_generator.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Automated Weekly Profile Report Generation (Priority: P1) 🎯 MVP

**Goal**: Generate a single, non-dated unified report combining SVG visualizations and top 50 repository analysis, automatically updated weekly

**Independent Test**: Trigger workflow manually, verify `/output/reports/{username}-analysis.md` exists with both SVG references and repository analysis. File should be <1MB, contain all 4 sections per FR-005.

### Tests for User Story 1 (OPTIONAL) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Unit test for UnifiedReportWorkflow.execute() in tests/unit/test_unified_report_workflow.py
- [ ] T011 [P] [US1] Integration test for end-to-end unified report generation in tests/integration/test_unified_workflow.py

### Implementation for User Story 1

**T012-T020: Workflow Orchestration (Sequential Data Pipeline)**

- [ ] T012 [US1] Implement UnifiedReportWorkflow._fetch_github_data() with retry logic in src/spark/unified_report_workflow.py
- [ ] T013 [US1] Implement UnifiedReportWorkflow._generate_svgs() with partial failure handling in src/spark/unified_report_workflow.py
- [ ] T014 [US1] Implement UnifiedReportWorkflow._analyze_repositories() with individual repo error handling in src/spark/unified_report_workflow.py
- [ ] T015 [US1] Implement UnifiedReportWorkflow._generate_unified_report() orchestration method in src/spark/unified_report_workflow.py
- [ ] T016 [US1] Implement UnifiedReportWorkflow.execute() main entry point with error/warning collection in src/spark/unified_report_workflow.py
- [ ] T017 [US1] Add comprehensive logging to all workflow stages in src/spark/unified_report_workflow.py
  <!-- NOTE: Use structured logging format: "[timestamp] [LEVEL] [stage] message". Example: "[2025-12-30T10:15:22Z] [INFO] [fetch_github_data] Fetching user profile for markhazleton". Ensure all log messages include context (username, repo count, API rate limit status) per FR-014 observable requirements. -->
- [ ] T018 [US1] Implement exponential backoff retry decorator (1min, 5min, 15min) for GitHub API calls in src/spark/unified_report_workflow.py
  <!-- NOTE: This implements workflow-level retry (FR-016). API-level retry (1s, 2s, 4s, 8s per constitution) is handled separately by existing fetcher.py. Two-layer retry strategy: fast retries for transient errors (API layer), slow retries for rate limits (workflow layer). -->
- [ ] T019 [US1] Add workflow execution time tracking and success rate calculation in src/spark/unified_report_workflow.py
- [ ] T020 [US1] Handle edge cases: no repos, <50 repos, API rate limits, SVG generation failures in src/spark/unified_report_workflow.py

**T021-T028: Report Generation (Markdown Templating)**

- [ ] T021 [P] [US1] Implement UnifiedReportGenerator._generate_header() with metadata in src/spark/unified_report_generator.py
- [ ] T022 [P] [US1] Implement UnifiedReportGenerator._generate_profile_overview() with SVG embedding in src/spark/unified_report_generator.py
- [ ] T023 [P] [US1] Implement UnifiedReportGenerator._generate_repository_analysis() with top 50 formatting in src/spark/unified_report_generator.py
- [ ] T024 [P] [US1] Implement UnifiedReportGenerator._generate_footer() with metadata and warnings in src/spark/unified_report_generator.py
- [ ] T025 [US1] Implement UnifiedReportGenerator._embed_svg() helper with fallback for missing SVGs in src/spark/unified_report_generator.py
- [ ] T026 [US1] Implement UnifiedReportGenerator._format_repository_entry() reusing existing ReportGenerator logic in src/spark/unified_report_generator.py
- [ ] T027 [US1] Implement UnifiedReportGenerator.generate_markdown() main method in src/spark/unified_report_generator.py
- [ ] T028 [US1] Implement UnifiedReportGenerator.generate_report() with file write and size validation in src/spark/unified_report_generator.py

**T029-T033: CLI Integration**

- [ ] T029 [US1] Add --unified flag to analyze command argument parser in src/spark/cli.py
- [ ] T030 [US1] Add --keep-dated flag for dual-output mode in src/spark/cli.py
- [ ] T031 [US1] Implement handle_unified_analyze() function in src/spark/cli.py
- [ ] T032 [US1] Update handle_analyze() to route to unified vs dated mode based on flags in src/spark/cli.py
- [ ] T033 [US1] Add unified mode logging and progress indicators in src/spark/cli.py

**T034-T037: GitHub Actions Workflow**

- [ ] T034 [US1] Update .github/workflows/generate-stats.yml to use --unified flag
- [ ] T035 [US1] Add workflow_dispatch input for report_mode (unified/dated/both) in .github/workflows/generate-stats.yml
- [ ] T036 [US1] Update git commit step to include {username}-analysis.md in .github/workflows/generate-stats.yml
- [ ] T037 [US1] Test workflow trigger manually via GitHub Actions UI

**T038-T040: Configuration & Validation**

- [ ] T038 [US1] Add unified report settings to config/spark.yml (svg_order, fallback_on_missing_svg, etc.)
- [ ] T039 [US1] Validate UnifiedReport entity structure against FR-001 to FR-017 requirements (section ordering, file paths, size limits) in src/spark/models/report.py
  <!-- NOTE: This validates the entity STRUCTURE. T048 validates SVG ordering specifically per FR-017. Different validation scopes. -->
- [ ] T040 [US1] Test complete User Story 1 flow: CLI → Workflow → SVGs → Analysis → Unified Report
- [ ] T040b [US1] Performance validation checkpoint: Test with user having 200 repos, verify completion <10 min (SC-002) and output file <1MB (SC-001)

**Checkpoint**: At this point, User Story 1 should be fully functional - unified reports auto-generate weekly with both SVGs and analysis

---

## Phase 4: User Story 2 - Embedded SVG Visualizations in Report (Priority: P2)

**Goal**: Ensure SVG visualizations render inline within the markdown report with proper relative paths for cross-platform compatibility

**Independent Test**: Open generated `{username}-analysis.md` in GitHub, VSCode, and local markdown viewer. All 6 SVGs should display inline without broken links.

### Tests for User Story 2 (OPTIONAL) ⚠️

- [ ] T041 [P] [US2] Unit test for SVG embedding logic in tests/unit/test_unified_report_generator.py
- [ ] T042 [P] [US2] Integration test for cross-platform markdown rendering in tests/integration/test_svg_rendering.py

### Implementation for User Story 2

- [ ] T043 [P] [US2] Implement FR-017 SVG ordering (overview, heatmap, streaks, release, languages, fun) in src/spark/unified_report_generator.py
- [ ] T044 [P] [US2] Add SVG subsection headings (Activity Dashboard, Commit Activity, Technology Breakdown, Release Patterns) in src/spark/unified_report_generator.py
- [ ] T045 [US2] Verify relative path calculation (../overview.svg from /output/reports/) in src/spark/unified_report_generator.py
- [ ] T046 [US2] Add SVG availability check with graceful fallback text in src/spark/unified_report_generator.py
- [ ] T047 [US2] Test SVG rendering on GitHub.com, VSCode preview, local markdown viewers, AND test embedding in GitHub profile README (create test profile repo, link to unified report, verify SVGs display correctly)
- [ ] T048 [US2] Update UnifiedReport.validate() to check SVG ordering matches FR-017 in src/spark/models/report.py

**Checkpoint**: SVG visualizations now embedded correctly with proper structure and ordering

---

## Phase 5: User Story 3 - Repository Analysis Integration (Priority: P1)

**Goal**: Include detailed analysis of top 50 repositories with rankings, technology stacks, and quality metrics in the unified report

**Independent Test**: Verify unified report contains repository analysis section with exactly 50 repos (or all if <50), each showing composite score, tech stack, activity metrics, and AI summary (or template fallback).

### Tests for User Story 3 (OPTIONAL) ⚠️

- [ ] T049 [P] [US3] Unit test for repository ranking and scoring in tests/unit/test_repository_ranking.py
- [ ] T050 [P] [US3] Integration test for top 50 repository analysis workflow in tests/integration/test_repository_analysis.py

### Implementation for User Story 3

- [ ] T051 [P] [US3] Verify existing RepositoryRanker uses correct weights (popularity 30%, activity 45%, health 25%) in src/spark/ranker.py
- [ ] T052 [P] [US3] Verify existing RepositorySummarizer supports AI fallback to templates in src/spark/summarizer.py
- [ ] T053 [US3] Integrate RepositoryRanker into UnifiedReportWorkflow._analyze_repositories() in src/spark/unified_report_workflow.py
- [ ] T054 [US3] Integrate RepositorySummarizer for each repo in analysis in src/spark/unified_report_workflow.py
- [ ] T055 [US3] Integrate RepositoryDependencyAnalyzer for tech stack currency in src/spark/unified_report_workflow.py
- [ ] T056 [US3] Format repository entries with composite score, rank, metrics, tech stack in src/spark/unified_report_generator.py
- [ ] T057 [US3] Add quality badges (CI/CD, Tests, License, Docs) formatting in src/spark/unified_report_generator.py
- [ ] T058 [US3] Handle edge case: users with <50 repos (show all available) in src/spark/unified_report_workflow.py
- [ ] T059 [US3] Handle edge case: users with 0 repos (SVGs only, note in report) in src/spark/unified_report_workflow.py
- [ ] T060 [US3] Validate repository analysis section structure matches contract schema in src/spark/unified_report_generator.py

**Checkpoint**: Repository analysis now fully integrated with rankings, tech stacks, and quality indicators

---

## Phase 6: User Story 4 - Manual and Workflow-Triggered Generation (Priority: P3)

**Goal**: Support both manual CLI execution and automated GitHub Actions workflow triggering with consistent output

**Independent Test**: Run `spark analyze --user testuser --unified` locally, then trigger workflow via GitHub Actions. Compare outputs - they should be structurally identical.

### Tests for User Story 4 (OPTIONAL) ⚠️

- [ ] T061 [P] [US4] Integration test for manual CLI execution in tests/integration/test_cli_unified.py
- [ ] T062 [P] [US4] Integration test for workflow dispatch trigger in tests/integration/test_workflow_dispatch.py

### Implementation for User Story 4

- [ ] T063 [P] [US4] Add environment variable support for SPARK_COMMAND=unified in src/main.py
- [ ] T064 [P] [US4] Update src/main.py to support unified report mode alongside existing generate/analyze modes
- [ ] T065 [US4] Add CLI help text and examples for --unified flag in src/spark/cli.py
- [ ] T066 [US4] Add validation: reject --unified with incompatible flags (if any) in src/spark/cli.py
- [ ] T067 [US4] Test manual execution: `python -m spark.cli analyze --user markhazleton --unified --verbose`
- [ ] T068 [US4] Test workflow dispatch trigger via GitHub Actions UI
- [ ] T069 [US4] Test scheduled cron trigger (Sunday midnight UTC) by adjusting schedule temporarily
- [ ] T070 [US4] Verify output consistency across manual/scheduled/dispatch triggers

**Checkpoint**: Unified report generation works reliably via all trigger mechanisms (CLI, workflow_dispatch, cron schedule)

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and finalize the feature

- [ ] T071 [P] Update README.md with unified report usage examples
- [ ] T072 [P] Update CHANGELOG.md with v2.0.0 feature addition (unified reports)
- [ ] T073 [P] Add example unified report to docs/spec/001-unified-profile-report/examples/
- [ ] T074 Validate quickstart.md instructions by following guide end-to-end
- [ ] T075 [P] Add unit tests for UnifiedReport.validate() in tests/unit/test_unified_report.py
- [ ] T076 [P] Add unit tests for GitHubData entity in tests/unit/test_github_data.py
- [ ] T077 [P] Add unit tests for WorkflowError exception in tests/unit/test_exceptions.py
- [ ] T078 Code cleanup: Remove debug logging, ensure consistent error messages
- [ ] T079 Performance test: Generate report for user with 200 repos, verify <10 min completion
- [ ] T080 File size validation: Verify all generated reports <1MB (SC-002)
- [ ] T081 [P] Security review: Verify no private repo data leakage (III. Data Privacy principle)
- [ ] T082 Accessibility check: Verify SVG alt text is descriptive for screen readers
- [ ] T083 Update agent context file (CLAUDE.md) with final implementation notes
- [ ] T084 Final integration test: Complete workflow from spec.md acceptance scenarios

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-6)**: All depend on Foundational phase completion
  - User Story 1 (P1): Core functionality - MUST complete first for MVP
  - User Story 2 (P2): Enhances US1 - should complete after US1
  - User Story 3 (P1): Core functionality - can run parallel to US1 if capacity allows
  - User Story 4 (P3): Lowest priority - depends on US1 being functional
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Foundation → US1 (no other dependencies) → **MVP READY**
- **User Story 2 (P2)**: Foundation → US1 complete → US2 (enhances SVG rendering)
- **User Story 3 (P1)**: Foundation → US1 partial → US3 (can develop analysis in parallel)
- **User Story 4 (P3)**: Foundation → US1 complete → US4 (adds flexibility to triggering)

### Critical Path (Sequential MVP)

1. Phase 1: Setup (T001-T003) → **3 tasks**
2. Phase 2: Foundational (T004-T009) → **6 tasks** 🚫 **BLOCKER**
3. Phase 3: User Story 1 (T010-T040b) → **32 tasks** 🎯 **MVP**
4. ✅ **STOP & VALIDATE** - Unified reports now work end-to-end

### Recommended Implementation Order

**Week 1: Foundation**
- Complete Setup + Foundational (T001-T009)
- Establish base entities and workflow skeleton

**Week 2: MVP Core (US1)**
- Complete User Story 1 workflow orchestration (T012-T020)
- Complete User Story 1 report generation (T021-T028)
- Unified report file generation working locally

**Week 3: MVP Integration (US1 continued)**
- Complete User Story 1 CLI integration (T029-T033)
- Complete User Story 1 GitHub Actions (T034-T037)
- Complete User Story 1 validation (T038-T040b)
- ✅ **MVP DEPLOYED** - Weekly automation live

**Week 4: Enhancements**
- Complete User Story 2 (T041-T048) - SVG rendering polish
- Complete User Story 3 (T049-T060) - Repository analysis depth

**Week 5: Flexibility & Polish**
- Complete User Story 4 (T061-T070) - Trigger mechanisms
- Complete Polish phase (T071-T084) - Documentation, tests, cleanup

### Parallel Opportunities

**Phase 2: Foundational (After T004)**
- T005, T006, T007 can run in parallel (different files: github_data.py, report.py, __init__.py)
- T008, T009 can run in parallel (different files: workflow.py, generator.py)

**Phase 3: User Story 1**
- T010, T011 can run in parallel (test files)
- T021, T022, T023, T024 can run in parallel (different generator methods)
- T029, T030 can run in parallel (CLI arg parsing)

**Phase 4: User Story 2**
- T041, T042 can run in parallel (test files)
- T043, T044, T046 can run in parallel (different generator sections)

**Phase 5: User Story 3**
- T049, T050 can run in parallel (test files)
- T051, T052 can run in parallel (validation in different modules)

**Phase 6: User Story 4**
- T061, T062 can run in parallel (test files)
- T063, T064, T065 can run in parallel (different integration points)

**Phase 7: Polish**
- T071, T072, T073, T075, T076, T077, T081 can all run in parallel (different files)

---

## Parallel Example: User Story 1 Core

```bash
# After Foundational phase completes, launch these in parallel:

# Workflow orchestration (main logic flow)
Task T012-T020: "UnifiedReportWorkflow implementation"

# Report generation (independent of workflow details)
Parallel Tasks T021-T028: "UnifiedReportGenerator sections"
  - T021: Header generation
  - T022: Profile overview
  - T023: Repository analysis
  - T024: Footer
  - T025-T028: Helpers

# CLI integration (independent of workflow/generator)
Parallel Tasks T029-T030: "CLI argument parsing"

# Then sequentially:
Task T031-T033: CLI routing (needs T029-T030)
Task T034-T037: Workflow updates (needs T012-T028 complete)
Task T038-T040: Validation (needs everything)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only) 🎯

**Goal**: Get unified reports working end-to-end as fast as possible

1. Complete Phase 1: Setup (T001-T003) - verify environment
2. Complete Phase 2: Foundational (T004-T009) - build foundation
3. Complete Phase 3: User Story 1 (T010-T040b) - full workflow
4. **STOP and VALIDATE**:
   - Run `spark analyze --user markhazleton --unified --verbose`
   - Verify `/output/reports/markhazleton-analysis.md` exists
   - Check file has all 4 sections (Header, Profile, Analysis, Footer)
   - Verify SVG references and repository analysis are present
   - Confirm file size <1MB
   - Performance validation: Test with 200 repos, verify <10 min completion (T040b)
5. Deploy to production (update workflow, test weekly automation)

**Estimated MVP Time**: 2-3 weeks (32 core tasks + foundation)

### Incremental Delivery (Recommended)

**Sprint 1: Foundation**
- Phase 1 + Phase 2 (T001-T009)
- Deliverable: Base entities and workflow skeleton exist

**Sprint 2: MVP Core**
- Phase 3: User Story 1 (T010-T040b)
- Deliverable: Unified reports generate locally via CLI
- **Demo**: Show `markhazleton-analysis.md` with SVGs + top 50 repos

**Sprint 3: MVP Production**
- Workflow deployment (T034-T037)
- Validation (T038-T040b)
- Deliverable: Weekly automation live
- **Demo**: GitHub Actions generates reports automatically

**Sprint 4: Enhancements**
- Phase 4: User Story 2 (SVG rendering polish) (T041-T048)
- Phase 5: User Story 3 (analysis depth) (T049-T060)
- Deliverable: Report quality improved
- **Demo**: Show enhanced formatting and complete repo analysis

**Sprint 5: Production Hardening**
- Phase 6: User Story 4 (flexibility) (T061-T070)
- Phase 7: Polish (T071-T084)
- Deliverable: Production-ready feature
- **Demo**: Complete documentation, all trigger mechanisms working

### Parallel Team Strategy

With 3 developers after Foundational phase completes:

**Developer A: Workflow Orchestration**
- T012-T020 (UnifiedReportWorkflow implementation)
- T034-T037 (GitHub Actions integration)

**Developer B: Report Generation**
- T021-T028 (UnifiedReportGenerator implementation)
- T043-T048 (User Story 2 SVG enhancements)

**Developer C: CLI & Analysis**
- T029-T033 (CLI integration)
- T051-T060 (User Story 3 repository analysis)

All converge at T038-T040b for final validation.

---

## Task Summary

**Total Tasks**: 85
- **Setup**: 3 tasks
- **Foundational**: 6 tasks (BLOCKER for all stories)
- **User Story 1 (P1)**: 32 tasks 🎯 MVP
- **User Story 2 (P2)**: 8 tasks (enhancement)
- **User Story 3 (P1)**: 12 tasks (core feature)
- **User Story 4 (P3)**: 10 tasks (flexibility)
- **Polish**: 14 tasks (finalization)

**Parallel Opportunities**: 41 tasks marked [P] can run in parallel (48.2% parallelizable)

**MVP Scope**: Phases 1-3 (41 tasks total) = Unified reports with SVGs and analysis

**Independent Test Criteria**:
- **US1**: Run workflow, verify non-dated report exists with all 4 sections, <1MB
- **US2**: Open report in 3 different viewers, verify all 6 SVGs render inline
- **US3**: Check report contains top 50 repos with scores, tech stacks, metrics
- **US4**: Generate via CLI and workflow, compare outputs for consistency

---

## Format Validation ✅

All 84 tasks follow strict checklist format:
- ✅ Start with `- [ ]` checkbox
- ✅ Sequential task ID (T001-T084)
- ✅ [P] marker for parallelizable tasks (41 tasks)
- ✅ [Story] label for user story phases (US1, US2, US3, US4)
- ✅ Clear description with exact file paths
- ✅ No story label for Setup, Foundational, and Polish phases

---

## Notes

- Tests are OPTIONAL (not explicitly requested in spec) - marked with ⚠️
- User Story 3 has P1 priority same as US1 - can develop in parallel if capacity allows
- User Story 2 depends on US1 SVG generation working
- User Story 4 adds flexibility but isn't blocking for core functionality
- Stop at any checkpoint to validate story independently before proceeding
- Commit after each task or logical group
- Avoid: implementing features not in spec, breaking backward compatibility with dated reports
