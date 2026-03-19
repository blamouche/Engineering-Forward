# Temporal: The 9-Year Journey to Fix Time in JavaScript
**Source**: https://bloomberg.github.io/js-blog/post/temporal/
**Date**: 2026-03-11
**Author**: Jason Williams
**Keywords**: JavaScript, Temporal, datetime API, WebAssembly, Stage 4, standardization, Date object, temporal_rs, Rust, TC39

## Elevator pitch
After nine years of development, Temporal—a new JavaScript datetime API with immutable, timezone-aware, calendar-conscious types—reached Stage 4 standardization, replacing the Date object ported from Java in a 10-day sprint in 1995.

## Takeaways
- JavaScript's Date object was ported from Java in a 10-day sprint in 1995, creating issues that became the second-largest developer pain point after static typing: mutability, inconsistent month arithmetic, ambiguous parsing.
- Temporal introduces multiple specialized types (ZonedDateTime, Instant, PlainDate, etc.) that are immutable, timezone-aware, and calendar-conscious.
- `temporal_rs`: a shared Rust library developed by Google's team and Boa that passes all Temporal tests and serves multiple JavaScript engines—eliminating redundant implementation across engines.
- Current support: Firefox, Chrome, Edge, TypeScript, and Node.js; Safari in preview.
- The project exemplifies cross-organization collaboration: Microsoft, Google, Mozilla, Bloomberg, Igalia, and independent contributors contributed over nine years.

## Synthesis
The Temporal story is a useful case study in how browser standards actually work—and how long it takes to fix foundational decisions. Date was broken for decades before Temporal. Developers worked around it with libraries (Moment.js, then date-fns, then Luxon), each of which addressed different subsets of Date's problems while adding their own tradeoffs. The correct long-term solution—a new API designed from scratch—required nine years of standardization work.

The immutability change is more significant than it might appear. Mutable date objects create a class of bugs where a function that receives a date can modify it, affecting the caller's copy. This pattern is subtle enough to survive code review and testing in many cases. Immutable dates make the bug class impossible: modifying a date always requires creating a new date, making mutation explicit rather than accidental.

The `temporal_rs` Rust library is an interesting engineering achievement beyond Temporal itself. JavaScript engine implementers typically re-implement features independently in each engine—V8, SpiderMonkey, JavaScriptCore, ChakraCore—creating redundant work and potential behavioral divergence. A shared Rust library that compiles into each engine reduces implementation overhead and virtually eliminates cross-engine behavioral differences, since they all run the same underlying code.

The nine-year timeline reflects the genuine complexity of reaching consensus across major browser vendors, each with different implementation constraints, user bases, and organizational priorities. It also reflects the challenge of shipping backward-compatible changes: Temporal must not break the existing Date API, which means it runs alongside it rather than replacing it. The coexistence creates developer education challenges that a clean replacement wouldn't have.
