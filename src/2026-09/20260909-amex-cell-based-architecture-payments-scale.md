# Built for Reliability: How American Express Processes Payments at Scale
**Source**: https://blog.bytebytego.com/p/built-for-reliability-how-american
**Date**: 2026-09-08
**Author**: ByteByteGo (interview with Ben Cane, Distinguished Engineer at American Express)
**Keywords**: cell-based architecture, payment processing, reliability, failure isolation, Global Transaction Router, deterministic routing, idempotency, microservices, resiliency

## Elevator pitch
American Express's payment platform uses a cell-based architecture where each cell is a complete, self-sufficient copy of the processing stack — and when a cell fails mid-transaction, the platform discards all partial work and restarts from scratch in a healthy cell, trading a few hundred milliseconds of wasted compute for complete failure isolation.

## Takeaways
- A cell is defined by its failure boundaries, not infrastructure constructs: it owns its microservices, databases, DNS, and supporting infrastructure, with no synchronous cross-cell dependencies in the critical path
- The Global Transaction Router is the single component that enforces cell boundaries — kept deliberately simple (no business logic, no persistent state) to remain trustworthy as the platform's chokepoint
- Two data strategies: reference data is pushed to every cell ahead of time (avoiding cold-cache penalties), while dynamic data uses deterministic routing to move the transaction to the data rather than the data to the transaction
- Mid-transaction failures trigger a full restart: the orchestrator sends the transaction back to the router, which selects a healthy cell, and the second cell processes from the beginning with the original input — no shared state between cells
- The "point of no return" is placed as late as possible in the payment flow to maximize the recoverable window, with idempotency identifiers protecting against duplicates across reroutes
- Design tradeoffs are explicit: duplicated services across cells, dropped log records under pressure (buffer truncation), delayed global visibility, and rejected transactions when consistency can't be guaranteed

## Synthesis
American Express's cell-based architecture is one of the clearest real-world explanations of how to build a mission-critical system that survives partial failure without degrading into a fragile distributed mess. The core insight is that cells are defined by failure boundaries, not by infrastructure — a cell is everything required to process a transaction end-to-end, and the boundary matters because crossing it is where the dangerous territory begins.

The Global Transaction Router is the architectural linchpin. Every transaction enters through it, and any transaction moving between cells travels back through it. Concentrating that much responsibility in one component is usually a red flag, but Amex's approach of keeping the router deliberately simple — no business logic, no persistent state, configuration loaded into memory and updated asynchronously — is the engineering discipline that makes it work. A router that accumulated business rules would gradually become a centralized system, which is exactly what the cell architecture is designed to avoid.

The most interesting design decision is the restart-from-scratch approach to mid-transaction failures. Instead of checkpointing and resuming (which would require sharing state between cells), Amex discards all partial work and restarts the transaction from the beginning in a healthy cell. This sounds wasteful, but the tradeoff works because a card payment is short — a few hundred milliseconds of wasted compute is trivially cheap compared to the permanent structural dependency that shared state would create between every pair of cells. This is a clean example of how accepting redundant work can buy you a fundamentally simpler and more reliable system.