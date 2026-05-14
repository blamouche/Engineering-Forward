# How Uber Uses AI for Development: Inside Look
**Source**: https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development
**Date**: March 10, 2026
**Author**: Gergely Orosz
**Keywords**: Uber, AI, agentic coding, Minion, MCP, developer tools, Shepherd, uReview, Claude Code

## Elevator pitch
Uber's principal engineer and engineering director reveal how they built Minion, Shepherd, uReview, and an internal AI platform with an MCP gateway — achieving 84% developer agentic coding adoption and 65-72% AI-generated code inside IDEs, while grappling with 6x cost increases since 2024.

## Takeaways
- 84% of Uber devs use agentic coding monthly; 65-72% of code in IDEs is AI-generated, with Claude Code usage nearly doubling from 32% to 63% in three months
- Uber built an MCP gateway, Agent Builder, and AIFX CLI to provide a unified AI platform across the company — a "tiger team" designed the entire MCP strategy
- Minion is Uber's background agent platform with monorepo access, enabling engineers to kick off parallel agents while waiting for others to complete
- Specialized agents include uReview for high-signal AI code review, Autocover generating 5,000+ unit tests/month, and Shepherd for end-to-end migration management
- AI costs are up 6x since 2024 and token cost optimization is now a growing priority; top-down AI mandates are less effective than peer-sharing of wins

## Synthesis
At the Pragmatic Summit in San Francisco, Uber principal engineer Ty Smith and director of engineering Anshu Chada provided an unusually transparent look at how a major tech company is integrating AI across its engineering function. Uber, which employs nearly 3,000 people in its tech function, has embedded AI into its official strategy with the goal of becoming a "GenAI-powered" company — not as a vague aspiration, but with concrete infrastructure and measurable outcomes.

The core of Uber's approach is a four-layer architecture. The bottom layer is the internal AI platform, built on top of Michelangelo (Uber's existing ML/AI platform), providing a model gateway to proxy frontier and internally hosted models. The second layer provides AI agents with context — source code, documentation, Slack, JIRA — effectively giving agents "memory" of Uber's entire engineering surface. The third layer supports industry agents like Claude Code, GitHub Copilot, Cursor, and Codex. The fourth layer consists of specialized internal agents: Minion (background agent platform), uReview (code review), Autocover (test generation), and Shepherd (large-scale migrations).

The MCP Gateway is particularly instructive. Uber formed a "tiger team" to design their MCP strategy and built a centralized gateway that proxies internal Thrift/Protobuf/HTTP endpoints as MCP servers with simple configuration changes. This abstracts away authentication, authorization, telemetry, and logging into a single platform concern, while providing a registry and sandbox for developers to discover and experiment with MCP servers. The Uber Agent Builder complements this with a no-code interface for building agents that can access internal data and hand off work to other agents, visualized through Agent Studio for debugging and evaluation.

The most striking insight is how AI is changing the act of programming itself at Uber. The pre-AI workflow was linear: plan, code in an IDE, review. The current workflow involves devs orchestrating multiple parallel agents. As Ty Smith notes, engineers naturally kick off additional background agents while waiting for one to complete — a behavioral shift from single-threaded coding to concurrent agent management. The AIFX CLI serves as the unified interface for provisioning agents, discovering MCP servers, running background tasks, and keeping tooling updated.

The challenges are as revealing as the achievements. Despite 92% monthly agent usage, adoption has been slower than expected, and top-down mandates prove less effective than engineers sharing peer successes. AI-related costs are up 6x since 2024, making token cost optimization a growing concern. The split between IDE-based tools (plateauing) and CLI-based agents like Claude Code (nearly doubling) suggests a structural shift toward terminal-first AI workflows. For engineering organizations watching Uber's playbook, the message is clear: successful AI adoption requires significant platform investment in context, governance, and cost management — not just tool licenses.
