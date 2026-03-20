# Spatial-TTT: Streaming Visual-based Spatial Intelligence with Test-Time Training
**Source**: https://github.com/THU-SI/Spatial-TTT
**Date**: 2026-03-13
**Author**: Fangfu Liu et al. (Tsinghua University, Tencent Hunyuan, NTU)
**Keywords**: spatial intelligence, test-time training, video understanding, 3D reasoning, transformer, TTT layers, VSI-Bench

## Elevator pitch
Spatial-TTT enables AI models to stream and continuously update 3D spatial understanding from unbounded video by combining Test-Time Training layers with self-attention, accumulating spatial evidence as compact adaptive memory.

## Takeaways
- Processes potentially unbounded video streams, updating spatial evidence continuously rather than requiring bounded input
- Hybrid architecture interleaves TTT (Test-Time Training) layers with self-attention, balancing knowledge preservation and spatial compression
- Adaptive fast weights update online as compact nonlinear memory for 3D evidence accumulation
- Includes Spatial-TTT-Data-97k: ~97K training samples for dense scene description
- Apache-2.0 licensed with training code, evaluation scripts, and Spatial-TTT-nano model available

## Synthesis
Spatial-TTT addresses a fundamental limitation of current video understanding models: they are designed for fixed-length inputs, but real-world spatial understanding tasks often involve continuous, unbounded video streams where spatial context accumulates over time. A robot navigating a building, an autonomous vehicle understanding its environment, or an AR system maintaining awareness of a physical space all require continuously updating spatial models rather than processing fixed clips.

The core innovation is the combination of Test-Time Training (TTT) layers with standard self-attention in a hybrid architecture. TTT layers maintain adaptive fast weights that update online as new video frames arrive—functioning as a compact, nonlinear memory for accumulated 3D evidence. Unlike static memory systems that must decide what to store at access time, TTT fast weights update through gradient-like operations that naturally compress and organize spatial evidence as it accumulates.

The interleaving of TTT and self-attention layers is architecturally principled. Pure self-attention excels at integrating information within a bounded context window but degrades as context grows without bound. Pure TTT layers provide compressed memory but may lose precise recent information. The hybrid approach uses self-attention for precise integration of recent frames while TTT layers handle long-horizon spatial evidence accumulation—each component doing what it does best.

Large-chunk processing with sliding-window attention addresses the computational efficiency challenge. Processing video frame-by-frame with full attention is prohibitively expensive; chunked processing reduces cost while the sliding window maintains temporal continuity across chunk boundaries. Lightweight depthwise 3D convolutions capture geometric correspondence between frames at lower computational cost than attention-based alternatives.

The Spatial-TTT-Data-97K training dataset—97K samples of dense scene description organized to help models learn systematic spatial signal organization—is potentially as valuable as the architectural innovation for practitioners who want to replicate or extend the work.
