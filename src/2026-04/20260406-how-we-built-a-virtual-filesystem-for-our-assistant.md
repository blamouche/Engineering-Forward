# How we built a virtual filesystem for our Assistant

**Source**: https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant
**Date**: April 6, 2026
**Author**: Mintlify
**Keywords**: RAG, virtual filesystem, documentation assistant, ChromaFs, retrieval, bash, docs AI

## Elevator pitch
Mintlify replaced sandboxed doc retrieval with a virtual filesystem over Chroma, letting its assistant navigate documentation like a codebase while cutting boot times from ~46 seconds to ~100 milliseconds and avoiding per-session compute costs.

## Takeaways
- Mintlify found plain RAG insufficient for multi-page synthesis and exact-structure navigation.
- Their solution virtualizes grep, cat, ls, find, and cd over a Chroma-backed doc store instead of spinning up sandboxes.
- The virtual filesystem preserves hierarchical traversal while staying fast enough for interactive UX.
- RBAC becomes easier because inaccessible paths can be pruned from the tree before the agent ever sees them.
- The approach suggests retrieval interfaces matter as much as retrieval models for agent quality.

## Synthesis
Mintlify’s post is a good example of a deeper shift in agent design: the best retrieval interface is often not “search,” but a substrate that looks like a familiar operating environment. Their assistant struggled when answers depended on structure across multiple docs pages. By exposing docs as a virtual filesystem, they let the agent browse the corpus the way a developer browses code—with ls, grep, find, and cat—instead of hoping top-k chunk retrieval reconstructs the right picture.

The real achievement is not conceptual novelty so much as systems pragmatism. A naïve version of this idea would clone repos into sandboxes and let agents work there, but Mintlify found that the latency and infrastructure bill were absurd for a user-facing assistant. ChromaFs preserves the filesystem illusion while mapping operations onto an index they already maintain. That is why the p90 boot time falls from tens of seconds to roughly instant.

There is also an important product lesson here. Agents do not need a “real” filesystem if the right affordances are preserved. If the interface behaves like a filesystem, supports the right primitives, and keeps access control intact, the agent gets most of the cognitive benefit without the infrastructure burden. That is a pattern worth copying elsewhere.

The broader implication is that RAG is not disappearing, but it is losing its monopoly as the default retrieval shape. The next generation of assistants will likely mix retrieval methods with more opinionated, task-native interfaces that make information easier for agents to explore.
