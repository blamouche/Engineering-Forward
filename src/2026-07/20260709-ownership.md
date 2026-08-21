# Ownership
**Source**: https://registerspill.thorstenball.com/p/ownership
**Date**: 2026-07-09
**Author**: Thorsten Ball
**Keywords**: ownership, engineering culture, software engineering, startups, shipping, juniors, end-to-end responsibility

## Elevator pitch
Ownership means taking a problem from "we have a problem" to "we don't have to think about it again"—and the complete checklist of what that actually requires in a small engineering team.

## Takeaways
- Ownership means solving a problem end-to-end: from identification through deployment to follow-up, not just writing the code.
- The ownership checklist includes: understanding the actual problem (not jumping to a solution), thinking about edge cases, handling failures, considering data flow, testing (both automated and manual), deployment verification, communication to stakeholders, and follow-up.
- Before merging, ask yourself: "Am I proud of this? Would I show this to John Carmack and say 'here's what I built, under these constraints, with these tradeoffs?'"
- For juniors, the expectation isn't to do all of these things immediately, but to aspire to one day being able to—and until then, to ask for help.
- The checklist is a mental framework, not a requirement that every item must be checked off for every task—many items won't apply to simple changes.

## Synthesis
Thorsten Ball's essay on ownership, originally shared as an internal Slack message with his Amp teammates, captures a philosophy that's simple to state but hard to practice: when you own something, you own it completely, from problem to resolved state.

The essay is essentially a comprehensive checklist of what "done" actually means. It starts with problem identification—many engineers jump to "we need to migrate from X to Y" without asking whether that's really the problem or just their preferred solution. It continues through edge cases, failure handling, data considerations, testing strategy, deployment, communication, and follow-up. Each item represents a way that "done" can quietly become "not actually done."

The John Carmack standard is particularly resonant. Ball asks engineers to evaluate their work against the question: "Am I proud of this? Would I show this to John Carmack?" This isn't about perfectionism—it's about having thought through the tradeoffs and being able to defend them. The constraints are acknowledged; what matters is making deliberate choices within those constraints rather than accidentally leaving gaps.

Ball addresses the junior question directly: he doesn't expect juniors to execute the full checklist immediately, but he does expect them to read it and aspire to it. The key distinction is between not knowing how to do something (which is fine—ask for help) and implicitly assuming someone else will handle the parts you haven't thought about (which is not fine).

For small teams without dedicated PMs or QA departments, this philosophy is essential. There's no one else to catch the things you drop. But even in larger organizations, the mindset of end-to-end ownership—understanding the full scope of what "done" means—is what separates engineers who ship reliably from those who ship and then spend as much time fixing as building.