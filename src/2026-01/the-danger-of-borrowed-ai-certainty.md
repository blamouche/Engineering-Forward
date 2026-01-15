# The Danger of Borrowed AI Certainty

**Source**: https://russmiles.substack.com/p/the-danger-of-borrowed-ai-certainty

**Date**: January 13, 2026

**Author**: Russ Miles

**Keywords**: AI coding, software engineering, critical thinking, AI tools, developer practices, technical debt, engineering judgment

## Elevator pitch

Teams adopting AI-generated solutions without genuine understanding are accumulating "borrowed certainty"—code that compiles and passes tests but fails in strange ways because the underlying understanding was never earned.

## Takeaways

- AI produces fluent, plausible outputs without grounding in reality, execution, or consequence—it predicts statistically what sounds right, not what is correct
- Developers are particularly vulnerable because they're trained to trust systems that compile and tests that pass, leading them to mistake fluency for validity
- Borrowed certainty conflates three distinct concepts: evidence (logs, metrics, tests), proof (formal guarantees, types), and belief (engineering judgment informed by evidence)
- Code written with unearned certainty passes review and deploys cleanly, then fails in production because nobody truly understood what was built
- The critical safeguard question: "Could I defend this decision without the AI present?"—if not, understanding has been borrowed rather than earned

## Synthesis

Russ Miles presents a nuanced critique of AI-assisted software development that avoids both naive enthusiasm and reflexive skepticism. His central concept—"borrowed certainty"—names a phenomenon that many developers have likely experienced but struggled to articulate: the unsettling feeling of deploying code you don't fully understand because an AI tool made it seem authoritative.

Miles is careful to acknowledge AI's legitimate benefits. These tools excel at accelerating recall, reducing cognitive load on repetitive tasks, and drafting boilerplate code. The problem isn't using AI—it's using AI as a substitute for understanding rather than an accelerant for it. When developers adopt AI-generated solutions wholesale, they're not learning or building mental models. They're borrowing confidence from a system that has none to lend.

The technical insight at the heart of Miles's argument is worth emphasizing: AI doesn't reason, it predicts. Large language models generate text that statistically resembles what a knowledgeable human might say, but this resemblance is superficial. The model has no understanding of whether the code will work, no model of the runtime environment, no appreciation of edge cases. It produces outputs that sound right based on patterns in training data. When those patterns align with reality, the results are useful. When they don't, the failure modes can be subtle and strange.

This creates a particular vulnerability for software developers. The profession trains practitioners to trust certain signals: code that compiles, tests that pass, reviews that approve. These heuristics generally work because they correlate with quality when humans are writing code with understanding. But AI-generated code can pass all these gates while remaining fundamentally unsound because the human responsible never developed genuine comprehension.

Miles identifies a critical confusion underlying this problem: the conflation of evidence, proof, and belief. Evidence consists of empirical observations—logs, metrics, test results. Proof involves formal guarantees—type systems, mathematical verification. Belief represents engineering judgment informed by evidence and experience. When developers accept AI outputs as authoritative, they often treat them as proof when they're really just plausible-sounding assertions that haven't been validated by either evidence or formal analysis.

The practical consequence is code that "fails in strange ways." These aren't the obvious bugs caught in testing. They're the subtle behavioral issues that emerge in production under unusual conditions—precisely the scenarios that require deep understanding to anticipate and address. When failures occur, teams cannot explain their decisions beyond "the AI recommended it," leaving them unable to debug effectively or prevent recurrence.

Miles's proposed safeguard is elegantly simple: before accepting any AI-generated solution, ask whether you could defend the decision without the AI present. If the answer is no, you haven't learned—you've borrowed. And borrowed certainty, like borrowed money, eventually comes due with interest.
