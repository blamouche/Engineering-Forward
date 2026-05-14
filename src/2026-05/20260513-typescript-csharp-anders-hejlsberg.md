# TypeScript, C# and Turbo Pascal with Anders Hejlsberg
**Source**: https://newsletter.pragmaticengineer.com/p/typescript-c-and-turbo-pascal-with
**Date**: 2026-05-13
**Author**: Gergely Orosz (interview with Anders Hejlsberg)
**Keywords**: Anders Hejlsberg, TypeScript, C#, Turbo Pascal, programming languages, compiler design, AI-assisted development, software craftsmanship

## Elevator pitch
Anders Hejlsberg, creator of Turbo Pascal, Delphi, C#, and TypeScript, reflects on four decades of language design and predicts AI will transform developers into "project managers of junior programmer agents."

## Takeaways
- Hejlsberg's design philosophy emphasizes the entire developer workflow (IDE, debugger, compiler), not just the language itself
- Small teams of experienced designers are optimal: C# was designed by only six people meeting six hours per week
- Async/await succeeded because compilers can generate state machines that humans hate writing by hand
- AI's effectiveness in a language depends primarily on training data volume, not language design features
- Hejlsberg predicts code review will become the primary craft of software engineering as AI agents generate most code

## Synthesis
This episode of The Pragmatic Engineer podcast features a landmark interview with Anders Hejlsberg, arguably the most influential programming language designer of the modern era. Over a 75-minute conversation, Hejlsberg traces his career from writing his first compiler for an HP 2100 with 32K of memory to his current role as a Microsoft Technical Fellow, offering unique insights into what makes programming languages succeed and how AI is reshaping the craft.

Hejlsberg's career began at Borland, where Turbo Pascal achieved "10x better for 1/10th of the price"—selling for $49.95 when competitors cost $500, while being faster and more interactive. His first "debugger" was an elegant hack: the compiler printed the program counter on runtime errors, and re-running in a special mode would show which line was being processed at that address. This constraint-driven creativity set a pattern for his career: always think about the complete developer experience, not just compilation. The move to Microsoft in 1996 was catalyzed by the Sun vs. Microsoft Java lawsuit (1997-2001), which forced Microsoft to create its own language. The result was C#, designed by a remarkably small team of six experienced language designers meeting for two hours, three times a week. Hejlsberg believes small, experienced teams consistently outperform larger ones for language design—a principle that resonates with current industry trends toward smaller AI-augmented teams.

The technical discussion covers several pivotal innovations. Async/await, which spread from C# to Python, JavaScript, Rust, and beyond, succeeded because it lets compilers handle the state machine generation that developers find tedious and error-prone. TypeScript's origin story is particularly revealing: the Outlook.com team wanted to cross-compile C# to JavaScript via "Script#," but Hejlsberg pushed back, insisting that fixing JavaScript itself—by adding types—was the better approach. He also credits TypeScript's success to "open development" on GitHub starting in 2014, where community engagement transformed the project. The TypeScript compiler itself breaks conventions: it uses lazy evaluation, deferred imports, and maintains cached ASTs for 499 of 500 files, only rebuilding the one being edited.

On AI, Hejlsberg offers pragmatic observations. AI's effectiveness with a language depends primarily on the volume of that language in training data—explaining why TypeScript and Python excel—rather than on language design features. AI remains limited for compiler writing because LLM training sets contain relatively little compiler-specific content. His most striking prediction: developers will become "project managers" overseeing "armies of junior programmers"—AI agents generating reams of code. He admits personal disinterest in reviewing code but sees potential for AI-generated commentary that guides reviewers through changes. His closing wisdom on language design: it's a 10-year play, requiring at least three versions before a language truly shines and adoption follows.
