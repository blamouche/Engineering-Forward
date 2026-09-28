# Open-Source Jev That Runs on CPU
**Source**: Unwind AI (unwindai@mail.beehiiv.com)
**Date**: 2026-09-28
**Author**: Unwind AI
**Keywords**: Jev, Julia 1, Supersonic Labs, decision models, CPU inference, mmBERT, TypeSafe, jev-router, OpenRouter, MCP tools, Google Cloud API Gateway, Claude Code, GLM-5.3-Flash, Ollaya, Gemini 3.8 Flash TTS, DeepSeek DSec, Agent Tincan, jevgrep

## Elevator pitch
Unwind AI covers Julia 1, a 144.3M open-source decision model from Supersonic Labs that mimics Jev's architecture on CPU, plus new Jev-powered routing from TypeSafe/OpenRouter, REST-to-MCP conversion via Google Cloud API Gateway, and DeepSeek's sandbox infrastructure paper for agent training at scale.

## Takeaways
- Supersonic Labs released Julia 1, a 144.3M parameter decision model built on multilingual mmBERT-small — not Jev weights or a Qwen fine-tune — that runs entirely on CPU, achieving ~5 decisions per second on a Samsung tablet
- TypeSafe and OpenRouter shipped jev-router, a cache-aware router powered by Jev that scores requests before an LLM call to pick the right model and reasoning effort, avoiding unnecessary token spend
- Google Cloud API Gateway can now turn REST APIs into MCP tools by annotating OpenAPI specs — the gateway serves REST operations as MCP tools on the /mcp path without a separate server, though tools/list is unauthenticated by default
- Claude Code now tries to find a graceful stopping point when hitting the five-hour session limit mid-task, with a small allowance from the weekly limit — Pro users get one wrap-up per week, Max/Team Premium get one per five-hour limit hit
- DeepSeek published DSec, a paper describing the sandbox infrastructure for large-scale agentic training, with function-calling, container, microVM, and full-VM backends through one SDK
- Agent Tincan by Matt Van Horn lets agents across different products (Grok Bot, Muse, Codex, Claude Code, ChatGPT) communicate with each other via a Tailscale-hosted relay

## Synthesis
Unwind AI's September 28 issue focuses on the rapid proliferation of decision models following TypeSafe's Jev. The headline story is Julia 1 from Supersonic Labs: a 144.3M parameter model that takes context, a question, and a changing set of possible answers, then returns scores instead of generating prose — exactly like Jev, but built independently on multilingual mmBERT-small rather than Jev weights or a Qwen fine-tune. The model runs entirely on CPU, including about 5 decisions per second on a Samsung tablet, making it the first genuinely portable open-source alternative to Jev for edge and low-infference-cost scenarios.

The Jev ecosystem is expanding fast. TypeSafe and OpenRouter shipped jev-router, which uses Jev to score a request before any LLM call, choosing the model plus reasoning effort to balance quality, speed, and cost. This is significant because it moves the routing decision to a purpose-built model rather than spending tokens on a general LLM to discover which model should have been called. Meanwhile, Privatemode demonstrated that GLM-5.3-Flash can be prompted to imitate a Jev-style decision system by making the first output token answer the question — a single forward pass produces a typed decision, but it remains a prompting technique on a standard LLM, not a purpose-trained model, so Jev is still several times cheaper.

On the infrastructure side, Google Cloud API Gateway now converts REST APIs into MCP tools by annotating existing OpenAPI specs — the gateway serves operations as MCP tools on the /mcp path without a separate server. One production caveat: tools/list is unauthenticated by default, and Google recommends securing discovery with JWT because API keys cannot protect that method. DeepSeek's DSec paper reveals the sandbox layer behind agent training at scale, exposing function-calling, container, microVM, and full-VM backends through one SDK with placement, lifecycle, memory sharing, image loading, and reward-hacking mitigation.

The issue also highlights Agent Tincan, which lets agents from completely different products ask one another for help — Grok Bot can ask Muse to call a restaurant, any agent can retrieve an old Claude chat, and the reply travels back without the user becoming the copy-paste layer. This requires a Tailscale network and one always-on machine, but it points toward an interoperable agent ecosystem where the boundaries between products become less rigid.