# AI rewards strict APIs

**Source**: https://dri.es/ai-rewards-strict-apis
**Date**: Unknown
**Author**: Dries Buytaert
**Keywords**: AI coding agents, strict APIs, Drupal, developer tooling, software architecture

## Elevator pitch
As coding work shifts toward AI assistance, the real productivity edge comes less from reducing boilerplate than from using strict, typed, validated APIs that shorten the feedback loop and reduce ambiguous failure modes.

## Takeaways
- Dries Buytaert argues that AI agents fail more on ambiguity than on complexity.
- Strict APIs make bindings explicit, type-checkable, and easier for tools or agents to follow end to end.
- Loose patterns such as magic strings, conventions, and unvalidated configuration create silent failures that waste debugging cycles and tokens.
- Drupal's long shift toward services, routing, attributes, and configuration validation is presented as an AI-era advantage.
- Architectural strictness, once debated as style or ergonomics, increasingly becomes a speed and cost issue for AI-assisted development.

## Synthesis
This article argues that AI-assisted software development changes the economics of API design. In older debates, strict interfaces and typed contracts often looked like a tradeoff: more boilerplate and steeper learning curves in exchange for clarity and reliability. Buytaert's claim is that this tradeoff shifts when an AI coding agent is part of the implementation loop. Agents are not especially harmed by boilerplate, but they are highly sensitive to ambiguity, silent failures, and conventions that are only implied rather than enforced.

The article's most concrete comparison is between explicit, typed bindings and older magic-string mechanisms. In loose systems, a function name, hook string, or configuration key can be wrong without producing a meaningful error. The result is not necessarily a crash. More often, nothing happens, and the developer or agent must infer what failed by trial and error. That is exactly the kind of environment in which an AI agent wastes time, burns tokens, and may still converge on the wrong fix. By contrast, explicit attributes, registered services, and validated schemas create a trail that static analysis, IDEs, and agents can inspect directly.

Drupal is used as the main example of a platform that happened to move in this direction before the AI wave made the benefits newly obvious. The article points to Drupal's migration toward Symfony services, routing, event dispatching, attributes, and configuration validation as choices that were painful from a backward-compatibility perspective but now create better feedback loops for agent-assisted work. The important idea is that strictness is not just about cleanliness. It turns more implementation mistakes into legible errors located near the root cause.

That makes the argument broader than Drupal versus WordPress. It is really about how software systems expose affordances to machine collaborators. If architecture relies heavily on conventions, undocumented magic, or unvalidated runtime behavior, then the system may remain usable for experienced humans while becoming much slower for agents to navigate. Conversely, a strict system can make both human and machine work more predictable, but the cost now shows up less as inconvenience and more as a measurable productivity advantage.

Overall, the article reframes API discipline as operational leverage in the AI era. What once looked like style preference or framework philosophy now affects how quickly agent-assisted tools can move from intent to correct implementation. In that sense, strict APIs are becoming part of the performance profile of a software platform, not just part of its aesthetic.