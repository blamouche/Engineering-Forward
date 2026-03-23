# AI Code: Semantic vs Pragmatic Functions
**Source**: https://aicode.swerdlow.dev/
**Date**: March 23, 2026
**Author**: Unknown
**Keywords**: code structure, semantic functions, pragmatic functions, models

## Elevator pitch
A short essay on writing self‑documenting code by separating semantic functions, pragmatic functions, and strong data models.

## Takeaways
- Semantic functions are minimal, side‑effect‑free building blocks.
- Pragmatic functions orchestrate complex flows and can tolerate messiness.
- Data models should make invalid states impossible through tight typing.
- Over‑generalized models and functions lead to brittle systems.
- Clear naming and structure reduce review burden for humans and agents.

## Synthesis
This essay argues that code should be self‑documenting, and that the best way to achieve this is by separating semantic and pragmatic functions. Semantic functions are described as minimal, side‑effect‑free units that take all required inputs and return all necessary outputs. Their role is correctness and reusability, making them easy to test and reason about. Pragmatic functions, by contrast, are wrappers that orchestrate complex flows and can contain messy logic. They should be used sparingly and documented with comments that highlight non‑obvious behavior.

The piece extends the idea to data modeling. Good models should make invalid states impossible: optional fields create ambiguity, loosely typed values invite misuse, and generic structures collapse distinct concepts. The author advocates for precise naming and even branded types to prevent accidental misuse, so incorrect states fail at construction rather than far downstream.

A recurring warning is about drift. Semantic functions can slowly turn pragmatic if they accrete side effects, and models can become junk drawers as teams add “just one more field.” When this happens, the codebase becomes harder to understand, and both humans and AI agents pay a tax in review time and bug risk.

The essay’s core message is architectural discipline. By keeping semantic building blocks small and clean, pragmatic flows explicit, and models tightly scoped, teams can build codebases that are easier to read, test, and maintain—especially in an era where AI agents will increasingly generate and review code.
