# The Pulse: AI load breaks GitHub – why not other vendors?
**Source**: https://newsletter.pragmaticengineer.com/p/the-pulse-github-breaks
**Date**: 2026-04-30
**Author**: Gergely Orosz
**Keywords**: GitHub reliability, AI infrastructure, Anthropic, Claude Code, GitHub Copilot, Mitchell Hashimoto, building block economy, Codex, developer trust, vendor lock-in

## Elevator pitch
GitHub's reliability has collapsed to below one nine (86-90%) under surging AI-generated load, while Anthropic's recent decisions—silently nerfing Claude Code, banning companies, and raising prices—represent a sharp erosion of developer trust, and industry veteran Mitchell Hashimoto proposes the "building block economy" as open source's path forward in an AI-dominated landscape.

## Takeaways
- GitHub's reliability dropped to 86% with a data integrity incident, which leadership attributes to a 3.5x increase in service load driven largely by AI agent traffic
- Mitchell Hashimoto, creator of Ghostty and prolific open source contributor, announced he is quitting GitHub, declaring it no longer suited for professional work
- Anthropic has rapidly burned through developer goodwill in a single month through silent Claude Code nerfs, company bans from Claude, and significant price increases
- GitHub Copilot imposed dramatic price increases while Codex experienced explosive growth, reshaping the economics of AI coding tools
- Hashimoto's "building block economy" thesis argues that open source components win massive adoption but face increasing difficulty building sustainable businesses on top of them

## Synthesis
The April 30, 2026 edition of The Pulse documents a convergence of crises affecting the developer tools ecosystem. At the center is GitHub's alarming reliability collapse. Third-party trackers showed GitHub's availability dropping from one nine (90%) to effectively zero nines (86%) in a single month, compounded by a serious data integrity incident. GitHub leadership's explanation points to a 3.5x increase in service load, which The Pragmatic Engineer connects directly to the explosive growth of AI coding agents that programmatically push, pull, and interact with repositories at rates far exceeding human developers.

The implications of this degradation are severe enough that Mitchell Hashimoto—creator of Vagrant, Terraform successor, and Ghostty terminal—publicly quit the platform, arguing it is no longer suitable for professional software development. This is a remarkable indictment from one of open source's most respected figures, and it raises uncomfortable questions: if GitHub cannot handle AI-generated load, why haven't other infrastructure vendors (package registries, CI/CD platforms, artifact repositories) experienced similar breakdowns? The article suggests the answer may lie partly in self-inflicted architectural choices rather than purely external demand.

Simultaneously, Anthropic's relationship with developers has soured dramatically. Within a single month, the company silently reduced Claude Code capabilities, began banning certain companies from using Claude, and imposed steep price increases—all without transparent communication. This pattern suggests what the article characterizes as an "extraction era": generating more revenue from the same or degraded service. For a company that previously enjoyed near-universal developer affection, this represents a remarkable reversal and a cautionary tale about the fragility of developer trust in an AI vendor landscape with few alternatives.

The industry pulse section captures broader turbulence: GitHub Copilot's dramatic price increases, Codex's explosive growth as an alternative, Google scrambling to build competitive coding models, and rumors of SpaceX/Cursor acquisitions. Hashimoto's "building block economy" concept offers a philosophical counterpoint—arguing that open source components achieve massive adoption precisely because they function as composable building blocks, but the business models that sustained open source are under pressure as AI changes both how software is built and how it's monetized.

The overarching theme is infrastructure strain. The AI revolution in software development is not just a tooling shift—it is generating fundamentally different traffic patterns, usage volumes, and economic pressures that the existing developer platform infrastructure was never designed to handle, and the gap is becoming impossible to ignore.
