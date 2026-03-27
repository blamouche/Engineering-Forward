# How to Do AI-Assisted Engineering
**Source**: https://newsletter.eng-leadership.com/p/how-to-do-ai-assisted-engineering
**Date**: 2026-03-27
**Author**: Gregor Ojstersek
**Keywords**: AI-assisted engineering, workflows, code review, planning, tooling

## Elevator pitch
A compilation of engineering leaders describing how they structure AI-assisted development, emphasizing rigorous planning, multi-pass review, and workflow standardization over ad‑hoc prompting.

## Takeaways
- The biggest gains come from better design and review, not faster typing.
- Structured workflows (requirements → plan → implement → review) reduce AI-induced drift.
- Multiple agents or roles help separate concerns (security, performance, correctness).
- AI magnifies existing process quality; weak processes create more tech debt faster.
- Human judgment remains essential for architecture, risk, and final merge decisions.

## Synthesis
This special edition of the Engineering Leadership newsletter aggregates perspectives from engineers, managers, and founders on how they actually use AI in day‑to‑day software work. The common thread is that AI is treated as a high‑leverage collaborator, but only inside a structured process that keeps quality and accountability intact. Contributors describe starting with explicit problem statements, requirements, and design artifacts before asking AI to generate code. Several emphasize that AI’s real value is shifting effort from implementation to design and review. When code generation is cheap, iteration becomes the bottleneck, so teams invest more time in architecture, tradeoff analysis, and careful specification. AI is fast, but it is not a substitute for technical judgment; it accelerates good decisions and amplifies bad ones.

Many respondents describe multi‑step workflows: convert requirements into a development plan, review and refine that plan, then implement with tests written alongside code. These processes commonly include a second AI reviewer or a human review pass focused on correctness, security, and maintainability. Some teams run AI review on every pull request, regardless of who authored the code, to provide consistent feedback and catch issues outside strict syntax errors. The idea is to separate generation from verification and avoid “first‑draft shipping.” Multiple contributors also highlight using different AI “modes” or specialists for different concerns—product reasoning, architecture, security, performance, or code style—to prevent conflicting goals from being mashed together.

Workflow standardization is a recurring theme. Teams codify their expectations in instruction files and reusable prompts or skills so they don’t have to restate constraints each session. This includes commit conventions, review checklists, PR templates, and tooling integrations. Several contributors note that AI works best when prompts are structured, inputs are explicit, and the agent has access to relevant context: architecture docs, prior decisions, and examples from the existing codebase. This reduces hallucinations and keeps outputs aligned with established patterns.

Another pattern is delegating operational or repetitive work to AI, while reserving judgment‑heavy tasks for humans. AI can scaffold endpoints, refactor across files, or draft tests and documentation quickly. But teams keep humans in the loop for critical decisions, especially around deployments, risk, and product strategy. Even when AI contributes to testing, reviewers validate that tests are meaningful and not merely confirming that mocks behave as mocks.

Finally, the article highlights the organizational impact of AI. Effective use requires investment in process and culture: clear documentation, disciplined review, and a willingness to iterate on specs until they are right. AI does not eliminate engineering rigor; it demands more of it. The most successful workflows treat AI as a force multiplier that increases the value of good practices like design docs, thoughtful reviews, and continuous refinement rather than as a shortcut around them.