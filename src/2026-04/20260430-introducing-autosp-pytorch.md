# Introducing AutoSP – PyTorch

**Source**: https://pytorch.org/blog/introducing-autosp/
**Date**: April 30, 2026
**Author**: Unknown
**Keywords**: pytorch, introducing, autosp

## Elevator pitch
¹ SSAIL Lab, University of Illinois Urbana-Champaign, ² Anyscale, ³ Snowflake TL;DR: AutoSP automatically converts standard transformer training code into sequence-parallel code for long-context LLM training across multiple GPUs

## Takeaways
- ¹ SSAIL Lab, University of Illinois Urbana-Champaign, ² Anyscale, ³ Snowflake TL;DR: AutoSP automatically converts standard transformer training code into sequence-parallel code for long-context LLM training across multiple GPUs.
- Integrated with DeepSpeed , it increases maximum trainable context length with little runtime overhead versus hand-written baselines.
- Increasingly, Large-Language-Models (LLMs) are being trained for extremely long-context tasks, where token counts can exceed 100k+.
- At these token counts, out-of-memory (OOM) issues start to surface, even when scaling device counts using conventional training techniques such as ZeRO/FSDP.
- To circumvent these issues, sequence parallelism (SP): partitioning the input tokens across devices to enable long-context training with increasing GPU counts, is a commonly used parallel training technique.

## Synthesis
¹ SSAIL Lab, University of Illinois Urbana-Champaign, ² Anyscale, ³ Snowflake TL;DR: AutoSP automatically converts standard transformer training code into sequence-parallel code for long-context LLM training across multiple GPUs. Integrated with DeepSpeed , it increases maximum trainable context length with little runtime overhead versus hand-written baselines. Increasingly, Large-Language-Models (LLMs) are being trained for extremely long-context tasks, where token counts can exceed 100k+. At these token counts, out-of-memory (OOM) issues start to surface, even when scaling device counts using conventional training techniques such as ZeRO/FSDP. To circumvent these issues, sequence parallelism (SP): partitioning the input tokens across devices to enable long-context training with increasing GPU counts, is a commonly used parallel training technique. However, implementing SP is notoriously difficult, requiring invasive code changes to existing libraries such as DeepSpeed or HuggingFace. These code changes often involve partitioning input token contexts (and intermediate activations), inserting communication collectives, and overlapping communication with computation, all of which must be done for both the forward and backwards pass. This results in researchers who want to experiment with long context capabilities spending significant effort on engineering the system’s stack to enable such capability, repeating this effort for different hardware vendors. To avoid this complexity, we introduce AutoSP : a fully automated compiler-based solution that automatically converts easy-to-write training code to multi-GPU sequence parallel code that efficiently uses GPUs to train on longer input contexts while composing with existing parallel strategies (such as ZeRO). This avoids the cumbersome need for developers to repeatedly modify training pipelines for long-context training.
