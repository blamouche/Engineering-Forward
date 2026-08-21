# Impressions from Visiting OpenAI, Anthropic, & Cursor
**Source**: https://newsletter.pragmaticengineer.com/p/impressions-from-visiting-openai
**Date**: 2026-06-30
**Author**: Gergely Orosz
**Keywords**: cloud-agents, openai, anthropic, cursor, coding-agents, dev-tools, ai-engineering

## Elevator pitch
After visiting OpenAI, Anthropic, and Cursor's offices, the clearest trend is that cloud-based AI agents are about to go mainstream — and the way software engineers work is fundamentally shifting.

## Takeaways
- Cloud agents are emerging as the next mega-trend: OpenAI acquired Ona (formerly Gitpod) for cloud dev environments, Anthropic built Claude Managed Agents over 6 months, and Cursor released Cloud Agents and an iOS app built on them.
- Mass adoption of coding harnesses by non-developers: at OpenAI, more than 95% of non-engineers use Codex rather than ChatGPT — suggesting coding interfaces are becoming the universal AI interface.
- Engineering work is shifting toward making agents more efficient: ever more effort at Anthropic and Cursor goes into building environments for agents to execute more efficiently.
- Companies are aggressively optimizing spend-per-token: AI spending by software engineers is so high that platform teams are slashing per-token costs, with Coinbase as a case study.
- Cloud agents are happening now because coding models got "good enough," context windows expanded to 1M tokens, infra for AI coding agents matured (MCP, skills), and cloud providers built sufficient GPU capacity.

## Synthesis
Gergely Orosz's on-the-ground observations from visiting three of the most important AI labs paint a clear picture: the era of locally-running AI coding agents is giving way to cloud-based agents that operate independently of a developer's laptop. This shift is happening simultaneously at OpenAI, Anthropic, and Cursor — not as a coordinated effort, but as a convergent solution to the same set of problems.

At Anthropic, Claude Managed Agents is a substantial engineering effort led by Katelyn Lesse, built over six months as a hosted service for long-running agents across cloud providers. At OpenAI, the acquisition of Ona (formerly Gitpod) provides the cloud development environment primitive that makes cloud agents practical — persistent, sandboxed environments where agents can operate over hours or days. At Cursor, cloud agents have been shipping since late 2025, and the just-launched iOS app is fundamentally built on top of them.

The convergence is driven by practical necessity. Running agents locally means keeping your laptop open, managing CPU heat, and dealing with limited parallelism. Cloud agents solve all three problems while enabling new workflows: handling incidents on-call from your phone, kicking off investigations during a commute, or running multiple agents in parallel on different tasks. The iOS app is not a code editor on a phone — it is a control plane for agents running elsewhere.

Perhaps the most striking anecdote: at OpenAI, more than 95% of non-engineers use Codex rather than ChatGPT. This suggests that coding-style harnesses — structured interfaces with tool use, file access, and execution environments — are becoming the default way to interact with AI, even for people who don't write production code. If this pattern holds, the "AI chat" paradigm may be a transitional form, and the "AI agent with tools" paradigm is where the puck is heading.

The spend-per-token optimization trend is also significant. Coinbase's case study shows that when engineers are spending heavily on AI tokens, it becomes economically rational for platform teams to invest in per-token cost reduction — creating a new category of infrastructure work specifically around AI cost efficiency.