# WavFlow: Audio Generation in Raw Waveform Space
**Source**: https://github.com/facebookresearch/WavFlow
**Date**: 2026-05-21
**Author**: Feiyan Zhou, Luyuan Wang, Shoufa Chen et al. (Meta AI / Northeastern University)
**Keywords**: Meta, WavFlow, audio generation, waveform, flow matching, multimodal, video-to-audio, text-to-audio

## Elevator pitch
Meta AI has released WavFlow, an open-source multimodal audio generation model that produces synchronized, high-fidelity audio from video and text inputs directly in raw waveform space — bypassing latent compression entirely and proving that end-to-end waveform generation can match established latent-based methods.

## Takeaways
- Generates audio directly in raw waveform space without latent compression, using waveform patchifying and amplitude lifting for stable flow matching via direct x-prediction
- Supports video-to-audio, text-to-audio, and combined video+text-to-audio generation
- Performance matches established latent-based methods on VGGSound and AudioCaps benchmarks in acoustic richness, fidelity, and synchronization
- CC-BY-NC 4.0 license; production checkpoints not yet released due to organizational policy, but full training code provided
- Architecture leverages CLIP and Synchformer for multimodal conditioning

## Synthesis
WavFlow represents a notable technical bet from Meta AI: that generating audio directly in raw waveform space — without the intermediate latent compression step used by nearly all current audio generation models — can match or exceed the quality of latent-based approaches. The model uses flow matching with direct x-prediction, stabilized through waveform patchifying and amplitude lifting techniques that make training on raw audio tractable.

The key technical claim is that the end-to-end waveform approach demonstrates performance on par with established latent methods on standard benchmarks (VGGSound for video-to-audio, AudioCaps for text-to-audio), across metrics of acoustic richness, fidelity, and synchronization. This matters because latent compression, while computationally convenient, inevitably introduces information loss — bypassing it could unlock higher fidelity ceilings.

The practical release is somewhat constrained: Meta can't release production-trained checkpoints due to organizational policy, but provides full training code, architecture, and a training guide. The model supports three modalities (video-only, text-only, and combined), making it a flexible foundation for synchronized audio generation tasks.

The CC-BY-NC 4.0 license limits commercial use, which is standard for Meta research releases. The architecture builds on MMAudio and Synchformer for audiovisual synchronization, positioning WavFlow within Meta's broader multimodal research portfolio. For researchers, the open training pipeline is the main value proposition — it enables training custom waveform-generation models on their own data without being locked into latent-space architectures.
