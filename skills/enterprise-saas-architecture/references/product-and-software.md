# Product and software assessment

## Product and domain (D01–D02)

Start from the decisions and journeys that deliver value. Map capability, owning team, business invariant and source of truth. Identify complexity caused by real domain differences versus accidental coupling. Inspect representative code paths and change history before recommending structure. Favor clear boundaries and local reasoning; service count and pattern conformance are not outcomes.

Ask how pricing, entitlements, tenant configuration and partner differences are represented. Configuration should have ownership, validation, compatibility and auditability; customer forks can create unbounded upgrade/support obligations. Test concurrent updates, retries, partial transactions and migrations of business rules. Examine dependency lifecycle and unsupported components using current versions/advisories.

Evidence: recent changes across boundaries, duplicated rules, transaction/consistency tests, architectural decisions and performance traces. Opportunity: reduce time to safely change a high-value capability. Avoid blanket rewrites; propose a bounded seam and a migration path.

## Tenancy and identity (D03, D07)

Separate authentication from authorization, tenant isolation, consumer relationships and entitlements. Trace trust from identity provider/token to query, object storage key, background message, cache, search index, report and privileged support action. Never trust a client-supplied tenant ID without server-side authorization. Test cross-tenant object access and indirect leakage through exports, metrics and search.

Assess onboarding, suspension, downgrade, deletion, legal holds, tenant restore and migration between isolation models. Validate quotas and fairness at all scarce resources. Enterprise identity needs federation/provisioning, role lifecycle, delegated administration and auditable emergency access; consumer recovery and account linking need their own abuse model. Review machine identities and partner credentials alongside people.

Use actual authorization policies and negative tests as evidence. Platform IAM alone cannot establish application-level tenant isolation. See the automotive module for dealer/consumer/vehicle relationship transitions.

## UX, accessibility and localization (D04–D05)

Inspect actual purchase/service/admin journeys including loading, empty, error and interrupted states. Check task completion and recovery, not only component screenshots. Assess browser/mobile compatibility, network constraints, frontend data exposure, session handling and perceived performance.

Agree applicable accessibility conformance goals; use WCAG guidance as a technical reference without equating a scanner score to legal compliance. Combine keyboard, focus, semantic structure, screen-reader and automated checks. Evaluate embedded partner widgets, authentication, payments, PDFs and notifications as part of the journey.

Internationalization: externalized content, pluralization, Unicode, locale-aware parsing/formatting, translated validation, bidirectional layouts where relevant, pseudo-localization, language fallback and translation ownership. Keep monetary precision and time-zone semantics explicit. Customer locale, currency, tenant timezone and storage region are different dimensions.

## APIs and integrations (D06)

Read contracts and actual consumers. Assess compatibility/deprecation policy, schema evolution, authentication, authorization, rate limits, idempotency scope/lifetime, pagination and error behavior. Webhooks/events need origin validation, replay defenses, duplicate handling, ordering assumptions, dead-letter resolution and reconciliation.

Prefer explicit sync/async semantics over hidden distributed transactions. Consumer contract tests and operational evidence must support claims of compatibility. Measure partner onboarding and failure resolution. Consider an adapter layer for unstable third-party systems, with traceable mappings and an exit strategy rather than a universal integration framework.

Outputs: journey/domain map, boundary findings, focused quality scenarios, incremental changes and capability opportunities. Link sources through [sources.md](sources.md).
