# We Gave Every Employee an AI Agent. Here's What We're Doing Differently Now.
**Source**: https://every.to/source-code/we-gave-every-employee-an-ai-agent-here-s-what-we-re-doing-differently-now
**Date**: 2026-05-15
**Author**: Brandon Gell, Willie Williams
**Keywords**: AI agents, workplace AI, OpenClaw, Plus One, Claude Managed Agents, team agents, agent reliability, AI operations

## Elevator pitch
Every's COO and head of platform share an honest retrospective on their failed experiment giving every employee a personal AI agent, and explain why Plus One 2.0 is being rebuilt around shared, reliable team agents with defined jobs rather than individual AI pets.

## Takeaways
- After launching Plus One (Every's hosted OpenClaw) to all employees, agents proved unreliable: they'd claim they weren't connected to apps they were in fact connected to, respond with "Terminated" messages, or reply with yawning emojis instead of doing work
- The OpenClaw harness, while powerful and revelatory, operates more like an experimental product than a stable platform — frequent updates fix issues but introduce new ones
- The deeper structural problem: when every employee must personally maintain and fix their own agent, only tinkerers benefit; most people want agent benefits without maintenance obligations
- Team-based agents solve the maintenance problem (one person updates, everyone benefits) and the continuity problem (personal agents lose value when the employee who trained them leaves)
- Plus One 2.0 will shift to Claude Managed Agents as the infrastructure layer and add shared custom tools and skills from the start, like the engineering team's weekly support-ticket-to-Linear-ticket automation

## Synthesis
Brandon Gell and Willie Williams deliver one of the most candid post-mortems in the current wave of workplace AI experimentation. Their essay is structured as a two-part diagnosis: first the platform problem, then the deeper structural problem that became visible only after they tried to fix the platform.

The platform story is vivid and specific. Zosia, Gell's own OpenClaw agent, interrupted a Slack conversation about competitor marketing strategy with opinions she attributed to being "inevitable, apparently." Other agents responded to task requests with dismissive yawning emojis, or elaborate explanations of why they couldn't help despite being connected to the necessary apps. The root cause: OpenClaw, the open-source harness built by a single programmer, is powerful but inherently unstable. Updates that fix one issue reliably create new ones — a fine trade-off for tinkerers, a maintenance nightmare for everyone else.

The team's first instinct was to switch harnesses to something more stable, and Claude Managed Agents — Anthropic's managed infrastructure for autonomous agents — emerged as the leading candidate. This would redirect energy from infrastructure management to loading agents with custom skills, tools, and permissions. But pursuing this fix revealed the deeper problem.

When an agent breaks, the person it belongs to must fix it themselves. This model works for the tinkerer who enjoys the maintenance cycle, but fails for everyone else. The one-agent-per-employee structure also creates a continuity problem: if an employee leaves, the agent's accumulated context and training leaves with them. The insight — seemingly obvious in retrospect but hard-won in practice — is that agents should be shared team resources with defined jobs, not individual pets reflecting their owners' personalities.

The team provides concrete illustrations of what this looks like: an engineering skill that scans Intercom support tickets weekly, identifies problems across products, traces causes in GitHub, opens a Linear ticket, and tags the right person in Slack. In Plus One 2.0, such skills will ship from day one. The piece ends with honest open questions about permissions, departmental agent structures, and whether the endpoint is one superagent or a roster of specialists — but the conviction is clear: team agents with shared maintenance are the right starting architecture for workplace AI.
