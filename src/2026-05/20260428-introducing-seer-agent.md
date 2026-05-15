# Introducing Seer Agent: The answer is already in Sentry. Now you can ask for it.
**Source**: https://blog.sentry.io/introducing-seer-agent/
**Date**: April 28, 2026
**Author**: Rahul Chhabria
**Keywords**: Sentry, Seer Agent, AI debugging, observability, trace-connected graph, Slack integration, Autofix, error monitoring

## Elevator pitch
Sentry launches Seer Agent — an AI-powered investigation tool that traverses Sentry's trace-connected telemetry graph to debug issues autonomously, available in open beta with Slack multiplayer mode for incident response.

## Takeaways
- Seer Agent navigates Sentry's trace-connected graph directly rather than doing generic text search, making investigations 10x faster
- Real-world example: a production outage was diagnosed in seconds by the agent identifying region-level rate limiting patterns before on-call arrived
- Slack integration enables "multiplayer mode" — engineers can redirect the agent mid-investigation, add context, and the investigation persists in threads
- Autofix can now be triggered directly from Slack alerts with a "Fix with Seer" button
- Upcoming: auto-triage on incident creation, proactive follow-up suggestions, and message queueing

## Synthesis
Sentry's Seer Agent represents a meaningful evolution in observability tooling: moving from dashboards developers query to AI agents that autonomously traverse telemetry. The key architectural insight is that Sentry's data isn't flat — it's a trace-connected graph where errors, spans, logs, deploys, and commits are all linked at ingest. Seer Agent walks these connections directly rather than guessing at time ranges and hoping relevant rows appear in text search.

The product's origin story is compelling: during a real production incident where Seer itself was failing, the Head of AI used the internal beta to diagnose a provider-side infrastructure outage in seconds — identifying the exact region-and-model pattern — before the on-call engineer could join the channel. This shifts the debugging bottleneck from "where do I look" to "what do I do about what I found."

The Slack integration is particularly well-designed for incident response. Rather than forcing engineers to context-switch to the Sentry UI during an outage, Seer Agent operates in-channel where the incident discussion is already happening. Multiple engineers can redirect the agent, add context, or learn by watching the traversal — and the investigation persists for post-mortem reference.

The roadmap reveals where this is heading: auto-triage that fires automatically on incident creation, proactive follow-up suggestions, and deeper CI/CD integration. The fundamental bet is that observability data is already rich enough to answer most debugging questions — the bottleneck has been the human effort required to navigate it. Seer Agent aims to eliminate that bottleneck entirely.
