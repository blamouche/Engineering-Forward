# The Pulse #159: Long-running agents and orchestrating lots of them
**Source**: https://newsletter.pragmaticengineer.com/p/the-pulse-159-long-running-agents
**Date**: 2026-01-15
**Author**: Gergely Orosz
**Keywords**: long-running agents, agent orchestration, Cursor, Claude Code, OpenCode, Codex, AI coding tools, developer workflows

## Elevator pitch
As of early 2026, experimentation with long-running AI agents and multi-agent orchestration is emerging as one of the year's key development trends, with early examples from Cursor and CLI-based coding tools, while competitive dynamics intensify between AI coding platforms like Claude Code, which bans OpenCode, and Codex, which embraces integration.

## Takeaways
- Long-running agents and orchestrating multiple agents simultaneously is becoming a major experimentation frontier for engineering teams in 2026
- Cursor is among the first tools to demonstrate practical multi-agent workflows that developers can orchestrate
- Claude Code notably banned OpenCode integration while Codex actively embraced and integrated with it, highlighting diverging competitive strategies
- The shift from single-agent to multi-agent workflows represents an evolution beyond the initial AI coding assistant paradigm
- Infrastructure and cost implications of long-running agents remain under-explored areas as adoption accelerates

## Synthesis
The Pulse #159 from The Pragmatic Engineer, published in January 2026, identifies long-running agents and multi-agent orchestration as one of the defining trends that will shape software engineering throughout the year. As AI coding tools mature beyond simple tab completion and single-session pair programming, the frontier is shifting toward agents that can run autonomously for extended periods and coordinate with other agents to complete complex tasks.

This represents a significant evolution from the first wave of AI coding assistants. Where early tools like GitHub Copilot provided inline suggestions and later tools like Claude Code enabled conversational coding sessions, the emerging paradigm envisions agents that developers can task with multi-step objectives and let run in the background—potentially across hours or even days. The implications for developer workflow are profound: engineers shift from writing code to specifying objectives, reviewing outputs, and orchestrating multiple concurrent agent tasks.

The competitive landscape among AI coding platforms is also heating up. A notable flashpoint covered in this issue is the divergent approaches of Claude Code and Codex toward OpenCode integration. Claude Code (Anthropic) took the defensive position of banning OpenCode, while Codex (OpenAI) embraced integration—a strategic contrast that reflects broader tensions in the AI tools ecosystem between walled-garden approaches and open integration strategies.

Early experiments from Cursor demonstrate what multi-agent workflows look like in practice, with developers able to kick off multiple specialized agents for different aspects of a task—one for implementation, another for testing, another for documentation. However, the article also highlights that the infrastructure requirements and cost implications of running many agents for extended periods remain significant unknowns. As teams move from experimentation to production-scale adoption in 2026, these operational concerns—GPU utilization, token costs, rate limiting, and agent coordination overhead—will become increasingly critical.

The broader theme is that agent orchestration mirrors the trajectory of cloud infrastructure: what started as manual, single-instance management evolved into orchestration platforms like Kubernetes. Similarly, the jump from single-agent coding to orchestrating fleets of agents represents the next maturity level for AI-assisted software development, and 2026 looks to be the year this transition begins in earnest.
