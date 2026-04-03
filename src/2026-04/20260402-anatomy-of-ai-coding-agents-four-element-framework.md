# AI Coding Agents, Deconstructed
**Source**: https://blog.apiad.net/p/the-anatomy-of-ai-coding-agents
**Date**: April 2, 2026
**Author**: Alejandro Piad Morffis
**Keywords**: AI coding agents, context management, framework design, modes, skills, commands, subagents, failure modes

## Elevator pitch
Context is the bottleneck in agentic systems, not the model; Morffis proposes a four-element framework (Mode, Skill, Command, Subagent) to address the systemic failure modes of unstated assumptions, permission leakage, and context saturation.

## Takeaways
- Three recurring failure modes: unstated assumptions, permission leakage (plan/build modes aren't enforced), and context saturation
- Four-element framework: Mode (persona + enforced permissions), Skill (implicitly applied domain knowledge), Command (explicitly invoked workflow), Subagent (ephemeral delegation)
- Context saturation occurs around 40-60% utilization; active management rather than linear growth is required
- Framework demonstrated across software development, research, and technical writing domains
- Identifies remaining gaps: better command structure, sandboxed security, and context-aware execution

## Synthesis
Morffis's anatomy of AI coding agents is valuable because it identifies systemic failure modes rather than describing what agents can do at their best. The three failure modes — unstated assumptions, permission leakage, and context saturation — occur reliably enough to shape the design of any serious agent architecture.

Unstated assumptions is the most subtle failure mode. Agents trained on large code corpora have strong default behaviors for common programming decisions: which error handling patterns to use, how to structure module boundaries, which libraries to reach for. These defaults are appropriate for training data but often wrong for specific codebases with established conventions. Without explicit representation of project-specific conventions as agent knowledge, agents silently apply training defaults instead.

Permission leakage is a more tractable problem but one that current tools handle poorly. "Plan mode" and "build mode" in common coding agents are suggestions rather than enforced constraints — nothing prevents a planning agent from making file modifications or a build agent from restructuring the architecture it was supposed to implement unchanged. Enforced permission boundaries at the mode level would prevent a large class of unwanted agent behaviors.

Context saturation is the hardest to manage because it is cumulative. Each tool call, file read, and agent reflection adds to the context window. Without active management, context grows until it either hits the limit or degrades reasoning quality through signal-to-noise ratio reduction. The 40-60% saturation target Morffis identifies as optimal suggests that agents should be designed to stay below half of context capacity, leaving room for the work that follows.

The four-element framework addresses these failure modes at the architectural level. Modes with enforced permissions prevent leakage. Skills as implicitly applied domain knowledge address unstated assumptions without requiring explicit invocation. Commands as explicit workflow invocations provide reproducible step sequences. Subagents as ephemeral delegates enable context isolation — a subagent completes a bounded task and returns a summary, preventing its context from polluting the parent agent's reasoning window.

The remaining gaps Morffis identifies — particularly context-aware execution that maintains 40-60% saturation rather than growing linearly — point toward agent runtime infrastructure that does not yet exist in commodity tools.
