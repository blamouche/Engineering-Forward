# Bugbot now self-improves with learned rules

**Source**: https://cursor.com/blog/bugbot-learning
**Date**: April 9, 2026
**Author**: Cursor
**Keywords**: Cursor, Bugbot, code review, learned rules, feedback loops, developer tools, self-improving agents

## Elevator pitch
Cursor is turning live PR outcomes into repository-specific Bugbot rules, aiming to move AI code review from static heuristics toward continuous, feedback-driven adaptation.

## Takeaways
- Cursor says Bugbot’s public-repo bug resolution rate has climbed from 52% at launch to roughly 78%.
- The new learned-rules system turns comment reactions, replies, and human reviewer feedback into candidate rules.
- Rules can be promoted, disabled, edited, or deleted based on ongoing signal from future PRs.
- The goal is to let Bugbot encode repo-specific patterns and priorities rather than operate as a one-size-fits-all reviewer.
- This pushes code review tooling toward an online-learning loop instead of relying only on offline model and prompt tuning.

## Synthesis
The key idea here is not simply that Bugbot got better. It is that Cursor is trying to shift improvement from an offline product cycle into the flow of real development work. Up to now, most AI coding tools have improved like traditional SaaS products: internal experiments, occasional model changes, and periodic launches. Learned rules changes that by treating every pull request as training signal about what was useful, what was noisy, and what the reviewer should notice next time.

That matters because code review quality is deeply contextual. Different repositories care about different invariants, business logic, architecture rules, and levels of strictness. A generic review model can catch broad classes of bugs, but it will always plateau if it cannot internalize local norms. Cursor’s rule system is a practical answer to that problem. Instead of pretending the model can infer everything from the diff, it builds a memory layer that accumulates repository-specific feedback and uses it to steer future reviews.

There is also a broader product lesson here. The most effective AI systems increasingly look less like static assistants and more like closed feedback loops. They observe outcomes, convert signal into reusable guidance, and then re-enter the workflow in a slightly improved form. That is exactly how many human teams get better too. Cursor is essentially operationalizing that pattern for code review, with the UI giving users some control over what the system learns and keeps active.

The implication is that the next generation of developer tools may compete as much on learning loops as on base model quality. If one product can adapt to a team’s codebase and priorities faster than another, raw intelligence may matter less than situated relevance. Bugbot’s learned rules are an early example of that shift. They suggest that durable advantage in AI coding tools will come from how well the system absorbs and compounds real-world feedback, not just from how smart it looked on day one.
