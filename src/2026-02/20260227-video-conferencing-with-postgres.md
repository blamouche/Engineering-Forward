# Video Conferencing with Postgres
**Source**: https://planetscale.com/blog/video-conferencing-with-postgres
**Date**: 2026-02-27
**Author**: Nick Van Wiggeren
**Keywords**: PostgreSQL, logical replication, real-time streaming, video conferencing, WebSocket, PlanetScale

## Elevator pitch
A developer successfully built a bidirectional video conferencing system using PostgreSQL's logical replication as a real-time message broker, demonstrating that a $5 database can stream 15fps video through JPEG frames stored in binary columns.

## Takeaways
- PostgreSQL as Real-Time Backbone: Logical replication enables reliable, ordered change streams without polling, making it viable for time-sensitive applications beyond traditional transactional use cases.
- Practical Performance: The system achieved 25-40KB per JPEG frame at 375-600 KB/s throughput per direction, with sub-100ms latency, proving modest database instances can handle continuous media ingestion.
- Alternative Approaches Have Tradeoffs: LISTEN/NOTIFY's 8KB payload limit and unlogged tables' incompatibility with replication both presented technical obstacles that made the table-based approach superior.
- Architectural Simplicity: The entire relay server required only approximately 400 lines of TypeScript, combining a SvelteKit frontend, Node.js WebSocket server, and PostgreSQL backend.
- Storage Flexibility: Video frames are crash-safe and queryable, enabling future retrieval and post-processing—a capability specialized video infrastructure typically doesn't offer.

## Synthesis
This project challenges conventional wisdom about database purpose and capability. While SpacetimeDB pioneered the concept of video calls through databases, this PostgreSQL implementation demonstrates the pattern's broader applicability to mature, widely-deployed systems.

The architecture leverages PostgreSQL's logical replication feature, which delivers INSERT, UPDATE, and DELETE events in commit order. Rather than polling with SELECT statements, the relay server subscribes to a replication stream, detecting new video frames as rows appear and forwarding them to recipients via WebSocket. This inversion—making the database push data rather than pull it—proves surprisingly elegant for real-time applications.

The technical execution involved encoding camera frames as JPEGs via browser canvas APIs and audio as 16-bit PCM samples, both packed into binary WebSocket frames with JSON headers. The recipient's browser reconstructs video from blob URLs and schedules audio samples on Web Audio APIs with careful jitter buffering to maintain synchronization.

Performance metrics revealed that a $5 PlanetScale PostgreSQL instance sustained the required throughput without degradation. The author observed approximately 76 frames per five seconds (15.2 fps) from each participant, matching the target specification. Latency remained acceptably low for real-time interaction.

The author deliberately rejected two plausible alternatives. LISTEN/NOTIFY, PostgreSQL's built-in pub/sub mechanism, enforces an 8KB payload ceiling. Unlogged tables, which accelerate inserts by skipping write-ahead logging, fail to integrate with logical replication, necessitating a return to polling-based retrieval.

Importantly, the author recommends against this approach for production video applications. WebRTC remains purpose-built for the domain and offers superior optimization. However, for developers seeking to understand logical replication mechanics or exploring how far a general-purpose database can extend into real-time domains, this project illuminates possibilities while maintaining reasonable engineering pragmatism. The durable, queryable nature of stored frames also opens possibilities for analytics and archival that typical ephemeral video infrastructure cannot provide.
