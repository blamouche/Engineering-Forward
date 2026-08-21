# Factory 2.0: From Coding Agents to Software Factories
**Source**: https://factory.ai/news/software-factory
**Date**: 2026-06-15
**Author**: Matan Grinberg, Eno Reyes (Factory.ai)
**Keywords**: Factory, software factory, autonomous agents, Droids, model independence, sovereign intelligence, continual learning, SDLC, multi-agent, Missions

## Elevator pitch
Factory announces its next phase: moving from individual coding-agent productivity to organization-wide "software factories"—interconnected, agent-native systems that automate the entire software development lifecycle with model independence, sovereign intelligence, and continual self-improvement.

## Takeaways
- The software factory concept extends beyond individual engineer productivity to an end-to-end system: signals → triage → planned changes → build → test → review → ship → monitor → more signals
- Three pillars define a robust software factory: model independence (choosing or routing to optimal models), sovereign intelligence (owning your data and learning loop), and continual learning (every SDLC stage instrumented and feeding back into the system)
- Already in production at NVIDIA, EY, Adobe, Palo Alto Networks, Adyen, Blackstone, Wipro, and Comarch
- Factory offers a spectrum of autonomy: simple Droid agents for well-defined tasks, Automations for recurring workflows, Droid Computers for long-running local agents, and multi-agent Missions for complex tasks over hours or days
- Engineers' roles shift from building software to building the factories that build software—with responsibilities expanding to governance, safety, and business outcomes

## Synthesis
Factory's 2.0 announcement represents a significant conceptual shift in the AI coding tools landscape. While most AI coding products focus on making individual engineers more productive, Factory argues that organization-wide productivity requires a fundamentally different approach—an interconnected system that treats the entire software development lifecycle as a continuous feedback loop.

The software factory model starts with external signals (bug reports, customer feedback, business requirements), triages them into planned changes, and then runs those changes through build, test, review, secure, ship, and monitor stages. Monitoring generates new signals, closing the loop. The key insight is that almost no organization has meaningfully instrumented this loop to be fully AI-driven—Factory is positioning itself to be the platform that does.

The three architectural pillars are worth examining. Model independence acknowledges that no single model fits every enterprise need, and Factory's Router can automatically select the best model per task based on cost, performance, and speed. Sovereign intelligence means the system learns from itself—every agent session, code review, and resolved incident feeds back into organizational context—while offering deployment flexibility from fully hosted to air-gapped. Continual learning ensures that when code review, security analysis, documentation, QA, and incident response all run on the same platform, they share context: a security finding informs code review, a deployment triggers documentation, an incident correlates with its causing PR.

The customer list is impressive—NVIDIA, EY, Adobe, Palo Alto Networks—and suggests enterprise traction beyond typical startup early adopters. Factory's autonomy spectrum (Droids → Automations → Droid Computers → Missions) recognizes that not every process should use long-horizon autonomous tasks, and that autonomy is a gradual maturation process specific to each organization's readiness.

The most provocative claim is about the evolving role of engineers: no longer sole custodians of building software, but responsible for building the factories that build software. This reframes engineering as a meta-discipline encompassing governance, safety, and business outcome ownership—a significant expansion rather than the displacement narrative that dominates much AI-coding discussion.