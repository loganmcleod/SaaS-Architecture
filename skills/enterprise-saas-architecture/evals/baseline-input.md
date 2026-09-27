# Synthetic engagement

Use the enterprise-saas-architecture skill for a baseline review and a practical 90-day leadership plan. This is a synthetic tabletop; you may read these facts and the skill, and consult public official documentation. Do not inspect other company files or any live environment.

We are a US public automotive B2B2C SaaS company. We provide dealer-branded consumer appointment booking and lead routing in the US, Canada, Germany and France. No telemetry, vehicle commands, lending decisions or payment-card collection. We have 80 dealer tenants and a team of 12 engineers.

Artifacts supplied as textual excerpts, not verified deployment facts:

E1 / architecture note: Cloud Run services, Cloud SQL PostgreSQL, Pub/Sub, BigQuery. US and EU deployments. An identity provider supplies workforce SSO. Application queries include dealer_id and integration tests cover API cross-dealer reads.

E2 / worker pseudo-code: upon a booking event, append a usage row with booking_id, dealer_id, event_time; retry on any exception. No uniqueness constraint is shown. A monthly aggregate feeds a billing service; the controller says invoice output is reconciled manually before posting. No reconciliation records were supplied.

E3 / customer ticket: a customer reports receiving a reminder from the previous dealer after moving their appointment. Cause is unconfirmed.

E4 / release record: peer review, automated checks and versioned artifacts. Last quarter's restore exercise report and cloud access reviews are not in the supplied material. The platform lead says they exist in a restricted evidence store.

E5 / product plan: wants AI-assisted support and expansion into the UK. Current delivery estimates are repeatedly missed because three teams need to coordinate schema changes. The team requests advice rather than a rewrite.

Provide conclusions that the supplied evidence supports, important unresolved questions, useful opportunities, and mentoring actions for application, platform and data leaders.
