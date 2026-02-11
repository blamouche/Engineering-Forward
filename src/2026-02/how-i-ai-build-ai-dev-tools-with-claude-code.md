# 🎙️ This week on How I AI: How to build your own AI developer tools with Claude Code
**Source**: https://www.lennysnewsletter.com/p/this-week-on-how-i-ai-how-to-build?publication_id=10845&post_id=187026884&isFreemail=true&r=fhb7r&triedRedirect=true
**Date**: Unknown
**Author**: Lenny Rachitsky (host), featuring CJ Hess
**Keywords**: Claude Code, developer tools, workflows, model-vs-model review, visual planning

## Elevator pitch
A practical walkthrough of a “custom dev tools” workflow: use Claude Code for intent-heavy generation, wrap planning in visual artifacts, and pair it with a second model (Codex) as an adversarial reviewer to raise code quality.

## Takeaways
- Claude is described as especially good at intent understanding and steerability for complex tasks.
- “Skills” (prompt/tooling recipes) turn one-off workflows into reusable capabilities.
- Visual planning (flowcharts, mockups) can reduce cognitive load vs text-only plans.
- Model-vs-model review: one model generates, another audits for smells and inconsistencies.
- With the right harness and safeguards, AI can plausibly cover the majority of front-end implementation.

## Synthesis
The interesting idea here isn’t just “use Claude Code,” but the shape of an emerging engineering loop: (1) externalize intent and constraints, (2) convert plans into artifacts humans can quickly validate (visual flowcharts, UI mockups), and (3) treat code review as an *adversarial* process by introducing a second model optimized for critique.

The “skills” angle is the compounding mechanism. Instead of repeatedly prompting ad hoc, CJ encodes instructions so Claude reliably outputs tool-specific JSON or structured plans that downstream tools can render. That effectively creates a personalized dev environment where the model learns the *local dialect* of your stack. Over time, the tool evolves and the skills evolve with it—so the workflow becomes faster and less fragile.

Visual planning is also a reminder that the bottleneck is increasingly human attention, not code generation. A text plan may be correct but still hard to evaluate quickly; a flowchart or mock UI compresses validation time and makes it easier to spot missing states, bad edge-case handling, or mismatched screens. In agentic engineering, “time-to-human-approval” becomes a key metric.

Finally, the model-vs-model pattern is a pragmatic response to the reality that no single model is best at everything. Generation and critique are different cognitive modes; using two specialized systems reduces correlated failures. The implication for teams is that the “best” setup might be a small portfolio of models plus a harness that routes tasks, enforces constraints, and integrates results into a tight feedback loop (tests + review + artifact validation).
