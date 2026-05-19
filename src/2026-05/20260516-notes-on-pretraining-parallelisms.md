# Notes on Pretraining Parallelisms and Failed Training Runs

**Source:** [Dwarkesh Patel](https://www.dwarkesh.com/p/notes-on-pretraining-parallelisms)
**Date:** 2026-05-16
**Author:** Dwarkesh Patel (based on conversation with an insider + lecture by Horace He)

## Summary

Deep technical notes on why pretraining runs fail and the strategies used to parallelize them at scale.

## Why Pretraining Runs Fail

### Breaking Causality
- **Expert routing** — "expert choice" routing (splitting tokens by relative expert preference to balance load) breaks causality: token N's expert assignment may depend on token N+K's routing. This information wouldn't be available in deployment. Rumor: this explains Llama 4's underwhelming performance.
- **Token dropping** — experts ignore lower-ranked tokens to avoid padding. Breaks causality when a later token being strongly matched to an expert leads to an earlier token being dropped. Reportedly an issue with Gemini 2 Pro.

### Adding Bias
- Bias is much worse than variance — variance averages out, bias compounds.
- **Original GPT-4 bug:** Using FP16 on all-reduce collectives. FP16 granularity is logarithmic — after 1024, mantissa steps are multiple whole numbers. Adding 1 to 1024 repeatedly rounds back to 1024, causing 10x error in accumulated values. Extremely difficult to find.

### Implications
- New bespoke bugs likely emerge at each new scale level (not a fixed set of problems)
- Bearish on AI automating kernel writing — Nvidia's best engineers took a long time to optimize for Blackwell
- Numerical drift between inference and training engines matters for RL training quality
- Disciplined process for amalgamating compute multipliers is critical

## Pretraining Parallelisms (Horace He)

- **FLOPs = 6ND** (2 forward + 4 backward per parameter per token)
- **Data Parallel:** Copy weights across GPUs, split batch. Hits HBM limits fast.
- **FSDP (Fully Sharded Data Parallel):** Each GPU stores 1/N of each layer; all-gathers full layer before processing. Default go-to. Comms volume ~ params × 3 (50% overhead vs vanilla DP).
- **Comms crossover:** FSDP compute time decreases with more GPUs but comms time doesn't → MFU craters. Need pipeline parallelism.
- **Batch size floor:** FSDP is data-parallel, each GPU processes at least one sequence. With critical batch 10M tokens and 10K sequence length → max ~1K GPUs.
- **Pipeline parallelism problems:** Bubbles (idle GPUs at batch boundaries), architecture constraints (interleaved attention layers cause imbalance). Slows research iteration — "the greatest sin."
