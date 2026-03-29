# The Agent That Saved My Brain
**Source**: https://every.to/p/the-agent-that-saved-my-brain
**Date**: March 23, 2026
**Author**: Austin Tedesco
**Keywords**: AI agents, Claude Code, OpenClaw, growth operations, workflow automation

## Elevator pitch
Every’s head of growth explains how he built an AI “command center” agent in Claude Code and Slack to automate cross‑app reporting and planning, freeing him to focus on higher‑value decisions.

## Takeaways
- The agent ("Montaigne") centralizes data from tools like Stripe, PostHog, Slack, Notion, and email to cut context switching.
- Building capability required weeks of experimentation and iterative prompting, not one‑shot setup.
- Context accuracy depends on refining definitions and sources of truth, with explicit corrections when outputs drift.
- The agent can draft briefs, answer metrics questions, and spawn subagents to execute routine tasks.
- The author highlights a tradeoff between improving the system and doing the work, requiring discipline to avoid endless tuning.

## Synthesis
Austin Tedesco describes building “Montaigne,” an AI agent that acts as a command center for his growth role at Every. The motivation is familiar: growth work spans many tools and data sources, and constant context switching drains energy for strategic decisions. By routing routine questions—like conversion rates on landing‑page buttons—through a Slack‑based agent, he can retrieve answers in minutes without a scavenger hunt through dashboards.

The system runs in Claude Code and as an OpenClaw bot in Slack. It has broad tool access (Stripe, PostHog, Notion, Figma, Slack, email, calendar) and a layered knowledge base about the business, plus a library of reusable skills for recurring workflows. Tedesco emphasizes that the agent’s usefulness came from weeks of “play” with Claude Code: building small projects, learning to ask for step‑by‑step guidance, and iterating on failures. This experimentation built intuition about what the model could do and how to scaffold tasks effectively.

A key operational lesson is that context accuracy is not automatic. Early on, Montaigne reported incorrect MRR figures because it used a different ChartMogul definition. The fix was not a model upgrade but explicit instruction: point the agent to the true source of record and correct its assumptions. This iterative alignment—correcting definitions, validating outputs, and reinforcing sources—turns a generic agent into a trusted coworker.

The workflow benefits are concrete. Montaigne can ingest a voice note describing a campaign strategy, pull relevant data, and draft a brief directly in Notion. It can also spawn subagents to handle execution tasks in parallel, acting as a multiplier rather than a simple query interface. This shifts the author’s time toward high‑judgment work while the system manages assembly and analysis.

Tedesco also flags a tension: improving the agent can become its own work sink. Spending hours tuning the system can feel productive while delaying actual shipping. His practical fix is to force focus—clear distractions, ask the agent to sequence remaining priorities, and use subagents for background work. The article ultimately frames agent adoption as an iterative, human‑guided process: start small, integrate real tools, correct errors, and balance system improvement with outcomes.
