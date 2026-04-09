# Scaling Managed Agents: Decoupling the brain from the hands

**Source**: https://www.anthropic.com/engineering/managed-agents
**Date**: April 9, 2026
**Author**: Anthropic
**Keywords**: Anthropic, managed agents, agent infrastructure, session logs, sandboxes, orchestration, enterprise AI

## Elevator pitch
Anthropic explains how Managed Agents turns long-running agents into a hosted systems problem by separating durable session state, stateless harnesses, and disposable execution environments.

## Takeaways
- Anthropic redesigned managed agents by splitting session logs, harness logic, and execution sandboxes into separate components.
- The architecture is meant to improve recovery, debugging, portability, and fault isolation for long-running agent workflows.
- Credential handling is pushed outside the sandbox through bundled resources and vault-backed proxies to reduce prompt-injection blast radius.
- Anthropic treats the session log as a durable context object outside the model context window rather than as the context window itself.
- The piece positions managed agents as a stable interface layer that can survive rapid model and harness evolution.

## Synthesis
This article is valuable because it frames agent deployment as an old distributed-systems problem wearing new clothes. Anthropic’s core argument is that useful long-running agents cannot be thought of as a single model invocation living inside a convenient container. Once agents need tools, files, retries, recovery, state, and credentials, they begin to look like operational software with all the usual failure modes: crashed processes, stuck sessions, debugging blind spots, and unsafe trust boundaries. Managed Agents is Anthropic’s attempt to turn that mess into a clean abstraction.

The most important move is the decoupling itself. Anthropic separates the “brain” and its harness from both the session log and the execution sandbox. That sounds architectural, but the payoff is extremely practical. If the harness crashes, the session is still there. If a sandbox dies, it can be reprovisioned. If a customer wants tools or resources in a different environment, the harness no longer assumes everything sits inside the same container. This is exactly the kind of systems design that matters more in production than another few points on a benchmark.

The security discussion is just as important. Anthropic is explicit that generated code should not live next to credentials, because a prompt injection in that world can become an escape hatch into much larger damage. By keeping auth with the resource or in a vault-backed proxy, Anthropic is trying to make the structure safer rather than simply hoping narrower scopes will stay sufficient as models improve. That is a mature stance: do not rely forever on today’s limits of model capability when you can redesign the boundary instead.

The broader implication is that managed agents may become a standard enterprise category, like managed databases or managed Kubernetes before them. If that happens, the winning vendors will not just be the ones with the smartest model. They will be the ones that make agents durable, observable, recoverable, portable, and governable. Anthropic’s article reads like a blueprint for that future, and it shows how much of the real differentiation in agent platforms is now happening below the chat interface.
