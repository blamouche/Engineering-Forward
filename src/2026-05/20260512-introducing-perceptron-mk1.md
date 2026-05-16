# Introducing Perceptron Mk1: Frontier Video and Embodied Reasoning at a Fraction of the Cost
**Source**: https://www.perceptron.inc/blog/introducing-perceptron-mk1
**Date**: May 12, 2026
**Author**: Perceptron
**Keywords**: Perceptron Mk1, video understanding, embodied reasoning, robotics, physical AI, temporal reasoning, multimodal AI, computer vision, VLAs, spatial primitives

## Elevator pitch
Perceptron released Mk1, a closed-source model purpose-built for video understanding and embodied reasoning that matches frontier model performance (Gemini Pro class) at lower cost than Gemini Flash Lite — $0.15/M input, $1.50/M output tokens.

## Takeaways
- Mk1 features temporal reasoning with thinking traces: it reasons across time (sports broadcasts, cooking videos) returning structured breakdowns of what happened and when, with a hybrid reasoning mode that can be toggled off.
- Temporal grounding with video clips operates at up to 2 FPS across a 32K-token context window, returning structured timecodes for specific moments — enabling auto-clipping of grasp attempts, restocking events, etc.
- In-context learning via multimodal prompting: show one reference image/video and Mk1 finds all matching instances across new media — collapsing defect detection, asset tracking, and visual search workflows into single model calls.
- Advanced image reasoning includes improved pointing/counting (reliable into the hundreds), complex OCR (analog gauges, clock faces), and structured document extraction to HTML/JSON/Markdown with layout preservation.
- Mk1 outputs structured spatial primitives (point, box, polygon, track, clip) as first-class outputs alongside text, directly consumable by downstream robotics policies — making it useful for training VLAs, running alongside policies, and closing RL loops.

## Synthesis
Perceptron's Mk1 launches into an increasingly crowded multimodal model market with a clear differentiator: specialization for the physical world. Where general-purpose multimodal models treat video as a secondary modality, Mk1 is architected around temporal and spatial reasoning from the ground up. The model matches or exceeds Gemini Pro on video and embodied reasoning benchmarks while undercutting Gemini Flash Lite on price — an aggressive positioning for production deployments where cost sensitivity is paramount.

The temporal reasoning capabilities are Mk1's standout feature. The model doesn't just label video content; it reasons across time with structured "thinking traces" that decompose events into timestamped breakdowns. The temporal grounding feature — auto-clipping specific moments from long streams — addresses a real bottleneck in robotics data pipelines where manual annotation of teleoperation footage is expensive and slow. The 32K-token multimodal context window at up to 2 FPS means Mk1 can process roughly 4.5 hours of video in a single context.

For robotics specifically, Mk1's spatial primitive outputs (point, box, polygon, track, clip) as first-class outputs alongside text are a practical design choice. These structured outputs can be consumed directly by downstream policies without parsing natural language descriptions, making Mk1 useful at multiple stages of the robotics stack: as an annotation pipeline for training data (subtask boundaries, success/failure labels, action-conditioned annotations), as an inference-time reasoning layer above the VLA (grasp affordances, constraint checks, multi-view understanding), and as a verification layer (reading task outcomes from video for retry-or-progress signals).

The six deployment archetypes — manufacturing/industrial, media/content, robotics/automation, geospatial/infrastructure, security/surveillance, and devices/multimodal agents — suggest Perceptron is targeting enterprise buyers with concrete ROI cases rather than selling model access alone. The mention of "enhanced vision for Claude, Codex, and other text-first agents" positions Mk1 as a potential vision backend for AI agents that currently struggle with real-world perception, though how this integration works in practice remains to be seen. The roadmap toward "action-grounded video understanding for embodied agents" and longer temporal reasoning horizons signals that Mk1 is a foundation release, not a final product.
