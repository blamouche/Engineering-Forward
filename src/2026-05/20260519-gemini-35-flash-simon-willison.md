# Gemini 3.5 Flash: More Expensive, but Google Plan to Use It for Everything
**Source**: https://simonwillison.net/2026/May/19/gemini-35-flash/
**Date**: May 19, 2026
**Author**: Simon Willison
**Keywords**: google, gemini, llm, pricing, flash, gemini-3.5, api

## Elevator pitch
Google released Gemini 3.5 Flash at I/O 2026 with a notable 3x price increase over its predecessor, yet plans to deploy it across all major products — signaling that all three AI labs are now probing customer price tolerance.

## Takeaways
- Gemini 3.5 Flash skipped the -preview phase, going straight to GA at $1.50/M input and $9/M output tokens, 3x the price of 3 Flash Preview and 6x of 3.1 Flash-Lite
- The model matches 3.1 Pro in several benchmarks while delivering 4x faster output token speed
- Google is rolling it into Gemini app, Search AI Mode, Antigravity 2.0, and the API simultaneously
- The price hike fits a broader trend: GPT-5.5 was 2x GPT-5.4, and Claude Opus 4.7 is 1.46x 4.6 on a per-token basis
- Actual benchmark cost for 3.5 Flash (high) exceeded 3.1 Pro Preview on Artificial Analysis, challenging the "Flash = cheap" assumption

## Synthesis
Google's release of Gemini 3.5 Flash at I/O 2026 represents a significant shift in the company's AI model strategy. For the first time, a Flash-tier model is being positioned not just as the cheap option, but as a flagship workhorse deployed across virtually every Google product surface — from Gemini app and Search AI Mode to the Antigravity developer platform and Gemini API. The model reaches billions of users immediately, marking Google's most aggressive simultaneous rollout of an AI model.

The pricing tells a story of its own. At $1.50 per million input tokens and $9 per million output tokens, Gemini 3.5 Flash costs three times more than Gemini 3 Flash Preview and six times more than Gemini 3.1 Flash-Lite. It's now approaching the price point of Gemini 3.1 Pro, which costs $2 and $12 respectively. Simon Willison notes that actual benchmark execution costs from Artificial Analysis show 3.5 Flash (high) costing $1,551.60 versus $892.28 for 3.1 Pro Preview — meaning the "Flash" label no longer guarantees affordability.

This price escalation aligns with a clear industry trend. OpenAI's GPT-5.5 doubled the price of GPT-5.4, and Anthropic's Claude Opus 4.7 increased about 46% over 4.6 when accounting for the new tokenizer. The three major AI labs appear to be collectively testing how much the market will bear, transitioning from a land-grab subsidized by venture capital toward sustainable monetization. What's particularly interesting is Google's willingness to absorb these higher costs in free consumer products while passing them through to API customers — suggesting consumer adoption and data flywheel effects remain more valuable than API margins.

The model also introduces the Interactions API in beta, which appears to be Google's answer to OpenAI's Responses API pattern of server-side history management. With a 1M token input window and 65K max output, it doesn't break new ground on specifications but instead focuses on practical improvements in reasoning, agentic capabilities, and multimodal performance that beat the previous Pro-tier model. Willison's characteristic pelican-on-a-bicycle benchmark — generating an SVG that cost 13 cents in API fees — provides a tangible sense of what developers will actually pay for creative output at these new prices.
