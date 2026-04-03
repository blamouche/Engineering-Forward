# How Roblox Uses AI to Translate 16 Languages in 100 Milliseconds
**Source**: https://blog.bytebytego.com/p/how-roblox-uses-ai-to-translate-16
**Date**: March 30, 2026
**Author**: ByteByteGo
**Keywords**: translation, NLP, Mixture of Experts, knowledge distillation, real-time ML, Roblox, multilingual

## Elevator pitch
Roblox built a single Mixture-of-Experts translation model serving 16 languages with 100ms latency at 5,000 chats/second, using knowledge distillation, quantization, cross-language caching, and dynamic batching.

## Takeaways
- Single MoE model handles all 16 languages (256 language pairs) rather than 256 separate models
- Knowledge distillation reduced from ~1B to <650M parameters; further compressed via quantization and compilation
- Dynamic batching + embedding cache between encoder and decoder prevents redundant computation for multi-language translations
- Custom quality estimation model scores translations without reference translations, evaluating accuracy, fluency, and context
- Back-translation synthesized training data for low-resource language pairs like French-Thai

## Synthesis
Roblox's translation system illustrates the engineering tradeoffs inherent in real-time machine learning at scale. The 100ms latency ceiling is not arbitrary — it represents the threshold above which translation latency becomes perceptible to users in live chat, breaking the conversational experience. Every architectural decision in the system flows from this constraint.

The choice of a single Mixture-of-Experts model over 256 language-pair models is the most consequential architectural decision. Individual language-pair models could theoretically achieve higher per-pair quality, but they create operational complexity that scales with the number of languages. Routing requests to the right model, managing 256 model lifecycles, coordinating updates — the overhead is substantial. The MoE approach elegantly sidesteps this by routing internally: a single model with specialized subnetworks that activate per-language pair keeps the operational surface manageable while still maintaining differentiated quality per language.

Knowledge distillation from 1B to under 650M parameters deserves emphasis. The distillation process trains a smaller student model to replicate the behavior of a larger teacher model, enabling a size reduction that would not be achievable through architectural simplification alone. Combined with quantization and compilation, the resulting model is substantially smaller and faster than what quality requirements alone would dictate, enabling the 100ms constraint to be met.

The embedding cache between encoder and decoder is an infrastructure-level optimization with significant impact. When one message needs to be translated into multiple languages simultaneously — which is the norm in a multilingual game chat environment — the encoder processes the source text once and the resulting representation is cached. All target language translations reuse this cached representation, avoiding redundant encoder computation. The savings compound at Roblox's scale: 5,000 chats per second, potentially each requiring multiple translations, means the encoder savings add up quickly.

The quality estimation model, operating without reference translations, solves a practical challenge in low-resource language pair evaluation. For high-resource pairs, reference translations from human translators are available. For the long tail of language combinations, they are not. A model that can assess translation quality from source text and output alone provides coverage across all 256 directions without requiring human translation resources proportional to the pair count.
