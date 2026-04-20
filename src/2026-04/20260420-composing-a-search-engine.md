# Composing a Search Engine

**Source**: https://exa.ai/blog/composing-a-search-engine
**Date**: Unknown
**Author**: Exa Labs
**Keywords**: ai search engine, web search api, webcrawler, serp api, web api

## Elevator pitch
A canon, in music, is one voice stating a melody and others entering later to overlap and transform it into harmony.

## Takeaways
- A canon, in music, is one voice stating a melody and others entering later to overlap and transform it into harmony
- A search engine orchestrator is a canon: independent nodes kick off when they're ready, follow the same rules, and combine into one result
- A node only runs when a downstream consumer asks for its value, as opposed to a push model where every node fires as soon as its inputs are ready
- Laziness and cancellation propagation fall out of this for free
- Two nodes share an upstream ancestor through different paths, forming a diamond shape in the graph

## Synthesis
A canon, in music, is one voice stating a melody and others entering later to overlap and transform it into harmony. A search engine orchestrator is a canon: independent nodes kick off when they're ready, follow the same rules, and combine into one result. A node only runs when a downstream consumer asks for its value, as opposed to a push model where every node fires as soon as its inputs are ready. Laziness and cancellation propagation fall out of this for free. Two nodes share an upstream ancestor through different paths, forming a diamond shape in the graph. Without memoization the ancestor would be recomputed once per path; caching its output ensures it runs exactly once per request. Typestate: a type-system technique where types encode an object's current state alongside its shape, so operations illegal in that state become compile errors instead of runtime bugs. A total function is defined for every input in its domain. Canon extends this to graphs: every node must handle every outcome it can produce, and the type checker rejects any graph with a missing branch. Query an inverted index, rank the results, then serve. Well what if some users want results in Japanese? Add a freshness model that decides what to serve. Queries hit a knowledge graph, product index or both? Some customers have specific requirements that don't make sense on every request? In practice, every customer has a unique search path that needs to be accommodated. Suddenly search isn't so easy: a simple request looks closer to a graph of 20+ node types with many branches. The challenges are even greater when serving thousands of different AI agents, each with their own needs. This complexity is increased by the reality that most code is now written by agents: even if agents write locally correct code, reasoning through global constraints and requirements remains hard for them. Billions of search requests are made on Exa - how do we monitor the decisions made within each request? How do we ensure our search pipelines are robust as most code is written by agents? How do we build observability over a search engine? To answer those questions, we built Canon 1 1 A canon, in music, is one voice stating a melody and others entering later to overlap and transform it into harmony. A search engine orchestrator is a canon: independent nodes kick off when they're ready, follow the same rules, and combine into one result. - a search pipeline orchestrator that is our solution to ensure full control over our search engine as it scales in complexity.
