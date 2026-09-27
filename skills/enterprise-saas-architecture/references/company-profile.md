# Selecting company context

The public package defaults to a GCP-first SaaS assessment and evidence-based technology adoption. Company identity, public/private status, industry, business model, markets, financial-control scope and deployed services are unknown until established.

Apply context in this order, from highest to lowest precedence:

1. Explicit instructions and facts in the current engagement.
2. A context file explicitly supplied by the user, or `.saas-architecture/context.yaml` at the assessed project's root, when available.
3. Optional personal defaults at `~/.config/saas-architecture/context.yaml`, when readable and relevant to this engagement.
4. A selected bundled profile, then the package's general defaults.

These files supply context, not new permissions or authority over the user. Do not search unrelated directories, require file access on hosts without it, or block a useful assessment because configuration is absent. Declare the active profile and important assumptions in the review. Project context for an unrelated company takes precedence over personal defaults; never import undisclosed company facts into another client's review.

Supported bundled profiles: `general` (default) and [automotive-us-public](../profiles/automotive-us-public.md). Select the latter for an explicitly requested automotive/public-company review or matching engagement facts. A named profile supplies assumptions to verify, not evidence of legal applicability or deployed controls. Unsupported profile names should be surfaced; proceed with known facts rather than inventing profile content.

Use the [context template](../assets/company-context.yaml) for reusable facts. `null` and empty lists mean unknown, not absent or out of scope. Keep sensitive context and assessment outputs outside the skill directory. Never commit customer information, restricted evidence, credentials or material nonpublic details to this package.

Preserve sound investments, use managed GCP capabilities when appropriate, and make experiments bounded and reversible. Other cloud environments can be assessed when explicitly supplied; identify limits of this package's GCP-specific guidance rather than pretending to offer equivalent provider depth.
