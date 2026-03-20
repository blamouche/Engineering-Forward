# Lossless Claw: LCM Plugin for OpenClaw
**Source**: https://github.com/martian-engineering/lossless-claw
**Date**: 2026-03-20
**Author**: Martian Engineering
**Keywords**: context management, OpenClaw, LCM, DAG, summarization, SQLite, token limits, conversation history

## Elevator pitch
Lossless Claw implements Lossless Context Management for OpenClaw, preserving every conversation message through hierarchical DAG summarization rather than discarding history when token limits are reached.

## Takeaways
- Persists all messages in SQLite while keeping active context within model token limits through hierarchical summarization
- Creates a directed acyclic graph (DAG) of summarization, condensing older chunks while preserving recent messages raw
- Three tools for historical recall: `lcm_grep` (search), `lcm_describe` (explain), `lcm_expand` (retrieve detail)
- Configurable parameters: context thresholds, message tail protection, token budgets, session exclusion patterns
- MIT licensed, Go implementation with interactive terminal UI for database management

## Synthesis
Context window management is one of the most practically frustrating aspects of extended AI agent sessions. Standard behavior when reaching the token limit is brutal: older messages are truncated or summarized lossy, effectively erasing the agent's memory of earlier work. For long research sessions, multi-day projects, or complex debugging investigations, this truncation can erase critical context—problem definitions, rejected approaches, discovered constraints—that the agent needs to avoid repeating mistakes or losing track of goals.

Lossless Claw implements an alternative strategy inspired by the LCM (Lossless Context Management) research paper. The core insight is that "lossless" doesn't mean keeping everything in the active context window—it means ensuring that everything is accessible even if not immediately present. The system persists every message to SQLite, creating a permanent record that survives context window overflow. The active context window then contains a carefully constructed blend: recent messages in their original form (preserved with high fidelity) plus hierarchical summaries of older content.

The DAG summarization structure is the technical heart of the approach. Rather than a flat list of summaries, the system builds a hierarchical condensation: message chunks are summarized, those summaries are summarized again as they age, creating progressively more compressed representations of increasingly distant history. This mirrors how human memory works—recent events are remembered in detail, older events in outline, distant events in gist—and it enables the system to maintain awareness of long history within bounded token budgets.

The three recall tools (`lcm_grep`, `lcm_describe`, `lcm_expand`) give the agent—and the user—a mechanism for recovering detail from compressed history when needed. If a summarized earlier section becomes relevant to the current task, `lcm_expand` retrieves the original messages. This makes the system genuinely lossless in the meaningful sense: nothing is permanently discarded, everything is recoverable on demand.

The configurable parameters address the practical tuning requirements of different workflows. Research sessions, coding sessions, and document review sessions have different optimal balances between active context richness and historical depth.
