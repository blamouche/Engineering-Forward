# Don't Vibe — Prove
**Source**: https://ngrislain.github.io/projects/2026-3-12-dont-vibe--prove/
**Date**: 2026-03-12
**Author**: NGrislain
**Keywords**: dependent types, Lean 4, formal verification, type-driven development, Curry-Howard, AI coding, proof, specification, correctness

## Elevator pitch
Dependent type systems like Lean 4 create a synergy with AI coding: the adversarial compiler feedback that exhausts human developers is exactly where AI thrives—enabling AI to construct complex proofs while humans write specifications that are simultaneously code.

## Takeaways
- Types as specifications: Curry-Howard correspondence means "types are propositions, programs are proofs"—a function signature like `List α → SortedList α` simultaneously defines requirements and proves correctness.
- The AI-verification synergy: AI excels at generating code; formal verification exhausted humans but creates the kind of systematic compiler feedback that AI handles efficiently.
- Dependent types close the specification-implementation gap: unlike TLA+ or model checking, type-driven development unifies spec and code—"the specification is the code."
- Practical demonstration: two AI-generated sort implementations (insertion sort and merge sort) satisfy identical type signatures, showing different algorithms meeting the same formally-verified specification.
- Why now: dependent type systems existed for decades but manual proof construction was economically infeasible; AI changes the cost-benefit analysis.

## Synthesis
The insight that "adversarial compiler feedback is where AI thrives" reframes the relationship between formal verification and AI coding tools. Humans find the iterative cycle of proof construction—write an attempt, get a type error, revise, repeat dozens of times—mentally exhausting and slow. LLMs operating in a tight feedback loop with a dependent type compiler like Lean 4 can iterate at machine speed, treating each type error as a training signal for the next attempt.

This is structurally different from using AI to write tests or even to write code. Tests verify behavior after the fact; types verify correctness before execution. When the type signature encodes the specification, an AI that can satisfy the type checker has produced provably correct code—not just code that passes a test suite, but code that cannot contain certain classes of errors by construction.

The unification of specification and implementation addresses a fundamental problem in software verification: specifications drift from implementations. A TLA+ model of a distributed protocol and its Go implementation can diverge; the model is maintained separately and may not reflect recent implementation changes. A type-driven approach where the types are the spec and the types are in the same file as the implementation cannot drift in the same way—the spec is literally compiled alongside the code.

The economic argument is the practical enabler. Dependent type proof construction was always theoretically rigorous but practically slow; the manual labor cost exceeded the benefits for most production code. If AI assistance reduces the cost of proof construction by 10x, the economic calculation shifts for safety-critical code (compilers, cryptographic implementations, medical devices) where the cost of bugs substantially exceeds the cost of verification.
