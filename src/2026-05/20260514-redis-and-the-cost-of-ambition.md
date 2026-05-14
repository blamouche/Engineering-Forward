# Redis and the Cost of Ambition
**Source**: https://charlesleifer.com/blog/redis-and-the-cost-of-ambition
**Date**: May 12, 2026
**Author**: Charles Leifer
**Keywords**: Redis, Valkey, open source licensing, feature bloat, second-system effect, ambition, BSD vs AGPL, Redis Inc, antirez, RESP3, database vs cache

## Elevator pitch
Charles Leifer argues that Redis lost its identity through unchecked ambition — chasing every database trend from JSON documents to AI vectors — while Valkey's focus on unglamorous performance improvements proves the market's verdict on what Redis should have been.

## Takeaways
- Redis' original success came from being simple, fast, and conceptually coherent: a single-threaded in-memory data-structure server with a beautifully minimal wire protocol
- The project's ambition expanded from "advanced key-value store" to chasing MongoDB (JSON), Kafka (streams), ElasticSearch (full-text), graph databases, time-series, and now AI vectors
- Licensing (BSD → AGPL) and enterprise DBaaS dynamics alienated the community, with Redis Inc described as having "waged a scorched-earth campaign against its users"
- The RESP3 protocol and client-side caching are framed as classic second-system failure modes — complex solutions to self-inflicted problems
- Valkey's existence and adoption, focusing on multi-threaded performance, memory efficiency, and cluster reliability, is the market's final verdict on the feature-chasing approach

## Synthesis
Charles Leifer's essay, published May 12, 2026, is a meditation on Redis' trajectory from indispensable infrastructure to a project he believes has lost its way. The piece was prompted by antirez's PR to add an array type to Redis, which Leifer uses as a jumping-off point to examine how a project that once captured the developer zeitgeist perfectly ended up in what he calls "a bit of a crisis."

Leifer places Redis' golden age around 2011, when it perfectly captured the NoSQL, web-scale, and Ruby on Rails zeitgeist. At that time, Redis described itself as "an advanced key-value store and data structure server" — notably not a database. The design decisions that made Redis indispensable were threefold: a wire protocol simple enough to be understood and coded in an hour; single-threaded, event-driven, in-memory architecture that guaranteed atomic operations by construction; and a tastefully chosen set of data structures (strings, lists, hashes, sets, sorted sets) that covered web applications' most common needs.

The essay traces how ambition transformed the project. Leifer identifies a pattern where Redis chased "the latest cool thing developers are talking about on HN." When MongoDB was hot, Redis needed JSON document support. When ElasticSearch mattered, Redis needed full-text search. Kafka buzz drove stream support. Graph databases, time-series databases, and AI vectors each got their moment, generating what Leifer sees as a growing collection of half-baked features that ignore two realities: most people serious about these domains want the real thing, not a Redis module inheriting all of Redis' restrictions; and Redis' HA story is complicated, its persistence has nuanced tradeoffs, and its protocol pain and client fragmentation are real hurdles.

Leifer draws on his own 2015 analysis of antirez's Disque project, where he predicted abandonment based on antirez's admission that Disque was built "in astronaut mode" — not triggered by an actual use case. That prediction held: Disque became abandonware. Leifer extends the same logic to Redis' feature explosion: features developed because they're interesting problems, not because Redis users need Redis to become a message broker, search engine, or graph database.

The licensing saga gets particular attention. Redis Inc's 2024 switch from BSD to a tri-license model (with AGPL as the lone OSI option) is framed as a "scorched-earth campaign" that backfired. Leifer traces the company's origin as Garantia Data, a NoSQL cloud hosting service that eventually signed antirez and took over Redis trademark rights, setting the stage for the licensing rugpull.

Valkey serves as the essay's counterpoint and conclusion. Rather than chasing feature bullet points, Valkey invested in multi-threaded performance, memory efficiency, cluster reliability, and throughput — the unglamorous engineering that makes infrastructure dependable. Leifer sees Valkey's existence and adoption as the wider market's final verdict: the community wanted a better Redis, not a Redis that tried to be everything.
