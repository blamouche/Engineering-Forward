# Agent Judge: Solving Long-Horizon Evals for Production Agents
**Source**: https://www.judgmentlabs.ai/blogs/agent-judge-solving-long-context-evaluations
**Date**: 2026-05-27
**Author**: Rishi Gujjar, Andrew Li (Judgment Labs)
**Keywords**: llm-evaluation, agent-evals, long-horizon-agents, trajectory-evaluation, llm-as-judge, multi-agent-evaluation, adaptive-rubrics, environment-verification

## Elevator pitch
Judgment Labs' Agent Judge is an agentic evaluation harness that solves three failure modes of simple LLM judges on long-horizon production agents — long trajectories that exceed context windows, stateful actions that can't be verified from the trajectory alone, and changing agent behavior that makes fixed rubrics go stale — through Search, Verification, and Adaptation.

## Takeaways
- Simple LLM judges break down on long-horizon agents because they can't fit full trajectories into context, can't verify stateful changes against source-of-truth systems (CRM, AWS, GitHub, Google Calendar), and can't adapt as models, tools, and workflows evolve
- Agent Judge addresses these through three capabilities: Search (making long trajectories queryable so buried evidence can be found), Verification (checking claimed actions against the actual environment state), and Adaptation (comparing evaluations against human feedback and production signals to evolve rubrics)
- The system runs as a multi-agent harness: reader agents inspect targeted evidence, spawned worker agents split search or verification work, and forked agents pursue new questions raised during the first pass
- Benchmarking on production traffic for trajectory-level hallucination detection shows Agent Judge with Rubric Builder refinement achieves the highest accuracy (0.76 initial, improving further after refinement) compared to Claude Code (0.73), Codex (0.69), GPT-5.4 LLM Judge (0.74), and GPT-5.4-mini LLM Judge (0.65)
- Agent Judge with Rubric Builder stays strongest in the hard tail of difficulty deciles, while a five-judge LLM ensemble baseline degrades sharply as trajectory difficulty increases
- The rubric becomes a living, versioned evaluation artifact: tested against production trajectories, updated from feedback, and grown alongside the agents instead of rewritten by hand each time behavior shifts

## Synthesis
As the AI industry moves toward long-horizon agents that autonomously perform tasks end-to-end — researching leads, updating a CRM, sending emails, booking meetings, editing dozens of files, updating AWS configs, opening GitHub PRs — simple LLM judges fail to consistently produce accurate evaluations. Judgment Labs identifies three structural failure modes that cause this breakdown.

The first is trajectory length. Long-horizon agents can span hundreds of tool calls across databases, services, documents, and other systems. Coding agents like Codex and Claude Code run for long horizons by compacting context as they work, but the resulting trajectories can exceed what an LLM judge can hold in context. Pasting the whole trace into one prompt may fail outright; truncating or slicing it leaves important parts unread. Agent Judge addresses this by turning trajectories into queryable objects — messages, tool calls, retrieved documents, database responses, logs, retries, and state changes all become navigable evidence rather than context to jam into a single prompt. Multi-hop reasoning is supported: one search surfaces a clue, that clue raises a new question, and the evaluator follows the chain.

The second is stateful actions. An LLM judge only sees the trajectory, not the corresponding environment, so stateful changes go unverified. Agent Judge queries the same systems the agent acted on and checks whether the action actually happened. It aligns each claimed action with the system's recorded state — for example, matching a "bug fixed" claim against CI results, which may still show a failing test.

The third is changing behavior. Models, tools, and user workflows evolve as AI systems improve. A fixed rubric keeps grading against old criteria, missing new failure modes or over-penalizing improved behavior. Agent Judge adapts through a Rubric Builder that turns evaluated trajectories and human-in-the-loop signals into improvements for the next rubric version, making the rubric a living, versioned artifact.

Benchmarking on internal production traffic for trajectory-level hallucination detection showed Agent Judge with the initial rubric achieving 0.76 accuracy, outperforming Claude Code (0.73), Codex (0.69), and LLM judges (GPT-5.4 at 0.74, mini at 0.65). After five refinement iterations, Agent Judge with Rubric Builder improved further across accuracy, recall, precision, and F1. Most notably, it stayed strongest in the hard tail of difficulty deciles while a five-judge LLM ensemble baseline degraded sharply as trajectory difficulty increased. The conclusion is that long-horizon agent evals should be done by agents with dynamic rubrics, not fixed LLM judge prompts — and that the evaluation loop can eventually feed back into agent improvement through failure diagnosis and targeted code changes.