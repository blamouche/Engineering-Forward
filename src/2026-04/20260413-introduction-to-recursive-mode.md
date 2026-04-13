# Introduction to recursive-mode

**Source**: https://recursive-mode.dev/introduction
**Date**: April 13, 2026
**Author**: recursive-mode
**Keywords**: recursive-mode, agent workflow, durable context, documentation, AI coding

## Elevator pitch
recursive-mode packages long-running AI-assisted development into durable repo docs, making requirements, plans, evidence, and lessons live in files instead of disappearing into chat context.

## Takeaways
- recursive-mode packages long-running AI-assisted development into durable repo docs, making requirements, plans, evidence, and lessons live in files instead of disappearing into chat context.
- recursive-mode’s pitch is straightforward: most long-running agent work fails because the important state lives in conversation history. The project answers that by moving requirements, plans, implementation evidence, testing, QA, and memory into repository files that persist across sessions and contributors.
- What makes the approach notable is not just documentation for humans but documentation as the operating substrate for agents. Each phase consumes the previous phase’s artifacts and loops through audit and repair until exit criteria are met. In other words, the workflow tries to encode discipline into the repo rather than relying on the model to remember it or re-invent it consistently.
- The result is a useful alternative to chat-first development. It trades spontaneity for traceability and resumability, which is often the right trade in complex software projects where auditability, handoff, and durable lessons matter more than a smooth demo.

## Synthesis

recursive-mode’s pitch is straightforward: most long-running agent work fails because the important state lives in conversation history. The project answers that by moving requirements, plans, implementation evidence, testing, QA, and memory into repository files that persist across sessions and contributors.

What makes the approach notable is not just documentation for humans but documentation as the operating substrate for agents. Each phase consumes the previous phase’s artifacts and loops through audit and repair until exit criteria are met. In other words, the workflow tries to encode discipline into the repo rather than relying on the model to remember it or re-invent it consistently.

The result is a useful alternative to chat-first development. It trades spontaneity for traceability and resumability, which is often the right trade in complex software projects where auditability, handoff, and durable lessons matter more than a smooth demo.
