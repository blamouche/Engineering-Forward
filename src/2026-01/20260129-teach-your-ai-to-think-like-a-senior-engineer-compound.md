# Teach Your AI to Think Like a Senior Engineer
**Source**: https://every.to/source-code/teach-your-ai-to-think-like-a-senior-engineer-789ba7ca-ca7c-45a1-91fa-4178f59f226f
**Date**: 2026-01-29
**Author**: Kieran Klaassen
**Keywords**: AI planning, compound engineering, codebase patterns, research agents, software development strategy

## Elevator pitch
A practical framework for training AI coding assistants to understand your codebase and development preferences through eight parallel research strategies, enabling faster feature development while avoiding costly architectural mistakes.

## Takeaways
- Planning beats coding: Running specialized research agents before writing code prevents wasting time building the wrong solution entirely.
- Parallel research accelerates discovery: Multiple specialized agents researching simultaneously (rather than sequential human planning) gathers diverse knowledge more efficiently while humans provide judgment and taste.
- Fidelity levels guide strategy selection: The framework uses three complexity tiers: Fidelity One (quick fixes), Fidelity Two (multi-file features), and Fidelity Three (major unknowns).
- Institutional memory compounds: Documenting patterns and findings in project documentation creates an evolving knowledge base that improves future AI assistance.
- Eight research strategies cover systematic discovery: Starting with bug reproduction and best practices research, escalating through codebase analysis and architectural exploration.

## Synthesis
Kieran Klaassen presents a methodology for leveraging AI as a collaborative engineering partner through structured planning phases. Rather than immediately coding, the approach deploys specialized agents to investigate problems from multiple angles—examining production logs, researching industry solutions, analyzing existing code patterns, and exploring architectural tradeoffs.

The core insight challenges conventional development wisdom: "Planning had saved me from wasting time building the wrong thing entirely." When Klaassen's team needed to archive 53,000 emails without deletion, they initially assumed a simple bulk operation. Research agents discovered Gmail's rate limits, timeout risks, and system constraints that transformed a perceived quick feature into a three-day architectural redesign.

The methodology operationalizes collaborative human-AI development. While agents excel at rapid parallel research—analyzing logs, surfacing best practices, identifying code duplication—humans contribute irreplaceable judgment about product priorities, user needs, and technical taste. This division of labor accelerates discovery.

The eight strategies form a graduated toolkit. Basic approaches like bug reproduction and best-practice research apply across all complexity levels. More sophisticated strategies—grounding solutions in existing codebase patterns, researching framework documentation, analyzing performance implications—address increasingly complex features. The highest fidelity challenges demand multiple specialized agents investigating feasibility, alternative approaches, and implementation risks simultaneously.

A distinctive feature involves creating compounding value through documentation. When agents identify useful patterns or upgrade procedures, findings automatically save to project documentation. Future work checks these internal references before external research, creating an evolving institutional memory that makes successive projects progressively easier.

The framework addresses a fundamental challenge in AI-assisted development: preventing capable AI from confidently building incorrect solutions. By requiring upfront research and planning, the methodology ensures AI assistance produces well-informed decisions rather than premature optimization. The compound engineering approach treats AI not as a code generator but as a research partner whose value multiplies through accumulated context and institutional knowledge.
