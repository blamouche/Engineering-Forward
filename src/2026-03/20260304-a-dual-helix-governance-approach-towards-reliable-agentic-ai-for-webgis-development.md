# A Dual-Helix Governance Approach Towards Reliable Agentic AI for WebGIS Development
**Source**: https://arxiv.org/abs/2603.04390
**Date**: March 04, 2026
**Author**: Levente Juhasz
**Keywords**: agentic AI, governance, WebGIS, reliability, software engineering

## Elevator pitch
The paper argues that reliable agentic AI needs governance structures—not just bigger models—and demonstrates a three‑track architecture that materially improves maintainability in a real WebGIS refactor.

## Takeaways
- Reliability failures stem from structural issues like context limits, forgetting, and stochasticity.
- The proposed “dual‑helix governance” reframes these as governance problems, not capability gaps.
- A three‑track architecture (Knowledge, Behavior, Skills) externalizes facts and protocols.
- Applied to a WebGIS tool, the governed agent reduced complexity and improved maintainability.
- The approach is implemented in the open‑source AgentLoom toolkit.

## Synthesis
This paper proposes a governance‑first approach to making agentic AI reliable in WebGIS development. The authors argue that common failures—context constraints, cross‑session forgetting, stochastic outputs, instruction drift, and rigidity—are structural governance problems rather than simple model‑capacity deficits. In other words, throwing a bigger model at the task does not solve the underlying operational instability of agents working on complex software systems.

The proposed solution is a “dual‑helix governance” framework. The paper implements this through a three‑track architecture: Knowledge, Behavior, and Skills. The Knowledge track externalizes domain facts and task context, often via a knowledge graph substrate. The Behavior track encodes executable protocols and constraints that guide agent actions. The Skills track focuses on capabilities and tools, with a self‑learning cycle that expands the agent’s knowledge over time. The goal is to stabilize execution by separating durable facts and processes from the model’s volatile internal state.

The authors argue that externalizing knowledge and protocols reduces the impact of LLM limitations. Context windows become less binding when facts are stored in a persistent substrate; cross‑session forgetting is mitigated through structured knowledge storage; stochasticity is constrained by executable rules; and instruction failure is addressed through enforceable protocols rather than relying on prompt adherence alone. This framing shifts the reliability challenge from model performance to system design.

To validate the approach, the paper applies the framework to the FutureShorelines WebGIS tool. A governed agent refactors a 2,265‑line monolithic codebase into modular ES6 components. The reported results include a 51% reduction in cyclomatic complexity and a 7‑point increase in maintainability index, indicating more readable and maintainable code. A comparative experiment against a zero‑shot LLM suggests that governance structures, not just raw model capability, drive operational reliability in this context.

The paper positions this as a general pattern for agentic software engineering: reliable agents require explicit governance layers that manage memory, rules, and workflows. The emphasis is on system architecture rather than prompt tricks. The authors also note that the approach has been packaged into an open‑source toolkit called AgentLoom, which operationalizes the governance framework.

Overall, the work contributes a concrete system design for stabilizing agentic AI in real software engineering tasks, particularly in the geospatial domain. It argues that reliability emerges from structured governance that persists across sessions and constrains behavior, rather than from larger models or ad‑hoc prompt engineering. The empirical results on a real WebGIS refactor give the proposal practical credibility and suggest a path for extending agentic AI to more rigorous development environments.
