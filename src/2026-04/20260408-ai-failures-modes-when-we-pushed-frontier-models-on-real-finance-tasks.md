# AI failures modes when we pushed frontier models on real finance tasks

**Source**: https://www.mercor.com/blog/Finance-tasks-ai-failures-modes
**Date**: 2026
**Author**: Mercor
**Keywords**: finance, multimodal reasoning, document extraction, visual QA, benchmarking

## Elevator pitch
Mercor tested frontier models on realistic finance documents and found the main bottleneck is not arithmetic but extracting the right numbers from messy charts, tables, and investor decks.

## Takeaways
- Image-based finance tasks materially underperform the same tasks when the numbers are provided as text.
- The biggest weakness is visual extraction from dense real-world documents, not pure calculation.
- Models also make surprisingly basic operation mistakes even when the relevant values are available.
- The benchmark design is interesting because it separates reading failures from reasoning failures.
- The article is a useful antidote to overgeneralizing from clean chart or DocVQA benchmarks.

## Synthesis
This is one of the more practical benchmarking write-ups because it isolates where the failure actually occurs. Lots of business workflows look “reasoning-heavy” from a distance, but the first challenge is often just reading the source artifact correctly. In finance that means crowded slides, multi-panel charts, ambiguous labels, and presentation layouts designed for humans, not models. Mercor shows that when you strip away the messy visual layer, model performance becomes much more respectable. So the blocker to analyst replacement is currently more “robust document ingestion in the wild” than “basic financial math.” That distinction matters for product builders: better OCR-plus-structure pipelines may unlock more value faster than trying to fine-tune ever more domain reasoning.
