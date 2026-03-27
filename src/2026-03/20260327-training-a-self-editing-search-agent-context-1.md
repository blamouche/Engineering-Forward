# Training a Self-Editing Search Agent (Context‑1)
**Source**: https://www.trychroma.com/research/context-1
**Date**: Unknown
**Author**: Chroma
**Keywords**: retrieval, agentic search, context management, RL, RAG

## Elevator pitch
Chroma introduces Context‑1, a 20B search‑only agent trained with RL to perform multi‑hop retrieval while actively pruning its own context to avoid “context rot.”

## Takeaways
- Context‑1 is a retrieval subagent that outputs ranked documents, not final answers.
- Uses a self‑editing context mechanism to prune irrelevant chunks mid‑search.
- Trained on 8k+ synthetic multi‑hop tasks across web, finance, legal, and email.
- Achieves frontier‑level retrieval at lower cost and ~10× faster inference.
- Releases model weights and data‑gen pipeline code.

## Synthesis
Chroma argues that traditional RAG pipelines assume single‑shot retrieval, which breaks down for multi‑hop questions. Context‑1 addresses this by training a purpose‑built search agent that iteratively decomposes queries, retrieves documents, and manages a bounded context window by pruning irrelevant chunks. The model is positioned as a retrieval subagent, separating search from reasoning so downstream LLMs can focus on synthesis.

The training approach combines supervised fine‑tuning for tool‑use behavior with reinforcement learning on verifiable rewards (RLVR). The reward function heavily weights recall early in training, then shifts toward precision via a curriculum. A key innovation is explicitly rewarding “trajectory recall” so the model gets credit for discovering relevant docs even if they are later pruned, encouraging exploration while still learning to select a final subset.

Chroma also emphasizes synthetic data quality. Tasks are generated in a BrowseComp‑style format with multi‑constraint queries, and verified via quote‑extraction to ensure supporting documents actually match the clues. This reduces label noise and scales generation without heavy human annotation.

Results show Context‑1 outperforming its 20B base model across retrieval metrics, and approaching frontier performance while being faster and cheaper. The paper highlights strong pruning accuracy and more parallel tool use, which shortens trajectories and improves latency. The release includes weights and a data‑generation pipeline, signaling a push toward open, specialized retrieval agents that can serve as cost‑effective search submodules in larger AI systems.
