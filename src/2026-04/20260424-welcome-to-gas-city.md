# Welcome to Gas City
**Source**: https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607
**Date**: April 24, 2026
**Author**: Steve Yegge
**Keywords**: Gas City, Gas Town, agent orchestration, dark factories, MEOW, Beads, Dolt, multi-agent, SDK

## Elevator pitch
Gas City, built by Chris Sells and Julian Knutsen from Yegge's vision, transforms Gas Town from an opinionated monolith into a composable SDK for building arbitrary agent orchestration topologies with enterprise-grade reliability, MIT licensing, and a growing Discord community.

## Takeaways
- Gas City deconstructs Gas Town into composable "packs" — declarative building blocks that let you assemble arbitrary agent topologies rather than being locked into one team shape.
- Built on the MEOW stack (Molecular Expression of Work), a Beads-based framework backed by Dolt, a git-versioned database — giving every agent action full version history and forensic auditability.
- Comes with a default "Gas Town" pack as a drop-in replacement, making migration seamless; also supports fine-grained model selection for cost control.
- Unlike Claude Code's "dark" subagents, Gas City keeps all agent workers visible and addressable — Yegge calls it a "Light Factory" where observability is a deliberate design choice.
- Beyond coding: dark factories can automate any business process, from CI/CD pipelines to incident response to image moderation queues.
- Gas City is built by serious, disciplined engineers (Knutsen, Sells) rather than Yegge's Wild West vibe-coding approach — enterprise-focused, MIT-licensed, rapidly maturing.

## Synthesis
Steve Yegge's "Welcome to Gas City" marks the transition of his multi-agent orchestration vision from a solo experiment into a community-driven enterprise SDK. Published in April 2026, the post celebrates the v1.0.0 release of Gas City, built by Chris Sells (former Flutter lead at Google) and Julian Knutsen based on the architectural vision Yegge outlined in January.

The key architectural shift from Gas Town to Gas City is composability. Where Gas Town was a hardwired team of seven agent roles, Gas City deconstructs everything into "packs" — declarative, composable building blocks that let developers assemble arbitrary agent topologies. The default pack replicates the original Gas Town configuration, making migration a drop-in replacement, but the SDK enables custom orchestrator designs for any workflow.

The technical foundation is the MEOW stack (Molecular Expression of Work), which places "Work" as a first-class system primitive. Built on Beads and backed by Dolt — a git-versioned SQL database — every agent action, every task state transition, and every piece of inter-agent communication gets full version history. This creates unparalleled forensic and auditing capabilities: you can trace exactly what any agent did and why.

Yegge introduces the "Light Factory" concept as a counterpoint to the industry's "dark factory" terminology. In Gas City, all agent workers are visible and addressable — you can dive into any worker's session at any time. This observability is deliberate, not accidental, and it differentiates Gas City from coding agents that hide subagent activity behind the scenes.

The post also broadens the scope of what agent orchestrators can do. Yegge shares a personal example: moderating player-uploaded images for his online game Wyvern. This has nothing to do with writing code — it's a routine business process that a dark factory can fully automate. As Yegge puts it, "devs will become shepherds, tending flocks of agents which do the ground-level work."
