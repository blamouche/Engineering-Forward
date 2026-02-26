# GPT-5-Codex Prompting Guide
**Source**: https://cookbook.openai.com/examples/gpt-5-codex_prompting_guide
**Date**: 2025-09-23
**Author**: Dave Leo
**Keywords**: GPT-5-Codex, prompting, Responses API, coding agents, tools

## Elevator pitch
A concise guide to prompting GPT-5-Codex, highlighting how its agentic coding focus changes prompt structure, tool usage, and the right level of instruction detail.

## Takeaways
- GPT-5-Codex is not a drop-in replacement for other GPT models; it expects different prompt patterns.
- The model is available through the Responses API, which makes tool use and reasoning steps first-class.
- Best results come from short, concrete instructions rather than long, over-specified prompts.
- Tool usage should be explicit but minimal, with clear success criteria and constraints.
- The guide emphasizes iteration: test a prompt, observe behavior, then refine with smaller changes.

## Synthesis
The GPT-5-Codex Prompting Guide reframes prompting as an engineering activity tailored to a model optimized for agentic coding tasks rather than general chat. Instead of treating GPT-5-Codex as a drop-in replacement for other GPT variants, the guide argues for prompt structures that align with how the model plans and executes code-centric workflows. The headline message is that Codex behaves best when given direct, concrete tasks with crisp boundaries, and that the Responses API is the primary interface for accessing its strengths. That API model encourages you to specify tools, structure outputs, and keep task state tight, which changes how you should design prompts.

A central emphasis is on brevity and specificity. The guide suggests that long system messages and verbose instructions can degrade performance because they obscure the immediate objective. GPT-5-Codex does not need repeated framing of what it is; it needs a compact goal, constraints, and the minimum context required to succeed. That means reducing preambles, trimming background explanations, and using short, testable directives. When the job is to update a file, compile code, or refactor a module, the best prompts read like well-formed tickets: one request, with acceptance criteria and the exact boundaries of what is in and out of scope.

Because Codex is optimized for tool-assisted work, the guide treats tool invocation as a core part of prompt design. Rather than asking the model to think in the abstract, you define which tools are available and when to use them. This makes the work more reliable because the model can consult files, run tests, and inspect outputs as part of the workflow. The guide suggests keeping the tool chain lean: only provide tools that are required for the task, and be explicit about what success looks like. This helps avoid tool thrashing and keeps the agent aligned with the intended workflow.

Another key message is that prompting is iterative. GPT-5-Codex can behave differently from other models, so you should treat prompts as hypotheses to be tested. The guide recommends making small adjustments, observing the change in behavior, and avoiding big prompt rewrites that make it hard to attribute improvements. This mirrors standard engineering practice: small diffs, measurable outcomes. Over time, these iterations converge on prompts that are robust across similar tasks.

The guide also clarifies that the model expects a more operational style of instruction. Instead of “explain how to do X,” you should ask it to “do X,” with clear constraints. The change in framing shifts the model from explanation to execution. This is particularly important when Codex is part of a larger workflow that depends on deterministic steps, such as updating a repository or generating code against a known interface. The guide advocates describing the target state, listing constraints, and specifying what not to touch. It treats prompts as executable specifications rather than conversational requests.

Taken together, the guide positions GPT-5-Codex as a specialized agent for coding tasks that thrives under tight, explicit direction. By aligning the prompt with the Responses API, minimizing unnecessary context, and iterating with small changes, teams can make Codex more reliable and faster to integrate into real engineering workflows. The takeaway is less about prompt “craft” and more about prompt “design”: define the smallest set of instructions that let the agent succeed, then tighten and iterate as you would with any piece of production software.
