# Coverage catalog

D IDs are internal identifiers, not external controls. Screen every row in a baseline; deepen according to business significance. Evidence below is to seek, not assumed present.

| ID | Discipline / scope | Evidence and outcome |
|---|---|---|
| D01 | Business/product: journeys, capabilities, differentiation, roadmap, buy/build, expansion. | Capability map, customer commitments, economics; business alignment. |
| D02 | Application/domain: invariants, boundaries, coupling, transactions, concurrency, change locality. | Code paths, dependency map, change history; safe evolution. |
| D03 | SaaS tenancy/lifecycle: hierarchy, isolation, onboarding, quotas, entitlements, migration, restore/offboarding. | Isolation tests, async/cache paths, lifecycle records. |
| D04 | Frontend/UX: task success, state/recovery, browser/mobile, design system, performance. | User journeys, browser traces, usability evidence. |
| D05 | Accessibility/i18n: assistive technology, keyboard, locale/language, currency, units, time zones, communications. | Manual/automated checks, locale matrix, pseudo-localization. |
| D06 | API/integration: contracts, versions, webhooks, replay, idempotency, interoperability, deprecation. | Specs, compatibility tests, failures, partner onboarding. |
| D07 | Identity/admin: enterprise/consumer identities, federation, provisioning, delegation, revocation, support. | Relationship/role matrix, access tests/reviews, service policies. |
| D08 | Security: threats, secrets, privilege, supply chain, abuse, vulnerabilities, blast radius. | Threat models, deployed policies, provenance, remediation. |
| D09 | Privacy/governance: purpose, roles, classification, retention, deletion, consent, residency/transfers. | Processing inventory, rights-request evidence, data flows. |
| D10 | Compliance/audit: applicability, controls/evidence, finance scope, segregation, audit events. | Control matrix, period evidence, exceptions, escalation. |
| D11 | Operational data: models, integrity, consistency, indexes, partitions, migrations, durability/recovery. | Constraints, query plans, migration rehearsal, restore results. |
| D12 | Data engineering/analytics: ingestion, contracts, lineage, quality, replay, reconciliation, metrics. | Pipeline runs, quality trends, reporting reconciliation. |
| D13 | Infrastructure/cloud: hierarchy, network, IaC, drift, runtime, configuration, geography. | GCP inventory, deployment state, policy/network evidence. |
| D14 | Reliability/resilience: journey SLOs, dependency failures, recovery, failover, continuity. | Customer-impact metrics, incidents, recovery exercises. |
| D15 | Performance/scale: p95/p99, throughput, capacity, fairness, queues, saturation, load costs. | Representative load results, scaling and bottlenecks. |
| D16 | Observability/operations/support: telemetry, alerting, on-call, diagnostics, runbooks, toil. | Incident timeline, tenant diagnostics, support trends. |
| D17 | Quality/delivery: tests, environments, CI/CD, provenance, approvals, flags, migrations, rollback. | Delivery/failure trends, release evidence, recovery demonstrations. |
| D18 | Platform/DX: self-service, local development, platform interfaces, adoption, cognitive load. | Developer research, first-change time, exceptions. |
| D19 | Economics/commercialization/sustainability: usage, pricing, allocation, margin, billing, efficiency. | Unit costs, usage-to-invoice reconciliation, resource measures. |
| D20 | Governance/knowledge/leadership: decision rights, docs/ADRs, ownership, debt, succession, investment. | Decisions/outcomes, onboarding, roadmap, coaching commitments. |
| X01 | AI/ML: use case, evaluation, provenance, access, tools, oversight, drift, economics. | Evaluation suite, traces, authorized data, rollback, outcome measures. |

## Quality overlay

Use scenarios for correctness; performance; scalability/elasticity; availability/reliability; resilience/recoverability; durability/integrity; security/privacy; usability/accessibility; compatibility/interoperability; maintainability/evolvability; testability/observability/operability; portability/replaceability; auditability/explainability; efficiency/sustainability. They cross disciplines; avoid duplicate scorecards.

Durability is survival of accepted data. Replication does not by itself protect against logical corruption. Availability is not integrity; region count does not prove recovery. Assess documentation by whether a new team member can reason, operate, and change safely.

Add functional-safety and product-security specialist assessment only for actual safety-relevant vehicle functions. Dealer scheduling and changing vehicle behavior have different assurance needs.
