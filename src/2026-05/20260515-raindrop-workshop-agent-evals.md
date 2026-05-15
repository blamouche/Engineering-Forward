# Raindrop Workshop: Give your coding agent the power to write and run agent evals
**Source**: https://github.com/raindrop-ai/workshop
**Date**: May 15, 2026
**Author**: Raindrop AI
**Keywords**: agent observability, coding agents, evals, tracing, Claude Code, debugging, LLM monitoring

## Elevator pitch
Raindrop Workshop is an open-source local debugger that gives coding agents like Claude Code the ability to read their own traces, write evals against a codebase, and self-heal through an automated eval loop — all streaming live to a local UI.

## Takeaways
- Live-streamed traces show every token, tool call, and decision as it happens — no polling or refreshing
- Claude Code integration enables a self-healing eval loop: Claude writes the eval, runs the agent, sees failures, fixes code, and re-runs until assertions pass
- Compatible with major SDKs (Vercel AI SDK, OpenAI Agents SDK, Anthropic SDK, LangChain, CrewAI, etc.) and coding agents (Claude Code, Codex, Devin, Cursor)
- Local replay feature scaffolds HTTP endpoints that replay production traces against real agent code
- Single-command install via curl, MIT licensed, 399 GitHub stars

## Synthesis
Raindrop Workshop addresses a critical gap in the agent development workflow: the ability to observe and evaluate agent behavior locally. As coding agents become more autonomous, the feedback loop between writing code and verifying it works becomes the bottleneck. Workshop's core insight is that agent traces are the richest source of truth about agent behavior — and giving agents access to their own traces creates a powerful self-improvement cycle.

The self-healing eval loop is the standout feature. Rather than developers manually writing tests for agent behavior, Claude Code reads trace data, programmatically generates evals, runs the agent against those evals, identifies failures, fixes the underlying code, and re-runs until all assertions pass. This closes the loop on agent quality in a way that scales beyond manual review.

Compatibility is broad: Workshop integrates with dozens of SDKs and agent frameworks across TypeScript, Python, Go, and Rust, plus all major cloud providers (AWS Bedrock, Azure, Vertex AI). The local-first architecture (SQLite database, single binary) means no cloud dependency for debugging sensitive agent workflows.

At 399 stars and in active development (v0.1.6 as of May 2026), Workshop represents the emerging category of "agent developer tools" — infrastructure built specifically for the agent development lifecycle rather than repurposed from traditional software development.
