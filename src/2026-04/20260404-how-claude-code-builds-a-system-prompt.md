# How Claude Code Builds a System Prompt

**Source**: https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html
**Date**: April 4, 2026
**Author**: Daniel Breunig
**Keywords**: Claude Code, system prompt, context engineering, AI agents, harness design, prompt assembly

## Elevator pitch
Daniel Breunig uses the leaked Claude Code source to show that the real product surface of an agent is the dynamic system-prompt assembly logic, not just the underlying model.

## Takeaways
- Claude Code’s prompt is assembled from many conditional components rather than a single static instruction block.
- The harness decides what guidance is always present, what is environment-specific, and what is activated only when certain tools or modes are enabled.
- This assembly logic reveals product priorities such as tool preference, safety boundaries, verbosity control, and context management.
- The article strengthens the case that “context engineering” is now a product discipline in its own right.
- For agent builders, prompt quality depends as much on orchestration and conditional structure as on model capability.

## Synthesis
Daniel Breunig’s article is valuable because it shifts attention from the final text of an extracted system prompt to the machinery that constructs it. Most discussions about prompts still assume there is a single magic string somewhere in the product. Breunig argues that this is increasingly the wrong mental model. In a serious agent product, the prompt is not static. It is assembled dynamically from many modules, some always present, some conditional on enabled tools, some tied to runtime environment, and others adapted to user preferences or operating mode.

The leaked Claude Code source offers a rare window into that assembly process. Breunig’s reconstruction shows just how much product logic now lives in context composition. Instructions about when to ask for confirmation, when to favor dedicated tools over shell commands, how concise to be, whether subagents are available, how skills are surfaced, how temporary directories are used, and how context is cached are all part of the agent’s effective behavior. In other words, the “system prompt” is really a packaging layer for product policy. It is where interface design, safety posture, workflow constraints, and model behavior all meet.

That matters because it clarifies why two tools using similar frontier models can feel dramatically different in practice. The difference is not only training data or raw capability. It is the harness: what context is injected, when it is injected, what instructions are omitted under certain modes, and how the tool stack is explained to the model. Breunig’s mapping makes the hidden product layer visible. The system prompt is not an implementation detail; it is a core part of the user experience.

The article also helps explain why context engineering is becoming a discipline rather than a hack. Once prompts are modular, product teams can reason about them like software: defaults, conditional branches, feature flags, cache boundaries, and environment-specific overrides. That creates a path toward more maintainable and testable agent behavior. It also raises the bar. If prompt assembly is now product architecture, weak structure will create confusing, inconsistent agents even when the underlying model is strong.

For teams building their own agents, the practical lesson is straightforward. Do not think only in terms of “writing a better prompt.” Think in terms of assembling the right context for the right situation. The winning products will likely be the ones that treat prompt construction as systems design: breaking instructions into components, attaching them to explicit conditions, and tuning the context boundary as carefully as any API surface. Breunig’s article shows that the future of agent quality is as much about how the prompt is built as what the prompt says.
