# Design Engineering with Maggie Appleton
**Source**: The Pragmatic Engineer (pragmaticengineer@substack.com)
**Date**: 2026-09-24
**Author**: Gergely Orosz (The Pragmatic Engineer)
**Keywords**: Maggie Appleton, design engineering, GitHub Next, AI agents, notebooks, jigs, capability gaslighting, Figma, Elicit, frontend, anthropology, vibe coding, AI tells

## Elevator pitch
Maggie Appleton — staff research engineer at GitHub Next, former first designer at Elicit, and one of the industry's best design engineers — shares how design processes are adapting to AI: why notebooks beat Claude Code for early ideation, why she stopped looking at generated PRs, the concept of "capability gaslighting" when models impress then fail, and why we need new artifacts for human-agent collaboration.

## Takeaways
- **Notebooks outlast prompts**: Maggie starts projects by sketching in a physical notebook because the idea is still there the next day. With Claude Code, dozens of prompts later, it's hard to go back to the original idea.
- **Jigs as personal Figma**: She regularly asks coding agents to build prototypes with sliders and color pickers for real-time tweaking — named after the woodworking device that helps with a specific job.
- **She stopped looking at generated code**: When a PR is generated, she doesn't review the code — appropriate for prototypes where she defines detailed specs and the agent verifies its own work.
- **Planning with AI agents breaks with too much text**: "An agent grills you with choice A, B, or C questions a hundred times over. By question 20, your brain starts shutting down." The recommended option becomes the path of least resistance.
- **"Capability gaslighting"**: Maggie coined the term for when frontier models convince users they're experts but fail the same task the next day. We keep believing because we're convinced they're capable — vigilance is required.
- **Familiar primitives beat novel interfaces**: At Elicit in 2021, months of work on an innovative AI UI (infinite canvases, composable documents) failed because researchers wanted simple tables they already knew.
- **New artifacts needed for human-agent collaboration**: "There's a world agents live in: weights, models, skills, MCPs. Then you have your human side: physicality, texture, light, materials. Finding artifacts that allow us to meet in the middle is a really hard challenge."
- **Engineers can use AI as a design tutor**: Agents are good at explaining when to change line height, what a good sidebar looks like, how many characters per line — acquiring product design skills is now easier.

## Synthesis
This conversation is a rare bridge between design practice and AI-native development. Maggie Appleton occupies a unique position: she's both a designer who understands engineering constraints and an AI researcher building prototypes at GitHub Next. Her observations cut through the hype because they come from daily practice, not theory.

The notebook-vs-prompt insight is deceptively important. It's not nostalgia for analog tools — it's a recognition that AI tools currently optimize for iteration speed at the cost of idea persistence. When you sketch in a notebook, the idea is fixed and retrievable. When you iterate with Claude Code, the idea evolves (or drifts) with every prompt, and the original intent becomes hard to recover. This has real consequences for creative work where the initial vision matters.

"Capability gaslighting" is the most quotable concept, and it names a problem the industry has been dancing around. Models that impress on first encounter and fail on second create a trust pattern that's corrosive: users keep believing because the impressive moments are vivid and the failures are explainable away. For agent-based workflows where consistency matters more than peak performance, this is a critical design challenge.

The call for new artifacts — things that let humans and agents "meet in the middle" — points to an unsolved problem in AI-native tooling. Current interfaces are either human-optimized (Figma, notebooks) or agent-optimized (code, APIs). The gap between physicality and weights is where the next generation of collaborative tools needs to live.