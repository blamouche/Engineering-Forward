# Can LLMs Be Computers?
**Source**: https://www.percepta.ai/blog/can-llms-be-computers
**Date**: 2026-03-11
**Author**: Christos Tzamos et al., Percepta
**Keywords**: LLM, transformer, Turing completeness, computation, C programs, 2D attention, computer science theory

## Elevator pitch
Percepta researchers demonstrate that transformers can execute arbitrary C programs for millions of steps by building a computer inside the architecture, achieving exponentially faster inference through novel 2D attention heads.

## Takeaways
- Researchers build a functional computer inside a transformer, executing arbitrary C programs for millions of steps
- Novel 2D attention head mechanism achieves exponentially faster inference compared to standard attention
- The work bridges theoretical computer science with practical neural network architecture
- Demonstrates that transformers possess capabilities beyond traditional language processing
- Opens questions about the fundamental computational equivalence of LLMs and general-purpose computers

## Synthesis
The question of what large language models are computationally capable of has occupied theorists since the transformer architecture became dominant. Percepta's research answers the question in a surprising direction: by building an actual computer inside a transformer, the team demonstrates not just that transformers can simulate computation but that they can execute it—running arbitrary C programs for millions of steps.

The core technical contribution is the 2D attention mechanism. Standard transformer attention operates on sequences, with attention computed as a function of positions in that sequence. The 2D variant extends this to a two-dimensional structure that enables the model to track program execution state across both the instruction sequence and time steps of execution. This architectural change, combined with careful encoding of CPU state into the transformer's representation space, produces a system capable of genuine general computation rather than statistical approximation of it.

The "exponentially faster inference" claim refers to the efficiency advantage of the 2D attention construction relative to the naive approach of simulating computation step-by-step in the attention mechanism. The 2D structure enables the model to make progress across multiple computation steps simultaneously, collapsing what would otherwise be a linear number of forward passes into a logarithmic (or better) number.

The practical implications are still emerging, but the theoretical significance is clear: if transformers can execute arbitrary C programs, they are Turing-complete (modulo memory constraints). This means that any limitation on transformer capability is a matter of training and context rather than fundamental architectural constraint. The work reframes the debate about AI capability ceilings—the question is no longer whether the architecture can support general computation, but whether training procedures can teach models to use that computational capacity reliably.
