# How NVIDIA Builds Open Models for the Age of AI
**Source**: https://blog.bytebytego.com/p/how-nvidia-builds-open-models-for
**Date**: 2026-07-27
**Author**: Alex Xu / ByteByteGo (interview with Bryan Catanzaro, VP Applied Deep Learning Research at NVIDIA)
**Keywords**: NVIDIA, open models, Nemotron, Cosmos, hybrid architecture, Mamba, GPU co-design, open source AI

## Elevator pitch
NVIDIA is the world's largest publisher of open AI models, spanning reasoning, physical AI, healthcare, and quantum computing — and it gives them away to grow the ecosystem that buys its GPUs.

## Takeaways
- NVIDIA's open model ecosystem spans three domains: reasoning models (Nemotron family), physical AI/world models (Cosmos), and specialized verticals (Isaac GR00T for robotics, Alpamayo for self-driving, BioNeMo for drug discovery, Earth-2 for climate).
- The hybrid architecture combines Mamba (efficient, linear-cost) layers with attention (precise recall) layers and mixture-of-experts, enabling million-token context windows at practical cost.
- NVIDIA co-designs its models with its GPUs: Nemotron models are pretrained in 4-bit (NVFP4) format from step one, matching Blackwell's hardware capabilities — rather than training in high precision and quantizing later.
- Post-training via large-scale reinforcement learning across diverse environments is where capability gains compound; NVIDIA's efficiency lets it scale RL at lower cost with over a million rollouts.
- The same foundation is reused across all model families (Cosmos Reason feeds into Isaac GR00T for robotics), following the "Unified" philosophy that made CUDA successful — build once, reuse everywhere.

## Synthesis
NVIDIA's emergence as the largest publisher of open AI models is a strategic move that merges hardware insight with software ecosystem thinking. In an interview with ByteByteGo, VP of Applied Deep Learning Research Bryan Catanzaro explains that NVIDIA doesn't just sell GPUs — it builds the models that demonstrate what those GPUs can do, then releases them openly so the world can build on them.

The technical architecture underpinning these models is a hybrid of Mamba state-space layers and attention layers, augmented with mixture-of-experts routing. Most layers are Mamba, which compresses long sequences into fixed-size memory at linear cost. A few attention layers provide pinpoint recall. MoE layers activate only a small subset of parameters per token. The result: models that can handle million-token contexts without the quadratic cost of pure Transformers, while maintaining strong retrieval performance.

A striking design choice is 4-bit pretraining. Rather than training in high precision and quantizing afterward — which degrades accuracy — NVIDIA trains in NVFP4 from the start, because it knew Blackwell GPUs would have fast 4-bit hardware. This is co-design of model and chip, and Catanzaro frames it as essential in a post-Moore's-law world where easy gains per generation are gone.

The open strategy goes beyond releasing weights. NVIDIA publishes training datasets, post-training datasets, RL environments, and recipes. This "open" extends to robotics simulation frameworks and evaluation datasets. The philosophy is that releasing data and recipes enables developers to post-train models at a fraction of the original cost, creating a thriving ecosystem of fine-tunes and derivatives — the Nemotron family recently crossed 100 million total downloads.

Why give it all away? Two reasons. First, NVIDIA needs deep AI understanding to design the right hardware, and open-sourcing keeps the work honest and connected to the community. Second, NVIDIA grows when AI grows — every team that builds on open models becomes a future compute customer. Catanzaro explicitly frames this not as charity but as the same long-term strategy that made CUDA dominant over a decade.

The key lessons from shipping many open models: the program matters more than any single release (models are obsolete before they ship, so sustained cadence builds trust); developer experience matters (licensing, documentation, examples); and community-trusted licenses (NVIDIA adopted OpenMDW from the Linux Foundation). Looking ahead, NVIDIA plans to open even earlier through the Nemotron and Cosmos Coalitions, letting partners shape models during development rather than after release.