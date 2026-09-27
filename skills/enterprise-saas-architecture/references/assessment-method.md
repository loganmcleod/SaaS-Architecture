# Evidence-based assessment

## Scope and traceability

Record objective, mode, boundary, countries, period, environment, source commit/configuration snapshot, and exclusions. Establish success criteria before scoring. Ask only for necessary artifacts; incomplete enterprise context need not block scoped advice.

Baseline: each D01–D20 receives exactly one coverage disposition: `reviewed`, `partially_reviewed`, `not_reviewed`, or `not_applicable`. Explain exclusions/N/A. Screen X01 AI for applicability. Coverage describes review work, not system quality.

For each requirement use `met`, `partially_met`, `not_met`, `unknown`, or `not_applicable`. Identify its basis: user goal, customer commitment, company policy, applicable obligation, or architectural recommendation. Recommendations are not automatically mandatory controls.

Evidence confidence is high/medium/low with rationale. Distinguish direct artifact/runtime observation, corroborated records/interview, uncorroborated statement, and unavailable evidence. Code usually cannot establish deployment, sustained operation, or control effectiveness.

## Evidence record

Capture ID; restricted location or path/line; environment; date/period; method; scope/population; redaction; limitations; and findings supported. For telemetry: query, window, filters, aggregation, sample size, tenant/region coverage. For controls: performer/reviewer, execution date, exceptions, population tested. Do not reproduce confidential raw populations in general reports.

Map actors → journeys → components → stores → dependencies → teams. Trace tenant/consumer identity through synchronous calls, queues, caches, exports, analytics, and support. Include control-plane and data-plane dependencies.

## Quality scenarios

Specify stimulus, operating condition, affected journey, expected response, and measurable threshold. Derive thresholds from business/customer needs or label them proposed. Examples: failover within agreed recovery time/data-loss budgets; noisy tenants cannot breach others' objectives; identity revocation reaches workers/caches within an agreed interval.

Evaluate load, partial failure, replay, concurrency, migration, revocation, regional restrictions, and emergencies when relevant. Recommend safe validation; intrusive tests require authorization.

## Findings

Record stable ID; kind (`risk`, `opportunity`, `evidence_gap`, `strength`); disciplines; journey; requirement/basis; observation; inference; consequence; implementation status; confidence; role owner; options including status quo; action; dependencies/effort; acceptance evidence. Risks also need severity, likelihood/exposure, mitigations, and residual risk. Opportunities need a measurable value hypothesis and adoption cost. Avoid duplicate root causes across frameworks.

Severity: critical = substantiated exposure needing immediate containment/executive attention; high = credible major impact inadequately mitigated; medium = consequential bounded exposure or partial mitigation; low = limited exposure/incremental improvement. Explain impact and likelihood; missing documentation alone is not critical. These are engineering labels, not legal materiality or auditor classifications. An evidence gap may warrant urgent investigation without asserting a defect. Financial estimates need assumptions/ranges.

Optional maturity: 0 evidenced absence; 1 ad hoc; 2 repeatable/owned; 3 measured/tested; 4 adaptively improved. Unknown and N/A are outside the scale. Do not target 4 everywhere. Show distributions and coverage; avoid unsupported composite percentages. Report critical findings independently.

## Prioritization and reassessment

Scale presentation to evidence and the user's decision. Keep the executive readout concise; group minor findings and shared evidence in tables. The full finding record is a completeness guide, not a demand for a long essay per item. Sparse evidence should produce a useful, clearly bounded review rather than speculative detail. Retain baseline coverage and material uncertainties even when compressing presentation.

Rank exposure/time sensitivity, then value, dependencies, effort, reversibility, confidence. Separate containment, evidence collection, structural remediation, and experiments. Dates/role owners remain proposed until accepted. Every action needs success evidence and verification owner. Risk acceptance records need decision-maker, rationale, compensating controls, review trigger/expiry, residual exposure. Compare equivalent scopes and definitions; explain changed evidence or targets. Closed tickets do not prove remediation.
