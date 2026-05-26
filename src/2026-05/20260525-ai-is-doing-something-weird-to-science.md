# AI is doing something weird to Science
**Source**: https://blog.apiad.net/p/ai-is-doing-something-weird-to-science
**Date**: May 25, 2026
**Author**: Alejandro Piad Morffis
**Keywords**: AI, science, discovery loops, proposer-verifier, Claude Code, AlphaFold, GNoME, mathematics, scientific method

## Elevator pitch
AI isn't replacing scientists or just parroting tokens — the real breakthrough is the discovery loop where models propose, verifiers filter, and humans curate, a pattern that's been working since 1976 but is now accelerated by general-purpose LLMs.

## Takeaways
- The "AI did the science" vs "it's just a tool" debate misses the point: the discovery loop (poser → proposer → verifier → curator) is what matters
- Four cases demonstrate the same pattern: Claude's Cycles (Knuth), Tao and Lean, AlphaFold, GNoME/A-Lab — model proposes, independent verifier filters, human curates
- The loop is 50 years old: Appel and Haken's four-color theorem proof (1976), Hales' Kepler conjecture (1998-2014), AI Feynman (2020) all followed the same shape
- What changed in 2022: the proposer slot is now occupiable by general-purpose LLMs instead of domain-specific hand-engineered systems
- The model is never the verifier, never the question-poser — it occupies exactly one slot in the loop

## Synthesis
Alejandro Piad Morffis opens with a striking scene: Donald Knuth, the 88-year-old father of algorithmic analysis and known AI skeptic, reading a chat log between mathematician Filip Stappers and Claude Code. Stappers ran 31 systematic explorations of combinatorial objects; Exploration 15 surfaced a structural pattern nobody had documented. Knuth verified it, proved it by hand, and published a paper calling it "Claude's Cycles" — noting he'd have to revise his opinions about generative AI.

Piad uses this as a launching point to dissect the two dominant narratives around AI in science. The replacement narrative claims AI is now the scientist, automating discovery. The stochastic-parrot dismissal insists it's just token prediction with no understanding. Both are wrong, and both make the same mistake: they're asking "did AI do the science?" when the real question is about the discovery loop.

The loop has four roles: the poser (who asks the question), the proposer (who generates candidates), the verifier (who filters candidates), and the curator (who selects what survives). In Claude's Cycles, Stappers posed the questions, Claude proposed, Knuth verified by hand, and the mathematicians together curated. In Terence Tao's work with Lean, the LLM proposes proof steps, Lean's type-checker acts as an unforgiving verifier, and Tao curates which directions to pursue. AlphaFold proposes protein structures; experimental crystallography verifies them; human researchers curate which proteins matter. GNoME generated 380,000 candidate crystal structures; A-Lab's autonomous laboratory physically synthesized 58 of them, producing 41 novel materials in 17 days.

Piad traces this pattern back 50 years: Appel and Haken's 1976 computer-assisted proof of the four-color theorem (1,482 configurations verified mechanically), Hales' 1998 Kepler conjecture proof (formally verified 16 years later by Flyspeck), and AI Feynman's 2020 symbolic regression for recovering physics equations. The loop has always worked. What changed in 2022 is specifically the proposer slot: it's now occupiable by general-purpose LLMs instead of domain-specific, hand-engineered systems.

The key insight is that the model is never the verifier. The verifier is always something independent: a type-checker, a crystal, a physical experiment. The model occupies exactly one role — proposer — and that role benefits most from creativity, speed, and a high tolerance for being wrong. The breakthrough isn't that AI can do science; it's that the loop can now run fast enough and cheaply enough to be useful across domains without requiring bespoke proposer engineering for each one.
