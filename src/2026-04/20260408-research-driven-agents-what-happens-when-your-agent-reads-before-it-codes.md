# Research-Driven Agents: What Happens When Your Agent Reads Before It Codes

**Source**: https://blog.skypilot.co/research-driven-agents
**Date**: April 8, 2026
**Author**: Alex Kim
**Keywords**: fusion, optimizations, agents, norm, attention, before

## Elevator pitch
The experiment log What the research turned up The pivot: from compute to memory Optimizations that landed 1.

## Takeaways
- Flash attention KQ fusion Results Optimizations that landed 1.
- Flash attention KQ fusion What didn’t work Experiments that failed The benchmark bug Cloud VMs are noisy The code review TL;DR: Coding agents generate better optimizations when they read papers and study competing projects before touching code.
- We added a literature search phase to the autoresearch / pi-autoresearch loop, pointed it at llama.cpp with 4 cloud VMs, and in ~3 hours it produced 5 optimizations that made flash attention text generation +15% faster on x86 and +5% faster on ARM ( TinyLlama 1.1B ).
- The full setup works with any project that has a benchmark and test suite.
- Agents that read papers and study competing projects before writing code find optimizations that code-only agents miss.

## Synthesis
The experiment log What the research turned up The pivot: from compute to memory Optimizations that landed 1. Flash attention KQ fusion Results Optimizations that landed 1. Flash attention KQ fusion What didn’t work Experiments that failed The benchmark bug Cloud VMs are noisy The code review TL;DR: Coding agents generate better optimizations when they read papers and study competing projects before touching code. We added a literature search phase to the autoresearch / pi-autoresearch loop, pointed it at llama.cpp with 4 cloud VMs, and in ~3 hours it produced 5 optimizations that made flash attention text generation +15% faster on x86 and +5% faster on ARM ( TinyLlama 1.1B ). The full setup works with any project that has a benchmark and test suite. Agents that read papers and study competing projects before writing code find optimizations that code-only agents miss. The literature research pointed the agent at operator fusions present in CUDA/Metal backends but absent from CPU. 5 of 30+ experiments landed: 4 kernel fusions and an adaptive parallelization.
