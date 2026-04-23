# Anker made its own chip to bring AI to all its products

**Source**: https://www.theverge.com/tech/916463/anker-thus-chip-announcement
**Date**: April 22, 2026
**Author**: The Verge
**Keywords**: Anker, custom silicon, AI chip, earbuds, edge AI, audio

## Elevator pitch
Anker has built a custom compute-in-memory chip for audio and small devices, betting that local AI features will spread through consumer hardware only if inference becomes tiny and power-efficient enough to live on-device.

## Takeaways
- The Thus chip is designed around compute-in-memory to reduce data movement and power usage.
- Anker is starting with flagship earbuds, where size and battery constraints are especially severe.
- The company says the chip can support larger on-device audio models than previous low-power designs.
- Initial benefits are framed around better noise suppression and voice isolation in difficult environments.
- The launch shows consumer electronics brands are starting to treat custom AI silicon as a product differentiator.

## Synthesis
Anker’s chip announcement is interesting because it brings the AI silicon story into a part of consumer hardware that is usually treated as peripheral. Instead of relying entirely on third-party chips, Anker is building its own compute-in-memory processor for audio devices, accessories, and IoT gear. The core bet is straightforward: if AI features are going to spread everywhere, they need to run locally on tiny devices without killing battery life or forcing everything through the cloud.

That is why earbuds are a useful first target. They are a harsh test environment: extremely limited space, constant-on operation, and demanding real-time audio processing. Traditional low-power neural approaches in earbuds have been constrained by the need to shuttle model parameters back and forth between storage and compute. Compute-in-memory changes that equation by putting computation where the model already lives, reducing movement and energy cost. Whether Anker’s implementation is as strong as advertised remains to be seen, but the architectural logic is credible.

The product angle matters too. Better call isolation and noise handling are tangible consumer benefits, not abstract AI features. If custom silicon lets Anker meaningfully outperform rivals on those basics, then the chip becomes a real differentiator rather than a branding exercise.

More broadly, this is a sign that edge AI is entering a new phase. It is no longer only about smartphone NPUs or big-platform companies. Accessory makers and device brands are starting to see custom AI hardware as a way to control performance, latency, and power at the product level. That could matter a lot as AI features spread into smaller devices where cloud dependence is costly, slow, or awkward.
