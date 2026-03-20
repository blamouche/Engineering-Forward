# OpenAI Launches GPT-5.4 Mini and GPT-5.4 Nano on APIs
**Source**: https://www.testingcatalog.com/openai-launches-gpt-5-4-mini-and-gpt-5-4-nano-on-apis/
**Date**: 2026-03-18
**Author**: Alexey Shabanov
**Keywords**: OpenAI, GPT-5.4, mini, nano, API, coding agents, SWE-Bench, pricing, context window

## Elevator pitch
OpenAI launches GPT-5.4 Mini and GPT-5.4 Nano—two smaller, faster variants of its flagship model targeting coding copilots and automation use cases where speed and cost matter more than maximum capability.

## Takeaways
- GPT-5.4 Mini runs 2x faster than GPT-5 mini and scores 54.4% on SWE-Bench Pro vs. 45.7% for its predecessor
- GPT-5.4 Nano is reserved for API users only, priced at $0.20/$1.25 per million input/output tokens
- Both models feature 400K-token context windows with 128K max output, supporting text and image inputs
- Mini is available in ChatGPT Free and Go tiers via the Thinking menu; Nano is developer-only
- The launch reinforces OpenAI's strategy of positioning GPT-5.4 as flagship for reasoning/coding with smaller variants handling execution-layer tasks

## Synthesis
The release of GPT-5.4 Mini and Nano represents OpenAI's continued expansion of its model family from capability flagships toward practical deployment tiers. Where the full GPT-5.4 targets complex reasoning and extended context tasks, the Mini and Nano variants are optimized for the high-frequency, latency-sensitive calls that dominate production agentic systems.

The benchmark improvements are meaningful. Mini's 54.4% score on SWE-Bench Pro versus 45.7% for its predecessor GPT-5 mini reflects a substantial coding capability uplift in the smaller model tier—a tier that handles the majority of actual developer tool interactions. The 2x speed improvement compounds this advantage: faster responses enable tighter development feedback loops, and in multi-step agentic workflows where many calls are made sequentially, latency reductions accumulate into significant total time savings.

The pricing structure is designed to expand adoption across different developer segments. Nano at $0.20/$1.25 per million tokens makes high-volume applications economically viable—scenarios where thousands of lightweight agent tool calls need to happen affordably. Mini at $0.75/$4.50 sits in a middle tier that balances capability and cost for interactive developer tools.

The decision to make Nano API-only while making Mini available in ChatGPT's consumer tiers reflects different optimization targets. Consumer users get faster interactive responses through Mini's Thinking menu integration. Developers building programmatic workflows get Nano's extreme cost efficiency for automation at scale. Both models share the 400K-token context window with 128K output, ensuring they can handle substantial code repositories without context truncation.

Microsoft's Foundry platform receiving both models (US Data Zone live, EU pending) signals the enterprise distribution pathway and confirms that these models will reach regulated industries through Microsoft's existing enterprise relationships—an important distribution vector that OpenAI's direct API channel cannot easily replicate.
