# An update on recent Claude Code quality reports

**Source**: https://www.anthropic.com/engineering/april-23-postmortem
**Date**: April 23, 2026
**Author**: Anthropic
**Keywords**: Claude Code, prompt engineering, reasoning effort, context management, regressions, product reliability

## Elevator pitch
Anthropic explains that recent Claude Code quality regressions came from product-layer changes to reasoning defaults, session thinking retention, and verbosity controls rather than from the underlying API model, then details the fixes and process changes meant to prevent repeats.

## Takeaways
- Anthropic says three separate product changes, not base-model degradation, caused the inconsistent quality reports users were seeing.
- Lowering the default reasoning effort improved latency but made Claude Code feel less capable, so Anthropic reverted the tradeoff.
- A caching optimization accidentally kept dropping prior reasoning after idle sessions, producing forgetfulness, repetition, and faster usage-limit drain.
- A system prompt change meant to reduce verbosity shaved output length but also hurt coding quality enough to require rollback.
- The company is responding with broader eval coverage, better prompt-change controls, stronger code review support, and usage-limit resets for subscribers.

## Synthesis
This post is notable because Anthropic is describing Claude Code regressions as an operations and product-systems problem, not a mysterious model-quality collapse. That distinction matters. Users often experience the tool as one thing, but the actual behavior is shaped by a layered stack that includes model defaults, prompt design, context handling, caching, and UI decisions. Anthropic’s account shows how multiple seemingly reasonable optimizations can combine into a user-visible drop in quality even when the core inference layer remains unchanged.

The first issue, around default reasoning effort, is a classic product tradeoff gone wrong. Anthropic lowered effort to cut latency and reduce frozen-feeling sessions, but users experienced the result as a less intelligent system. The company’s reversal suggests that for a coding tool, perceived intelligence and reliability matter more than shaving some delay off the default path. In practice, people appear willing to tolerate higher latency if they trust the output more. That is a useful lesson for anyone building AI-assisted developer workflows.

The second issue is even more revealing because it sits at the boundary between infrastructure efficiency and cognitive continuity. Anthropic tried to prune old reasoning after an idle period to reduce uncached tokens, but a bug caused repeated loss of reasoning history across the rest of the session. The result was not total failure. It was something subtler and arguably more damaging: forgetfulness, repetition, and increasingly odd choices. That is a sharp reminder that long-running coding agents live or die by context integrity. Small errors in how prior thinking is preserved can make a capable model feel erratic and unreliable.

The third issue, a prompt instruction to reduce verbosity, reinforces how fragile system-prompt tuning can be when intelligence and communication style are tightly coupled. Anthropic found that a short instruction on response length was enough to create a measurable coding-quality drop. That is a strong argument for broader ablations and per-model evaluation before prompt changes ship widely. More broadly, the post shows that agent products are now mature enough to need incident-style writeups. Reliability is no longer only about uptime. It is about preserving the quality characteristics users depend on from one release to the next.
