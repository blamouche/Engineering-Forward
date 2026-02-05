# Agentic Engineering
**Source**: https://addyosmani.com/blog/agentic-engineering/?utm_source=tldrnewsletter
**Date**: Unknown (published before 2026-02-05)
**Author**: Addy Osmani
**Keywords**: vibe coding, agentic engineering, AI-assisted development, testing, code review, senior skill gap

## Elevator pitch
Addy Osmani argues we need a clean distinction between reckless “vibe coding” (no review, YOLO iteration) and disciplined, professional workflows where AI agents implement under human architectural ownership—what he calls “agentic engineering.”

## Takeaways
- “Vibe coding” is specifically *not reviewing the code*; it’s great for prototypes and learning but fails hard when reality (scale, security, maintenance) arrives.
- Professional teams are getting large productivity gains by pairing agents with rigorous specs, diff review, and tests.
- “Agentic engineering” is a better term than “vibe engineering” because it’s professionally legible and signals discipline.
- The biggest differentiator is testing: a good suite lets agents iterate safely until green; without tests, agents can confidently ship broken work.
- The benefits skew senior: strong fundamentals make review/orchestration effective; juniors risk skill atrophy if they generate more than they understand.

## Synthesis
This essay is a taxonomy and a naming proposal. It starts from Andrej Karpathy’s “vibe coding” label and insists that the term has become overloaded. Originally, vibe coding meant a very specific behavior: prompt an AI, accept output without reviewing diffs, run it, paste errors back, repeat. It’s a legitimate technique for greenfield demos, one-off scripts, and exploration, where quality and long-term maintenance are not the objective.

The problem, Osmani argues, is that people now use “vibe coding” to describe disciplined AI-assisted engineering too—work that *does* include specs, architecture decisions, reviews, tests, CI, and production ownership. Conflating the two makes it harder for teams to talk honestly about risk, process, and expectations.

He proposes “agentic engineering” for the professional end of the spectrum: engineers orchestrate AI agents that can generate, test, and refine code, while humans remain accountable for architecture, correctness, and quality. The workflow he sketches is intentionally familiar: write a plan/spec; delegate well-scoped tasks; review output as if it were a junior engineer’s PR; test relentlessly; own and maintain the system. In this framing, AI doesn’t replace engineering discipline—it amplifies it. Better specs produce better output; stronger test suites make delegation safer; cleaner architectures reduce hallucinated abstractions.

The essay also calls out a skill gradient. Senior engineers can use AI as a force multiplier because they can evaluate tradeoffs and quickly spot flawed code. Juniors who rely on AI before building fundamentals risk shipping systems they can’t debug or reason about, leading to a potential long-term talent and capability gap.

Overall, the piece is useful as a shared vocabulary: “vibe coding” for playful, low-stakes speed; “agentic engineering” for serious, accountable software development with agent assistance.
