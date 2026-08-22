# What I'm Finding About LLM Code Style and Token Costs
**Source**: https://www.jimmont.com/llm-style-token-costs
**Date**: 2026-06-25
**Author**: Jim Montgomery
**Keywords**: token costs, LLM code generation, Web APIs, Deno, code style, output tokens, security

## Elevator pitch
LLMs generate code patterns from their training data that cost 7-10x more output tokens than necessary because they don't know to use the native Web APIs your runtime already ships — and the fix is a single directive in your prompt.

## Takeaways
- Output tokens cost 3-5x more than input tokens in API pricing, making LLM-generated verbose code patterns significantly more expensive than necessary
- LLMs default to legacy Node.js patterns (manual URL parsing, per-field form state, custom abort timers) because those dominate their training corpus, generating ~140 tokens vs ~12 tokens for native Web API equivalents
- The gap between what the model defaults to and what the platform already provides is where most output token cost lives — a Deno handler using native APIs runs 60-90 tokens vs 400-600 in the model's default style
- Native APIs eliminate categories of bugs: manual query string parsing is a prototype pollution vector, manual decodeURIComponent fails silently on malformed input, custom modal focus management breaks accessibility
- Comments aren't neutral for LLMs — research shows models follow comment intent even when it contradicts the code, and stale comments actively degrade LLM comprehension below the no-comment baseline

## Synthesis
Jim Montgomery's investigation into LLM code style and token costs reveals a structural inefficiency that has been hiding in plain sight. The core finding is that LLMs generate code patterns from their training data — patterns dominated by legacy Node.js approaches — that cost dramatically more in output tokens than the native Web APIs that modern runtimes already ship. Since output tokens cost 3-5x more than input tokens in API pricing, this inefficiency compounds quickly in production.

The magnitude of the problem is striking. For query parameter parsing, the model's default manual approach generates ~140 tokens; the native `URLSearchParams` equivalent generates ~12 — a 90% reduction per occurrence. For form data handling, the model generates 200+ tokens of per-field state tracking versus 14 tokens using `FormData`. A complete Deno request handler written in the model's default style runs 400-600 output tokens for boilerplate alone; the same handler using native APIs runs 60-90 tokens. This is not a marginal optimization — it's a 7-10x difference in infrastructure code cost.

The security implications are equally important. Manual query string parsing with `params[key] = value` is a prototype pollution vector. Manual `decodeURIComponent` fails silently on malformed input. Custom `setTimeout`-based abort patterns leak when cleanup paths are missed during refactoring. The native implementations are spec-compliant, tested against the Web Platform Tests suite, and handle edge cases correctly by definition. The model's hand-rolled equivalents handle whatever the author thought of that day.

The comment findings from MITRE research add a surprising dimension. Comments are not neutral metadata for LLMs — models treat them as authoritative input. Inaccurate comments that describe what code used to do before a refactor actively degrade LLM comprehension below the no-comment baseline. This means stale comments are not just harmless clutter; they are misinformation with authority that actively misleads the model.

The practical solution is remarkably simple: an explicit directive at the start of the session naming specific APIs ("use Web APIs natively: URL, URLSearchParams, FormData, AbortController, fetch, Headers, Request, Response, Promise.allSettled()") produces the most visible difference in output quality and cost. The model doesn't know what your runtime ships unless you tell it, and once you do, it's consistent about using native APIs. The biggest lever here — using what the platform already built — isn't a new coding technique. It's closing the gap between the model's training-data defaults and the platform's actual capabilities.