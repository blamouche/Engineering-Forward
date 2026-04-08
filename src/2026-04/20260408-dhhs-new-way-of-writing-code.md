# DHH’s new way of writing code

**Source**: https://newsletter.pragmaticengineer.com/p/dhhs-new-way-of-writing-code
**Date**: April 8, 2026
**Author**: Gergely Orosz
**Keywords**: AI coding, software engineering, 37signals, DHH, Ruby on Rails, agent workflows

## Elevator pitch
DHH says the real inflection in AI coding was not autocomplete but agent harnesses good enough for senior engineers to review and merge, which is reshaping how 37signals builds software and who benefits most from the shift.

## Takeaways
- DHH’s position changed once agent-style tools became strong enough to produce code worth serious review instead of noisy autocomplete.
- He now works with multiple models in parallel and uses the terminal plus git-centric review as the control surface.
- Rails benefits from AI because its conventions, integrated testing, and readability make agent output easier to validate.
- AI compounds the advantage of senior engineers who can judge correctness and product quality quickly.
- 37signals’ long-standing small-team, design-heavy model may become more mainstream as agents increase individual leverage.

## Synthesis
The interesting shift in this conversation is that DHH does not present himself as having adopted a new philosophy so much as having finally encountered tools that satisfy old standards of craftsmanship. Six months earlier, AI coding felt like intrusive autocomplete. Now, with stronger models and agent harnesses, he describes a workflow where the machine can generate whole chunks of work and the human stays in charge of review, direction, and taste. That distinction matters because it frames the current wave less as 'AI writes code for me' and more as 'I can supervise far more execution than before.'

His setup reflects that stance. Instead of surrendering to a monolithic IDE experience, he uses multiple models in tmux, keeps neovim in the middle, and reviews diffs through existing developer tools. That makes the AI layer feel like an accelerator bolted onto a mature engineering workflow, not a replacement for it. There is also a strong argument here for why Rails is well positioned in the agent era: the framework’s conventions, batteries-included testing, and readable defaults reduce ambiguity for both models and reviewers. The less time you spend inferring intent from bespoke patterns, the more easily you can let agents operate at speed.

The wider implication is organizational. DHH sees senior engineers gaining disproportionately because they can tell good output from plausible nonsense, while junior engineers face a harder path to learning by doing. At the same time, he suggests AI could reinforce 37signals’ model in which designers are also implementers and small teams own more of the product end to end. So the article is not just about one founder changing his mind on AI coding. It is about the convergence of tool quality, team structure, and engineering maturity into a new default where software development becomes more supervisory, taste-driven, and asymmetric in who can benefit fastest.
