# Forge: A Python framework for self-hosted LLM tool-calling and multi-step agentic workflows
**Source**: https://github.com/antoinezambelli/forge
**Date**: May 27, 2026
**Author**: Antoine Zambelli
**Keywords**: LLM, tool-calling, guardrails, self-hosted, local models, agentic workflows, Python, open source, reliability, proxy

## Elevator pitch
Forge is a Python reliability layer for self-hosted LLM tool-calling that lifts an 8B local model from single-digit accuracy to 84% on its 26-scenario eval suite, and boosts Sonnet 4.6 from 85% to 98% — available as a drop-in proxy, WorkflowRunner, or composable middleware.

## Takeaways
- Forge dramatically improves local model reliability: an 8B model goes from single-digit performance to 84% accuracy on structured tool-calling tasks.
- Even frontier models benefit: Sonnet 4.6 improves from 85% to 98% on the same evaluation suite.
- Three usage modes: HTTP proxy (drop-in between any client and model server), WorkflowRunner (full lifecycle management), and composable middleware (use inside your own orchestration loop).
- Supports multiple backends: Ollama, llama.cpp (llama-server), Llamafile, vLLM, and Anthropic API.
- Open-source (MIT), Python 3.12+, with active development including structured workflows (required steps, prerequisites, terminal tools), context compaction, and priority-queued multi-agent slot sharing.

## Synthesis
Antoine Zambelli's Forge addresses a critical gap in the local LLM ecosystem: tool-calling reliability. While frontier models handle structured tool calls reasonably well out of the box, self-hosted models (8B parameters and below) typically fail catastrophically — Forge's eval shows single-digit accuracy without guardrails. The framework applies rescue parsing (handling malformed JSON), retry nudges (guiding the model toward correct formats), and response validation to close this gap, achieving 84% on 8B models.

The proxy server mode is the most accessible entry point: it speaks both OpenAI chat-completions and Anthropic Messages APIs, sitting transparently between any client (opencode, Continue, aider, Cline, Claude Code) and a local model server. Clients see a smarter model without any code changes. The WorkflowRunner mode provides full lifecycle management for structured agent loops — system prompts, tool execution, context compaction, and guardrails. An interesting addition is SlotWorker, which enables priority-queued access to a shared inference slot with auto-preemption, designed for multi-agent architectures where specialist workflows share a single GPU.

Forge's composable middleware approach means you can use its reliability stack inside your own orchestration loop, keeping full control while benefiting from response validation and tool-call rescue. The project supports the major local inference backends (Ollama, llama.cpp, vLLM) plus Anthropic's cloud API, making it applicable across the spectrum from fully local to hybrid deployments. The evaluation transparency — publishing v0.6.0 and v0.7.0 results including a configurable eval rig — sets a high bar for empirical validation in the tool-calling space.
