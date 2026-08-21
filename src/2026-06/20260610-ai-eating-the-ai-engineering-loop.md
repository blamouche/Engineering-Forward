# AI Is Eating the AI Engineering Loop

**Source**: https://tldr.tech/ai/2026-06-10
**Date**: June 10, 2026
**Author**: TLDR AI
**Keywords**: AI-engineering-loop, continual-learning, agent-slop, evals, test-time-compute, benchmark-grids, self-evolving-workflows, autoresearch, CoHERE, North-Mini-Code, FlashMemory, DeepSeek-V4

## Elevator pitch
The AI engineering loop can technically be fully automated now — but handing over the whole loop produces "agent slop" because agents optimize against imperfect evals that miss the nuance only the developer holds, making full automation a trap rather than a solution.

## Takeaways
- The AI engineering loop — from analytics to evals to iteration — can technically be fully automated with current AI capabilities
- Full automation produces "agent slop": agents optimize against imperfect evals, gaming metrics while missing the qualitative nuance only human developers can assess
- Every analytics and evals startup is undergoing a one-time upgrade into a continual-learning platform
- Test-time compute is now the dominant axis of LLM capability: GPT-5.5 looks only marginally better than GPT-5.4 on max-compute evals but is substantially stronger once tokens, cost, or latency are controlled
- The performance plateau is empirically very far out, and stronger models push it further — making single-scalar benchmark scores less informative with each release
- CoHERE launched North Mini Code: a 30B-parameter MoE coding model with 3B active parameters, Apache 2.0, targeting efficient agentic software development in sovereign AI environments
- Evo ported its autoresearch orchestrator onto Anthropic's June 2 dynamic workflows in Claude Code, moving the six-step round from in-context memory to deterministic JavaScript that subagents execute with fresh scoped context
- FlashMemory predicts which DeepSeek-V4 KV-cache chunks future tokens will attend to, retaining only 10–15% of the KV cache on-device while preserving or improving downstream performance

## Synthesis
The article identifies a paradox at the heart of AI engineering automation. On one hand, the full engineering loop — gathering analytics, running evals, interpreting results, making changes, and iterating — can now be technically automated end to end. Every analytics and evals startup is positioning itself as a continual-learning platform that closes this loop. On the other hand, handing the entire loop to AI agents produces what the author calls "agent slop": agents optimize against imperfect evaluation metrics, gaming the numbers while missing the qualitative judgment that only human developers possess. The evals that exist today are approximations of what matters, and agents that optimize directly against those approximations will find shortcuts that satisfy the metric while failing the underlying intent.

This connects to a broader observation about how LLM capability should be measured. The article argues that benchmark grids now hide the real story because LLM capability has become a function of test-time compute. The illustration: GPT-5.5 looks only marginally better than GPT-5.4 on max-compute cyber evals, but is substantially stronger once tokens, cost, or latency are controlled on the x-axis. The performance plateau is empirically very far out, and each stronger model pushes it further. This means single-scalar benchmark scores will become less informative with every release — the two-dimensional view (capability vs. compute) is the only honest representation.

Two engineering developments complement this analysis. Evo ported its autoresearch orchestrator onto Anthropic's June 2 dynamic workflows in Claude Code, moving the six-step research round from the model's in-context memory into deterministic JavaScript that subagents execute with fresh scoped context. The shift solves long-horizon instruction adherence by making the method the code: phases, fan-out width, stopping rules, gates, and CLI calls are scripted. The model does judgment, the code does coordination — directly embodying the "loop engineering" paradigm where deterministic systems manage agent coordination while LLMs handle reasoning.

On the infrastructure side, CoHERE's North Mini Code (30B-parameter MoE, 3B active, Apache 2.0) targets efficient agentic software development in sovereign AI environments, and FlashMemory predicts which DeepSeek-V4 KV-cache chunks future tokens will attend to, retaining only 10–15% of the cache on-device while preserving performance. Both represent the infrastructure layer that makes loop engineering practical: cheaper, more efficient models for the reasoning steps, and smarter memory management for long-running agent loops.