# How Warp Builds Self-Improving Agents on Claude
**Source**: https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude
**Date**: 2026-08-31
**Author**: Michael Segner (Warp / Anthropic blog)
**Keywords**: Warp, Claude, self-improving agents, agent skills, feedback loops, code review, issue triage, skill files, prompt engineering, agent orchestration

## Elevator pitch
Warp built a self-improving agent framework on Claude's platform using a two-skill pattern — an inner base skill that holds domain knowledge and an outer improver skill that periodically reviews human feedback and proposes edits to the base skill — creating a compounding loop where agent quality improves from real usage data without manual prompt tuning.

## Takeaways
- The core technique uses two skills: an inner/base skill with functional domain knowledge that runs per-task, and an outer/improver skill that runs on a schedule, pulls accumulated human feedback, compares it against what the agent suggested, and proposes a small focused edit to the base skill
- Because skills are plain files, agent improvements flow through normal PR/code-review workflows — they are reviewable, approvable, and mergeable, keeping humans in control
- Warp runs this pattern across its entire open-source repo with separate spec-writing, review, and triage agents, each carrying its own self-improvement loop
- Best practices from the Warp team: write principles not rules, explain the "why" behind instructions, make feedback effortless to give (capture it where work happens), keep skills small with progressive disclosure, and put extra effort into the reusable improver skill
- Warp has grown to 800K monthly developers and 56% of the Fortune 500 uses Warp, with 10M Claude Code sessions run inside Warp and 400K+ sessions per week
- The improver skill is highly reusable across use cases — the improver for a code review agent is not that different from the improver for any other agent

## Synthesis
Warp's self-improving agent framework, documented on the Anthropic blog, describes a deceptively simple pattern that turns stateless agent sessions into a compounding feedback loop. The central insight is that feedback to an agent — no matter how valuable — typically disappears when the session ends, removing critical context from the system. Warp's solution captures that feedback and channels it into iterative improvements to the agent's skill files.

The architecture consists of two Claude Agent Skills. The inner (or base) skill holds the functional domain knowledge and instructions for a specific task. When a PR is opened, for example, Warp's code review agent executes using this base skill and its context to produce its review. Human feedback on the agent's output — whether a simple thumbs up or detailed reasons why a code review comment was unhelpful — is captured where the work happens, directly on the PR or issue.

The outer (or improver) skill functions as an observer agent that runs on a schedule rather than per-task. It pulls the accumulated human feedback, compares what the agent suggested against how humans responded, and proposes the smallest edit that captures the feedback signals. Because skills are plain files, these updates move through the normal code review workflow: a human reviews, approves, and merges the PR, and the next run of the inner skill inherits the improvement. This final human step closes the loop and keeps a person in control of what actually changes.

Warp's issue triage agent demonstrates the pattern concretely. When someone files a GitHub issue, a GitHub Action triggers an agent that analyzes the issue for complexity, assigns labels, and suggests a fix direction. In one documented case, the triage agent missed the "ready to spec" label. A maintainer caught the gap and left feedback on the issue, explaining both what was expected and why. The outer improver skill then ran in Warp's orchestration platform (Oz), authenticated to GitHub, pulled recent issues with feedback, and proposed a PR editing the inner skill to apply the "ready to spec" label when an issue describes a real problem even if the UI shape is not yet defined.

The Warp team's best practices reveal hard-won lessons. Writing principles rather than rules lets the agent reason about the problem instead of following rigid instructions. Explaining the "why" behind a rule enables better generalization. Making feedback effortless to give — capturing it automatically where people already work, with no extra submission step — is what keeps signal flowing. Keeping skills small and using progressive disclosure (referencing resource files rather than dumping everything into context) follows Claude's own skill authoring best practices. And putting extra effort into the improver skill pays off because improver skills are reusable across different agent use cases.

The framework's distinction between skills and memory is important. Skills are procedural and stable — "how to do X," run-agnostic, changed deliberately. Memory is auto-written by the agent at inference time and never stops changing. Conflating the two leads to systems where knowledge drifts unpredictably rather than improving through deliberate review.