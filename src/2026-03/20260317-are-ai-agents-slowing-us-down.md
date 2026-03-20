# Are AI Agents Actually Slowing Us Down?
**Source**: https://newsletter.pragmaticengineer.com/p/are-ai-agents-actually-slowing-us
**Date**: 2026-03-17
**Author**: Gergely Orosz
**Keywords**: AI agents, software quality, technical debt, Anthropic, Amazon, Meta, Uber, productivity paradox

## Elevator pitch
Gergely Orosz documents a troubling pattern: as AI coding tools proliferate and are measured through token usage and PR velocity, software quality is declining—Anthropic's own site had obvious bugs, Amazon experienced AI-related outages, and Sentry warns of bloated unmaintainable code.

## Takeaways
- Anthropic's website had an obvious bug losing user input despite Claude generating 80% of production code internally
- Amazon required senior engineer approval for junior engineers' AI-generated changes after experiencing a "trend of incidents"
- Meta and Uber track token usage in performance reviews, incentivizing volume over quality
- OpenCode's founder warns AI agents lower shipping standards while discouraging necessary refactoring
- Sentry's CTO observes AI produces "bloated, hard-to-maintain code that slows long-term development"—turning initial velocity gains into future velocity debt

## Synthesis
Gergely Orosz's investigation into whether AI agents are actually improving software engineering arrives at an uncomfortable finding: the productivity gains are real but may be temporary, and the quality costs are already manifesting in observable ways at some of the world's most sophisticated engineering organizations.

The Anthropic case is particularly striking. The company that makes Claude uses Claude to generate approximately 80% of its production code—yet its flagship website contained an obvious bug that lost user input, visible to any visitor who tested basic form functionality. The implication is not that AI coding tools are bad at producing code, but that the human review practices designed to catch quality issues are being bypassed or diluted when AI is generating the volume. High-velocity AI-assisted development appears to create conditions where bugs that would previously have been caught in review accumulate undetected.

Amazon's response is revealing: requiring senior engineer approval for junior engineers' AI-generated code changes represents a manual quality gate inserted to counter the quality degradation that AI assistance was creating. This is a significant organizational overhead—essentially adding a review layer not to catch the junior engineer's conceptual errors, but to catch the AI's code quality issues that the junior engineer missed or accepted uncritically.

The incentive structure problem that Meta and Uber have created is concerning. Tracking engineer token usage and celebrating developers who generate 52% more pull requests creates direct career incentives for volume over quality. Engineers in these environments face a rational choice: produce more AI-assisted work at lower quality standards, or produce less at higher standards and perform poorly in reviews. Most will choose their careers.

The longer-term risk Orosz surfaces through the Sentry CTO's observation is perhaps the most serious: AI-generated code tends toward verbosity and specificity over generality and abstraction. The accumulated technical debt from thousands of verbose, specific, untested AI-generated implementations creates a codebase that is increasingly expensive to modify—turning the initial velocity gain into a future velocity tax that compounds over time.
