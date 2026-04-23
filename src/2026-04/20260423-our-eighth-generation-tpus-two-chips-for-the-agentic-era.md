# Our eighth generation TPUs: two chips for the agentic era

**Source**: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era
**Date**: April 22, 2026
**Author**: Google Cloud
**Keywords**: TPU 8t, TPU 8i, training, inference, agentic AI, efficiency, Google DeepMind

## Elevator pitch
Google split its eighth-generation TPU family into a training chip and an inference chip, arguing that agents and reasoning workloads need distinct hardware tradeoffs instead of one general-purpose accelerator.

## Takeaways
- TPU 8t is optimized for large frontier-model training with bigger clusters, memory pools, and interconnect bandwidth.
- TPU 8i is optimized for inference and reinforcement-learning loops with more SRAM, more HBM, and lower-latency collectives.
- Google says specialization improves both economics and performance compared with one blended design.
- Both chips fit inside a larger co-designed system including Axion hosts, Virgo networking, and liquid cooling.
- The company is positioning TPUs as open to JAX, PyTorch, SGLang, and vLLM rather than as a Google-only stack.

## Synthesis
Google’s TPU post makes a clean strategic argument: the market has matured enough that training and inference should no longer be treated as the same hardware problem. That is the real significance of TPU 8t and TPU 8i. TPU 8t is the training workhorse, built for raw cluster scale, shared memory, and utilization across giant superpods. TPU 8i is the reasoning engine, built for low-latency inference, KV-cache-heavy serving, and the communication patterns of multi-agent and mixture-of-experts workloads.

This split reflects how AI workloads are changing. Frontier training still rewards scale, throughput, and resilience, but production inference now has its own demanding profile. Agents do not simply answer a prompt and stop. They think in loops, call tools, hold state, and operate under real-time expectations. That puts pressure on memory bandwidth, cache locality, and collective operations in ways that a training-optimized chip may not handle economically. Google’s emphasis on larger SRAM, improved HBM, new topology choices, and a collectives acceleration engine on TPU 8i is basically an admission that serving intelligent systems at scale is its own first-class market.

The article also shows how much Google’s TPU strategy depends on full-stack control. The chips are described alongside Axion hosts, Virgo networking, storage paths, and software compatibility. That matters because AI infrastructure economics are increasingly system-level, not chip-level. A faster accelerator is only useful if the network, storage, and failure handling around it preserve goodput.

The broader takeaway is that AI infrastructure is entering a more specialized phase. Instead of one giant accelerator family stretched across all tasks, providers are starting to tune hardware to the actual economics of model development and deployment. Google wants that specialization to be seen as a strength, especially in a world where agentic workloads could become a larger share of demand than classic chatbot traffic.
