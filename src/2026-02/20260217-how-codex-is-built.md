# How Codex is built
**Source**: https://newsletter.pragmaticengineer.com/p/how-codex-is-built
**Date**: 2026-02-17
**Author**: Gergely Orosz
**Keywords**: codex, openai, engineering

## Elevator pitch
Gergely Orosz’s deep dive explains how OpenAI’s Codex agent works, how the team builds with it, and why the tooling is reshaping engineering practices inside OpenAI.

## Takeaways
- Codex usage has surged, with over a million weekly developers and a new desktop app.
- The agent loop centers on prompt assembly, inference, tool calls, and iterative responses.
- Compaction keeps long conversations efficient and avoids quadratic inference costs.
- Codex writes most of its own code, with engineers acting as multi-agent managers.
- Practices like tiered code review, AGENTS.md, and sandboxing shape safe adoption.

## Synthesis
Gergely Orosz reports that OpenAI’s Codex has grown into a widely used multi‑agent coding assistant, with more than a million developers using it weekly and usage up sharply since January. OpenAI recently released a desktop app and a new GPT‑5.3‑Codex model, described internally as the first model to help create itself. To understand how Codex works and how it changes engineering practices, Orosz interviewed several OpenAI leaders: Thibault Sottiaux (head of Codex), SQ Mah (researcher on the Codex team), and Emma Tang (head of data infrastructure, whose team uses Codex heavily).

At a technical level, Codex runs as an agent loop. The workflow starts with prompt assembly, where user input is combined with system instructions, coding standards, available tools, and contextual files such as AGENTS.md and local environment info. The model then performs inference and streams output events, which can include tool calls. If a tool is invoked, the system executes the action (read a file, run a command, write code) and sends results or errors back to the model, which may retry or adjust. The loop ends with a final message to the user and restarts when the next instruction arrives. This architecture emphasizes iterative tool use rather than a single, static response.

To keep the system efficient, Codex uses compaction. As the context window fills, the system calls a special endpoint to generate a shorter representation of the conversation history. This condensed version replaces the original context, reducing token load and mitigating the quadratic cost of self‑attention. Compaction is framed as a practical necessity for long‑running agent workflows.

Safety is handled through sandboxing. Codex runs with restricted network and filesystem access by default, an intentional friction that limits potential harm for less technical users. OpenAI allows users to disable these safeguards, but the default posture is “safe by default,” even if it hurts adoption. This aligns with the broader reality that LLMs are nondeterministic and can produce unexpected actions, especially when given tool access.

A defining feature of the team’s workflow is that Codex largely builds itself. The team estimates that Codex generated more than 90% of the desktop app’s code, mirroring reports from other AI lab tools like Claude Code. Engineers typically run several agents in parallel—for feature implementation, code review, security review, codebase summaries, and bug fixes—acting more as “agent managers” than individual coders. This parallelism reshapes daily work: engineers juggle multiple agent threads at once rather than concentrating on a single task.

The article also describes internal “skills” as reusable agent capabilities. The Codex team maintains more than 100 skills, from security best‑practice audits to a “yeet” skill that drafts a pull request based on a plan, and a Datadog integration that surfaces alerts and proposes fixes. These skills steer the model toward desired behavior and can be combined, creating a composable toolkit for common tasks.

Code review is tiered. Codex performs automated AI reviews whenever a pull request enters review, using a bespoke model optimized for high‑signal feedback. For non‑critical code, teams can merge after AI review alone; for core components, human review remains mandatory. The team also structures the codebase to be “inevitable for the model to succeed,” with strong tests, clear module boundaries, and explicit instructions for validation. Codex can even run tests against its own codebase via a dedicated skill, and nightly runs scan for issues and propose fixes for engineers to review in the morning.

Overall, Orosz’s deep dive positions Codex as both a product and a new way of working: fast release cadence, agent‑driven development, and process adjustments like AGENTS.md, sandboxing, and tiered review. The implication is that engineering organizations adopting agentic tools will need to retool workflows, expectations, and quality gates to match an environment where code is written by many parallel agents and human developers orchestrate rather than manually craft every line.
