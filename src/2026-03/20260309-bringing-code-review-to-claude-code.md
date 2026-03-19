# Bringing Code Review to Claude Code
**Source**: https://claude.com/blog/code-review
**Date**: 2026-03-09
**Author**: Anthropic
**Keywords**: Code review, AI agents, pull requests, bug detection, software development, Claude Code, multi-agent

## Elevator pitch
Anthropic launches Code Review, a multi-agent system that automatically reviews pull requests to catch bugs human reviewers often miss, now available in research preview for Team and Enterprise customers.

## Takeaways
- Problem Context: Code productivity has grown 200% annually at Anthropic, making human code review a significant bottleneck with many PRs receiving only cursory attention.
- Internal Success Metrics: Running the system internally increased substantive review comments from 16% to 54% of PRs, with less than 1% of findings marked as incorrect by engineers.
- Parallel Agent Architecture: The system dispatches multiple agents simultaneously to identify bugs, verify findings to reduce false positives, and rank issues by severity.
- Cost Structure: Reviews average $15-25 per PR, with pricing tied to token usage and PR complexity, featuring organization caps and repository-level controls for cost management.
- Real-World Impact: The system identified critical production bugs that would likely have escaped human review, including authentication failures and latent type mismatches in adjacent code.

## Synthesis
Anthropic's Code Review represents a practical application of AI agents to address a genuine operational challenge: as development velocity increases, traditional code review processes struggle to maintain depth and consistency. The system is "built for depth, not speed," reflecting the company's apparent philosophy of thorough verification over expedience.

The mechanism relies on distributing review tasks across multiple agents working in parallel, similar to how human review teams would approach complex changesets. By separating bug detection from verification, the system reduces false positives that might otherwise reduce developer trust. The 54% increase in substantive comments—compared to the baseline 16%—suggests the tool surfaces findings that human reviewers often overlook, potentially due to fatigue or time constraints.

Notably, the system doesn't supplant human judgment; it prepares better conditions for it. Engineers retain final approval authority, and the tool's role is to "close the gap so reviewers can actually cover what's shipping." This positioning acknowledges the irreducible human role in software governance while automating labor-intensive pattern detection.

The pricing model ($15-25 per review) and administrative controls reflect enterprise-grade thinking. Organizations can set monthly caps and enable reviews selectively, addressing concerns about runaway costs. The average 20-minute review duration suggests the system conducts substantive analysis rather than superficial checks.

Real-world examples—including a ZFS encryption issue in TrueNAS middleware that represented a "latent issue" in adjacent code—demonstrate the system's value in detecting problems beyond the immediate changeset scope. This broader contextual awareness may reflect Claude's training and reasoning capabilities applied to code semantics.

The research preview status suggests Anthropic is gathering feedback before general availability, with the tool currently available for Team and Enterprise tiers. The system models processes "we run on nearly every PR at Anthropic," positioning it as battle-tested internal infrastructure now offered externally. For engineering organizations scaling their AI-assisted development, Code Review represents a meaningful step toward automated quality assurance that integrates with existing workflows rather than demanding their replacement.
