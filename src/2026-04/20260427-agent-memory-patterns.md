# Agent Memory Patterns
**Source**: https://timkellogg.me/blog/2026/04/27/memory-patterns
**Date**: April 27, 2026
**Author**: Tim Kellogg
**Keywords**: agent memory, files, memory blocks, skills, observability

## Elevator pitch
The essay argues that agent memory is best understood as a small set of practical patterns, chiefly files, prompt-visible memory blocks, and skills, each serving different kinds of learning and recall.

## Takeaways
- The piece distinguishes between file-based memory, prompt-level memory blocks, and skills as separate memory mechanisms.
- Files are framed as the default place for data and knowledge because they are easy to explore, read, write, and version.
- Memory blocks are positioned as learnable prompt fragments best suited for preferences, identity, and behavior rules.
- Skills are described as indexed files whose descriptions in the prompt help agents load the right instructions only when needed.
- The author argues for versioning memory and warns against over-structured writable systems such as knowledge graphs or rigid schemas.

## Synthesis
This essay is valuable because it strips away the mystical framing that often surrounds agent memory and turns it into a design problem. Instead of asking whether an agent “has memory,” Tim Kellogg asks what sort of mutable information store the agent actually needs and how visible that store should be during reasoning. The resulting framework is simple: files for broad knowledge and working data, memory blocks for prompt-level behavioral context, and skills for selectively loaded instructions plus supporting assets.

The first contribution is the insistence that files remain the foundation. That sounds almost boring, which is exactly the point. If an agent can list, search, read, and write long text at stable paths, then it already has a powerful memory substrate. Files are flexible, versionable, and naturally inspectable by both humans and models. The essay pushes back against the temptation to over-engineer agent memory with exotic databases before basic file ergonomics are handled well.

The distinction between files and memory blocks is also useful. Files are for information the agent can retrieve when needed. Memory blocks are for information the agent should not forget to notice because they sit directly in the prompt. That makes them a better home for preferences, identity, and durable operating instructions, but also a more expensive one in token and cache terms. The article treats memory blocks less like storage and more like editable system prompt fragments, which is a clarifying mental model.

Skills occupy the middle ground. They are still files, but their names and descriptions are surfaced in the prompt so the agent knows when to consult them. This gives systems a form of progressive disclosure: detailed instructions stay out of context until relevant. That is not just a convenience feature. It is a scaling strategy for keeping agents capable without drowning them in permanent prompt mass.

The essay’s broader lesson is that memory quality depends as much on interfaces and observability as on storage. Versioning, discoverability, and clear triggers matter more than structured schemas the model does not naturally understand. In that sense, the piece is really about harness design. Good memory is not a giant brain implant. It is a set of readable, writable, inspectable surfaces that let the agent learn without becoming opaque.