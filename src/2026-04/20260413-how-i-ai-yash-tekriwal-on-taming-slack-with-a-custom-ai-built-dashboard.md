# How I AI: Yash Tekriwal on Taming Slack with a Custom AI-Built Dashboard

**Source**: https://www.chatprd.ai/how-i-ai/taming-slack-with-a-custom-ai-built-dashboard
**Date**: April 13, 2026
**Author**: ChatPRD
**Keywords**: Slack, personal productivity, AI dashboards, OpenClaw, Perplexity Computer

## Elevator pitch
Yash Tekriwal’s workflow turns Slack overload into a custom triage layer by using AI to build the tool once, then leaning on deterministic code and lightweight classification for the daily job.

## Takeaways
- Yash Tekriwal’s workflow turns Slack overload into a custom triage layer by using AI to build the tool once, then leaning on deterministic code and lightweight classification for the daily job.
- Yash Tekriwal’s setup is a concrete example of using AI as a software construction layer rather than as a permanent human-in-the-loop assistant. He starts by defining a triage model for Slack notifications, then uses OpenClaw to understand Slack’s API and generate a text digest that groups alerts by source and urgency.
- The clever move is that most of the system is deterministic. AI helps with the messy subjective classification at the end, but the rest is engineering: timestamps, grouping logic, direct links, and integrations. From there, Perplexity Computer is used to turn the digest into a Kanban-style dashboard with actions like archiving low-priority items.
- The larger lesson is that personal productivity software is getting cheap to build. Instead of waiting for Slack to support one person’s ideal workflow, AI lets that person build a thin custom layer tailored to their own attention model.

## Synthesis

Yash Tekriwal’s setup is a concrete example of using AI as a software construction layer rather than as a permanent human-in-the-loop assistant. He starts by defining a triage model for Slack notifications, then uses OpenClaw to understand Slack’s API and generate a text digest that groups alerts by source and urgency.

The clever move is that most of the system is deterministic. AI helps with the messy subjective classification at the end, but the rest is engineering: timestamps, grouping logic, direct links, and integrations. From there, Perplexity Computer is used to turn the digest into a Kanban-style dashboard with actions like archiving low-priority items.

The larger lesson is that personal productivity software is getting cheap to build. Instead of waiting for Slack to support one person’s ideal workflow, AI lets that person build a thin custom layer tailored to their own attention model.
