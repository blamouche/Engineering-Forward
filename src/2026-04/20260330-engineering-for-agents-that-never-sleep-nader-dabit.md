# Engineering for Agents That Never Sleep
**Source**: https://nader.substack.com/p/engineering-for-agents-that-never
**Date**: March 30, 2026
**Author**: Nader Dabit
**Keywords**: AI agents, autonomous agents, engineering practices, testing, documentation, developer infrastructure

## Elevator pitch
Agent initiation ratios are inverting from 70% human-triggered to 90% autonomous within a year, requiring engineering teams to build the testing, documentation, and environment infrastructure that enables agents to ship software rather than just write code.

## Takeaways
- Currently 70% of agent sessions are human-triggered; Dabit predicts this flips to 90% autonomous within a year
- Machine-readable signals already exist in every engineering workflow — alerts, test failures, spec approvals — but humans act as inefficient relays between them and agents
- Prerequisites for reliable autonomous agents: comprehensive unit tests, quality documentation, reproducible environments, rich system context
- The distinction: "Without it, you have agents that write code. With it, you have agents that ship software."
- The prompt interface persists but becomes secondary on high-performing teams

## Synthesis
Dabit's essay describes a transition that is already underway in leading engineering organizations: the shift from AI agents as on-demand tools that humans activate to AI agents as autonomous components of engineering infrastructure that respond to system signals independently.

The relay metaphor is precise. In current workflows, a test failure generates a CI notification, a human reads that notification, interprets the failure, opens an agent session, and translates the notification into a prompt. The human is acting as an information router between two systems — the CI infrastructure and the AI agent — that have no direct integration. This routing adds latency and requires human attention for tasks that don't benefit from human judgment. As agent capabilities improve, eliminating this relay becomes a natural engineering optimization.

The prerequisite list — unit tests, documentation, reproducible environments, system context — reads as a checklist for the quality of a team's existing engineering practices. Teams with mature testing cultures and well-maintained documentation are closer to autonomous agent deployment than teams without them, because agents operating without a human relay need to self-verify their work. A unit test suite is how an agent confirms that its change didn't break anything; quality documentation is how an agent understands what it's supposed to do; a reproducible environment is how an agent runs its verification. Without these, an autonomous agent has no feedback mechanism beyond attempting to commit code and seeing if the build fails.

The predicted timeline — 10/90 human/autonomous within a year — implies that teams treating this as a distant future consideration are already behind. The engineering infrastructure investment required to support reliable autonomous agent operation takes time to build, and teams that start investing now in test coverage, documentation quality, and environment reproducibility will be positioned to unlock autonomous agents when the capability threshold crosses.

The persistence of the prompt interface is an important nuance. Dabit is not predicting that human engineers become irrelevant — rather that on high-performing teams, the most impactful work shifts from prompt-based task initiation to defining goals, reviewing agent outputs, and building the infrastructure that enables autonomous operation. This is a higher-leverage role than acting as a relay between machines.
