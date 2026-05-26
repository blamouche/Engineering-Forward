# Introducing BenchBench
**Source**: https://www.strangeloopcanon.com/p/introducing-benchbench
**Date**: 2026-05-25
**Author**: Rohit Krishnan
**Keywords**: AI benchmarks, GPT-5.2, model evaluation, benchmark creation, model self-awareness, creativity testing, BenchBench

## Elevator pitch
Rohit Krishnan introduces BenchBench — a meta-benchmark where AI models must create benchmarks that defeat other frontier models — revealing that GPT-5.2 alone succeeds, while GPT-5.5 and Opus 4.6 are surprisingly timid creators despite being excellent solvers.

## Takeaways
- GPT-5.2 is the only model to produce a genuinely hard and solvable benchmark (Reimbursement Forensics: calculating total reimbursable cents from messy expense packets).
- GPT-5.5 and Opus 4.6 — the consensus top models — were "timid and useless" as benchmark creators: either too easy or unsolvable puzzles, revealing poor self-awareness of their own capabilities.
- Gemini 3.1 Pro is the most creatively interesting creator (spatial traversal, corrupted recovery, lease CAM reconciliation) but extremely brittle.
- BenchBench measures capabilities invisible to standard benchmarks: creativity, self-knowledge, and the gap between Creator vs. Solver roles — which are not highly correlated.
- The meta-benchmark approach could enable automated discovery of new evaluation dimensions and RL environments for hill-climbing.

## Synthesis
Rohit Krishnan's BenchBench is a clever meta-benchmark born from a real problem: AI models are saturating existing benchmarks faster than humans can create new ones. The natural next step is to test whether models themselves can generate challenging evaluations — and the results reveal a fascinating capability gap.

The experiment is straightforward: give each frontier model a report of all existing benchmarks, then ask it to design a new one that would defeat other frontier models while remaining practically solvable. Models that fail get feedback and another attempt. Only GPT-5.2 succeeded, producing "Reimbursement Forensics" — a task requiring models to calculate total reimbursable amounts from messy travel expense packets riddled with voided receipts and duplicates.

The most striking finding is the divergence between Creator and Solver capabilities. GPT-5.5 and Claude Opus 4.6, widely considered the strongest general-purpose models, were ineffective benchmark designers. They either created problems too easy for frontier models (but hard for smaller ones — suggesting they don't know their own strength) or produced unsolvable puzzles. This points to a self-awareness gap: the models can solve hard problems but can't accurately model what would be hard for versions of themselves.

Gemini models emerged as the most creative creators — Gemini 3.1 Pro produced spatial traversal tasks and corrupted recovery problems with genuinely novel mechanisms — but their brittleness made them unreliable. Krishnan's affection for Gemini is palpable ("I really really like this model and wish Google would do it justice"), echoing a common sentiment that Google's models have untapped potential constrained by their deployment harness.

BenchBench also reveals a thematic convergence: all models gravitated toward "bureaucratic forensics" — real-world messy situations involving policies, compliance, and reimbursement rules. This reflects the training data these models are built on, but also hints at where frontier labs see the economic opportunity: navigating organizational complexity rather than solving abstract puzzles.

The project is open-source on GitHub and Krishnan invites community scaling. The long-term vision is provocative: if models can generate benchmarks that reveal their own weaknesses, those benchmarks become RL training environments, creating a feedback loop where AI systems help design the tests that improve them.
