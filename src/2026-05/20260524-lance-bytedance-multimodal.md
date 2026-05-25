# Lance: Unified Multimodal Modeling by Multi-Task Synergy
**Source**: https://huggingface.co/bytedance-research/Lance
**Date**: May 24, 2026 (arXiv: 2605.18678)
**Author**: Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (ByteDance Research)
**Keywords**: ByteDance, Lance, multimodal, unified model, image generation, video generation, image editing, video understanding, 3B parameters

## Elevator pitch
ByteDance Research unveils Lance, a lightweight 3B-parameter unified multimodal model that supports image and video understanding, generation, and editing in a single framework, trained from scratch on just 128 A100 GPUs.

## Takeaways
- Lance is a native unified multimodal model that handles image/video understanding, generation, and editing within a single 3B active parameter framework.
- Trained from scratch using a staged multi-task recipe within a 128-A100-GPU budget, making it accessible for academic and smaller industrial labs.
- Capabilities span text-to-image, text-to-video, image editing, video editing, multi-turn consistency editing, and visual question answering.
- The model demonstrates strong performance on image generation, editing, and video benchmarks despite its compact size.
- Released under Apache 2.0 license with weights on Hugging Face, a unified CLI for all tasks, and detailed documentation.

## Synthesis
ByteDance Research's Lance represents a notable push toward unified multimodal models that don't require the massive compute budgets typically associated with frontier AI. At 3B active parameters, Lance handles a remarkable breadth of tasks — text-to-image generation, text-to-video generation, image editing, video editing, multi-turn consistency editing, image understanding, and video understanding — all within a single architecture trained from scratch on 128 A100 GPUs.

This is significant because the multimodal AI landscape has largely been dominated by either specialized models (dedicated text-to-image, separate video models) or massive generalist systems from well-funded labs. Lance demonstrates that unified multimodal capabilities can be achieved at a scale accessible to broader research communities. The staged multi-task training recipe appears to be a key innovation, suggesting that careful curriculum design can extract more capability per parameter than monolithic training approaches.

The model's video capabilities are particularly noteworthy at this scale. It supports text-to-video at 480p resolution with up to 121 frames, video editing with instruction following, and multi-turn consistency editing where outputs remain coherent across sequential edits. Video understanding includes both visual question answering (multiple choice and open-ended) and detailed video captioning.

On the image side, Lance handles generation, editing, and understanding including chart reading, OCR (license plate recognition), and detailed scene description. The demos show competent performance across all modalities, though the paper focuses on demonstrating breadth rather than claiming state-of-the-art on any single benchmark.

The Apache 2.0 license and Hugging Face release make this immediately usable by the research community. The provided CLI supports all tasks through a unified interface, with separate model weights for image-focused (Lance_3B) and video-focused (Lance_3B_Video) variants. This release pattern — open weights, permissive license, accessible compute requirements — positions Lance as a practical foundation for multimodal research and applications where the cost of larger proprietary models is prohibitive.
