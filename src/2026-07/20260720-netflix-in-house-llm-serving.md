# In-House LLM Serving at Netflix
**Source**: https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c
**Date**: 2026-07-17
**Author**: Netflix Technology Blog
**Keywords**: Netflix, LLM serving, vLLM, Triton, inference, constrained decoding, GPU, production

## Elevator pitch
Netflix details how it deployed and operated LLM inference within its existing production infrastructure, covering engine selection (vLLM over TensorRT-LLM), model packaging, deployment strategies, and constrained decoding at scale.

## Takeaways
- Netflix chose vLLM over TensorRT-LLM for LLM serving, trading some performance for faster iteration, better debuggability, extensibility for custom decoding, and researcher familiarity—then integrated it with NVIDIA Triton Inference Server.
- The vLLM backend for Triton (vs. Python backend) proved architecturally superior by decoupling model artifacts from frontend upgrades, but production exposed version compatibility issues between Triton and vLLM.
- Netflix offers two deployment strategies: Red-Black (cheaper, atomic rollback) for stable interfaces, and Versioned (independent deployments per model version) for breaking changes, with a temporary GPU cost trade-off during transitions.
- Constrained decoding—enforcing business rules inside the decode loop rather than post-hoc—required migrating from vLLM V0's per-request GIL-bottlenecked processing to V1's batch-level design with C++ hot paths, achieving flat logits processing time regardless of batch size.
- Production surprises included partial prefills breaking state machine assumptions, vLLM preemption invalidating monotonic output growth, and Triton's OpenAI frontend silently dropping response_format constraints.

## Synthesis
Netflix's LLM serving deep dive is one of the most detailed production engineering accounts of running large models at member scale. The architecture decisions are instructive because Netflix optimized for its specific constraints: a unified JVM serving system, strict latency requirements, and a culture of A/B testing everything.

The vLLM-over-TensorRT-LLM choice is significant. TensorRT-LLM is faster in raw benchmarks, but Netflix valued iteration speed, extensibility for constrained decoding, and the research-to-production handoff. This is a pattern that will likely repeat across the industry: pure performance matters less than the total cost of owning and evolving a production system. The version compatibility pitfall—where Triton 25.09 imports a module removed in vLLM 0.11.2, causing silent failures—is the kind of integration surface that only surfaces at scale.

The constrained decoding work is the technical highlight. Rather than accepting invalid outputs and retrying, Netflix pushes business constraints into the decode loop itself, using state machines that emit token-eligibility masks at each step. The V0-to-V1 migration story—moving from sequential per-request Python processing to batch-level C++ with multi-threading—illustrates the real engineering cost of making constrained decoding production-viable at batch sizes where CPU processing becomes the bottleneck.

The deployment strategy section reveals an underappreciated problem: GPU deployments have longer cold starts than CPU services, and I/O schema changes create coordination gaps between upstream consumers and new model versions. Netflix's solution—embedding variable configurations directly into the inference model to make it version-agnostic—is a practical pattern that other teams deploying LLMs should adopt.

For teams building LLM serving infrastructure, Netflix's account provides a rare window into the gap between benchmark performance and production reality. The unified metrics endpoint merging Triton and vLLM metrics, the FSx model caching strategy, and the Red-Black versus Versioned deployment trade-offs are all patterns worth studying.