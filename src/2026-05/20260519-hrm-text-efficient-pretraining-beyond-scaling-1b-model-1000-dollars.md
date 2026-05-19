# HRM-Text — Efficient Pretraining Beyond Scaling: A 1B Model Trained for ~$1,000
**Source**: https://github.com/sapientinc/HRM-Text
**Date**: 2026-05
**Author**: Sapient Inc.
**Keywords**: HRM architecture, efficient pretraining, Hierarchical Reasoning Model, 1B model, FSDP2, FlashAttention 3, low-cost training, latent space reasoning

## Elevator pitch
HRM-Text demonstrates that a 1B-parameter foundation model can be pretrained from scratch for approximately $1,000 using a hierarchical recurrent architecture, achieving competitive benchmark scores with 130-600x less compute and 150-900x less data than conventional approaches.

## Takeaways
- The 1B XL model achieves 84.7% on GSM8k, 56.5% on MATH, 82.3% on DROP, and 60.7% on MMLU — trained on 16 H100s for 46 hours (~$1,472)
- The smaller 0.6B L model achieves 77.6% on GSM8k on 8 H100s for 50 hours (~$800)
- Architecture uses PrefixLM sequence packing, FlashAttention 3 kernels, and PyTorch FSDP2 for distributed training
- Hierarchical Recurrent Model architecture splits layers between H and L modules with half_layers configuration
- Full pretraining framework includes data pipeline, distributed training, evaluation across 8 benchmarks, and HuggingFace-format export

## Synthesis
Sapient Inc.'s HRM-Text challenges the assumption that training foundation models requires massive compute budgets. Built on the Hierarchical Reasoning Model (HRM) architecture — a recurrent design that splits layers between H (high-level) and L (low-level) modules — the 1B parameter XL variant trains on just 16 H100 GPUs for 46 hours at an estimated cost of $1,472. The smaller 0.6B L variant runs on a single 8-GPU node for $800.

The benchmark results are competitive for models in this size class. The 1B model scores 84.7% on GSM8k math reasoning, 60.7% on MMLU, 82.3% on DROP reading comprehension, and 81.9% on ARC-Challenge. These numbers don't approach frontier models, but they represent a dramatically different point on the compute-performance Pareto frontier — achieving respectable results with 130-600x less compute than conventional scaling approaches.

The training framework is production-ready and open-source. It includes a companion data pipeline (data_io) for cleaning, tokenizing, and stratified-sampling pretraining corpora; PrefixLM sequence packing that masks instruction tokens by default; multipack batching with LPT allocation; and FlashAttention 3 kernels for efficient attention computation. FSDP2 handles distributed training across multiple nodes with checkpoint sharding. Evaluation covers eight benchmarks (GSM8k, MATH, DROP, MMLU, ARC-C, HellaSwag, Winogrande, BoolQ) with a single-command interface.

The repository supports multiple architectures beyond HRM, including standard Transformer, Tiny Recursive Model (TRM), Recursive Inference Scaling (RINS), and Universal Transformer baselines — making it useful as a research framework for comparing recurrent architectures. With vLLM support in progress and native Transformers integration scheduled for the next release, HRM-Text positions itself as both a practical tool for low-cost pretraining and a demonstration that architectural innovation can dramatically reshape the economics of foundation model development.
