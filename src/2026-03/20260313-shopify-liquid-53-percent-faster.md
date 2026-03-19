# Shopify/liquid: Performance: 53% faster parse+render, 61% fewer allocations
**Source**: https://simonwillison.net/2026/Mar/13/liquid/
**Date**: 2026-03-13
**Author**: Simon Willison
**Keywords**: Shopify, Liquid, Ruby, performance optimization, autoresearch, AI coding agent, Tobias Lütke, benchmark, memory allocations, automated experiments

## Elevator pitch
Shopify CEO Tobias Lütke used an AI coding agent running ~120 automated experiments to achieve 53% faster parsing and 61% fewer allocations in the Liquid template engine—a case study in executive-level AI-driven performance work.

## Takeaways
- Result: 53% faster parse+render, 61% fewer memory allocations in Shopify's open-source Ruby Liquid template engine.
- Methodology: Lütke deployed a coding agent running ~120 systematic micro-optimization experiments, generating 93 commits tracked via `autoresearch.jsonl`.
- Specific wins: replacing regex tokenization with byte-level searching (~12% parse time reduction), eliminating costly string resets, caching integer-to-string conversions.
- Critical enablers: a robust test suite (974 unit tests) and clear benchmarking scripts that allowed safe, measurable iteration.
- Broader pattern: AI coding agents are enabling senior executives, previously too interrupt-driven for sustained deep technical work, to contribute meaningfully to codebases.

## Synthesis
The Tobias Lütke angle is the most interesting part of this story. CEOs of large technology companies typically drift away from hands-on technical contribution as their schedules fill with strategic and organizational demands. The observation that AI coding agents enable a different pattern—where executives can contribute meaningfully to technical work without requiring sustained uninterrupted focus—suggests AI tools may change how technical leadership functions, not just how individual contributors work.

The methodology reveals an important principle: the agent succeeded because it had excellent feedback infrastructure. 974 unit tests provided safety (the agent knew when it broke something), clear benchmarks provided direction (the agent could measure whether a change helped), and systematic experiment tracking via `autoresearch.jsonl` created a record that could be analyzed and iterated. Without these infrastructure elements, the same approach would produce chaotic, unreliable results.

The specific optimization pattern—systematic micro-optimization through automated experimentation—is particularly suited to AI assistance. Identifying that byte-level string searching is faster than regex tokenization is the kind of insight that requires methodically testing alternatives; it's not something that emerges from reading code. An agent can run 120 variations systematically, measuring each one, in a timeframe that would be unrealistic for human-driven optimization.

The 61% reduction in memory allocations is significant for a template engine called at scale. Liquid is used to render millions of Shopify store pages; allocation reduction at this scale compounds across the entire Shopify infrastructure, reducing GC pressure and improving latency consistency. This is exactly the kind of impact that makes infrastructure-level optimization valuable despite its lack of user-visible features.
