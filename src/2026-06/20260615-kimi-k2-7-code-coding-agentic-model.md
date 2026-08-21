# Kimi K2.7 Code: Coding-Focused Agentic Model from Moonshot AI
**Source**: https://huggingface.co/moonshotai/Kimi-K2.7-Code
**Date**: 2026-06-15
**Author**: Moonshot AI
**Keywords**: Kimi K2.7 Code, Moonshot AI, MoE, coding agent, open-weight, INT4 quantization, preserve_thinking, agentic coding

## Elevator pitch
Moonshot AI releases Kimi K2.7 Code, a coding-focused agentic model built on the K2.6 architecture with a 1T-parameter MoE (32B activated), 256K context, and a new `preserve_thinking` mode that retains reasoning across multi-turn interactions—achieving substantial improvements on real-world long-horizon coding tasks while reducing thinking-token usage by ~30%.

## Takeaways
- Built on Kimi K2.6 architecture: 1T total parameters, 32B activated per token, 384 experts with 8 selected, 61 layers, 256K context, MLA attention
- `preserve_thinking` mode is forced on and cannot be disabled—it retains full reasoning content across multi-turn conversations, significantly improving coding agent performance where context from previous reasoning steps matters
- Thinking-token usage reduced by ~30% compared to K2.6, improving token efficiency for long agentic coding workflows without sacrificing quality
- Benchmarks: Kimi Code Bench v2 jumps from 50.9 (K2.6) to 62.0 (K2.7 Code), narrowing the gap with GPT-5.5 (69.0) and Claude Opus 4.8 (67.4)
- Agentic benchmarks show strong gains: MCP Atlas improves from 69.4 to 76.0, and MCP Mark Verified from 72.8 to 81.1, demonstrating real tool-use capability improvements
- Released under Modified MIT license with native INT4 quantization, deployable via Transformers, vLLM, SGLang, and Docker Model Runner

## Synthesis
Kimi K2.7 Code represents Moonshot AI's focused bet on the coding-agent market segment. Rather than chasing general-purpose frontier benchmarks, K2.7 Code is specifically optimized for the workflows that matter to coding agents: long-horizon task completion, tool calling, and multi-turn reasoning. The `preserve_thinking` feature is the most architecturally interesting addition—it addresses a real problem in agentic coding where reasoning context from earlier turns is lost, causing agents to repeat analysis or miss connections between steps.

The benchmark improvements are meaningful. On Kimi Code Bench v2, the jump from 50.9 to 62.0 is a 22% improvement—significant for an incremental model release. The agentic benchmarks (MCP Atlas, MCP Mark Verified) show even larger relative gains, suggesting the model has been specifically trained on tool-use patterns. However, the gap to GPT-5.5 and Claude Opus 4.8 remains: on Program Bench, K2.7 Code scores 53.6 vs GPT-5.5's 69.1. The model is closing the distance but not yet at parity.

The 30% reduction in thinking-token usage is strategically important for cost-conscious deployments. Agentic coding workflows can consume hundreds of thousands of tokens per task; a 30% reduction in reasoning tokens directly translates to lower serving costs and faster end-to-end task completion. Combined with native INT4 quantization, this makes K2.7 Code one of the most token-efficient models in its capability class.

The Modified MIT license continues Moonshot's open-weight strategy, though the "Modified" qualifier means teams should review the specific terms before commercial deployment. The model works with Kimi Code CLI as its recommended agent framework, available at kimi.com/code, but is also compatible with standard inference engines (vLLM, SGLang, Transformers) for self-hosted deployments.