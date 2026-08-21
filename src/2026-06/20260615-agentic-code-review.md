# Agentic Code Review: The Most Leveraged Skill in Software
**Source**: https://addyosmani.com/blog/agentic-code-review/
**Date**: 2026-06-15
**Author**: Addy Osmani
**Keywords**: code review, agentic engineering, AI coding agents, verification bottleneck, Faros AI, CodeRabbit, GitClear, comprehension debt, blast radius, review capacity

## Elevator pitch
AI coding agents have made writing code cheap but kept understanding it exactly as expensive—making code review the most leveraged skill in software, with 2026 data showing 4x raw output but only ~12% delivered value gain, and the gap between those numbers being entirely review work.

## Takeaways
- Faros AI's 22,000-developer study found code churn up 861%, per-developer defect rate up from 9% to 54%, review duration up 441%, and zero-review merges up 31% as AI adoption increased
- GitClear data shows daily AI users produce ~4x raw output but only ~12% real productivity gain—the gap between those numbers is the review problem in one line
- CodeRabbit found AI-coauthored PRs carry ~1.7x more issues: logic problems up 75%, security issues 1.5-2x more common, readability problems tripled
- GitHub reports 60M+ Copilot reviews run, with 1-in-5 reviews on the platform involving an agent—a 10x increase in under a year
- Review needs scale with blast radius: solo developers with no users need less review, but large organizations with old codebases face every alarming figure at full strength

## Synthesis
Addy Osmani's analysis of agentic code review cuts through the productivity debate with hard data from four independent sources. The central insight is that the "happy accident" of code review—where senior engineers could read code faster than juniors could write it—no longer holds. AI agents produce a thousand lines of code faster than a human can read this paragraph, while human reading speed hasn't changed. The bottleneck moved from generation to verification.

The data is striking in its consistency. Faros AI instrumented 22,000 developers and found that as teams moved from low to high AI adoption, throughput climbed but so did everything bad: code churn up 861%, defect rates up from 9% to 54% per developer, review duration up 441%, and perhaps most alarmingly, zero-review merges up 31%. Nobody decided to stop reviewing—reviewers simply couldn't keep pace. CodeRabbit's study of 470 open source PRs found AI-coauthored changes carried 1.7x more issues, with security problems 1.5-2x more common. GitClear's headline number crystallizes the problem: 4x the code for ~12% more delivered value.

Osmani is careful to contextualize by blast radius. A solo developer shipping a side project with no users faces a fundamentally different problem than a team maintaining a ten-year-old payments system. The three variables—blast radius, code longevity, and team size—determine what "good review" means. Most bad advice in this space comes from one position on the spectrum prescribing to another.

The practical recommendations center on tiered review: treating changes by risk level, requiring evidence (test plans, regression coverage, performance baselines) for higher-risk changes, and using AI agents themselves as review triage tools. Osmani describes pointing Claude Code or Codex at incoming PR queues for triage—a meta-application of AI to manage the volume AI created.

The organizational warning is sharp: reducing engineering headcount because "AI made us faster" is dangerous unless you've closed the review gap first. The senior-engineer tax—review time up by triple digits—falls hardest on the people organizations can least afford to bottleneck. Teams that do well over the next few years won't be those generating the most code, but those who built a review system they can actually trust.