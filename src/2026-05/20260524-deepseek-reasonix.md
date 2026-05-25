# Reasonix — DeepSeek-native AI coding agent for your terminal
**Source**: https://esengine.github.io/DeepSeek-Reasonix/
**Date**: May 24, 2026
**Author**: esengine (community project)
**Keywords**: DeepSeek, Reasonix, coding agent, terminal, prefix cache, CLI, TypeScript, open source, AI coding

## Elevator pitch
Reasonix is an open-source, DeepSeek-native terminal coding agent engineered around prefix-cache stability to keep token costs low across long sessions, rapidly gaining traction on Hacker News with 6,300+ GitHub stars.

## Takeaways
- Reasonix is a TypeScript-based coding agent specifically optimized for DeepSeek's API, focusing on maximizing prefix-cache hit rates that other agent harnesses often degrade below 20%.
- The project argues that most agent loops reorder, rewrite, or inject fresh timestamps each turn, destroying cache stability — a claim that sparked debate on Hacker News.
- It reached 6,349 GitHub stars and significant community interest, with v0.30.4 as the latest release and active development.
- Hacker News discussion highlighted that DeepSeek's aggressive pricing combined with cache-optimized tooling creates a compelling cost advantage: users report 95%+ cache hit rates (39M cached tokens vs 1.7M uncached).
- Skeptics on HN questioned whether the cache-degradation claims are overstated, noting that tools like OpenCode also achieve high cache hit rates with DeepSeek's API without specialized optimization.

## Synthesis
Reasonix represents an interesting development in the AI coding agent landscape: a tool built from the ground up around a single provider's API characteristics rather than trying to be model-agnostic. The project, developed by the esengine collective, is a TypeScript-based terminal coding agent that treats DeepSeek's prefix-cache behavior as a first-order design constraint.

The core architectural argument is that DeepSeek's automatic prefix caching — which can dramatically reduce token costs when consecutive requests share identical prefixes — is systematically undermined by how most agent harnesses construct their prompts. The Reasonix team claims typical cache hit rates fall below 20% in practice because agent loops reorder messages, rewrite content, or inject fresh timestamps into the prompt prefix. By carefully controlling message construction to preserve byte-level prefix stability, Reasonix aims to keep cache hit rates high across long coding sessions.

The Hacker News discussion revealed both enthusiasm and skepticism. On the enthusiastic side, users report achieving 95%+ cache hit rates with DeepSeek V4 Pro, with cached tokens dwarfing uncached ones (e.g., 39M cached vs 1.7M uncached in a session). Combined with DeepSeek's recent permanent 75% price cut, this creates a cost proposition an order of magnitude cheaper than frontier Western models. One commenter noted they built a simple bridge to use DeepSeek via Codex and got excellent cache rates without any special optimization, suggesting the cache stability problem may be less severe than Reasonix claims.

Skeptics on HN questioned whether the degradation claims are grounded or "AI slop" — arguing that most well-known harnesses (Codex, Kimi-CLI, OpenCode) don't exhibit the described behavior, and that examining actual source code would verify this. The OpenCode maintainers have discussed cache behavior extensively, noting that tool call pruning can sometimes improve cache hit rates and reduce spend by 30% depending on the provider.

Regardless of the technical debate's resolution, Reasonix's rapid traction (6,300+ stars, active Discord community, frequent releases) signals strong demand for tools that maximize the cost advantage of DeepSeek's aggressively priced models. It also highlights how provider-specific optimizations are becoming a meaningful differentiator in the coding agent space, as the gap between different models' API economics widens.
