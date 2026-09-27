# Security, privacy and audit engineering

## Security (D08)

Scope threats by assets, actors, entry points, trust boundaries and plausible abuse. Include partner compromise, dealer support tools, consumer account takeover, credential leakage, bulk export and privileged pipelines. Evaluate preventive, detective, response and recovery controls together. Use versioned OWASP ASVS requirements where useful; cite real identifiers from the version retrieved, not remembered numbers.

Seek deployed least privilege, secret lifecycle, encryption/key access, software inventory/provenance, vulnerability remediation, edge/application controls and incident exercises. An enabled service is not evidence it covers the relevant threat. Verify exception ownership and emergency access. Security findings need an exploit/failure path or a clearly labelled uncertainty, not generic advice.

## Privacy and governance (D09)

Create a processing-purpose map: data categories, collection source, controller/processor roles, authority/lawful basis, access, sharing, location, retention and downstream use. Legal terminology and requirements must be checked with current jurisdictional sources. Consent is not a universal basis, and a contract with a dealer is not automatic authority for every secondary use of consumer data.

Inspect implementation of minimization, rights requests, access/correction/export/deletion, opt-outs, consent withdrawal and legal-hold exceptions. Trace replicas, backups, derived tables, feature stores, search indexes, logs and AI providers. Pseudonymization is not automatic anonymization. Do not promise immediate physical deletion from every backup; verify a documented expiry/restoration/suppression process consistent with applicable requirements.

Assess production data in development, support access, vendor data use, telemetry and training reuse. Ask whether new analytics or AI changes the purpose or legal role. Distinguish residency, sovereignty, transfer basis, operational access and contractual hosting promises.

## Audit design (D10)

Separate diagnostic logs, security logs, cloud audit logs, business audit trails and financial-control evidence. They can share infrastructure but have distinct purposes and access/retention requirements. For sensitive business actions record attributable actor, acting-on-behalf-of identity, tenant/subject references, action, time, outcome, correlation, policy/consent/configuration version and authorized reason where relevant. Avoid copying sensitive payloads unnecessarily.

Evaluate append behavior, tamper resistance, access separation, clock consistency, delivery failure, evidence export, retention/legal holds and deletion restrictions. Ordinary logs should not be described as immutable without verifying configuration and privileged bypasses. Assess whether failed and denied actions needed for investigation are retained, while controlling cost and privacy.

Deliver a threat/data-flow map and obligation→control→evidence crosswalk. Use the public-company module for ICFR and disclosure dependencies. SOC 2, ISO certification, PCI and sector obligations need explicit applicability and scope; none is a blanket substitute for another.
