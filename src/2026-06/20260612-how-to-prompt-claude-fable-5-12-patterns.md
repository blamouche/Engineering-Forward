# How to Prompt Claude Fable 5: 12 Patterns Before June 22
**Source**: https://linas.substack.com/p/prompting-claude-fable-5-guide
**Date**: June 12, 2026
**Author**: Linas Beliūnas
**Keywords**: Claude Fable 5, Anthropic, prompting patterns, orchestrator routing, agent skills, effort levels, Mythos 5, migration checklist, AI-OS framework

## Elevator pitch
Claude Fable 5 requires a fundamentally different prompting approach than prior Claude models — setting goals rather than steps — and operators have until June 22, 2026 to extract durable assets before the free plan ends and every prompt becomes a budget decision.

## Takeaways
- Fable 5 is built for problems that are too complex, long-running, or ambiguous for prior models — end-to-end work that takes a person hours, days, or weeks.
- Prompts and skills built for prior Claude models are often too prescriptive for Fable 5 and actively degrade output quality; the old playbook is a downgrade.
- The guide synthesizes 12 core prompting patterns, an effort-level decision framework, and four high-impact use cases from Anthropic's official documentation.
- Key patterns include the orchestrator-and-cheaper-workers routing, the four-layer Context-Connections-Capabilities-Cadence AI-OS framework, screenshot-first vision workflows, and the medium-effort sleeper setting.
- Fable 5 is included in Pro, Max, Team, and Enterprise plans only until June 22, 2026, after which it requires usage credits at $10/M input and $50/M output tokens — twice the cost of Opus 4.8.

## Synthesis
Linas Beliūnas's newsletter guide synthesizes Anthropic's official Claude Fable 5 prompting documentation with the most useful patterns from the model's launch week. The central thesis is that most people are wasting Fable 5 by prompting it the same way they prompted Sonnet — opening a chat, typing a one-shot prompt, watching it think for five minutes, and closing the tab. Anthropic itself states that prompts and skills built for prior Claude models are often too prescriptive for Fable 5 and actively degrade output quality. The mental model that works is "set goals, not steps."

Fable 5 is described by Anthropic as a model built for problems that were previously too complex, long-running, or ambiguous, designed for end-to-end work that takes a person hours, days, or weeks. The teams getting the best results are not testing it on toy apps but pointing it at their hardest unsolved problems: codebase audits, IC memos, market maps, and multi-day product builds. The guide covers 12 core prompting patterns, an effort-level decision framework, and four high-impact use cases. Key patterns include the orchestrator-and-cheaper-workers routing (using Fable 5 as an orchestrator that delegates to cheaper models), the four-layer Context-Connections-Capabilities-Cadence AI-OS framework, screenshot-first vision workflows, the medium-effort sleeper setting, and the loop architecture that turns Fable 5 into an autonomous operating partner. The guide also covers the silent Opus 4.8 fallback, the Markdown memory system, the send_to_user tool, and Mythos 5 loop engineering.

The economic urgency is significant. Fable 5 is included in Pro, Max, Team, and seat-based Enterprise plans only until June 22, 2026. After that, continued use requires usage credits billed at API rates — $10 per million input tokens and $50 per million output tokens, exactly twice the cost of Opus 4.8. Beliūnas argues that the most obvious asymmetric move for founders, builders, and investors is not to wait and see but to extract the durable assets now: battle-tested prompts, reusable agent scaffolds, diligence workflows, memory files, distilled Agent Skills, and migration notes that will compound long after the free window closes. The guide includes a ready-to-use starter system prompt and a 10-action playbook to run before June 22.