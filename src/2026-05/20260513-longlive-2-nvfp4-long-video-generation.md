# LongLive 2.0: An NVFP4 Parallel Infrastructure for Long Video Generation
**Source**: https://github.com/NVlabs/LongLive
**Date**: May 13, 2026
**Author**: NVIDIA Research (NVlabs)
**Keywords**: LongLive, video generation, NVFP4, NVIDIA, sequence parallelism, AR training, inference optimization, ICLR 2026

## Elevator pitch
NVIDIA releases LongLive 2.0, an infrastructure for training and running long video generation models that uses NVFP4 quantization and sequence parallelism to achieve up to 45.7 FPS at 5B parameters — accepted at ICLR 2026.

## Takeaways
- LongLive 2.0 is an infrastructure play, not just a model: it supports NVFP4 (4-bit floating point) for both training (AR teacher-forcing) and inference, plus few-step DMD distillation.
- The 5B parameter NVFP4-quantized model achieves 45.7 FPS at 2-step inference, with performance staying competitive (VBench 83.14 vs 85.06 for BF16) — a 1.8x speed jump from the 24.8 FPS BF16 baseline.
- Key architectural innovations include balanced sequence parallelism, multi-shot attention sink, KV-cache relative RoPE for infinite-length videos, and async decoding.
- The original LongLive 1.0 pioneered real-time interactive long video generation with sequential user prompts; 2.0 adds multi-shot training and NVFP4 quantization.
- The 1.3B model delivers 20.7 FPS with 84.87 VBench, while the 5B BF16 model hits 24.8 FPS and 85.06 — establishing a clear efficiency-quality trade-off curve.
- LongLive also integrates with SANA-Video for 60-second real-time interactive video generation using linear attention.

## Synthesis
LongLive 2.0 is NVIDIA flexing its full-stack advantage: custom hardware (NVFP4), systems expertise (sequence parallelism, async decoding), and model research (AR training, distillation) combined into a single release. The headline is 45.7 FPS at 5B parameters with 4-bit quantization — numbers that would have been absurd for long video generation even a year ago.

The infrastructure-first framing is deliberate. This isn't just a model; it's a training and inference pipeline that supports both BF16 and NVFP4 backends with a unified API. The four model variants form a clear quality-speed trade-off curve: from the original 1.3B model at 20.7 FPS and 84.87 VBench, up through 5B BF16 (24.8 FPS, 85.06), to NVFP4 4-step (29.7 FPS, 84.51) and NVFP4 2-step (45.7 FPS, 83.14). Each step along the curve sacrifices ~0.5-1.4 VBench points for substantial speed gains — a pragmatic trade-off for real-time applications.

The technical innovations are worth noting beyond the quantization. Balanced sequence parallelism enables distributed AR training across GPUs. Multi-shot attention sink allows the model to process multiple video clips with shared context. KV-cache relative RoPE, introduced in January 2026, enables theoretically infinite video length by making positional encodings relative rather than absolute. The integration with SANA-Video's linear attention models shows the infrastructure is architecture-agnostic.

ICLR 2026 acceptance validates the research contribution, but the practical impact is in the open-source release: weights, training code, inference code, and documentation all public. This follows NVIDIA's pattern of releasing infrastructure that makes their hardware ecosystem more valuable — NVFP4 only runs on NVIDIA GPUs, after all — while genuinely advancing the state of the art.
