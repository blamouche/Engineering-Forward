# Deep Dive: How Claude Code's /insights Command Works
**Source**: https://www.zolkos.com/2026/02/04/deep-dive-how-claude-codes-insights-command-works.html?utm_source=tldrai
**Date**: 2026-02-04
**Author**: Zolkos
**Keywords**: Claude Code, insights, telemetry, session logs, qualitative analysis, report generation

## Elevator pitch
A detailed reverse-engineering walkthrough of Claude Code’s `/insights` feature: how it gathers local session logs, extracts structured metadata and qualitative “facets” via LLM prompts, aggregates results, and renders an interactive HTML report.

## Takeaways
- `/insights` is a multi-stage pipeline: collect logs → filter sessions → extract metadata → (optionally) chunk/summarize long transcripts → LLM facet extraction → aggregation → multi-prompt insight generation → HTML rendering.
- It explicitly filters out sub-sessions and internal operations to focus on “real” user sessions.
- The system mixes quantitative telemetry (tokens, tools, edits, durations) with qualitative judgments (“facets”) extracted from transcripts.
- Caching facets makes subsequent runs faster and cheaper.
- The prompts try to reduce over-attribution by counting only explicit user goals and explicit satisfaction/friction signals.

## Synthesis
This post dissects the mechanics behind Claude Code’s `/insights` command, which produces a comprehensive HTML report about how you use Claude Code over time. The core claim is that the feature is not just a simple stats dump; it’s a layered analysis pipeline that combines local log processing with targeted LLM calls.

The pipeline starts by collecting session transcripts from the local Claude Code projects directory and filtering out things that would skew the analysis: agent sub-sessions, internal analysis runs, extremely short sessions, and sessions with too few user turns. From the remaining sessions it extracts structured metadata—timing, token counts, tool usage, languages inferred from file extensions, and even development activity signals like git commits/pushes and code churn.

For long transcripts, the system performs a preprocessing step: chunking and summarizing the transcript to stay within model context limits while preserving salient details such as filenames, errors, and user feedback. The heart of the qualitative layer is “facet extraction,” where an LLM is prompted to convert a session transcript into a JSON object describing the underlying goal, categorized intent counts, outcome, satisfaction signals, friction types, and a brief summary.

The post emphasizes guardrails in these prompts. For example, goal categories are meant to reflect what the user explicitly asked for—not what the assistant decided to explore autonomously—reducing the risk of mischaracterizing user intent. Likewise, satisfaction is based on explicit user signals (“thanks”, “that’s not right”) rather than inferred sentiment.

After facet extraction, the system aggregates data across sessions and runs additional specialized prompts to generate higher-level insights: project areas, interaction style, what works well, friction patterns, and actionable suggestions. Finally, it renders the output into an interactive HTML report stored locally.

Taken together, the article is a useful blueprint for anyone building “developer analytics” for agentic tooling: treat raw telemetry as necessary but incomplete, add qualitative extraction with explicit schemas, cache intermediate artifacts, and use multiple narrow prompts rather than one monolithic “analyze everything” call.
