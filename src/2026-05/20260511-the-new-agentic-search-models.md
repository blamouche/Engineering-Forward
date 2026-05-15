# Agentic search models
**Source**: https://softwaredoug.com/blog/2026/05/11/the-new-agentic-search-models.html
**Date**: 2026-05-11
**Author**: Doug Turnbull
**Keywords**: agentic search, LLM, search infrastructure, SID-1, Glean Waldo, retrieval, RAG, embeddings, reranking, query understanding, domain-specific models

## Elevator pitch
A new class of domain-specific "agentic search models"—LLMs trained specifically to orchestrate search tasks rather than general-purpose models like GPT-5—promises to replace the traditional thick, monolithic retrieval stack with simpler retrieval primitives orchestrated by intelligent, search-aware agents.

## Takeaways
- Traditional search stacks are "thick monoliths" where each component (query classifiers, rerankers, embeddings) operates in isolation, ignorant of the whole problem
- General-purpose models like GPT-5 handle 80% of search cases well but stumble on the last 20%: domain-specific nuances, user preferences, and non-obvious relevance patterns
- New agentic search models (SID-1, Glean's Waldo, Charcoal) are trained specifically on search tasks and can be smaller, faster, and cheaper than frontier models
- These models unbundle the retrieval stack by controlling simpler primitives—basic keyword search, embedding retrieval with filters—through an intelligent orchestrator that sees the entire process
- The future likely includes a family of domain-specific agentic search models, similar to how HuggingFace today hosts hundreds of domain-tuned embedding models for legal, financial, and e-commerce use cases

## Synthesis
Doug Turnbull, a search infrastructure consultant and educator, sketches a compelling vision for the next evolution of search architecture. His central thesis is that the traditional search stack—built up over one to two decades—has become a "thick monolith" of specialized components that each address narrow parts of the retrieval problem but never see the whole picture. Query classifiers don't know what the reranker is doing. The reranker doesn't understand the embedding model's biases. Each piece optimizes locally without global awareness.

The first wave of AI in search brought general-purpose models like GPT-5 into the loop. These work well for the 80% case—they have broad world knowledge and can surface defensible results. But Turnbull argues that the last 20% is where competitive differentiation lives. GPT-5 doesn't know that in your furniture catalog, "bistro tables" means "small outdoor tables," not restaurant equipment. It doesn't know your fashion shoppers prefer dark patterns over complex ones. And critically, GPT-5 was trained on web search, where retrieval tools work near-flawlessly—it struggles when orchestrating the simpler, messier search backends that most product teams actually operate.

The solution emerging in 2026 is agentic search models: LLMs trained specifically on the search task, often tuned to particular domains. SID-1 from SID.ai was the first notable example, followed by Glean's Waldo and startups like Charcoal that tailor models to specific corpora. These models are smaller, faster, and cheaper to run than GPT-5 while delivering better results on their target domain because they understand the retrieval primitives they're orchestrating and the domain-specific relevance patterns that matter.

The architectural implication is radical: instead of building ever-more-complex query and reranking pipelines, teams could deploy simple retrieval primitives—basic keyword search, embedding models with a few filters—and let an agentic search model orchestrate them intelligently. The model handles query understanding, hybrid search strategy, and result synthesis as a unified process rather than a series of reductive, hand-coded steps.

Turnbull draws a parallel to the embedding model ecosystem: HuggingFace today hosts scores of domain-specific embedding models for finance, legal, e-commerce, and more. He predicts a similar proliferation of domain-tuned agentic search models. While current models are too slow for real-time site search, the trajectory is clear—and for teams building search experiences, the future will look radically different than the pipeline architectures that have dominated the past two decades.
