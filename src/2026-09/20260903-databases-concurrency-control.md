# How Databases Keep Their Sanity with Concurrency Control
**Source**: https://blog.bytebytego.com/p/how-databases-keep-their-sanity-with
**Date**: 2026-09-03
**Author**: Alex Xu (ByteByteGo)
**Keywords**: databases, concurrency control, transactions, pessimistic locking, optimistic locking, isolation levels, MVCC, data corruption, system design

## Elevator pitch
A practical deep dive into how databases handle concurrent transactions — from the four ways data gets corrupted, to pessimistic vs optimistic locking, to how MVCC stopped readers and writers from waiting for each other, to choosing the right isolation level.

## Takeaways
- Overlapping transactions are the normal condition in databases, not a rare edge case — multiple processes write to the same records constantly
- Four ways data gets corrupted: dirty reads, non-repeatable reads, phantom reads, and lost updates
- Pessimistic locking blocks everyone up front — acquire locks before modifying data, preventing conflicts but reducing concurrency
- Optimistic locking gambles that conflicts won't happen and checks afterwards — better throughput when conflicts are rare
- MVCC (Multi-Version Concurrency Control) was the breakthrough that stopped readers and writers from waiting for each other
- Isolation levels let you pick the right tradeoff between data protection and performance: Read Uncommitted, Read Committed, Repeatable Read, Serializable
- The safest setting (Serializable) was made practical through Snapshot Isolation — "strict without slow"

## Synthesis
ByteByteGo's article tackles one of the most fundamental problems in database engineering: how to maintain correctness when multiple transactions operate on the same data simultaneously. The article begins with a vivid example — a bank account with $100 where two simultaneous $10 withdrawals result in $90 instead of $80, because both transactions read the correct balance but overwrite each other's results.

The article explains that overlapping transactions are the normal operating condition for databases, not a rare exception. At any given moment, multiple processes are writing to the same records, and it takes only a collision within a few milliseconds to produce bugs. The piece covers four ways data gets corrupted: dirty reads (reading uncommitted data), non-repeatable reads (same query returning different results), phantom reads (new rows appearing in a range query), and lost updates (two writes overwriting each other).

Two main approaches handle these conflicts. Pessimistic locking acquires locks before modifying data — safe but reduces concurrency. Optimistic locking assumes conflicts are rare, performs the work, and validates before committing — better throughput when conflicts are infrequent. The major breakthrough was MVCC (Multi-Version Concurrency Control), which keeps multiple versions of rows so readers see a consistent snapshot without blocking writers. Finally, isolation levels (Read Uncommitted through Serializable) let database designers pick the right tradeoff, with Snapshot Isolation making the safest Serializable level practical by giving each transaction its own consistent snapshot.