# Cerebras Is Coming to AWS
**Source**: https://www.cerebras.ai/blog/cerebras-is-coming-to-aws
**Date**: 2026-03-13
**Author**: James Wang
**Keywords**: Cerebras, AWS, Bedrock, disaggregated inference, AI inference, CS-3, Trainium, speed

## Elevator pitch
Cerebras and AWS announce a partnership deploying CS-3 systems in AWS data centers to deliver ultra-fast inference through disaggregated architecture, splitting prefill on Trainium and decode on Cerebras WSE for 5x more high-speed token capacity.

## Takeaways
- Disaggregated architecture: AWS Trainium handles prefill (processing queries), Cerebras WSE handles decode (generating tokens)—optimizing each phase for its hardware strengths
- Delivers "5x more high-speed token capacity" compared to traditional unified-chip inference approaches
- Agentic coding generates ~15x more tokens per output than conversational AI, creating demand for faster inference to maintain developer productivity
- Cerebras claims leadership in inference speed, "powering models from OpenAI, Cognition, and Meta at up to 3,000 tokens per second"
- Available through AWS Bedrock, running open-source LLMs and Amazon Nova models; both aggregated and disaggregated configurations supported

## Synthesis
The Cerebras-AWS partnership represents a significant infrastructure moment for AI inference. AWS's existing government and enterprise relationships combined with Cerebras's inference speed capabilities create a distribution channel for ultra-fast AI inference that neither company could achieve independently.

The technical architecture is the most interesting element. Inference consists of two computationally distinct phases: prefill, which processes the input prompt, and decode, which generates output tokens one at a time. These phases have different computational profiles—prefill is highly parallelizable and benefits from massive matrix computation, while decode is sequential and benefits from extremely fast memory access. Running both phases on the same hardware requires compromising on at least one.

The disaggregated architecture sends each phase to hardware optimized for it: AWS Trainium (designed for training but applicable to compute-intensive prefill) handles query processing, while Cerebras's Wafer Scale Engine (the largest chip ever built, with extraordinary on-chip memory bandwidth) handles decode. This split delivers "5x more high-speed token capacity" compared to unified approaches—a claimed improvement meaningful enough to change the economics of several application categories.

The 15x token multiplier for agentic coding versus conversational AI is the contextual detail that makes the speed case compelling. When AI agents are generating code, plans, and tool call responses in multi-step workflows, inference throughput directly limits how quickly the agent can complete tasks. At 1,000 tokens per second, a 5,000-token coding response takes 5 seconds; at 3,000 tokens per second, it takes under 2 seconds. In workflows with dozens of such calls, this compounds into meaningful development velocity differences.

AWS Bedrock availability makes Cerebras's inference speed accessible to the organizations that have already standardized on AWS infrastructure, removing the deployment barrier that previously required separate Cerebras API integration. The open-source model support ensures compatibility with the Llama, Mistral, and Qwen variants that dominate enterprise open-source deployments.
