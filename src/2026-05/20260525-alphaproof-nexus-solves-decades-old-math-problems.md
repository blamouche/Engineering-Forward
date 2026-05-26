# Google DeepMind's AlphaProof Nexus Solves Decades-Old Math Problems for a Few Hundred Dollars
**Source**: https://the-decoder.com/google-deepminds-alphaproof-nexus-solves-decades-old-math-problems-for-a-few-hundred-dollars/
**Date**: 2026-05-25
**Author**: Matthias Bastian
**Keywords**: AlphaProof Nexus, DeepMind, Erdős problems, formal verification, Lean, LLM agents, automated theorem proving, Gemini 3.1 Pro

## Elevator pitch
DeepMind's AlphaProof Nexus used Gemini 3.1 Pro and Lean formal verification to autonomously solve 9 of 353 Erdős problems — including two unanswered for 56 years — at just a few hundred dollars per problem, while also proving 44 OEIS conjectures and contributing to ongoing quantum optics and graph theory research.

## Takeaways
- AlphaProof Nexus combines an LLM (Gemini 3.1 Pro) generating proof steps in Lean with compiler feedback loops — the Lean compiler catches errors and feeds them back for correction, grounding the LLM's reasoning.
- Four agent variants of increasing complexity were tested: the simplest (LLM + compiler only) surprisingly solved all nine problems too, suggesting a trend away from specialized systems toward simple agentic loops as base models improve.
- The system also proved 44 of 492 OEIS conjectures, settled a 15-year-old Hilbert functions question, and improved a convex optimization bound.
- Even failed proof attempts proved valuable — mathematicians reported they deepened understanding, and formal verification allowed focusing on unsolved sub-goals without re-checking entire arguments.
- Success rate on Erdős problems is ~2%, concentrated in combinatorics and number theory where Lean's Mathlib is mature; harder problems requiring new theory remain out of reach.

## Synthesis
DeepMind's AlphaProof Nexus represents a pragmatic approach to AI mathematics: rather than betting on an LLM to carry entire logical chains in natural language (as OpenAI has done with GPT-5.x solving Erdős problems), it uses formal verification as a safety net. Gemini 3.1 Pro generates proof steps in Lean's formal language, the compiler checks each one, and errors feed back into the next attempt. This architecture offsets the well-known logical weaknesses of language models while producing machine-checkable results.

The system's four-agent hierarchy is instructive. Agent (A) is the simplest — just an LLM generating proof steps with compiler feedback. Agent (B) adds AlphaProof, DeepMind's RL-based olympiad math system, to fill in missing segments. Agent (C) introduces evolutionary search with Elo-rated proof sketches. Agent (D) combines everything. The surprising post-hoc finding: Agent (A) could also solve all nine Erdős problems, though at higher cost for the hardest ones. The researchers frame this as evidence of "an ongoing shift from specialized trained systems toward simple agentic loops as LLMs become more capable" — a thesis with implications far beyond mathematics.

The numbers are striking but sobering. Nine out of 353 Erdős problems, 44 out of 492 OEIS conjectures — roughly a 2% success rate. This aligns with Terence Tao's assessment that AI's actual Erdős success rate sits at one to two percent, concentrated on easier problems in mature domains. The system also inherits the unreliability of its underlying LLM.

But the paper argues for value beyond solved problems. Mathematicians collaborating with the system reported that even failed proof attempts deepened their understanding, because the formal sketches let them focus on unsolved sub-goals. The agents also caught flawed formalizations in the literature, and the system is already deployed in active quantum optics and graph theory research. This positions AlphaProof Nexus less as a math-replacing oracle and more as a research amplifier — a tool that makes mathematicians more productive rather than obsolete.
