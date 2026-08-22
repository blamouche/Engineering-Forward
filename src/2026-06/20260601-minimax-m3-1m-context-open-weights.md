# MiniMax M3: 1M Context Window with Open Weights Promise
**Source**: https://www.implicator.ai/minimax-promises-m3-weights-after-1m-context-model-launch/
**Date**: 2026-06-01
**Author**: Marcus Schuler (Implicator)
**Keywords**: MiniMax, M3, open weights, 1M context, multimodal, SWE-Bench, MSA, sparse attention, coding model, API, Hugging Face

## Elevator pitch
MiniMax released M3 with a 1M-token context window and native multimodality—the first open-weight model to combine frontier coding, multimodality, and million-token context—but the weights and technical report won't arrive for 10 days, leaving developers with API access before local inspection.

## Takeaways
- MiniMax M3 offers a 1M-token context window with a guaranteed 512,000-token minimum for API use, the first open-weight model to combine frontier coding, native multimodality, and 1M-token context
- Benchmark scores: 59.0% on SWE-Bench Pro, 66.0% on Terminal-Bench 2.1, 74.2% on MCP Atlas
- MiniMax Sparse Attention (MSA) uses a pre-filtering step to pick relevant key-value blocks before full attention, cutting per-token compute at 1M context
- Standard API pricing: $0.60 per million input tokens, $2.40 per million output—significantly cheaper than frontier closed models
- A STAR Market disclosure triggered a 16% Hong Kong share drop after launch, despite strong benchmark results

## Synthesis
MiniMax released M3 on June 1, 2026, marking a significant milestone as the first open-weight model to combine frontier coding capabilities, native multimodality, and a 1M-token context window. The Shanghai-based company is offering M3 through MiniMax Code, token plans, and an API, with model weights and a technical report promised within 10 days on Hugging Face and GitHub.

The model's benchmark performance is competitive: 59.0% on SWE-Bench Pro, 66.0% on Terminal-Bench 2.1, and 74.2% on MCP Atlas. In a company-run Hopper test, M3 worked on FP8 matrix multiplication for about 24 hours, made 147 benchmark submissions and 1,959 tool calls, then raised hardware utilization from 7.6% to 71.3%. The model uses MiniMax Sparse Attention (MSA), which partitions cached keys and values into blocks and reads each selected block once through a "KV outer gather Q" operator design, cutting per-token compute at the 1-million-token context length.

The pricing is aggressive: $0.60 per million input tokens and $2.40 per million output tokens, positioning M3 as a cost-effective alternative to frontier closed models for tasks requiring long context. The API-first release strategy means developers can build and test immediately, but the open-weight claim still depends on the company delivering model files and a technical report—the gap between API access and local inspection is a notable caveat.

The market response was mixed. A STAR Market disclosure triggered a 16% Hong Kong share drop after launch, suggesting investors had concerns about the company's financial position or the competitive landscape despite the strong technical release. The methodology notes also cite internal infrastructure, Mini-SWE-Agent, Claude Code scaffolding, and MiniMax scoring choices for different tests, which means some benchmark results may not be directly comparable to other models' self-reported scores.