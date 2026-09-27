# US public-company responsibilities

This module supports architecture and control-readiness decisions. It does not perform an audit, determine securities-law materiality, classify a material weakness, or certify compliance. Use current official sources and confirm entity/filer applicability with Finance, Legal, Security, and the responsible control owners. Internal Audit and external auditors retain their respective independent responsibilities.

## Applicability and decision rights

Keep securities reporting, internal control over financial reporting (ICFR), disclosure controls, customer commitments, and general security obligations distinct. Do not put every system in SOX scope merely because the company is public. Trace actual dependencies into significant financial accounts, disclosures, and related controls. A system outside ICFR scope may still be important for cybersecurity disclosures or customer obligations.

SOX 302 concerns executive certifications and disclosure-control responsibilities; SOX 404 concerns ICFR assessment, with auditor attestation applicability dependent on the issuer's circumstances. Confirm the current filer classification and exemptions; “smaller reporting company” is not automatically equivalent to “non-accelerated filer.” See SEC sources PC1–PC3 in [sources.md](sources.md).

Use a top-down, risk-based scope discussion informed by [PCAOB AS 2201](https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201). It is an auditing standard, not a universal engineering checklist. Proposed architecture controls below are implementation suggestions whose necessity and precision depend on company risks and control design.

## Financial-system dependency tracing

Trace product usage → rated usage/pricing → entitlements/contracts → invoices/credits → revenue/receivables feeds → finance systems → reconciliations and reporting. Include data transformations, manual files, integration failures, reruns, period cutoffs, timezone behavior, corrections, and privileged changes. Do not assert the product performs revenue recognition merely because it produces invoices.

For each relevant flow identify system/data owner, source of truth, completeness/accuracy checks, duplicate/lost event detection, reconciliation, exception approval, historical reproducibility and access/change controls. Distinguish operational dashboards from data used in public disclosures. For publicly used metrics, preserve definitions, transformations, definition changes, review and substantiation; SEC metric guidance is linked as PC5.

## Suggested control-readiness questions

| Area | Questions and evidence |
|---|---|
| Access | Who grants/reviews/revokes access? Can developers alter production data and approve their own changes? Inspect service identities and emergency access as well as human roles. |
| Change | Can a release be traced from requirement and review to tested artifact and deployed configuration? Inspect emergency changes, database scripts, feature flags, pricing logic and CI policy changes. |
| Operations | Are failed jobs, incomplete feeds, backups and restores detected and resolved? Can reruns duplicate financial activity? Examine period evidence and exception closure. |
| Automated controls | What exact condition is checked, with what precision? What upstream data and IT controls support it? Inspect negative cases and bypasses. |
| Reports used as evidence | Are parameters, filters, population completeness, query version, time period and source accuracy reproducible? A screenshot alone may not establish this. |
| Third parties | What service and period does the assurance report cover? Are relevant customer responsibilities and exceptions addressed? A provider report does not prove the customer's controls operate. |
| Evidence | Can authorized reviewers establish who did what, when, against which population and version? Inspect integrity, restricted access, retention schedule and legal holds. |
| Deficiencies | Is there an owner, impact assessment, compensating control, remediation, retest and escalation? Engineering severity is not an auditor deficiency classification. |

Assess control design and implementation separately from operation over a period. Do not infer operating effectiveness from a policy, configured feature, or a single successful sample. Avoid prescribing universal retention periods or mandatory human gates on every release; seek company-approved control objectives and design precise, automatable evidence.

## Cyber incident and disclosure readiness

For domestic registrants, the SEC's Item 1.05 rule generally requires filing within four business days after determining an incident is material; materiality determination must be made without unreasonable delay after discovery. This is not a four-day-from-detection rule. Exceptions and current applicability require Legal verification. Annual disclosures also address cybersecurity risk management, strategy and governance. Reference: [SEC cybersecurity guidance](https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/cybersecurity-risk-management-strategy-governance-incident-disclosure).

Architecture should support timely, reliable facts: timeline, affected systems/customers/data, operational and financial impacts, containment, confidence levels, evidence preservation and updates. Record detection time separately from escalation and determination times. The response process needs an established path to Security, Legal, Finance and disclosure leadership. Do not make a materiality decision, publish an incident notice, or promise a filing deadline on behalf of the company.

Propose a tabletop linking incident operations to leadership decisions; no public communications or live disruption. Ensure board/audit committee information is decision-relevant and distinguish allegations, known facts, estimates and unresolved issues. Protect material nonpublic information in evidence repositories and reports.

## Required module output

Produce a dependency/control map with scope status (`confirmed`, `candidate`, `out_of_scope`, `unknown`), basis, role owner, evidence need and next decision. Add disclosure-readiness gaps where relevant. Route unresolved accounting/legal conclusions to the appropriate owner while completing the technical assessment.
