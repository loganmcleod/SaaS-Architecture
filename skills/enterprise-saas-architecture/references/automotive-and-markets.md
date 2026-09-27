# Automotive B2B2C across North America and Europe

## Business and identity boundaries

Establish actual participants: OEM/importer, dealer group, franchise/store, fleet, marketplace, finance/insurance partner, owner, lessee, driver, purchaser and service customer. These are candidate roles, not confirmed customers. Separate tenant, corporate hierarchy, franchise rights, data-sharing agreement, consumer identity and vehicle relationship. One consumer may interact with multiple unrelated dealers; a vehicle changes hands and drivers. VIN is an identifier, not an authorization credential, and can link to personal information.

Trace actual journeys such as lead/consent capture, inventory/search, quote/reservation, financing handoff, purchase, service booking, ownership transfer and deletion. Identify commissions, attribution, promotions and analytics only where present. Define the system of record and conflict handling for dealer-management/CRM/OEM integrations. Verify ordering, stale inventory, price validity, duplicate leads, replay, partner outages and manual corrections.

Priority boundary scenarios:

- A consumer's new dealer relationship does not silently grant access to prior dealers' records.
- Dealer employees lose privileges after transfer/termination, including exported reports, cached authorizations and queued work.
- A sale, lease termination, fleet reassignment or shared-driver change revokes obsolete vehicle access without deleting legally retained transaction records indiscriminately.
- Support impersonation has scoped purpose, attributable identity and audit evidence; consumer support does not bypass partner boundaries.
- Consent/marketing preferences remain purpose-, recipient- and jurisdiction-aware across partners; deletion/correction propagates to applicable downstream systems.
- If vehicle commands exist: verify authority, replay protection, stale commands, confirmation, safe failure and specialist safety review. Do not apply this to a product with no vehicle-control function.

## Geographic applicability screen

Maintain a matrix of country/state/province, legal entity, customer and data-subject location, service offered, data category, role/purpose, applicable obligation/contract, source/version, owner, status and evidence. A legal hypothesis remains `needs_confirmation`; it is not a finding of noncompliance. Exact countries are presently unspecified.

| Area | Screen for, conditionally |
|---|---|
| EU/EEA | GDPR roles and lawful basis by purpose; processors/subprocessors, rights, profiling, DPIA triggers, transfer mechanisms; ePrivacy/national rules for tracking and marketing; relevant accessibility obligations; Data Act scope for connected products/related services and separately data-processing-service switching; AI regulation where AI use and role bring it into scope. |
| UK / Switzerland | Separate privacy, transfers, marketing, consumer and accessibility requirements; do not assume EU rules alone settle them. |
| United States | Applicable state privacy and consumer rights, location/sensitive data, advertising/marketing and communications, breach obligations; credit/financing and payments where offered. |
| Canada | PIPEDA and applicable provincial regimes; Quebec-specific privacy/language questions when relevant; transborder processing, consent and marketing obligations. |
| Mexico | Confirm whether served; if so, investigate current private-sector privacy, notices, consumer and transfer rules using current official sources. |

Avoid asserting GDPR categorically requires EU hosting. Storage location, international transfer basis, remote access and onward processing are distinct. Map logs, backups, analytics, support tooling, AI prompts and disaster-recovery copies—not just the primary database.

## Conditional automotive obligations

The [EDPB connected-vehicle guidance](https://www.edpb.europa.eu/documents/guideline/guidelines-012020-on-processing-personal-data-in-the-context-of-connected_en) is relevant when mobility/vehicle data is processed. Assess location history, behavior inference, shared users and secondary use; vehicle data must not be presumed anonymous.

The [EU Data Act guidance](https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained) addresses access/sharing of connected-product data and other duties. Determine the company's role and relevant provisions, exceptions and transitional dates. Separately screen cloud/data-processing switching requirements; do not reduce the entire Act to connected cars or presume every provision applies to every SaaS service.

[FTC guidance for automobile dealers](https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act) identifies financial-service activities that can bring dealers within GLBA/Safeguards obligations. Determine whether this company is directly covered, a service provider with contractual duties, or neither. Dealer financing does not automatically put every SaaS workflow under the same obligations.

Vehicle cybersecurity/type approval, software update, functional safety, US connected-vehicle restrictions, payment-card standards, credit/insurance rules and export/trade restrictions are applicability questions when features, markets, counterparties or supply chains trigger them. Use current specialist sources before naming a binding requirement. No blanket claim that ISO 26262, ISO/SAE 21434, UNECE R155/R156 or PCI DSS applies to the entire platform.

## International product engineering

Assess language and locale independently of hosting region. Include dealer-local versus consumer-local time, daylight-saving transitions, recurring appointments, decimal/currency precision, tax presentation, units (miles/km), addresses, names, phone numbers, translated legal notices, email/PDF/SMS, search/collation and analytics aggregation. Test representative actual locales, accents, long strings and screen readers. Support multiple relationships without treating vehicle ownership as permanent or exclusive.

Output a journey/actor map, applicability register, critical boundary scenarios and market-enablement opportunities, with factual uncertainties and responsible roles.
