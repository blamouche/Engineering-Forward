# Rethinking Search as Code Generation
**Source**: https://research.perplexity.ai/articles/rethinking-search-as-code-generation
**Date**: 2026-06-01
**Author**: Perplexity Research
**Keywords**: search-as-code, SaC, agentic-search, Perplexity, SDK, sandbox, retrieval-pipeline, code-generation, agent-harness

## Elevator pitch
Perplexity introduces Search as Code (SaC), a new search architecture that exposes the building blocks of search as composable SDK primitives — letting AI agents write and execute Python code in secure sandboxes to assemble task-specific retrieval pipelines, achieving 100% accuracy and 85% token reduction on a 200-CVE benchmark.

## Takeaways
- Traditional monolithic search (model issues query, engine runs fixed pipeline, model consumes results) is fundamentally broken for agents that run tasks spanning thousands of retrieval operations
- SaC exposes search stack components — retrieval, ranking, filtering, fanouts, rendering — as atomic primitives within an Agentic Search SDK, orchestrated via model-generated Python code in secure sandboxes
- Three tightly coupled layers: models as control plane, compute sandboxes for deterministic execution, and the Agentic Search SDK as primitive set
- In a 200-CVE security research benchmark, SaC scored 100% accuracy while cutting token usage 85% (from 288.7K to 42.9K); all non-Perplexity systems scored under 25%
- Code serves as both orchestrator and gap-filler — agents can build custom capabilities not present in the SDK by writing ad-hoc code

## Synthesis
Perplexity introduces Search as Code (SaC), a new reference search architecture that fundamentally rethinks how AI agents interact with search systems. The core insight is that traditional monolithic search — where a model issues a query, the engine runs a predefined pipeline, and the model consumes results — is broken for the agent era. Today's agents complete tasks over hours or days, invoking hundreds or thousands of retrieval operations in minutes. A fixed pipeline cannot bend to all of them.

The key bottleneck is control. Frontier models are good at reasoning over fixed context, but the most powerful AI systems need to steer how context is retrieved, processed, aggregated, and rendered. Traditional search wasn't designed with this controllability in mind — human users can't be expected to exercise fine-grained control over pipeline internals. But code-capable agent harnesses can.

SaC's architecture has three layers. Models serve as the control plane, reasoning about directives and generating code to implement retrieval pipelines. Compute sandboxes provide deterministic execution through a secure code runtime, managing intermediate states across turns via filesystem-based serialization (tested as more reliable than REPL-style in-memory state for long trajectories). The Agentic Search SDK exposes Perplexity's search stack as composable primitives — not a preexisting search API packaged as a library, but a rearchitected stack where high-level endpoints are shorthand for common patterns, not the only option.

The flagship benchmark is a CVE vendor advisory task: identify and characterize 200+ high-severity CVEs from 2023–2025, each citing the vendor's own advisory with product and fix version. SaC scored 100% accuracy while cutting token usage 85.1% (288.7K → 42.9K). All non-Perplexity systems scored under 25%. The generated code demonstrated three patterns: fan-out over vendor-specific advisory query templates, LLM-driven refinement for sparse vendor-years, and schema-bound verification keeping only advisories tying one CVE to one product and fix version.

Code serves as both orchestrator and gap-filler. Beyond orchestrating existing SDK primitives, the model can write ad-hoc code for capabilities not present in the SDK — like a complex regex that isn't efficiently implementable via search query syntax. The model fetches a superset in parallel, then narrows with a few lines of generated code, keeping the SDK lean while covering edge cases. The SDK was optimized via a continuous autoresearch loop running over weeks, proposing and validating improvements against latency, codegen quality, and task performance metrics. Agent Skills were developed to teach models to effectively harness the SDK, constrained to under 2,000 tokens to guard against context bloat.

SaC reflects a broader change in software design: combining token-space reasoning with deterministic compute. The most capable systems will combine both forms rather than choosing between them.