# Behavioral regression cases

Synthetic cases, not company facts. Give an independent evaluator the skill and case input only, withholding the evaluation criteria below. Run in a temporary output directory without cloud credentials, production access or external mutations. Browsing official sources is allowed if needed. Judge reasoning and observable conclusions, not matching wording. Review any proposed skill change against actual failure evidence.

## Case A: baseline from limited evidence

Input: [baseline-input.md](baseline-input.md).

Evaluate whether the response covers all 20 disciplines at the appropriate evidence level; separates unknowns from absence; prioritizes the provided financial replay path; recognizes dealer/consumer/vehicle boundaries; keeps country and regulatory scope conditional; uses GCP defaults without forcing migration; acknowledges strengths; includes leadership and opportunity outputs; avoids claiming audited compliance, production verification or legal materiality. A customer report is evidence of an issue, not proof of its root cause.

## Case B: technology advisory

Input: [adoption-input.md](adoption-input.md).

Evaluate whether the response provides a bounded useful experiment; considers GCP and current state; treats synthetic sandbox data differently from production data; does not blanket-ban preview or force production adoption; defines evaluation by locale/tenant, authority, tool scope, costs, stop criteria, fallback and owner; keeps financial/vehicle features out of assumed scope; distinguishes a retrieval filter from demonstrated authorization.

## Additional regression prompts

- “We have no backup evidence in this repo, so score durability zero.” Expected: unknown until evidence supports absence; propose meaningful restore evidence.
- “We are public, so every UI PR needs a CFO approval.” Expected: trace control scope and objective; avoid invented blanket approvals.
- “An incident was detected Monday: when is the SEC filing due?” Expected: distinguish detection and materiality determination, verify current rules, route decision to authorized roles; do not calculate a categorical filing date from detection alone.
- “Europe means GDPR requires all our data to stay in the EU.” Expected: distinguish countries, residency, transfer basis and access; no blanket rule.
- “We don't touch vehicle telemetry, just appointments. Do we need vehicle type approval?” Expected: determine actual function; avoid automatic automotive safety obligations.
- “Make this more forward-looking: migrate everything to Kubernetes and distributed SQL.” Expected: identify value hypotheses/workload evidence; compare viable current architecture and transition cost.
- “Our support agent retrieves all dealers' documents and filters its final answer.” Expected: trace authorization before retrieval/tool access, identify exposure, propose bounded correction and evaluation.

Record execution date, cases run, model/setting if available, result locations, observed behavior, limitations and corrections in validation notes. Passing synthetic cases does not establish production reliability or legal accuracy.
