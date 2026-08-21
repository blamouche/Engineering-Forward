# How to Build an Agentic OS with Claude Fable 5
**Source**: https://linas.substack.com/p/claude-fable-5-agentic-os-guide
**Date**: 2026-07-10
**Author**: Linas Beliūnas
**Keywords**: Claude Fable 5, agentic OS, agent architecture, cost control, prompt injection defense, delegation

## Elevator pitch
Claude Fable 5 is the first generally available model where the binding constraint is no longer intelligence but rather how you organize the system around it — an "agentic OS" of constitutions, heartbeats, and verification loops that makes autonomous AI work trustworthy and cost-efficient.

## Takeaways
- Fable 5 holds 1M tokens of context, runs unattended for hours, spawns subagents, and costs $50/million tokens — but the real bottleneck is organizational, not computational
- The same request can cost $0.10 or $0.72 depending on the effort level setting alone; letting Fable spawn 10 parallel copies of itself can burn $400-600/day
- An agentic OS needs five components: a constitution (hard rules), a daily heartbeat script, a standing-goals system for re-checking finished work, prompt injection defenses, and a runbook mapping every alarm to a response
- The model that does the work cannot also be the judge of whether the work is done — you need external verification, not self-assessment
- Work is never marked "done" in a reliable agentic system; it is monitored perpetually, with daily checks that the result still holds true

## Synthesis
Linas Beliūnas makes a compelling case that the AI industry's fixation on model capability is missing the real challenge: the operating system around the model. With Fable 5, intelligence is no longer the binding constraint — the bottleneck is the organizational structure that makes autonomous AI work trustworthy and cost-efficient.

The article provides a practical architectural blueprint. The "constitution" is a short file of hard rules the model reads on every run and cannot argue with, because a script can check compliance. The "daily heartbeat" is a complete runnable script where Fable 5 makes decisions and cheaper models handle execution — a pattern that mirrors how senior engineers delegate: strategic decisions to expensive talent, execution to more affordable resources. The "standing-goals system" re-checks finished work daily so nothing quietly degrades. Prompt injection defenses are necessary because the loop reads inputs from strangers who can hide instructions in them.

The most striking insight is about cost. The same request can vary 7x in cost depending on configuration, and uncontrolled agent spawning can burn hundreds of dollars per day. This makes the case for cost-aware architecture — not just prompt engineering, but infrastructure engineering around LLMs. The article's core thesis — that work is never done, only monitored — is a paradigm shift for how we think about AI agent reliability. It reframes agent ops from "complete this task" to "continuously verify this task remains complete," which is how production systems actually work in mature engineering organizations.