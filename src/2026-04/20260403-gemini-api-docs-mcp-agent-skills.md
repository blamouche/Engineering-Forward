# Improve Coding Agents' Performance with Gemini API Docs MCP and Agent Skills

**Source**: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-docsmcp-agent-skills/
**Date**: 2026-04-03
**Author**: Google DeepMind
**Keywords**: Gemini API, MCP, coding agents, developer tools, AI coding, Model Context Protocol

## Elevator pitch
Google introduces two complementary tools — Gemini API Docs MCP and Agent Skills — that together achieve a 96.3% pass rate on coding evals with 63% fewer tokens compared to vanilla prompting.

## Takeaways
- Coding agents often generate outdated Gemini API code due to training data cutoff dates
- Gemini API Docs MCP connects agents to live, current Gemini API documentation via Model Context Protocol
- Agent Skills adds best-practice instructions and SDK patterns to guide the agent
- Combined, they achieve 96.3% pass rate and 63% fewer tokens per correct answer vs vanilla prompting
- Both tools are available at ai.google.dev/gemini-api/docs/coding-agents

## Synthesis
One of the persistent problems in AI-assisted coding is that language models have training data cutoffs — meaning any API or SDK that has evolved since their training date will be misrepresented, leading to broken or suboptimal generated code. Google addresses this directly for its own Gemini API ecosystem with two complementary tools designed to keep coding agents accurate and efficient.

The Gemini API Docs MCP (Model Context Protocol server) solves the knowledge staleness problem by connecting coding agents to live, up-to-date documentation, SDKs, and model information in real-time. Rather than relying on what the model learned during training, the MCP injects fresh documentation context at query time.

The Gemini API Developer Skills addresses the pattern and practice layer: it adds structured instructions, resource links, and best-practice patterns directly into the agent's context, guiding it toward current SDK usage patterns.

The compelling result is in the combination: together, these two tools achieve a 96.3% pass rate on Google's eval set, while requiring 63% fewer tokens per correct answer compared to vanilla prompting. This is significant — not just for accuracy but for cost efficiency in production deployments where token usage directly impacts billing.

For engineering teams building on the Gemini ecosystem, this pattern illustrates a broader principle: rather than waiting for model retraining to fix knowledge gaps, you can inject authoritative documentation via MCP at inference time. This approach — documentation-as-context rather than documentation-in-weights — is likely to become standard practice as APIs evolve faster than model training cycles. The same strategy could be adapted for any evolving API ecosystem.
