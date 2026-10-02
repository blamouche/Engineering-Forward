# Why State Is the Hardest Thing in Software Design
**Source**: ByteByteGo (bytebytego@substack.com)
**Date**: 2026-10-01
**Author**: ByteByteGo
**Keywords**: state management, stateless, distributed systems, caching, consistency, CAP theorem, database, session state, application state, software architecture

## Elevator pitch
ByteByteGo explores why state is the hardest problem in software design — the advice to "make applications stateless" doesn't mean no state, it means relocating important state while keeping application servers replaceable — and walks through the strategies developers can use to manage it.

## Takeaways
- State is information a system retains that affects functionality: login sessions, document text, task completion logs, database records
- "Make the application stateless" is commonly misunderstood — it means making application servers easy to replace while putting important state elsewhere, not eliminating state entirely
- Understanding state requires answering three questions: why does state exist, who owns it, and what happens when it becomes unavailable
- The difficulty is keeping state correct as requests overlap, servers are added, machines fail, and software is deployed
- The article serves as a primer on state management strategies for distributed systems design