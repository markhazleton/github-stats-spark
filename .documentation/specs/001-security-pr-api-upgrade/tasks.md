# Tasks: Repository Security and PR Signals

**Input**: Design documents from `/.documentation/specs/001-security-pr-api-upgrade/`
**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/repositories-json.md`, `quickstart.md`

**Tests**: Add backend tests for pull request enrichment, security enrichment, partial-availability handling, and staged API-version behavior because the specification defines independent test criteria for each story and the repository requires regression coverage for core modules.

**Organization**: Tasks are grouped by user story to preserve independent implementation and validation for each increment.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel when the referenced files do not overlap and prerequisite tasks are complete
- **[Story]**: Maps the task to a specific user story from `spec.md` (`[US1]`, `[US2]`, `[US3]`)
- Each task includes the exact file path that should be updated or created

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare reusable fixtures and validation inputs for the new repository enrichment work.

- [ ] T001 Extend repository enrichment fixture coverage in `tests/fixtures/sample_repositories.json`
- [ ] T002 [P] Add staged API-version and partial-access configuration samples in `tests/fixtures/sample_config.yml`
- [ ] T003 [P] Add schema-consumer adoption notes for PR and security summaries in `documentation/guides/unified-pipeline.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Establish shared models, cache behavior, and request plumbing required by all user stories.

**Critical**: No user story work should start until these tasks are complete.

- [ ] T004 Extend repository enrichment models and serialization helpers in `src/spark/models/repository.py`
- [ ] T005 [P] Add repository-scoped enrichment cache helpers in `src/spark/cache_manager.py` using `pushed_at`-keyed invalidation, no TTL refresh, and force-refresh bypass support
- [ ] T006 [P] Add GitHub REST API version request plumbing and shared enrichment helpers in `src/spark/fetcher.py`
- [ ] T007 Wire schema-version bump support for additive repository fields in `src/spark/unified_data_generator.py`
- [ ] T008 [P] Create privacy regression coverage proving private repositories never reach PR or security enrichment in `tests/unit/test_fetcher.py`

**Checkpoint**: Shared enrichment infrastructure is ready for story-specific implementation.

---

## Phase 3: User Story 1 - Enriched Repository Signals (Priority: P1)

**Goal**: Add compact pull request and security summaries to every included public repository record.

**Independent Test**: Run unified generation for an account with open pull requests and visible security signals, then verify every repository record contains `pull_request_summary` and `security_summary` with a zero, clear, or populated state.

### Tests for User Story 1

- [ ] T009 [P] [US1] Create pull request and security enrichment unit coverage in `tests/unit/test_fetcher.py`
- [ ] T010 [P] [US1] Add unified repository enrichment integration coverage in `tests/integration/test_unified_repository_enrichment.py`

### Implementation for User Story 1

- [ ] T011 [US1] Implement compact open pull request summary collection in `src/spark/fetcher.py`
- [ ] T012 [US1] Implement repository security signal and alert-count collection in `src/spark/fetcher.py`
- [ ] T013 [P] [US1] Add repository summary serialization for `pull_request_summary` and `security_summary` in `src/spark/models/repository.py`
- [ ] T014 [US1] Populate repository enrichment summaries during assembly in `src/spark/unified_data_generator.py`
- [ ] T015 [US1] Preserve additive schema metadata for the new repository fields in `src/spark/unified_data_generator.py`

**Checkpoint**: User Story 1 is complete when enriched repository data is generated without removing or renaming existing repository fields.

---

## Phase 4: User Story 2 - Transparent Partial Availability (Priority: P2)

**Goal**: Distinguish confirmed clear states from permission gaps, endpoint limitations, and per-repository enrichment failures.

**Independent Test**: Run unified generation with credentials that cannot read all security sources and confirm repositories still emit `security_summary` and `pull_request_summary` objects with explicit `availability` and `reason` values.

### Tests for User Story 2

- [ ] T016 [P] [US2] Add availability-state unit coverage for partial and unavailable enrichment in `tests/unit/test_repository_enrichment_status.py` *(requires T004 and T013 for model definitions)*
- [ ] T017 [P] [US2] Add partial-result integration coverage in `tests/integration/test_unified_repository_partial_enrichment.py` *(requires T004 and T013 for model definitions)*

### Implementation for User Story 2

- [ ] T018 [US2] Classify permission, unsupported, and API failure outcomes into repository enrichment reasons in `src/spark/fetcher.py`
- [ ] T019 [US2] Persist explicit partial and unavailable repository summaries during assembly in `src/spark/unified_data_generator.py`
- [ ] T020 [P] [US2] Surface enrichment warnings and partial-result logging in `src/spark/unified_report_workflow.py`
- [ ] T021 [P] [US2] Document access requirements, availability semantics, and schema adoption guidance in `documentation/guides/unified-pipeline.md`

**Checkpoint**: User Story 2 is complete when partial data stays trustworthy, observable, and clearly distinguishable from zero findings.

---

## Phase 5: User Story 3 - API Upgrade Readiness (Priority: P3)

**Goal**: Stage GitHub REST API version `2026-03-10` adoption behind explicit configuration, validation, and rollout documentation.

**Independent Test**: Enable the explicit `2026-03-10` request path, verify generation still succeeds, and confirm the upgrade guidance identifies affected paths, breaking-change checks, and fallback behavior.

### Tests for User Story 3

- [ ] T022 [P] [US3] Add GitHub REST API version behavior coverage in `tests/unit/test_fetcher_api_version.py`

### Implementation for User Story 3

- [ ] T023 [P] [US3] Add GitHub REST API version configuration in `config/spark.yml`
- [ ] T024 [US3] Read staged GitHub REST API version settings in `src/spark/config.py`
- [ ] T025 [US3] Apply `2026-03-10` request headers and fallback logging in `src/spark/fetcher.py`
- [ ] T026 [US3] Emit staged API-upgrade assessment conclusions in logs or generation metadata in `src/spark/unified_report_workflow.py`
- [ ] T027 [P] [US3] Document rollout gates, breaking changes, and fallback decisions in `documentation/api/api-reference.md`

**Checkpoint**: User Story 3 is complete when the staged version path is configurable, validated, and documented without forcing a full cutover.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Finalize documentation, runtime validation, and release readiness across all stories.

- [ ] T028 [P] Add runtime-budget instrumentation or explicit budget-exceeded reporting for enrichment runs in `src/spark/unified_report_workflow.py`
- [ ] T029 [P] Update quickstart validation steps for repository enrichment and staged API rollout in `documentation/quickstart/QUICKSTART_UNIFIED.md`
- [ ] T030 [P] Update release notes for schema version `2.1.0` and enrichment behavior in `documentation/CHANGELOG.md`
- [ ] T031 Validate runtime, cache reuse, force-refresh behavior, and mitigation reporting against `.documentation/specs/001-security-pr-api-upgrade/quickstart.md`
- [ ] T032 [P] Verify enrichment code in `src/spark/fetcher.py`, `src/spark/models/repository.py`, and `src/spark/unified_data_generator.py` meets >80% line coverage per constitution quality gates

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies and can start immediately.
- **Foundational (Phase 2)**: Depends on Setup completion and blocks all user stories.
- **User Story 1 (Phase 3)**: Starts after Foundational and delivers the MVP repository enrichment payload.
- **User Story 2 (Phase 4)**: Starts after Foundational and builds on the enrichment payload to make partial results explicit and trustworthy.
- **User Story 3 (Phase 5)**: Starts after Foundational and can proceed in parallel with later US1 or US2 finishing work when file conflicts are avoided.
- **Polish (Phase 6)**: Starts after the desired user stories are complete.

### User Story Dependencies

- **US1**: Depends on Phase 2 only.
- **US2**: Depends on Phase 2 and the US1 enrichment objects existing in the repository contract.
- **US3**: Depends on Phase 2 only.

### Constitution-Sensitive Dependencies

- Privacy regression task T008 must complete before closing any enrichment implementation in `src/spark/fetcher.py` or `src/spark/unified_data_generator.py`.
- Cache task T005 must complete before runtime validation so the quickstart checks exercise the approved `pushed_at` invalidation behavior.
- Runtime reporting task T028 and upgrade observability task T026 must complete before final validation so FR-013 and FR-014 are satisfied operationally.

### Within Each User Story

- Write and run the story tests before closing implementation tasks.
- Update shared models before relying on new fields in assembly code.
- Complete fetcher behavior before finalizing workflow logging and documentation for that story.
- Validate each story independently before moving to the next priority.

### Dependency Graph

- `Phase 1 -> Phase 2 -> US1 -> US2 -> Phase 6`
- `Phase 2 -> US3 -> Phase 6`

---

## Parallel Execution Examples

### User Story 1

```text
T009 tests/unit/test_fetcher.py
T010 tests/integration/test_unified_repository_enrichment.py
T013 src/spark/models/repository.py
```

### User Story 2

```text
T016 tests/unit/test_repository_enrichment_status.py
T017 tests/integration/test_unified_repository_partial_enrichment.py
T020 src/spark/unified_report_workflow.py
T021 documentation/guides/unified-pipeline.md
```

### User Story 3

```text
T022 tests/unit/test_fetcher_api_version.py
T023 config/spark.yml
T027 documentation/api/api-reference.md
```

---

## Implementation Strategy

### MVP First

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3 for User Story 1.
3. Validate unified generation against the User Story 1 independent test.
4. Stop after US1 if only the MVP repository enrichment payload is required.

### Incremental Delivery

1. Deliver US1 to add the new repository fields.
2. Deliver US2 to make missing data explicit and observable.
3. Deliver US3 to stage and document the API version upgrade path.
4. Finish with Phase 6 runtime and release validation.

### Parallel Team Strategy

1. One developer completes the shared foundational changes in `src/spark/models/repository.py`, `src/spark/cache_manager.py`, `src/spark/fetcher.py`, and `src/spark/unified_data_generator.py`.
2. After Phase 2, one developer can focus on US1 payload assembly while another handles US3 configuration and documentation.
3. US2 can start once the US1 enrichment objects are present and stable.

---

## Notes

- Parallel tasks are marked only when they target different files and do not depend on incomplete work in the same file.
- The task list keeps frontend dashboard changes out of scope because the approved plan treats frontend consumption as optional follow-up rather than core implementation.
- The feature is complete only after privacy regression coverage, runtime mitigation or budget-exceeded reporting, cache behavior, and force-refresh behavior are validated against the quickstart scenarios.