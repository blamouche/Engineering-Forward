# Claude Code Cache Bug: Prompt-Cache Misses Costing Money in Long Sessions
**Source**: https://code.claude.com/docs/en/changelog
**Date**: 2026-08-28
**Author**: Claude Code Team
**Keywords**: Claude Code, prompt cache, cache miss, OAuth token refresh, long sessions, cost optimization, debugging

## Elevator pitch
The Claude Code team fixed a quiet cache bug where tool definitions were re-rendered after OAuth token refreshes, causing prompt-cache misses roughly once an hour — an invisible cost leak in long agent sessions.

## Takeaways
- A cache bug in Claude Code caused prompt-cache misses approximately once per hour during long sessions
- Tool definitions were being re-rendered after OAuth token refreshes, triggering cache invalidation
- For users running long agent sessions, this was an invisible cost leak worth upgrading for
- The bug highlights how prompt caching is a critical cost lever for agentic coding
- OAuth token refreshes — a mundane infrastructure detail — can have outsized impact on LLM costs

## Synthesis
The Claude Code cache bug fix is a master class in why prompt caching matters for agentic coding. The bug was quiet: tool definitions were being re-rendered after OAuth token refreshes, which happen approximately once per hour. Each re-rendering triggered a prompt-cache miss, meaning the entire context window had to be re-sent and re-processed from scratch rather than served from cache.

For short coding sessions, this is barely noticeable. For long agent sessions that run for hours — the exact use case Claude Code is designed for — the cost adds up quickly. Every cache miss means re-processing the full context window, which is the most expensive operation in LLM-based coding. A session that should benefit from near-constant cache hits was instead paying full price for context processing once an hour.

The fix is a reminder that prompt caching is not just an optimization — it is the economic foundation of agentic coding. Without effective caching, long agent sessions become prohibitively expensive because every interaction requires re-processing the entire context. The caching layer is what makes multi-hour coding sessions economically viable.

The bug also illustrates how infrastructure details that seem unrelated to AI — OAuth token refresh schedules — can have outsized impact on LLM costs. The interaction between authentication infrastructure and prompt caching is not obvious, and this kind of invisible cost leak is exactly the type of problem that distinguishes production AI systems from demos. Teams building agentic systems should audit their cache hit rates regularly, especially after any infrastructure change that might invalidate the cache.