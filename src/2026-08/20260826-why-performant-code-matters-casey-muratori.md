# Why Performant Code Matters (But Gets Widely Ignored), with Casey Muratori
**Source**: https://newsletter.pragmaticengineer.com/p/why-performant-code-matters-but-gets
**Date**: 2026-08-26
**Author**: The Pragmatic Engineer / Gergely Orosz
**Keywords**: software performance, Casey Muratori, clean code, TDD, CPU architecture, assembly, premature optimization, game development

## Elevator pitch
Casey Muratori argues that software performance is critical to the bottom line yet widely dismissed by the industry, and that the standard profiler-driven optimization approach is backwards—engineers should start from what hardware can theoretically do and close the gap.

## Takeaways
- Profiler-driven optimization finds only a local minimum; every great optimizer Casey has worked with starts by establishing what the hardware can theoretically do, then doesn't stop until they've closed the gap to that performance level
- Learning to read assembly (not write it) requires only 20-30 instructions and gives engineers direct insight into what the compiler produces and where the time goes
- "Premature optimization is the root of all evil" is widely misused as an excuse to delay performance work; not optimizing in time means only hotspots can be fixed later, not the architectural issues that create poor performance
- Understanding CPUs comes down to three things: how data moves (load/store units, L1-L3 caches), how instructions flow (branch prediction, i-cache), and execution unit scheduling (raw throughput per operation type)
- Casey critiques "clean code" practices, arguing that many received programming wisdom items are "just nonsense" that nobody has tested in practice, and that tests should be a cost/benefit decision rather than put in place by default
- The games industry already had its "AI moment" when licensable engines flooded the market, destroying organic discovery—a cautionary tale for AI's impact on software

## Synthesis
Casey Muratori, programmer and game developer known for Handmade Hero and his Computer, Enhance Substack, has spent years evangelizing software performance to an industry that largely dismisses it. The Pragmatic Engineer podcast conversation reveals a systematic critique of how the software industry treats performance—and why the conventional wisdom is often wrong.

The core argument is that the standard approach to optimization—profile, tweak hotspots, check stats—is fundamentally limited. It finds local minima, not global ones. Every great optimizer Casey has worked with takes the opposite approach: establish what the hardware can theoretically deliver, then work backward to close the gap. This requires understanding what the CPU is actually doing, which Casey reduces to three pillars: data movement (load/store units and cache hierarchy), instruction flow (branch prediction and instruction cache), and execution unit scheduling. Knowing these, he says, lets you predict from any CPU announcement roughly how well it performs.

The interview challenges several sacred cows. "Premature optimization is the root of all evil" is the most abused quote in programming, says Casey—used as an excuse to delay performance work until it's too late to fix architectural issues. Clean code practices are critiqued as performance-destroying dogma that hasn't been tested against alternatives. TDD's "test" component gets pushback: tests should be a cost/benefit decision, not a default. One trait of great engineers, Casey argues, is refusing to accept programming wisdom untested in the real world: "I find there's a lot of received programming wisdom that's just nonsense. Clearly, no one's ever tested it."

The conversation also touches on game development history and its parallels to AI. When game engines became licensable, anyone could build and publish a game—but the market flooded with tens of thousands of releases per year, destroying organic discovery. Casey sees this as a warning for the software industry's AI moment. He himself refuses to use AI for coding in his upcoming game: "I want to program things because I want to program them. If I only wanted output, I'd just get the Unreal Engine."