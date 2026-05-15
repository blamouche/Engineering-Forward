# Development environments for your cloud agents
**Source**: https://cursor.com/blog/cloud-agent-development-environments
**Date**: May 13, 2026
**Author**: Samantha Whitmore, David Wetterau & Nick Bradford
**Keywords**: cloud agents, development environments, Cursor, multi-repo, Dockerfile, agent infrastructure, enterprise

## Elevator pitch
Cursor ships new tools for configuring cloud agent development environments with multi-repo support, environment-as-code via Dockerfiles, and enterprise governance controls — making it possible to run fleets of parallelized agents that handle engineering tasks end-to-end.

## Takeaways
- Cloud agents need full development environments (cloned repos, dependencies, credentials, build systems) to close the loop on work rather than just writing code
- Multi-repo environments let agents reason across microservices and multiple codebases, with early adopters like Amplitude using it for automated issue triage
- Environment configuration as code via Dockerfiles now supports build secrets and 70% faster rebuilds via improved layer caching
- Cursor can auto-configure Dockerfiles by inspecting repos — currently in private beta for Enterprise teams
- New governance features include environment version history, audit logs, and egress/secrets scoped per environment

## Synthesis
Cursor's latest release addresses a critical gap in the agent development workflow: the environment itself. Agents that can only generate code without running tests, querying services, or reaching internal APIs cannot independently verify their work. The core insight is that cloud agents need environments that mirror a developer's laptop setup — cloned repositories, installed dependencies, credentials, and access to toolchains.

Multi-repo support is the standout feature. Most enterprise engineering spans multiple codebases, and a single-repo agent has limited usefulness. Cursor enables environments with multiple repositories that persist across sessions, allowing agents to reason about cross-repo impacts. Amplitude's engineering manager reports that agents can now investigate reported issues, identify which repos are affected, and open PRs with fixes — all with full context.

The infrastructure-as-code approach via Dockerfiles brings reproducibility and auditability. Build secrets allow secure access to private registries without leaking credentials into the agent runtime, while improved caching cuts rebuild times by 70%. Notably, Cursor can inspect repositories and auto-generate Dockerfiles, reducing the configuration burden on teams — though this is still in private beta.

Governance receives thoughtful attention: environment version history with rollback capabilities, audit logs for every action, and network egress controls scoped per environment. This reflects the enterprise reality that different environments need different security postures.

The trajectory points toward environments that evolve autonomously as codebases change, rather than being static configurations. As agent-based development scales, the environment layer — not just the model — becomes a key differentiator in agent effectiveness.
