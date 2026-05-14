# The Pulse #159: Long-Running Agents and Orchestrating Lots of Them
**Source**: https://newsletter.pragmaticengineer.com/p/the-pulse-159-long-running-agents
**Date**: January 15, 2026
**Author**: Gergely Orosz
**Keywords**: AI agents, agent orchestration, long-running agents, Cursor, Claude Code, Codex, OpenCode

## Elevator pitch
2026 is shaping up as a year of experimentation with long-running AI agents and multi-agent orchestration, with early examples emerging from Cursor and tension rising between Claude Code (which banned OpenCode) and Codex (which embraced it).

## Takeaways
- Long-running agents represent the next frontier beyond single-shot AI tasks — agents that operate over extended periods managing complex workflows
- Agent orchestration — coordinating multiple agents across parallel tasks — is becoming a major area of experimentation
- Early examples of long-running agent patterns are emerging from products like Cursor
- A competitive rift is forming: Claude Code has banned OpenCode integration while Codex has embraced it
- The trend mirrors Uber's observed shift toward engineers running multiple parallel background agents simultaneously

## Synthesis
In this edition of The Pulse, Gergely Orosz identifies long-running agents and multi-agent orchestration as defining trends for 2026 in AI-assisted software development. The newsletter frames this as a natural evolution from single-task AI assistance — where an agent writes a function or fixes a bug — toward systems where agents operate continuously over hours or days, managing complex, multi-step engineering workflows.

The shift toward long-running agents represents more than a technical capability improvement; it signals a change in how engineers conceptualize their relationship with AI tools. Rather than treating AI as a faster autocomplete or a pair programmer for discrete tasks, the long-running agent paradigm positions AI as a persistent collaborator that can be assigned work, left to execute, and checked on later — much like delegating to a human colleague. This requires new infrastructure for task persistence, state management, error recovery, and progress visibility that goes well beyond what current agent tools provide.

The newsletter touches on emerging competitive dynamics in the agent ecosystem. Claude Code has chosen to ban OpenCode integration — a defensive move to protect its ecosystem — while Codex has taken the opposite approach by embracing OpenCode. This divergence suggests the agent market is entering a phase where platform strategies around openness and interoperability will determine competitive positioning, similar to earlier platform wars in operating systems and cloud services.

The trend toward agent orchestration — running and coordinating multiple agents in parallel — aligns with patterns already observed at companies like Uber, where engineers naturally gravitate toward kicking off multiple background agents simultaneously. As the tooling matures, the question becomes whether individual engineers will manage agent orchestration directly or whether orchestration layers will abstract this complexity away. The tension between open and closed approaches, combined with the infrastructure demands of long-running agents, suggests 2026 will be a foundational year for establishing the patterns that define the next era of AI-assisted software engineering.
