# Understanding Is the New Bottleneck
**Source**: https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck.html
**Date**: 2026-07-02
**Author**: Geoffrey Litt (Notion)
**Keywords**: AI agents, code understanding, cognitive debt, human-AI collaboration, education, literate diffs, micro-worlds, shared spaces

## Elevator pitch
As AI agents write more code, the bottleneck shifts from writing to understanding — and the solution isn't just verification but active participation, borrowing techniques from education to keep humans creatively engaged with agent-built systems.

## Takeaways
- The common answer to "why understand code?" is "to verify" — but agents are getting better at self-verification, so the deeper answer is "to participate": understanding gives you the concepts needed to come up with the next idea and evolve the system.
- Cognitive debt (popularized by Margaret Storey and Simon Willison) is like tech debt: you can skip understanding in the short term, but it eventually bites you when you've lost the plot of your own system.
- Technique 1 — Explanations: the `/explain-diff` skill produces structured code explainers with background info, intuition before details, literate diffs (prose-structured walkthroughs), and interactive quizzes that act as speed regulators on the AI loop.
- Technique 2 — Micro-worlds: inspired by Seymour Papert's "Mathland" concept, these are interactive environments you inhabit to naturally intuit how a system works — like a Prolog debugger that lets you step through execution and leave comments.
- Technique 3 — Shared spaces: teams need shared mental models to communicate efficiently; Notion's collaborative pages where humans and agents (Claude, Cursor) work together create shared understanding instead of siloed work.

## Synthesis
Geoffrey Litt's talk at the AI Engineer conference challenges a common assumption in the AI coding discourse: that the goal is to remove humans from the loop. He argues that understanding remains essential — not merely to verify agent output (a thumbs-up/thumbs-down check that agents are increasingly doing themselves), but to participate in the creative process. A project is many iterative loops with an agent, and the understanding you carry from one loop to the next is what enables you to think creatively about how to evolve the system. Without that fluency, your ability to contribute is meaningfully limited.

The talk draws a crucial distinction between verification and participation. Verification is a binary check — does the code match the spec, is it well-architected? As agents improve at self-verification, the human's role in this capacity diminishes. But participation is open-ended: it's about having a rich enough mental model to propose the next direction, spot opportunities, and make creative decisions. This frames understanding not as a quality-control cost but as a creative capability.

The three techniques Litt presents borrow explicitly from education theory. The `/explain-diff` skill is the most developed: it produces structured code explainers that teach background info before diving into changes, build intuition before showing code, and present diffs as prose rather than alphabetical file lists. The embedded quiz at the bottom acts as a "speed regulator" — a mechanical check that prevents the AI loop from running faster than human understanding. Litt's rule: he won't send code to others until he can pass the quiz. This is a practical pattern any team can adopt.

Micro-worlds take the educational analogy further, drawing on Seymour Papert's vision of "living in Mathland" — environments where you learn concepts naturally through interaction. Litt built a Prolog debugger that let him step through execution, scrub through time, and see the stack — and the key insight is that building the debugger himself (with agent help) is how he developed understanding, rather than letting the agent debug for him. This is a subtle but important point: the activity of building understanding tools is itself the understanding-building process.

The shared spaces technique addresses the team dimension. When everyone holds the same mental model, communication is efficient — you can "jam and riff" with shared vocabulary. Litt notes that Notion now supports running Claude and Cursor agents directly in collaborative pages, so technical plans are created in shared spaces where teams can comment and discuss, rather than in individual silos. This extends the understanding-building from individuals to groups.

The talk closes with a reference to Alan Kay's 50-year-old vision of computers as a medium for helping people understand complex concepts through interactive simulations. Litt argues that AI makes creating such simulations accessible — and that the point was always to augment, not just automate. The optimistic conclusion: with the right tools, we can understand the world better than ever, getting deeper into the loop rather than removing ourselves from it.