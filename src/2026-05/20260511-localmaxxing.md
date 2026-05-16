# Localmaxxing
**Source**: https://www.tomtunguz.com/localmaxxing/
**Date**: May 11, 2026
**Author**: Tomasz Tunguz
**Keywords**: local inference, localmaxxing, tokenmaxxing, Qwen, Claude Opus, MacBook Pro M5, agentic tasks, latency, privacy, cost optimization

## Elevator pitch
Tomasz Tunguz finds that 50% of his 1,478 daily agentic AI tasks can run successfully on a local 35B model running on his MacBook Pro M5, with latency as the decisive advantage — local inference is twice as fast, and the local model produces terser, equally correct outputs for routine work.

## Takeaways
- Over five weeks tracking 1,478 agentic tasks, Tunguz found that half (618 tasks across email, scheduling, summarization, and admin) succeed on a local Qwen 35B model — only complex market research and engineering tasks need cloud frontier models.
- In head-to-head benchmarks, the local Qwen 35B matched Claude Opus 4.5 on task completion correctness while running 2x faster; Opus won on polish and structure, Qwen won on brevity (often half the tokens).
- For agentic workflows where output feeds into another system, terseness is a feature — the local model's concise output is actually preferable.
- Local models lag frontier by 3–4 months and score ~20% lower on reasoning benchmarks, but for routine agent tasks this gap rarely matters.
- "Localmaxxing" is framed as an inevitable response to "tokenmaxxing" — as AI inference demand explodes, pushing workloads to local hardware extracts value from depreciating assets while delivering better latency and privacy.

## Synthesis
Tomasz Tunguz coins the term "localmaxxing" to describe a strategy he's been testing over five weeks: shifting as much AI inference as possible from cloud frontier models to local models running on his own hardware. With AI inference demand exploding, he asked a simple question: how much of his daily work can a 35B-parameter model handle?

The answer, based on tracking 1,478 agentic tasks across categories, is 50%. Tunguz classified his tasks into seven categories: email and inbound (11.5%), scheduling (17.2%), summarization (12.4%), admin (0.7%), market research (13%), engineering (9.9%), and a catch-all "other" (35.3%). The first four categories — totaling 618 tasks or 41.8% of the total — succeed reliably on a local model. Market research and engineering split roughly 50/50 between tasks simple enough for local inference and those requiring frontier-model reasoning. That gets to 50% overall.

The head-to-head benchmark is the most concrete evidence. Tunguz ran eight agentic tasks with identical prompts on both Qwen 3.6 35B-A3B-4bit running locally on his MacBook Pro M5 and Claude Opus 4.5 via API. Both models completed every task correctly. The differences were in style, not substance: Opus delivered more structured output with bullet points, headers, and cleaner code. Qwen produced output that was often half the length. For agentic workflows where one model's output feeds directly into another system, brevity is genuinely preferable — it means fewer tokens to process downstream.

The latency advantage is what Tunguz identifies as the real killer feature. Local inference on his MacBook runs twice as fast as API calls to cloud frontier models. When half of your daily AI interactions run at 2x speed on hardware you already own, the trade-off becomes obvious. Privacy and cost are bonus reasons; latency is the one that actually matters day to day.

Tunguz positions localmaxxing as a natural counter-force to "tokenmaxxing" — the trend of AI systems consuming ever more tokens per task. As local models continue to close the gap with frontier models (currently lagging by 3–4 months), and as the GPU shortage makes cloud inference increasingly expensive, more users will shift workloads to their own hardware. The MacBook Pro, Tunguz notes, depreciates whether you use it or not — running local inference extracts compute value from a sinking asset. His conclusion is pragmatic: if half the work runs twice as fast on hardware you already own, you take that trade every time.
