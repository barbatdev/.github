# Project Lifecycle

This framework records why a project exists, who can sustain it, and what evidence supports its next state. It guides portfolio decisions without prescribing product implementation.

## Purpose, scope, and non-goals

Use this framework to propose, prioritize, sustain, pause, and close RefactorIA projects. It covers portfolio decisions, continuity, and recorded exceptions.

It does not prescribe architecture, dependencies, versions, implementation, testing, continuous integration, branch controls, deployment, operational security, incident handling, releases, or version support. Those decisions and their evidence belong to the product repository.

## Lifecycle states

| State | Meaning | Minimum entry evidence | Exit evidence |
| --- | --- | --- | --- |
| Proposed | A need or opportunity is awaiting evaluation. | Initial purpose and context are recorded. | Priority assessment and decision are recorded. |
| Incubating | A bounded hypothesis is being tested. | Accountable owner, initial scope, and learning criterion are identified. | Validation result and a decision to continue, pause, deprecate, or archive. |
| Active | The project delivers value and receives planned attention. | Current purpose, accountable ownership, and sustained capacity. | A review of continuity, scope, or maintenance needs. |
| Maintenance | Stable value is preserved through limited change. | Maintenance boundaries and accountability are clear. | A decision to reactivate, pause, or deprecate. |
| Paused | Active work is not currently expected. | Reason, review condition, and known state are recorded. | A decision to reactivate, deprecate, or archive. |
| Deprecated | Retirement is being communicated for a project or capability. | Reason, future boundaries, and user guidance are recorded. | Closure evidence and an archive decision. |
| Archived | The active lifecycle is complete and the project remains historical record. | Closure decision and final-state reference are recorded. | No direct exit. A distinct effort begins as Proposed. |

## Visibility is separate

Publication and visibility are independent of lifecycle status. A project in any state may be public, non-public, or pending publication. Publication requires an [OSS readiness](OSS_READINESS.md) assessment; it does not make a project Active.

## Allowed transitions

| From | To | Confirm before deciding |
| --- | --- | --- |
| Proposed | Incubating, Paused, Archived | Priority, capacity, and decision rationale. |
| Incubating | Active, Paused, Deprecated, Archived | Learning outcome, expected value, and viable continuity. |
| Active | Maintenance, Paused, Deprecated | Current value, future burden, and required communication. |
| Maintenance | Active, Paused, Deprecated | Changed priority, capacity, or need. |
| Paused | Active, Deprecated, Archived | Changed condition and available accountability. |
| Deprecated | Archived | Communicated closure and preserved references. |

Do not skip states to avoid the evidence required by a decision. A new opportunity after archival starts as a new proposal.

## Intake and portfolio review

Before starting or reactivating work, consider these factors. They inform judgment; they are not an automatic score.

| Factor | Review question |
| --- | --- |
| Mission alignment | Does the work clearly advance the community's purpose? |
| User and community value | Does it solve a problem or enable meaningful learning? |
| Accountable ownership and capacity | Is someone accountable with realistic capacity? |
| Legal, privacy, and security readiness | Are the conditions to proceed or publish understood? |
| Dependency leverage | Does it reuse useful work without creating unjustified coupling? |
| Reversibility and maintenance burden | Can it be adapted or closed at a reasonable cost? |

New evidence may change priority. Record the reason and its effect on lifecycle status.

## Continuity and authority

The [Owner and RefactorIA Coordinator responsibilities](REFACTORIA_TEAM.md) govern final decisions, priorities, and follow-through. This document references those responsibilities and does not redefine them.

| Continuity condition | Decision |
| --- | --- |
| Responsible continuity exists | Transfer accountability with the necessary context. |
| The community can sustain the work | Designate it community-maintained with explicit boundaries. |
| Capacity is temporarily unavailable | Pause it and define a review condition. |
| Value or viability has ended | Deprecate or archive it. |

## Evidence and exceptions

Record lifecycle decisions, supporting evidence, and exceptions through the existing [GitHub governance](GITHUB_GOVERNANCE.md) process. An exception explains context; it does not remove accountability or required evidence.

## Transition checklist

- [ ] The source state is confirmed.
- [ ] Purpose and scope remain understandable.
- [ ] Priority, value, capacity, and maintenance burden were reviewed.
- [ ] Required entry or exit evidence is recorded.
- [ ] Continuity accountability is clear.
- [ ] The decision and any exception follow GitHub governance.
- [ ] Public publication, if planned, has an OSS readiness assessment.
