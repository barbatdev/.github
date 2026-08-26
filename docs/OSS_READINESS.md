# OSS Readiness

A project is ready for open-source publication only when every gate below has sufficient evidence and publication has been explicitly decided. The outcome is always `Ready` or `Blocked`.

## Portable publication decision

This is a portable framework for projects. It defines what must be demonstrated, not the implementation tools, configurations, or exact evidence. Each product repository selects and maintains its own controls and evidence tooling.

This guidance is not legal advice. It does not replace product-repository decisions about security, privacy, support, or maintenance.

| Outcome | When it applies | Next action |
| --- | --- | --- |
| `Ready` | Every gate has sufficient evidence and publication is explicitly approved. | Continue through the product repository's publication process. |
| `Blocked` | Evidence is missing, a gate is unmet, or no publication decision exists. | Record the blocker and resolve it before publication. |

## Publication gates

| Gate | What must be demonstrated |
| --- | --- |
| Public purpose and boundaries | A public audience can understand the purpose, scope, and non-goals. |
| Accountable ownership | Accountability for decisions and continuity is identified. |
| License and attribution | The applicable license and required attribution are defined. |
| Provenance and right to publish | The repository has the right to publish included content, materials, and contributions. |
| Privacy and data | No secrets, personal data, or information unsuitable for public release is exposed. |
| Public routes | A public README and accessible contribution and security-reporting routes exist. |
| Support and maintenance boundaries | Public support, maintenance, and expectation boundaries are clear. |
| Proportional verification evidence | Verification evidence and known limits are proportionate to the work. |
| Repository and history hygiene | Publishable content and history do not contain information that must remain private. |
| Explicit publication decision | The applicable authority has recorded the decision. |

These are publication conditions, not product prescriptions. The product repository chooses its architecture, dependencies, versions, implementation, tests, continuous integration, deployment, operational security, incident handling, releases, and version support.

## Exceptions

A recorded exception may explain proportional evidence or a particular condition. It cannot waive license or right-to-publish requirements, secrets or privacy protection, or an accessible security reporting route.

## Responsibilities

| Topic | RefactorIA | Product repository |
| --- | --- | --- |
| Portfolio framework | Defines the shared lifecycle and readiness criteria. | Provides its project context and evidence. |
| Publication decision | Maintains governance and applies the established decision authority. | Prepares a reviewable decision with evidence. |
| Implementation and verification | Does not prescribe tools or configuration. | Selects, applies, and documents controls and evidence tooling. |
| Security and privacy | Requires a public reporting route and prevents protected information from publication. | Implements controls, handles incidents, and maintains its applicable reporting route. |
| Maintenance and support | Requires public boundaries to be communicated. | States and sustains its product and version boundaries. |

Consult the [RefactorIA Team Charter](REFACTORIA_TEAM.md) for decision responsibilities, [GitHub governance](GITHUB_GOVERNANCE.md) for decision and exception records, and the applicable [Security Policy](../SECURITY.md) for vulnerability reporting.

## Maintainer checklist

- [ ] Purpose, scope, and non-goals are public and clear.
- [ ] Accountable ownership and continuity capacity are identified.
- [ ] License, attribution, provenance, and right to publish are reviewed.
- [ ] Privacy review confirms that no secrets or personal data will be published.
- [ ] A public README and accessible contribution and security-reporting routes exist.
- [ ] Support and maintenance boundaries are communicated.
- [ ] Proportional verification evidence and known limits are recorded.
- [ ] Repository content and history are suitable for publication.
- [ ] The publication decision is recorded.
- [ ] Any exception preserves license, right-to-publish, secrets, privacy, and security-reporting requirements.

If any item cannot be confirmed, the outcome is `Blocked`.
