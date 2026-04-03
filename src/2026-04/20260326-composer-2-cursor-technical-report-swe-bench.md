# Composer 2 Technical Report: Frontier-Level Coding Model for Agentic Tasks
**Source**: https://arxiv.org/abs/2603.24477
**Date**: March 25, 2026
**Author**: Aaron Chan et al. (Cursor Research)
**Keywords**: Cursor, Composer 2, coding model, agentic software engineering, CursorBench, SWE-bench, reinforcement learning, pretraining

## Elevator pitch
Cursor's Composer 2 technical report documents a two-phase training approach — extended pretraining plus reinforcement learning on long-horizon coding tasks — achieving 73.7% on SWE-bench Multilingual and 61.3% on their internal CursorBench.

## Takeaways
- Two-phase training: extended pretraining for coding knowledge + RL targeting end-to-end agentic coding performance
- Training infrastructure mirrors the deployed Cursor harness environment for authentic evaluation
- 61.3% on CursorBench (internal), 61.7% on Terminal-Bench, 73.7% on SWE-bench Multilingual
- CursorBench is constructed from real engineering problems on large codebases — a methodological contribution
- Demonstrates that domain-specialized training from real problem datasets can achieve frontier-level results

## Synthesis
The Composer 2 technical report is notable as much for what it reveals about methodology as for the benchmark numbers it reports. The two-phase training approach — extended pretraining followed by reinforcement learning targeting end-to-end agentic coding performance — reflects a design philosophy that distinguishes domain-specialized models from general-purpose coding models fine-tuned for specific tasks.

The extended pretraining phase builds on a foundation of diverse coding knowledge, but the RL phase is what shapes behavior for the specific challenges of agentic software engineering. Where general RL for coding might reward task completion on synthetic benchmarks, Cursor's approach uses an environment that matches the deployed Cursor harness — meaning the model trains in conditions that closely mirror production use. This alignment between training environment and deployment environment is a standard principle in RL that is often under-implemented in practice.

CursorBench, constructed from real engineering problems on large codebases, is itself a contribution. Most public coding benchmarks use small, self-contained problems that don't capture the complexity of working in mature codebases — navigating large dependency graphs, understanding implicit conventions, making changes that are locally correct but globally consistent. Real-world coding tasks have this complexity, and a benchmark that captures it provides a more meaningful evaluation signal than isolated algorithmic problems.

The 73.7% SWE-bench Multilingual score places Composer 2 in competitive range with frontier models on a benchmark that tests real software engineering tasks across multiple programming languages. The 61.7% Terminal-Bench score is consistent with the broader picture of a model optimized for the interactive, terminal-based workflow that Cursor employs.

For the industry, Composer 2 demonstrates that application-layer companies can develop frontier-level domain-specific models by investing in training data quality and environment fidelity rather than simply scaling parameters. The proprietary user interaction traces that Cursor has access to, combined with the RL training against a production-faithful environment, create a training signal that general-purpose labs cannot easily replicate.
