# Operations, delivery and economics

## Reliability and performance (D14–D15)

Define critical journey SLIs/SLOs, customer commitments, dependencies, error-budget decisions, recovery-time and data-loss objectives. Targets come from business needs and evidence. Distinguish availability from correctness, regional outage from tenant outage, and live service recovery from reporting data recovery.

Inspect dependency timeouts, bounded retries with jitter, circuit breaking where justified, backpressure, queue age, load shedding, concurrency limits and graceful degradation. Evaluate retry amplification and single control-plane dependencies. Failover needs consistency, routing, credentials, keys, capacity, runbooks and failback—not just duplicate compute. Use incident history and exercises to identify common-cause failures.

Load models need tenant distribution, peak/concurrent users, batch imports, regional latency, database size, cold starts and partner delays. Report percentiles and errors per critical journey rather than averages alone. Measure scalability against saturation and cost; autoscaling that overwhelms the database is not successful scaling. Validate capacity headroom and quotas against growth assumptions. Propose tests in safe environments unless live testing is explicitly authorized.

## Observability and support (D16)

Can responders identify impact, affected tenants/consumers, failed dependency and deployment/configuration changes? Inspect meaningful traces/logs/metrics, correlation, alert precision, on-call burden, runbooks, ownership and incident learning. Protect data while preserving diagnostic value. Track detection, mitigation and recovery with clear definitions; don't optimize a metric at the expense of customer outcomes.

Support tools need least privilege, attributable impersonation, approval where risk warrants, audit evidence and revocation. Audit trails differ from debugging logs. Examine vendor outages, customer communication processes, support escalation and service ownership.

## Delivery and developer platform (D17–D18)

Assess behavior-focused tests, contract and isolation tests, migrations, representative test data, environment parity, build provenance, dependency scanning, artifact promotion, deployment/feature-flag changes and rollback/forward repair. Tests should target important failure behavior rather than mirror implementation. Review database compatibility during mixed-version rollout. Trace a real release from change to runtime and evidence.

Prefer automated policy/evidence and proportional segregation over universal manual gates. Public-company controls can coexist with frequent delivery. Measure lead time, deployment/failure/recovery trends using current DORA definitions where adopted; state windows and populations. Do not rank individuals by team/system metrics.

Treat the internal platform as a product: research developer needs, measure adoption and time saved, provide supported paths and bounded exceptions, clarify ownership and versioning. Investigate local setup, first safe change, feedback latency and cognitive load. A portal alone does not establish platform value.

## Economics and sustainability (D19)

Map revenue model, entitlements, usage metering, pricing versions, billing reconciliation and support obligations. Measure direct and shared costs per meaningful business unit (tenant, completed booking, transaction or inference), explain allocation and uncertainty, and include support/licensing/operational costs in choices. Budget alerts are not automatic spending caps.

Evaluate cost elasticity, idle resources, query/egress/observability expense, committed capacity tradeoffs and inefficient retries. Track resource efficiency without inventing carbon estimates. A profitable high-value tenant and a low-cost tenant are not synonymous. Opportunities should improve customer value or cost to serve with measurable outcomes.
