# Data Model

## AuditFinding

- **Purpose**: Represents one verified high-severity problem that this feature must remediate.
- **Fields**:
  - `id`: Stable finding identifier such as `CONF1` or `ARCH1`
  - `category`: Configuration, Accuracy, Documentation, Testability, or Architecture
  - `severity`: Priority level, constrained here to HIGH for in-scope work
  - `source_artifact`: Audit report or code path that established the finding
  - `target_outcome`: Observable condition that marks the finding resolved
  - `verification_method`: Audit rerun, unit test, config validation, or manual documentation review
- **Relationships**:
  - Belongs to one `RemediationScope`
  - Must be covered by at least one `QualityGate`

## RemediationScope

- **Purpose**: Defines the bounded set of findings and artifacts included in this feature.
- **Fields**:
  - `feature_id`: `001-remediate-high-issues`
  - `included_findings`: Ordered list of in-scope HIGH findings
  - `excluded_findings`: MEDIUM/LOW findings deferred unless required for safe remediation
  - `affected_areas`: Runtime code, tests, Speckit scripts, templates, and documentation guidance
  - `governance_rule`: Documentation and privacy constraints that must remain satisfied
- **Validation Rules**:
  - Must include exactly the six HIGH baseline findings
  - Must not expand into unrelated runtime or frontend redesign work

## QualityGate

- **Purpose**: Captures a measurable completion condition for one or more findings.
- **Fields**:
  - `name`: Coverage Gate, Accuracy Gate, Configuration Gate, Documentation Gate, or Audit Gate
  - `metric`: Numeric or boolean success indicator
  - `threshold`: Required pass value
  - `evidence_source`: Test report, generated output comparison, or audit result
  - `status`: Planned, Verified, or Blocked
- **Validation Rules**:
  - Coverage Gate must meet the constitutional threshold for core visualization work
  - Audit Gate must clear all in-scope HIGH findings

## DocumentationAsset

- **Purpose**: Represents a Markdown artifact whose ownership and placement must be explicit after remediation.
- **Fields**:
  - `path`: Current repository path
  - `owner_type`: Speckit artifact, project guide, generated output, or deployment metadata
  - `approved_location`: `.documentation/`, `documentation/`, or explicit exception list
  - `discoverability_entrypoint`: Where contributors are expected to find it
  - `status`: Approved, Reclassified, or Needs follow-up
- **Validation Rules**:
  - Every affected Markdown asset must be classified
  - Speckit planning artifacts for this feature must live under `.documentation/specs/001-remediate-high-issues/`

## VerificationRun

- **Purpose**: Records the validation evidence used to close the feature.
- **Fields**:
  - `type`: Unit test, config validation, unified run, or audit rerun
  - `command`: Executed verification command
  - `scope`: Targeted module, workflow, or documentation surface
  - `result`: Pass or Fail
  - `timestamp`: Execution time
- **Relationships**:
  - Can satisfy one or more `QualityGate` entries

## State Transitions

- **AuditFinding**: `Identified -> Planned -> In Progress -> Verified`
- **QualityGate**: `Planned -> Measured -> Verified`
- **DocumentationAsset**: `Discovered -> Classified -> Approved`
