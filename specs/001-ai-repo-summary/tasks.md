# Implementation Tasks: AI-Powered GitHub Repository Summary Report

**Feature Branch**: `001-ai-repo-summary`
**Generated**: 2025-12-29
**Spec**: [spec.md](spec.md) | **Plan**: [plan.md](plan.md) | **Research**: [research.md](research.md)

This task list is organized by user story priority and implementation phases. Tasks are dependency-ordered within each phase.

**Task Format**: `- [ ] [TaskID] [P?] [Story?] Description with file path`
- **[P]** = Foundational/prerequisite task (blocks multiple stories)
- **[US1]** = User Story 1 (P1 - Generate Top 50 Repository Report)
- **[US2]** = User Story 2 (P2 - Overall Developer Profile Analysis)
- **[US3]** = User Story 3 (P2 - Technology Stack Currency Assessment)

---

## Phase 1: Project Setup & Dependencies

**Purpose**: Initialize project structure, install dependencies, configure environment

- [X] T001 [P] Add new dependencies to requirements.txt (anthropic>=0.40.0, tenacity>=9.0.0, packaging>=23.0, tomli>=2.0.0)
- [X] T002 [P] Update setup.py with new package metadata and entry points
- [X] T003 [P] Create src/spark/models/ directory for data model classes
- [X] T004 [P] Add ANTHROPIC_API_KEY to .github/workflows/generate-stats.yml environment variables
- [X] T005 [P] Update config/spark.yml with analyzer configuration section (top_n, cache_ttl, ai_provider)
- [X] T006 [P] Create output/reports/ directory for generated analysis reports
- [X] T007 [P] Create tests/fixtures/sample_repositories.json with mock repository data
- [X] T008 [P] Create tests/fixtures/sample_readmes/ directory with sample README files
- [X] T009 [P] Create tests/fixtures/sample_dependency_files/ directory (package.json, requirements.txt, etc.)

**Completion Criteria**: All dependencies installed, directory structure created, configuration files updated

---

## Phase 2: Core Data Models (Foundational)

**Purpose**: Define entity classes used across all user stories

- [X] T010 [P] Create Repository model in src/spark/models/repository.py (name, description, url, created_at, updated_at, primary_language, language_stats, stars, forks, issues, is_archived, is_fork)
- [X] T011 [P] Create CommitHistory model in src/spark/models/commit.py (total_commits, recent_90d, recent_180d, recent_365d, last_commit_date, patterns)
- [X] T012 [P] Create TechnologyStack model in src/spark/models/tech_stack.py (languages, frameworks, dependencies, version_info)
- [X] T013 [P] Create RepositorySummary model in src/spark/models/summary.py (repo_id, ai_summary, fallback_summary, generation_method)
- [X] T014 [P] Create UserProfile model in src/spark/models/profile.py (username, total_repos, active_repos, tech_diversity, activity_patterns, overall_impression)
- [X] T015 [P] Create Report model in src/spark/models/report.py (user_profile, repositories, generation_timestamp, metadata)
- [X] T016 [P] [US1] Implement language detection using GitHub API in src/spark/fetcher.py (GET /repos/{owner}/{repo}/languages returns bytes by language)

**Completion Criteria**: All model classes created with proper typing, validation, and serialization methods; language detection retrieves stats from GitHub API

---

## Phase 3: Repository Ranking & Analysis (US1 - P1)

**Purpose**: Implement repository ranking algorithm and top 50 selection

- [X] T020 [P] [US1] Create src/spark/ranker.py with RepositoryRanker class
- [X] T021 [P] [US1] Implement popularity scoring (logarithmic scaling for stars, forks, watchers) in ranker.py
- [X] T022 [P] [US1] Implement activity scoring (multi-window time decay: 90d/180d/365d) in ranker.py
- [X] T023 [P] [US1] Implement health scoring (documentation, maturity, issue management) in ranker.py
- [X] T024 [P] [US1] Implement composite scoring (30% popularity + 45% activity + 25% health) in ranker.py
- [X] T025 [P] [US1] Implement edge case handling (archived repos, forks, zero-star active repos) in ranker.py
- [X] T026 [P] [US1] Extend src/spark/fetcher.py to retrieve time-windowed commit counts (90d, 180d, 365d)
- [X] T027 [P] [US1] Implement privacy filter in ranker.py to explicitly exclude private repositories (constitution requirement)
- [X] T028 [P] [US1] Create unit tests for ranking algorithm in tests/unit/test_ranker.py
- [X] T029 [P] [US1] Create test fixtures with sample ranking scenarios in tests/fixtures/ranking_scenarios.json

**Completion Criteria**: Ranking algorithm passes all tests including edge cases, successfully ranks repositories by composite score, privacy filter validated

---

## Phase 4: AI-Powered Summarization (US1 - P1)

**Purpose**: Implement AI summary generation with fallback strategies

- [X] T030 [US1] Create src/spark/summarizer.py with RepositorySummarizer class
- [X] T031 [US1] Implement Anthropic Claude Haiku API integration in summarizer.py
- [X] T032 [US1] Implement retry logic with exponential backoff using tenacity in summarizer.py
- [X] T033 [US1] Implement README truncation to fit Claude context window (200K tokens) in summarizer.py
- [X] T034 [US1] Implement commit pattern analysis (frequency, recency, consistency) in summarizer.py
- [X] T035 [US1] Implement prompt engineering for technical repository summaries in summarizer.py
- [X] T036 [US1] Implement enhanced template fallback (extract from README + metadata) in summarizer.py
- [X] T037 [US1] Implement basic template fallback (metadata only) in summarizer.py
- [X] T038 [US1] Add cost tracking and logging for API usage in summarizer.py
- [X] T039 [US1] Create unit tests with mock API responses in tests/unit/test_summarizer.py
- [X] T040 [US1] Create integration tests for fallback scenarios in tests/integration/test_summarizer_fallback.py
- [X] T041 [US1] Create unit test for no-README fallback scenario in tests/unit/test_summarizer.py (validates FR-012 requirement)

**Completion Criteria**: AI summarization works with all three fallback tiers, retry logic handles API failures, cost tracking logs API usage, no-README scenario explicitly tested

---

## Phase 5: Technology Stack Currency Assessment (US3 - P2)

**Purpose**: Implement dependency version checking against package registries

- [ ] T050 [US3] Create src/spark/dependencies/parser.py with DependencyParser class
- [ ] T051 [US3] Implement package.json parser (NPM) in parser.py
- [ ] T052 [US3] Implement requirements.txt parser (PyPI) in parser.py
- [ ] T053 [US3] Implement pyproject.toml parser (PyPI) using tomli in parser.py
- [ ] T054 [US3] Implement Gemfile parser (RubyGems) in parser.py
- [ ] T055 [US3] Implement go.mod parser (Go Modules) in parser.py
- [ ] T056 [US3] Create src/spark/dependencies/version_checker.py with RegistryClient base class
- [ ] T057 [US3] Implement NPM registry client (https://registry.npmjs.org) in version_checker.py
- [ ] T058 [US3] Implement PyPI registry client (https://pypi.org/pypi) in version_checker.py
- [ ] T059 [US3] Implement RubyGems registry client (https://rubygems.org/api) in version_checker.py
- [ ] T060 [US3] Implement Go Proxy client (https://proxy.golang.org) in version_checker.py
- [ ] T061 [US3] Implement hybrid caching (file-based 7-day + in-memory) in version_checker.py
- [ ] T062 [US3] Implement version comparison using packaging.version.Version in version_checker.py
- [ ] T063 [US3] Create src/spark/dependencies/analyzer.py with RepositoryDependencyAnalyzer class
- [ ] T064 [US3] Implement currency assessment logic (versions behind calculation) in analyzer.py
- [ ] T065 [US3] Implement graceful error handling for unsupported ecosystems in analyzer.py
- [ ] T066 [US3] Create unit tests for dependency parsers in tests/unit/test_dependency_parser.py
- [ ] T067 [US3] Create unit tests for registry clients with mock responses in tests/unit/test_version_checker.py
- [ ] T068 [US3] Create integration tests for full dependency analysis in tests/integration/test_dependency_analysis.py

**Completion Criteria**: Dependency parsing works for 5+ ecosystems, version checking uses cached data 80%+, currency assessment identifies outdated packages

---

## Phase 6: Overall Profile Analysis (US2 - P2)

**Purpose**: Generate AI-powered user profile and overall impression

- [ ] T070 [US2] Extend src/spark/summarizer.py with UserProfileGenerator class
- [ ] T071 [US2] Implement technology diversity analysis (language distribution, framework variety) in summarizer.py
- [ ] T072 [US2] Implement activity pattern analysis (commit frequency, consistency, trends) in summarizer.py
- [ ] T073 [US2] Implement contribution classification (active maintainer, hobbyist, specialist) in summarizer.py
- [ ] T074 [US2] Implement AI-powered overall impression generation using repository portfolio in summarizer.py
- [ ] T075 [US2] Implement fallback profile generation (template-based) in summarizer.py
- [ ] T076 [US2] Create unit tests for profile generation in tests/unit/test_profile_generator.py

**Completion Criteria**: Profile analysis identifies 3+ observable patterns, overall impression references user's tech focus and activity trends

---

## Phase 7: Report Generation & Formatting (US1 - P1)

**Purpose**: Generate markdown reports with all analysis results

- [X] T080 [US1] Create src/spark/report_generator.py with ReportGenerator class
- [X] T081 [US1] Implement markdown header generation (title, timestamp, metadata) in report_generator.py
- [X] T082 [US1] [US2] Implement user profile section formatting in report_generator.py
- [X] T083 [US1] Implement repository listing section (top 50 ranked) in report_generator.py
- [X] T084 [US1] Implement per-repository entry formatting (stats, summary, creation date) in report_generator.py
- [ ] T085 [US1] [US3] Implement technology stack section formatting (currency indicators) in report_generator.py
- [X] T086 [US1] Implement failure/skip notes section in report_generator.py
- [X] T087 [US1] Implement GitHub-flavored markdown compliance in report_generator.py
- [X] T088 [US1] Implement file writing to output/reports/ directory in report_generator.py
- [ ] T089 [US1] Create unit tests for markdown formatting in tests/unit/test_report_generator.py

**Completion Criteria**: Generated reports render correctly in GitHub, include all required sections, handle partial results gracefully

---

## Phase 8: CLI Integration & Progress Tracking (US1 - P1)

**Purpose**: Add CLI commands and user-facing interface

- [X] T090 [P] [US1] Extend src/spark/cli.py with `analyze` command group
- [X] T091 [US1] Implement `spark analyze --user <username> --output <path>` command in cli.py
- [X] T092 [US1] Implement `spark analyze --list-only` dry-run command in cli.py
- [ ] T093 [US1] Implement progress indicator (current repo + percentage) in cli.py
- [ ] T094 [US1] Implement partial report generation on errors in cli.py
- [ ] T095 [US1] Implement error logging with actionable guidance in cli.py
- [ ] T096 [US1] Implement rate limit handling and user notifications in cli.py
- [ ] T097 [P] Update src/main.py to support analyze command for GitHub Actions execution
- [ ] T098 [US1] Create CLI integration tests in tests/integration/test_cli_analyze.py

**Completion Criteria**: CLI commands work locally and in GitHub Actions, progress tracking displays correctly, errors provide actionable messages

---

## Phase 9: End-to-End Integration & Testing (All Stories)

**Purpose**: Validate complete workflow with real and mock data

- [ ] T100 [P] Create tests/integration/test_full_report_generation.py with end-to-end scenarios
- [ ] T101 [US1] Test scenario: User with 50+ public repositories
- [ ] T102 [US1] Test scenario: User with fewer than 50 repositories
- [ ] T103 [US1] Test scenario: Repository with README and commit history
- [ ] T104 [US1] Test scenario: Repository without README (fallback summary)
- [ ] T105 [US1] Test scenario: Empty repository (no commits)
- [ ] T106 [US1] Test scenario: GitHub API rate limit reached (partial report)
- [ ] T107 [US2] Test scenario: Overall profile analysis with diverse repositories
- [ ] T108 [US3] Test scenario: Technology currency assessment with multiple ecosystems
- [ ] T109 [P] Test scenario: Privacy filter excludes private repositories
- [ ] T110 [P] Test scenario: Complete report generation within 3-minute performance target (SC-001)
- [ ] T111 [P] Test scenario: AI summary accuracy validation (SC-002: 90%)
- [ ] T112 [P] Test scenario: Technology identification accuracy (SC-003: 95%)
- [ ] T113 [P] Test edge case: User with no public repositories (edge case spec.md L75)
- [ ] T114 [P] Test edge case: Repository with unrecognized programming language (edge case spec.md L78)
- [ ] T115 [US3] Test edge case: Dependency file that cannot be parsed (edge case spec.md L82)
- [ ] T116 [P] Test edge case: Archived repository handling (edge case spec.md L81 - validate 50% activity penalty)

**Completion Criteria**: All test scenarios pass, performance targets met, accuracy metrics validated, all edge cases handled gracefully

---

## Phase 10: Documentation & Polish

**Purpose**: Update user documentation and project metadata

- [ ] T120 [P] Update README.md with analyze command usage examples
- [ ] T121 [P] Create docs/analyze-command.md with detailed CLI documentation
- [ ] T122 [P] Update config/spark.yml.example with analyzer configuration
- [ ] T123 [P] Add ANTHROPIC_API_KEY setup instructions to documentation
- [ ] T124 [P] Create sample report in output/reports/markhazleton-example.md
- [ ] T125 [P] Update CHANGELOG.md with new feature announcement
- [ ] T126 [P] Update version number to reflect feature addition (semantic versioning)

**Completion Criteria**: Documentation complete, example reports generated, changelog updated

---

## Cross-Cutting Concerns (Throughout Implementation)

- [ ] T130 [P] Implement logging with timestamps and context in all modules (constitution V. Observable)
- [ ] T131 [P] Validate privacy filter in integration tests (constitution III. Data Privacy)
- [ ] T132 [P] Ensure all calculation logic has >80% test coverage (constitution IV. Testability)
- [ ] T133 [P] Verify all modules are independently importable (constitution I. Python-First)
- [ ] T134 [P] Validate CLI accessibility for all features (constitution II. CLI Interface)
- [ ] T135 [P] Implement 6-hour cache TTL for all API responses (performance standard)
- [ ] T136 [P] Add exponential backoff for all external API calls (performance standard)

**Completion Criteria**: Constitution compliance validated, all standards met

---

## Dependency Graph

**Story Completion Order**:
1. **Phase 1-2**: Setup & Data Models (blocking prerequisites)
2. **Phase 3-4**: US1 Core (ranking + summarization) - **MUST COMPLETE FIRST** (P1 priority)
3. **Phase 7-8**: US1 Reporting & CLI - **MUST COMPLETE SECOND** (P1 priority, depends on Phase 3-4)
4. **Phase 5**: US3 Currency Assessment (P2 priority, independent of US1/US2)
5. **Phase 6**: US2 Profile Analysis (P2 priority, depends on US1 completion for repository data)
6. **Phase 9**: Integration Testing (depends on all stories)
7. **Phase 10**: Documentation & Polish (final phase)

**Critical Path**: T001-T015 → T020-T040 → T080-T098 → T100-T112 → T120-T126

**Parallel Work Opportunities**:
- Phase 5 (US3) can be developed in parallel with Phase 3-4 (US1) after Phase 1-2
- Phase 6 (US2) can be developed in parallel with Phase 5 (US3)
- Cross-cutting concerns (T130-T136) should be implemented alongside feature development

---

## Task Statistics

- **Total Tasks**: 141 (updated from 136)
- **Foundational [P]**: 40 tasks (includes T016 language detection, T113-T116 edge cases)
- **User Story 1 [US1]**: 47 tasks (P1 priority, includes T041 no-README test)
- **User Story 2 [US2]**: 7 tasks (P2 priority)
- **User Story 3 [US3]**: 20 tasks (P2 priority, includes T115 unparseable dependency test)
- **Multi-Story Tasks**: 27 tasks

**Estimated Completion**:
- Phase 1-2: Foundation (16 tasks, includes T016 language detection)
- Phase 3-8: Feature Development (86 tasks, includes T041 no-README test)
- Phase 9: Integration Testing (17 tasks, includes T113-T116 edge cases)
- Phase 10: Documentation (7 tasks)
- Cross-cutting: Throughout (7 tasks)

---

## Performance Validation Checkpoints

**SC-001**: Report generation <3 minutes for 50 repos
- Validate at: T110 (end-to-end test)

**SC-002**: AI summary accuracy 90%
- Validate at: T111 (accuracy test)

**SC-003**: Tech stack identification 95%
- Validate at: T112 (identification test)

**SC-007**: Active repos in top 10 (85% of time)
- Validate at: T028 (ranking tests)

---

## Notes

- All file paths are relative to repository root `C:\GitHub\MarkHazleton\github-stats-spark`
- Test fixtures should be created before implementing corresponding features
- Constitution compliance validated throughout (especially privacy filter T027, T109, T131)
- Performance budget validated at T110 (must meet <3 minute target)
- Dependency on external APIs (Claude, NPM, PyPI, etc.) requires error handling and fallbacks
