# Tokenomics: The 62.5-Minute Rule for Claude's Cache

**Source:** [skids.dev](https://skids.dev/blog/anthropic-cache-tokenomics) — May 17, 2026  
**Author:** Ryan Skidmore (Cloudflare)

## TL;DR
Quantitative analysis of Anthropic's prompt caching economics. Key finding: if you expect to reuse a cache within 62.5 minutes, refresh it; otherwise let it expire. The break-even is model- and prefix-size-independent (ratios cancel out). Also analyzes auto-compaction economics and documents cache footguns.

## Key Findings

### The 62.5-Minute Rule
- Cache write = 1.25× base input; cache read/refresh = 0.10× base input
- Break-even: `T = 5 × (W/R) = 5 × (1.25/0.10) = 62.5 minutes`
- **Independent of model and prefix size** — the multipliers are the same across Opus 4.7, Sonnet 4.6, Haiku 4.5
- Dollar amounts differ, but the decision point is identical

### Compaction Economics
- Break-even turns = `(1 + 62.5×r) / (1 − r)` where r = summary/original ratio
- 20:1 compression → pays back in ~4.3 turns
- 10:1 → ~8 turns
- 5:1 → ~17 turns
- 2:1 → ~65 turns (not worth it)
- Output tokens are 5× base — verbose summaries can be a strict loss

### Cache Footguns
1. **Opus 4.7 new tokenizer** — same text may be up to 35% larger in tokens
2. **Minimum token floor** — Opus needs 4,096 tokens, Sonnet needs 1,024; below floor, caching silently fails (check `cache_creation_input_tokens` in usage block)
3. **20-block lookback window** — cache breakpoint scans backward 20 content blocks max; add explicit breakpoints for longer requests

### Dollar Impact (Opus 4.7, 500K prefix)
- 30 min idle: refresh saves $1.63 vs rewrite
- 60 min: saves only $0.13
- 90 min: refresh costs $1.38 more than rewrite

## Relevance to Engineering-Forward
Critical operational knowledge for anyone running Claude at scale. Understanding cache tokenomics is essential for cost-optimizing agent workflows, CI/CD pipelines, and long-running coding sessions. The model-independent ratios make the rule portable.
