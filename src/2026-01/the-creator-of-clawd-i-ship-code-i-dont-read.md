# The Creator of Clawd: "I Ship Code I Don't Read"

**Source**: https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code

**Date**: January 28, 2026

**Author**: Gergely Orosz

**Keywords**: AI agents, software development, productivity, workflow, Claude Code, Codex, architecture, code review

## Elevator pitch

Peter Steinberger demonstrates that individual developers can operate at team scale by centering workflows around AI agents, shipping code without reading it while maintaining sophisticated architectural thinking and directional governance over automated implementation.

## Takeaways

- Steinberger's Moltbot has become the fastest-growing GitHub repository, attracting more searches than Claude Code or Codex combined
- Managing 70+ people taught him to accept code that doesn't match personal preferences, a skill essential when collaborating with AI agents
- Pull requests become prompt requests: reviewing the prompts that generated code matters more than the code itself
- AI agents must operate in closed-loop systems where they can verify their own work through compilation, linting, and execution
- Outcome-oriented engineers who value shipped products thrive with AI-native approaches while algorithm enthusiasts struggle with the transition

## Synthesis

Gergely Orosz profiles Peter Steinberger, whose AI-driven development workflow has produced Moltbot, the fastest-growing repository on GitHub. The approach challenges conventional software engineering practices while revealing sophisticated thinking about how humans and AI agents should collaborate on code production.

Steinberger's central claim is provocative: he ships code without reading it. This statement requires context. His experience managing over 70 employees at PSPDFKit taught him to accept code that doesn't match personal preferences. This organizational skill translates directly to AI collaboration, where agents produce functional but potentially unfamiliar implementations. The transition from writing code to directing code generation requires abandoning perfectionism about implementation details.

The workflow operates on several key principles. AI agents must function in closed-loop systems where they can verify their own work through compilation, linting, execution, and self-validation. Steinberger queues 5-10 agents simultaneously, maintaining productive flow across different features. He invests significant time iterating with agents on solid plans before execution, preferring Codex for its sustained task focus over Claude Code's tendency toward interruptions. Strategic vagueness in prompts intentionally lets AI explore solutions beyond predetermined directions.

The implications for code review are substantial. Steinberger reframes pull requests as prompt requests, prioritizing the prompts that generated code over the code itself. Team discussions focus on high-level architecture rather than implementation details. This reflects his view that most application code involves data transformation unworthy of obsessive attention; engineering energy belongs on system design. Running tests locally through agents beats remote CI pipelines to avoid infrastructure waiting times.

The profile reveals a crucial distinction: Steinberger isn't abandoning software engineering but practicing sophisticated architectural thinking while delegating implementation to agents. His extensible bot design and directional governance demonstrate that human judgment remains central to AI-augmented development. The approach works best for outcome-oriented engineers who value shipped products over algorithmic elegance. Those who derive satisfaction from personally crafting solutions struggle with this transition. The broader implication is that AI-native development may amplify existing differences in engineering motivation and reward structures, favoring those who measure success by impact rather than code quality.
