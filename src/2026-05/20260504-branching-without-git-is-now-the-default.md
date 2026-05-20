# Branching Without Git Is Now The Default
**Source**: https://supabase.com/blog/branching-without-git-is-now-the-default
**Date**: 2026-05-04
**Author**: Joshen Lim, Qiao, Saxon Fletcher
**Keywords**: Supabase, database branching, Postgres, schema management, pg-delta, migrations, MCP, AI workflows, dashboard

## Elevator pitch
Supabase made dashboard-based database branching (without Git) the default for all projects, adding a second branching path that lets developers iterate on schemas directly from the dashboard while keeping git-based workflows fully supported.

## Takeaways
- Branching without Git, previously a feature preview (Branching 2.0), is now the default for all Supabase projects — no GitHub connection required.
- The workflow is four steps: create a branch from the dashboard (gets its own Postgres instance with current production schema), make changes via SQL/Table Editor, review a schema diff, and merge.
- A new diffing engine, pg-delta (built inside pg-toolbelt), replaces migra as the default with better coverage of Postgres-specific DDL: tables, columns, RLS policies, functions, triggers, indexes, and extensions.
- Git-based branching remains fully supported and both approaches can be used together or switched between freely — the infrastructure is shared.
- MCP server integration means AI tools can create branches, make changes, and merge programmatically without touching git — designed for agentic database workflows.
- pg-delta is also available in the Supabase CLI behind a flag for local use, though it's still alpha software.

## Synthesis

Supabase's decision to make dashboard-based branching the default represents a significant philosophical shift in how they think about database schema management. The original branching system (Launch Week X) required a GitHub connection and tracked migrations in version control — an infrastructure-as-code approach that works well for teams already committed to git-based workflows. Branching 2.0, now the default, acknowledges that many developers — especially those prototyping, working solo, or using AI tools — don't want or need that overhead.

**The "two paths" strategy** is well-executed. Rather than replacing git-based branching, Supabase added a parallel path and made it the default for new users. Existing git-integrated projects are unaffected. New users get the simpler path first, with the option to add git integration later when their workflow demands it. This is the right sequencing: start simple, add ceremony when needed, don't force infrastructure-as-code on someone building their first prototype.

**pg-delta is the technical enabler.** The merge experience — reviewing a diff, confirming, and merging — depends entirely on the quality of the schema diff. Migra, the previous engine, had gaps in Postgres-specific DDL coverage. pg-delta, built from scratch in pg-toolbelt, targets the full range of Postgres objects. Being alpha software is a honest disclosure, and the invitation to file GitHub issues suggests the team is treating this as a community-driven improvement cycle.

**AI workflow integration is explicit and forward-looking.** Every branch created through the Supabase MCP server uses dashboard branching automatically. This means AI agents can iterate on database schemas programmatically — create a branch, apply changes, verify, and merge — without any git ceremony. When combined with the Agent Skills release (teaching agents how to use Supabase correctly), this creates a complete loop: agents know what to do and have the infrastructure to do it safely. The branch acts as a sandbox; merging is the quality gate.

**The practical workflow is worth emphasizing.** Create a branch → get an isolated Postgres instance with production schema → make changes using any Supabase tool → review a generated migration diff → merge. This is essentially a database-level feature branch workflow without version control. For teams that manage their database through the dashboard (which is likely the majority of Supabase users), this is dramatically simpler than setting up a git integration.

**What's missing** is discussion of collaboration workflows. Git-based branching naturally supports pull request reviews. Dashboard branching doesn't have an equivalent review mechanism — the merge confirmation appears to be a single-developer flow. For teams, this could be a limitation. But Supabase's framing ("prototyping schema changes and want fast iteration") suggests they see this as a development-time tool, with production changes potentially still going through git-based review.

The move also reflects broader industry trends. As databases become more accessible (Supabase, Neon, PlanetScale all offer branching), the infrastructure-as-code orthodoxy is being challenged by developer experience arguments. Branching without Git is a bet that "just branch and iterate" is the right default, with version control available as an opt-in for teams that need it.
