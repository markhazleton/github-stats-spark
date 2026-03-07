# Tasks: Audit High-Issue Remediation

**Input**: Design documents from `/.documentation/specs/001-remediate-high-issues/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Automated verification is required by the feature specification, so story-specific regression and coverage tasks are included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., [US1], [US2], [US3])
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the shared verification scaffolding required by multiple stories.

- [X] T001 Create shared remediation fixtures in tests/unit/conftest.py
- [X] T002 [P] Create CLI regression harness in tests/unit/test_cli.py
- [X] T003 [P] Create unified workflow regression harness in tests/unit/test_unified_report_workflow.py
- [X] T004 [P] Create dashboard generator regression harness in tests/unit/test_dashboard_generator.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Extract the low-risk helper boundaries that later story work will build on.

**⚠️ CRITICAL**: User Stories 1 and 2 should not begin until this phase is complete.

- [X] T005 Create CLI output path helpers in src/spark/cli_output_layout.py
- [X] T006 [P] Create CLI parser builder helpers in src/spark/cli_argument_builders.py
- [X] T007 [P] Create shared repository filtering helper in src/spark/cache_repository_filter.py
- [X] T008 [P] Create cache refresh strategy coordinator in src/spark/cache_refresh_strategy.py
- [X] T009 Update src/spark/cli.py to consume src/spark/cli_output_layout.py and src/spark/cli_argument_builders.py
- [X] T010 Update src/spark/cache_manager.py to consume src/spark/cache_repository_filter.py and src/spark/cache_refresh_strategy.py

**Checkpoint**: Shared helper boundaries exist and regression harnesses are in place.

---

## Phase 3: User Story 1 - Reliable Generated Outputs (Priority: P1) 🎯 MVP

**Goal**: Ensure generated outputs honor configured theme selection and report correct dashboard aggregate totals.

**Independent Test**: Run `spark config --validate`, then run `spark unified --user markhazleton --max-repos 2 --verbose` and confirm generated outputs use the configured theme while dashboard totals match the included repositories.

### Tests for User Story 1

- [X] T011 [P] [US1] Add configured theme regression cases in tests/unit/test_config.py
- [X] T012 [P] [US1] Add unified workflow theme application cases in tests/unit/test_unified_report_workflow.py
- [X] T013 [P] [US1] Add dashboard aggregate total cases in tests/unit/test_dashboard_generator.py

### Implementation for User Story 1

- [X] T014 [US1] Update src/spark/unified_report_workflow.py to resolve themes from configuration through shared theme loaders
- [X] T015 [US1] Update src/spark/dashboard_generator.py to compute total_stars and total_forks from included repositories
- [X] T016 [US1] Update src/spark/visualizer.py to enforce consistent invalid-theme handling for workflow consumers

**Checkpoint**: User Story 1 is independently testable and delivers configuration-correct, aggregate-correct outputs.

---

## Phase 4: User Story 2 - Constitution-Aligned Quality Gates (Priority: P1)

**Goal**: Raise calculation and visualization verification to the constitutional threshold and reduce single-responsibility pressure in the highest-risk backend orchestration paths.

**Independent Test**: Run `pytest tests/unit/test_calculator.py tests/unit/test_visualizer.py tests/unit/test_cli.py tests/unit/test_cache_manager.py`, then run `pytest --cov=spark --cov-report=html` and confirm the calculation and visualization modules clear the constitutional gate while the refactored CLI and cache paths still behave identically.

### Tests for User Story 2

- [X] T017 [US2] Expand constitutional-gate coverage in tests/unit/test_calculator.py and tests/unit/test_visualizer.py
- [X] T018 [P] [US2] Add cache-manager delegation regression cases in tests/unit/test_cache_manager.py
- [X] T019 [P] [US2] Add CLI delegation and dispatch regression cases in tests/unit/test_cli.py

### Implementation for User Story 2

- [X] T020 [US2] Refactor src/spark/cli.py to delegate parser construction and output layout responsibilities
- [X] T021 [US2] Refactor src/spark/cache_manager.py to delegate repository filtering and refresh coordination
- [X] T022 [US2] Refine refresh strategy implementations in src/spark/cache_refresh_strategy.py to preserve existing cache contracts
- [X] T023 [US2] Simplify component initialization and orchestration boundaries in src/spark/unified_report_workflow.py

**Checkpoint**: User Story 2 is independently testable and clears the in-scope architectural and coverage findings.

---

## Phase 5: User Story 3 - Governance-Aligned Documentation and Tooling (Priority: P2)

**Goal**: Make documentation ownership and feature, audit, and upgrade workflow structure explicit so contributors can follow one supported operating model.

**Independent Test**: Review the documentation entry points and Speckit guidance files, then verify that contributors can locate feature artifacts under `.documentation/specs/`, user-facing guides under `documentation/`, and upgrade guidance in the supported workflow structure without relying on undocumented exceptions.

### Implementation for User Story 3

- [X] T024 [P] [US3] Update .github/copilot-instructions.md to align feature artifact paths and documentation ownership rules
- [X] T025 [P] [US3] Update documentation/README.md to document user-facing guides versus Speckit artifacts
- [X] T026 [P] [US3] Update docs/README.md to label deployment README ownership and exception handling
- [X] T027 [P] [US3] Update output/README.md to label generated-output README ownership and exception handling
- [X] T028 [P] [US3] Update frontend/README.md to clarify whether it is user-facing documentation or an approved exception
- [X] T029 [US3] Align audit workflow guidance with the supported structure in .github/agents/speckit.site-audit.agent.md
- [X] T030 [US3] Align upgrade workflow guidance with the supported structure in .github/agents/speckit.upgrade.agent.md

**Checkpoint**: User Story 3 is independently reviewable and resolves the documentation/tooling governance path ambiguity.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Run end-to-end validation and capture completion evidence across all stories.

- [X] T031 [P] Update validation steps and expected outcomes in .documentation/specs/001-remediate-high-issues/quickstart.md
- [X] T032 Record post-implementation verification evidence in .documentation/specs/001-remediate-high-issues/research.md
- [X] T033 [P] Save a follow-up audit report in .documentation/copilot/audit/2026-03-07_followup-high-findings-remediation-check.md
- [X] T034 Document final completion notes and gate status in .documentation/specs/001-remediate-high-issues/plan.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; start immediately.
- **Foundational (Phase 2)**: Depends on Setup completion; blocks User Stories 1 and 2.
- **User Story 1 (Phase 3)**: Depends on Phase 2 completion.
- **User Story 2 (Phase 4)**: Depends on Phase 2 completion.
- **User Story 3 (Phase 5)**: Depends on Phase 1 completion so the canonical `.documentation/specs/` feature path and shared scaffolding are in place, and can proceed independently of runtime refactoring once that prerequisite is satisfied.
- **Polish (Phase 6)**: Depends on all desired user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: No dependency on other user stories after foundational helper extraction is complete.
- **User Story 2 (P1)**: No dependency on User Story 1, but shares the foundational helper work and verification scaffolding.
- **User Story 3 (P2)**: No dependency on User Stories 1 or 2 after Phase 1 is complete; it depends on the canonical `.documentation/specs/` feature path and shared scaffolding created during setup.

### Within Each User Story

- Regression tests should be written before the corresponding implementation changes.
- Helper modules before delegation updates.
- Configuration and data fixes before end-to-end validation.
- Documentation classification before follow-up audit capture.

### Parallel Opportunities

- T002, T003, and T004 can run in parallel after T001.
- T006, T007, and T008 can run in parallel after Phase 1.
- T011, T012, and T013 can run in parallel inside User Story 1.
- T018 and T019 can run in parallel with different test files inside User Story 2.
- T024 through T028 can run in parallel across separate documentation files inside User Story 3.
- T031 and T033 can run in parallel during polish.

---

## Parallel Example: User Story 1

```bash
# Launch the User Story 1 regression tasks together:
Task: "Add configured theme regression cases in tests/unit/test_config.py"
Task: "Add unified workflow theme application cases in tests/unit/test_unified_report_workflow.py"
Task: "Add dashboard aggregate total cases in tests/unit/test_dashboard_generator.py"
```

## Parallel Example: User Story 3

```bash
# Launch the documentation-classification tasks together:
Task: "Update documentation/README.md to document user-facing guides versus Speckit artifacts"
Task: "Update docs/README.md to label deployment README ownership and exception handling"
Task: "Update output/README.md to label generated-output README ownership and exception handling"
Task: "Update frontend/README.md to clarify whether it is user-facing documentation or an approved exception"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup.
2. Complete Phase 2: Foundational.
3. Complete Phase 3: User Story 1.
4. **STOP and VALIDATE**: Run the User Story 1 independent test flow from quickstart.
5. Demo configuration-correct output generation before moving on.

### Incremental Delivery

1. Finish Setup + Foundational to create safe extraction seams.
2. Deliver User Story 1 to restore trustworthy generated outputs.
3. Deliver User Story 2 to clear quality-gate and architecture findings.
4. Deliver User Story 3 to close documentation/tooling governance gaps.
5. Finish with a follow-up audit and recorded verification evidence.

### Parallel Team Strategy

1. One developer handles the foundational helper extractions in `src/spark/cli/` and `src/spark/cache/`.
2. One developer handles User Story 1 runtime fixes and tests.
3. One developer handles User Story 3 documentation and workflow guidance updates.
4. User Story 2 consolidation starts once the helper extractions land.

---

## Notes

- [P] tasks target separate files and avoid incomplete-task dependencies.
- [US1], [US2], and [US3] map directly to the user stories in spec.md.
- The MVP scope is **User Story 1** because it restores trustworthy generated output with the smallest deliverable slice.
- Follow-up audit evidence is required to close the feature.