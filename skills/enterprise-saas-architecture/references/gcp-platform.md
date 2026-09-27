# GCP architectural defaults

These are company-oriented starting preferences, not Google mandates. Consult current [official sources](sources.md) for capabilities, regional support, quotas, SLAs, pricing, and lifecycle status before making a deployment-specific recommendation. Use Google Cloud Well-Architected and enterprise foundations as reference structures; assess the application and organization as well as the cloud configuration.

## Decision defaults and exceptions

| Decision | Preferred starting point | Evidence that can justify an alternative |
|---|---|---|
| Application structure | Clear domain boundaries in the simplest deployable shape; a modular monolith is valid. | Independent ownership/scaling, fault containment, deployment cadence, or contractual boundaries justify service extraction. |
| Stateless HTTP/event workloads | Evaluate Cloud Run first for supported workload shapes. | Kubernetes APIs/operators, scheduling/network needs, specialized runtime, economics at sustained load, or existing platform investments can justify GKE. Validate current execution and connection limits. |
| Kubernetes | Evaluate GKE Autopilot when Kubernetes is justified. | Node/host control, privileged workloads, unsupported constraints, or measured economics can justify Standard. VMs remain valid for specific legacy/runtime constraints. |
| Operational relational data | Evaluate managed PostgreSQL, initially Cloud SQL; compare AlloyDB where requirements warrant it. | Distributed transactional scale/geography may justify Spanner; access patterns may justify document/key-value stores. Validate semantics, regional topology, cost, and migration effort. Never recommend Spanner solely because growth is expected. |
| Analytics | Evaluate BigQuery with governed definitions, data contracts, and cost controls. | Existing capabilities, specialized workloads, interoperability, or economics can favor another platform. An analytical store is not an automatic OLTP replacement. |
| Messaging | Pub/Sub for event distribution; evaluate task/workflow services for directed work and orchestration. | Ordering, delivery semantics, latency, integration constraints, and replay needs determine the choice. Business handlers still need idempotency and reconciliation. |
| Infrastructure | Declarative IaC, reviewed plans, environment separation, drift detection, reproducible changes. | Use the established supported toolchain; tool replacement needs measurable benefit. Version modules and provider dependencies. |
| Workload authentication | Short-lived identities; evaluate Workload Identity Federation for external CI/workloads and the supported GKE identity mechanism. | Document tightly bounded exceptions, rotation and exit plans for long-lived keys. Workforce and workload federation are different. |
| Delivery and artifacts | Existing trusted CI, Artifact Registry or equivalent, provenance/verification, controlled promotion, rollback. | Cloud Build/Cloud Deploy are candidates where they fit; no mandatory migration from a sound existing pipeline. |
| Observability | OpenTelemetry-compatible instrumentation, Cloud Logging/Monitoring or the established backend, service/tenant/region context. | Data residency, observability spend, sampling, and existing workflows influence backend choice. Avoid unbounded label cardinality and raw PII. |
| Network protection | Private service access/connectivity where justified; explicit ingress/egress paths and managed edge protections. | Public endpoints with strong application controls can be valid. Select Cloud Armor, IAP, API Gateway/Apigee, or service perimeters for specific threats/use cases, not a product checklist. |
| Secrets/encryption | Secret Manager and appropriate managed key services; narrow identities and rotation evidence. | Customer-managed keys when contractual, control, or threat requirements justify lifecycle/availability costs. Encryption alone is not isolation. |
| AI services | Evaluate GCP managed model/agent capabilities against the use case and existing model portfolio. | Model quality, data use, availability, residency, cost and evaluation results justify other providers. Verify current product/model names and terms. |
| Geography | Place data/compute based on customer latency, residency, transfers, failure objectives, and dependency locations. | Multi-region or dedicated deployments need an explicit value/risk case. Include DNS, identity, keys, CI, support and control-plane dependencies in recovery. |

## Foundation checks

Inspect organization/folder/project hierarchy, billing ownership, environment boundaries, organization policies, IAM inheritance, privileged access, resource inventory, network boundaries, logging ownership, keys, break-glass procedures and policy exceptions. A project is not automatically a tenant isolation boundary; a namespace is not proof of isolation either.

For every preventive policy ask where it is enforced, who can bypass/change it, what evidence detects drift, and whether emergency operation still works. Evaluate Shared VPC and centralized services against ownership and blast radius rather than treating centralization as universally better. Protect the deployment identity, IaC state, artifact repositories, and the audit evidence plane independently of application administrators where needed.

Cloud Audit Logs have distinct categories. Data Access logging needs explicit verification by service; it is generally disabled by default outside exceptions such as BigQuery. Inspect enablement, exclusions, routing, coverage, access and retention in deployed state. Cloud infrastructure logs do not replace business audit events such as consent changes, impersonation or pricing overrides. Reference: [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

For sensitive-data perimeters, verify supported services, ingress/egress policy, dry-run outcomes, and operational exceptions. Service perimeters are not substitutes for application authorization. For resilience, validate backup location, key access, restore permissions, infrastructure reconstruction, dependency recovery and tenant-level restoration—not just the managed service's availability claim.

## Decision output

Compare workload fit, operational burden, security/control evidence, region availability, scale behavior, full cost, team capability, portability, and reversibility. Include the current state as an option. Prefer standards at integration/data boundaries where they preserve useful options, without imposing a lowest-common-denominator multicloud layer. Produce an ADR for consequential choices and specify what evidence would change the recommendation.
