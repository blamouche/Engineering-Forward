# claude-ground: Modular Rules & Skills System for Claude Code
**Source**: https://github.com/akinalpfdn/claude-ground
**Date**: 2026-03-06
**Author**: akinalpfdn
**Keywords**: Claude Code, rules system, coding workflow, AI coding, workflow management, best practices, CLAUDE.md, developer tooling

## Elevator pitch
claude-ground provides a structured rule and skills system for Claude Code that enforces disciplined coding practices, addressing common behavioral gaps like losing track of plans, inadequate testing, and poor code modification habits.

## Takeaways
- Phase-based workflow management that survives context resets—ensuring Claude doesn't lose track of multi-step plans mid-session.
- Decision logging system captures reasoning behind implementation choices for future reference.
- Language-specific best practices for Go, Swift, TypeScript, Kotlin, Flutter, Rust, Python, .NET, and Spring.
- Common rules covering git workflows, testing discipline, debugging, and frontend design.
- Severity-level tagging (MUST/SHOULD/RECOMMENDED) distinguishes hard constraints from guidance.
- Global rule installation with per-project template setup; 97 stars at time of review, 9 commits.

## Synthesis
claude-ground addresses a gap that emerges when using Claude Code for multi-step, multi-session projects: the model's behavior can drift between sessions, priorities shift without documentation, and per-language best practices aren't enforced consistently. The CLAUDE.md convention in Claude Code provides the mechanism; claude-ground provides the structured content to put in it.

The phase-based workflow management is the most practically valuable feature. Long coding tasks that span multiple Claude invocations face a specific failure mode: each new context window starts fresh, and without explicit structure the agent may retrace steps, change approaches mid-task, or lose track of decisions made in earlier phases. Externalizing phase state into the rule system rather than relying on context memory directly addresses this.

The severity tagging system (MUST/SHOULD/RECOMMENDED) mirrors how engineering organizations think about standards—distinguishing non-negotiable constraints from preferred practices from optional guidance. This matters because overly prescriptive rules in every category create rigidity that prevents Claude from adapting to task-specific requirements. Tiered severity lets developers express priorities rather than just policies.

The language-specific rule sets reflect accumulated community knowledge about where Claude tends to deviate from idiomatic patterns in each ecosystem. TypeScript and Python rules likely diverge significantly given the different type systems, testing cultures, and tooling conventions. Centralizing this in a sharable format creates a commons for Claude Code workflows that individual teams would otherwise reinvent independently.
