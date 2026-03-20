# Introducing Mistral Small 4
**Source**: https://mistral.ai/news/mistral-small-4
**Date**: 2026-03-16
**Author**: Mistral AI
**Keywords**: Mistral Small 4, multimodal, MoE, reasoning, latency, Apache 2.0, open source, AI model

## Elevator pitch
Mistral Small 4 unifies reasoning, multimodal, and fast instruct capabilities into a single 119B sparse MoE model with 6B active parameters, delivering 40% lower latency and 3x higher throughput than its predecessors.

## Takeaways
- 119B total parameters with only 6B active per token using 128 experts (4 active per token) in a sparse MoE architecture
- 256K context window with native multimodal support for text and image inputs
- 40% reduction in completion latency versus previous versions; 3x throughput improvement over Mistral Small 3
- Available on Mistral API, HuggingFace, NVIDIA accelerated computing, and Apache 2.0 licensed for open use
- Configurable reasoning effort parameter allows trading compute for reasoning depth on demand

## Synthesis
Mistral Small 4 represents the company's latest attempt to collapse what has historically been a necessary tradeoff: choosing between specialized models optimized for different tasks. Previous versions required separate models for reasoning-intensive work, multimodal inputs, and fast inference—each optimized for its use case at the cost of operational complexity.

The architectural choice to use a 128-expert Mixture of Experts (MoE) model with 4 active experts per token is central to this unification. By activating only 6B of the model's 119B total parameters per inference step, Mistral achieves the speed characteristics of a small model while retaining the knowledge and capability of a large one. The 40% latency reduction and 3x throughput improvement over Mistral Small 3 are direct consequences of this efficiency: fewer active parameters per token means faster computation per request.

The 256K context window is generous for a model in this performance tier and enables practical deployment in document analysis and code review scenarios where long-context understanding previously required much more expensive models. Native multimodal support (text and image) eliminates the need for separate vision models in applications that process mixed content.

The configurable reasoning effort parameter is a pragmatic addition. Rather than choosing between "fast" and "reasoning" model variants, developers can tune the depth of reasoning on a per-request basis—maximizing throughput for simple tasks while engaging extended reasoning for complex ones. This runtime flexibility reflects mature understanding of how AI models are actually deployed in production, where different request types have wildly different complexity profiles.

Apache 2.0 licensing continues Mistral's open-source strategy, ensuring the model can be deployed commercially without royalty obligations and can be fine-tuned without restrictions. Combined with NVIDIA accelerated computing support and HuggingFace availability, the distribution breadth positions Mistral Small 4 as viable infrastructure for organizations that want capable, commercially deployable AI without vendor lock-in.
