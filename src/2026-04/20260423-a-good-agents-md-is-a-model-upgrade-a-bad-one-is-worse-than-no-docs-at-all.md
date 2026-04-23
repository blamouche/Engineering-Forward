# A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all.

**Source**: https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files
**Date**: April 22, 2026
**Author**: Augment
**Keywords**: AGENTS.md, coding agents, documentation, prompting, software engineering

## Elevator pitch
Augment found that short, structured AGENTS.md files can materially improve coding-agent quality, while sprawling guidance and warning-heavy docs often make agents over-explore and ship worse work.

## Takeaways
- The best AGENTS.md files were concise and used progressive disclosure with linked references.
- Procedural workflows and decision tables consistently improved completion and codebase adherence.
- Short real-code examples helped reuse, but too many examples caused mis-generalization.
- Warning-only guidance pushed agents into cautious over-exploration and incomplete solutions.
- The surrounding documentation environment matters as much as the AGENTS.md entry file itself.

## Synthesis
Augment’s study is one of the more concrete attempts to measure whether agent-facing documentation actually helps coding systems do better work. The answer is yes, but only when the documentation is shaped for how agents discover and consume context. A focused AGENTS.md can act like a model upgrade by giving the system decisive guidance at the point of action. A bloated or warning-heavy one can do the opposite by pulling the agent into unnecessary reading, extra abstractions, and conservative behavior that harms completion.

The strongest patterns in the article are strikingly practical. Progressive disclosure beats comprehensive coverage. Decision tables help agents choose between multiple acceptable patterns before they write code. Numbered workflows reduce missing wiring and other implementation gaps. A few short examples from the real codebase improve reuse and convention-following. In other words, the best agent docs look less like architecture essays and more like compact operational playbooks.

The most valuable caution is the overexploration trap. When a file contains too much architecture overview or long lists of what not to do, the agent starts treating the surrounding repository as an investigation target instead of a delivery surface. It reads widely, tries to verify every possible edge case, and often ends up shipping less. That diagnosis feels important because many teams are currently responding to coding agents by adding more documentation everywhere. Augment’s evidence suggests that unstructured sprawl can actively hurt.

More broadly, the article hints at a new documentation discipline. Human-readable docs and agent-usable docs overlap, but they are not identical. Agents need concise, discoverable instructions that resolve ambiguity quickly and point to deeper material only when necessary. As coding agents become normal parts of software teams, writing good AGENTS.md files may become a real engineering skill, not a niche prompt-hacking exercise.
