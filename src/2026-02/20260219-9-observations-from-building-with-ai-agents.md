# 9 Observations from Building with AI Agents
**Source**: https://tomtunguz.com/9-observations-using-ai-agents/
**Date**: 2026-02-19
**Author**: Tomasz Tunguz
**Keywords**: ai, agents, engineering

## Elevator pitch
Tomasz Tunguz shares nine practical lessons from building agent systems, from prototyping on frontier models to using static typing, agent critiques, and automated prompt optimization.

## Takeaways
- Start with frontier models for messy inputs, then fine-tune for stable tasks.
- Static typing and compiler checks reduce hallucinated code errors.
- Competing agents improve plans and implementations through critique loops.
- Closed-loop prompt optimization and logging drive steady quality gains.
- Cost-performance parity across models shifts optimization toward tooling and workflow design.

## Synthesis
Tomasz Tunguz distills a year of building AI agent systems into nine pragmatic observations focused on reliability, workflow design, and cost-aware engineering. His first point is to prototype with the best available models when inputs are messy or unpredictable. For tasks like email parsing or transcription, the top frontier models are most robust. Once a task and its inputs stabilize, he recommends specializing the model—either through fine-tuning or a smaller model—to improve cost and latency while retaining adequate accuracy. He illustrates this by fine-tuning Qwen 3 for a task classification problem, achieving strong results on an 8B model that runs locally.

A key engineering insight is that static typing functions like spell-check for AI-written code. Tunguz found that dynamically typed languages allow agents to produce plausible but incorrect code that fails at runtime. Using a language with a strong type system and compilation checks forces the model to confront errors early, increasing one-shot success rates for medium-complexity tasks. This is a practical recommendation for teams deciding how to structure agent-assisted code generation: tooling that enforces correctness early can compensate for model hallucination.

He emphasizes the value of “agent rivals” in decision loops. His workflow uses one agent to draft a plan, then other models to critique it, after which the original agent incorporates critiques and implements the solution. The cycle repeats with critique of the implementation against the plan. This creates a structured adversarial review process that leverages differences among models and reduces blind spots. The framing is that agents are effective micromanagers when used as a coordinated braintrust rather than a single voice.

Another theme is unifying the toolchain. Tunguz describes agent development as mixing different “clays”: memory management, prompt templates, logging, and evaluation. He wants these components in one system because improvement is a closed loop from prompt to output to evaluation and back. That loop enables systematic optimization rather than ad hoc tinkering.

He observes that the model landscape has entered an “iPhone 15 era,” where multiple open and frontier models are now strong enough for common workflow tool-calling. Benchmarks like Tau2 suggest models have reached a capability threshold where additional intelligence yields diminishing returns for many tasks. As a result, the competitive edge moves to cost and product design rather than raw model accuracy, encouraging teams to focus on the surrounding system rather than chasing the latest model release.

Documentation and tracing are central in his approach. Tunguz cites the idea that in AI systems, traces document the app. His team runs nightly prompt optimization using the last 100 conversations, extracting failures and generating improved prompts via an LLM-as-judge. This produces incremental quality improvements week over week without manual intervention. The key is logging and structured evaluation—without traces, agent systems are opaque and hard to improve.

He also recommends separating prompt updates from deployment. Agents watch a prompt file and reload when it changes, enabling continuous experimentation without downtime. Combined with versioned prompt files, this yields rollback capabilities similar to software deployments. This fits a DSPy-style workflow where prompts evolve through programmatic optimization rather than manual tweaks.

Finally, Tunguz draws a line between skills and code. Skills are for interactive conversations and are easier to debug because failures are localized. Agent code chains many function calls, which makes failures harder to diagnose without disciplined logging. The practical implication is to choose the right abstraction—skills for human-facing interactions, code for automated agents—and to invest in observability when chaining functions.

Overall, the nine observations emphasize that agent performance depends at least as much on system design—typing discipline, critique loops, logging, and prompt ops—as on the choice of model. The post encourages teams to treat agent development like engineering a production system: start with the best, specialize, instrument everything, and continuously refine.
