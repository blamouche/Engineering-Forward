# Why Rust Is Different, with Alice Ryhl
**Source**: https://newsletter.pragmaticengineer.com/p/why-rust-is-different-with-alice
**Date**: May 20, 2026
**Author**: Gergely Orosz
**Keywords**: Rust, memory safety, Tokio, compiler, Linux kernel, AI agents, systems programming, ownership

## Elevator pitch
Alice Ryhl from Google's Android Rust team explains why Rust's compiler-enforced correctness, memory safety, and edition-based evolution make it uniquely suited for reliable backend systems, AI agent-generated code, and kernel-level work — and why developers stick with it despite the steep learning curve.

## Takeaways
- Rust turns implicit failures (null checks, uninitialized variables, error propagation) into compile errors, making "once it compiles, it works" a real phenomenon
- The hardest part of learning Rust is not syntax but designing data structures that respect the ownership/borrowing model — newcomers often battle cyclic object graphs
- Rust's compiler feedback loop makes it an optimal language for AI agents: agents can iterate with the compiler, and the language blocks entire bug classes by design
- Rust editions (2015, 2018, 2021, 2024) allow breaking syntactic changes without breaking the ecosystem — crates on different editions interoperate seamlessly
- Rust in the Linux kernel graduated from experimental in December 2025, boosted by US DoD regulations pushing agencies away from non-memory-safe languages
- AI code review may matter more than AI code generation in safety-critical codebases — kernel maintainers are already using AI bots for patch review
- Risk of AI-assisted Rust: false fluency, where junior engineers accept AI-generated code that compiles without understanding why

## Synthesis
Gergely Orosz interviews Alice Ryhl, a software engineer on Google's Android Rust team and a core maintainer of Tokio, the most widely-used async runtime in Rust. The conversation spans Rust's design philosophy, its practical advantages over languages like TypeScript, Go, and C++, and its growing role in systems programming and AI workflows.

Ryhl's own career path illustrates a key dynamic in open source: she landed at Google not through an application but through years of answering questions on Rust forums and contributing to documentation and code. She became a Tokio maintainer while still in college. An email eventually arrived asking if she wanted to work on the Android Rust team.

At the technical level, Rust's defining characteristic is its compiler. Where other languages allow developers to forget null checks, leave variables uninitialized, or ignore error propagation, Rust makes these omissions into compilation errors. This design philosophy — turning implicit failures into explicit compiler feedback — produces code that, once it compiles, is far more likely to be correct. Ryhl describes refactoring in Rust as a mechanical process: change a return type or struct field, then follow the compiler errors until they stop. By the end, every affected location has been updated.

The learning curve, however, is real. Ryhl identifies data structure design as the primary challenge, not syntax. Newcomers instinctively build cyclic object graphs — a Book referencing Page objects that reference back to the Book — and end up fighting the borrow checker. The solution is to embrace structs and internalize ownership semantics rather than replicating patterns from garbage-collected languages.

Two forward-looking insights stand out. First, Rust's compiler feedback loop makes it an ideal language for AI coding agents. Agents can propose changes, receive precise compiler feedback, and iterate — all while the language prevents entire classes of memory bugs. This combination of strictness and feedback may make Rust one of the best languages for agent-generated production code. Second, AI code review may prove more valuable than AI code generation in safety-critical contexts. Kernel maintainers are already experimenting with AI bots that review mailing-list patches, and early impressions are positive — quality and reliability have always mattered more than quantity in kernel development.

The governance story is equally interesting. Unlike Python or Linux, Rust has no benevolent dictator for life. Teams self-organize, delegate to each other, and hash out tough questions at in-person events like Rust All Hands. The editions mechanism — 2015, 2018, 2021, 2024 — allows the language to make breaking syntactic changes (like adding async/await as keywords) while keeping crates on different editions fully interoperable. This avoids the painful ecosystem-wide migrations that have fractured other language communities.

On the kernel front, Rust's graduation from experimental status at the December 2025 Linux Kernel Maintainer Summit is a milestone. Combined with US Department of Defense regulations steering agencies away from non-memory-safe languages, Rust adoption in the kernel and elsewhere is likely to accelerate. Ryhl also flags a cautionary note about AI-assisted Rust: the compiler's strictness can create a false sense of security when AI generates code that compiles but makes no functional sense — such as Rust versions of C build flags that serve no purpose. Junior engineers using AI to learn Rust risk accepting code without understanding why the compiler accepts it.
