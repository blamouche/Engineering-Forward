# Lance: ByteDance's 3B Unified Multimodal Model for Image and Video
**Source**: https://github.com/bytedance/Lance
**Date**: 2026-05-21
**Author**: Fengyi Fu, Mengqi Huang, Shaojin Wu et al. (ByteDance)
**Keywords**: ByteDance, Lance, multimodal, unified model, image generation, video generation, video editing, 3B parameters, open-source

## Elevator pitch
ByteDance has open-sourced Lance, a 3B-parameter native unified multimodal model trained from scratch that handles image/video understanding, generation, and editing in a single framework — delivering strong performance across all modalities with just 128 A100 GPUs and 3B active parameters.

## Takeaways
- Single unified model handles image understanding, video understanding, text-to-image, text-to-video, image editing, video editing, and multi-turn consistency editing
- Only 3B active parameters, trained from scratch (except ViT/VAE encoders) on just 128 A100 GPUs
- Supports video understanding with VQA, detailed captioning, and temporal reasoning
- Video editing includes multi-turn consistency editing (preserving identity across multiple edit rounds)
- Apache 2.0 license, weights on HuggingFace, with Gradio demo and inference scripts included

## Synthesis
ByteDance has released Lance, a surprisingly efficient unified multimodal model that challenges the assumption that you need massive parameter counts to achieve strong multimodal performance. At just 3B active parameters, Lance handles the full pipeline of image and video understanding, generation, and editing — tasks typically spread across multiple specialized models.

The model was trained from scratch (the transformer backbone, at least) using a staged multi-task recipe on a budget of 128 A100 GPUs, making it unusually accessible for a model of this capability. This efficiency-first approach contrasts with the trillion-parameter trajectories of frontier labs and suggests that architectural innovation and multi-task synergy can compensate for raw scale.

The unified architecture is the key technical contribution: rather than separate models for understanding and generation, Lance handles both within a single framework, enabling capabilities like multi-turn consistency editing where the model preserves character/scene identity across sequential edit rounds. The video understanding demos show temporal reasoning (counting actions, detecting unrealistic phenomena), while generation spans text-to-video, image editing, and intelligent video generation.

The release includes full inference code, Gradio demos, and model weights on HuggingFace under Apache 2.0. For the open-source community, this represents a significant step toward accessible, all-in-one multimodal models that don't require enterprise-scale compute budgets. ByteDance's track record in video (TikTok) makes their entry into open multimodal models particularly notable — the company clearly has deep expertise in video processing at scale.
