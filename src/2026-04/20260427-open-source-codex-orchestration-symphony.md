# An open-source spec for Codex orchestration: Symphony
**Source**: https://openai.com/index/open-source-codex-orchestration-symphony/
**Date**: April 27, 2026
**Author**: Alex Kotliarskyi, Victor Zhu, Zach Brock
**Keywords**: Symphony, Codex, agent orchestration, OpenAI, harness engineering, Linear, coding agents, multi-agent

## Elevator pitch
OpenAI open-sourced Symphony, a SPEC.md-based agent orchestrator that turns a project management board like Linear into a control plane for coding agents, resulting in a 500% increase in landed PRs among some internal teams.

## Takeaways
- Symphony is technically just a SPEC.md file — a language-agnostic specification that any implementation can follow, turning an issue tracker into an always-on agent orchestrator.
- The orchestrator watches the task board, ensures every active task has an agent running, restarts crashed/stalled agents, and manages CI/rebase/merge pipelines.
- Among OpenAI teams, landed PRs increased by 500% in the first three weeks; Linear founder noted a spike in workspaces created after release.
- The economics of code changes shift: the cost of trying an idea drops to near zero, enabling speculative exploration and throwaway prototypes.
- Non-engineers (PMs, designers) can file feature requests directly into Symphony and receive review packets with video walkthroughs.
- Key lesson: treating agents as rigid state machine nodes is limiting — give them objectives and tools instead, letting them reason about how to complete tasks.
- Not every task fits: ambiguous problems requiring strong judgment still need interactive Codex sessions.

## Synthesis
OpenAI engineers Alex Kotliarskyi, Victor Zhu, and Zach Brock describe how they solved the next bottleneck after harness engineering: the human attention ceiling. Even with powerful coding agents, engineers could only manage 3-5 parallel sessions before context switching became counterproductive. The solution was Symphony.

Symphony's key insight is reorienting the system around deliverables rather than sessions. Instead of engineers manually steering Codex instances, an open Linear issue automatically gets an agent that works continuously until done. This decouples work from sessions and from PRs — some issues produce multiple PRs across repos, others are pure investigation without touching the codebase.

The architecture is deliberately minimalist: Symphony is a SPEC.md file defining the problem, goals, and component specifications (Workflow Loader, Config Layer, Issue Tracker Client, Orchestrator, Workspace Manager, Agent Runner). Implementations are language-agnostic and expected to document their own trust and safety posture. The orchestrator polls the issue tracker on a cadence, dispatches work with bounded concurrency, and handles restart recovery without a persistent database.

The results were dramatic: 500% more landed PRs among some teams in the first three weeks. But the deeper shift was behavioral — when the cost of trying an idea drops to near zero, teams explore more. PMs and designers can file feature requests directly, receiving review packets with video walkthroughs. Agents handle CI watching, rebasing, conflict resolution, and flaky check retries — the "last mile" of landing PRs.

The team learned that rigid state machines constrain agent capabilities. Early versions only asked Codex to implement tasks; later versions gave it tools (gh CLI, CI log reading) and broader objectives. The takeaway: treat agents like direct reports — give them goals, context, and tools, then let them reason about the best approach. Not every task fits this model — ambiguous, judgment-heavy work still benefits from interactive sessions — but Symphony handles the routine bulk, letting engineers focus on one hard problem at a time.
