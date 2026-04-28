# Batch API is terrible for one agent. It might be great for a fleet.

**Source**: https://eran.sandler.co.il/post/2026-04-27-batch-api-is-terrible-for-one-agent/
**Date**: April 28, 2026
**Author**: Unknown
**Keywords**: eran, batch, terrible, agent, might, great, fleet

## Elevator pitch
Wrapping every agent turn in a single-entry batch is the wrong way to use Anthropic's Batch API - and that's exactly what makes it interesting

## Takeaways
- What does an agent harness feel like when every model turn goes through Anthropic’s Batch API instead of the synchronous endpoint?
- For anyone burning real money on agents (eval suites, background subagents, anything that runs unattended), half-price tokens are the kind of number that makes you stop and squint.
- The trade is latency: batches are asynchronous, with up to a 24-hour processing window.
- So I built a tiny harness to find out what that actually feels like.
- The result is batching-harness , a single-file Python REPL that wraps every turn in a one-entry batch, polls until it ends, and runs the tool loop on top.

## Synthesis
What does an agent harness feel like when every model turn goes through Anthropic’s Batch API instead of the synchronous endpoint? For anyone burning real money on agents (eval suites, background subagents, anything that runs unattended), half-price tokens are the kind of number that makes you stop and squint. The trade is latency: batches are asynchronous, with up to a 24-hour processing window. So I built a tiny harness to find out what that actually feels like. The result is batching-harness , a single-file Python REPL that wraps every turn in a one-entry batch, polls until it ends, and runs the tool loop on top. rich for the terminal UI, sandbox-runtime (bubblewrap on Linux, Seatbelt on macOS) to keep the bash tool from nuking my home directory, and a /stats panel that compares what I paid via batch against what I would have paid via the synchronous endpoint. The sandbox setup here is intentionally minimal: just enough to keep an experiment from going sideways. For real execution-layer security for AI agents across models, harnesses, and frameworks, that’s AgentSH , my main project. What I actually wanted to know The experiment isn’t whether the Batch API works. The interesting question is what the agent loop looks like when every turn is async.
