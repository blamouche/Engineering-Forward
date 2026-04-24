# An update on recent Claude Code quality reports

**Source**: https://www.anthropic.com/engineering/april-23-postmortem
**Date**: April 24, 2026
**Author**: Unknown
**Keywords**: anthropic, update, recent, claude, code, quality, reports

## Elevator pitch
Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems

## Takeaways
- Engineering at Anthropic An update on recent Claude Code quality reports Published Apr 23, 2026 We traced recent reports of Claude Code quality issues to three separate changes.
- Here's what happened and what we're changing.
- Over the past month, we’ve been looking into reports that Claude’s responses have worsened for some users.
- We’ve traced these reports to three separate changes that affected Claude Code, the Claude Agent SDK, and Claude Cowork.
- All three issues have now been resolved as of April 20 (v2.1.116).

## Synthesis
Engineering at Anthropic An update on recent Claude Code quality reports Published Apr 23, 2026 We traced recent reports of Claude Code quality issues to three separate changes. Here's what happened and what we're changing. Over the past month, we’ve been looking into reports that Claude’s responses have worsened for some users. We’ve traced these reports to three separate changes that affected Claude Code, the Claude Agent SDK, and Claude Cowork. All three issues have now been resolved as of April 20 (v2.1.116). In this post, we explain what we found, what we fixed, and what we’ll do differently to ensure similar issues are much less likely to happen again. We take reports about degradation very seriously. We never intentionally degrade our models, and we were able to immediately confirm that our API and inference layer were unaffected. After investigation, we identified three different issues: On March 4, we changed Claude Code's default reasoning effort from high to medium to reduce the very long latency—enough to make the UI appear frozen—some users were seeing in high mode. We reverted this change on April 7 after users told us they'd prefer to default to higher intelligence and opt into lower effort for simple tasks.
