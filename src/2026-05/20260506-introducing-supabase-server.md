# Introducing @supabase/server
**Source**: https://supabase.com/blog/introducing-supabase-server
**Date**: 2026-05-06
**Author**: tomas_pozo, kalleby_santos, katerina_skroumpelou, matt_johnston
**Keywords**: supabase-server, edge-functions, server, typescript, auth, JWT, RLS, developer-experience

## Elevator pitch
`@supabase/server` is a new package that eliminates repetitive auth verification, client setup, and CORS boilerplate from Supabase Edge Functions, giving developers a declarative, runtime-agnostic wrapper to jump straight into business logic.

## Takeaways
- `@supabase/server` replaces the shared utility files and manual JWT verification that plague Edge Functions with a single `withSupabase` wrapper
- Supports five declarative auth modes: `user`, `none`, `secret`, `publishable`, and combined `['user', 'secret']`
- Works across Edge Functions, Vercel Functions, Cloudflare Workers, Hono, and Bun — any runtime that supports the standard `Request`/`Response` Web API
- Automatically handles new asymmetric JWT signing keys and key validation without requiring `jose` or JWKS configuration
- Designed with AI agent compatibility in mind: Claude Code migrated an entire project's Edge Functions in a single prompt due to the uniform API pattern

## Synthesis
Supabase analyzed 25,000 deployed Edge Functions and discovered the same pattern everywhere: developers were constantly rebuilding the same setup code — creating Supabase clients, verifying JWTs, handling CORS, wiring up auth context, and copying shared utility files between functions. `@supabase/server` is the answer to this fragmentation.

The package's centerpiece is `withSupabase`, a higher-order function that wraps a standard `(Request) => Promise<Response>` handler. Before the handler executes, it verifies the declared auth mode, creates the appropriate Supabase clients (user-scoped and admin), and provides a `SupabaseContext` containing verified user identity, JWT claims, and auth metadata. For developers who need finer control, the lower-level `createSupabaseContext` and composable primitives (`createAdminClient`, `createContextClient`, `resolveEnv`, `verifyAuth`) let you build custom middleware, per-route auth, or MCP server wrappers.

A significant driver for this package was Supabase's recent security improvements — asymmetric JWT signing keys and new API keys. Migrating existing functions to these new security features previously required installing `jose`, configuring a JWKS endpoint, building custom auth middleware, and touching every function individually. `@supabase/server` absorbs all of that internally. Adopting the package automatically brings the new security model along with it.

The team explicitly designed the package for agentic development. Every function follows the same structure: declare access, receive context, write logic. During internal testing, Claude Code migrated an entire project's Edge Functions to `@supabase/server` in a single prompt — including adopting new API keys, removing shared utility files, and switching every function to `withSupabase`. All functions worked on the first run.

The package is not a replacement for `@supabase/ssr` (which handles cookie-based session management for SSR frameworks like Next.js). It targets stateless, header-based auth for Edge Functions and Workers. A Hono adapter ships with the package, a community-contributed H3 adapter has already been merged, and more adapters are expected. The package is in public beta and ships with full documentation in its GitHub repo and an AI skill installable via `npx skills add supabase/server`.
