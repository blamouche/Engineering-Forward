# Turn Claude From a Chatbot Into a Thinking Partner 🧠
**Source**: https://linas.substack.com/p/thinkwithclaude?publication_id=81819&post_id=187367623&isFreemail=true&r=fhb7r&triedRedirect=true&utm_source=substack&utm_medium=email
**Date**: Unknown
**Author**: Linas (newsletter)
**Keywords**: prompting, Claude, prompt engineering, structure, examples, constraints

## Elevator pitch
A practical prompt-structuring playbook: choose the right model tier, make instructions specific, wrap context in XML tags, provide examples, and constrain outputs so Claude behaves less like a generic chatbot and more like a deliberate reasoning partner.

## Takeaways
- Model selection matters: “workhorse” vs “deep thinking” vs “fast/cheap” tiers.
- Specificity is the highest-leverage variable; vague prompts yield vague outputs.
- XML tagging helps separate context, instructions, constraints, and output formats.
- Few-shot examples outperform abstract style guidance.
- Explicit constraints (“don’t do X”, word limits, no fluff) reduce “AI voice” failure modes.

## Synthesis
The piece is effectively a checklist for turning prompting into a lightweight specification discipline. The underlying claim is simple: most disappointing outputs are not caused by model incapability, but by ambiguous requirements. The proposed remedy is to write prompts the way you’d brief a brilliant but literal new hire: concrete goals, clear boundaries, and unambiguous success criteria.

The structural techniques (XML tags, explicit output formats) are not magic incantations; they’re guardrails that reduce instruction collision. As prompts grow, models can blur what is background vs what is the task, or ignore constraints buried mid-paragraph. Tagging makes the prompt parseable and therefore easier to follow.

Examples are positioned as the strongest steering mechanism because they remove interpretation. Instead of telling the model “be executive,” you show an executive-style output. This matters because many failures are “style/format mismatches” rather than factual errors.

The author also emphasizes negative constraints—explicitly forbidding common filler or behaviors. That’s a useful counterpoint to the typical “add more context” advice: sometimes the right move is to *delete degrees of freedom* so the model can’t wander into default patterns.

In the context of agentic workflows, this reads like a recipe for building reusable “skills”: standardized prompt templates that encode your preferred structure, guardrails, and output contracts. Once those are stable, you can layer tools and automation on top (parsers, validators, downstream renderers), which is how prompting turns from art into system design.
