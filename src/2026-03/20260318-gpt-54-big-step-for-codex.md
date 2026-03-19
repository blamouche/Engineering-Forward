# GPT 5.4 is a big step for Codex
**Source**: https://www.interconnects.ai/p/gpt-54-is-a-big-step-for-codex
**Date**: 2026-03-18
**Author**: Nathan Lambert
**Keywords**: GPT 5.4, OpenAI, Codex, Claude, agent comparison, token efficiency, context management, model philosophy, agentic AI

## Elevator pitch
GPT 5.4 is "the first OpenAI agent that feels like it can do a lot of random things"—excelling through precise instruction-following and token efficiency—while Claude appeals differently through personality and intent-understanding that don't appear on benchmarks.

## Takeaways
- GPT 5.4 marks genuine practical improvement: the first OpenAI agent that handles diverse tasks reliably, not just defined benchmarks.
- Technical strengths: superior token efficiency, better context management with less noticeable compacting, fast mode with generous rate limits.
- Philosophical distinction: "Claude will likely appeal to the newcomers, but GPT 5.4 will likely appeal to the master agent coordinator"—Claude through personality and intent-understanding; GPT 5.4 through precise instruction-following.
- Shared limitation: "light forgetfulness" when handling multiple simultaneous tasks—an important gap for complex multi-agent orchestration.
- Despite acknowledging GPT 5.4's technical advantages, Lambert still prefers typing "claude" in his terminal for subjective qualities of warmth and character.

## Synthesis
Lambert's "master agent coordinator" framing captures a real distinction in model usage patterns. Systems engineers building complex agent pipelines value predictable, precise instruction-following over personality—they want models that do exactly what they're told, not models that interpret intent helpfully but sometimes differently than specified. Claude's intent-understanding is valuable for individual users with ambiguous requirements; it's a liability in multi-agent systems where the orchestrator needs exact compliance from sub-agents.

The context compaction observation is practically important for long-running agents. When agents work on extended tasks, context windows fill and need to be compressed. Visible compaction artifacts—where the agent seems to forget or misremember earlier context—disrupt the user experience and can cause task failures. Better compaction that's less noticeable improves reliability for the tasks that matter most: complex, long-horizon work.

Lambert's personal preference for Claude despite acknowledging GPT 5.4's technical advantages is genuinely interesting data. He's an informed technical user who understands the architectural differences between the models, yet he chooses based on subjective qualities that "will never show up on benchmarks." This suggests that for daily-driver use, model personality and interaction quality compete with benchmark performance in ways that purely technical comparisons miss.

The "light forgetfulness" shared limitation points at a remaining challenge for both frontier models: multi-task execution where context about multiple parallel work streams must be maintained simultaneously. This is different from long-context understanding (where both models have improved significantly) and represents a genuine cognitive limitation in current architectures.
