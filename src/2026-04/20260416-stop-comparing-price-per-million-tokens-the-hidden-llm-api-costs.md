# Stop comparing price per million tokens: the hidden LLM API costs

**Source**: https://www.tensorzero.com/blog/stop-comparing-price-per-million-tokens-the-hidden-llm-api-costs/
**Date**: April 16, 2026
**Author**: Unknown
**Keywords**: tensorzero, stop, comparing, price, million, tokens, hidden, costs

## Elevator pitch
Stop comparing price per million tokens: the hidden LLM API costs.

## Takeaways
- Stop comparing price per million tokens: the hidden LLM API costs April 16, 2026 · Gabriel Bianconi Summary Token pricing is misleading: the same input produces 2.65x+ more tokens depending on the model.
- We got wildly different token counts from identical content using OpenAI, Anthropic, and Google’s official token counting APIs.
- Text, JSON, YAML, and tool definitions all tokenize differently.
- The cheapest provider changes depending on what you’re sending.
- The only way to know what you’re actually paying is to measure it.

## Synthesis
Stop comparing price per million tokens: the hidden LLM API costs April 16, 2026 · Gabriel Bianconi Summary Token pricing is misleading: the same input produces 2.65x+ more tokens depending on the model. We got wildly different token counts from identical content using OpenAI, Anthropic, and Google’s official token counting APIs. Text, JSON, YAML, and tool definitions all tokenize differently. The cheapest provider changes depending on what you’re sending. The only way to know what you’re actually paying is to measure it. On tool-heavy workloads, claude-opus-4-7 costs 5.3x more than gpt-5.4 despite list prices being only 2x apart. Most engineers know they need to evaluate models on their specific task because performance varies. But so does cost: the same input can cost several times more on one provider than another, even when their list prices look similar. The typical metric for comparing LLM API costs is price per million tokens ($/MTok). Here’s what the major providers charge today: Model $/MTok (input) gemini-3.1-pro-preview $2.00 gpt-5.4 $2.50 claude-sonnet-4-6 $3.00 claude-opus-4-6 $5.00 claude-opus-4-7 $5.00 But not all tokens are equal!
