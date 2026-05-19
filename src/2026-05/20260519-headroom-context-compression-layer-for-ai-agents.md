# Headroom — Context Compression Layer for AI Agents
**Source**: https://github.com/chopratejas/headroom
**Date**: 2026-05
**Author**: chopratejas (Tejas Chopra)
**Keywords**: context compression, token savings, AI agents, LLM optimization, agent tools, MCP, reversible compression, context window

## Elevator pitch
Headroom compresses tool outputs, logs, files, and RAG chunks before they reach the LLM, achieving 60-95% token savings with preserved accuracy across standard benchmarks, available as a library, proxy, MCP server, or agent wrapper.

## Takeaways
- Achieves 92% token reduction on code search and SRE debugging workloads, 73% on GitHub issue triage, with zero accuracy loss on GSM8K, TruthfulQA, SQuAD v2, and BFCL benchmarks
- ContentRouter detects content types and routes to the right compressor: SmartCrusher for JSON, CodeCompressor (AST-aware) for code, Kompress-base for prose
- Reversible compression (CCR) stores originals locally; the LLM can retrieve them on demand via `headroom_retrieve`, so nothing is permanently lost
- Works as a drop-in proxy (zero code changes), library (Python/TypeScript), agent wrapper (`headroom wrap claude`), or MCP server
- Cross-agent shared memory with auto-dedup and `headroom learn` that mines failed sessions and writes corrections to CLAUDE.md/AGENTS.md

## Synthesis
The economics of AI agents increasingly hinge on context window costs. Every tool output, every log line, every RAG result burns tokens — and those tokens add up fast at scale. Headroom tackles this problem directly by sitting between agents and LLM providers, compressing everything the agent reads before it reaches the model.

The compression is content-aware. The ContentRouter detects whether input is JSON, code, or prose and routes to specialized compressors: SmartCrusher handles structured JSON by collapsing arrays of similar dicts and removing redundant fields; CodeCompressor uses AST-aware compression across Python, JS, Go, Rust, Java, and C++; Kompress-base is a custom HuggingFace model trained specifically for prose compression. Together they achieve dramatic savings — 92% on code search workloads, 92% on SRE debugging, 73% on GitHub issue triage — without degrading accuracy on standard benchmarks.

The reversible compression feature (CCR) addresses the anxiety of lost information: originals are stored locally and the LLM receives a `headroom_retrieve` tool it can call when it needs the full content. This means compression is safe to apply aggressively. The agent wrapper mode (`headroom wrap claude|cursor|codex`) makes adoption trivial — a single command wraps an existing agent setup with compression. The cross-agent shared memory and `headroom learn` feature add another dimension: the system learns from failed sessions and writes improvements back to agent configuration files.

With 60B+ tokens saved by the community and integration support for virtually every major agent framework (Claude Code, Codex, Cursor, Aider, OpenClaw, LangChain, Agno, Vercel AI SDK), Headroom represents a pragmatic layer in the growing agent infrastructure stack — one that directly addresses the cost problem that will only intensify as agents run longer and do more.
