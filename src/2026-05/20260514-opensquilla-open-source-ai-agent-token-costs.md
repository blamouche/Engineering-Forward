# OpenSquilla launches open-source AI agent to cut token costs
**Source**: https://www.testingcatalog.com/opensquilla-launches-open-source-ai-agent-to-cut-token-costs/
**Date**: May 14, 2026
**Author**: Nero Soares
**Keywords**: OpenSquilla, open-source, AI agent, token cost optimization, ML routing, memory architecture, sandbox isolation

## Elevator pitch
OpenSquilla releases v0.1.0 — an open-source, self-hostable AI agent runtime that combines ML-based model routing, four-tier cognitive memory, and syscall-level sandbox isolation to cut token spend by 60-80% compared to flat single-model configurations.

## Takeaways
- An ML classifier routes simple queries to cheaper models and disables deep reasoning for lightweight tasks, reducing unnecessary token burn
- Four-tier memory (working, episodic, semantic, raw) with automatic consolidation every 24 hours — called "Memory Dream Consolidation"
- Syscall-level isolation via Bubblewrap (Linux) and Seatbelt (macOS) with three policy tiers, a denial ledger, and prompt injection protection
- Microkernel architecture: ~100-line core orchestrator with pluggable modules for providers, memory backends, and channels
- In testing, 80% of input tokens served from cache — $0.0094 total cost for 279K tokens across three prompts

## Synthesis
OpenSquilla enters the increasingly crowded agent framework space with a specific value proposition: cost optimization as a first-class architectural concern rather than an afterthought. While most frameworks focus on capability and flexibility, OpenSquilla's thesis is that most agent deployments burn tokens unnecessarily — reloading the same context, running expensive models on trivial queries, and packing unused skills into every context window.

The routing classifier is the key innovation: an ML model that combines hand-crafted signals (message length, code blocks, keyword patterns) with embedding-based semantic features to score each request by complexity. Simple queries route to cheaper models; deep reasoning is disabled for trivial tasks. The claimed 60-80% token reduction versus flat configurations is significant for teams running long-horizon agent workloads.

The memory architecture borrows explicitly from cognitive science: working, episodic, semantic, and raw memory layers with automatic consolidation. "Memory Dream Consolidation" — a nightly pass that restructures scattered memories — is both an evocative name and a practical solution to context fragmentation. Hybrid retrieval combining vector search with BM25 keeps data local via bundled ONNX inference.

On security, the syscall-level isolation (Bubblewrap/Seatbelt) avoids Docker dependencies, and the three-tier policy system with denial ledger is pragmatic for production deployment. The Apache-2.0 license and microkernel architecture make it suitable for teams wanting control over their agent infrastructure without cloud lock-in.
