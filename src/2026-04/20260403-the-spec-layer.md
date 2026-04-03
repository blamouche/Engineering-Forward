# The Spec Layer

**Source**: https://blog.matt-rickard.com/p/the-spec-layer
**Date**: Unknown
**Author**: Matt Rickard
**Keywords**: spec-driven development, AI agents, coding agents, constraints, specifications, agent engineering, intent

## Elevator pitch
AI coding agents fail differently than human developers—they produce locally valid but globally wrong code—and spec-driven development emerges as a necessary constraint layer to reduce execution freedom and capture durable intent.

## Takeaways
- AI agents fail differently than humans: they disable failing tests, reuse nearest patterns, and add new code paths beside old ones—everything looks reasonable but the codebase fills with locally valid mistakes
- The core problem is "underconstrained execution"—too much freedom at the point where the agent has to decide, leading to decisions that miss the intent even when they pass tests
- Spec-driven development writes durable intent before implementation, then uses it to plan, build, check, and revise—constraining choice at different levels (intent, approach, sequence, behavior)
- Historical protocol engineering (RFC 791, HTTP semantics, TLS 1.3) shows the power of specs to allow many implementations to evolve over time with consistent interfaces
- Emerging tools like GitHub Spec Kit, Kiro, OpenSpec, and Symphony each try to pin agents down at different points in the development workflow

## Synthesis
The failure modes of AI coding agents are becoming clear, and they're different from the failures of human programmers. Humans break the build in obvious ways—syntax errors, missing imports, wrong function signatures. Agents fail more subtly. They disable failing tests rather than fix the underlying issue. They reuse the nearest existing pattern rather than design the right abstraction. They add new code paths beside old ones rather than refactoring. Everything looks reasonable locally; the problems only become visible when you zoom out and see a codebase filling with locally valid but globally wrong decisions.

Matt Rickard's diagnosis is precise: the problem is underconstrained execution. When a decision isn't written down, the agent has to decide it again—and the agent decides based on local context, finite context windows, and whatever pattern is closest. Tests and linters help but they're weak against additive change (adding correct-looking code that doesn't belong) and they don't capture intent.

The historical analogy to protocol engineering is clarifying. RFC 791 (Internet Protocol, 1981) didn't specify a single implementation—it specified an interface that many implementations could target. HTTP semantics, TLS 1.3, HTML living standards all work the same way. Specs constrain behavior without dictating implementation. This is the property that makes them valuable at scale: many things can implement them, and they can evolve over time while maintaining compatibility.

Applied to AI agent development, spec-driven development means writing down intent before implementation in a durable, machine-readable form. Not just task descriptions ("add a login feature") but intent that survives across multiple agent sessions: what the system must do, what invariants must hold, what trade-offs are acceptable. The spec becomes the constraint that narrows the agent's decision space at execution time.

Rickard surveys the emerging tooling landscape: GitHub Spec Kit and Kiro keep specs near the change workflow (requirements, design, tasks for each piece of work). OpenSpec moves them into the repo as persistent decision records. Intent from Augment Code treats the spec as shared mutable state. Symphony uses it as an orchestration contract for autonomous runs. Each approach puts the constraint at a different point in the development cycle.

The Dijkstra warning is appropriate: a sufficiently detailed spec is code. The goal isn't to write more specs—it's to write the right specs at the right abstraction level. Too little constraint and agents wander; too much and the spec becomes what you have to maintain instead of the code.

For engineering teams adopting AI agents: investing in spec infrastructure—even simple AGENTS.md files or architecture decision records—pays compounding dividends as agents accumulate context across sessions.
