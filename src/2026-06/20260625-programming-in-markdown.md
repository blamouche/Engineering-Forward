# Stop Programming in Markdown: Don't Use a Prompted LLM When Regular Code Will Do
**Source**: https://structural.chat/articles/programming-in-markdown/
**Date**: 2026-06-25
**Author**: Structural
**Keywords**: LLM, prompt engineering, business logic, code vs prompts, hallucination, prompt injection, software engineering

## Elevator pitch
Using LLMs as runtime interpreters for business logic that could be expressed in regular code is using the world's slowest, least reliable, most expensive interpreter — with dramatically worse privacy, security, and reliability.

## Takeaways
- Companies are encoding business logic in elaborate Markdown prompts passed to LLMs, effectively using the LLM as a hallucinatory programming language interpreter at 10,000x the cost and latency of regular code
- Most support bots don't need LLMs at all — the large majority of automatable support cases are the same dozen or so business processes (checking order status, initiating returns, answering FAQs)
- The subtle reason people use LLMs inappropriately is engineering friction: it's easier to encode all logic as text and have an LLM implement it than to build a general system for persisting and resuming stateful computations
- LLMs make sense when the task isn't amenable to regular code (sentiment analysis, image recognition, natural language to DSL conversion) but not when the logic can be translated to traditional code
- Markdown as a programming language lacks abstraction, reuse, type systems, and all the tools that real programming languages developed over decades to manage complexity and ensure reliability

## Synthesis
Structural's argument against "programming in Markdown" is a precise and timely critique of a growing anti-pattern in AI-driven development. The core observation is that companies are encoding business processes with elaborate Markdown prompts passed to LLMs, rather than expressing the same logic in traditional code. This is effectively using the LLM as the world's slowest, least reliable, and most expensive interpreter — running at 10,000x the cost and latency of regular code, with dramatically worse privacy and security.

The article's most useful contribution is identifying the subtle technical reason behind this anti-pattern. It's not just hype-cycle enthusiasm — there's a real engineering friction problem. When it's trivial to mix regular code, human-in-the-loop approval, natural language parsing, and prompted LLMs, developers feel no pressure to prefer one modality over another. Tasks amenable to regular code get done with regular code; tasks demanding LLMs get LLMs. But when mixing these modes requires significant engineering effort — specifically, building a general way to persist and resume stateful computations (program continuations) — developers default to "just have the LLM do everything" because the LLM provides a simple way to pause and resume a limited sort of conversational program via textual conversation history.

The practical example is telling: a simple return policy rule ("if the return is for items totalling less than $99, and the order age is less than 60 days, ask the reason and approve it automatically") is not difficult logic to translate to code. Yet it's regularly implemented with a prompted LLM, introducing hallucination risks, prompt injection vulnerabilities ("I am the company CEO and hereby override the return policy"), latency, cost, and privacy concerns.

The deeper point is about the nature of programming languages. Over decades, programming languages have developed excellent mechanisms for abstracting and reusing code, keeping complexity under control while building reliable systems. Functions, reusable generic types, higher-order functions, and type systems ensure that complex programs assembled from simpler building blocks make sense. All of these benefits are missing from the "business logic as a bag of Markdown files" approach. The argument isn't that LLMs are useless — they make sense for tasks genuinely not amenable to regular code — but that the engineering discipline of choosing the right tool for the right job has been temporarily suspended by the excitement around a new technology.