# How to Shrink a Language Model Without Making it Too Dumb
**Source**: https://blog.bytebytego.com/p/how-to-shrink-a-language-model-without-295
**Date**: 2026-09-01
**Author**: Alex Xu (ByteByteGo)
**Keywords**: LLM, model compression, quantization, pruning, knowledge distillation, model size, inference, FP32, BF16, INT4, consumer hardware

## Elevator pitch
A detailed explainer of three techniques — quantization, pruning, and knowledge distillation — that make large language models small enough to run on consumer hardware without significantly degrading their intelligence, and how these techniques can be stacked.

## Takeaways
- A 70B parameter model takes ~140 GB of storage, but a good GPU has only 24 GB — the gap has grown 100x in a few years while consumer memory has only doubled
- Quantization stores each weight in fewer bits (e.g., 4-bit instead of 16-bit), using block-level scale factors to reconstruct approximate values
- Pruning deletes weights that contribute least — either by setting small weights to zero or removing entire neurons/attention heads/layers
- Knowledge distillation trains a smaller "student" model to mimic a larger "teacher" model's full output distribution, not just the correct answer
- All three techniques can be stacked: distill at the lab, prune in research, quantize on the user's machine
- 32-bit to 8-bit quantization causes almost no noticeable intelligence loss; pushing to 4-bit or lower can have significant impact
- Pruning idle pathways is safe; aggressive pruning of deeper pathways degrades multi-step logic
- Distilled student models can mimic teacher style but may fail on completely novel problems the teacher didn't cover

## Synthesis
ByteByteGo's article addresses one of the most practical challenges in AI deployment: the gap between model sizes and available hardware. A 70 billion parameter model requires ~140 GB of storage (2 bytes per weight × 70B), while a good consumer GPU has only 24 GB. Models have grown roughly 100-fold in a few years, but consumer graphics memory has only doubled. The article explains three complementary techniques to bridge this gap.

Quantization reduces the precision of each weight. During training, weights are stored as 32-bit floats (FP32); at distribution, they're typically reduced to 16-bit (FP16/BF16). The article walks through the process of further reducing to 4-bit integers: mapping the range of a small block of weights to integers from -7 to 7, rounding each weight to the nearest step, and storing a single scale factor per block. Going from 32-bit to 8-bit causes almost no noticeable intelligence loss, but pushing to 4-bit or lower can significantly impact the model's ability to handle nuance.

Pruning takes the opposite approach — instead of using fewer bits per weight, it deletes weights entirely. Most weights have values close to zero and barely impact output. The simplest approach sorts by magnitude and deletes the smallest; a better method runs sample texts through the model and scores each weight's actual contribution. Structural pruning (removing entire neurons or heads) shrinks matrices more effectively but causes more collateral damage than simply zeroing out individual weights.

Knowledge distillation creates a new, smaller "student" model trained to mimic the "teacher" model's behavior. Critically, the student learns from the teacher's full probability distribution over the vocabulary — not just the correct answer, but also which alternatives were plausible and which were absurd. This richer signal helps the student learn faster than ordinary training. The student can perfectly mimic the teacher's style but may fail on novel problems the teacher didn't explicitly demonstrate.

The key insight is that these techniques stack: a model can be distilled at the lab, pruned by a research team, and quantized by the end user before loading — making it possible to run high-end LLMs on normal consumer hardware.