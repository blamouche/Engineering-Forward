# An AI State of the Union: We've Passed the Inflection Point, Dark Factories Are Coming

**Source**: https://www.lennysnewsletter.com/p/an-ai-state-of-the-union
**Date**: Unknown
**Author**: Simon Willison (Lenny's Newsletter interview)
**Keywords**: AI coding, agentic engineering, Claude Code, prompt injection, dark factory, mid-career engineers, Simon Willison

## Elevator pitch
Simon Willison argues that November 2025 was the true inflection point where AI coding agents crossed from "mostly works" to "actually works," and maps out the agentic engineering patterns and risks that define the new era.

## Takeaways
- November 2025 (GPT-5.2 and Opus 4.5) was the inflection point where AI coding agents became reliably capable—Simon now writes 95% of his code from his phone
- Three key agentic engineering patterns: red/green TDD (write failing tests first, let the agent make them pass), templates (hoard working examples), and the compound engineering loop
- Mid-career engineers (not juniors) face the most risk—they're expensive, their specific skills are being automated, and companies know exactly what tasks they do
- The "dark factory" pattern represents the next leap: no code writing or review by humans, AI does its own QA in fully automated pipelines
- Prompt injection remains a critical unsolved security problem—the "lethal trifecta" of autonomous agents, untrusted inputs, and consequential actions is likely to cause a major incident

## Synthesis
Simon Willison has an unusual vantage point on the AI transformation of software engineering: he co-created Django, coined the term "prompt injection," coined "agentic engineering," and has built over 100 open source projects. More importantly, he made the transition to AI-native development more fully and publicly than almost anyone else, documenting everything in real time on his blog.

His core claim is that November 2025 represented a genuine inflection point—not incremental improvement, but a phase transition. GPT-5.2 and Claude Opus 4.5 crossed some threshold where AI coding agents moved from "mostly works, sometimes" to "actually works, reliably." The evidence: Simon now writes 95% of his code from his phone using voice and text, and is mentally exhausted by 11 AM because he's directing agents all morning rather than writing code manually.

The agentic engineering patterns he's developed represent practical wisdom from this transition. Red/green TDD is perhaps the most powerful: write failing tests first, then tell the agent to make them pass. This gives the agent a clear, verifiable success criterion and catches regressions automatically. Templates and hoarding—maintaining a library of working examples and prompt patterns—makes agent delegation dramatically more reliable because you're recombining proven approaches rather than starting from scratch each time.

The "dark factory" concept frames what comes next: fully automated software development pipelines where no human writes or reviews code, and AI systems do their own QA. This isn't speculative—it's a direction visible from current trends where the human role is shifting from implementation to direction and verification.

Willison's analysis of workforce impact cuts against a common assumption. It's not junior engineers who face the most immediate risk—they're cheap and adaptable. It's mid-career engineers who are expensive, perform well-defined tasks that can be enumerated, and whose specific skills are being automated. Companies know exactly what their senior engineers do; that makes automation targeting cleaner.

The prompt injection warning is the most urgent near-term concern. As AI agents gain access to external tools, email, web browsing, and consequential actions, the attack surface for prompt injection expands dramatically. Malicious content in the environment can redirect agent behavior. The "lethal trifecta"—autonomous agents, untrusted inputs, consequential actions—creates conditions for catastrophic failures. Willison predicts this will produce an incident comparable in impact to the Challenger disaster: a visible, high-profile failure that resets expectations about agent deployment in sensitive contexts.

For engineering leaders: the patterns Willison describes are available to implement today. The risk awareness about prompt injection should shape how you deploy agents. And the workforce implications deserve honest conversation rather than reassuring platitudes.
