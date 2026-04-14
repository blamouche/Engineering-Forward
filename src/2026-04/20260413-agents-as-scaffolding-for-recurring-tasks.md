# Agents as scaffolding for recurring tasks.

**Source**: https://lethain.com/agents-as-scaffolding
**Date**: April 13, 2026
**Author**: Will Larson
**Keywords**: agents, workflow automation, scaffolding, deterministic control, security operations, engineering process

## Elevator pitch
Will Larson argues that the best role for agents in recurring operational work is as scaffolding around code-driven workflows: prototype with autonomy, then progressively replace agentic control flow with deterministic software while preserving LLM help for the ambiguous parts.

## Takeaways
- Larson’s Dependabot example shows that fully agent-driven workflows can be useful prototypes but often fail at the precision needed for interrupting real teams.
- His preferred pattern is to move filtering and flow control back into code, then let agents handle fuzzy subproblems like ownership discovery or message drafting.
- The resulting systems are faster, cheaper, and more trustworthy because agents are used where they are strong rather than as universal software replacements.

## Synthesis
Will Larson puts his finger on one of the most durable agent design patterns I have seen this year: use agents first as exploratory scaffolding, then gradually harden the workflow by replacing brittle control flow with software. That is a much more convincing posture than either “agents can do everything” or “agents are useless.” It treats them as a discovery tool for where ambiguity actually lives.

His Dependabot example is perfect because the failure mode is so common. An agent can look surprisingly capable until the cost of being slightly wrong becomes socially expensive. Notifying the wrong team about a security issue is not catastrophic, but it is noisy enough to erode trust fast. That is exactly where deterministic filters, explicit thresholds, and code-level routing beat prompt-level pleading.

The broader takeaway is architectural. Good agent systems often end up narrower than the first prototype suggests. The durable value is not autonomous everything; it is a decomposition where code handles the crisp rules and agents handle interpretation, search, or formatting. That makes the whole system more reliable without giving up the leverage agents provide on messy edges.
