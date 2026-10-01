# Distributed Databases with Peter Mattis
**Source**: The Pragmatic Engineer (pragmaticengineer@substack.com)
**Date**: 2026-09-30
**Author**: Gergely Orosz
**Keywords**: Peter Mattis, CockroachDB, Cockroach Labs, GIMP, Google, Gmail, Colossus, B-trees, LSM trees, Pebble, Raft consensus, Spanner, distributed databases, AI coding, code review

## Elevator pitch
Peter Mattis — co-founder and CTO of Cockroach Labs, original creator of GIMP, and former Google engineer — shares his journey from open source to Google to building a distributed database company, with deep technical insights on B-trees, Colossus, consensus protocols, and how AI has brought him back to coding after years in management.

## Takeaways
- Peter initially turned down Sergey Brin's offer to join Google because of the commute from San Francisco to Mountain View; joined another startup first, then accepted when Google reached out again
- He almost didn't ship GIMP after seeing a competitor's announcement, but shipped anyway — "there's always going to be someone else working on your idea... most won't ship it"
- B-trees were used in the first version of Gmail: threads and unread counts were tracked by B-trees, with each incoming message matched to a thread using the search index
- Colossus reduced Google's file storage overhead by 33% while increasing redundancy, using Reed-Solomon erasure coding instead of GFS's three full copies
- Peter twice "beat" standard library data structures: replaced std::map's red-black tree with a faster, smaller B-tree at Google, and built a Swiss Table implementation for Go that was faster than the built-in map and made it into the Go library
- CockroachDB's design was inspired by Google's Colossus and Spanner; uses Pebble (open-sourced by Peter in 2019) as its storage engine, moving away from RocksDB
- For consensus, CockroachDB uses three replicas by default (up to five for system tables) — with fewer, recovery after crashes isn't reliable
- Peter predicts we will stop reviewing code: "the agents are getting better; you're having to give less and less scrutiny... we're materially going to stop looking at the code in the same way we don't look at assembly anymore"
- Non-engineers at Cockroach Labs built ~1,000 internal apps in a couple of months using an internal platform ("internal Lovable"), echoing OpenAI's observation that non-engineers moved token spend from ChatGPT to Codex in 4 months
- On flow with AI: "it's maybe a bit less intense, but you're managing more things cognitively... like a college professor with a whole swarm of research assistants"