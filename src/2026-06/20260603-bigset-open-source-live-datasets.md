# BigSet: Open-Source Live Datasets from Text Prompts
**Source**: https://github.com/tinyfish-io/bigset
**Date**: 2026-06-03
**Author**: TinyFish
**Keywords**: BigSet, TinyFish, open source, live datasets, web scraping, AI agents, schema inference, auto-refresh, AGPL, data pipeline

## Elevator pitch
BigSet is an open-source tool from TinyFish that turns a natural language prompt into a structured, verified dataset pulled from the live web—with auto-refresh schedules to keep data current and CSV/XLSX export for immediate use.

## Takeaways
- Describe a dataset in one sentence and BigSet infers the schema, fans out AI agents to research in parallel, deduplicates, and returns a clean table with citations
- Auto-refresh schedules (30 min to weekly) keep datasets current—agents re-run on schedule, pulling fresh data automatically
- Schema inference from English: BigSet figures out column names, types, and primary keys without manual schema design
- Full stack open source: Next.js 16 frontend, Fastify backend, Mastra workflows for agent orchestration, powered by TinyFish's Search and Fetch APIs, AGPL-3.0 licensed
- Self-hosted via npm install in one command; 1.7K GitHub stars

## Synthesis
BigSet closes a gap in the web data tooling ecosystem. Existing tools—scraping frameworks, search APIs, pre-built actors, lead gen platforms—work well for what they do, but the moment you need something that cuts across categories or isn't covered by existing tools, you're back to square one: stitching together search, extraction, schema design, deduplication, verification, and a cron job to keep it fresh. For every dataset. Every time.

BigSet's approach is to collapse all of that into a single natural language prompt. You describe the dataset you want—"YC companies currently hiring engineers, with their funding stage, location, and number of open roles"—and BigSet infers the schema, sends an orchestrator agent to discover entities via web search, fans out sub-agents in parallel to investigate each entity, fetches real data, verifies it against real sources, deduplicates, and returns a structured table.

The architecture is a modern full-stack application. The frontend is Next.js 16 with Convex for real-time schema and functions. The backend is Fastify with Mastra for agent orchestration. TinyFish's Search and Fetch APIs power the web research. The system requires two API keys: TinyFish for web search and page fetching, and OpenRouter for LLM calls (schema inference and agent reasoning).

The roadmap points toward deeper agent integration: an agent-native API so AI agents can create, query, and consume BigSet datasets programmatically; SQL query support instead of just exporting; per-cell source provenance for traceability; healer agents that automatically detect and fix broken or stale rows; and incremental updates that refresh only what changed instead of rebuilding the whole dataset. The project is experimental but already useful, with 1.7K GitHub stars and active development.