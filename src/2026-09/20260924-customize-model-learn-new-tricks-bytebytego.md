# How to Customize a Model to Learn New Tricks
**Source**: ByteByteGo (bytebytego@substack.com)
**Date**: 2026-09-24
**Author**: ByteByteGo
**Keywords**: fine-tuning, LoRA, QLoRA, RAG, prompting, supervised fine-tuning, RLHF, parameter-efficient fine-tuning, quantization, adapters, overfitting, gradient accumulation

## Elevator pitch
ByteByteGo's comprehensive guide to model customization walks through the full spectrum from prompting and RAG to supervised fine-tuning and parameter-efficient techniques (LoRA, QLoRA), explaining how adapters learn compact adjustments while keeping base weights frozen, how quantization reduces memory for larger models, and the practical training process from baseline to evaluation.

## Takeaways
- **The customization ladder**: Prompting → few-shot → RAG → fine-tuning. Each step adds capability but also cost and complexity. Prompting and RAG work through information supplied during a request without changing model parameters.
- **Fine-tuning changes the model itself**: Supervised fine-tuning (SFT) trains on input-response pairs so desired behavior becomes part of the model's default, persisting across future requests without re-including training data.
- **LoRA learns a smaller set of changes**: Low-Rank Adaptation keeps original weights frozen and attaches small trainable adapters implemented as two compact matrices. The first creates a compact intermediate representation; the second produces an adjustment added to the original result. Rank (8, 16, 32, 64) controls adapter capacity.
- **QLoRA reduces the frozen model's memory**: Quantized LoRA stores base weights in 4-bit form while keeping adapters at higher precision (16-bit or 32-bit). This makes it possible to customize a larger model within a fixed memory budget.
- **Storage vs. computation distinction**: A weight can be stored compactly and reconstructed at higher precision for calculation. This creates an approximation but doesn't recover detail discarded during quantization.
- **Training process essentials**: Choose a suitable starting model, establish a prompt-based baseline, prepare train/validation/test sets (no leakage), configure rank/learning rate/batch size, watch for overfitting (validation performance worsening while training improves).
- **Memory-saving techniques**: Gradient accumulation (several smaller batches contribute to one update), gradient checkpointing (fewer intermediate results, recreated when needed).
- **Adapter deployment**: Keep adapters separate for multiple specializations on one base model, or merge into base weights for a standalone customized model (loses storage advantage).

## Synthesis
ByteByteGo's article is the kind of foundational technical explainer that the AI engineering community relies on — clear, structured, and grounded in actual practice rather than hype. The progression from prompting through RAG to fine-tuning is presented as a ladder of escalating intervention, which is the right mental model: you don't fine-tune when a prompt will do, and you don't LoRA when RAG suffices.

The LoRA and QLoRA explanations are particularly well-constructed. The insight that "the model already has a pretty good grasp on language" — so adaptation doesn't require adjusting every parameter independently — is the theoretical justification for parameter-efficient fine-tuning. The "low rank" concept (shared patterns in adjustments, represented through limited coordinated patterns) is explained without requiring linear algebra background.

The practical guidance on training process — baseline first, clean datasets, watch for overfitting, evaluate the actual task not just output quality — reflects hard-won experience. The warning that "an adapter can improve one behavior while weakening another, even though the original weights remain frozen" is a subtle but critical point that practitioners often learn the hard way. The combined model's behavior has changed, so it must be evaluated as a whole, not just on the fine-tuned task.