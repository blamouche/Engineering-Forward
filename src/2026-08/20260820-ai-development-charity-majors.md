# Stop Being Skeptical About AI for Development
**Source**: https://newsletter.pragmaticengineer.com/p/stop-being-skeptical-about-ai-for
**Date**: August 20, 2026
**Author**: Gergely Orosz and Charity Majors
**Keywords**: AI development, observability, engineering workflow, skepticism

## Elevator pitch
Charity Majors' case for using AI in development is conditional: use it to accelerate feedback and exploration while retaining the operational disciplines that make software trustworthy.

## Takeaways
- Skepticism is useful when it identifies a concrete failure mode rather than becoming a default refusal.
- AI speeds up generation, but it does not remove the need to understand production behaviour.
- Observability supplies the feedback needed to validate agent-assisted changes.
- Smaller, reviewable changes preserve engineering control as throughput rises.
- Teams should judge tools by outcomes in their own delivery system, not demonstrations.

## Synthesis
The episode's title presents a provocation, but its argument is more measured than an adoption mandate. AI development tools can remove friction from routine work and broaden the range of experiments an engineer can run. That does not make their output self-validating. The essential question is whether a team has enough feedback from tests, code review, deployment, and production telemetry to know what a proposed change actually does.

Majors' operational perspective makes observability central. A system that cannot explain its behaviour is hard to improve by hand and even harder to delegate to an agent. Faster code creation raises the importance of traces, metrics, and useful debugging paths because these are the evidence available to the humans who remain accountable. AI can propose an implementation, but it cannot eliminate the uncertainty created by distributed systems, changing requirements, or incomplete context.

The practical implication is to integrate tools into a disciplined delivery loop. Keep changes small enough to inspect, run targeted verification, use production signals to test assumptions, and record recurring failures so the workflow improves. This treats skepticism as an engineering function: identify the risk, instrument it, and decide from observed outcomes. It is more productive than either uncritical enthusiasm or a blanket refusal to use assistants.
