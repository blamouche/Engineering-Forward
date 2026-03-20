# Leanstral: Open-Source Foundation for Trustworthy Vibe-Coding
**Source**: https://mistral.ai/news/leanstral
**Date**: 2026-03-16
**Author**: Mistral AI
**Keywords**: Leanstral, Lean 4, formal verification, proof engineering, open source, Mistral, AI coding, mathematics

## Elevator pitch
Mistral's Leanstral is the first open-source AI model specialized for Lean 4 proof engineering, reducing human verification time for AI-generated code in high-stakes mathematical and safety-critical contexts.

## Takeaways
- Leanstral targets the bottleneck of human verification time for machine-generated code in formal proof environments
- 6B active parameters in a sparse architecture, optimized specifically for Lean 4 proof engineering tasks
- Benchmarks: 26.3 score with half the compute passes of open-source rivals; 31.9 at maximum depth, exceeding Claude Sonnet by 8 points
- Cost comparison: $36 vs Claude Sonnet's $549 for comparable proof tasks
- Apache 2.0 licensed; accessible via Mistral Vibe, free API endpoint (`labs-leanstral-2603`), and downloadable weights

## Synthesis
Leanstral addresses a problem that most AI coding discussions overlook: for mathematics research, safety-critical software, and formal verification work, the limiting factor is not code generation speed but human expert time spent verifying that AI-generated proofs are actually correct.

Lean 4 is a proof assistant that can express sophisticated mathematical objects and verify software specifications with mathematical rigor. It is used in cutting-edge mathematics research (including several recent Fields Medal-adjacent results) and in high-assurance software development where correctness must be formally demonstrable rather than merely tested. The challenge is that Lean proofs are notoriously difficult to write—even skilled mathematicians spend significant time on proof engineering details rather than mathematical substance.

Leanstral's 6B active parameter architecture is deliberately lean (the name is intentional). The sparse architecture optimizes inference efficiency for the specific token distribution and syntactic patterns of Lean 4, where general-purpose language model capabilities are largely irrelevant. This specialization produces meaningful benchmark advantages: competitive performance at half the compute passes of rival models, and exceeding Claude Sonnet's scores at maximum testing depth while costing approximately 15x less ($36 vs $549).

The practical case studies reported—diagnosing Lean version compatibility issues and translating formal reasoning frameworks between programming languages—hint at the workflow being automated. These are exactly the tasks where domain experts currently lose hours to mechanical debugging rather than mathematical insight. By handling the proof engineering scaffolding, Leanstral frees mathematicians and formal verification engineers to focus on the hard mathematical content.

Apache 2.0 licensing and multiple access paths (free API endpoint, downloadable weights, Mistral Vibe integration) reflect a genuine commitment to academic accessibility. Mathematics research runs on academic budgets where $549 per proof task is prohibitive, but $36 is potentially viable. This cost accessibility is arguably as important as the capability improvement for driving actual adoption in the domains where formal verification matters most.
