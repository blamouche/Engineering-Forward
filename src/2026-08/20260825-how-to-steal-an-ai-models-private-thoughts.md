# How to Steal an AI Model's Private Thoughts
**Source**: https://blog.bytebytego.com/p/how-to-steal-an-ai-models-private
**Date**: 2026-08-25
**Author**: ByteByteGo
**Keywords**: AI security, reasoning traces, model privacy, encrypted reasoning, extraction attack

## Elevator pitch
Researchers demonstrated that encrypted reasoning blocks from frontier AI models can be replayed into cheaper models in the same family to extract hidden reasoning traces in plaintext, exposing proprietary chain-of-thought that providers deliberately withhold.

## Takeaways
- Frontier models produce three outputs: a visible answer, a summary labeled "thinking," and a full reasoning trace that providers encrypt and withhold from users
- Researchers from MATS Research, ELLIS Institute Tübingen, and Max Planck Institute showed that encrypted reasoning blocks can be replayed into a cheaper model in the same family to print the hidden reasoning in plaintext
- The attack exploits three forms of compatibility: the cheaper model accepts the encrypted block, decrypts it using shared family parameters, and uses it as a prefix to continue generating text that reveals the original reasoning
- Four attack vectors were identified, and a scan of published session logs found real-world cases where encrypted reasoning was inadvertently exposed
- Proposed fixes include not sharing encrypted reasoning at all, or using client-side encryption keys, but a fundamental limit remains: the client must be able to read the reasoning to display the summary, which creates an inherent extraction surface

## Synthesis
When a frontier AI model handles a complex question, it generates three distinct pieces of text: the answer displayed to the user, a shorter "thinking" or "reasoning" summary shown while the answer is assembled, and a full internal reasoning process that is never displayed. The visible summary is generated separately from the full reasoning and serves as a compressed stand-in. Most major providers—including Anthropic, OpenAI, and Google—deliberately withhold the complete reasoning trace from users, sharing only the summary and an encrypted version of the full reasoning.

In August 2026, a research team from MATS Research, the ELLIS Institute Tübingen, and the Max Planck Institute for Intelligent Systems tested whether those encrypted reasoning blocks actually keep the reasoning private. They demonstrated that the encrypted blocks can be replayed into a cheaper model within the same model family, which then prints the hidden reasoning in plaintext. The attack exploits three forms of compatibility that exist between models in the same family: the cheaper model accepts the encrypted block as valid input, decrypts it using shared family-level parameters, and treats the decrypted content as a reasoning prefix that it continues to generate from, effectively reproducing the original model's private thoughts.

The researchers identified four specific attack vectors and scanned published session logs to find real-world cases where encrypted reasoning had been inadvertently exposed. This is significant because providers withhold reasoning traces for competitive and safety reasons: the traces reveal problem-solving strategies, could enable distillation of model capabilities into competitors, and may contain information about how models circumvent safety guardrails.

The proposed fixes are limited. Providers could stop sharing encrypted reasoning entirely, but this creates a storage problem: the full reasoning must be retained server-side for audit and debugging purposes. Alternatively, client-side encryption keys could prevent cross-model replay, but the client must still be able to decrypt the reasoning to display the summary—creating an inherent surface for extraction. The finding suggests that current approaches to reasoning privacy in frontier AI models are fundamentally fragile, and that the assumption of confidentiality for model reasoning traces may not hold against determined adversaries.