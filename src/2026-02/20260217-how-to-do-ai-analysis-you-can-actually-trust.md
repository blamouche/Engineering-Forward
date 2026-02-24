# How to do AI analysis you can actually trust
**Source**: https://www.lennysnewsletter.com/p/how-to-do-ai-analysis-you-can-actually
**Date**: 2026-02-17
**Author**: Caitlin Sullivan
**Keywords**: ai, user research, analysis

## Elevator pitch
Caitlin Sullivan outlines four common failure modes in AI-assisted customer research and the prompting techniques that make analysis verifiable and decision‑ready.

## Takeaways
- AI analysis often hallucinates evidence and overconfidently cherry‑picks quotes.
- Generic theme clustering hides important edge cases and decision‑critical nuance.
- Context loading must be structured (project, goal, product, participant) to guide interpretation.
- Verification and quote‑selection rules force traceable evidence.
- Reliable insights require checks for contradictions and decision relevance.

## Synthesis
This guest post by user‑research expert Caitlin Sullivan tackles a recurring problem: AI output looks confident even when it is wrong. In customer research, that manifests as invented quotes, false conclusions, and overly tidy themes that can mislead teams into major product bets. Sullivan argues that the mistakes are easy to miss until a stakeholder questions the evidence or a decision collapses months later. Her goal is to make AI‑assisted analysis trustworthy and decision‑ready by identifying failure modes and applying specific prompting techniques to counter them.

She highlights four failure modes that quietly distort AI analysis. The first is invented evidence, where the model fabricates quotes or attributes statements that are not in the data. The second is false or generic insights, where the model compresses answers into bland themes that do not inform real decisions. The third is “signal” that does not guide action—patterns that sound analytical but do not help teams decide what to build. The fourth is contradictory insights, where models miss tensions in user feedback and flatten conflicting signals into a single story. These failures are particularly damaging because they produce persuasive narratives that can pass a casual review.

A key part of her fix is verification. She recommends quote‑selection rules and explicit checks so that models must anchor claims to direct evidence. The goal is to force traceability: if an insight cannot be tied to specific quotes or timestamps, it should not be used. This is especially important in qualitative data, where the temptation to summarize away nuance is high.

Another technique is structured context loading. Sullivan argues that many prompts either include too little context or dump excessive background without framing. Effective context should include at least four elements: project context (the concrete decision and constraints), business goal (what the analysis is meant to decide), product context (domain knowledge that shapes interpretation), and participant overview (who is speaking and why that matters). Without this, AI defaults to generic analysis or applies priors from its training data.

She illustrates the difference between weak and strong analysis with a comparison: a poor output cherry‑picks enthusiastic quotes to recommend a feature, while a strong output challenges the premise, segments users by need, and flags risks with evidence. The better analysis is messier but grounded in real data and explicit uncertainty.

The broader message is that AI can be useful for customer research, but only if prompts and workflows enforce evidence, context, and decision‑relevance. Models are pattern‑finders that optimize for consensus and compression; useful analysis often lives in edge cases, contradictions, and precise framing. By enforcing verification, improving context, and checking for actionable signal, teams can turn AI from a fast summarizer into a reliable research assistant.
