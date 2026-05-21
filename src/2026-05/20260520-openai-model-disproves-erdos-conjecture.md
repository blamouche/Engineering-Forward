# An OpenAI Model Has Disproved a Central Conjecture in Discrete Geometry
**Source**: https://openai.com/index/model-disproves-discrete-geometry-conjecture/
**Date**: 2026-05-20
**Author**: OpenAI
**Keywords**: OpenAI, mathematics, Erdős, unit distance problem, discrete geometry, algebraic number theory, AI reasoning, AI proof

## Elevator pitch
An OpenAI general-purpose reasoning model has autonomously disproved a nearly 80-year-old conjecture by Paul Erdős in discrete geometry, marking the first time AI has independently resolved a prominent open problem central to a subfield of mathematics — using unexpected connections from algebraic number theory that surprised human experts.

## Takeaways
- The model disproved Erdős's 1946 unit distance conjecture, which held that the square grid construction was essentially optimal for maximizing unit-distance pairs among n points in a plane
- The AI proof constructs configurations achieving at least n^(1+δ) pairs for δ>0, beating the previous best n^(1+C/log log n) bound — a polynomial improvement
- The proof was checked by external mathematicians including Fields medalist Tim Gowers, who called it "a milestone in AI mathematics"
- The method was surprising: it applied sophisticated algebraic number theory (class field towers, Golod-Shafarevich theory) to an elementary geometric question
- The model was a general-purpose reasoning system, not specialized for math — tested on a collection of Erdős problems as part of evaluating frontier reasoning capabilities

## Synthesis
OpenAI has announced a landmark result in AI-assisted mathematics: an internal reasoning model has independently disproved a conjecture by Paul Erdős that stood for nearly 80 years. The planar unit distance problem — how many pairs of n points in a plane can be exactly distance 1 apart — is one of the most famous open questions in combinatorial geometry, described as "possibly the best known problem" in the field.

The prevailing belief, held since Erdős's original 1946 work, was that constructions based on rescaled square grids were essentially optimal, achieving growth of n^(1+C/log log n) — only slightly faster than linear. The AI proof constructs infinite families of configurations with at least n^(1+δ) unit-distance pairs for a fixed δ>0 (a forthcoming refinement by Princeton's Will Sawin gives δ=0.014), representing a genuine polynomial improvement.

What makes this particularly significant is threefold. First, the model was a general-purpose reasoning system, not a mathematics-specific architecture or one scaffolded with proof-search strategies — suggesting frontier reasoning capabilities are becoming broadly applicable. Second, the proof imported sophisticated tools from algebraic number theory — class field towers, Golod-Shafarevich theory — into discrete geometry, an unexpected bridge that surprised domain experts. Third, the proof has been validated by external mathematicians including Tim Gowers, Noga Alon, and Arul Shankar, with a companion paper providing context.

The broader implication extends beyond this single result: as Thomas Bloom notes in the companion remarks, this demonstrates that AI can reveal "unexpected connections and push existing technical machinery to its limit" across mathematics. OpenAI frames this as evidence that AI is entering a phase where it can serve as a genuine research partner — capable of holding together difficult arguments, connecting distant knowledge areas, and surfacing paths human experts might not prioritize. The company explicitly ties this to urgency around understanding and aligning increasingly capable reasoning systems.
