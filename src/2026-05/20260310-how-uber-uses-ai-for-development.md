# How Uber uses AI for development: inside look
**Source**: https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development
**Date**: 2026-03-10
**Author**: Gergely Orosz
**Keywords**: Uber, AI agents, developer productivity, agentic coding, MCP, Minion, code review AI, internal AI platform, Claude Code, token costs

## Elevator pitch
Uber built a comprehensive internal AI development platform—spanning MCP gateways, no-code agent builders, background agent systems, and AI-powered code review tools—achieving 84% developer adoption of agentic coding with 65-72% of code being AI-generated inside IDEs, while confronting rising token costs and adoption friction.

## Takeaways
- Uber constructed a four-layer agentic system: internal AI platform, Uber-specific context sources, industry agent tools (Claude Code, Copilot, Codex), and specialized agents for testing and code review
- The MCP Gateway provides a unified interface for all internal and external MCP servers, handling auth, telemetry, and logging centrally
- Minion, Uber's background agent platform, enables parallel agent orchestration—devs kick off multiple agents simultaneously for different tasks
- Code Inbox and uReview handle the downstream challenge of AI-generated PR noise with smart routing and high-signal automated review comments
- Despite 84% adoption, AI-related costs are up 6x since 2024 and token cost optimization has become a growing priority across engineering leadership

## Synthesis
Uber's engineering leadership presented a remarkably transparent deep-dive into their AI-for-development strategy at the 2026 Pragmatic Summit. The company has built an extensive internal AI platform that goes far beyond simply giving developers access to tools like Claude Code or Cursor. Their approach is structured across four distinct layers, reflecting the complexity of deploying AI agents at the scale of a company with nearly 3,000 people in its tech function.

The internal AI platform layer builds on Michelangelo, Uber's existing ML platform, providing a model gateway that proxies to both frontier models and internally hosted models. The context layer gives agents access to Uber's source code, engineering docs, Slack, and JIRA—essentially the "memory" for agents to be effective within Uber's specific ecosystem. The industry agents layer supports multiple tools (Claude Code, GitHub Copilot, Codex, Cursor) enabling engineers to use whatever works best. Finally, the specialized agents layer houses Uber's own tools: the background agent platform, test generation, and code review agents.

One of the most innovative components is the MCP Gateway. A dedicated tiger team designed a centralized gateway built on the Model Context Protocol that proxies internal endpoints (Thrift, Protobuffer, HTTP) as MCP servers through simple configuration changes. The gateway also exposes first-party and third-party MCPs, handling auth, telemetry, and logging in one place. The Agent Builder adds a no-code layer on top—engineers can create agents that access internal data sources and delegate work to other agents, then publish them to a discoverable registry.

The AIFX CLI solves practical deployment headaches. It provisions and updates AI agent clients across the company, discovers and configures MCP servers, runs background agent tasks, and manages versioning—solving the problem of how to keep 3,000 engineers on the latest, best-configured versions of fast-moving AI tools.

Perhaps the most significant operational insight is how AI has changed developer workflows at Uber. The old model was single-threaded: plan, code, review. Early agentic workflows added one agent to that loop. But Uber's current state sees engineers orchestrating multiple parallel agents—each kicked off with their own tasks—which fundamentally shifts the developer's role from writing code to managing and directing agent work. This parallel orchestration creates new resource and cost challenges.

The downstream effects are substantial. With more AI-generated code comes more code reviews and more noise. Uber built Code Inbox for smart PR routing and uReview for high-signal AI code review comments. Autocover generates over 5,000 unit tests per month. Shepherd manages large-scale migrations end to end. The numbers are striking: 92% of devs use agents monthly, 11% of pull requests are opened by agents, and Claude Code usage nearly doubled in three months from 32% to 63%. Yet the challenges remain real—adoption is slower than expected despite these numbers, top-down mandates are less effective than peer sharing, and the 6x cost increase since 2024 means token optimization is now a critical engineering concern alongside feature velocity.
