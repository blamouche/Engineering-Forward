# OpenAI Codex Harness as an API
**Source**: https://openai.com/index/introducing-the-agents-api/
**Date**: 2026-09-11
**Author**: Unwind AI
**Keywords**: OpenAI, Agents API, Codex, Sakana AI, Fugu, Edge0, model routing, edge inference, MoE, AI agent infrastructure

## Elevator pitch
OpenAI launches the Agents API — the same managed harness behind Codex — as a public beta, enabling developers to spin up agents with compute environments, tools, and subagents in a single API call; plus Sakana AI's cheaper-model routing, Edge0's on-device 35B inference, and more AI infrastructure news.

## Takeaways
- OpenAI's Agents API bundles the Codex harness into a single call: managed compute environment, files, tools, MCP servers, up to 3 concurrent subagents, cross-context-window persistence, and automatic context compaction
- The API is in public beta with no platform fee — you pay only for models and tools used
- Sakana AI launched Fugu Max and Fugu Ultra v2, routing work across swappable model pools instead of using the largest model for every task; Fugu Max approaches elite-model performance at 2-6x lower cost
- Edge0 runs a 35B sparse mixture-of-experts model on Apple Silicon by streaming weights from SSD instead of loading everything into RAM: 23 GB on disk, ~2.9 GB active memory, 14.9-17.7 tokens/sec on M4 Pro
- The newsletter also covers Databricks' DBRX 3 open model, Google's Gemini 2.5 Flash-Lite, and Microsoft's AutoGen 0.4 framework update

## Synthesis
The headline story is OpenAI productizing the infrastructure behind Codex into a standalone API. This is significant because it removes the most expensive engineering work from agent-building: the harness, sandboxing, context management, tool routing, and subagent coordination. By offering it with no platform fee (revenue comes from model and tool usage), OpenAI is positioning itself as the default substrate for agentic applications, much as AWS became the default for web services.

Sakana AI's Fugu approach challenges the frontier-model orthodoxy. Instead of throwing the largest model at every problem, Fugu routes work across a pool of cheaper open and specialized models, achieving near-elite performance at a fraction of the cost. Fugu Ultra v2 reportedly beats Opus 5 and Fable 5 on Sakana's Chartography benchmark — though the benchmark's independence is worth questioning. The broader point stands: for many production workloads, model routing across cheaper models may deliver better cost-to-performance than defaulting to a single frontier model.

Edge0's on-device inference is the most technically interesting development. By treating the SSD as extended memory and streaming weights on demand, a 35B parameter model runs on consumer Apple Silicon with under 3 GB of active RAM. The sparse mixture-of-experts architecture means only a subset of parameters is active per token, making this streaming approach viable. At ~15-17 tokens/sec on an M4 Pro, it's not fast enough for real-time chat but is sufficient for background agentic workloads — and it runs entirely offline, which matters for privacy-sensitive and air-gapped use cases.