# NVIDIA Blackwell Leads on First Agentic AI Infrastructure Benchmark
**Source**: https://blogs.nvidia.com/blog/nvidia-blackwell-agentperf-artificial-analysis/
**Date**: 2026-06-12
**Author**: Shruti Koparkar (NVIDIA)
**Keywords**: NVIDIA, Blackwell, GB300 NVL72, AgentPerf, Artificial Analysis, agentic AI benchmark, inference infrastructure, DeepSeek V4 Pro

## Elevator pitch
NVIDIA's Blackwell Ultra GB300 NVL72 platform delivers leading performance on AgentPerf—the industry's first agentic AI infrastructure benchmark from Artificial Analysis—running up to 20x more agents per megawatt than NVIDIA Hopper H200, measured on real-world coding agent trajectories rather than single LLM calls.

## Takeaways
- AgentPerf is the first benchmark designed specifically for agentic AI workloads, measuring how many chained LLM+tool-call agent tasks a platform can run simultaneously while meeting latency and throughput targets
- NVIDIA GB300 NVL72 runs up to 20x more concurrent agents per megawatt than HGX H200, measured at both 20 and 60 tokens/second per agent service-level objectives
- The benchmark uses DeepSeek V4 Pro (a large MoE frontier model) as the workload, reflecting the class of models powering production agents
- AgentPerf is built on real coding agent trajectories: file reading, code writing/editing, command execution, and iteration across 12+ programming languages
- The 72-GPU rack-scale system enables efficient MoE distribution, with CUDA kernels overlapping communication and compute to absorb coordination costs
- TensorRT LLM separates input processing from output generation for independent optimization, sustaining efficiency as concurrent sessions scale

## Synthesis
AgentPerf represents a meaningful shift in how AI infrastructure is benchmarked. Existing inference benchmarks (throughput per single LLM call, latency for one request) fundamentally misrepresent agentic workloads, where dozens to hundreds of chained LLM calls with growing context and tool-call delays create multiplicative complexity. By building the benchmark on real coding agent trajectories—file reads, code edits, command execution, iteration loops—Artificial Analysis has created a proxy for the actual production workload that enterprises care about.

NVIDIA's 20x agents-per-megawatt advantage over Hopper is the headline, but the methodology details matter more. Tool calls are simulated with representative CPU processing time, so the benchmark isolates accelerated computing performance rather than measuring tool execution speed. This means the results directly inform GPU-level infrastructure decisions: how many concurrent agentic tasks can run per accelerator and per megawatt.

The full-stack codesign argument is credible. GB300 NVL72 connects 72 GPUs in a single rack, enabling large MoE models like DeepSeek V4 Pro to distribute efficiently. The CUDA kernel optimization that overlaps communication and compute is not a marketing claim—it's the standard pattern for MoE serving at scale, and NVIDIA's vertical integration (silicon, networking, CUDA, TensorRT) makes this hard to replicate on commodity hardware. The mention of Vera Rubin being in full production signals that NVIDIA is already planning the next benchmark round with next-generation hardware.

For engineering teams, the practical takeaway is that agentic AI infrastructure sizing requires a fundamentally different approach than chat inference. The number of concurrent agents, the SLO per agent (tokens/second), and the total useful work per megawatt are the metrics that matter. Teams should evaluate infrastructure using AgentPerf-style benchmarks rather than extrapolating from single-call throughput numbers.