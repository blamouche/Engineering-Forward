# Benchmarking Inference Engines on Agentic Workloads

**Source**: https://www.appliedcompute.com/research/inference-benchmark
**Date**: April 22, 2026
**Author**: Applied Compute
**Keywords**: inference engines, agentic workloads, benchmarking, KV cache, latency, throughput

## Elevator pitch
Applied Compute argues that classic prompt-in/prompt-out benchmarks miss what matters for agents, and releases workload traces that stress KV cache retention, scheduling, and long multi-turn sessions instead.

## Takeaways
- Agentic workloads have very different traffic shapes from single-turn chatbot benchmarks.
- The company highlights long traces, dozens of tool turns, heavy-tailed latency, and repeated prefills as core serving challenges.
- It proposes evaluating batch, background, and interactive agent deployments with different metrics.
- The open-source harness replays full traces instead of averaging them into one synthetic request shape.
- The paper pushes the industry toward benchmarking engines on realistic agent sessions rather than static token ratios.

## Synthesis
This post makes a strong case that the industry’s default inference benchmarks are increasingly detached from the workloads that matter most. Traditional tests usually reduce serving to a single request shape, such as a fixed number of input and output tokens. That works reasonably well for ordinary chat or summarization, but it breaks down once you move to agents. Real agents think in loops, call tools, wait on external systems, append more context, and resume generation across many turns. That pattern stresses schedulers, cache retention, and concurrency management in ways a single prompt-response test cannot capture.

Applied Compute’s framing is useful because it shows what changes operationally. The serving engine now has to decide whether to keep or evict large KV caches while tools run. It has to handle many short generations, long tails in tool outputs, and highly variable wait times. That means system design is no longer mainly about raw tokens per second. It is about how well an engine handles the lifecycle of a trace.

The article’s metric breakdown also matters. Batch jobs care about throughput per dollar. Background agents care about meeting an SLA for total trace completion. User-facing agents care about time to first answer token and the pace of streamed interaction. Those are different optimization targets, and pretending one benchmark covers them all obscures important tradeoffs.

The broader implication is that agentic software will push the inference stack to mature. Workloads are becoming less like independent API calls and more like long-lived sessions with state. Providers that benchmark and optimize for that reality will likely have an edge, especially as coding agents, research agents, and enterprise workflow agents become a larger share of traffic.
