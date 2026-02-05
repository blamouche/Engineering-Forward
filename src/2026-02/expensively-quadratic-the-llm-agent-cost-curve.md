# Expensively Quadratic: the LLM Agent Cost Curve
**Source**: https://blog.exe.dev/expensively-quadratic?utm_source=tldrai
**Date**: Unknown (published before 2026-02-05)
**Author**: exe.dev
**Keywords**: LLM agents, cost, context windows, caching, token economics, agent loops

## Elevator pitch
As agent conversations grow, the *cache read* component of LLM pricing can dominate total spend, creating an effectively quadratic-looking cost curve driven by (context length × number of calls) rather than raw tokens alone.

## Takeaways
- In agent loops, every tool call round-trips the full conversation, so costs accumulate across many LLM calls.
- With provider caching, you pay for cache writes and (cheap but growing) cache reads; over long contexts, cache reads become the majority of cost.
- Empirically, a sample feature-implementation run ended with cache reads at ~87% of total cost; “half the cost” point occurred around ~27.5k tokens.
- The scary part is not strictly tokens²; it’s tokens × calls—different workflows have very different call counts.
- Practical levers: reduce call count, avoid splitting large tool outputs into many small returns, use subagents/out-of-band iteration, and sometimes restart conversations.

## Synthesis
This post models the economics of modern coding agents as a loop: the agent repeatedly sends the “conversation so far” to an LLM, receives output plus tool calls, executes tools, and repeats. That structure means long tasks involve many LLM calls, and each call reprocesses (or re-reads) a growing context.

LLM pricing now often includes multiple components: input tokens, output tokens, cache writes (what you ask the provider to store), and cache reads (what subsequent calls read from that cache). In an agent loop, the previous turn’s output typically becomes the next turn’s cached content. As the context grows, each subsequent call reads more from the cache. Even if cache reads are discounted, the total cost of “reading the story so far” increases steadily and can dominate the bill.

The author visualizes this as rectangles per call (input/write/output/read) where the bottom “cache read” band grows with context length. Summed across many calls, this creates a triangular area that looks quadratic: the longer the context, the more each subsequent call pays to read it. In one real conversation cited, total cost was about $12.93 and cache reads were 87% of cost by the end.

To test whether this is common, the post references aggregate cost telemetry from exe.dev’s gateway across many agent conversations (without storing message content), showing wide variation in curves depending on behavior: some runs generate lots of expensive output; others read many files (tool output) which effectively becomes cache writes; others re-write to cache after expiry.

A key clarification is that the “quadratic” is better thought of as *tokens × number of calls*. Two sessions with similar final context length can differ dramatically in total cost depending on how chatty the loop is. That insight matters for agent design: reducing the number of iterations can be as impactful as shrinking context.

The post ends with practical suggestions and a useful metaphor (“dead reckoning”): fewer calls may be cheaper but risk less feedback-driven correction. It argues that splitting large tool outputs into multiple small chunks is counterproductive—if the agent will read the whole file anyway, send it once. It also points to subagents and tools that do work outside the main context window, and even restarting conversations when the marginal cost of continuing exceeds the cost of re-establishing context.
