# How Meta Used AI to Map Tribal Knowledge in Large-Scale Data Pipelines

**Source**: https://engineering.fb.com/2026/04/06/developer-tools/how-meta-used-ai-to-map-tribal-knowledge-in-large-scale-data-pipelines
**Date**: April 6, 2026
**Author**: Meta Engineering
**Keywords**: context engineering, tribal knowledge, agents, codebase mapping, data pipelines

## Elevator pitch
Meta describes building a swarm of specialized agents to read a large multi-repo data pipeline, distill undocumented engineering knowledge into compact context files, and improve downstream agent efficiency.

## Takeaways
- Meta used more than 50 specialized tasks to map over 4,100 files across several repositories and languages.
- The output was 59 concise context files plus documented non-obvious patterns that were previously trapped in engineers’ heads.
- The files are intentionally short “compasses,” not encyclopedic summaries, to stay useful inside modern context windows.
- Precomputed context reduced exploratory tool calls in preliminary tests and made agent guidance more reliable.
- Meta positions freshness and automatic refresh as essential because stale context can be worse than no context.

## Synthesis
Meta’s write-up captures a key shift in agent engineering: the bottleneck is often not the model but the absence of legible, durable context about proprietary systems. In large internal codebases, the most valuable knowledge rarely lives in docs. It lives in local conventions, hidden dependencies, naming traps, and historical reasons that only a few engineers remember.

Their solution is notable because it treats context creation itself as an agentic workload. Rather than hand-authoring giant reference manuals, Meta orchestrated specialist agents to explore, summarize, critique, repair, and continuously refresh a knowledge layer. That is a much more scalable pattern for organizations with sprawling, evolving codebases.

The “compass, not encyclopedia” idea is the right insight. Context files only help if they improve routing and decision quality at the moment of action. Overlong summaries merely reintroduce the original problem in a different format. Short files that point to the key files, patterns, and pitfalls are more aligned with how agents actually work.

The broader lesson is that AI readiness is becoming a documentation problem of a new kind. The winning teams will not just add copilots to codebases; they will build machine-readable maps of their internal systems and keep them fresh. Meta is showing what that operational layer can look like in practice.
