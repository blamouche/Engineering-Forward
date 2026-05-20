# AI Agents Know About Supabase. They Don't Always Use It Right.
**Source**: https://supabase.com/blog/supabase-agent-skills
**Date**: April 9, 2026
**Author**: Pedro Rodrigues
**Keywords**: Supabase, agent skills, AI coding agents, RLS, security, MCP, Claude Code, Codex, Cursor, Agent Skills Open Standard, SKILL.md

## Elevator pitch
Supabase released Agent Skills, an open-source instruction set that teaches AI coding agents how to build on Supabase correctly — addressing the gap between agents "knowing about" Supabase and actually implementing it with proper security patterns like Row Level Security.

## Takeaways
- AI agents frequently skip critical security patterns like RLS policies, `security_invoker = true` on views, and proper `service_role` key handling — the skill encodes these requirements inline
- The skill is ~100 lines in SKILL.md and teaches agents *how* to find current docs rather than replicating them, keeping it maintainable
- Testing across Claude (Opus/Sonnet 4.6) and Codex (GPT-5.4) showed consistent improvement: MCP + Skill outperformed MCP-only and baseline in every combination, with Codex GPT-5.4 reaching 88% task completion
- Key design insight: agents are "lazy about reading reference files" — all critical security guidance must live directly in SKILL.md where it can't be skipped
- The skill introduces an opinionated schema management workflow: modify directly during development, then run database advisors, then commit migrations once stable

## Synthesis
Supabase's Agent Skills release is a fascinating artifact of the AI agent era because it openly acknowledges a problem everyone building AI tools faces but few discuss: LLMs already "know" about your product from training data, but knowing isn't the same as using correctly. Supabase found that agents consistently made predictable mistakes — skipping RLS policies on exposed schemas, hallucinating CLI commands that don't exist, creating views that silently bypass security, and relying on stale training data rather than checking current documentation.

The solution is elegantly simple: a SKILL.md file of about 100 lines that agents load as context. The design philosophy is worth studying for anyone building agent-facing tooling. Rather than replicating Supabase's documentation inside the skill — a maintenance nightmare that would inevitably go stale — the skill teaches agents *how* to find current information: MCP search_docs tool, fetching docs pages as markdown, or web search as a fallback. The skill encodes the *judgment calls* that training data can't provide, not the *facts* that docs already maintain.

The security section is particularly instructive. Supabase initially put critical security guidance in separate reference files. Agents skipped them. So they moved everything critical into SKILL.md itself — RLS requirements, `app_metadata` vs `user_metadata` for authorization, the `service_role` key exposure risk, view security patterns, and JWT session revocation requirements. These are loaded with the skill, giving the agent "no excuse to miss them."

The evaluation results validate the approach. Across four model/architecture combinations (Claude Opus 4.6, Claude Sonnet 4.6, Codex GPT-5.4, Codex GPT-5.4 Mini), every single one performed better with MCP + Skill than with MCP alone. Codex GPT-5.4 went from 71% to 88%. The most revealing finding: MCP alone sometimes performed *worse* than baseline — agents with tool access but no workflow guidance guessed at how to combine tools, leading to worse outcomes than simply relying on training data.

Supabase's Agent Skills signals a maturation of the "skills" pattern that's spreading across the AI ecosystem. As agents become more autonomous and developers more comfortable giving them direct database access, encoding institutional knowledge about security, tooling workflows, and documentation practices into portable instruction sets becomes essential infrastructure — not just for Supabase, but for any platform that wants AI agents to be competent rather than dangerous users of its services.
