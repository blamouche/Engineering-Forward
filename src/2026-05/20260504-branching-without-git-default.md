# Branching Without Git Is Now The Default
**Source**: https://supabase.com/blog/branching-without-git-is-now-the-default
**Date**: 2026-05-04
**Author**: joshenlim, qiao, saxonf
**Keywords**: branching, postgres, database, schema-migration, developer-experience, AI-workflows, pg-delta

## Elevator pitch
Supabase has made dashboard-based database branching (without requiring a Git connection) the default for all projects, powered by a new schema diffing engine called pg-delta, and explicitly built for AI agent workflows.

## Takeaways
- Branching without Git is now the default for all Supabase projects, removing the GitHub connection requirement that previously blocked many developers
- Supabase supports two branching paths: dashboard-based (fast iteration, no config) and Git-based (migrations in version control, PR-triggered branches) — both using the same underlying infrastructure
- The new pg-delta diffing engine, built from scratch, handles the full range of Postgres DDL and replaces migra as the default for dashboard branching
- Every branch created through the Supabase MCP server uses dashboard branching automatically, making it the default foundation for AI-agent database workflows
- Teams can start with dashboard branching and add Git integration later when workflows demand it, with no migration friction

## Synthesis
Supabase originally shipped database branching through a git-based workflow that connected GitHub repos, tracked migrations in version control, and created preview branches automatically on pull requests. That approach worked well for teams managing their schema as code, but it locked out anyone who didn't want to set up a GitHub integration. Branching 2.0, first introduced behind a feature preview, removed that requirement — and now that preview is gone. Dashboard branching is the default for every project.

The workflow is straightforward: create a branch from the dashboard (which provisions its own Postgres instance with the current production schema), make changes using the SQL Editor or Table Editor, review a schema diff, and merge. The merge experience is powered by pg-delta, a new diffing engine built from scratch inside pg-toolbelt. pg-delta handles the full range of Postgres objects — tables, columns, RLS policies, functions, triggers, indexes, and extensions — and generates the correct migration statements. It's also available in the Supabase CLI behind a flag for local use, though it's currently alpha software.

The branching release is explicitly designed for AI workflows. Every branch created through the Supabase MCP server uses dashboard branching automatically. When an AI agent needs to iterate on a database schema, it can create a branch, make changes, and merge without touching git. The branch exists as long as the agent needs it and gets cleaned up afterward. This is a deliberate architectural choice that positions Supabase as a platform where AI agents can safely and programmatically manipulate database schemas.

The two approaches coexist cleanly: dashboard branching for rapid prototyping, schema experiments, and AI workflows; git-based branching for teams that want migrations in version control, PR-based review, and an infrastructure-as-code approach. Users can switch between them or use them together. Existing git-based setups continue to work unchanged.
