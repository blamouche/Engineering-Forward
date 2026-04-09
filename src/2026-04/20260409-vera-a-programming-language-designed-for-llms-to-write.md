# Vera: A programming language designed for LLMs to write, not humans

**Source**: https://veralang.dev/
**Date**: April 9, 2026
**Author**: Allan Allan
**Keywords**: Vera, programming languages, LLMs, verification, contracts, De Bruijn indices, agent tooling

## Elevator pitch
Vera is an experiment in redesigning programming language ergonomics around machine authorship, replacing naming freedom and implicit behavior with structurally referenced bindings, mandatory contracts, typed effects, and verification-first feedback.

## Takeaways
- Vera assumes that the main weakness of model-written code is not syntax but maintaining coherence, invariants, and naming discipline across larger programs.
- The language removes variable names in favor of typed structural references, aiming to reduce a class of naming-related hallucinations.
- Contracts, effect declarations, and refinement-style constraints are mandatory so correctness can be checked mechanically instead of guessed.
- Compiler diagnostics are intentionally written as natural-language repair instructions for LLMs, treating errors as part of the agent interface.
- The project suggests a broader thesis: if models become primary code authors, languages and tooling may evolve to optimize for machine-checkability rather than human convenience.

## Synthesis
Vera is interesting less as a likely mass-adoption language and more as a sharp provocation about where software tooling could go if LLMs become primary code producers. Most languages evolved around human ergonomics: readability, expressiveness, shorthand, naming, and developer preference. Vera inverts that assumption. It asks what a language would look like if the top priority were not making humans comfortable, but making model-generated programs easier to verify, repair, and reason about mechanically.

That framing explains its unusual design choices. Replacing variable names with typed structural references sounds hostile to humans, but it directly targets a known model failure mode: inconsistent naming and scope confusion. Mandatory contracts and typed effects push the same way. Instead of trusting the model to implicitly do the right thing, Vera tries to make the important properties explicit and checkable. The compiler becomes less a passive parser than an active supervisor, with diagnostics designed to guide another machine toward a fix. That is a fascinating shift because it treats the language, compiler, and agent as one combined system.

The strongest idea here may be the notion of ‘checkability over correctness.’ Models do not need to be omniscient if the environment makes wrong outputs easy to detect and repair. That aligns with a lot of current agent practice, where the best systems win not by generating perfect first drafts, but by operating inside loops with tests, validators, and constrained interfaces. Vera extends that philosophy all the way down to the language level.

Whether Vera itself wins is almost secondary. The project matters because it makes visible a design space many people are only vaguely gesturing at. If AI-written code becomes common, we may eventually see more languages, DSLs, or frameworks that trade some human elegance for machine legibility and proof. Vera is one of the clearer early examples of that future being taken seriously enough to prototype.
