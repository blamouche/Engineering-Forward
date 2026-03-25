# A Ramsey-style Problem on Hypergraphs
**Source**: https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs
**Date**: Unknown
**Author**: Unknown
**Keywords**: FrontierMath, hypergraphs, Ramsey theory, AI math, open problems

## Elevator pitch
Epoch’s FrontierMath page documents an open hypergraph Ramsey-style problem that has now been solved with AI assistance, detailing the construction goal, evaluation scaffold, and follow‑up validation by a human contributor.

## Takeaways
- The problem seeks improved lower bounds for a hypergraph partition function H(n).
- Epoch reports the problem as solved using GPT‑5.4 Pro, later confirmed by the contributor.
- The solution removes inefficiency in earlier constructions and matches upper bounds more tightly.
- FrontierMath now includes scaffolding to test multiple models on the same problem.
- The page includes transcripts, prompts, and metadata for reproducibility.

## Synthesis
Epoch’s FrontierMath “Open Problems” entry presents a Ramsey‑style hypergraph problem focused on improving lower bounds for a sequence H(n), defined via hypergraphs that avoid large partitions. The task: construct hypergraphs with many vertices, no isolated vertices, and no partitions of size greater than n, thereby pushing the lower bound for H(n). The entry lays out three tiers of difficulty—warm‑up (with known constructions), a single challenge for an unsolved n, and a full problem that asks for a general algorithm.

The page includes a notable update: the problem has now been solved. Epoch reports that a solution was first elicited by Kevin Barreto and Liam Price using GPT‑5.4 Pro. The solution was verified by the original contributor, Will Brian, who described it as eliminating inefficiencies in the previous lower‑bound construction and mirroring the structure of the upper‑bound argument. The update suggests that the solution is strong for Ramsey‑theoretic problems, and that Brian plans to write it up for publication, with potential coauthorship for the AI‑assisted solvers.

Beyond the headline result, the page is structured as a reproducibility artifact. It links to transcripts of the GPT‑5.4 Pro interaction and the model’s final write‑up, along with later runs using other systems (Opus 4.6, Gemini 3.1 Pro, and GPT‑5.4 xhigh) in an updated evaluation scaffold. This scaffolding formalizes the prompting, constraints, and verification process for the FrontierMath Open Problems suite, indicating a shift toward standardized benchmarks for model‑assisted mathematics.

The entry also defines the problem in full technical detail. It specifies the hypergraph partition property, the function H(n), and the known recursive lower bound k_n, then asks for a constant‑factor improvement with an algorithmic construction. The evaluation prompt is explicit, requiring a Python function that outputs a hypergraph representation as a string and runs within practical time limits.

Overall, the page is both a problem statement and a milestone report: it documents a previously open mathematical challenge, the AI‑assisted path to a solution, and a framework for systematically testing models on similar problems. The combination of full prompt transparency, linked transcripts, and a verified human confirmation positions this as a well‑documented example of AI contributing to mathematical discovery in a bounded, verifiable setting.
