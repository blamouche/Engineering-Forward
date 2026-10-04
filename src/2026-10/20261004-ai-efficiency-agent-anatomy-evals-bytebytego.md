# Six Techniques for Efficient AI Systems, the Anatomy of an AI Agent, and How to Evaluate AI Apps
**Source**: ByteByteGo (bytebytego@substack.com)
**Date**: 2026-10-03
**Author**: ByteByteGo
**Keywords**: LLM serving, streaming, quantization, continuous batching, prefix caching, paged KV cache, speculative decoding, AI agent architecture, planning, tools, memory, guardrails, AI evaluation, LLM-as-judge, evals, CI/CD, red-teaming

## Elevator pitch
ByteByteGo's EP228 newsletter covers three AI engineering topics in one issue: six techniques for serving LLMs efficiently at scale (streaming, quantization, continuous batching, prefix caching, paged KV cache, speculative decoding), a breakdown of AI agent anatomy (brain, planning, tools, memory, loop, guardrails), and a practical three-step recipe for evaluating AI applications (pick a task, collect eval data, develop a grader using code-based, model-based, and human graders).

## Takeaways
### Top 6 Techniques to Make Your AI System Efficient
- **Streaming**: The model sends each token as soon as it's ready, changing perceived latency to time-to-first-token
- **Quantization**: Convert model weights to lower precision like FP8 for less memory usage, faster and cheaper serving
- **Continuous batching**: New requests join the batch as slots free up, keeping the GPU less idle
- **Prefix caching**: Cache internal calculations for given input prompts; if a prompt has a cached prefix, those calculations are skipped
- **Paged KV cache**: Store cache in fixed-size blocks instead of one contiguous chunk; blocks are allocated as sequences grow, so memory isn't reserved up front
- **Speculative decoding**: A small model (speculator) proposes multiple tokens, then the main model verifies them in one forward pass

### The Anatomy of an AI Agent
- An AI agent is essentially a while-loop: use an LLM to select an action, execute it, evaluate the result, and repeat until the task is complete
- **Brain**: The LLM is the core — the shift from chatbot to agent is that the model makes choices, not just text
- **Planning**: Hard tasks need multiple steps; methods include Chain of Thought, Tree of Thoughts, and Reflexion (learn from mistakes and retry)
- **Tools**: Functions the model can call — web search, code execution, APIs, files, browsers (often via the MCP standard)
- **Memory**: Short-term memory is the context window; long-term memory lives in vector stores, files, and knowledge bases; when the window fills, agents summarize old turns and carry the summary forward
- **Loop**: All four pieces work in a cycle — look at current state, decide, use a tool, see the result, repeat
- **Guardrails**: Sandboxing, human checks, token limits, output validation, and scope limits keep autonomy from turning into expensive chaos

### How Do You Know If Your AI App Actually Works?
- Every good eval is a three-step recipe: pick a task, collect eval data, develop a grader
- **Step 1 — Pick a task**: For LLMs it can be safety or math capability; for RAG it can be grounding and retrieval
- **Step 2 — Collect eval data**: Gather inputs paired with the right answer or expected behavior (e.g., a safety set pairs risky prompts with "refuse")
- **Step 3 — Develop a grader**: Use code-based graders (if/else, unit tests) for clear correct answers, model-based graders (LLM-as-judge) for subjective tasks like safety, and human graders for edge cases where nuance matters more than throughput
- Most production evals combine all three: code-based for what's cheap to check, model-based for scale, human-based for what matters most
- ByteByteGo's new "AI Evals in Practice" course (starts Oct 7) covers designing evals for quality/safety/reliability/cost/latency, building LLM-as-a-Judge systems, red-teaming agents for prompt injection and jailbreaks, creating eval datasets from real and synthetic data, and running evals in CI/CD to catch regressions and drift

## Synthesis
ByteByteGo's EP228 system design refresher bundles three AI engineering primers into a single issue, each pitched at practitioners building production systems.

The first section addresses the cost of serving LLMs at scale. Six techniques are presented as a toolkit: streaming reduces perceived latency to time-to-first-token; quantization (FP8) cuts memory and cost; continuous batching keeps GPUs busy by filling slots as they free up; prefix caching skips redundant computation for repeated prompt prefixes; paged KV cache allocates memory in fixed-size blocks rather than reserving it up front; and speculative decoding uses a small model to propose tokens that the main model verifies in a single forward pass. The framing is practical — each technique is described in terms of what it changes at runtime, not just theory.

The second section decomposes AI agent architecture into five components plus a loop and guardrails. The key insight is that an agent is a while-loop, not a pipeline: the LLM selects an action, the system executes it, the result is evaluated, and the cycle repeats until done. The brain (LLM) makes choices rather than generating text. Planning methods (Chain of Thought, Tree of Thoughts, Reflexion) turn fuzzy goals into clear actions. Tools — often accessed via the MCP standard — give the model real capabilities. Memory spans the context window (short-term) and vector stores or files (long-term), with summarization as the bridge when the window fills. Guardrails (sandboxing, human checks, token limits, output validation) become more critical as autonomy increases.

The third section tackles the question every AI team faces: how do you know your app actually works? The answer is a three-step eval recipe — pick a task, collect eval data paired with expected behavior, and develop a grader. The grader taxonomy is the most useful part: code-based graders for deterministic checks, model-based graders (LLM-as-judge) for subjective tasks at scale, and human graders for edge cases. Production evals combine all three. The issue also announces a new "AI Evals in Practice" course starting October 7, covering eval design across quality/safety/reliability/cost/latency, LLM-as-a-Judge systems, red-teaming for prompt injection and jailbreaks, synthetic eval datasets, and running evals in CI/CD to catch regressions and drift.