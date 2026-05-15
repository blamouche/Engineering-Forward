# Agentic Search Models
**Source**: https://softwaredoug.com/blog/2026/05/11/the-new-agentic-search-models.html
**Date**: 2026-05-11
**Author**: Doug Turnbull
**Keywords**: agentic search, LLM, retrieval, search models, RAG, SID-1, Waldo, embeddings, rerankers, domain-specific AI

## Elevator pitch
Agentic search models—LLMs trained specifically to orchestrate search tasks—are emerging as a new paradigm that replaces monolithic, hand-built retrieval pipelines with intelligent models that can manage the entire search process, especially for domain-specific "last 20%" relevance tuning.

## Takeaways
- Traditional search stacks are monolithic, manual, and bespoke, with each component (embeddings, rerankers, query classifiers) seeing only its part of the problem
- Agentic search unbundles the stack by letting a single model orchestrate simple retrieval primitives, seeing the whole process end-to-end
- Frontier models like GPT-5 handle web search well but struggle with domain-specific nuances (e.g., "bistro tables" meaning "small outdoor tables" in a furniture store)
- New specialized models like SID-1, Glean's Waldo, and Charcoal are being trained specifically on document search for targeted domains
- Embedding models proliferated across domains (financial, legal, e-commerce); agentic search models will likely follow the same trajectory

## Synthesis

Doug Turnbull's piece marks a significant inflection point in how the search community thinks about information retrieval architecture. For two decades, search engineers have built thick, monolithic pipelines: query understanding feeds into business rules, which route to multiple retrieval backends, followed by post-processing and reranking. Each component solves its narrow slice of the problem in isolation. The reranker doesn't understand the query classifier's intent mappings; the embedding model doesn't know about business rules that override certain results.

Agentic search proposes something fundamentally different. Instead of a rigid pipeline of disconnected components, a single intelligent model—trained specifically on search—orchestrates thin, simple retrieval primitives. The model has tools: keyword search, embedding-based retrieval, filters. It reasons about which to use, when to combine them, and how to interpret results for the user's actual need.

The key insight is about the "last 20%." Frontier models like GPT-5 and Claude Sonnet handle the generic 80% of search queries competently—they understand natural language, they know common facts, they can surface reasonable results from a clean web search index. But enterprise and domain-specific search lives in that last 20%: the furniture retailer who knows "bistro tables" means small outdoor tables, not restaurant equipment; the fashion site where users consistently prefer dark, plain patterns over complex ones; the legal database where specific citation formats matter more than semantic similarity.

Turnbull points to a growing ecosystem of models purpose-built for this challenge. SID.ai released SID-1, Glean launched Waldo, and startups like Charcoal are training models tailored to specific corpora. These models are smaller, faster, and cheaper to deploy than GPT-5, while outperforming it on domain-specific search tasks. They know the domain, understand the users, and can orchestrate simpler retrieval backends effectively.

This mirrors the trajectory of embedding models, which have proliferated across domains—financial embeddings, legal embeddings, e-commerce embeddings on HuggingFace. Turnbull argues agentic search models will follow the same path: a family of domain-tuned models replacing the heavy engineering work of building and maintaining complex search pipelines.

The implications for search infrastructure are substantial. If agentic search models become the norm, teams won't need to build elaborate query classifiers, intent detectors, and multi-stage reranking cascades. They'll maintain simple, scalable retrieval backends—a keyword index, an embedding store—and let the agentic model handle the intelligence layer. Query understanding, hybrid search strategy, and result selection become model capabilities rather than engineering artifacts.

Turnbull is realistic about current limitations—these models are still too slow to drive real-time site search today—but he's confident the economics will shift rapidly. The future of search isn't thicker pipelines; it's smarter models that orchestrate simpler tools. For search engineers, the skill set shifts from pipeline architecture to model selection, domain tuning, and retrieval tool design. It's a vision where the lego pieces still matter, but a single intelligent model finally sees how they fit together.
