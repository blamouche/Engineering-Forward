# Google Engineers Launch "Sashiko" For Agentic AI Code Review Of The Linux Kernel
**Source**: https://www.phoronix.com/news/Sashiko-Linux-AI-Code-Review
**Date**: 2026-03-18
**Author**: Michael Larabel
**Keywords**: Sashiko, Linux kernel, code review, AI, Google, Gemini Pro, open source, automated code review, Roman Gushchin

## Elevator pitch
Sashiko, Google's open-source agentic AI system for Linux kernel code review, found 53% of bugs in a sample of 1,000 recent upstream issues that human reviewers missed—serving as an augmentative layer rather than a replacement for expert review.

## Takeaways
- Found 53% of bugs from a completely unfiltered set of 1,000 recent upstream Linux kernel issues—with human reviewers having missed all identified bugs.
- Built for Google Gemini Pro 3.1 but compatible with Claude and other LLMs.
- Google funds token usage and infrastructure; project transitioning to Linux Foundation for hosting.
- Design philosophy: augmentative layer catching defects that escape peer review, not a replacement for human judgment.
- Code available on GitHub; web interface at Sashiko.dev.

## Synthesis
A 53% bug detection rate on human-missed issues in production Linux kernel code is a substantial result, particularly given the difficulty of the domain. Linux kernel patches undergo rigorous human review from experienced engineers who deeply understand the codebase. Finding bugs that these experts missed suggests the AI system brings a different perspective—likely finding different categories of bugs than humans, rather than simply being more thorough at the same checks.

The "augmentative layer" framing is appropriate and important for adoption. Replacing human code review with AI review would face cultural resistance from open source maintainers who have strong opinions about review quality and autonomy. Positioning Sashiko as additional review that runs before or alongside human review—catching issues that would otherwise slip through—creates value without threatening the existing review culture.

The Linux Foundation transition for hosting signals intent to make this a community resource rather than a Google-owned tool. Open source communities are appropriately cautious about infrastructure owned by single large companies; Linux Foundation governance provides the independence and longevity commitment that would make maintainers willing to depend on Sashiko for their review process.

The multi-LLM compatibility (Gemini Pro 3.1 primary, Claude and others supported) is important for community trust. If Sashiko required Google's proprietary model, the community would be dependent on Google's continued investment in both the tool and the model. Supporting multiple backends allows the community to switch models as capabilities evolve or if governance concerns emerge.
