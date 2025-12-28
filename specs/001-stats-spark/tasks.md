# Tasks: Stats Spark - GitHub Profile Statistics Generator

**Input**: Design documents from `/specs/001-stats-spark/`
**Prerequisites**: plan.md (complete), spec.md (complete)

**Tests**: Not explicitly requested in specification - focusing on implementation tasks

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single Python project**: `src/`, `tests/`, `config/`, `output/` at repository root
- Paths follow the structure defined in plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure per plan.md (src/, tests/, config/, output/, docs/, assets/, .github/workflows/)
- [x] T002 Initialize Python project with requirements.txt (PyGithub, PyYAML, svgwrite, requests, python-dateutil)
- [x] T003 [P] Create requirements-dev.txt (pytest, pytest-mock, black, flake8, mypy)
- [x] T004 [P] Create setup.py with package metadata and entry points
- [x] T005 [P] Create .gitignore (exclude .cache/, __pycache__/, *.pyc, .venv/, .env)
- [x] T006 [P] Create LICENSE file (MIT License)
- [x] T007 [P] Create initial README.md with project description and placeholder instructions
- [x] T008 [P] Create output/.gitkeep to ensure directory exists in git
- [x] T009 [P] Create output/README.md with SVG usage instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T010 Create src/__init__.py (package initialization)
- [x] T011 Create src/spark/__init__.py with version constant
- [x] T012 [P] Implement APICache class in src/spark/cache.py (get, set, is_expired, clear methods with 6-hour TTL)
- [x] T013 [P] Implement SparkConfig class in src/spark/config.py (load, validate, get_theme methods for YAML parsing)
- [x] T014 Create config/spark.yml with default configuration (user: auto, enabled stats, thresholds, theme: spark-dark, effects)
- [x] T015 [P] Create config/themes.yml with theme definitions (spark-dark, spark-light color schemes)
- [x] T016 [P] Create src/spark/themes/__init__.py with Theme base class
- [x] T017 [P] Implement SparkDarkTheme in src/spark/themes/spark_dark.py (primary: #0EA5E9, accent: #FCD34D, dark background)
- [x] T018 [P] Implement SparkLightTheme in src/spark/themes/spark_light.py (bright backgrounds, accessible contrast)
- [x] T019 [P] Implement CustomTheme in src/spark/themes/custom.py (loads from themes.yml)
- [x] T020 Create logging utility in src/spark/logger.py (stdout/stderr logging with timestamps and error details)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Automated Daily Statistics Generation (Priority: P1) 🎯 MVP

**Goal**: Enable automated daily statistics generation via GitHub Actions with manual trigger support

**Independent Test**: Set up GitHub Actions workflow, manually trigger it, verify SVG files are generated in output/ with current timestamps

### Implementation for User Story 1

- [x] T021 [P] [US1] Create .github/workflows/generate-stats.yml with cron schedule (0 0 * * *) and workflow_dispatch trigger
- [x] T022 [P] [US1] Implement GitHubFetcher class in src/spark/fetcher.py (authentication, fetch_user_profile, fetch_repositories methods)
- [x] T023 [US1] Add pagination support to GitHubFetcher.fetch_repositories (handle max 500 repos with configurable limit)
- [x] T024 [US1] Add rate limiting handling to GitHubFetcher (detect rate limits, exponential backoff retry)
- [x] T025 [US1] Integrate APICache with GitHubFetcher (cache responses for 6 hours, respect force-refresh flag)
- [x] T026 [US1] Implement main.py entry point (load config, initialize fetcher, coordinate generation flow)
- [x] T027 [US1] Add GitHub token authentication from environment variable (GITHUB_TOKEN from secrets)
- [x] T028 [US1] Add username auto-detection in main.py (from GITHUB_REPOSITORY environment variable)
- [x] T029 [US1] Implement error logging to workflow output in main.py (capture API errors, config errors, generation failures)
- [x] T030 [US1] Configure GitHub Actions workflow to install dependencies and run main.py
- [x] T031 [US1] Add workflow output artifact upload (persist generated SVGs)
- [x] T032 [US1] Create workflow documentation comment in generate-stats.yml explaining setup steps

**Checkpoint**: At this point, GitHub Actions workflow can run daily and generate statistics automatically

---

## Phase 4: User Story 2 - Comprehensive Statistics Dashboard (Priority: P1)

**Goal**: Generate SVG visualizations showing commits, languages, time patterns, collaboration metrics, and Spark Score

**Independent Test**: Run generation for test account, verify overview SVG contains all metrics (commits, languages, time patterns, Spark Score, collaboration)

### Implementation for User Story 2

- [x] T033 [P] [US2] Implement StatsCalculator class in src/spark/calculator.py (initialize with user data)
- [x] T034 [P] [US2] Add calculate_spark_score method to StatsCalculator (40% consistency, 35% volume, 25% collaboration, 0-100 scale)
- [x] T035 [P] [US2] Implement consistency score calculation (regularity of commits over time, gaps penalize score)
- [x] T036 [P] [US2] Implement commit volume score calculation (normalized commit count with diminishing returns for very high counts)
- [x] T037 [P] [US2] Implement collaboration score calculation (forks, stars, contributors, PR activity)
- [x] T038 [US2] Add calculate_lightning_rating method (map 0-100 score to 1-5 lightning bolts)
- [x] T039 [P] [US2] Implement analyze_time_patterns method in StatsCalculator (hourly distribution, categorization)
- [x] T040 [P] [US2] Add night owl detection (majority commits 22:00-4:00)
- [x] T041 [P] [US2] Add early bird detection (majority commits 5:00-9:00)
- [x] T042 [P] [US2] Implement aggregate_languages method (percentage breakdown, commit count per language)
- [x] T043 [P] [US2] Implement calculate_streaks method (coding streaks, learning streaks for new languages)
- [x] T044 [US2] Add fetch_commits method to GitHubFetcher (paginate commits, max 100 per repo, extract timestamps and languages)
- [x] T045 [US2] Add fetch_languages method to GitHubFetcher (get language stats for each repository)
- [x] T046 [P] [US2] Create StatisticsVisualizer class in src/spark/visualizer.py (coordinate SVG generation, apply themes)
- [x] T047 [P] [US2] Implement generate_overview method in StatisticsVisualizer (layout: Spark Score, commits, languages, time pattern)
- [x] T048 [P] [US2] Add SVG text rendering with WCAG AA contrast compliance for all themes
- [x] T049 [P] [US2] Implement generate_heatmap method (commit frequency calendar visualization)
- [x] T050 [P] [US2] Implement generate_languages method (bar chart with percentage labels)
- [x] T051 [P] [US2] Implement generate_fun_stats method (Lightning Round Stats one-liners)
- [x] T052 [P] [US2] Implement generate_streaks method (current/longest streak visualization)
- [x] T053 [US2] Add theme application to all SVG generators (colors, effects from theme config)
- [x] T054 [US2] Add gradient and glow effects when enabled in config (SVG filters)
- [x] T055 [US2] Implement "Powered by Stats Spark" branding footer (conditional on config.branding.show_powered_by)
- [x] T056 [US2] Wire up visualization pipeline in main.py (fetch → calculate → visualize → save SVGs to output/)
- [x] T057 [US2] Add graceful handling for users with no commits (display "Start your coding journey!" message)
- [x] T058 [US2] Add graceful handling for minimal activity users (show "starter" indicator)
- [x] T058a [US2] Add handling for deleted/private repositories (mark as "unavailable" in historical stats per FR-028)
- [x] T058b [P] [US2] Write unit tests for StatsCalculator.calculate_spark_score (verify weighted formula, normalization, test fixtures)
- [x] T058c [P] [US2] Write unit tests for StatsCalculator.analyze_time_patterns (night owl, early bird, balanced categorization)
- [x] T058d [P] [US2] Write unit tests for StatsCalculator.calculate_streaks (coding streaks, learning streaks edge cases)
- [x] T058e [P] [US2] Write unit tests for StatisticsVisualizer SVG generation (validate output structure, theme application)

**Checkpoint**: At this point, comprehensive statistics are generated and saved as SVG files

---

## Phase 5: User Story 3 - Theme Customization (Priority: P2)

**Goal**: Enable users to switch between spark-dark, spark-light, and custom themes via configuration

**Independent Test**: Change theme in spark.yml, regenerate stats, verify SVG uses correct colors and contrast

### Implementation for User Story 3

- [x] T059 [US3] Add theme validation to SparkConfig.validate (verify theme exists in themes.yml or is built-in)
- [x] T060 [P] [US3] Extend SparkDarkTheme with all color properties (primary, accent, background, text, borders)
- [x] T061 [P] [US3] Extend SparkLightTheme with all color properties (ensure WCAG AA contrast for light backgrounds)
- [x] T062 [US3] Implement CustomTheme.load_from_yaml (read user-defined colors from themes.yml)
- [x] T063 [US3] Add theme preview support in SparkConfig (validate custom themes before generation)
- [x] T064 [US3] Update StatisticsVisualizer to apply theme.effects (glow, gradient, animations flags)
- [x] T065 [US3] Add WCAG AA compliance validation for custom themes (warn if contrast ratio insufficient, minimum 4.5:1 per SC-005)
- [x] T065a [P] [US3] Write unit tests for WCAG contrast validation (test various color combinations, verify warnings)
- [x] T066 [US3] Update README.md with theme customization instructions and examples

**Checkpoint**: At this point, users can customize themes and see visual changes in generated SVGs

---

## Phase 6: User Story 4 - Selective Statistics Output (Priority: P2)

**Goal**: Allow users to enable/disable individual statistics categories via spark.yml configuration

**Independent Test**: Modify enabled list in spark.yml, run generation, verify only specified SVGs are created

### Implementation for User Story 4

- [x] T067 [US4] Add stats.enabled parsing to SparkConfig (validate category names against allowed list)
- [x] T068 [US4] Implement selective generation logic in main.py (check config before generating each SVG)
- [x] T069 [US4] Skip overview generation when not in enabled list
- [x] T070 [US4] Skip heatmap generation when not in enabled list
- [x] T071 [US4] Skip languages generation when not in enabled list
- [x] T072 [US4] Skip fun stats generation when not in enabled list
- [x] T073 [US4] Skip streaks generation when not in enabled list
- [x] T074 [US4] Add performance optimization (skip data fetching for disabled categories)
- [x] T075 [US4] Update spark.yml comments explaining each statistics category purpose
- [x] T076 [US4] Add configuration validation error messages for invalid category names

**Checkpoint**: At this point, users have granular control over which statistics are generated

---

## Phase 7: User Story 5 - Local Preview and Testing (Priority: P3)

**Goal**: Provide CLI tool for local statistics generation, theme preview, and configuration validation

**Independent Test**: Run `python -m spark.cli generate --user testuser`, verify local SVGs are created

### Implementation for User Story 5

- [x] T077 [P] [US5] Create src/cli.py with click or argparse CLI framework
- [x] T078 [P] [US5] Implement `generate` command in cli.py (--user, --output-dir, --config flags)
- [x] T079 [P] [US5] Implement `preview` command in cli.py (--theme flag, generates sample data)
- [x] T080 [P] [US5] Implement `config` command in cli.py (--validate, --set subcommands)
- [x] T081 [US5] Add sample data generator for preview mode (mock GitHub API responses)
- [x] T082 [US5] Wire up local generation flow (load config, fetch or use samples, generate to specified directory)
- [x] T083 [US5] Add --force-refresh flag to bypass cache in CLI
- [x] T084 [US5] Add verbose logging flag (--verbose) for debugging
- [x] T085 [US5] Add CLI help text and usage examples
- [x] T086 [US5] Update setup.py with console_scripts entry point for `spark` command

**Checkpoint**: At this point, developers can test and preview locally before deploying to GitHub Actions

---

## Phase 8: User Story 6 - Profile README Setup Documentation (Priority: P2)

**Goal**: Provide clear step-by-step instructions for embedding statistics in GitHub profile README

**Independent Test**: Follow documentation from scratch, verify stats display correctly in profile README without issues

### Implementation for User Story 6

- [x] T087 [P] [US6] Create docs/getting-started.md with prerequisites and setup steps
- [x] T088 [P] [US6] Create docs/embedding-guide.md with markdown examples for each SVG category
- [x] T089 [P] [US6] Add markhazleton demo examples to docs/embedding-guide.md (actual working URLs)
- [x] T090 [P] [US6] Create docs/configuration.md explaining all spark.yml options
- [x] T091 [P] [US6] Create docs/api-reference.md documenting SparkConfig, StatsCalculator, Visualizer classes
- [x] T092 [US6] Update README.md with Quick Start section (fork, configure token, enable workflow, embed)
- [x] T093 [US6] Add troubleshooting section to README.md (common issues: token expiration, rate limits, workflow failures)
- [x] T094 [US6] Create assets/examples/markhazleton/ directory with generated example SVGs
- [x] T095 [US6] Generate demo statistics for markhazleton account and commit to assets/examples/
- [x] T096 [US6] Add screenshot examples to README.md showing each statistics category
- [x] T097 [US6] Create embedding template in README.md with copy-paste markdown snippets
- [x] T098 [US6] Add FAQ section addressing common setup questions

**Checkpoint**: At this point, new users can follow clear documentation to set up and embed statistics successfully

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T099 [P] Add special character sanitization for commit messages (prevent SVG injection)
- [x] T100 [P] Add text truncation for extremely long commit messages in SVGs
- [x] T101 [P] Implement repository limit enforcement (default 500, configurable via spark.yml)
- [x] T102 [P] Add "Other" language grouping for unrecognized languages
- [x] T103 [P] Add detailed error logging for API failures (include endpoint, status code, retry count)
- [x] T104 [P] Optimize SVG file size (minimize whitespace, optimize path data)
- [x] T105 [P] Add mobile rendering optimization (responsive SVG dimensions)
- [x] T106 [P] Create assets/logo.svg for Stats Spark branding
- [x] T107 [P] Add repository privacy check (exclude private repos from statistics)
- [x] T108 [P] Implement force-refresh mechanism (bypass cache when explicitly requested)
- [x] T109 [P] Add end-to-end integration test in tests/integration/test_end_to_end.py (full workflow with mock GitHub API, verify all SVGs generated, validate SC-007 99% success rate)
- [x] T110 [P] Add unit tests for cache TTL logic in tests/unit/test_cache.py (verify 6-hour expiration, force-refresh)
- [x] T111 [P] Add unit tests for config parsing in tests/unit/test_config.py (validate FR-015 error messages)
- [x] T112 [P] Create test fixtures in tests/fixtures/ (sample_user_data.json, sample_config.yml)
- [x] T113 [P] Add unit tests for commit message sanitization in tests/unit/test_visualizer.py (special characters, truncation per edge case #7)
- [x] T114 [P] Add accuracy validation test comparing generated stats to known GitHub insights data (verify SC-006 <1% discrepancy)
- [x] T115 Run all documentation validation (spelling, broken links, code examples)
- [x] T116 Performance profiling and optimization (ensure <5 minute completion for 500 repos per SC-002)
- [x] T117 Security audit (token handling, input sanitization, dependency vulnerabilities)
- [x] T118 Verify >80% test coverage for core modules (calculator, visualizer, cache per constitution Principle IV)
- [x] T119 Final README polish (add badges, improve formatting, add contributing guidelines)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-8)**: All depend on Foundational phase completion
  - US1 (Automated Generation) - Can start after Foundational ✅
  - US2 (Comprehensive Stats) - Depends on US1 (needs fetcher and main.py) 🔗
  - US3 (Theme Customization) - Can start after Foundational ✅
  - US4 (Selective Output) - Depends on US2 (needs visualizer) 🔗
  - US5 (Local CLI) - Can start after Foundational ✅
  - US6 (Documentation) - Can start after US1 completes (needs working examples) 🔗
- **Polish (Phase 9)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - Independent
- **User Story 2 (P1)**: Depends on US1 (needs GitHubFetcher and main.py base) - Core feature
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Independent (themes are separate)
- **User Story 4 (P2)**: Depends on US2 (needs complete visualizer) - Enhancement
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - Independent (separate CLI)
- **User Story 6 (P2)**: Depends on US1 completion (needs working system to document) - Documentation

### Within Each User Story

- US1: workflow → fetcher → main.py → integration
- US2: calculator → fetcher extensions → visualizer → integration
- US3: theme classes → theme application
- US4: config parsing → selective logic
- US5: CLI framework → commands → samples
- US6: documentation files → examples → polish

### Parallel Opportunities

- **Phase 1 Setup**: All tasks marked [P] can run in parallel (T002-T009)
- **Phase 2 Foundational**: Cache, Config, Themes, Logger can be built in parallel (T012-T020)
- **After Foundational**:
  - US1 and US3 and US5 can start in parallel (all independent)
  - US2 starts after US1 completes
  - US4 and US6 start after their dependencies complete
- **Within US2**: All individual generator methods can be built in parallel (T047-T052)
- **Phase 9 Polish**: Most tasks marked [P] can run in parallel

---

## Parallel Example: User Story 2 (Comprehensive Stats)

```bash
# Launch all generator methods together:
Task: "Implement generate_overview method in src/spark/visualizer.py"
Task: "Implement generate_heatmap method in src/spark/visualizer.py"  # Wait - same file!

# Actually parallel (separate score calculations):
Task: "Implement consistency score calculation in src/spark/calculator.py"
Task: "Implement commit volume score calculation in src/spark/calculator.py" # Wait - same file!

# Truly parallel (different generator methods as separate functions or after initial file creation):
# First create the file structure, then:
Task: "Implement overview SVG layout logic"
Task: "Implement heatmap SVG layout logic"
Task: "Implement language bar chart logic"
Task: "Implement fun stats formatting logic"
# (Each can be worked on simultaneously if using git branches)
```

**Note**: Most tasks in Stats Spark are sequential within modules but can be parallelized across different developer branches.

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. ✅ Complete Phase 1: Setup (T001-T009)
2. ✅ Complete Phase 2: Foundational (T010-T020) - CRITICAL BLOCKER
3. ✅ Complete Phase 3: User Story 1 (T021-T032) - Automated workflow
4. ✅ Complete Phase 4: User Story 2 (T033-T058) - Statistics generation
5. **STOP and VALIDATE**: Manually trigger GitHub Actions workflow, verify all SVGs generate correctly
6. Deploy/demo with working automated statistics generation

**MVP Scope**: US1 + US2 delivers core value - automated GitHub statistics with SVG visualizations

### Incremental Delivery

1. Foundation (Phases 1-2) → Infrastructure ready
2. Add US1 → Test workflow trigger → **Deploy** (automation works!)
3. Add US2 → Test statistics accuracy → **Deploy** (full MVP with visualizations!)
4. Add US3 → Test theme switching → **Deploy** (customization available)
5. Add US4 → Test selective output → **Deploy** (performance optimization)
6. Add US5 → Test local CLI → **Deploy** (developer experience enhancement)
7. Add US6 → Validate documentation → **Deploy** (complete with guides)
8. Polish (Phase 9) → Final quality pass → **Production Ready**

### Parallel Team Strategy

With multiple developers:

1. **Together**: Complete Setup + Foundational (Phases 1-2)
2. **After Foundational completes**:
   - Developer A: User Story 1 (Workflow automation)
   - Developer B: User Story 3 (Themes - independent)
   - Developer C: User Story 5 (CLI - independent)
3. **After US1 completes**:
   - Developer A: User Story 2 (Statistics - builds on US1)
   - Developer B: Continue US3
   - Developer C: Continue US5
4. **After US2 completes**:
   - Developer A: User Story 4 (Selective output - builds on US2)
   - Developer B: User Story 6 (Documentation - needs working system)
5. **All together**: Phase 9 Polish

---

## Notes

- [P] tasks = different files OR independent functions within files (use git branches for parallel work)
- [Story] label maps task to specific user story (US1, US2, etc.) for traceability
- Each user story should be independently testable after completion
- Commit after each task or logical group of related tasks
- Stop at each checkpoint to validate user story functionality
- **File path specificity**: Every implementation task includes exact file path and class/function name
- **markhazleton demo**: Create actual working examples in Phase 8 for documentation
- **No tests phase**: Tests are handled in Phase 9 Polish since not explicitly required in spec
- **MVP = US1 + US2**: Focus on automated generation and comprehensive statistics first

---

## Total Task Count: 127 tasks

**By Phase**:
- Phase 1 (Setup): 9 tasks
- Phase 2 (Foundational): 11 tasks (CRITICAL BLOCKER)
- Phase 3 (US1 - Automated Generation): 12 tasks
- Phase 4 (US2 - Comprehensive Stats): 31 tasks (added 5 test tasks + deleted repo handling)
- Phase 5 (US3 - Theme Customization): 9 tasks (added WCAG test task)
- Phase 6 (US4 - Selective Output): 10 tasks
- Phase 7 (US5 - Local CLI): 10 tasks
- Phase 8 (US6 - Documentation): 12 tasks
- Phase 9 (Polish): 23 tasks (added 4 test/validation tasks)

**By User Story**:
- US1 (P1): 12 tasks
- US2 (P1): 31 tasks (includes test coverage)
- US3 (P2): 9 tasks (includes WCAG validation test)
- US4 (P2): 10 tasks
- US5 (P3): 10 tasks
- US6 (P2): 12 tasks

**Parallel Opportunities**:
- Setup: 7 tasks can run in parallel
- Foundational: 9 tasks can run in parallel (after T010-T011)
- User Stories: US1, US3, US5 can start in parallel after Foundational
- Polish: 19 tasks can run in parallel

**Suggested MVP**: Phases 1-4 (Setup + Foundational + US1 + US2) = 63 tasks for fully automated statistics generation with test coverage

**Constitution Compliance**: Test tasks now paired with implementation (T058b-e, T065a, T109-T114, T118) to meet Principle IV >80% coverage requirement
