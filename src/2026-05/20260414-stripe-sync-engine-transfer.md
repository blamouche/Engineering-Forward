# We're Transferring the Stripe Sync Engine to Stripe
**Source**: https://supabase.com/blog/stripe-sync-engine-transfer
**Date**: 2026-04-14
**Author**: raminder_singh, matt_linkous, gregor_vand, ana_mogul
**Keywords**: Stripe, Supabase, sync engine, Postgres, open-source, billing, Apache 2.0, integration

## Elevator pitch
Supabase is transferring its open-source Stripe Sync Engine repository to Stripe's GitHub organization, deepening a collaboration that brings Stripe billing data directly into Postgres with one-click dashboard integration.

## Takeaways
- The Stripe Sync Engine, originally open-sourced by Supabase in 2021, is moving from `supabase/stripe-sync-engine` to `stripe/sync-engine` under the Apache 2.0 license with no breaking changes for existing users.
- Stripe engineers contributed significantly to the project: incremental sync with cursor-based pagination, JSONB storage with generated columns, multi-account Stripe Connect support, and a new CLI with event ordering.
- A key technical breakthrough was Stripe's work on automatic incremental backfilling using Supabase Cron and Queue, enabling reliable large-scale data ingestion.
- The latest release adds coupons sync (a top user request), branching support for safer dev workflows, immediate sync on install, one-click upgrades, and SSL enforcement support.
- The transfer exemplifies Supabase's philosophy: build in the open, support the ecosystem, and contribute back as projects grow — even when that means handing the repo to a partner.

## Synthesis
The transfer of the Stripe Sync Engine from Supabase's GitHub organization to Stripe's represents a mature, pragmatic evolution in open-source collaboration between two major platforms. What started in 2021 as Supabase solving its own problem — joining billing data in Stripe with product data in Postgres — grew through sustained open development and eventually attracted direct engineering contributions from Stripe itself.

The collaboration intensified after December 2025, when Supabase announced a one-click dashboard integration for the sync engine. Stripe engineers brought significant technical improvements: cursor-based pagination for incremental sync, JSONB storage with generated columns for queryable structured data, multi-account support for Stripe Connect platforms, and a new CLI with proper event ordering guarantees. Perhaps most importantly, Stripe built the automatic incremental backfilling system using Supabase Cron and Queue, which solved the hard problem of reliably ingesting all existing Stripe data at scale. This was the technical unlock that made the dashboard integration viable.

The repo transfer itself is pragmatic rather than dramatic. The code remains open-source under Apache 2.0. The old repo redirects to the new one. The dashboard integration continues working. Both teams will keep contributing. What changes is the symbolic ownership — this is now a Stripe project that Supabase contributes to, rather than the reverse. For a younger company like Supabase, this is a sign of ecosystem maturity: sometimes the right move is to let a project graduate to its natural home.

The latest release alongside the transfer adds meaningful improvements. Coupons sync addresses one of the most-requested features. Branching support lets developers test sync configurations on database branches before applying them to production. Immediate sync on install removes the friction of waiting for the first cron cycle. One-click upgrades, SSL enforcement support, and Admin/Owner-restricted install controls make the integration more production-ready. The dashboard also now shows Edge Function source code directly, improving transparency.

For developers, the practical value proposition remains unchanged and compelling: with Stripe data in Postgres, you can join billing data directly with application data for operational decisions (feature gating, subscription checks) and analytical queries (MRR calculation, churn analysis). The transfer to Stripe's GitHub organization doesn't change the technical value — it signals that the project has achieved enough importance to warrant being maintained directly by the company whose API it serves.
