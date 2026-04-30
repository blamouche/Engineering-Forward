# Granite 4.1 LLMs: How They’re Built

**Source**: https://huggingface.co/blog/ibm-granite/granite-4-1
**Date**: April 30, 2026
**Author**: Unknown
**Keywords**: huggingface, granite, llms, they, built

## Elevator pitch
A Blog post by IBM Granite on Hugging Face.

## Takeaways
- Back to Articles Granite 4.1 LLMs: How They’re Built Enterprise Article Published April 29, 2026 Upvote 34 +28 Yousaf Shah yousafshah Follow ibm-granite An in-depth technical walkthrough of data engineering, pre-training, supervised fine-tuning, and reinforcement learning behind the Granite 4.1 LLMs.
- Authors: Granite Team, IBM TL;DR — Granite 4.1 is a family of dense, decoder‑only LLMs (3B, 8B, and 30B) trained on ~15T tokens using a multi‑stage pre‑training pipeline, including long‑context extension of up to 512K tokens.
- The models are further refined with supervised fine‑tuning on ~4.1M high‑quality curated samples and reinforcement learning via on‑policy GRPO with DAPO loss ( Yu et al., 2025 ).
- Notably, the 8B instruct model matches or surpasses the previous Granite 4.0‑H‑Small (32B‑A9B MoE) despite using a simpler dense architecture with fewer parameters.
- All Granite 4.1 models are released under the Apache 2.0 license.

## Synthesis
Back to Articles Granite 4.1 LLMs: How They’re Built Enterprise Article Published April 29, 2026 Upvote 34 +28 Yousaf Shah yousafshah Follow ibm-granite An in-depth technical walkthrough of data engineering, pre-training, supervised fine-tuning, and reinforcement learning behind the Granite 4.1 LLMs. Authors: Granite Team, IBM TL;DR — Granite 4.1 is a family of dense, decoder‑only LLMs (3B, 8B, and 30B) trained on ~15T tokens using a multi‑stage pre‑training pipeline, including long‑context extension of up to 512K tokens. The models are further refined with supervised fine‑tuning on ~4.1M high‑quality curated samples and reinforcement learning via on‑policy GRPO with DAPO loss ( Yu et al., 2025 ). Notably, the 8B instruct model matches or surpasses the previous Granite 4.0‑H‑Small (32B‑A9B MoE) despite using a simpler dense architecture with fewer parameters. All Granite 4.1 models are released under the Apache 2.0 license. Links: Granite 4.1 HF Collection GitHub Repository Granite Docs Overview Building high‑quality small language models goes beyond simply scaling compute—it requires rigorous data curation throughout training. For Granite 4.1, we prioritized data quality over quantity, progressively refining the data mixture across five pre‑training stages. We further curated supervised fine‑tuning data using an LLM‑as‑Judge framework and applied a multi‑stage reinforcement learning pipeline to systematically strengthen performance in math, coding, instruction following, and general chat. Model Architecture Granite 4.1 models use a decoder-only dense transformer architecture. The core design choices include Grouped Query Attention (GQA) , Rotary Position Embeddings (RoPE) , SwiGLU activations , RMSNorm , and shared input/output embeddings .
