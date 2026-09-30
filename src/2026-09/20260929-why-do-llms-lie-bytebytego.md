# Why Do LLMs Lie?
**Source**: ByteByteGo (bytebytego@substack.com)
**Date**: 2026-09-29
**Author**: ByteByteGo
**Keywords**: LLM hallucination, factual hallucination, faithfulness hallucination, fabrication, RAG, tools, grounding, uncertainty, verification, Sentry Agent Tracing

## Elevator pitch
ByteByteGo systematically breaks down why LLMs hallucinate — distinguishing factual, faithfulness, and fabrication errors — and surveys the mitigation techniques from RAG and tool use to output verification, explaining why an explanation is not proof and how to catch errors before they reach the user.

## Takeaways
- Hallucination in LLMs is generated information that is factually incorrect, invented, or inconsistent with source material — it resembles a confident falsehood but without the intention to deceive that defines "lying"
- Three categories of error: factual hallucination (contradicts reality — e.g., saying refund window is 30 days when it's 14), faithfulness hallucination (contradicts supplied evidence), and fabrication (invents policy sections, confirmation numbers, or citations)
- The categories overlap: a fabricated policy section can be both factually false and unsupported by documents
- An AI assistant can faithfully summarise an outdated document and still give an incorrect answer about current policy — faithfulness and factuality are different failure modes
- LLMs hallucinate because text prediction produces invented facts: the model generates the most plausible-sounding next token, not the most accurate one, and admits uncertainty poorly because training data rewards confident-sounding answers
- RAG (Retrieval-Augmented Generation) gives the model evidence to ground responses, but only helps if the retrieved context is relevant and the model actually uses it rather than overriding it with parametric knowledge
- Tool use lets models look up missing facts rather than guessing, shifting from "generate an answer" to "find and report the answer"
- An explanation is not proof: a model can produce a plausible-sounding chain of reasoning that justifies a wrong answer — verification must be independent of the generation process
- Output verification — checking the answer against source material before it reaches the user — is the last line of defence, and tools like Sentry Agent Tracing can instrument agent workflows to catch bad tool calls and unexpected output

## Synthesis
The taxonomy of factual, faithfulness, and fabrication errors is the most useful framework here because it maps directly to different mitigation strategies. Factual errors require external grounding (RAG, tools, fact-checking). Faithfulness errors require source-comparison (does the answer match the retrieved context?). Fabrication requires provenance verification (does the cited document actually exist?). Conflating these leads to misplaced confidence: a RAG system that faithfully summarises an outdated document has zero hallucination by the faithfulness measure and 100% by the factuality measure.

The insight that an explanation is not proof is underappreciated. Chain-of-thought reasoning makes models more useful and more trustworthy-feeling, but a well-constructed rationale for a wrong answer is worse than no rationale at all — it makes the error harder to catch. The implication for agent architecture is clear: verification must be structurally separate from generation, using different evidence or a different model, because a model that generated a wrong answer will tend to justify it consistently when asked to verify it. This is why tools like Sentry Agent Tracing matter — they externalise the verification to a system that doesn't share the model's bias.