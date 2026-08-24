# GitHub Governance

GitHub is the public record for proposals, changes, technical decisions, and review evidence. Community coordination may happen elsewhere, but decisions that affect public work return here.

## Contribution path

1. Search public issues and pull requests for related work.
2. Open or contribute to an issue for every change, including documentation and maintenance work.
3. Wait for the `status:approved` label before implementation.
4. Assign the issue to yourself and comment with the plan.
5. Create a valid branch in your fork from `upstream/main`.
6. Implement and verify the change, keeping tests and documentation with the behavior they verify.
7. Open a focused pull request to `upstream/main` that closes the approved issue.
8. Select exactly one pull request type and use the matching `type:*` label.

If scope or requirements are unclear, ask in the issue before implementation. If work stops, comment with the current state, relevant evidence, and remaining work, then unassign the issue.

## Public snapshot: 2026-08-23

The following table records public observations as of this date.

| Repository | Default branch | Public protection | SPDX license observed | Community health |
| --- | --- | --- | --- | --- |
| `.github` | `main` | Publicly protected | No SPDX license observed | 75% |
| `presupuestos` | `main` | Publicly protected | MIT | 87% |
| `refactor-ia.github.io` | `main` | Publicly protected | No SPDX license observed | 75% |

- All three repositories were publicly observed as public and unarchived.
- Effective public README, CONTRIBUTING, and pull request template coverage was observed where applicable.
- A central public [SECURITY policy](https://github.com/refactor-ia/.github/security/policy) was present.
- No central public Code of Conduct or Support file was observed.
- This snapshot makes no inference about private configuration.

This snapshot is not an audit of private configuration or access. It does not establish product, security, or operational claims beyond what public pages can show.

## Desired public policy

### Issues

- Describe the problem, scope, acceptance criteria, and relevant context.
- Search for duplicates and related work before opening a new issue.
- Every change, including documentation and maintenance work, requires an issue.
- Wait for `status:approved` before implementation.
- Assign the issue and comment with the implementation plan before starting work.
- Treat an issue as a record of work, not as a grant of authority or priority.
- Keep sensitive reports out of public issues and follow the [public SECURITY policy](https://github.com/refactor-ia/.github/security/policy).

### Pull requests

- Work from a valid fork branch based on `upstream/main`.
- Open a focused pull request to `upstream/main` that closes the approved issue with `Closes #N` when the work is complete.
- Explain what changes and why, including documentation and maintenance work.
- Select exactly one pull request type in the template and use the matching `type:*` label.
- Keep technical discussion in the pull request so the decision remains reviewable.
- Review scope, security, maintainability, tests, and documentation.

### Review and merge

| Decision | Desired public criterion |
| --- | --- |
| Review | Adds concrete evidence or objections; it does not replace the merge decision. |
| Merge | An authorized merge decision follows when the goal and evidence are sufficient. |
| Disagreement | Records reasons and alternatives so the final decision retains context. |
| Automation | Uses stable, relevant checks rather than process for its own sake. |
| Shared guidance | Is maintained centrally when useful; repositories add their own rules. |

Do not use process to block a contribution without a verifiable reason. Record exceptions in the change context.

## Not publicly verifiable

Public information cannot confirm exact branch rules, approval or check requirements, merge behavior, access permissions, internal automation, or sensitive security operations. Those details remain outside this documentation. This guide describes desired public process, not private configuration.

## Contribution checklist

- [ ] Related issues and pull requests were reviewed for duplicate or related work.
- [ ] An issue exists for this change, including documentation or maintenance work.
- [ ] The issue has `status:approved` before implementation.
- [ ] The issue is assigned and includes a commented implementation plan.
- [ ] The work uses a valid fork branch based on `upstream/main`.
- [ ] The pull request closes the approved issue with `Closes #N`.
- [ ] Exactly one pull request type and matching `type:*` label are selected.
- [ ] Evidence is proportionate to the change.
- [ ] Affected documentation is current.
- [ ] Sensitive matters follow SECURITY and are not exposed publicly.
