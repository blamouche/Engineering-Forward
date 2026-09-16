# Mini-Vibe Check: TypeSafe's Jev Judged Everything I've Written in 0.7 Seconds
**Source**: Every (hello@every.to)
**Date**: 2026-09-15
**Author**: Mike Taylor (Every)
**Keywords**: TypeSafe, Jev, probability model, structured outputs, RLCD, evals, classification, AI agents

## Elevator pitch
TypeSafe, a new AI lab, launched Jev — a model that answers fuzzy questions with probabilities rather than prose, enabling software to act on the results directly. It's not a chatbot; it's a structured-output engine designed for the workflow automation layer where speed and cost matter more than eloquence. Mike Taylor tested it across 11 experiments and found it could make 1,709 judgments for less than a cent, turning the prospect of checking an AI agent's work mid-task from a luxury into a trivial routine.

## Takeaways
- Jev returns probabilities (0–1) for yes/no questions or custom categories, letting code branch on structured answers without parsing natural language
- TypeSafe's cofounder Diogo Almeida coauthored the 2022 InstructGPT paper at OpenAI; the training approach is called Reinforcement Learning for Calibrated Decisions (RLCD)
- The model's confidence is designed to match its accuracy: if it flags 100 items at 90%, roughly 90 should be correct
- Priced at $42 per billion tokens (not per million like most LLMs), with output tokens "too cheap to meter"
- Can answer multiple questions in parallel in fractions of a second; processed 37 documents × 21 questions = 777 judgments in 0.7 seconds for ~$0.0025
- CEO Dan Shipper tested Jev vs Fable 5.1: Jev was 25× faster (0.35s vs 8.83s median) and ~580× cheaper, catching 6 of 7 defects vs Fable's 7 of 7
- Use cases span finding context, checking work, and making decisions — from grading support replies to sorting startup pitches to prioritizing customer queues
- Could act as a "code linter for knowledge work" — flagging problems in AI-generated output as it's being produced

## Synthesis
Mike Taylor's hands-on review of TypeSafe's Jev model makes a compelling case for a new category of AI model that isn't trying to be a better chatbot. Jev is built for the workflow automation layer — the if-then decisions that route customer requests, classify transactions, or check whether an agent's output meets your standards. The key insight is that most LLMs waste tokens generating prose when the application just needs a number.

The RLCD training approach is designed so the model's confidence scores are calibrated: a 0.9 answer means roughly 90% probability of being correct. This is fundamentally different from coaxing a chatbot to output JSON via frameworks like DSPy — Jev natively produces structured answers that code can act on directly. The System One architecture allows parallel question answering without token-by-token generation, explaining the dramatic speed advantage.

Taylor's 11 experiments — from AI-writing detection to customer prioritization to simulated ad-click prediction — demonstrate the model's versatility. The most compelling vision is using Jev as a real-time quality checker: give Codex or Claude access to Jev and a list of checks, and it can flag problems in AI-generated work as it's being produced, rather than waiting for a post-hoc review. At a quarter-cent per 777 judgments, running checks multiple times during a task becomes economically trivial.

The caveat is accuracy: Jev caught 6 of 7 deliberately introduced defects vs Fable 5.1's perfect 7 of 7. Taylor acknowledges the need for more thorough accuracy validation before production deployment. But as an early warning system — "the alternative is not checking at all" — the speed/cost profile makes it a practical new tool in the AI builder's toolkit.