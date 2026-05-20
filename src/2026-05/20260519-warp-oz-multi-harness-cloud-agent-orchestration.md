# A single pane of glass for managing all of your cloud agents
**Source**: https://www.warp.dev/blog/multi-harness-cloud-agent-orchestration
**Date**: May 19, 2026
**Author**: Warp
**Keywords**: Warp, Oz, multi-harness, cloud agents, Claude Code, Codex, agent orchestration, enterprise

## Elevator pitch
Warp launches Oz as the first multi-harness control plane for cloud agents, letting enterprises run Claude Code, Codex, and Warp Agent side by side with unified triggers, environments, secrets, and observability.

## Takeaways
- Oz now supports three harnesses — Warp Agent, Claude Code, and Codex — all sharing the same triggers (Slack, Linear, schedules, CI, API), environments, and secrets.
- The key value proposition is avoiding vendor lock-in: enterprises can pick the best agent runtime per task without betting on a single model or harness.
- All harnesses inherit the same Oz platform features: observability, access control, billing, and orchestration — a "single pane of glass" for managing distributed coding agents.
- Third-party harnesses (Claude Code, Codex) run as cloud agents alongside Warp's native agent, with the same deployment patterns including self-hosting options (Docker, Kubernetes, direct).
- Warp Agent remains the only harness capable of orchestrating subagents and full terminal access, giving it a differentiation within the multi-harness ecosystem.
- The platform supports team-wide cloud agents triggered by events, schedules, or integrations, with cloud-synced conversations and session sharing.

## Synthesis
Warp's multi-harness Oz launch is a strategic move in the increasingly crowded agent orchestration space. Rather than competing on model quality, Warp is competing on operational infrastructure — the layer that enterprises actually need to deploy agents at scale. By supporting Claude Code, Codex, and its own Warp Agent as interchangeable runtimes, Oz positions itself as Switzerland in the agent wars.

The architecture is pragmatic. All three harnesses share the same triggers, secrets, environments, and observability. An enterprise team can trigger a Claude Code agent from a Slack message, run a Codex agent on a schedule, and use Warp Agent for tasks requiring subagent orchestration — all through the same control plane. This modularity addresses the real enterprise concern of vendor lock-in at a time when the agent landscape shifts monthly.

Warp Agent's unique position as the only harness with full subagent orchestration and terminal access gives Warp a carrot for its own runtime without forcing it. The self-hosting options (Docker, Kubernetes, direct) suggest Warp is targeting enterprises with existing infrastructure who want agent capabilities without migrating to a new platform.

The "single pane of glass" framing is more than marketing. As enterprises deploy agents across development workflows — PR reviews, issue triage, scheduled code maintenance, CI/CD pipelines — the management surface area explodes. Oz's bet is that the winning platform won't be the best agent, but the best place to run all of them.
