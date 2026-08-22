# How OpenAI Built Its Data Agent
**Source**: https://blog.bytebytego.com/p/how-openai-built-its-data-agent
**Date**: 2026-06-03
**Author**: ByteByteGo (interview with Emma Tang, Head of Data Platform Engineering at OpenAI)
**Keywords**: OpenAI, data agent, GPT-5.5, context assembly, vanilla architecture, Codex, MCP, data platform, embeddings, retrieval

## Elevator pitch
OpenAI's data platform team built a deliberately "vanilla" agent that reliably answers questions across 90,000 tables and 1.5 exabytes—proving that at scale, the engineering around context assembly matters far more than agent complexity.

## Takeaways
- The data agent uses a single LLM (GPT-5.5), a context assembly layer, 13 curated tools, and an agent runtime—no router, no fine-tuning, no special post-training
- Six layers of context (table usage metadata, human annotations, Codex enrichment, institutional knowledge, memory, runtime context) turn a single model into a reliable analyst across 90,000 tables
- A nightly Codex job crawls pipeline code to enrich table descriptions, capturing what each table actually contains and how it's derived
- The team initially connected ~40 tools but results were bad—the model picked wrong tools and got confused by overlapping capabilities; capping at 13 with no overlap fixed it
- OpenAI used Codex internally to migrate 10,000 DAGs and 90,000 tables between clouds in two months—a migration that takes years at other companies

## Synthesis
OpenAI's data platform stores 1.5 exabytes across 90,000 datasets and serves approximately 4,000 internal users as of May 2026. The hardest part of data analysis at this scale isn't writing SQL—it's finding the right tables and understanding semantically how to use them. Many tables look similar but mean different things. Analysts can spend hours figuring out which tables to use before writing a single line of code.

The data agent's architecture is intentionally simple: a single LLM (GPT-5.5), a context assembly layer, a curated set of 13 tools, and an agent runtime. The team found that a simple architecture works well at their scale because the reliability comes from the engineering around the model, not the model itself. The real engineering work lives in context assembly—building the right foundation before any user asks a question.

The context assembly relies on six layers. Table usage metadata provides schema, lineage, and query history, with queries from popular dashboards ranking highest. Human annotations capture business meaning and caveats. A nightly Codex enrichment job reads the pipeline code that produces each table, capturing what it contains and how it's derived. Institutional knowledge from Slack, Google Docs, and Notion is ingested and embedded through an access-controlled retrieval service. Memory holds corrections from prior conversations. Runtime context fills gaps when offline descriptions are stale.

The team shared five key lessons. First, the data foundation matters more than the agent—if data is scattered or inconsistent, the agent is not the first investment. Second, fewer tools beat more tools—the model is better at reasoning than at choosing between near-duplicate tools. Third, trusted queries should be used for retrieval—queries behind heavily used dashboards rank highest because they tend to be correct and reusable. Fourth, guide the goal, not the path—prescriptive step-by-step instructions produced worse answers than high-level guidance. Fifth, be more ambitious—timeline estimates from before Codex no longer apply.

Looking ahead, OpenAI plans to generate custom React apps per question instead of fixed dashboard widgets, and is building platform-side agents to triage and validate the deluge of AI-generated code hitting shared infrastructure.