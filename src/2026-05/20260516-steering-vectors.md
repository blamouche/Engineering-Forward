# DeepSeek-V4-Flash Means LLM Steering Is Interesting Again

**Source:** [seangoedecke.com](https://www.seangoedecke.com/steering-vectors/)
**Date:** 2026-05-16
**Author:** Sean Goedecke

## Summary

A deep dive into LLM steering vectors — the technique of manipulating model activations at inference time to guide outputs. The release of DeepSeek-V4-Flash and the DwarfStar 4 project by antirez makes steering practical for local-model users for the first time.

## Key Takeaways

- **Steering = extracting a concept from activations, then boosting it during inference** — either via prompt-pair differencing or sparse autoencoders
- **DeepSeek-V4-Flash + DwarfStar 4** makes local steering accessible: a strong open model + built-in steering support
- **Why steering hasn't caught on**: it's beneath big labs (they fine-tune instead), out of reach of API users (no activation access), and often outcompeted by prompting
- **Interesting use cases**: removing refusals (abliteration), compressing long context into a vector, potentially steering for "intelligence"
- **Author is skeptical** — thinks most gains are more efficiently achieved via prompting or fine-tuning, but the next 6 months will be telling

## Key Quote

> "Steering sounds like a cheat code. Instead of painstakingly assembling a training set... why not simply go uncover the 'smart' dial in the model's brain and turn it all the way to the right?"

## Tags

AI, LLM, steering vectors, interpretability, DeepSeek, local models, DwarfStar

---

*Generated from: https://www.seangoedecke.com/steering-vectors/*
