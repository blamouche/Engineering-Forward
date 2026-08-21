# Bun's Rapid Rust Rewrite with AI: What Can We Learn?
**Source**: https://newsletter.pragmaticengineer.com/p/the-pulse-what-can-we-learn-from-07f
**Date**: 2026-07-16
**Author**: Gergely Orosz
**Keywords**: Bun, Rust, Zig, AI rewrite, Fable, Anthropic, code migration, LLM-assisted development, memory safety

## Elevator pitch
Bun's creator migrated 535,496 lines of Zig to Rust in 11 days using Anthropic's Fable model, at a cost of $165,000 in API tokens — demonstrating that AI-assisted large-scale code rewrites are now practical when backed by robust test suites and expert human oversight.

## Takeaways
- Bun's 535K-line Zig→Rust migration was driven by persistent memory safety issues: use-after-free, double-free, and memory leaks in a codebase mixing garbage-collected and manually-managed memory
- The rewrite followed a structured 10-step process: prep work (3h creating a PORTING.md guide), trial run with adversarial review, splitting work across 64 parallel AI agents, 2 days of parallel code generation, 12 hours fixing ~16,000 compiler errors, 2 days for local test runs, and 3 days for CI
- Fable consumed 5.9B uncached input tokens, 690M output tokens, and 72B cached input token reads — at $165K in API pricing, roughly equivalent to one US engineer's annual base salary
- Three prerequisites made this feasible: an engineer who knows the codebase intimately, an extremely robust test suite, and willingness to invest heavily in tokens
- Skills that compensated for model weaknesses on Opus 4.8 actually harmed performance on Fable 5 — suggesting that AI-assisted migration techniques have a shelf life and must be re-evaluated per model version

## Synthesis
Jarred Sumner, creator of the Bun JavaScript runtime, undertook one of the most ambitious AI-assisted code migrations to date: rewriting 535,496 lines of Zig into Rust. The motivation was straightforward — Zig is not memory-safe, and Bun's codebase mixed garbage-collected and manually-managed memory, a combination that produced a continuous stream of memory leaks, use-after-free bugs, and crashes. As Sumner put it: "I was tired of going to sleep worrying about crashes in Bun."

The process was far from a simple "rewrite it in Rust" prompt. Sumner spent three hours in a detailed conversation with Claude about how to map Zig patterns to Rust, producing a 600-line PORTING.md document that specified ground rules like "no tokio, rayon, hyper, async-trait" and "no async fn — everything is callbacks + state machines." This document served as the contract for 64 parallel AI agents. The workflow involved splitting 1,448 .zig files across 4 worktrees, each running 16 agents committing and pushing files. Agents were instructed to never run git stash, git reset, or any slow commands. After two days of parallel generation, 16,000 compiler errors remained, which Claude then fixed crate-by-crate in parallel.

The cost was substantial: $165,000 at API pricing. But Mitchell Hashimoto noted that no engineer at that salary could have achieved the same milestones in 11 days. The key insight is that AI migrations are viable for well-engineered projects with strong test suites and motivated maintainers — not a general-purpose shortcut for any rewrite. The remaining caveats are clear: you need deep codebase knowledge, robust tests, and a willingness to invest significantly in tokens. As models improve, the cost equation will shift, but the process blueprint — structured prep, parallel agent execution, adversarial review, and human oversight — provides a template that other teams can adapt.