# Compound Engineering
**Source**: https://every.to/guides/compound-engineering
**Date**: March 23, 2026
**Author**: Kieran Klaassen; Claude
**Keywords**: compound engineering, AI‑assisted development, planning, review, workflows

## Elevator pitch
A development philosophy where each unit of work makes future work easier, built around a loop of plan → work → review → compound.

## Takeaways
- Compound engineering aims to reduce complexity over time instead of accumulating it.
- The method emphasizes planning and review as the majority of engineering effort.
- The “compound” step captures reusable patterns and updates system knowledge.
- AI agents and workflows make the loop practical for small teams.
- Plugins and structured docs turn insights into durable institutional memory.

## Synthesis
This guide introduces “compound engineering,” a philosophy for AI‑assisted software development that focuses on making each unit of work simplify future work. The authors contrast it with conventional development, where features often add complexity and make the codebase harder to change. In compound engineering, the goal is to codify lessons, patterns, and fixes so the system becomes easier to build on over time.

The method is organized as a four‑step loop: plan, work, review, compound. Planning is deliberate and thorough: understand requirements, study the codebase, research external best practices, design a solution, and validate it before implementation. The authors argue that planning and review should consume most of the engineer’s time—often 80 percent—because good plans reduce errors and reduce the need for rework.

The work phase focuses on execution with guardrails. It encourages isolation (using branches or worktrees), step‑by‑step implementation, and running validations after changes. The workflow assumes an agent can do much of the implementation while the human monitors progress and adapts when issues appear. This reflects a broader view that AI is best used for execution, while humans remain responsible for direction and quality control.

Review is treated as essential, not optional. The guide recommends multiple agents reviewing output in parallel, prioritizing findings, and resolving issues before shipping. This stage is where mistakes are caught, but it’s also where new knowledge emerges. Rather than stopping at a “pass,” the loop continues into the most distinctive step: compounding.

The compound step captures what was learned and converts it into reusable assets. This can mean writing solutions into documentation, tagging patterns with metadata, and updating the system’s core instruction files (like CLAUDE.md) so future work benefits from past effort. In this model, each fix becomes a tool or rule that reduces the chance of recurrence. The result is a codebase and workflow that grow more resilient with each cycle.

The guide notes that these practices are formalized in a plugin with specialized agents, commands, and skills. The plugin structure shows how planning, review, and compounding can be embedded into tooling, giving teams a repeatable system for AI‑assisted development. The emphasis on institutional memory—plans, solutions, and review notes—signals that the real asset is not just the code, but the accumulated decision history that makes future work faster.

Overall, compound engineering reframes AI tooling as part of a continuous learning loop. It is less about speeding up one task and more about building a system that improves itself through captured knowledge and disciplined workflow.
