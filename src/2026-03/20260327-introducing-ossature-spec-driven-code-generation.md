# Introducing Ossature: Spec-Driven Code Generation
**Source**: https://ossature.dev/blog/introducing-ossature/
**Date**: Unknown
**Author**: Ossature
**Keywords**: code generation, specs, harness engineering, LLM tooling

## Elevator pitch
Ossature is an open‑source harness for spec‑driven code generation that validates specs, audits them with an LLM, and then generates code task‑by‑task with strict context boundaries.

## Takeaways
- Large codebases fail when LLMs generate components without coherent scaffolding.
- Ossature uses structured specs (SMD) and optional architecture files to define behavior and interfaces.
- It follows a validate → audit → build pipeline, with human‑editable task plans.
- Each generation task gets only the context it needs, reducing drift.
- Verification and automated fixing loops are built into the workflow.

## Synthesis
The Ossature announcement positions the tool as a response to a key bottleneck in LLM‑generated software: coherence across many files and modules. While models can generate small components well, full projects often fall apart because nothing enforces consistency. The post argues that the real problem is harness engineering—creating constraints, tests, and structure so the generated output remains reliable. Ossature aims to provide that harness in an open‑source, spec‑driven way.

Projects in Ossature are defined by specification files written in a markdown‑based SMD format. Specs describe behaviors, inputs, outputs, error cases, and implementation details with enough precision for an LLM to implement correctly. The post emphasizes that vague requirements lead to guesswork, while concrete rules (like exact edge‑case behavior) help models stay consistent. Teams can also add architecture definitions (AMD) to lock down file paths and interfaces, or let Ossature infer architecture during an audit step.

The workflow has three stages. First, validation parses specs and checks structural integrity (dependencies, cycles, duplicates) without invoking any model. Second, an audit uses an LLM to detect ambiguities and generate a build plan. The plan is a TOML file listing tasks, their dependencies, required spec sections, injected files, and verification commands. This plan is human‑readable and editable, so teams can reorder tasks or adjust verification before code generation starts.

In the build stage, Ossature executes each task in order. For each task it assembles a narrowly scoped prompt composed of selected spec sections, required interface files, and any explicit context files. The LLM produces code, verification runs, and a fixer agent attempts repairs on failure up to a set number of tries. All prompts, outputs, and logs are saved, improving traceability when something goes wrong in later steps.

A major design principle is narrow context. Instead of feeding a giant repository to a model, each task sees only the components it must interact with, reducing confusion and architectural drift. Dependencies are explicit, similar to header files in C, ensuring downstream tasks only rely on published interfaces. This approach reflects broader harness‑engineering advice: constrain the solution space rather than asking models to “figure it out.”

Overall, Ossature is presented as a structured alternative to ad‑hoc agentic coding. It treats specs as the source of truth, enforces deterministic boundaries, and adds human‑reviewable planning and verification. The goal is not just code generation, but reliable, maintainable software produced through a repeatable harness.
