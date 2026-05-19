# Zero: A Programming Language for Agents

**Source:** [zerolang.ai](https://zerolang.ai)
**Date:** 2026-05 (ongoing project)

## Summary

Zero is Vercel's experimental systems programming language designed from the ground up for AI agents as primary users. It aims for a small surface area, library-first design, agent-readable tooling with structured JSON diagnostics, and deterministic repair loops.

## Key Takeaways

- **Learnable on demand**: regular syntax, few special cases, small surface area — designed for agents to learn while working
- **Library-first**: broad, consistent standard library to minimize dependency searches
- **Inspectable by tools**: diagnostics, graphs, size reports, and repair plans as structured JSON
- **Explicit effects**: outside-world access, fallibility, and resource use stay visible to both readers and tools
- **Pre-1 by design**: breaking changes expected; run only in safe environments
- **Design philosophy**: regularity over cleverness, one obvious path, no legacy promises

## Code Example

```zero
fun answer() -> i32 {
  return 40 + 2
}

pub fun main(world: World) -> Void raises {
  if answer() == 42 {
    check world.out.write("math works\n")
  }
}
```

## Key Quote

> "The aim is a language that is easy to learn on the fly, deterministic to inspect and repair, standard-library first, and explicit enough that most tasks have one obvious path."

## Tags

Zero, Vercel, programming languages, AI agents, compiler, developer tools

---

*Generated from: https://zerolang.ai*
