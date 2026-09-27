# SaaS Architecture

A **GCP-first architecture assessment and leadership advisory skill** for enterprise SaaS teams. Evaluate a platform across 20 disciplines, identify supported gaps and opportunities, and turn findings into decisions, experiments and capability improvements.

The package works with agent hosts that support `SKILL.md`, including Codex. The core is readable Markdown; Codex UI metadata is optional for other hosts. It is advisory guidance, not a scanner, an audit opinion or a compliance certification.

## Get started

```sh
git clone https://github.com/loganmcleod/SaaS-Architecture.git
cd SaaS-Architecture
python3 tools/package.py install --destination "$HOME/.codex/skills"
```

The installer requires Python 3.11+ and no third-party Python packages. Repository access is required while the repository is private. See [installation and updates](docs/installation.md) for other hosts, safe replacement, context files and release archives.

Then ask your agent:

> Use $enterprise-saas-architecture to assess this platform. Identify the highest-impact gaps and opportunities, distinguish verified issues from missing evidence, and propose an improvement and leadership development plan.

## What it does

| Mode | Outcome |
|---|---|
| Baseline assessment | Coverage across all 20 disciplines, strengths, supported findings and unresolved evidence. |
| Focused review | A deep dive into a journey, subsystem, discipline or failure mode. |
| Decision advisory | Options, costs, tradeoffs, reversibility and a recommended direction. |
| Technology adoption | A bounded experiment with measurable outcomes, operating requirements and exit criteria. |
| Leadership coaching | Diagnostic questions, delegated exercises, ownership and capability goals. |
| Roadmap / reassessment | Sequenced investments and evidence that previous actions improved outcomes. |

Coverage includes product and domain architecture; SaaS tenancy; frontend experience; accessibility and internationalization; APIs and identity; security, privacy and auditability; operational data and analytics; infrastructure; reliability, performance and support; delivery and developer experience; economics; governance and documentation. An AI/ML extension addresses evaluation, data access, tool authority, oversight and operations. See the [discipline catalog](skills/enterprise-saas-architecture/references/discipline-catalog.md).

## Opinionated, adaptable context

**GCP-first:** Prefer fitting managed GCP capabilities and preserve viable investments. Kubernetes, microservices, multi-region and multicloud need a business case; they are not maturity scores.

**Evidence first:** Separate implementation status, review coverage, risk severity, maturity and confidence. Missing evidence does not prove a defect. Recommendations connect technical findings to business outcomes and team capability.

**Forward-looking:** Test promising technology with bounded exposure, a meaningful baseline and a supported path to adoption or exit.

The default profile is general SaaS. Select the **automotive-us-public** profile for automotive B2B2C, North American/European markets, and US public-company responsibilities. It adds dealer/consumer/vehicle relationships, financial-reporting dependencies, control evidence and disclosure readiness without assuming every automotive or financial rule applies.

> Use $enterprise-saas-architecture with the automotive-us-public profile to review our dealer/consumer authorization model across APIs, background jobs, analytics and support tools.

Company facts belong in private context files, not in the distributed skill. Explicit engagement facts override project context, which overrides optional personal defaults and profile assumptions. Start from the [context template](skills/enterprise-saas-architecture/assets/company-context.yaml); see [context selection](skills/enterprise-saas-architecture/references/company-profile.md).

## Repository layout

```text
skills/enterprise-saas-architecture/   Self-contained installable skill
  SKILL.md                            Entry point and reference routing
  agents/                             Optional Codex interface metadata
  references/                         Focused assessment guidance and sources
  profiles/                           Optional industry/company perspectives
  assets/                             Context and output templates
  evals/                              Synthetic inputs and evaluation criteria
  LICENSE                             License included in installations

docs/                                 Installation, development, validation history
tools/package.py                      Validate, build, install safely
tests/                                Packaging and installation behavior checks
.github/                              CI and contribution templates
VERSION                               Package version
LICENSE                               MIT license
```

The release build includes only the skill directory and version. Private context, generated assessments, local artifacts and development tooling are excluded. There are no cloud credentials, external skill dependencies or runtime network calls in the installer. An agent may need approved project access and current public sources to conduct an assessment.

## Develop and validate

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/package.py validate
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python tools/package.py build
```

Builds produce a versioned ZIP and SHA-256 file in `dist/`. See [development and release policy](docs/development.md), [validation history](docs/validation.md), and [changelog](CHANGELOG.md). CI checks structure and packaging; it does not run an AI model, access production or publish releases.

## Contribute and reuse

Read [CONTRIBUTING.md](CONTRIBUTING.md) for focused changes and primary-source expectations. Use [SECURITY.md](SECURITY.md) for sensitive reports. The project is [MIT licensed](LICENSE); linked standards, vendor documents and third-party references retain their own terms. The project is not affiliated with or endorsed by Google, OpenAI, regulators or standards bodies.

The [source register](skills/enterprise-saas-architecture/references/sources.md) records references and retrieval limitations. Current legal applicability, vendor capabilities and production effectiveness require engagement-specific verification.
