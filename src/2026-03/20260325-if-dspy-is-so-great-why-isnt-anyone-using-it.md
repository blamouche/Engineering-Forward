# If DSPy is So Great, Why Isn't Anyone Using It?
**Source**: https://skylarbpayne.com/posts/dspy-engineering-patterns/
**Date**: Unknown
**Author**: Unknown
**Keywords**: DSPy, LLM engineering, prompts, RAG, evals

## Elevator pitch
The post argues that many AI teams reinvent pieces of DSPy as their systems scale, and that DSPy’s unfamiliar abstractions—not lack of value—explain its low adoption.

## Takeaways
- DSPy’s adoption lags despite benefits like model flexibility, maintainability, and focus on context.
- Teams often rebuild DSPy features ad hoc as their AI systems mature.
- Typical evolution includes prompt management, structured outputs, retries, RAG, and evaluation pipelines.
- DSPy packages these patterns into signatures, modules, and optimizers that are model-agnostic.
- The core barrier is cognitive: DSPy forces engineers to rethink how they build LLM systems.

## Synthesis
The article tackles a practical question: if DSPy solves core AI engineering problems, why doesn’t it see broader adoption? The author argues the issue isn’t that DSPy is wrong, but that it is hard. Its abstractions are unfamiliar and require a shift in how engineers think about LLM systems. In the short term, most teams just want to make the pain go away, so they build incremental fixes instead of adopting a new framework. The result, in the author’s view, is “DSPy at home”: ad hoc, fragmented implementations of the same ideas, built slowly and with more bugs.

To make the point, the article walks through the typical lifecycle of an AI system using a simple extraction task. Stage one is a basic prompt call that “works.” As product demands faster iteration, teams add prompt storage and editing, turning prompts into database-driven templates. Next comes structured outputs to combat format inconsistencies, then retries and fallbacks for transient failures. As tasks become more complex, RAG is layered in, introducing extra prompts, embedding models, retrieval parameters, and interdependencies between them. Finally, teams realize they need evals to measure whether changes improve performance or cause regressions. Each stage is logical on its own, but the accumulation creates a brittle, homegrown framework that recreates DSPy’s architecture without the cohesive design.

The author argues DSPy was built to formalize these patterns. It provides typed signatures for inputs and outputs, composable modules that chain behaviors, and optimizers that tune prompts and examples systematically. With DSPy, swapping models or providers becomes a configuration change rather than a multi-day refactor. Evaluation and optimization are integrated into the same pipeline rather than bolted on after the fact. In other words, DSPy encodes separation of concerns and composability—principles that software engineers already understand—into LLM workflows.

The deeper claim is that engineers are likely to end up building something like DSPy anyway. As systems scale, the probability of needing model-agnostic interfaces, reliable evaluation, and reusable components approaches certainty. DSPy simply exposes those requirements early and packages them as first-class abstractions. The resistance, then, is psychological: engineers are comfortable with imperative prompts and quick patches, and DSPy pushes them toward a declarative, pipeline-driven mental model that feels unfamiliar.

Overall, the post frames DSPy adoption as a product of organizational readiness rather than technical merit. Teams that are still in the “ship it” phase may not feel the pain that DSPy addresses. But as complexity grows—multiple models, RAG stacks, evaluation suites, and evolving prompts—teams tend to recreate DSPy anyway. The author suggests that adopting DSPy sooner can save time and prevent the accumulation of brittle infrastructure, but only if teams are willing to embrace a different way of thinking about AI system design.