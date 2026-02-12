# Building a Better Bugbot

**Source**: https://cursor.com/blog/building-bugbot

**Date**: January 15, 2026

**Author**: Jon Kaplan

**Keywords**: Code review automation, AI-driven metrics, Bugbot development, Machine learning optimization, Pull request analysis, Agentic architecture, Quality measurement, Software testing

## Elevator pitch

Cursor's Bugbot demonstrates how systematic measurement and agentic AI architecture transformed an AI code review tool from 52% to 70% resolution rate by treating bug detection as a measurable optimization problem rather than pure heuristics.

## Takeaways

- Parallel processing with randomized diff orderings and majority voting significantly improved bug detection confidence by identifying issues flagged independently across multiple passes
- Resolution rate—measuring which flagged bugs developers actually fixed—proved essential for systematic optimization, enabling 40 major experiments to identify real improvements
- Transitioning from fixed sequential passes to a fully agentic architecture that dynamically reasons and investigates yielded the largest performance gains
- Counter-intuitively, many experimental changes regressed performance, validating the importance of quantitative metrics over qualitative judgments
- Bugbot now reviews over 2 million PRs monthly with resolved bugs per PR more than doubling from 0.2 to 0.5 between July 2025 and January 2026

## Synthesis

Cursor's journey building Bugbot offers a masterclass in applied AI engineering, demonstrating how systematic measurement and architectural evolution transform theoretical AI capabilities into production-grade tools. The article chronicles the development of an AI-powered code review agent that identifies logic bugs, performance issues, and security vulnerabilities before they reach production.

The early development phase revealed a fundamental truth about AI tooling: baseline model capability determines feasibility. Initial attempts failed simply because models weren't capable enough. As foundation models improved, Cursor experimented extensively with configurations, pipelines, and context management strategies. The breakthrough came through parallel processing—running eight concurrent bug-finding passes with randomized diff orderings, then applying majority voting to filter results. This approach leveraged a key insight: bugs identified independently across multiple randomized passes represented higher-confidence findings than those appearing in single passes.

The initial production system combined these parallel passes with bug deduplication, category filtering, validator models, and result consolidation. Supporting infrastructure included a rebuilt Rust-based Git integration for fast repository access, rate-limit monitoring, request batching, and GitHub-compatible proxy infrastructure. Recognizing that different codebases required different checks, the team introduced "Bugbot rules" for customizable, codebase-specific analysis.

The critical inflection point came with measurement. Without quantitative metrics, the team lacked a systematic basis for improvement. They developed "resolution rate"—using AI to determine which flagged bugs authors actually fixed when merging PRs. Internal validation confirmed the LLM's accuracy in this classification, providing a reliable optimization target. This metric unlocked systematic experimentation.

With resolution rate as their North Star, the team conducted 40 major experiments across models, prompts, iteration counts, validators, and architectural approaches. Surprisingly, many changes that seemed promising actually regressed performance, validating earlier qualitative judgments and demonstrating why measurement matters. Some experiments improved specific scenarios while degrading overall performance—tradeoffs impossible to assess without systematic metrics.

The largest gains emerged from architectural redesign. Rather than fixed sequential passes, the team transitioned to a fully agentic architecture where the agent reasoned over diffs, called tools dynamically, and decided where investigation was needed. This required fundamentally rethinking prompting strategy—shifting from restraining models with specific instructions to encouraging aggressive, thorough investigation. The agentic approach allowed the system to adapt its analysis strategy to each PR's unique characteristics rather than applying uniform processing.

The results speak volumes. From July 2025's Version 1 to January 2026's Version 11, resolution rate improved from 52% to over 70%. Average bugs flagged per run increased from 0.4 to 0.7. Most importantly, resolved bugs per PR more than doubled from approximately 0.2 to 0.5—meaning developers were actually fixing substantially more issues identified by Bugbot.

Today, Bugbot reviews over two million PRs monthly for companies including Rippling, Discord, and Airtable. The roadmap includes Bugbot Autofix, which will automatically deploy Cloud Agents to fix identified issues, code execution capabilities for self-verification, and always-on codebase scanning beyond pull requests.

The Bugbot story illustrates several principles for building production AI systems. First, baseline model capability is foundational—no amount of engineering overcomes insufficient model capabilities. Second, systematic measurement enables optimization—without resolution rate metrics, the team would have been guessing. Third, architectural flexibility matters—the shift to agentic design yielded gains impossible with fixed pipelines. Fourth, surprising results require empirical validation—many "obvious" improvements actually degraded performance. Finally, production AI systems require substantial infrastructure beyond models—Git integration, rate limiting, batching, and proxying are essential for scale.

Cursor's transparency about both successes and failures provides valuable lessons for teams building AI-powered development tools, demonstrating that systematic engineering discipline applied to AI systems yields compounding improvements over time.
