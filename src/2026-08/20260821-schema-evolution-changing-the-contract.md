# Schema Evolution: Changing the Contract Without Breaking What Runs
**Source**: https://blog.bytebytego.com/p/schema-evolution-changing-the-contract
**Date**: 2026-08-20
**Author**: ByteByteGo
**Keywords**: schema evolution, backward compatibility, forward compatibility, expand and contract, API versioning, database migration

## Elevator pitch
Schema changes are the hardest kind of software change to get right because multiple versions always coexist; this article maps the strategies — from expand-and-contract migrations to schema registries — that let you evolve data contracts without breaking running systems.

## Takeaways
- More than one schema version is always in play simultaneously: mobile apps from 18 months ago still call your API, queue messages from old consumers still arrive, and rows written years ago are still read by current code.
- Backward compatibility means new code reads old data; forward compatibility means old code reads new data. A safe migration requires both, and the expand-and-contract pattern (add field, deploy, migrate data, remove old field, deploy again) is the canonical way to achieve it.
- Breaking changes include renaming fields, removing fields, and changing types — but qualifiers matter: making a field optional is backward-compatible; making an optional field required is not.
- Schema registries (Avro, Protobuf, JSON Schema) enforce compatibility checks at deploy time, preventing a producer from shipping a schema that breaks existing consumers.
- The same problem surfaces differently across databases (dual-write), APIs (versioned endpoints), and event streams (topic-based evolution), and each domain has its own best-practice patterns.

## Synthesis
Schema evolution is one of those infrastructure topics that seems trivial in code review — rename a column, add a field — but becomes a production incident when two versions of your service are running simultaneously and only one understands the new format. The article systematically walks through why the problem is inevitable (version overlap is always present), what makes a change safe or breaking, and how to manage it.

The core insight is that a schema is a contract, and changing a contract requires coordination with all parties that depend on it. The expand-and-contract pattern is the workhorse: first add the new field alongside the old one (backward and forward compatible), deploy, migrate existing data, then remove the old field in a second deployment. This two-phase approach is verbose but safe.

Schema registries add a governance layer, preventing producers from registering incompatible schemas. They turn a runtime failure into a deploy-time error, which is always preferable. The article also covers how different domains — databases, REST APIs, event streams — each have their own evolution patterns. Database changes need dual-write phases, APIs use versioned endpoints or content negotiation, and event streams use topic-level compatibility modes.

The practical takeaway is that any team operating a distributed system should treat schema changes with the same caution as API versioning, and invest in tooling (registries, compatibility checks, automated migration scripts) that makes the safe path also the easy path.