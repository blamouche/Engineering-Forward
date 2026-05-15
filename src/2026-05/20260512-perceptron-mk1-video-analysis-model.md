# Perceptron Mk1 shocks with highly performant video analysis AI model 80-90% cheaper than Anthropic, OpenAI & Google
**Source**: https://venturebeat.com/technology/perceptron-mk1-shocks-with-highly-performant-video-analysis-ai-model-80-90-cheaper-than-anthropic-openai-and-google
**Date**: May 12, 2026
**Author**: Carl Franzen
**Keywords**: Perceptron, Mk1, video analysis, physical AI, spatial reasoning, efficiency frontier, Armen Aghajanyan, multimodal

## Elevator pitch
Two-year-old startup Perceptron Inc. released its Mk1 video analysis reasoning model at $0.15/$1.50 per million input/output tokens—80-90% cheaper than comparable models from Anthropic, OpenAI, and Google—while matching or exceeding their performance on spatial and video reasoning benchmarks.

## Takeaways
- Mk1 achieves state-of-the-art results on spatial reasoning benchmarks (85.1 on EmbSpatialBench vs Google Robotics-ER 1.5's 78.4) and dominates referring expression comprehension (72.4 vs GPT-5m's 9.0 on RefSpatialBench).
- The model processes native video at up to 2 FPS across a 32K token context window with temporal continuity, maintaining object identity through occlusions—critical for robotics and surveillance.
- Physical reasoning is a key differentiator: Mk1 can analyze causal relationships like determining if a basketball shot was released before a buzzer by jointly reasoning over ball position and shot clock.
- The company maintains a dual licensing strategy: closed-source Mk1 via API for enterprise, plus the open-weights Isaac series (2B parameters) for edge and low-latency deployments.
- Led by former Meta FAIR researchers Armen Aghajanyan and Akshat Shrivastava, the team built on their work from Meta's Chameleon and MoMa multimodal foundation model projects.

## Synthesis
Perceptron's Mk1 launch introduces a compelling new entrant in the physical AI space, challenging the assumption that frontier video understanding requires frontier-model pricing. At $0.15 per million input tokens and $1.50 per million output tokens, Mk1 sits at approximately 10-20% of the cost of comparable offerings from Anthropic, OpenAI, and Google, while posting competitive or superior benchmark scores across spatial reasoning, video understanding, and referring expression comprehension tasks.

The cost-performance achievement rests on what Perceptron calls a "multi-modal recipe" developed over 16 months from first principles. Rather than adapting an existing language model architecture to video, the team built specifically for the complexities of the physical world: temporal continuity, object persistence through occlusion, and causal reasoning about physical interactions. This manifests in concrete capabilities like reading analog gauges and clocks, pixel-precise pointing and counting in dense scenes, and reasoning about the temporal order of events—tasks that have historically challenged even the most capable vision-language models.

The founding team's pedigree is notable. Armen Aghajanyan and Akshat Shrivastava were both research scientists at Meta FAIR, where they contributed to the Chameleon early-fusion multimodal models and the MoMa efficiency-focused follow-on. Perceptron represents a direct commercialization of that research direction, targeting use cases that span robotics teleoperation data curation, manufacturing quality control, sports highlight auto-clipping, and wearable smart-glass assistants.

The dual licensing approach is strategically astute. The closed-source Mk1 API captures enterprise revenue for high-stakes applications, while the open-weights Isaac series (starting at 2B parameters with sub-200ms time-to-first-token) builds developer ecosystem and serves edge deployment scenarios. This mirrors strategies from players like Meta and Mistral, but applied specifically to the physical AI domain. The key risk is whether a two-year-old startup can sustain the engineering velocity to keep pace with well-resourced incumbents who will inevitably respond to the pricing pressure. For now, Mk1 has established a new efficiency frontier that redefines expectations for cost-conscious video AI deployment.
