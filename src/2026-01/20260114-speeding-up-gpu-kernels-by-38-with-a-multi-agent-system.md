# Speeding up GPU kernels by 38% with a multi-agent system

**Source**: https://cursor.com/blog/multi-agent-kernels
**Date**: January 14, 2026
**Author**: Wilson Lin
**Keywords**: cursor, speeding, kernels, with, multi, agent, system

## Elevator pitch
Our multi-agent system autonomously optimized 235 CUDA kernels for NVIDIA Blackwell 200 GPUs, achieving a 38% geomean speedup over baselines in just 3 weeks

## Takeaways
- Blog / research Over the past few months, we've been developing a multi-agent system that can build, maintain, and deploy complex software autonomously.
- As part of that work, we've been testing the system in a variety of domains, including having it build a browser from scratch and solve a research-level math problem on the First Proof benchmark .
- Recently, we began collaborating with NVIDIA on a new challenge: applying the multi-agent harness to optimize CUDA kernels.
- These are difficult technical problems with important real-world consequences: CUDA kernels are the core software that supports AI model training and inference on NVIDIA GPUs.
- Faster kernels mean better GPU utilization, reduced energy consumption, lower latency, and reduced cost per token—allowing providers to serve bigger, more capable models to more users at once.

## Synthesis
Blog / research Over the past few months, we've been developing a multi-agent system that can build, maintain, and deploy complex software autonomously. As part of that work, we've been testing the system in a variety of domains, including having it build a browser from scratch and solve a research-level math problem on the First Proof benchmark . Recently, we began collaborating with NVIDIA on a new challenge: applying the multi-agent harness to optimize CUDA kernels. These are difficult technical problems with important real-world consequences: CUDA kernels are the core software that supports AI model training and inference on NVIDIA GPUs. Faster kernels mean better GPU utilization, reduced energy consumption, lower latency, and reduced cost per token—allowing providers to serve bigger, more capable models to more users at once. Our multi-agent harness operated autonomously for three weeks across 235 problems. The system achieved a 38% geomean speedup by building and optimizing Blackwell GPU kernels from scratch, all the way down to the assembly level. These levels of performance improvement are typically only found through months or years of work from highly experienced kernel engineers. The multi-agent system accomplished it in weeks, addressing a long-tail of kernel problems that had been impractical with existing approaches. # Kernel optimization as a test of agent system capabilities One of the best ways to evaluate long-running, multi-agent systems is to give them open-ended optimization problems where even we don't know the right answer.
