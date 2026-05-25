# Macro Evals for Agentic Systems
**Source**: https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems
**Date**: May 19, 2026
**Author**: Shikhar Kwatra, Will Thieme, Bradley Strauss (OpenAI)
**Keywords**: evals, agentic systems, macro evaluation, multi-agent, observability, tracing, OpenAI, Promptfoo, debugging

## Elevator pitch
OpenAI's cookbook introduces "macro evals" — a methodology for analyzing recurring failure patterns across thousands of agent traces rather than grading individual responses, using a synthetic automotive order workflow with specialist agents to demonstrate how teams can move from trace data to actionable system improvements.

## Takeaways
- Macro evals complement lower-level evals by looking across many traces to identify recurring patterns: which problems repeat, where they concentrate, and which part of the agent workflow to inspect first.
- The cookbook uses a synthetic multi-agent EV order simulation with specialists for pricing, compliance, supply, factory routing, scheduling, and release decisions.
- Key labels used throughout: case_type (business situation), run_outcome (how the run ended), eval_finding (local symptom), and behavior_pattern (population-level pattern).
- The approach separates analysis into two levels: lower-level evals grade individual agents/handoffs/tools, while macro evals discover cross-trace patterns.
- Precomputed synthetic traces and saved eval labels let users run the full workflow without an OpenAI API key.

## Synthesis
OpenAI's cookbook addresses a growing pain point in agentic system development: when a multi-agent system fails, the problem is rarely a single bad response. A handoff might happen too late, a specialist agent might miss the same signal across many runs, or a review process might trigger for the wrong cases. Individual evals can't capture these systemic patterns.

The proposed solution is "macro evals" — a two-level evaluation framework. Lower-level evals (represented by Promptfoo in the example) grade individual agents, handoffs, tools, and completed runs against criteria like decision quality, policy correctness, specialist routing, market awareness, and review appropriateness. Macro evals then aggregate across many traces to discover recurring behavior patterns, answer concentration questions (where do problems cluster?), and guide human inspection to the highest-impact areas.

The cookbook demonstrates this on a synthetic automotive EV order workflow, chosen because it mirrors real business complexity: component availability, supplier substitution, factory capacity, pricing exceptions, tariffs, compliance, and multi-step escalation paths. The agent swarm maps specialists to business responsibilities — validation, supply risk, procurement, capacity balancing, factory routing, market intelligence, pricing, compliance, customer communications, and release review — orchestrated through the OpenAI Agents SDK with handoffs, tools, guardrails, and structured outputs.

A useful conceptual framework emerges: case_type describes the scenario setup, run_outcome is how the run ended, eval_finding is the local symptom, and behavior_pattern is the population-level pattern discovered across traces. The goal is not to build a perfect taxonomy but to show how AI engineering teams can move from thousands of agent events to a small number of patterns understandable by both technical and business stakeholders.

The cookbook ships with precomputed synthetic traces and saved eval labels, making it runnable without an OpenAI API key. This is significant because it lowers the barrier for teams to experiment with macro-eval patterns before instrumenting their own systems. The methodology reflects a maturation of AI engineering practices: as agentic systems grow in complexity, evaluation must grow from per-response grading to systemic pattern analysis.
