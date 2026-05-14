# Perceptron Mk1 shocks with highly performant video analysis AI model 80-90% cheaper than Anthropic, OpenAI & Google
**Source**: https://venturebeat.com/technology/perceptron-mk1-shocks-with-highly-performant-video-analysis-ai-model-80-90-cheaper-than-anthropic-openai-and-google
**Date**: May 12, 2026
**Author**: Carl Franzen
**Keywords**: Perceptron, Mk1, video analysis, physical AI, spatial reasoning, temporal continuity, efficiency frontier, Armen Aghajanyan, open weights

## Elevator pitch
Two-year-old startup Perceptron Inc. released its Mk1 video analysis reasoning model at 80-90% lower cost than Anthropic, OpenAI, and Google equivalents, while matching or exceeding their performance on spatial and video benchmarks.

## Takeaways
- Mk1 is priced at $0.15/M input tokens and $1.50/M output tokens, compared to blended costs of ~$2.00 for GPT-5 and ~$3.00 for Gemini 3.1 Pro
- The model achieved 85.1 on EmbSpatialBench (surpassing Google Robotics-ER 1.5 at 78.4) and 72.4 on RefSpatialBench (vs. GPT-5m at 9.0 and Sonnet 4.5 at 2.2)
- Mk1 processes native video at up to 2 FPS across a 32K token context window with temporal continuity, maintaining object identity through occlusions
- The model features "Physical Reasoning" capabilities, including understanding physics, reading analog gauges, and pixel-precise counting in dense scenes
- Perceptron maintains a dual strategy: closed-source Mk1 via API and open-weights "Isaac" series (0.2-2b-preview) for edge deployments, with commercial licenses available

## Synthesis
On May 12, 2026, Bellevue, Washington-based Perceptron Inc. unveiled its flagship model Mk1, delivering a significant shock to the AI video analysis market. Founded by former Meta FAIR researchers Armen Aghajanyan (CEO) and Akshat Shrivastava, the two-year-old startup has produced a video reasoning model that not only matches or beats frontier offerings from Anthropic, OpenAI, and Google on spatial and temporal benchmarks, but does so at an 80-90% cost reduction. Mk1's API pricing of $0.15 per million input tokens and $1.50 per million output tokens places it at a blended cost of approximately $0.30 — compared to roughly $2.00 for GPT-5 and $3.00 for Gemini 3.1 Pro.

The raw benchmark numbers tell a compelling story. On EmbSpatialBench (spatial reasoning), Mk1 scored 85.1, outpacing Google's Robotics-ER 1.5 (78.4) and rivaling Alibaba's Q3.5-27B. More dramatically, on RefSpatialBench — which measures referring expression comprehension — Mk1 hit 72.4 while GPT-5m managed only 9.0 and Claude Sonnet 4.5 scored 2.2, a staggering performance gap suggesting Mk1's architecture is fundamentally better suited to grounded spatial understanding. On the EgoSchema "Hard Subset" for video understanding, Mk1's 41.4 matched Q3.5-27B and nearly doubled Gemini 3.1 Flash-Lite's 25.0.

The technical underpinnings center on temporal continuity. Unlike conventional vision-language models that process video as discrete frames, Mk1 processes native video at up to 2 FPS across a 32K token context window, maintaining object identity through occlusions — essential for real-world surveillance and robotics applications. The model's "Physical Reasoning" capability goes beyond pattern recognition: it can determine whether a basketball shot was released before a buzzer by jointly reasoning over ball position and shot clock readouts, read analog gauges, and perform pixel-precise counting in dense scenes.

Perceptron's go-to-market strategy is notably pragmatic. The flagship Mk1 remains closed-source and API-accessed for enterprise security, but the company maintains an open-weights "Isaac" series (most recently Isaac 0.2-2b-preview, December 2025) optimized for sub-200ms time-to-first-token on edge devices. Commercial licenses are available for enterprises needing on-premise deployment. The accompanying Python SDK adds specialized functions like "Focus" (auto-cropping based on natural language prompts), "Counting" (dense scene enumeration), and in-context learning from just a few examples.

Founded in November 2024 from research roots in Meta's Chameleon and MoMa mixed-modal models, Perceptron's thesis is that AI must function in the physical world — not just text windows. Early adopters are already deploying Mk1 for sports highlight auto-clipping, robotics teleoperation data curation, manufacturing quality control, and smart-glass wearable assistants. The Mk1 release positions Perceptron as the efficiency leader in video AI, challenging incumbents on both price and performance simultaneously.
