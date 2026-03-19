# The Science of Why AI Still Can't Write Like You
**Source**: https://every.to/p/the-science-of-why-ai-still-can-t-write-like-you
**Date**: 2026-03-12
**Author**: Marcus Moretti
**Keywords**: writing style, stylometry, AI writing, voice, subconscious language, ChatGPT, Spiral, author attribution

## Elevator pitch
AI writing remains detectable and generically polished because the most distinctive elements of writing style—the unconscious words—emerge from habits authors don't deliberately choose, making them nearly impossible to replicate in post-trained models optimized for generic quality.

## Takeaways
- The most distinctive writing characteristics emerge from words writers don't consciously choose: articles, pronouns, and function words that follow recognizable patterns as authors focus on content meaning.
- Stylometry has deep historical roots: Hamilton's contributions to the Federalist Papers were identified largely on the presence of the word "upon"—subconscious lexical habits as authorial fingerprints.
- Post-training refinement makes AI generic: models trained for helpfulness and safety develop "generic politeness" that systematically removes idiosyncratic stylistic variation.
- Ted Chiang's formulation: "ChatGPT is a blurry JPEG of the web"—capturing approximations rather than precise individual expression.
- Cornell research systematically removed text attributes to measure their impact on author attribution accuracy, identifying which elements AI most struggles to replicate.

## Synthesis
The core insight here is about where style actually lives, and it's counterintuitive: style isn't primarily in the choices authors consciously make (vocabulary, sentence structures, rhetorical devices) but in the habits they don't notice. Function words—the, a, of, that, which—appear so frequently and so automatically that authors never think about them. Yet these invisible choices are more individually consistent than any deliberate stylistic decision.

This is structurally different from how most AI writing enhancement tools approach the problem. They focus on tone, complexity, formality, vocabulary range—the features that writers can consciously describe about their style. But the subconscious lexical habits are precisely what can't be described, because the author doesn't know they have them. You can't instruct a model to replicate habits you're unaware of.

Post-training makes this worse. RLHF and similar fine-tuning processes reward outputs that seem helpful, clear, and polished to diverse raters. This systematically selects against idiosyncratic variation—the quirks that make individual writing recognizable. The result is a model that writes competently but blandly, exactly as Chiang's "blurry JPEG" metaphor suggests: resolution lost in the compression.

The implication for tools like Spiral (whose general manager wrote this article) is that replicating individual style probably requires extended exposure to the individual's actual writing—building a model of their specific function word distributions rather than their described preferences. This is technically feasible but requires data collection that most users won't provide, and raises questions about data ownership and privacy that complement tools haven't fully resolved.
