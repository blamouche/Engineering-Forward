# AI Agents Know About Supabase. They Don't Always Use It Right.
**Source**: https://supabase.com/blog/supabase-agent-skills
**Date**: 2026-04-09
**Author**: Pedro Rodrigues
**Keywords**: Supabase, AI agents, agent skills, RLS, security, Postgres, MCP, Claude Code, Codex, Cursor, open-source

## Elevator pitch
Supabase released Agent Skills, an open-source instruction set that teaches AI coding agents how to build on Supabase correctly — fixing the gap between what agents know from training data and what they actually need to implement securely.

## Takeaways
- AI agents frequently get Supabase wrong: skipping RLS policies, hallucinating CLI commands, creating views without `security_invoker = true`, and ignoring docs in favour of stale training data.
- The skill is only ~100 lines in SKILL.md, containing critical security rules inline (never use `user_metadata` for auth, views need `security_invoker`, UPDATE requires SELECT policy, etc.) because agents were lazy about reading reference files.
- Core design principle: teach agents *how* to find current docs (MCP search, fetch docs as markdown, web search), not *what* the current docs say — keeping the skill maintainable and always accurate.
- Evaluation across Claude Code and Codex showed consistent improvement: Codex (GPT-5.4) went from 71% to 88% with the skill, Claude Code (Sonnet 4.6) from 58% to 71%.
- The skill introduces an opinionated schema management workflow: modify schema directly during development, run database advisors, then commit migrations — avoiding migration-per-change overhead.
- MCP alone is insufficient: agents default to training data even when docs search tools are available; the skill steers them to verify against current docs first.

## Synthesis

Supabase's Agent Skills release addresses a growing pain point in AI-assisted development: the gap between what models know and what they actually need to do. The blog post is refreshingly honest about the problem — agents know Supabase exists, they've seen plenty of Supabase code, but they consistently make the same security and correctness mistakes.

**The problem is context, not capability.** The evaluation results tell a clear story. Claude Code (Sonnet 4.6) scored 46% at baseline (no tools, no skill), 58% with MCP tools only, and 71% with the skill. Codex (GPT-5.4) went from 71% baseline to 88% with the skill. The models *can* implement things correctly — they know what `security_invoker = true` means — they just don't know *when* to apply it. The skill bridges that gap by encoding the judgment calls that training data can't provide.

**Design lessons for skill authors** are the most transferable part of this post. Supabase tried spreading guidance across reference files and found agents skipped them. The solution: put everything critical directly in `SKILL.md`, about 100 lines, loaded on activation. The second key insight is to teach agents how to fetch docs rather than replicating them — docs are already maintained, so duplicating them in skills creates a maintenance burden and staleness risk. The third is to be opinionated: encode your product's best practices as rules, not suggestions.

**Security is treated as non-negotiable.** The skill includes an inline checklist that covers the most common Supabase security pitfalls: never use `user_metadata` for authorization (it's user-editable), views bypass RLS by default (`security_invoker = true` is required), UPDATE needs a SELECT policy or updates silently fail, storage upsert requires three policies not one, and deleting users doesn't invalidate JWTs. These aren't edge cases — they're footguns that would silently cause security vulnerabilities or data corruption.

**The schema management workflow** is an interesting opinionated choice. Instead of requiring migrations for every DDL change, the skill encourages agents to modify schemas directly during development, run database advisors to catch issues, then commit a migration once stable. This speeds iteration significantly but comes with a strong warning: don't connect MCP to production. It's a pragmatic acknowledgment that migration-by-migration workflows are too slow for AI-driven development, while still maintaining the safety net of formalised migrations for production.

**Integration with the Agent Skills ecosystem** is also noteworthy. The skill follows the Agent Skills Open Standard and works with Claude Code, Codex, GitHub Copilot, and Cursor. Installation is a single `npx skills add` command. This positions Supabase as a first-class citizen in the agentic development toolchain — not just a database, but a platform with deep integrations into how AI agents actually work.

The post is transparent about being v0.1.0 with small sample sizes in evaluation, but the consistent improvement across all tested models and conditions suggests the approach is sound. The broader lesson for the industry: as AI agents become the primary interface for building software, the quality of their "skills" — the instruction sets that guide them — will become as important as the quality of the underlying models.
