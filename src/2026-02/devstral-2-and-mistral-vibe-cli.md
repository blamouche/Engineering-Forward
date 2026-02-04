# Devstral 2 and Mistral Vibe CLI
**Source**: https://mistral.ai/fr/news/devstral-2-vibe-cli
**Date**: 2026-02-04
**Author**: Mistral AI
**Keywords**: Mistral, Devstral, coding model, open-source, CLI, AI agents, SWE-bench

## Elevator pitch
Mistral releases Devstral 2, a 123B open-weight coding model scoring 72.2% on SWE-bench Verified with up to 7x better cost-efficiency than Claude Sonnet, alongside Mistral Vibe CLI, an open-source terminal-based coding agent.

## Takeaways
- Devstral 2 (123B) achieves 72.2% on SWE-bench Verified, establishing it as one of the best open-weight coding models while being 5x smaller than DeepSeek V3.2
- Devstral Small 2 (24B) scores 68.0% on SWE-bench Verified and runs on consumer hardware, released under Apache 2.0
- Mistral Vibe CLI is an open-source command-line coding assistant with project-aware context, multi-file orchestration, and Agent Communication Protocol support
- Devstral 2 is currently free via API, with future pricing at $0.40/$2.00 per million tokens (input/output)
- Human evaluations show Devstral 2 beats DeepSeek V3.2 (42.8% win vs 28.6% loss) but Claude Sonnet 4.5 remains significantly preferred

## Synthesis
Mistral AI has released Devstral 2, its next-generation coding model family, marking a significant step in the open-source AI coding race. The release includes two models: Devstral 2 at 123B parameters under a modified MIT license, and Devstral Small 2 at 24B parameters under Apache 2.0, both designed to accelerate distributed intelligence through permissive licensing.

The headline achievement is Devstral 2's 72.2% score on SWE-bench Verified, placing it at the frontier of open-weight coding models. What makes this particularly noteworthy is its efficiency: the model is 5x smaller than DeepSeek V3.2 and 8x smaller than Kimi K2, while matching or exceeding their performance. Mistral claims up to 7x better cost-efficiency compared to Claude Sonnet on real-world tasks, though human evaluations conducted through Cline show that Claude Sonnet 4.5 remains the preferred model overall.

Devstral Small 2 is equally interesting for different reasons. At just 24B parameters, it achieves 68.0% on SWE-bench Verified — competitive with models five times its size — and can run locally on consumer hardware including NVIDIA GeForce RTX cards. This democratizes access to capable coding models for individual developers and small teams who cannot afford cloud GPU costs.

Alongside the models, Mistral introduces Vibe CLI, an open-source command-line coding assistant powered by Devstral. The tool provides an interactive chat interface with project-aware context, smart file references, multi-file orchestration, and persistent history. It supports the Agent Communication Protocol for IDE integration and is already available as a Zed extension. Key features include automatic scanning of file structure and Git status, configurable tool permissions, and programmable execution for scripting workflows.

The release reflects a broader industry trend where open-source models are closing the gap with proprietary ones, particularly in specialized domains like coding. Mistral's strategy of releasing smaller, more efficient models challenges the assumption that frontier performance requires massive scale. For enterprise users, the on-premise deployment capability and fine-tuning support offer alternatives to API-dependent workflows, particularly in regulated environments.

The competitive positioning is clear: Mistral wants to be the default open-source choice for coding agents, competing against both closed models like Claude and other open alternatives like DeepSeek. With early partnerships with Kilo Code and Cline, and the free API access during the introductory period, Mistral is betting that developer adoption will follow from accessibility and performance.
