# We're Transferring the Stripe Sync Engine to Stripe
**Source**: https://supabase.com/blog/stripe-sync-engine-transfer
**Date**: 2026-04-14
**Author**: raminder_singh, matt_linkous, gregor_vand, ana_mogul
**Keywords**: stripe, postgres, open-source, sync-engine, billing, integration, collaboration

## Elevator pitch
Supabase is transferring the Stripe Sync Engine repository to Stripe's GitHub organization after years of collaborative development, keeping it open source under Apache 2.0 while both teams continue building it together.

## Takeaways
- The Stripe Sync Engine moves from `supabase/stripe-sync-engine` to `stripe/sync-engine` after a deep engineering collaboration between the two companies
- Stripe engineers contributed significant improvements: incremental sync with cursor-based pagination, JSONB storage with generated columns, multi-account Stripe Connect support, and a new CLI
- The repo remains open source under Apache 2.0 — nothing breaks for existing users, and the Supabase dashboard integration continues to work
- New capabilities shipped alongside the transfer: coupons sync, branching support, immediate data sync on install, one-click upgrades, and SSL enforcement support
- The transfer is framed as a natural evolution of Supabase's philosophy: build in the open, support the tools and communities around them, and contribute back as things grow

## Synthesis
The Stripe Sync Engine started in 2021 as a solution to Supabase's own problem: billing data lived in Stripe, product data lived in Postgres, and there was no good way to join them. They built a tool to sync Stripe data into a `stripe` schema in Postgres, open-sourced it, and kept building in the open. It grew beyond expectations.

The turning point came in December 2025 when Supabase launched a one-click dashboard integration for the Sync Engine, built through close collaboration with Stripe's engineering team. Stripe engineers contributed directly: incremental sync using cursor-based pagination, JSONB storage with generated columns, multi-account support for Stripe Connect platforms, and a new CLI with proper event ordering. A key contribution was Stripe's work on automatic incremental backfilling using Supabase Cron and Queue, which enabled reliable, at-scale ingestion of existing Stripe data into Postgres — the feature that unlocked the dashboard integration.

The repo transfer to `stripe/sync-engine` is the next step in this collaboration. It stays open source under Apache 2.0, the old repo redirects, and all future changes from both teams go to the new repo. The latest release, shipped alongside the transfer, adds coupons sync (one of the most requested features), branching support for safer dev workflows, immediate data sync on install (no waiting for the first cron cycle), one-click upgrades, SSL enforcement support, and improved install/uninstall controls restricted to Admins and Owners.

The announcement frames the transfer not as a handoff but as a natural evolution of how Supabase operates: build in the open, collaborate with ecosystem partners, and when tools grow beyond their origin, support their continued growth wherever they live. Both teams keep building it together.
