# Latency vs Throughput vs Bandwidth: System Design Fundamentals and AI Trends for 2026
**Source**: https://blog.bytebytego.com/p/ep217-latency-vs-throughput-vs-bandwidth
**Date**: 2026-06-06
**Author**: ByteByteGo
**Keywords**: system-design, latency, throughput, bandwidth, tpu, ai-trends, claude-code, open-weight

## Elevator pitch
ByteByteGo's weekly system design refresher clarifies the often-confused trio of latency, throughput, and bandwidth, introduces Google's 8th-generation TPU in dual training/inference flavors, and maps the five AI trends shaping 2026: efficient reasoning, persistent agents, repo-scale coding, open-weight everywhere, and world models for physical AI.

## Takeaways
- Latency is the delay for a single packet, throughput is the actual delivery rate, and bandwidth is the maximum capacity — they are distinct metrics that solve different performance problems
- Throughput is always less than bandwidth due to congestion, packet loss, and protocol overhead; low latency doesn't guarantee high throughput
- Google's TPU v8 ships in two flavors for the first time: TPU 8t for training (raw throughput) and TPU 8i for inference (latency and chip-to-chip speed), sharing the same software stack
- Claude Code's 7 permission modes (plan, default, acceptEdits, auto, dontAsk, bypassPermissions, bubble) give developers granular control over agent autonomy
- The five AI trends for 2026: efficient reasoning via RLVR, persistent always-on agents, repo-scale coding agents, open-weight models reaching frontier competitiveness, and world models enabling physical AI

## Synthesis
ByteByteGo's EP217 refresher tackles one of the most common confusions in system design: the difference between latency, throughput, and bandwidth. The analogy is memorable — bandwidth is the highway width, throughput is the traffic flow, and latency is how long a single car takes to get from A to B. The key insight is that these three metrics are independent: a low-latency connection can have poor throughput if payloads are small or window sizes are tight, and throughput never reaches theoretical bandwidth capacity due to real-world overhead.

The TPU section highlights a significant architectural shift at Google. The 8th-generation TPU, unveiled at Cloud Next '26, is the first to split into two specialized variants. TPU 8t targets training where raw throughput is king, while TPU 8i optimizes for inference where latency and chip-to-chip communication speed matter most. Both share Axion CPUs, liquid cooling, and the same software stack, meaning code written for one runs on the other — a practical design choice that reduces developer friction.

The AI trends section identifies five categories to watch in 2026. Efficient reasoning is being driven by RLVR-style training that auto-checks math and code, with Gemini's adaptive thinking and Qwen3.5's sparse MoE as early signals. Persistent agents are evolving from chat into always-on loops with tools and memory, with examples like OpenClaw showing the direction. Repo-scale coding has moved from autocomplete to multi-file edits with tests and builds, with agents increasingly able to ship security-aware PRs. Open-weight models like GLM5 and Kimi K2.5 are now competing directly with closed models. Finally, multimodal world models are becoming the foundation for physical AI and robotics, with Google Genie 3 and humanoid robots as early examples.

The article also covers Claude Code's seven permission modes, noting that only five are user-selectable while "auto" is feature-flagged and "bubble" is internal. This taxonomy of agent autonomy levels is becoming increasingly important as coding agents gain more power.