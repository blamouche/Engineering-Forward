# LLM Wiki v2 — Extending Karpathy's LLM Wiki Pattern with Lessons from Building Agent Memory
**Source**: https://gist.github.com/kanmadigital/2369c4f5ea410cb8f6a1647b40c0e2a1
**Date**: 2026-05-16
**Author**: kanmadigital (forked from rohitg00)
**Keywords**: LLM wiki, knowledge management, agent memory, Karpathy, knowledge graphs, memory lifecycle, RAG, personal knowledge base

## Elevator pitch
A production-hardened extension of Karpathy's LLM Wiki concept, adding memory lifecycle management, typed knowledge graphs, hybrid search, automation hooks, and multi-agent collaboration — turning the wiki from a flat collection of claims into a living, self-maintaining knowledge base.

## Takeaways
- The original LLM Wiki pattern (raw sources → wiki pages → schema) works but lacks lifecycle management: knowledge needs confidence scoring, supersession, retention decay, and consolidation tiers
- A typed knowledge graph layered on wiki pages — with entities, typed relationships, and graph traversal for queries — surfaces connections that keyword search misses
- Hybrid search combining BM25, vector search, and graph traversal beats any single approach, especially beyond ~100 pages
- Automation via hooks (auto-ingest on new source, auto-consolidation on session end) eliminates the bookkeeping that makes people abandon wikis
- The schema document (CLAUDE.md, AGENTS.md) is the most important file — it turns a generic LLM into a disciplined knowledge worker and is co-evolved over time

## Synthesis
This gist builds on Andrej Karpathy's original LLM Wiki idea — using LLMs as librarians that compile knowledge instead of constantly re-deriving it — with hard-won lessons from building agentmemory, a persistent memory engine for AI agents. The core insight remains correct: RAG retrieves and forgets; a wiki accumulates and compounds. But production use reveals gaps the original didn't anticipate.

The biggest missing piece is memory lifecycle. The original treats all wiki content as equally valid forever, but in practice knowledge decays, strengthens with reinforcement, and needs supersession when contradicted. The authors propose confidence scoring (every fact carries a score based on source count, recency, and contradictions), retention curves based on Ebbinghaus's forgetting curve, and a four-tier consolidation pipeline: working memory → episodic memory → semantic memory → procedural memory. Each tier is more compressed, confident, and long-lived than the one below.

Beyond flat pages, the gist advocates for a typed knowledge graph with entity extraction and typed relationships (uses, depends on, contradicts, caused, fixed, supersedes). When querying "what's the impact of upgrading Redis?", the system walks the graph outward through dependency edges rather than relying on keyword matching. Search scales through hybrid approaches combining BM25, vector search, and graph traversal fused with reciprocal rank fusion.

The automation layer is where the pattern becomes sustainable. Hooks fire on new sources, session starts, session ends, queries, memory writes, and schedules — handling the bookkeeping that makes people abandon wikis. Quality scoring, self-healing lint operations, and contradiction resolution keep the knowledge base healthy. The authors provide an implementation spectrum from minimal viable wiki to full collaboration with mesh sync across multiple agents, making the pattern adoptable at any scale. The Memex, they argue, is finally buildable — not because of better documents or search, but because we have librarians that actually do the work.
