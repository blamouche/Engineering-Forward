# Long horizon tasks with Codex
**Source**: https://developers.openai.com/cookbook/examples/codex/long_horizon_tasks
**Date**: 2026-02-26
**Author**: Unknown
**Keywords**: Codex, agentic coding, long-running tasks, verification, project memory

## Elevator pitch
A practical write-up argues that the real breakthrough in coding agents is time horizon—showing how a Codex run can stay coherent for ~25 hours by externalizing specs, plans, and status into durable project memory and enforcing a verify-repair loop.

## Takeaways
- Long-horizon performance is about maintaining coherence across many plan→execute→verify cycles, not one-shot prompts.
- Durable project memory (spec, plan, runbook, status logs) reduces drift and makes runs inspectable.
- Milestones with acceptance criteria and mandatory validation create a “stop-and-fix” discipline.
- Tool feedback (tests/lint/typecheck/build) is the steering signal that keeps the agent grounded.
- The workflow shifts developers from micromanaging code to supervising checkpoints, reviewing diffs, and adjusting goals.

## Synthesis
This article is essentially a playbook for getting value from coding agents on multi-hour or multi-day tasks. It opens with a claim: the meaningful progress in agentic coding isn’t just that models got smarter—it’s that they can reliably follow instructions for longer and recover from errors without losing the thread. That increase in time horizon changes what’s feasible: instead of delegating a function, you can delegate a project slice.

The core example is a stress test where Codex is given a blank repository and asked to build a design tool end-to-end. The specifics matter less than the harness: the agent is operating in a loop of planning, editing, running verification, observing failures, repairing, and updating state. The essay ties this to an emerging benchmark lens (how long a model can complete tasks at given reliability levels) and emphasizes that “agentic coding” is increasingly a problem of sustained control.

The key technique presented is externalizing state into files the agent can reread: a frozen spec (Prompt.md), a milestone plan with validations (Plan.md), a runbook (Implement.md), and a living status/audit log (Documentation.md). This “durable project memory” is described as the antidote to drift: the agent can always re-anchor on what “done” means and which constraints matter.

Another repeated idea is verification as the primary reward signal. Rather than hoping the code works, the agent is instructed to run tests/lint/typecheck/build after each milestone and to stop-and-fix immediately if validation fails. The result is not framed as perfection, but as a credible, testable artifact produced through disciplined iteration.

The takeaway for practitioners is a change in posture: treat long runs as a managed process with guardrails and checkpoints, not as a magic prompt. The spec and the verifiers become the real product interface for steering autonomous work.