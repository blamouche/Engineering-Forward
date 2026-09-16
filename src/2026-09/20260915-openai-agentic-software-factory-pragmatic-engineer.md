# Inside OpenAI's Agentic Software Factory
**Source**: The Pragmatic Engineer (pragmaticengineer+deepdives@substack.com)
**Date**: 2026-09-15
**Author**: Gergely Orosz (The Pragmatic Engineer)
**Keywords**: OpenAI, Codex, agentic software factory, CI/CD, code review, pull requests, engineering practices, infrastructure

## Elevator pitch
Gergely Orosz visited OpenAI's headquarters and found that Codex has become the backbone of virtually everything the company does — not just for engineers but for finance, legal, and marketing teams too. The piece details OpenAI's "agentic software factory": an automated pipeline where Codex agents gather context, write code, run CI, perform multi-specialist code reviews, deploy changes with per-change SRE agents, monitor production, and respond to outages. IDE usage is declining, pull requests are surging 10x, and the traditional PR and code review processes are being fundamentally reimagined.

## Takeaways
- Codex adoption went from ~0% to 90% across non-engineering orgs (finance, legal, recruitment) in four months, without a mandate from above
- OpenAI's Codex app bet against the IDE: since January, IDE usage has declined as Codex usage surged; the team dismissed the temptation to fork VS Code
- PRs per engineer are growing "like a hockey stick" — roughly a 10x increase in load on CI/CD systems in six months
- The agentic software factory pipeline: human defines outcome → Codex gathers context (Git, Slack, Notion, Databricks) → Codex implements → CI build & test → multi-specialist agentic code review → agentic deploy with per-change SRE agent → production monitoring → Perf Factory feeds back
- Multiple "domain specialist" agents review each change (cloud infra, security, etc.), with risk classification determining whether human review is required
- Sevbot is OpenAI's incident response agent built on Codex — it collects context, proposes mitigations, and answers questions in Slack; the goal is autonomous mitigation of routine outages
- Engineers are becoming "more like product managers than traditional systems engineers" — judgment, prioritization, and taste matter more
- Shipping native mobile apps is an increasingly painful bottleneck: code can be written in minutes but Apple/Google approval takes days
- The /goal setting lets agents work on long-running tasks for days, with agents spinning off sub-agents to reduce the human's management surface

## Synthesis
This is one of the most detailed looks inside a frontier AI lab's engineering practices to date. Gergely Orosz interviewed seven engineering leaders at OpenAI and paints a picture of a company that has fully committed to an agentic software development model — not as an experiment, but as the way work happens.

The most striking finding is the speed of Codex adoption across non-engineering teams. Finance, legal, and recruitment went from near-zero usage to 90% in four months, without a mandate. The key driver was the /goal feature and improved handling of long-running tasks: people set a goal and let the agent work for days, with the agent spinning off sub-agents. This reduced the number of things a human needs to manage in parallel.

The "software factory" pipeline is the piece's centerpiece. It maps a nine-step process from human-defined outcomes through context gathering, implementation, CI, multi-specialist code review, agentic deployment with per-change SRE agents, production monitoring, and the Perf Factory feedback loop. The multi-specialist code review approach — spinning off separate agents configured as "cloud infra expert" or "security specialist" — is notable because it would be impractical to have human experts from every team review every change. Risk classification routes high-risk changes through stricter processes.

The infrastructure challenges are equally revealing. A 10x increase in CI/CD load in six months is exposing bottlenecks everywhere, and the native mobile app deployment bottleneck is a structural problem: code can be written in minutes but Apple's App Store review still takes days. Sulman Choudhry (Head of Engineering, ChatGPT) notes this gap is "already becoming painful" and expects pressure to increase.

The human side of the transformation: engineers are becoming more like product managers, with judgment and agency mattering more than traditional systems engineering skills. Engineering specializations are disappearing, and it only takes one or two engineers for previously "impossible" rewrites and migrations to succeed.