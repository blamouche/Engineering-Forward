# Agentic Engineering Patterns

**Source**: https://simonwillison.net/guides/agentic-engineering-patterns
**Date**: Unknown
**Author**: Simon Willison
**Keywords**: agentic engineering, Claude Code, Codex, coding agents, TDD, subagents, git, prompt engineering, patterns

## Elevator pitch
Simon Willison's comprehensive guide to getting the best results from coding agents like Claude Code and Codex, covering principles, patterns, anti-patterns, testing, and practical prompt examples.

## Takeaways
- Agentic engineering is distinct from "vibe coding"—it requires discipline, good habits, and understanding how coding agents actually work under the hood
- Code is cheap now, but good code still has a cost: agents help avoid technical debt when used correctly, and can explore more options than humans can in the same time
- Key patterns: hoarding (building a library of working examples and templates), red/green TDD (write failing tests first), and parallel/specialist subagents for complex tasks
- Using Git with coding agents is critical: commit frequently, use branches, understand how to rewrite history to clean up agent-generated commits
- Anti-patterns to avoid: inflicting unreviewed code on collaborators, letting agents accumulate technical debt, skipping tests

## Synthesis
Simon Willison's Agentic Engineering Patterns guide is one of the most practically useful references for software engineers learning to work effectively with AI coding agents. Rather than treating agent delegation as magic or as a simple productivity multiplier, it approaches the topic as a craft with specific principles, techniques, and failure modes.

The guide opens with an important distinction: agentic engineering is not vibe coding. Vibe coding—just describing what you want and accepting whatever output the agent produces—is fine for personal projects but produces unreliable, unreviewed code that shouldn't be inflicted on collaborators or production systems. Agentic engineering applies discipline to agent delegation: clear requirements, tests, review, and an understanding of the agent's actual behavior.

Central to the guide is the insight that code is cheap now but good code still has a cost. AI agents can generate enormous amounts of code quickly, but poor code still accumulates technical debt, introduces bugs, and creates maintenance burdens. The good news: agents can also help eliminate technical debt by handling the kinds of tedious cleanup tasks that engineers often skip due to time pressure. They can also explore multiple implementation options in parallel, finding better solutions than any single human could evaluate in the same time.

The hoarding pattern is particularly valuable. Willison recommends building a library of working examples—prompts that produced good code, templates for common patterns, examples of successful agent interactions. Coding agents make this more powerful: you can recombine elements from your hoard in natural language prompts, and the agent synthesizes them into new solutions. The library grows faster with agents because every successful delegation is a potential template.

Red/green TDD is the most powerful testing pattern in the guide. Write a failing test first. Tell the agent to make the test pass without modifying it. This gives the agent a clear, verifiable success criterion and catches regressions automatically. Combined with "first run the tests" (always confirm the test suite passes before starting agent work), this provides a robust quality floor.

The subagents section covers both Claude Code's Explore subagent (for codebase exploration) and patterns for spawning parallel and specialist subagents. Parallel subagents can explore multiple implementation approaches simultaneously; specialist subagents can be given narrow, well-defined tasks within a larger orchestration.

Git integration is non-negotiable. The guide covers committing frequently, branching for experimental work, and rewriting history to clean up agent-generated commit chains before merging. Agents tend to commit at irregular intervals with verbose messages; cleaning this up before sharing code with collaborators is a basic courtesy.

For anyone building or reviewing code with AI assistance, this guide establishes the baseline practices that separate professional agentic engineering from undisciplined vibe coding.
