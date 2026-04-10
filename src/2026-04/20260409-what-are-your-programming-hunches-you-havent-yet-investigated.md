# What are your programming "hunches" you haven't yet investigated?

**Source**: https://lobste.rs/s/gns27z/what_are_your_programming_hunches_you
**Date**: April 9, 2026
**Author**: Lobsters community
**Keywords**: programming, software architecture, accessibility, infrastructure as code, pointer compression, developer intuition, engineering discussion

## Elevator pitch
This Lobsters thread is a compact snapshot of how experienced programmers think in hypotheses: accessibility-first UI architecture, property-based infrastructure, compressed pointers, and codified codebase rules all surface as promising directions before they are fully validated.

## Takeaways
- Several commenters argue that designing UI systems from the accessibility tree outward could improve testing, scripting, and portability.
- Others revisit low-level ideas like 32-bit pointers on 64-bit systems as a practical way to save memory and improve cache behavior.
- A recurring theme is that mature software still hides many underexplored architecture choices behind familiar defaults.
- One interesting proposal is “property-based infrastructure,” where teams specify required system properties instead of enumerating exact infrastructure layouts.
- The thread also hints that AI agents may need codebase-specific rules written down explicitly instead of left as tribal knowledge.

## Synthesis
This thread is valuable less as a source of settled truth than as a view into how strong engineering ideas often begin: as informed hunches that have not yet been turned into full projects. The comments span UI architecture, systems performance, infrastructure design, and code quality, but they share a common instinct. Many parts of software development still inherit old defaults because they are familiar, not because they remain optimal. The best comments are essentially invitations to revisit those defaults.

The accessibility-first UI discussion is especially interesting. Commenters point out that if a toolkit starts from a semantic tree that already captures relationships, interactions, and testable structure, the benefits extend far beyond accessibility. You get cleaner automation, better scripting, more resilient testing, and potentially multiple rendering targets such as GUI, TUI, voice, or browser output. That is a useful reminder that “accessibility” is often shorthand for deeper architectural discipline rather than a bolt-on compliance layer.

The systems comments make a parallel point from the opposite end of the stack. Ideas like x32-style pointer compression or alternate ABI choices sound niche, but they reflect the same broader question: how much inefficiency persists simply because the ecosystem normalized one path? Software often carries hidden cost from historical tradeoffs that were sensible once but are no longer obviously right. Revisiting those assumptions can still unlock meaningful wins.

The thread is also quietly relevant to AI-assisted engineering. One commenter suggests that the specific rules senior developers follow in a codebase may need to become explicit machine-readable constraints. That is exactly the kind of shift many teams are starting to make: translating tacit engineering taste into concrete rules that agents and humans can both follow. In that sense, the conversation is not just a list of quirky ideas. It is a reminder that software progress often comes from noticing which assumptions have become invisible—and then daring to question them.
