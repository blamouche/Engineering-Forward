# Context Engineering with Dex Horthy
**Source**: https://newsletter.pragmaticengineer.com/p/context-engineering-with-dex-horthy
**Date**: 2026-07-15
**Author**: Gergely Orosz
**Keywords**: context engineering, LLM, agents, software factories, 12-factor agents, HumanLayer, code quality

## Elevator pitch
Dex Horthy, CEO of HumanLayer and author of "12-Factor Agents," explains why context engineering—managing what goes into an LLM's context window—is becoming the critical skill for building reliable AI-assisted software.

## Takeaways
- Shipping unread AI-generated code spells disaster within months; Dex's team abandoned an entire codebase after four months of no-review AI coding because production broke and no one could find the root cause
- Today's coding models are likely trained to optimize for SWE-bench-style benchmarks, which reward reproducing known fixes but cannot evaluate poor architecture decisions, causing codebases to degrade over time
- Context engineering means figuring out where the "dumb zone" begins—Dex uses roughly 300-400K of a 1M context window before performance degrades; larger context windows don't mean smarter models
- Frequent intentional compaction—compressing noisy context into a clean Markdown document and starting a fresh session—is a key technique for complex projects, using a workflow of research → design → plan → review
- Three viable software factory models exist: "turn off the lights" (failed by Dex), read all AI code (30-50% productivity lift), or find leverage with people in the loop on design/architecture (2-3x faster)

## Synthesis
Context engineering, a term coined by Dex Horthy, is rapidly becoming essential knowledge for any engineer working with LLMs. The core insight is deceptively simple: the less context you use, the better the model performs, because the attention mechanism is quadratic—more tokens means more compute and more room for error. Dex identifies four dimensions that matter in the context window: size, information quality, missing information, and trajectory. Trajectory poisoning occurs when an LLM gets stuck in a loop of mistakes reinforced by the autoregressive nature of the model, signaled by phrases like "you're completely right"—a clear indication it's time to start a new session.

The conversation delivers a sobering case study: Dex's team tried shipping code without human review in July 2025. Within four months, production broke and even Opus 4.1 couldn't find the root cause in the spaghetti codebase. It took days of human review to discover a primary key routed incorrectly through the entire codebase, followed by three weeks of re-onboarding. The lesson aligns with broader industry observations—models trained on SWE-bench benchmarks excel at reproducing known fixes but cannot evaluate architectural decisions, systematically degrading codebases over time.

Dex's approach to "loop engineering" favors slow loops: nightly agents that open PRs for review each morning. This stands in contrast to the "token harder" mentality that maximizes usage of expensive subscriptions. Instead, "token smarter" means intentional compaction—compressing a long, noisy context into a clean Markdown document, then starting fresh. His recommended workflow chains sessions: one reads code and emits a research document, the next creates a design document, and the human reviews architecture at the leverage points. For software factories, Dex identifies three models and endorses the third: invest heavily in design and architecture review while letting agents handle implementation, achieving 2-3x speedups while preserving code quality.