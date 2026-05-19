# GBrain — Garry Tan's Opinionated OpenClaw/Hermes Agent Brain
**Source**: https://github.com/garrytan/gbrain
**Date**: 2026-05
**Author**: Garry Tan (Y Combinator President & CEO)
**Keywords**: agent memory, knowledge graph, OpenClaw, Hermes, personal knowledge base, hybrid search, MCP, agent brain, PGLite, Y Combinator

## Elevator pitch
GBrain is a production-grade "brain" for AI agents built by Y Combinator's CEO, featuring a self-wiring knowledge graph, hybrid search, 43 curated skills, and a job queue — all running on embedded PGLite with zero server setup in 30 minutes.

## Takeaways
- Production deployment handles 17,888 pages, 4,383 people, 723 companies, and 21 autonomous cron jobs — built in 12 days
- Self-wiring knowledge graph extracts entity references from markdown and creates typed edges (attended, works_at, invested_in, founded, advises) with zero LLM calls
- Hybrid search combines vector (HNSW on pgvector), BM25 keyword, and reciprocal-rank fusion, achieving P@5 of 49.1% — a 31.4-point improvement over the graph-disabled variant
- ZeroEntropy embedding (2.2× faster, 2.6× cheaper than OpenAI) is the new default with 1,280-dimension Matryoshka embeddings
- Agent-driven brain health: `gbrain doctor --remediate --yes --target-score 90` runs a dependency-ordered remediation loop with cost caps

## Synthesis
Garry Tan built GBrain to solve a personal problem: his AI agents were smart but forgetful. The solution is a brain that runs on embedded PGLite (database ready in 2 seconds), uses no external servers, and can be installed in 30 minutes. It's what powers his OpenClaw and Hermes agent deployments in production, and it's now available as an open-source project.

The architecture centers on a self-wiring knowledge graph. Every page write extracts entity references from markdown, wikilinks, and typed-link syntax, then creates typed edges — attended, works_at, invested_in, founded, advises — with zero LLM calls. This graph is what produces the dramatic search quality improvement: a +31.4 point P@5 lift over vector-only RAG on a 240-page corpus. The graph enables multi-hop traversal, letting agents answer questions like "what did Bob invest in this quarter?" that vector search alone can't reach.

Under the hood, GBrain features a durable job queue (Minions) supporting LLM tool loops that survive crashes, shell jobs with audit trails, child jobs with cascading timeouts, and rate leases for outbound providers. The 43 curated skills cover signal capture, ingest, enrichment, querying, brain operations, citation fixing, daily task management, cron scheduling, and eval frameworks. The new ZeroEntropy embedding default delivers 2.2× faster and 2.6× cheaper embeddings than OpenAI while winning 11 of 20 queries head-to-head.

The `gbrain doctor` self-remediation feature is particularly notable: it computes a dependency-ordered plan (sync before extract, embed after consolidate), submits each step as a background job, and refuses to spend past a configurable cost cap. An agent can drive its own brain to 90/100 health score without human intervention. This is what production agent memory looks like: not a theoretical architecture but a working system handling thousands of entities, running autonomously, and getting smarter while you sleep.
