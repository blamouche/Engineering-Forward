# Long-running Agents

**Source**: https://addyosmani.com/blog/long-running-agents
**Date**: Unknown
**Author**: Addy Osmani
**Keywords**: long-running agents, agent harnesses, persistence, verification, orchestration

## Elevator pitch
Long-running agents matter less because they can reason for longer in one sitting than because they externalize memory, recovery, and verification into durable systems that let useful work continue across sessions, sandboxes, and failures.

## Takeaways
- Addy Osmani separates long-horizon reasoning, long-running execution, and persistent agency as related but distinct agent problems.
- The practical bottlenecks are finite context windows, missing persistent state, and weak self-verification.
- Durable artifacts such as task files, progress logs, and event streams are what let agents resume useful work after interruptions.
- Anthropic's managed-agent architecture illustrates a broader trend toward decoupling model logic, execution sandboxes, and session logs.
- Lightweight practitioner patterns like the Ralph loop already approximate these ideas with ordinary files and repeated sessions.

## Synthesis
This article argues that the next meaningful step in agent engineering is not a smarter chat loop but an execution model that survives time, failure, and context resets. Osmani starts by clarifying that people often bundle several different ideas together under the label of long-running agents. There is long-horizon reasoning, where a model can handle more dependent steps. There is long-running execution, where a harness invokes the model over many hours or days. And there is persistent agency, where an agent accumulates identity and memory across tasks. Distinguishing those layers is useful because each creates different engineering constraints and business opportunities.

The central claim is that the limiting factor is not raw intelligence alone. It is operational continuity. Standard chat-based agents run into three recurring problems: the context window fills, session state disappears, and the model is too optimistic when evaluating whether its own work is actually done. Those failure modes explain why many agents look impressive for a few minutes and then become unreliable as tasks stretch across hours or across multiple restarts. Long-running systems need state outside the model, plus verification signals outside the model's own self-assessment.

Osmani's most practical contribution is the emphasis on external artifacts. He points to lightweight patterns such as task lists, progress logs, and rule files that live on disk and get re-read by each new session. That makes the filesystem, or a session log, the durable memory rather than the context window. In that framing, a supposedly amnesiac model can still produce continuity if the surrounding harness keeps enough structured state around it. This is why simple practitioner setups like the Ralph loop can work surprisingly well. They are crude, but they solve the right problem: handoff between sessions.

The article also uses Anthropic's public writing on managed agents to show how this pattern is becoming institutionalized. Separating the brain, the hands, and the session log means a crashed sandbox or a new execution container does not destroy the run. That architecture matters because it shifts reliability from the model to the system around the model. Recovery stops being a heroic prompt trick and becomes a property of the harness.

Overall, the piece is useful because it reframes agent progress away from spectacle and toward systems design. Long-running agents are valuable not because they endlessly think, but because they can pick up unfinished work, preserve context in durable structures, and keep moving without a human re-explaining the task each time. That is the path from demo-grade assistants to software and research workflows that remain dependable over time.