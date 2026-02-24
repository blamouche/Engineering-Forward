# How OpenAI's Codex Team Works and Leverages AI
**Source**: https://newsletter.eng-leadership.com/p/how-openais-codex-team-works-and
**Date**: 2026-02-24
**Author**: Gregor Ojstersek (interview with Thibault Sottiaux)
**Keywords**: OpenAI Codex, AI-native teams, engineering culture, autonomy, onboarding, code review, velocity

## Elevator pitch
A look inside the Codex org: a small, high-autonomy team that bakes AI into planning, onboarding, review, QA and prioritization to sustain extreme shipping velocity.

## Takeaways
- The Codex org is described as ~40 people with minimal hierarchy, few meetings, and strong local decision-making.
- A single PM can scale impact dramatically by using Codex for real-time triage, prioritization, and coordination.
- Full end-to-end ownership (often 1–3 people per project) is the norm: plan → build → launch → iterate.
- AI is used across the lifecycle: onboarding, codebase comprehension, PR review loops, QA/verification, and large refactors (incl. sub-agents).
- The team emphasizes guardrails and codebase structure so speed doesn’t degrade into entropy.

## Synthesis
The article portrays OpenAI’s Codex team as an “AI-native” engineering org where AI isn’t a sidecar productivity boost but part of the operating system of the team. Structurally, the team is intentionally small and flat: limited management layers, very few recurring meetings, and high trust in individuals to make decisions. That design supports rapid iteration because decisions happen close to the work, and ownership is clear.

A concrete example is product management: the team reportedly has a single PM for the whole org, and the point isn’t heroics—it’s leverage. With Codex assisting in scanning feedback, categorizing issues, and assigning priorities, the PM can process high volumes of signal in real time. The article highlights an hour-long bug bash where >100 issues were triaged quickly and most fixed within 24 hours, illustrating a tight feedback loop made feasible by AI-assisted coordination.

On the engineering side, the work spans low-level systems (often in Rust), orchestration/runtime (“Codex harness”), API surface (Responses API), and distributed infrastructure. The operating pattern is small teams (two-slice style) or even single engineers shipping end-to-end. Ideas are bottom-up and experimental: not everything ships, but exploration is rewarded and selection pressure is high.

AI usage is described as pervasive. New hires use Codex for onboarding—from machine setup to understanding the codebase—compressing time-to-first-ship and reinforcing a “ship on day one” culture. During development, Codex supports plan/discussion modes to clarify underspecified requirements, performs local code review loops, and runs QA-like checks via custom skills. Sub-agents are used for parallel testing and large refactors. The throughline is that speed is the primary optimization, but only sustainable if guardrails and structure prevent codebase drift.

For other teams, the transferable lesson is less “copy OpenAI” and more “design your org and workflow so AI can amplify it”: encode best practices into reusable prompts/skills, use AI to accelerate feedback loops, and maintain codebase boundaries so velocity doesn’t collapse over time.