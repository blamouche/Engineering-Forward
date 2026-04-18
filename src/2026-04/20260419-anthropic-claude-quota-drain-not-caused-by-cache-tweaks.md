# Anthropic: Claude quota drain not caused by cache tweaks

**Source**: https://www.theregister.com/2026/04/13/claude_code_cache_confusion/
**Date**: April 19, 2026
**Author**: Tim Anderson
**Keywords**: theregister, anthropic, claude, quota, drain, caused, cache, tweaks

## Elevator pitch
: Dev reports suggest long sessions now burn through usage much faster.

## Takeaways
- AI + ML 27 Claude Code cache chaos creates quota complaints 27 Dev reports suggest long sessions now burn through usage much faster Tim Anderson Mon 13 Apr 2026 // 15:14 UTC Anthropic last month reduced the TTL (time to live) for the Claude Code prompt cache from one hour to five minutes for many requests, but said this should not increase costs despite users reporting faster depleting quotas.
- User Sean Swanson posted a bug report showing that Anthropic introduced a one-hour cache for Claude Code context around February 1, then changed it back to a five-minute cache around March 7.
- "The 5m TTL is disproportionately punishing for the long-session, high-context use case that defines Claude Code usage," said Swanson.
- When using AI coding assistants or agents, the context is additional data sent along with the user's prompts, such as existing code or background instructions.
- Context improves the accuracy of the AI but also requires more processing.

## Synthesis
AI + ML 27 Claude Code cache chaos creates quota complaints 27 Dev reports suggest long sessions now burn through usage much faster Tim Anderson Mon 13 Apr 2026 // 15:14 UTC Anthropic last month reduced the TTL (time to live) for the Claude Code prompt cache from one hour to five minutes for many requests, but said this should not increase costs despite users reporting faster depleting quotas. User Sean Swanson posted a bug report showing that Anthropic introduced a one-hour cache for Claude Code context around February 1, then changed it back to a five-minute cache around March 7. "The 5m TTL is disproportionately punishing for the long-session, high-context use case that defines Claude Code usage," said Swanson. When using AI coding assistants or agents, the context is additional data sent along with the user's prompts, such as existing code or background instructions. Context improves the accuracy of the AI but also requires more processing. Claude prompt caching avoids re-processing previously used prompts including context and background information. The cache can have either a five-minute or one-hour TTL. Writing to the five-minute cache costs 25 percent more in tokens, and writing to the one-hour cache 100 percent more, but reading from cache is around 10 percent of the base price. Jarred Sumner, the creator of the Bun JavaScript runtime who now works for Anthropic , agreed that the analysis was "good detective work" but claimed that the change back to the five-minute cache made Claude Code cheaper because "a meaningful share of Claude Code's requests are one-shot calls where the cached context is used once and not revisited." Sumner said that the Claude Code client determines the cache TTL automatically and there are no plans for a global setting. Swanson revised his analysis in response, agreeing that sessions using subagents do benefit from the lower write cost of the five-minute cache since they interact quickly and "their caches almost never expire." However, he said he has been a $200 per month subscriber for over six months and had never hit a quota limit until March.
