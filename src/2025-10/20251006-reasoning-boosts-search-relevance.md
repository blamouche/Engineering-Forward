# Reasoning boosts search relevance 15-30%
**Source**: https://softwaredoug.com/blog/2025/10/06/how-much-does-reasoning-improve-search-quality
**Date**: 2025-10-06
**Author**: Doug Turnbull
**Keywords**: agentic search, reasoning agents, BM25, search relevance, LLM tools, structured outputs, information retrieval

## Elevator pitch
An experimental study demonstrating that AI agents using simple search tools achieve 15-30% better relevance than baseline BM25 methods by iteratively reasoning through query reformulation.

## Takeaways
- Measurable improvement confirmed: Agent-driven search outperformed baseline BM25 on two datasets (WANDS: 0.56 to 0.64; ESCI: 0.30 to 0.39 NDCG scores).
- Simple tools enable reasoning: The agent succeeds not from complex search systems but from transparent, understandable search mechanics that allow iteration and learning.
- Three critical components: Success requires thoughtful prompting with examples, a clearly-documented search tool with known limitations, and structured output schemas forcing explicit reasoning.
- Structured outputs matter: Requiring the agent to explain user intent and search plans forces deeper consideration of relevance compared to unstructured responses.
- Production applicability uncertain: While experiments show promise, questions remain about scalability, tool memory effects, and whether agent reasoning can transfer to non-agentic systems.

## Synthesis
Turnbull's research challenges conventional wisdom about search system design. Rather than building increasingly sophisticated ranking algorithms, he demonstrates that "agentic search" pairs basic lexical search with reasoning capabilities, enabling iterative improvement through agent-driven query reformulation.

The experimental methodology compares a naive BM25 baseline against the same underlying search mechanism controlled by a reasoning agent (GPT-4). On two e-commerce datasets, the agent consistently outperformed the baseline by 8-9 points in normalized discounted cumulative gain—a substantial improvement from architecture alone.

The mechanism operates through a feedback loop: the agent receives the user query, accesses a documented search tool with explicit limitations, makes tool calls, evaluates results, and refines subsequent searches based on reasoning about user intent. The system explicitly tells the agent it lacks "synonyms, compounding, decompounding, query understanding" and must handle these requirements independently.

Three design elements appear critical. First, the prompt includes few-shot examples of relevant, marginally-relevant, and irrelevant query-product pairs, anchoring the agent's understanding of evaluation criteria. Second, the search tool documentation emphasizes its constraints rather than hiding complexity, preventing the agent from assuming nonexistent capabilities. Third, structured outputs require the agent to articulate intent explanations and search plans, potentially forcing more deliberate reasoning.

Turnbull acknowledges substantial unanswered questions. The structured output requirement might represent wasted tokens. Semantic caching of training queries, tool memory accumulation, and category filtering weren't systematically evaluated. Most ambitiously, he wonders whether learned tool interactions could improve traditional non-agentic search interfaces.

The work sits at the intersection of practical engineering and theoretical curiosity. The code is publicly available, inviting reproducibility and extension. Rather than claiming definitive solutions, Turnbull frames these results as "experimentation, exploration, and happy failures," emphasizing that this represents early-stage exploration of how reasoning changes search fundamentally. For practitioners building search systems, the research offers a compelling argument that reasoning-first architecture can dramatically outperform carefully engineered lexical approaches—at least at experimental scale.
