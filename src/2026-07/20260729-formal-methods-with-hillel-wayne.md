# Formal Methods with Hillel Wayne
**Source**: https://newsletter.pragmaticengineer.com/p/formal-methods-with-hillel-wayne
**Date**: 2026-07-29
**Author**: Gergely Orosz
**Keywords**: formal-methods, tla-plus, verification, distributed-systems, software-engineering, property-based-testing

## Elevator pitch
Hillel Wayne makes the case that formal methods like TLA+ are essential tools for reasoning about complex systems, but predicts AI will increase their use only modestly—from 0.1% to perhaps 0.3% of the industry—while property-based testing remains the more practical approach for most engineers.

## Takeaways
- The "are we real engineers?" debate has a nuanced answer: software engineering requires real rigor, and version control is one of its unique advantages that traditional engineers envy
- TLA+ is a formal specification language by Leslie Lamport that models systems as state machines, enumerating all reachable states and checking predefined properties—Amazon used it to find a bug with a 35-step shortest error trace that passed all conventional testing
- Lack of practice makes most engineers bad at reasoning about concurrency and race conditions; TLA+ can surface race conditions immediately rather than months later in production
- Formal methods remain niche because real-world specs are a "nightmare to write"—even simple problems like "find the file with the most lines" become complex when modeling edge cases like symlinks and unreadable files
- Hillel recommends most engineers adopt property-based testing as a practical middle ground: define properties, throw thousands of inputs at the system, and get lightweight formal verification without the overhead
- AI won't make formal verification mainstream, but will increase its use slightly; people who succeed at using AI to generate formal specs are often already formal verification experts

## Synthesis
This podcast episode with Hillel Wayne is one of the clearest introductions to formal methods for working engineers. Wayne, a formal methods consultant and author of "Logic for Programmers," brings a pragmatist's perspective that cuts through the hype.

The conversation starts with a fascinating cross-disciplinary comparison. Wayne's "Crossover Project" interviewed ~20 people across traditional and software engineering. The key finding: version control is genuinely unique to software—traditional engineers wish they had it. But traditional engineering has something software lacks: comprehensive reference books on fundamentals. Wayne laments that software has no equivalent of "The First Snap-Fit Handbook" (a 500-page tome on plastic clips)—there isn't even a canonical book on how to version an API.

The technical meat centers on TLA+, which Wayne demonstrates with a live walkthrough. The core insight is that TLA+ models your system as a state machine and then exhaustively checks all reachable states against properties you define. This is how Amazon found a subtle distributed systems bug with a 35-step error trace—something no amount of conventional testing would have caught. The tool literally enumerates every possible interleaving of concurrent operations.

But Wayne is candid about the limitations. Writing real-world specs is painful. Even trivial problems balloon in complexity when you model all edge cases. His practical recommendation for most engineers: stop at property-based testing. Define invariants, let the framework generate thousands of inputs, and catch the vast majority of bugs without the full formal methods investment.

On AI, Wayne is measured. He doesn't buy the "AI will make formal verification mainstream" narrative. The people who successfully use AI to generate TLA+ specs tend to already be experts. But even increasing formal methods adoption from 0.1% to 0.3% of the industry would be significant—it would mean more critical systems verified, more bugs caught before production. The episode also covers other formal methods tools like Alloy, Dafny, and PRISM, giving engineers a map of the landscape beyond TLA+.