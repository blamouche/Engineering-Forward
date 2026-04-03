# Does GitHub Still Merit "Top Git Platform for AI-Native Development" Status?
**Source**: https://newsletter.pragmaticengineer.com/p/does-github-still-merit-top-git-platform
**Date**: April 3, 2026
**Author**: Gergely Orosz (The Pragmatic Engineer)
**Keywords**: GitHub, reliability, AI agents, Claude Code, uptime, infrastructure, platform engineering, Microsoft

## Elevator pitch
GitHub's availability has dropped to approximately 90% uptime as AI coding agent traffic (Claude Code contributions up 6x in 3 months) overwhelms infrastructure designed for human developers, with no clear leadership to address the crisis.

## Takeaways
- GitHub running at approximately 90% uptime ("one nine") — roughly 2.5 hours of degraded service daily or 3 days per month
- Root cause: infrastructure saturation from AI coding agent traffic; Claude Code contributions grew 6x in three months
- Three major outages in two months: database cluster overload, Redis cluster failures, security misconfiguration post-failover
- Competitive threat: Pierre Computer's Code.storage claims 15,000+ repos per minute handling capacity
- Organizational vacuum: no CEO since Thomas Dohmke stepped down; platform reliability deprioritized relative to Copilot revenue

## Synthesis
The GitHub reliability crisis documents a transition point in developer infrastructure: the platform designed for human developers is being stress-tested by a different kind of user — autonomous AI coding agents that interact with repositories at frequencies and volumes that human development workflows never generated.

The 6x growth in Claude Code contributions in three months is the key data point. This is not gradual organic growth that allows infrastructure teams to plan and provision ahead of demand — it is rapid adoption by a new class of users (AI agents) with fundamentally different access patterns. Humans push code when they finish a feature; agents push code continuously. Humans read repositories contextually; agents may clone and analyze entire codebases for every task. The aggregate load difference is substantial.

The uptime degradation to approximately 90% is particularly damaging for agent-based workflows. Human developers tolerate occasional outages with annoyance; AI agent pipelines that depend on GitHub for CI triggers, code review automation, and deployment gating fail completely when GitHub is unavailable. An agent that cannot push to GitHub or trigger CI cannot ship software. The 2.5 hours daily of degraded service represents 2.5 hours daily of agent productivity loss across every team using GitHub for AI-assisted development.

The absence of CEO leadership creates a governance vacuum at exactly the moment when GitHub needs strategic clarity. The platform faces a choice: invest heavily in infrastructure to serve the AI agent use case (which would require prioritizing reliability over Copilot feature development) or continue current priorities while ceding the reliability-focused market to competitors. Without a CEO, this strategic choice is difficult to make and execute.

Pierre Computer's claimed 15,000 repos per minute capacity illustrates that the AI-native repository hosting market is being defined now, and GitHub's incumbent position does not guarantee it will remain the platform of choice if reliability does not improve. For organizations building AI-native development workflows, the reliability degradation is an active evaluation trigger.
