# Source register and freshness

Research baseline: 2026-09-27. This is a curated starting register, not a frozen legal opinion or a mirror of entire standards. Links below were inspected through official pages or indexed official excerpts during package creation unless marked otherwise. Reopen relevant current sources at assessment time; record the specific document/version, access date, applicability, and any changed advice. A checked overview does not verify every related service capability or legal provision.

Distinguish binding applicable law, company/customer commitments, voluntary standards, vendor guidance and this package's architectural preferences. Do not reuse internal D/PC/G IDs as if they were regulator control identifiers. Proposals, drafts and announced future capabilities are not operative requirements or shipped features. If a source cannot be retrieved, retain that limitation rather than silently asserting verification.

Inspect redirect destinations. A legacy product URL that lands on a generic catalog does not verify the requested product terms or capability. Record renamed products and retrieve the specific current document before relying on it.

## GCP

| ID | Source | Use |
|---|---|---|
| G1 | [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) | Primary cloud review framework; read relevant pillars/perspectives. |
| G2 | [Enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations) | Organization, identity, network, policy and evidence foundation. |
| G3 | [Cloud Run overview](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) | Runtime fit; follow links to current limitations, regions and pricing. |
| G4 | [GKE Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) | Managed Kubernetes fit and constraints. |
| G5 | [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) | Keyless external workload access; distinguish workforce identity. |
| G6 | [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) | Categories and service-specific enablement/coverage. |
| G7 | [BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction) | Analytics capability; verify geography, access and cost per use case. |

For Cloud SQL, AlloyDB, Spanner, messaging, key services, AI products and other candidates named in the GCP module, obtain current official product documentation before recommending a specific configuration. No fixed quotas, prices, model IDs, preview status or SLA values are embedded in the package.

## Public-company responsibilities

| ID | Source | Use |
|---|---|---|
| PC1 | [SEC: certification of quarterly and annual reports](https://www.sec.gov/rules-regulations/2002/08/certification-disclosure-companies-quarterly-annual-reports) | Section 302 background; confirm current form requirements. |
| PC2 | [SEC: management ICFR report FAQ](https://www.sec.gov/oca/controlfaq1004) | ICFR scope/background; interpret with current issuer facts. |
| PC3 | [SEC: smaller reporting companies](https://www.sec.gov/resources-small-businesses/going-public/smaller-reporting-companies) and [Regulation S-K interpretations](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/regulation-s-k) | Filer distinctions and attestation applicability; verify current rules. |
| PC4 | [PCAOB AS 2201](https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201) | Risk-based ICFR audit approach; check version/effective period. |
| PC5 | [SEC: MD&A metrics guidance](https://www.sec.gov/rules-regulations/2020/01/commission-guidance-managements-discussion-analysis-financial-condition-results-operations) | Substantiation and governance of metrics used in disclosures. |
| PC6 | [SEC: cybersecurity compliance guide](https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/cybersecurity-risk-management-strategy-governance-incident-disclosure) and [adopting release](https://www.sec.gov/files/rules/final/2023/33-11216.pdf) | Incident/governance reporting, determination timing and applicable exceptions. |

## Automotive, markets and privacy

| ID | Source | Use |
|---|---|---|
| A1 | [EDPB connected-vehicle guidelines](https://www.edpb.europa.eu/documents/guideline/guidelines-012020-on-processing-personal-data-in-the-context-of-connected_en) | Vehicle/mobility processing when applicable; consult adopted version. |
| A2 | [European Commission: Data Act explained](https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained) | Connected-product and data-processing-service provisions; check role and transition dates. |
| A3 | [FTC GLBA guidance](https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act) and [auto dealer Safeguards FAQ](https://www.ftc.gov/system/files/ftc_gov/pdf/2025-GLB-Safeguards-FAQs-for-Auto-dealers.pdf) | Conditional dealer finance/leasing and supplier responsibilities. |
| A4 | [OPC: cross-border processing](https://www.priv.gc.ca/en/privacy-topics/airports-and-borders/gl_dab_090127/) | Canadian transborder-processing background; confirm applicable federal/provincial law. |
| A5 | [EDPB international transfers](https://www.edpb.europa.eu/sme/be-compliant/international-data-transfers_en) and [individual rights](https://www.edpb.europa.eu/sme/be-compliant/respect-individuals-rights_en) | GDPR transfer/rights overview; simplified guidance is not a complete enterprise analysis. |
| A6 | [GDPR official text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) | Canonical legal-text link. Retrieval was blocked by a browser challenge during creation; reopen/verify relevant consolidated provisions before legal conclusions. |

Country-specific privacy, ePrivacy/marketing, accessibility, AI, connected-vehicle trade/type-approval, lending and payment obligations are screening candidates, not pre-verified applicability. Research them using current official authorities when the company's product and geography are known.

## Quality, security, delivery and innovation

| ID | Source | Use |
|---|---|---|
| Q1 | [SEI ATAM collection](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/) | Quality scenarios and tradeoff evaluation. |
| Q2 | [arc42 quality guidance](https://docs.arc42.org/section-10/) | Document measurable quality expectations. |
| Q3 | [OWASP ASVS](https://owasp.org/projects/asvs) | Versioned security verification; retrieve the actual chosen release and identifiers. |
| Q4 | [W3C WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/) and [internationalization tips](https://www.w3.org/International/quicktips/) | Technical accessibility and localization references; determine legal obligations separately. |
| Q5 | [DORA capabilities](https://dora.dev/capabilities/) | Delivery/platform improvement; verify metric definitions before comparisons. |
| Q6 | [FinOps Framework](https://www.finops.org/framework/) | Value, allocation, unit economics and investment practices. |
| Q7 | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) and [Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Voluntary AI risk guidance; verify publication/version and applicable legal overlays separately. |

## Existing skills studied

[AWS's review skill](https://github.com/aws/agent-toolkit-for-aws/blob/main/skills/core-skills/aws-well-architected-review/SKILL.md), [agent-skill-router architectural review](https://github.com/paulpas/agent-skill-router/blob/main/skills/coding/architectural-review/SKILL.md), and [soderlind architecture documentation](https://github.com/soderlind/skills/blob/main/skills/document-architecture/SKILL.md) were inspected as workflow references. This package uses original instructions, does not bundle or depend on their implementation, and does not install them. The [older AWS sample](https://github.com/aws-samples/sample-well-architected-skills-and-steering) points to its successor; do not treat it as a maintained default. Recheck license and implementation before any future reuse.
