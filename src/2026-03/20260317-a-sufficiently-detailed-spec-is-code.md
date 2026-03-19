# A sufficiently detailed spec is code
**Source**: https://haskellforall.com/2026/03/a-sufficiently-detailed-spec-is-code
**Date**: 2026-03-17
**Author**: Gabriella Gonzalez
**Keywords**: specification, code generation, agentic coding, formal methods, Haskell, Symphony, Dijkstra, AI coding tools, natural language specifications

## Elevator pitch
Making specifications precise enough for reliable AI code generation requires contorting them into code—Dijkstra's principle that formal notation is necessary for precision applies equally to AI-readable specs, meaning specs transmute rather than eliminate programming labor.

## Takeaways
- Misconception 1: specifications are simpler than code—precision requirements force specs to contain database schemas, algorithms, and literal pseudocode (as in OpenAI's Symphony spec).
- Misconception 2: specifications promote more thoughtful engineering—when optimized for delivery speed, they become "AI-written slop" lacking coherence and critical analysis.
- Dijkstra's principle: narrower formal interfaces are necessary for precision; broader natural language cannot escape this requirement.
- Practical evidence: generating Symphony in Haskell using Claude Code with an extensive specification still produced multiple bugs and ultimately failed to function reliably.
- Core conclusion: specifications transmute labor rather than eliminate it; when prioritizing delivery speed, direct code authorship may be preferable to specification intermediaries.

## Synthesis
Gonzalez's argument is a precise technical critique of a claim circulating in the AI coding space: that writing natural language specifications is easier and more cognitively accessible than writing code. The claim assumes that precision can be conveyed in natural language, but Dijkstra's observation—that formal notation is necessary precisely because natural language is ambiguous—applies to AI-targeted specifications just as it does to human-targeted ones.

The Symphony example is compelling because it comes from an AI company's own project spec. When a company trying to demonstrate specification-driven development produces a spec that contains database schemas and pseudocode, it provides direct evidence that precise specification converges toward code regardless of intent. The spec isn't instead of code; it's a different notation for code.

The delivery-speed dynamic is important. When specifications are produced under time pressure—as most software deliverables are—they lose the careful deliberation that would make them valuable. The resulting specs are as error-prone as quickly-written code but less verifiable. Code can be compiled and tested against behavior; informal specifications can't be automatically verified for completeness or consistency.

The failed Haskell generation experiment provides personal empirical evidence. Even with a detailed specification, Claude Code produced a non-functional implementation with multiple bugs. This is consistent with the theoretical argument: if the specification lacks the precision of code, the code generator must fill in ambiguities with assumptions that may not match the spec author's intent. More detailed specs improve outcomes but don't eliminate this problem—they just move it to a different level of the abstraction hierarchy.
