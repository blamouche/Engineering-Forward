# The Tech Stack Powering Wise

**Source**: https://blog.bytebytego.com/p/the-tech-stack-powering-wise
**Date**: April 29, 2026
**Author**: ByteByteGo
**Keywords**: blog, tech, stack, powering, wise

## Elevator pitch
AI inference: 24,240 TPS vs 1,863 TPS H100 (Sponsored).

## Takeaways
- The Tech Stack Powering Wise ByteByteGo Apr 29, 2026 233 1 Share AI inference: 24,240 TPS vs 1,863 TPS H100 (Sponsored) Most teams optimize models.
- We benchmarked NVIDIA RTX PRO 6000 Blackwell on Akamai Cloud against H100 using real LLM workloads.
- At 100 concurrent requests, Blackwell reached 24,240 tokens/sec per server, compared to 1,863 TPS on H100.
- That’s up to 1.63× higher throughput, with additional gains from FP4 precision.
- The difference comes down to architecture.

## Synthesis
The Tech Stack Powering Wise ByteByteGo Apr 29, 2026 233 1 Share AI inference: 24,240 TPS vs 1,863 TPS H100 (Sponsored) Most teams optimize models. We benchmarked NVIDIA RTX PRO 6000 Blackwell on Akamai Cloud against H100 using real LLM workloads. At 100 concurrent requests, Blackwell reached 24,240 tokens/sec per server, compared to 1,863 TPS on H100. That’s up to 1.63× higher throughput, with additional gains from FP4 precision. The difference comes down to architecture. These GPUs run on a globally distributed platform built for real-time, latency-sensitive inference, not centralized batch jobs. If you're building agentic systems or high-concurrency AI apps, infrastructure choices matter as much as model selection. See the full setup, methodology, and results. View benchmark results View Benchmark results In 2024, Wise’s deployment system automatically blocked hundreds of releases that would have caused production incidents. There was no human intervention, but the system routed just 5% of traffic to the new version, watched technical and business metrics for 30 minutes, and rolled back when it detected anomalies.
