# The Building Block Economy

**Source**: https://mitchellh.com/writing/building-block-economy
**Date**: April 8, 2026
**Author**: Mitchell Hashimoto
**Keywords**: AI, agents, software development, open source, product strategy, building blocks, Ghostty

## Elevator pitch
Mitchell Hashimoto argues that AI shifts software leverage away from polished monolithic apps and toward high-quality building blocks, because agents are especially good at recombining documented primitives into many niche applications.

## Takeaways
- Hashimoto distinguishes “building blocks” from classic libraries because the pattern now spans frameworks, apps, and forkable components.
- He argues agentic development massively increases software output and especially favors composing existing parts over inventing everything from scratch.
- This lowers the value of shipping every feature in a mainline product and raises the value of offering stable primitives others can extend.
- He sees side benefits for maintainers: more outsourced R&D, easier refusal of niche feature requests, and broader awareness through derivative projects.
- The unresolved pressure point is commercialization, since agents currently prefer open and free components over closed commercial alternatives.

## Synthesis
Hashimoto is describing a real strategic inversion in software. Historically, success often came from owning the full polished application and minimizing the need for users to assemble anything themselves. In his framing, AI changes that because the expensive part is no longer gluing things together. Agents are increasingly competent at composition, adaptation, and local customization, especially when the inputs are well documented and already proven.

That pushes value toward robust primitives. A building block can spread farther than a single flagship app because it can participate in many downstream products, forks, and workflows. Hashimoto’s Ghostty/libghostty example captures this: the core component may end up with far greater aggregate reach than the branded mainline application built on top of it.

This also changes the maintainer’s job. Instead of trying to satisfy every niche from the center, the maintainer can stabilize interfaces, improve documentation, and let the ecosystem explore the edge cases. AI effectively subsidizes experimentation by making it cheaper for others to test ideas and ship variants. That turns the ecosystem into a distributed R&D engine.

The hard commercial question remains unsolved, but the product lesson is already useful: in an AI-native market, defensibility may come less from feature completeness and more from being the component agents reliably choose to assemble around. That favors open, well-documented, composable systems and suggests many “applications” will increasingly function as reference implementations for larger block economies.
