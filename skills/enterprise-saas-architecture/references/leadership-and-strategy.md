# Leadership, governance and strategic counsel

## Diagnose systems before judging people (D20)

Separate technical conditions, team practices, organizational constraints and individual development needs. Repository evidence does not establish a person's competence or intent. Ask how goals, decision rights, incentives, staffing, dependencies and feedback loops produce observed outcomes. Identify strengths that can be extended.

Map business capabilities to accountable teams, service/data/control owners and escalation paths. Test whether the team that owns a service can deploy, operate, fund and improve it within clear boundaries. Cross-team controls need explicit shared responsibilities without duplicating ambiguous accountability. Risk acceptance needs the right business owner, not a default architect signature.

## Coaching by function

| Leader | Useful questions | Practical exercise / success evidence |
|---|---|---|
| Product | Which customer outcome or market commitment changes the architecture? Which assumptions are weakest? | Convert a roadmap item into business and quality scenarios with measurable acceptance. |
| Application engineering | Where does change fan out, and why? Which invariant is repeatedly violated? | Trace one change/failure; improve a bounded seam and measure change effort/defects. |
| Platform/infrastructure | Which developer/customer problem does the platform solve? Who operates exceptions? | Interview consumers, improve one self-service path, measure adoption/time saved. |
| Data | Which decision depends on this data? Who owns its definition and failures? | Reconcile one end-to-end metric, establish contract and exception ownership. |
| Security/privacy | Where is exposure concentrated? Which control is evidenced versus assumed? | Trace a cross-boundary scenario and demonstrate prevention/detection. |
| Reliability/operations | Which failure most threatens the business promise? What have we actually recovered? | Run an authorized tabletop or safe recovery exercise with measured gaps. |
| Finance/control owners | Which product/data paths affect reporting and evidence? | Agree scope and one reproducible control/evidence chain with engineering. |
| Executive leadership | Which investments create options, reduce exposure, or enable revenue? | Compare status quo and two viable options with costs, owners and review triggers. |

Coaching should include a diagnostic question, a teachable decision principle, a delegated exercise, an observable outcome and a follow-up trigger. Avoid performance ratings or generic exhortations. A leader can delegate execution while retaining accountability for outcomes and escalation.

## Architecture governance and documentation

Use lightweight decision records for consequential choices: context, options, evidence, consequences, owner and reversal/review trigger. Record accepted exceptions with expiry/trigger and compensating measures. Replace central approval bottlenecks with clear boundaries and automated checks where appropriate, while retaining necessary segregation and independent assurance.

Maintain current system context, responsibilities, data/trust flows, invariants, critical failure behavior, runbooks, API/data contracts, ownership and decision rationale. Documentation quality is demonstrated by onboarding, incident response and safe changes. Keep current-state facts close to implementation; clearly separate proposed target state. Avoid diagrams that hide the operational dependencies that determine recovery.

## Investment and roadmap

Connect each initiative to a customer/business outcome, evidence-based exposure or capability gap. Include economic assumptions, opportunity cost, dependencies, staffing and transitional risk. Distinguish immediate containment, foundational improvements, growth enablement and experiments. Make tradeoffs explicit: latency versus locality, isolation versus cost, autonomy versus consistency, delivery speed versus control precision.

Use now/next/later or 30/60/90-day commitments only with realistic capacity. Name a role owner and acceptance evidence for every action. Executive readouts should lead with decisions needed, top exposures, opportunities, confidence and investment options; keep technical details available for accountable teams. Reassess benefits and assumptions, including whether to stop an initiative.
