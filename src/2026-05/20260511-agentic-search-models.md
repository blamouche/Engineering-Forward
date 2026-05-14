# Agentic Search Models
**Source**: https://softwaredoug.com/blog/2026/05/11/the-new-agentic-search-models.html
**Date**: 2026-05-11
**Author**: Doug Turnbull
**Keywords**: agentic search, LLMs, retrieval, search infrastructure, embeddings, SID-1, Waldo, domain-specific models, RAG

## Elevator pitch
A new class of smaller, domain-trained "agentic search models" is emerging to replace monolithic retrieval pipelines with intelligent orchestration of simpler search primitives.

## Takeaways
- Traditional search stacks are monolithic, manual, and bespoke—each component (rerankers, query classifiers) sees only its piece
- Frontier models like GPT-5 handle 80% of search well but lack domain-specific knowledge for the critical last 20%
- New models like SID-1 (SID), Waldo (Glean), and Charcoal are purpose-built for search, offering smaller size and lower latency
- Agentic search unbundles retrieval stacks: the agent orchestrates simple primitives (keyword search, embeddings, filters) to solve queries holistically
- The future will likely mirror the embedding model ecosystem—scores of domain-specific agentic search models for e-commerce, legal, finance, and more

## Synthesis
Doug Turnbull, an experienced search engineer and consultant, articulates a fundamental shift in how search systems are being architected. For 1-2 decades, the industry has built thick, monolithic search stacks: queries flow through business rules, query classifiers, multiple retrieval backends, post-processing, and reranking—each piece optimized in isolation, none seeing the whole picture. This architecture is inherently manual, programmatic, and bespoke to each deployment.

The emergence of agentic search models represents a paradigm change. Instead of a monolithic pipeline, an LLM-based agent is given tools (simple retrieval primitives wrapped around backend indices), knowledge, and context to orchestrate a solution. The agent sees the entire process, unbundling the traditional stack while the underlying components become thinner and simpler.

Turnbull identifies a crucial limitation of frontier models for search: while GPT-5 and similar models perform well on 80% of queries, the last 20% is where competitive advantage lives and where these models fail. A generalist model doesn't know that "bistro tables" means "small outdoor tables" in a furniture domain, or that fashion users prefer dark, plain patterns. These models are trained on web search expectations—near-flawless retrieval tools—but real-world teams work with simpler, domain-specific backends that require different reasoning.

The solution emerging is domain-specialized agentic search models. SID released SID-1, Glean released Waldo, and startups like Charcoal tailor models to specific corpora—all advertising smaller size and lower latency compared to GPT-5. These models are trained on document search specifically, focusing on that critical last 20% of relevance. Turnbull draws an analogy to the current embedding model ecosystem on Hugging Face, which has scores of domain-specific models for legal, financial, and e-commerce. He predicts agentic search models will proliferate similarly across domains. While current models are too slow for real-time site search, this will change. The implications are significant: search teams may shift from building complex pipelines to deploying simpler retrieval primitives orchestrated by intelligent, domain-aware agents—a radically different search future.
