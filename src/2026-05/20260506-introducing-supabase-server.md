# Introducing @supabase/server
**Source**: https://supabase.com/blog/introducing-supabase-server
**Date**: 2026-05-06
**Author**: Tomas Pozo, Kalleby Santos, Katerina Skroumpelou, Matt Johnston
**Keywords**: Supabase, server, Edge Functions, auth, RLS, TypeScript, Deno, Hono, Cloudflare Workers, Vercel Functions, JWT, open-source

## Elevator pitch
Supabase released `@supabase/server` in public beta — a package that eliminates server-side boilerplate for Edge Functions by handling auth verification, client setup, request context, and CORS in a single `withSupabase` wrapper.

## Takeaways
- Analysis of 25,000 deployed Edge Functions revealed developers were repeatedly rebuilding the same setup code (auth clients, JWT verification, CORS, shared utility files) before reaching business logic.
- `withSupabase` accepts a declarative auth mode (`'user'`, `'none'`, `'secret'`, `'publishable'`, or combinations) and provides a pre-configured `SupabaseContext` with user-scoped and admin clients, verified identity, and JWT claims.
- Works across Edge Functions, Vercel Functions, Cloudflare Workers, Bun, Hono, and any runtime supporting the standard Web API `Request`/`Response` pattern.
- Internally handles new asymmetric JWT signing keys and API keys — adopting the package gives you the new security model without manual `jose` setup or JWKS configuration.
- Designed for AI agents: the consistent `withSupabase` pattern allowed Claude Code to migrate an entire project's Edge Functions in a single prompt, with all functions working on first run.
- Composable primitives (`createAdminClient`, `createContextClient`, `verifyAuth`) are exposed for teams needing custom middleware, MCP servers, or framework adapters.

## Synthesis

The `@supabase/server` release is a classic example of a platform team noticing a painful pattern and shipping a focused solution. The decision to analyse 25,000 deployed functions before designing the API is notable — it grounds the package in real usage patterns rather than hypothetical developer needs.

**The problem is universal to serverless.** Every serverless function that needs auth ends up with the same 30-50 lines of boilerplate: parse headers, verify JWT, create a Supabase client, handle CORS preflight, wire up context. Developers solve this with shared utility files, but those files need to be copied between projects, kept in sync, and maintained. `@supabase/server` compresses this into a single function call: `withSupabase({ auth: 'user' }, handler)`.

**Declarative access control** is the killer feature. Rather than writing auth middleware, developers declare who can access an endpoint in one line: `auth: 'user'` for authenticated users, `auth: 'none'` for public webhooks, `auth: 'secret'` for server-to-server calls, or `auth: ['user', 'secret']` for hybrid endpoints. The security model of a function becomes visible at a glance. This matters for code review, onboarding, and security auditing — no more tracing through middleware chains to understand who can call what.

**The migration story for new auth keys** addresses a real pain point. Supabase previously improved security with asymmetric JWT signing keys and new API key formats, but migrating existing functions required installing `jose`, configuring JWKS, and rewriting auth middleware. `@supabase/server` absorbs all of this internally. Adopting the package means adopting the new security model with no additional work. This is how platform security improvements should be delivered — as a drop-in upgrade, not a migration project.

**AI agent compatibility** is deliberately designed in. The post mentions that Claude Code migrated an entire project to `@supabase/server` in a single prompt because every function follows the same pattern. When a codebase is uniform, agents produce correct code from a single example. This is an emerging design consideration for libraries and frameworks: consistency and predictability matter more than ever when AI agents are the primary consumers of your API surface.

**The package doesn't replace `@supabase/ssr`.** The post is careful to clarify that `@supabase/server` handles stateless header-based auth for backend runtimes, while `@supabase/ssr` handles cookie-based session management for SSR frameworks like Next.js. The two coexist. This distinction matters because the naming could confuse developers about which package to use where.

**Framework adapter strategy** is pragmatic. Hono ships with a first-party adapter; H3 (used by Nuxt) already has a community-contributed adapter. The team is accepting more community adapters rather than trying to build and maintain every integration themselves. This is the right call for an open-source project — the community knows their frameworks better than Supabase does.

The package is in public beta, which means the API surface may evolve. But the design direction — minimal boilerplate, declarative auth, runtime portability, AI-compatible patterns — is clearly right. If it delivers on its promises, `@supabase/server` could become as essential to Supabase's serverless story as `@supabase/ssr` is to its frontend story.
