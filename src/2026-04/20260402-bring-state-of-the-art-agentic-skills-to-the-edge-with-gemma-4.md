# Bring state-of-the-art agentic skills to the edge with Gemma 4

**Source**: https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4
**Date**: April 2, 2026
**Author**: Google DeepMind
**Keywords**: Gemma 4, edge AI, on-device agents, LiteRT-LM, Google AI Edge, mobile AI, agent skills

## Elevator pitch
Google is positioning Gemma 4 as a serious on-device agent platform, pairing open models with edge tooling that can run multi-step workflows, tool calling, and multimodal experiences directly on phones, desktops, and embedded hardware.

## Takeaways
- Gemma 4 is being pushed not just as an open model family but as a full edge-agent stack.
- Google AI Edge Gallery showcases skill-based, multi-step workflows running entirely on-device.
- LiteRT-LM extends Gemma deployment across mobile, desktop, web, Raspberry Pi, and Qualcomm hardware.
- Tool calling and multimodal support make small local models more useful for practical app experiences.
- The release suggests agentic UX is moving from cloud novelty toward real local infrastructure.

## Synthesis
This announcement is notable because it treats on-device agents as a product category rather than a benchmark stunt. Google is packaging Gemma 4 with the surrounding runtime needed to make it useful on real hardware: mobile SDKs, LiteRT-LM, examples, tool calling, and cross-device deployment paths. That stack matters more than raw model claims because local AI succeeds only when developers can actually ship it.

The interesting strategic move is coupling openness with deployability. Gemma 4 is under Apache 2.0, supports many languages, and is presented as capable of multi-step planning and multimodal work without special fine-tuning. That combination lowers the barrier for app teams that want agentic behavior without a permanent cloud dependency. If local models become good enough for many workflows, the economics and UX of AI products start to shift in meaningful ways.

There is also a broader architectural signal here. Edge inference used to mean small offline assistants with narrow capabilities. Google is now presenting a world where local models can orchestrate tools, generate code, process images and audio, and stitch together multi-step flows. That expands the design space for privacy-sensitive, latency-sensitive, or intermittently connected applications.

The larger takeaway is that “agentic” no longer implies server-side by default. As runtimes improve and open models get more efficient, some of the most practical AI products may end up running close to the user rather than in a distant inference cluster.
