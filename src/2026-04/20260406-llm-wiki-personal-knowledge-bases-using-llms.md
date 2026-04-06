# llm-wiki

**Source**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
**Date**: April 6, 2026
**Author**: Andrej Karpathy
**Keywords**: personal knowledge base, wiki, Obsidian, LLM agents, memory, knowledge management, markdown

## Elevator pitch
Karpathy sketches a compelling alternative to RAG: let an agent continuously maintain a structured markdown wiki that sits between raw sources and future queries, so synthesis compounds instead of being rebuilt from scratch every time.

## Takeaways
- The central idea is to maintain a persistent wiki rather than repeatedly querying raw documents through RAG alone.
- An LLM-maintained wiki can update summaries, entities, contradictions, and cross-links as new sources arrive.
- The human curates sources and questions while the model handles bookkeeping and knowledge maintenance.
- Index and log files provide lightweight navigability without requiring embeddings at modest scale.
- The concept treats markdown plus git plus an agent schema as a practical knowledge operating system.

## Synthesis
Karpathy’s “llm-wiki” gist is interesting because it reframes knowledge work from retrieval to compilation. Standard RAG assumes that every hard question starts over: fetch chunks, re-synthesize, hope the right fragments surface. The wiki model instead creates an intermediate artifact that accumulates understanding over time. Once an agent has already extracted themes, contradictions, and cross-links into a persistent markdown graph, future questions can operate on a richer substrate than raw documents.

That matters because a lot of useful knowledge work is not about finding one fact; it is about building and maintaining a mental model. Humans are bad at the bookkeeping required to keep such a model fresh across dozens or hundreds of sources. LLMs are unusually good at exactly that kind of low-status maintenance work: updating summaries, inserting links, filing notes, reconciling changes, and keeping indexes current.

The proposal is also attractive because it is low-tech in the best way. Markdown files, git history, Obsidian, index pages, and logs are all understandable and inspectable. You do not need a giant retrieval stack to start. The wiki becomes the memory layer, the schema becomes the behavioral contract, and the agent becomes the maintainer. That is a more legible architecture than many “AI knowledge platform” pitches.

The bigger lesson is that compounding knowledge requires compounding artifacts. If every answer disappears into chat history, you are wasting previous work. If good answers are filed back into a maintained wiki, the system gets stronger with use.
