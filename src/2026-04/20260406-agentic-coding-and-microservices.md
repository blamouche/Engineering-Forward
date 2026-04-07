# Agentic coding and microservices

**Source**: https://www.natemeyvis.com/agentic-coding-and-microservices
**Date**: April 6, 2026
**Author**: Nate Meyvis
**Keywords**: software architecture, monoliths, microservices, agentic coding, encapsulation

## Elevator pitch
Nate Meyvis argues that while LLMs reward strong encapsulation, they do not necessarily push teams toward microservices and may actually make some teams favor better-structured monoliths.

## Takeaways
- The author agrees that AI benefits from clear boundaries but rejects the idea that microservices are the only or best way to get them.
- Microservices still create hard data-sharing and deployment coordination problems that AI does not remove.
- Rapid AI-assisted iteration can increase the value of faster monolithic deploys.
- Encapsulation can be enforced inside a monolith with strong conventions and project instructions such as AGENTS.md.
- The piece reframes architecture around real coupling rather than service-count ideology.

## Synthesis
This essay is a good corrective to a simplistic meme that “AI means microservices.” The underlying truth is narrower: agents benefit from modularity, clear interfaces, and tight scopes. But those properties are not synonymous with splitting systems into many separately deployed services.

Meyvis’s argument is strongest when he focuses on the costs that do not disappear in an AI-first workflow. Shared data, cross-service dependencies, and deployment coordination remain real. In some cases AI accelerates development enough that those pain points appear sooner, not later. That makes premature service-splitting even riskier.

The essay also points to something increasingly important in practice: instruction layers and project conventions can substitute for some of the architectural clarity people previously sought through physical separation. If teams can enforce stronger boundaries through code organization, explicit rules, and agent-facing docs, they may get many of the benefits of modularity without paying the full operational tax of microservices.

The broader takeaway is that AI does not eliminate architecture tradeoffs. It changes their relative weight. Strong encapsulation matters more. Fast iteration matters more. That can make well-disciplined monoliths more attractive, not less.
