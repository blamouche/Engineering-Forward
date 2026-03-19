# Vibe Check: Opus 4.6—The Best Coding Model We've Tested (With Some Maddening Habits)
**Source**: https://every.to/vibe-check/opus-4-6
**Date**: 2026-02-05
**Author**: Dan Shipper, Katie Parrott
**Keywords**: Opus 4.6, Anthropic, coding model, adaptive thinking, iOS coding, extended thinking, agentic AI, code review

## Elevator pitch
Opus 4.6 solved a real iOS coding task that stumped GPT-5.3 Codex and Opus 4.5—earning the title "best AI coder we've tested"—but exhibits slowness, verbosity, and "classic Claudisms" (unexpected code modifications) that require closer oversight.

## Takeaways
- Solved a complex iOS architectural task that stumped both GPT-5.3 Codex and Opus 4.5, demonstrating genuine capability advancement.
- Adaptive Thinking replaces Extended Thinking: automatically adjusts reasoning depth based on task complexity rather than requiring manual activation.
- Parallel task processing enabled by Adaptive Thinking without manual prompting—particularly beneficial for complex knowledge work.
- Trade-offs: slower and more verbose than predecessors; "classic Claudisms" include unexpected code modifications and occasional overestimation of capabilities.
- Writing quality: more collaborative drafting experience than 4.5, but blind testing showed preference for 4.5's prose—Opus 4.6 exhibits more "AI-isms" in style.

## Synthesis
The "best AI coder we've tested" claim with the caveat "requires closer oversight" captures a real tension in frontier model development: capability improvements at the frontier often come with behavioral changes that affect usability. Opus 4.6's improved problem-solving on hard architectural tasks is real and valuable; the unexpected code modifications are a genuine reliability concern for production use.

Adaptive Thinking is architecturally more elegant than Extended Thinking's manual activation. When developers must decide whether to enable extended reasoning for a given task, they need to correctly predict which tasks will benefit—a meta-cognitive task that adds overhead. Automatic reasoning depth adjustment removes this decision from the developer's workflow while theoretically achieving the same quality improvements on complex tasks.

The "classic Claudisms" observation refers to a pattern that Claude models have exhibited: taking initiative to improve code beyond what was asked, which is sometimes helpful and sometimes confusing or disruptive. For developers using AI coding tools in tightly scoped review loops, unexpected modifications are a real problem: they introduce changes that weren't requested, which must be evaluated before the requested change can be assessed. This is a quality assurance cost that offsets part of the productivity gain.

The blind writing test finding—that testers preferred Opus 4.5's prose despite finding 4.6's drafting more collaborative—reflects something real about reasoning models and writing. More capable reasoners tend to produce writing that is more structurally sound but more formulaic in expression. The "AI-isms" Shipper and Parrott identify are the stylistic signatures of highly competent, optimized-for-quality generation rather than natural human expression.
