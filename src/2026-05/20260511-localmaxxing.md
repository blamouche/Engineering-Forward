# Localmaxxing
**Source**: https://www.tomtunguz.com/localmaxxing/
**Date**: 2026-05-11
**Author**: Tomasz Tunguz
**Keywords**: local inference, on-device AI, latency, model comparison, Qwen, Claude Opus, agentic workflows, tokenmaxxing, edge computing

## Elevator pitch
Tomasz Tunguz demonstrates through five weeks of personal experimentation that half of knowledge-worker AI tasks can run successfully on a local 35B model with better latency than cloud frontier models, coining "localmaxxing" as the practice of shifting inference to local hardware.

## Takeaways
- Over five weeks, Tunguz analyzed 1,478 AI tasks and found that 50% (618 tasks: email, scheduling, summarization, admin) succeed on a 35B local model like Qwen 3.6.
- In a head-to-head benchmark of eight agentic tasks, the local Qwen 35B on a MacBook Pro M5 matched or exceeded Claude Opus 4.5 on task completion while running 2x faster on latency.
- Opus wins on output structure and polish (bullet points, headers, cleaner code); Qwen wins on brevity (often half the tokens), which is a feature when output feeds into another system.
- Local models lag frontier by approximately 3-4 months on reasoning benchmarks and ~20% on raw capability, but this gap rarely matters for routine agent tasks.
- Besides latency, local inference offers privacy benefits, zero marginal cost, and the ability to extract compute value from depreciating hardware assets.

## Synthesis
Tomasz Tunguz introduces "localmaxxing" as a deliberate practice: pushing as much AI inference as possible to local, on-device models rather than relying on cloud frontier models. The concept emerges from five weeks of personal experimentation where he tracked 1,478 discrete AI tasks across his daily workflow as a venture capitalist. The result: half of his workload runs successfully on a 35B parameter local model.

The task breakdown is instructive. Email and inbound management (11.5%), scheduling (17.2%), summarization (12.4%), and administrative tasks (0.7%) are nearly entirely local-model-compatible — totaling 41.8% of all tasks. Market research and engineering work split roughly 50/50 between simple tasks (data lookups, script fixes) and complex ones (multi-source synthesis, architectural decisions) that still require frontier models. Together, this gets to exactly 50% of all knowledge-work AI tasks being candidates for local inference.

The benchmark comparison provides empirical grounding. Running Qwen 3.6 35B-A3B-4bit on his MacBook Pro M5 against Claude Opus 4.5 via API on eight identical agentic tasks, Tunguz found both completed tasks correctly. Opus produces more structured, polished output (bullet points, headers, cleaner formatting), while Qwen delivers terser output — often half the tokens — which becomes a feature rather than a bug when output feeds directly into another automated system.

The latency difference is the decisive factor. While the local model isn't smarter (Opus scores ~20% higher on reasoning benchmarks) and lags frontier by about 3-4 months, Tunguz argues this gap rarely matters for routine agent tasks. For work where the output just needs to be correct and fast, the 2x speed advantage of local inference is compelling. He frames the broader thesis: as token consumption accelerates ("tokenmaxxing"), the counter-pressure to run inference locally becomes irresistible. Privacy, zero marginal cost, and extracting value from depreciating hardware all reinforce the trend, but latency is the one that actually matters in daily use.
