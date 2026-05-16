# Localmaxxing
**Source**: https://www.tomtunguz.com/localmaxxing/
**Date**: May 11, 2026
**Author**: Tomasz Tunguz
**Keywords**: local inference, on-device AI, Qwen, MacBook, agent tasks, latency, privacy, cost optimization, tokenmaxxing

## Elevator pitch
Tomasz Tunguz finds that half of his 1,400+ weekly AI tasks can run successfully on a local 35B model on his MacBook, with the local model delivering 2x faster responses than cloud frontier models — making "localmaxxing" an inevitable response to soaring inference demand.

## Takeaways
- Over five weeks of testing, Tunguz classified 1,478 AI agent tasks; 50% could be handled by a local 35B model instead of cloud frontier models
- Email, scheduling, summarization, and admin tasks (41.8% of total) are almost entirely local-compatible
- Market research and engineering tasks split roughly 50/50 between simple tasks (local-ready) and complex ones (requiring frontier models)
- In head-to-head benchmarks, local Qwen 3.6 35B matched cloud Opus 4.5 on task completion, with Opus winning on polish and Qwen winning on brevity
- Local models reduce both cost and latency while keeping sensitive data on-device, but they lag frontier by 3-4 months on reasoning benchmarks

## Synthesis
Tomasz Tunguz's "localmaxxing" experiment tests a deceptively simple question: how much of a knowledge worker's AI usage can be satisfied by local models running on personal hardware rather than trillion-parameter models in the cloud? The answer — roughly half — has significant implications for how AI workloads will be distributed as inference demand explodes.

Over five weeks, Tunguz tracked and classified 1,478 AI agent tasks across seven categories. The results show a clear pattern: routine, structured tasks gravitate toward local feasibility while complex, open-ended tasks still require frontier models. Email and inbound handling, scheduling, summarization, and administrative tasks collectively represent 41.8% of all tasks and can almost entirely run locally. Market research and engineering tasks split evenly — simple data lookups and script fixes work locally, but multi-source synthesis and architectural decisions need cloud models. The remaining "other" category (35.3%) contains unstructured requests that fall somewhere in between.

The head-to-head benchmark between Qwen 3.6 35B-A3B (4-bit quantized, running on a MacBook Pro M5) and Claude Opus 4.5 via API reveals an interesting quality trade-off. Opus 4.5 scores roughly 20% higher on standard reasoning benchmarks and produces more structured, polished outputs with proper formatting. Qwen wins on brevity — often using half the tokens — and for agent tasks where output feeds into another system rather than being consumed by humans, terseness is a feature, not a bug. Both models completed all eight benchmark tasks correctly.

Tunguz identifies latency as the single most compelling argument for local inference. The local model ran roughly 2x faster on equivalent tasks, and in agentic workflows where multiple model calls chain together, this speed advantage compounds. Privacy and cost are secondary benefits: sensitive messages stay on-device, and the marginal cost of local inference is effectively zero. Tunguz frames localmaxxing as an inevitable response to tokenmaxxing — as users and organizations push more work through AI, the pressure to optimize inference location will only intensify. The gap between local and frontier models is currently 3-4 months and closing.
