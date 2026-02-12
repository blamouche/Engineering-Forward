# On-Device LLMs: State of the Union, 2026

**Source**: https://v-chandra.github.io/on-device-llms/

**Date**: January 24, 2026

**Author**: Vikas Chandra, Raghuraman Krishnamoorthi (AI Research @ Meta)

**Keywords**: on-device LLM, edge AI, quantization, mobile AI, inference optimization, ExecuTorch, privacy, latency

## Elevator pitch

On-device language models have evolved from toy demos to production systems running billion-parameter models on smartphones, enabled not by hardware improvements alone but by fundamental rethinking of model architecture, compression, and deployment strategies.

## Takeaways

- Memory bandwidth, not compute, is the primary bottleneck for on-device inference; mobile devices have 30-50x less bandwidth than data center GPUs
- 4-bit quantization has become the production standard, achieving 4x memory reduction with only 1-3% quality loss through techniques like AWQ and GPTQ
- Sub-1B parameter models trained on curated data can match 3B models trained on web scrapes, proving architecture matters more than size at small scale
- ExecuTorch 1.0 from Meta now deploys across Instagram, WhatsApp, and Messenger serving billions with a 50KB runtime footprint
- Speculative decoding achieves 2.2-3.6x speedup by having smaller draft models propose multiple tokens verified in parallel

## Synthesis

Meta's AI Research team has published a comprehensive analysis documenting how on-device language model deployment has transformed over three years from experimental demonstrations to production systems running efficiently on flagship smartphones. The paper challenges conventional assumptions about what constitutes viable on-device AI and provides practical frameworks for implementation.

Four drivers justify the shift to on-device inference: latency reduction from 200-500ms cloud roundtrips to sub-20ms token generation, privacy guarantees through exclusive on-device data retention, improved unit economics by shifting inference costs to amortized device hardware, and reliability independence from network connectivity. The tradeoff remains that frontier reasoning, extensive world knowledge, and prolonged multi-turn conversations still favor cloud deployment.

The central technical insight is that memory bandwidth, not compute capacity, constrains on-device performance. Contemporary mobile NPUs deliver impressive throughput: Apple A19 Pro at 35 TOPS, Qualcomm Snapdragon 8 Elite at 60 TOPS. However, mobile devices offer only 50-90 GB/s memory bandwidth compared to 2-3 TB/s in data center GPUs, a 30-50x gap. Since decoding is memory-bound, quantization from 16-bit to 4-bit provides not just 4x less storage but 4x less memory traffic per token.

Conventional scaling laws proved incorrect at small scale. Sub-billion parameter models can be effective when architecture is optimized. Deep-thin architectures with more layers and smaller hidden dimensions outperform wide-shallow alternatives. A 125M parameter model runs at 50 tokens per second on iPhone and handles basic tasks well. Key efficient models include Llama 3.2 at 1B/3B variants, Gemma 3 spanning 270M to 27B, and SmolLM2 from 135M to 1.7B trained on 11 trillion tokens.

Quantization has evolved into a layered hierarchy. 4-bit post-training quantization through GPTQ and AWQ has become the production standard, with AWQ surpassing 19 million HuggingFace downloads. Outlier-aware techniques like SmoothQuant and SpinQuant achieve 4-bit weights and activations with under 3% accuracy loss. Sub-4-bit approaches including BitNet at 1.58-bit enable 2B models to fit in 400MB. The paper provides clear guidance: 8-bit for unconstrained servers, 4-bit for server/mobile/edge with 1-3% quality drop, and sub-4-bit for aggressive mobile optimization.

Production deployment has matured substantially. ExecuTorch 1.0, released by Meta in October 2025, provides a 50KB runtime footprint supporting 12+ hardware backends across Apple, Qualcomm, Arm, and MediaTek. Over 80% of popular HuggingFace edge LLMs work out-of-box, and the framework is deployed across Instagram, WhatsApp, and Messenger serving billions of users. For practitioners, the recommended workflow is to validate use cases with quantized models in llama.cpp, profile on real hardware early since emulators prove inaccurate, then transition to ExecuTorch for production deployment.
