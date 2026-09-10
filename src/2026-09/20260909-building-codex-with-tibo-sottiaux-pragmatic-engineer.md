# Building Codex with Tibo Sottiaux
**Source**: https://newsletter.pragmaticengineer.com/p/building-codex-with-tibo-sottiaux
**Date**: 2026-09-09
**Author**: The Pragmatic Engineer (Gergely Orosz)
**Keywords**: OpenAI Codex, Tibo Sottiaux, Rust, open source, harness, code review, SDLC, ChatGPT merger, cloud development environments, AI coding agents

## Elevator pitch
Tibo Sottiaux, one of the engineers who created Codex and now heads OpenAI's Core Products & Platform org, shares how Codex was built: why it's written in Rust, why it's open source, how the harness stays slightly ahead of each new model, and how AI is lowering the cost of changing code from years to days.

## Takeaways
- Codex is written in Rust because the team designed for millions of cloud instances from day one — performance and security were first design principles, despite AI models being weak at Rust at the time
- Open source has a rarely discussed downside: the Codex team's work sometimes gets copied and released in other tools before Codex ships it
- Codex supports multiple AI models because open source means anyone could fork it — Tibo believes in winning by letting users choose the best model
- The Codex harness is always slightly ahead of OpenAI's latest model, providing guardrails that shrink as models improve — some "crutches" are discarded as the harness evolves
- Codex is plugged into Slack, every document, and all code at OpenAI by default — new joiners are told "have you asked Codex?" for any question
- Correctness checks and security reviews will be automated with AI, but conversations about what a system should do still matter and belong before code is written
- Maintenance and re-architecting are becoming very cheap: dependency upgrades take hours instead of weeks; re-architecting that took years now takes days
- Being "in the zone" is history: AI agents let engineers gather data faster, reducing the need for lengthy coding sessions

## Synthesis
The Pragmatic Engineer's conversation with Tibo Sottiaux is a rare deep dive into how OpenAI builds and iterates on Codex, its open-source coding agent. The choice of Rust — when AI models were much better at Python and TypeScript — is a case study in architectural foresight: the team designed for millions of cloud instances from the start, choosing performance and security over developer convenience, even though AI models struggled to generate Rust code at the time.

The harness-model dynamic is the most interesting technical insight. The harness provides "crutches" — guardrails, safety, efficiency, steerability, and a developer message injected at the start of each turn. As models improve, crutches are discarded and the harness shrinks. This co-evolution cycle between harness and model is the development loop that has produced Codex's iterative improvements.

The SDLC implications are profound. Maintenance tasks that used to take weeks (dependency upgrades) now take hours via a model "blasting through the codebase." Re-architecting for new tradeoffs that took years now takes days. Tibo's caveat — that quality code, good abstractions, and good test suites greatly affect ease — is important: agents amplify the quality of the underlying codebase. The merger of ChatGPT and Codex signals that coding agents and general AI assistants are converging into a single product surface.