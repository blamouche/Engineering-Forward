# FlashDrive: Flash Vision-Language-Action Inference For Autonomous Driving

**Source**: https://z-lab.ai/projects/flashdrive/
**Date**: April 21, 2026
**Author**: Z Lab
**Keywords**: z-lab, flashdrive, flash, vision, language, action, inference, autonomous

## Elevator pitch
FlashDrive: Flash Vision-Language-Action Inference For Autonomous Driving. Zekai Li*, Yihao Liang*, Hongfei Zhang et al.. Preview

## Takeaways
- FlashDrive: Flash Vision-Language-Action Inference For Autonomous Driving Zekai Li* , Yihao Liang* , Hongfei Zhang , Jian Chen , Zhijian Liu Preview Tap to play This is an early preview.
- The paper and additional results will be available shortly.
- Traditional autonomous driving systems separate perception and planning, which leaves them brittle on the âlong tailâ of rare, complex scenarios that real-world driving demands.
- Vision-Language-Action (VLA) models take a fundamentally different approach: by integrating chain-of-thought reasoning into end-to-end driving, they can think through novel situations step by step, producing explicit reasoning traces alongside trajectory predictions.
- This year, NVIDIA released Alpamayo 1 and Alpamayo 1.5 , the industryâs first open-source reasoning VLA models for autonomous driving.

## Synthesis
FlashDrive: Flash Vision-Language-Action Inference For Autonomous Driving Zekai Li* , Yihao Liang* , Hongfei Zhang , Jian Chen , Zhijian Liu Preview Tap to play This is an early preview. The paper and additional results will be available shortly. Traditional autonomous driving systems separate perception and planning, which leaves them brittle on the âlong tailâ of rare, complex scenarios that real-world driving demands. Vision-Language-Action (VLA) models take a fundamentally different approach: by integrating chain-of-thought reasoning into end-to-end driving, they can think through novel situations step by step, producing explicit reasoning traces alongside trajectory predictions. This year, NVIDIA released Alpamayo 1 and Alpamayo 1.5 , the industryâs first open-source reasoning VLA models for autonomous driving. Alpamayo 1.5 (10B parameters, built on Qwen3-VL) takes 716ms per step on an NVIDIA RTX PRO 6000, roughly 1.4 Hz, far short of the real-time requirements for safe driving. FlashDrive is an algorithm-system co-design framework that attacks all four stages (encode, prefill, decode, and action), reducing end-to-end latency to 159ms , a 4.5Ã speedup with negligible accuracy loss. The Bottleneck Is Everywhere A typical VLA driving modelâs inference breaks into four stages: vision encoding, prompt prefilling, reasoning token decoding, and action generation via flow matching. We profiled Alpamayo 1.5 and found that latency is spread across all four stages with no single dominant bottleneck. Getting close to real-time requires optimizing the entire stack.
