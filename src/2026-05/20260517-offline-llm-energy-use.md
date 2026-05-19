# Apple Silicon Costs More Than OpenRouter

**Source:** [williamangel.net](https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html)
**Date:** 2026-05-17
**Author:** William Angel

## Summary

A cost analysis comparing running local LLM inference on an M5 Max MacBook Pro versus using OpenRouter. Conclusion: local inference is ~3x more expensive per token than cloud, with hardware depreciation dominating costs over electricity.

## Key Takeaways

- **Hardware costs dominate**: electricity (~$0.02/hr) is negligible; hardware depreciation ($0.05-$0.16/hr) is the real cost
- **$1.50/M tokens local vs ~$0.50/M on OpenRouter** for comparable models like Gemma 4 31B
- **Local is slower**: 10-40 tok/s on M5 Max vs 60-70 tok/s on OpenRouter
- **5-year lifespan estimate**: $860/year hardware cost → ~$0.10/hr
- **Human salary dwarfes tokens**: a developer's salary is ~1000x the cost of tokens, making cloud APIs the rational choice
- **Still remarkable**: a consumer device runs models close to Anthropic Sonnet-level performance

## Key Quote

> "Apple silicon costs more than OpenRouter. [...] At a few tens of tokens per second this works out to amortized costs of ~$1.50 per million tokens. OpenRouter for comparable models is 1/3rd the price and ~2x the speed."

## Tags

LLM, local inference, Apple Silicon, OpenRouter, cost analysis, hardware

---

*Generated from: https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html*
