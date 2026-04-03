# Chroma Context-1: Training a Self-Editing Search Agent
**Source**: https://www.trychroma.com/research/context-1
**Date**: March 26, 2026
**Author**: Hammad Bashir, Kelly Hong, Patrick Jiang, Zhiyi Shi (Chroma)
**Keywords**: retrieval, search agent, self-editing, reinforcement learning, RAG, 20B model, Apache 2.0, BrowseComp

## Elevator pitch
Chroma's Context-1 is a 20B open-weight retrieval agent that matches frontier models at 10x faster inference and 25x lower cost by training a model to self-edit its context window — discarding irrelevant results to free capacity for further search.

## Takeaways
- 20B parameter model specialized for retrieval, not answer generation — separates search from downstream reasoning
- Self-editing capability: actively prunes irrelevant retrieved documents mid-search to prevent context saturation
- Training uses staged curriculum (recall then precision), synthetic task generation across 4 domains, and RL with verifiable rewards
- 8,000+ training tasks generated with >80% human-judge alignment via extraction-based verification
- Apache 2.0 licensed with synthetic data generation codebase released for reproducibility

## Synthesis
Context-1 represents a principled architectural choice: treating retrieval as a specialized task that warrants a dedicated model rather than a capability absorbed into a general-purpose reasoning model. The premise is that a 20B model trained specifically on retrieval tasks — decomposing queries, executing multi-hop searches, and selectively pruning results — can match frontier models (which are orders of magnitude larger) at this specific task, while being substantially faster and cheaper to run.

The self-editing capability is the conceptual innovation. In multi-turn retrieval, agents gather information across multiple search iterations. Each iteration fills context window space with retrieved content, some of which is irrelevant to the final answer. Without pruning, context windows fill with noise that degrades reasoning quality and increases cost. Context-1 trains the retrieval agent to actively discard irrelevant content during the search process, treating context management as part of the retrieval task itself rather than an external concern.

The training methodology is carefully sequenced. The staged curriculum — first optimizing for recall (finding all relevant documents) before shifting to precision (filtering irrelevant ones) — reflects the insight that you cannot train for selectivity before establishing the ability to find relevant information. Trying to optimize both simultaneously risks training a model that conservatively retrieves very little to avoid precision penalties, missing the retrieval goal entirely.

Synthetic task generation across four domains (web, finance, legal, email) addresses the challenge of obtaining training data for complex multi-hop retrieval tasks. Real-world retrieval tasks are difficult to annotate because verifying that a retrieved document is truly relevant often requires expert judgment. The extraction-based verification pipeline — generating tasks where the answer can be extracted and verified programmatically — enables automated quality control at the scale needed for RL training.

The open-source release, including model weights and the data generation codebase, enables the research community to replicate and build on this work. For engineering teams building RAG systems, Context-1 provides a practical alternative to using frontier models for retrieval — a task where specialized smaller models may outperform general-purpose large models at significantly lower cost.
