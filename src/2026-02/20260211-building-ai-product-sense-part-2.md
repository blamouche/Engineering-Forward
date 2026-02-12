# Building AI product sense, part 2
**Source**: https://www.lennysnewsletter.com/p/building-ai-product-sense-part-2?publication_id=10845&post_id=186661807&isFreemail=true&r=fhb7r&triedRedirect=true
**Date**: Unknown
**Author**: Dr. Marily Nika (via Lenny’s Newsletter)
**Keywords**: product management, AI, evaluation, failure modes, guardrails, trust

## Elevator pitch
AI product sense is less about clever prompts and more about systematically *surfacing failure modes* early—then defining minimum quality and guardrails—so the product behaves predictably when real users bring ambiguity and messy inputs.

## Takeaways
- Meta’s “Product Sense with AI” interview signals a shift: PMs are judged on managing uncertainty with models.
- Ritual #1: deliberately push models into hallucination-prone situations (messy Slack threads, ambiguous asks).
- Map the system’s failure signatures and define intended behavior explicitly.
- Define “minimum viable quality” (MVQ) before shipping; be explicit about what “good enough” means.
- Design guardrails: constraints, clarification steps, retrieval, UI nudges, and system boundaries.

## Synthesis
This piece is pragmatic PM advice for the era where “the demo works” but production fails. The key observation is that LLMs often respond to ambiguity by inventing structure—confidently. That behavior isn’t a rare edge case; it’s a default pattern. So the PM’s job becomes anticipating where users will be vague, emotional, inconsistent, or underspecified, and then designing the product so the system either (a) asks clarifying questions, (b) refuses safely, or (c) transparently communicates uncertainty.

The proposed weekly ritual is effectively a lightweight red-teaming exercise. You take real messy inputs (Slack snippets, meeting notes, Jira comments), ask the model to do something “strategic,” observe how it hallucinates, then add a minimal guardrail (“only include explicitly mentioned items; otherwise say not enough information”) and see what changes. That contrast teaches you both the model’s current behavior and what constraints are required for trustworthy output.

Framing this as “AI product sense” is useful because it moves evaluation upstream. Instead of waiting for users to teach you the failure modes through churn and trust loss, you proactively map the failure signature. MVQ then becomes the product contract: what counts as acceptable behavior under ambiguity, and what is a hard stop.

The deeper implication is that AI PM work becomes more like systems engineering: define behavior, measure it, and add guardrails where the probabilistic core breaks. Teams that develop this muscle will ship more reliable AI features—and will waste less time arguing whether the issue is “a model problem” or “a product problem.”