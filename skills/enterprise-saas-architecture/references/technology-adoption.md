# Forward-looking technology adoption

Be actively curious and willing to adopt technology that improves product differentiation, delivery, reliability, economics or team capability. Neither novelty nor conservatism is a decision rule. Search current primary sources when assessing a candidate; separate shipped capabilities, previews, roadmaps and vendor claims. Retain the current option as a baseline.

## Radar and decision stages

Use `explore` (credible hypothesis), `trial` (bounded experiment), `adopt` (supported production use for a defined context), `hold` (insufficient fit/evidence), and `retire` (planned replacement). Assign an owner, context, evidence date and review trigger. Adoption is contextual: success for internal knowledge search does not approve credit decisions or vehicle commands.

Assess value and alternatives; technical/workload fit; GCP integration; supplier/product maturity; regional availability; security/privacy/control evidence; maintainability; skill availability; total economics; operational failure modes; portability; and exit cost. GA status alone is insufficient evidence of fitness. Preview status alone is not grounds to ban a safe, reversible sandbox experiment. Production use needs explicit risk ownership and demonstrated controls/support appropriate to impact.

An experiment specifies problem, baseline, target improvement, representative workload, time/budget bounds, permitted data, environment, metrics/guardrails, owner, stop conditions, success/failure criteria and next decision. Use synthetic or appropriately authorized minimized data. Do not promise benefit before measurement. Define containment, rollback and operational ownership before widening exposure.

## AI and agents (X01)

Evaluate the workflow rather than the model in isolation. Prefer a deterministic solution if it meets the need more reliably/economically; use AI where empirical value warrants it. Start GCP comparisons with current managed offerings, but choose models/providers by evidence and data terms. Verify versions, regions, retention/training use, subprocessors, quotas, deprecation and fallback.

Inspect retrieval and tool authorization at every step: tenant/consumer context, document permissions, indexes/caches, output validation, tool scope, confirmations for consequential actions, prompt injection, data exfiltration and runaway loops. Untrusted retrieved text must not grant tool authority. An agent service account's cloud permissions do not prove that the consumer may access or change a record.

Use representative evaluation sets by language, region, customer role and risk class; record provenance, holdouts, leakage, task success, hallucination/error severity, refusal/overblocking, bias where relevant, latency and cost. Test adversarial cross-tenant retrieval, stale permissions, malicious documents, replayed tool requests and model/provider failure. Human oversight must specify who reviews what, with what information and ability to intervene.

Version model, prompt, retrieval configuration, tools and policies as a released system. Monitor real outcomes, drift, unresolved errors and escalations; record meaningful traces while minimizing personal data and sensitive reasoning artifacts. Prefer auditable inputs/actions/results and decision rationale appropriate to the task. Include kill switches, safe fallback and rollback evidence.

Credit, insurance, employment, sensitive profiling or vehicle-impacting uses require additional applicability and specialist review. Apply NIST AI RMF as voluntary risk guidance, not a certification or proof of regulatory compliance. Verify current AI-law role/classification and transition dates before advising on obligations.

## Broader horizon

Consider AI-assisted delivery, agent-supported operations, modern analytical architectures, event-driven integration, managed runtimes, identity improvements and stronger cryptographic approaches only as they address a real objective. Do not hard-code a particular model or trend as the next investment. Include debt from unsupported/deprecating technology and a planned retirement path. The roadmap should contain both exploitation of proven capabilities and a bounded portfolio of experiments.

Output: radar entry, decision record, experiment charter, adoption conditions and a leadership learning objective. Use [output templates](../assets/output-templates.md).
