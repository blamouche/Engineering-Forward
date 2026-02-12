# Minions: Stripe’s one-shot, end-to-end coding agents
**Source**: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents?utm_source=tldrnewsletter
**Date**: 2026-02-09
**Author**: Alistair Gray
**Keywords**: AI, coding agents, developer productivity, unattended automation, CI, MCP, tool integration

## Elevator pitch
Stripe built “minions”: fully unattended, one-shot coding agents that start from a Slack request and end as a CI‑passing pull request—by tightly integrating LLM loops with Stripe’s internal tooling, guardrails, and feedback systems.

## Takeaways
- The goal is **unattended, one-shot** execution: no mid-flight interaction, but always **human review** at the end.
- Scale and constraints matter: Stripe’s massive, atypical stack (Ruby + Sorbet, homegrown libs, regulatory/compliance needs) makes “vibe coding” insufficient.
- Minions work because they’re **tool-first**: deterministic steps (git, lint, test, templating) are interleaved with agent reasoning to reduce variance.
- Context is hydrated via **MCP** and a large internal tool catalog ("Toolshed"), plus conditional rule files based on repo subdirectories.
- Feedback is “shifted left” with fast local checks on push, selective CI, and at most two CI iterations to balance cost/time.

## Synthesis
Stripe’s “minions” are positioned as the next step in practical agentic coding: not an interactive copilot, but an unattended worker that can be launched in parallel across many small tasks. The key product promise is end-to-end: a run begins with a request (often from Slack, in the same thread where engineers discuss an issue) and completes as a pull request that passes CI and follows the company’s PR conventions. Humans still review and merge, but the code itself can be entirely agent-produced.

The article argues that building this in-house was less about model capability and more about operating constraints. Stripe’s codebase spans hundreds of millions of lines across large repositories, uses an uncommon backend stack (Ruby with Sorbet typing, without Rails), and relies heavily on internal libraries and practices that foundation models won’t “know” by default. Add the real-world stakes—payment systems with regulatory and compliance obligations—and it becomes clear why a generic agent that performs well on greenfield demos won’t reliably make correct, policy-compliant changes in a mature production system.

Minions therefore live inside the same developer productivity foundations Stripe created for humans. The run executes in an isolated, pre-warmed “devbox” environment that can be spun up quickly and kept away from production resources. The orchestration loop is based on an early coding agent (a fork of Block’s Goose) but is made deliberately opinionated: deterministic automation (git operations, linters, tests, CI flows) is interleaved with the agent’s generative steps. This design choice is the core thesis: you get the creativity of LLMs where it helps, and repeatable compliance with required engineering steps where you can’t tolerate variance.

For context gathering and actions across systems, minions speak MCP and connect to curated subsets of a large internal MCP tool server (“Toolshed”) with hundreds of tools spanning internal and SaaS systems. They also consume the same rule files used by human-driven tools like Cursor or Claude Code, but in Stripe’s case those rules are largely conditional by directory to avoid a brittle wall of global constraints.

Finally, reliability comes from layered feedback loops. Stripe emphasizes “shift-left” checks: a fast local heuristic runner on each push catches many issues in seconds, before expensive CI. CI is selective but huge in aggregate, and the system includes autofixes for some failures. Importantly, Stripe caps iteration—often one, at most two CI rounds—reflecting a pragmatic tradeoff between completeness and the cost of tokens/compute/time. The overall message is that unattended agents become viable not by magic prompts, but by deep integration with environments, tools, policies, and fast feedback.
