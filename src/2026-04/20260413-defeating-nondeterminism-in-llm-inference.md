# Defeating Nondeterminism in LLM Inference

**Source**: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference
**Date**: April 13, 2026
**Author**: Thinking Machines Lab
**Keywords**: LLM inference, nondeterminism, reproducibility, batching, kernel design, systems engineering

## Elevator pitch
Thinking Machines argues that practical LLM nondeterminism is driven less by mysterious GPU race conditions than by batch-size sensitivity inside otherwise deterministic kernels, making reproducibility a systems-design problem around batch invariance.

## Takeaways
- The essay distinguishes run-to-run kernel determinism from user-visible API nondeterminism, which can arise even when the core forward pass is deterministic.
- Its main claim is that changing batch composition under variable server load alters results because key kernels are not batch-invariant.
- The proposed path to reproducible inference is to engineer batch-invariant implementations of normalization, matrix multiplication, and attention rather than blame sampling alone.

## Synthesis
This is a strong systems paper because it attacks a folk explanation that has become too comfortable. Many people hand-wave LLM nondeterminism as “GPUs are parallel and floating point is messy,” which is directionally true but not precise enough to help. Thinking Machines makes the more useful claim: a lot of the nondeterminism users experience comes from batch-size dependence inside inference systems whose kernels may be deterministic in isolation. In other words, the problem is not just stochastic sampling or random race conditions. It is that the surrounding service architecture changes the computation path.

That reframing matters for product teams. If nondeterminism is partly a batching artifact, then reproducibility stops being purely a model concern and becomes a serving concern. Queueing strategy, load patterns, and kernel implementation details all shape whether identical requests behave identically. That is especially relevant for evaluation, enterprise reliability, and scientific workflows where “close enough” is not an acceptable definition of repeatability.

The deeper lesson is that we are entering a phase where inference quality is not just about cheaper tokens or faster throughput. It is also about numerical behavior guarantees. Vendors that can offer strong reproducibility may end up with an advantage in regulated, scientific, and engineering-heavy use cases where trust depends on re-running the same thing and getting the same answer.
