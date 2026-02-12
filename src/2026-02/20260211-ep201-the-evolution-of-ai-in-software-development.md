# EP201: The Evolution of AI in Software Development
**Source**: https://blog.bytebytego.com/p/ep201-the-evolution-of-ai-in-software?publication_id=817132&post_id=187148454&isFreemail=true&r=fhb7r&triedRedirect=true&utm_source=substack&utm_medium=email
**Date**: Unknown
**Author**: ByteByteGo
**Keywords**: software engineering, coding agents, copilots, workflows, git

## Elevator pitch
A simple “three waves” model for AI-assisted coding—chat assistants → editor autocompletion → end-to-end agents—plus a short refresher on foundational engineering workflow concepts (e.g., git fetch vs pull) and agentic browser architecture.

## Takeaways
- Wave 1: general chat assistants (copy/paste code in/out) — useful but manual.
- Wave 2: coding autocompletes in-editor — speeds typing, limited repo context.
- Wave 3: coding agents — operate across the repo, edit multiple files, iterate to green tests.
- Reinforces that agents require layers: perception, reasoning roles, security, execution.
- Practical reminder: `git fetch` updates remotes; `git pull` fetches + merges.

## Synthesis
The value of the “three waves” framing is that it separates *where* the AI sits in the workflow from *how much responsibility* it can take. Wave 1 helps you think, but keeps execution manual. Wave 2 makes typing cheaper. Wave 3 changes the unit of work from “lines of code” to “tasks,” because the system can search, edit, and validate changes across a repository.

This matters because each wave moves the bottleneck. When autocompletion is good, typing is not the constraint—understanding requirements, navigating architecture, and managing risk are. Agents promise to absorb more of the navigation and implementation, but they also introduce new failure modes: brittle understanding of intent, partial changes, silent regressions, and security issues from tool use.

That’s why the “agentic browser layers” diagram is relevant even for coding agents. Reliability comes from harness design: a perception layer that faithfully represents state, a reasoning layer that can split roles (planner vs executor vs reviewer), a security layer that constrains what actions are allowed, and an execution layer that performs deterministic operations and refreshes state.

The git refresher is a good reminder that human mental models still matter. Even in an agent-first future, teams need shared operational understanding to debug what happened when an agent modifies history, merges changes, or resolves conflicts. The most effective teams will treat agents as accelerators, not replacements for basic engineering literacy.
