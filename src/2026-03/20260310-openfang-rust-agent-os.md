# OpenFang: Open-Source Agent Operating System in Rust
**Source**: https://github.com/RightNow-AI/openfang
**Date**: 2026-03-10
**Author**: RightNow-AI
**Keywords**: OpenFang, Rust, agent operating system, autonomous agents, WASM sandbox, security, LLM providers, MCP, Merkle chain

## Elevator pitch
OpenFang is a 32MB Rust binary that functions as a complete agent operating system—running seven types of autonomous agents on schedules across 40 messaging platforms with 16 security layers including WASM sandboxing and Merkle hash-chain auditing.

## Takeaways
- Complete agent OS: 137K LOC, 14 crates, 1,767+ tests, single ~32MB binary deployment.
- Seven bundled "Hands" (capability packages): Clip, Lead, Collector, Predictor, Researcher, Twitter, and Browser.
- 40 messaging channel adapters including Telegram, Discord, Slack, and WhatsApp.
- 16 security systems: WASM sandbox, Merkle hash-chain auditing, and taint tracking for cryptographic accountability.
- 27 LLM provider integrations with 123+ models; 53 built-in tools plus MCP support.
- Agents run on schedules autonomously rather than waiting for user prompts—a fundamentally different operating model from chat-first assistants.

## Synthesis
OpenFang's defining characteristic is the combination of Rust's performance and memory safety with enterprise-grade security architecture in a deployable single binary. This combination is unusual in the AI agent space, which has predominantly used Python frameworks that prioritize developer convenience over operational characteristics.

The WASM sandbox is the most significant security feature. Sandboxing agent-executed code prevents agents from accessing host system resources they shouldn't touch, containing the blast radius of a prompt injection or tool misuse incident. Most Python agent frameworks don't sandbox tool execution at all; OpenFang makes it a first-class architectural component.

The Merkle hash-chain auditing is equally important for enterprise adoption. When agents take autonomous actions on schedules—sending messages, making API calls, triggering workflows—organizations need accountability mechanisms that prove what happened and when. A cryptographic audit trail that can't be tampered with retrospectively creates the kind of accountability that security and compliance teams require.

The schedule-first operating model distinguishes OpenFang from most agent frameworks, which are designed around request-response patterns (user sends prompt, agent responds). Agents that run on schedules have different requirements: they need persistent configuration, autonomous trigger evaluation, and operational monitoring without human-in-the-loop at each invocation. OpenFang's architecture is built for this pattern rather than retrofitting it onto a chat-first design.
