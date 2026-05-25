# EP216: RAGs vs Agents
**Source**: https://blog.bytebytego.com/p/ep216-rags-vs-agents
**Date**: May 23, 2026
**Author**: ByteByteGo
**Keywords**: RAG, agents, Claude Code, context management, proxy patterns, API gateway, system design

## Elevator pitch
ByteByteGo's EP216 breaks down the architectural choice between RAG (retrieval-augmented generation) and agent-based AI systems, alongside deep dives into proxy patterns, Claude Code's request lifecycle, and context management strategies for long-running agent sessions.

## Takeaways
- RAG (one retrieval, one generation) is cheap, predictable, and easy to debug — use it when answers live in your documents
- Agents wrap LLMs in a reasoning loop with tools, trading flexibility and action capability for more tokens and harder debugging
- Forward proxy represents the client, reverse proxy represents the server, API gateway layers auth/rate limiting across microservices
- Claude Code's request lifecycle reveals 8 steps from prompt to tool result streaming, with permissions gating every action
- Long sessions use 5-layer lazy degradation: budget reduction → snip → microcompact → context collapse → auto-compact

## Synthesis
ByteByteGo's latest system design refresher tackles the fundamental architectural decision between RAG and agent-based AI systems. RAG follows a simple pipeline: embed the query, retrieve relevant chunks from a knowledge base, paste them into the prompt as context, and generate a grounded answer. It's deterministic and cost-efficient — but limited to answering questions from existing documents.

Agents, by contrast, wrap an LLM in a reasoning loop. The model reads a goal, picks a tool (Read, Write, Edit, Bash, etc.), the runtime executes it and feeds the result back, and the cycle repeats until task completion. This flexibility comes at a cost — more tokens consumed, and errors that drift and compound across multiple reasoning steps, making debugging significantly harder.

The newsletter also unpacks Claude Code's internal architecture through a trace of a single request ("Fix the failing test in auth.test.ts"). The 8-step pipeline shows how context is bundled, actions pass through a permission gate, approved tool calls execute as real syscalls, and the agent loop persists state before streaming results. This architecture explains why building a reliable coding agent is non-trivial — the permission system, tool execution environment, and state persistence must all be bulletproof.

For session management, Claude Code employs five context strategies applied lazily: budget reduction caps oversized tool outputs, snip trims oldest history segments, microcompact prunes tool turns by ID to keep the cache warm, context collapse does a read-time projection, and auto-compact — the last resort — calls the model itself to summarize prior turns. Each only activates if the cheaper layer fails to free enough room.

The proxy refresher adds practical clarity: forward proxies represent clients for outbound filtering, reverse proxies represent servers for TLS termination and load balancing, and API gateways add auth, rate limiting, and request shaping when multiple microservices need consistent policies.
