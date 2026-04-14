# GitHub Stacked PRs

**Source**: https://github.github.com/gh-stack
**Date**: April 13, 2026
**Author**: GitHub
**Keywords**: GitHub, stacked PRs, developer workflow, code review, CLI, AI agents

## Elevator pitch
GitHub’s native stacked pull requests and `gh stack` CLI formalize a workflow that breaks large changes into reviewable layers, which is especially useful for AI-assisted coding where big diffs need structure, dependency tracking, and safe merge paths.

## Takeaways
- GitHub now treats stacks as a first-class review concept, showing relationships between dependent PRs and handling rebases and merges across the chain.
- The `gh stack` CLI manages the local mechanics of creating branches, pushing layers, and submitting ordered pull requests with the correct bases.
- GitHub is explicitly pitching the workflow for AI coding agents, since stacks turn large machine-generated diffs into smaller reviewable units.

## Synthesis
This launch is less about a new CLI and more about GitHub acknowledging that modern software work often happens in layered changes rather than single monolithic pull requests. Stacked PR workflows have existed in tools like Graphite and internal developer setups for years, but native support matters because it reduces the friction of adopting the pattern across normal GitHub repositories. Reviewers can now reason about a change as a sequence of focused layers instead of one giant diff that mixes refactors, API changes, and UI updates.

That matters even more in the age of coding agents. Agents are good at producing a lot of code quickly, but they often create diffs that are technically coherent and socially hard to review. Stacks are a practical answer: split one ambitious change into a dependency chain where each PR has a narrow purpose and can be validated independently. This improves review quality, keeps CI and merge queues manageable, and reduces the cost of backing out one layer without discarding the whole effort.

The deeper signal is that development platforms are adapting to agentic coding by building workflow primitives around reviewability and context, not just generation. If AI increases throughput, the bottleneck shifts to trust, comprehension, and merge safety. Native stacked PRs are one of the clearest examples of product infrastructure evolving around that new constraint.
