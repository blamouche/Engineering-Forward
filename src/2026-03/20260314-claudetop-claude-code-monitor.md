# claudetop: htop for Your Claude Code Sessions
**Source**: https://github.com/liorwn/claudetop
**Date**: 2026-03-14
**Author**: liorwn
**Keywords**: Claude Code, cost monitoring, token usage, productivity, developer tools, iTerm2, plugins, budgets

## Elevator pitch
claudetop is a real-time terminal monitoring tool for Claude Code that tracks spending, burn rates, cache efficiency, and projections—built after its creator discovered a $55 overage between estimated and actual AI costs.

## Takeaways
- Displays real-time cost tracking with hourly burn rates and monthly projections for Claude Code sessions
- Shows model cost comparisons: what the same tokens would cost across Opus, Sonnet, or Haiku
- Cache efficiency monitoring identifies when context reuse isn't working properly
- Smart alerts only appear when action is needed; supports daily budgets and custom thresholds
- Extensible plugin system with 8 examples; integrates with iTerm2 for status bar indicators; MIT licensed

## Synthesis
claudetop was born from a concrete pain point: its creator ran a Claude Code session expecting a $10 bill and received a $65 invoice. This 6.5x overage is not unusual for developers who are first learning the cost profile of agentic coding—the combination of long context windows, many tool calls, and expensive Opus model usage can compound unexpectedly.

The tool's design philosophy is monitoring-first. Rather than imposing spending controls (which would interrupt workflow), claudetop provides visibility that enables informed decision-making. Real-time cost display with hourly burn rates and monthly projections converts abstract token counts into concrete financial metrics that developers can actually reason about. The hourly burn rate in particular is useful for long-running agentic sessions where cumulative cost is hard to intuit without seeing the rate at which it accumulates.

The model cost comparison feature addresses a decision that developers make implicitly but rarely evaluate explicitly: whether to use Opus, Sonnet, or Haiku for a given task. By showing in real time what the current session's tokens would cost across all three model tiers, claudetop makes the cost-capability tradeoff concrete and actionable. A session costing $20 on Opus might be completable at $3 on Sonnet—a comparison worth making before the session is over.

Cache efficiency monitoring addresses a less obvious cost driver. Claude's prompt caching feature significantly reduces costs for sessions with repeated context, but the cache isn't always hit as expected due to context structure issues. Monitoring cache efficiency enables developers to identify and fix underperforming caching configurations before they result in unnecessary spending.

The plugin extensibility—with examples ranging from git branch status to meeting countdowns—reflects the tool's architecture as a general-purpose terminal overlay rather than a single-purpose cost tracker. Automatically updated pricing from a repository-maintained JSON file ensures accuracy as Anthropic adjusts its pricing, without requiring users to manually update configuration.
