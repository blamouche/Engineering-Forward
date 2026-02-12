# NanoClaw: a small, container-isolated Claude assistant
**Source**: https://github.com/gavrielc/nanoclaw?utm_source=www.theunwindai.com&utm_medium=newsletter&utm_campaign=clawdbot-in-just-500-lines-of-code&_bhlid=ee1649147d4a6aa7be0dafb677e397d95ebacbb8
**Date**: Unknown
**Author**: gavrielc (GitHub)
**Keywords**: personal assistant, Claude Agent SDK, container isolation, security, minimalism, WhatsApp

## Elevator pitch
NanoClaw is a deliberately minimal personal Claude assistant that prioritizes OS-level isolation (agents run in Linux containers with explicit mounts) and “small enough to understand” code over feature breadth and configuration sprawl.

## Takeaways
- The project positions itself as an alternative to OpenClaw: fewer modules/dependencies, one process, and a codebase you can review quickly.
- Security model centers on container isolation (Apple Container on macOS or Docker) rather than application-level allowlists.
- AI-native setup and customization: Claude Code guides installation and users change behavior via code edits, not sprawling config.
- Opinionated product scope: built for one user, with WhatsApp I/O by default; other channels should be added via skills that transform a fork.
- Includes core “assistant platform” primitives: per-group isolation, a main admin channel, scheduled tasks, web search/fetch.

## Synthesis
This repository README is written as both a technical overview and an argument about how personal agent software should be built. The author starts from a trust premise: running a large, complex agent framework with deep access to one’s “life” is uncomfortable if the codebase is hard to audit. NanoClaw’s response is to compress the system into a small, understandable surface area—one Node.js process and a handful of files—so the user can realistically reason about what is happening.

The second pillar is security by isolation. Rather than depending primarily on internal permission checks and allowlists, NanoClaw runs agent execution inside Linux containers and relies on explicit filesystem mounts to define what the agent can see. On macOS it can use Apple Container for a lightweight runtime (or Docker), and on Linux it uses Docker. The claim is that Bash/tool access is safer when the command execution environment is sandboxed at the OS/container boundary.

A third theme is “AI-native” ergonomics. There’s no conventional installer wizard or monitoring dashboard; instead, Claude Code orchestrates setup via a guided /setup flow, and debugging is meant to happen conversationally (“ask Claude what’s happening”). This aligns with the broader trend of tools being controlled through natural-language workflows rather than bespoke UIs.

NanoClaw is also intentionally not a generic multi-channel framework. It’s “built for one user,” and the author discourages expanding the base code with every possible integration. Instead, the suggested contribution model is to ship skills (e.g., /add-telegram) that transform a user’s fork into what they need, preserving a minimal upstream.

Overall, the repo is a strong example of the design space around personal agents: minimalism and auditability, OS-level sandboxing, and an approach that treats “customization” as safe code modification because the codebase is small enough for an LLM (and human) to reason about.
