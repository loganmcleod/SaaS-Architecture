# Data architecture and engineering

## Operational data (D11)

Map sources of truth, ownership, tenant boundaries, identifiers, invariants and consistency requirements before choosing a datastore. Inspect uniqueness and referential constraints, transaction isolation, races, deletion/retention behavior, indexing, query plans and hotspots. Treat externally supplied VINs, dealer IDs and consumer identifiers as data requiring validation and relationship-aware access.

Evaluate expand/contract migrations, mixed-version compatibility, backfills, rollback/forward repair, encryption/key availability and point-in-time recovery. A successful backup job does not establish recoverability; request restore evidence including correctness, elapsed time, access and keys. Test tenant-specific recovery without overwriting another tenant or resurrecting deleted/revoked relationships.

## Pipelines and analytics (D12)

Trace ingest → raw → curated → semantic → consuming application/report/model. Identify batch/stream latency needs, change-data capture, data contracts, schema compatibility, lineage, orchestration and owners. Specify handling for duplicate/missing/late/out-of-order data, poison messages, replay/backfill, partial runs and idempotent writes. Broker delivery guarantees do not establish end-to-end exactly-once business effects.

Define quality as fit for a purpose: completeness, accuracy, freshness, uniqueness, consistency and validity. Choose measurable thresholds and exception disposition. Reconcile source-to-target counts and value totals where relevant; exclude known adjustments explicitly. Alert on business impact and data staleness, not only task failure. Preserve reproducibility of published metrics and datasets used in decisions.

For GCP, evaluate BigQuery for analytical needs, Pub/Sub for event transport, Dataflow for fitting stream/batch processing and orchestration/SQL transformation tools based on existing team capabilities. These are candidates, not a mandated stack; verify current capabilities, locations, cost and lifecycle. Assess query partitioning/clustering, scan costs, reservations where relevant, access policy, authorized sharing, data catalog/lineage and regional transfer paths.

## Governance and economics

Assign data-product owners and consumer contracts; do not introduce data mesh solely as an organizational fashion. Separate transactional truth from analytics and inference. For customer-facing analytics, validate tenant enforcement in queries, caches, materializations, exports and BI permissions. For ML/AI, track consent/purpose, provenance, training/evaluation contamination, retention and deletion implications.

For financial/reporting flows use the public-company module: metering-to-invoice completeness, pricing versions, corrections, cutoff, currency/rounding, exception approvals and reconciliation. Metrics need a business definition and version, not just a SQL query.

Outputs: lineage and ownership map; high-impact quality failures; recovery evidence; cost/freshness tradeoffs; data-product opportunities; acceptance tests tied to actual consuming decisions.
