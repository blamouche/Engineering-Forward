# Optimizing Effective Training Time for Meta’s Internal Recommendation/Ranking Workloads – PyTorch

**Source**: https://pytorch.org/blog/optimizing-effective-training-time-for-metas-internal-recommendation-ranking-workloads/
**Date**: April 21, 2026
**Author**: Unknown
**Keywords**: pytorch, optimizing, effective, training, time, meta, internal, recommendation

## Elevator pitch
Motivation and Introduction Across the industry, teams training and serving large AI models face aggressive ROI targets under tight compute capacity

## Takeaways
- Motivation and Introduction Across the industry, teams training and serving large AI models face aggressive ROI targets under tight compute capacity.
- As workloads scale, improving infrastructure effectiveness gets harder because end-to-end runtime increasingly includes overheads beyond “real training” (initialization, orchestration, checkpointing, retries, failures, and recovery).
- Meta utilizes Effective Training Time (ETT%) to quantify efficiency, defining it as the percentage of total end-to-end (E2E) wall time dedicated to productive training.
- This metric directly points to areas where time is wasted, thus facilitating the prioritization of efficiency improvements.
- In this work stream, while grounded in Meta’s production experience using PyTorch for model training, we aim to share broadly useful lessons: some improvements have been implemented in open source—e.g., TorchRec sharding plan improvements and PyTorch 2 (PT2) compilation optimizations that reduce compile time and recompilation—while others (like checkpointing and model publishing) are more Meta-specific, but address common industry bottlenecks and can be adapted elsewhere.

## Synthesis
Motivation and Introduction Across the industry, teams training and serving large AI models face aggressive ROI targets under tight compute capacity. As workloads scale, improving infrastructure effectiveness gets harder because end-to-end runtime increasingly includes overheads beyond “real training” (initialization, orchestration, checkpointing, retries, failures, and recovery). Meta utilizes Effective Training Time (ETT%) to quantify efficiency, defining it as the percentage of total end-to-end (E2E) wall time dedicated to productive training. This metric directly points to areas where time is wasted, thus facilitating the prioritization of efficiency improvements. In this work stream, while grounded in Meta’s production experience using PyTorch for model training, we aim to share broadly useful lessons: some improvements have been implemented in open source—e.g., TorchRec sharding plan improvements and PyTorch 2 (PT2) compilation optimizations that reduce compile time and recompilation—while others (like checkpointing and model publishing) are more Meta-specific, but address common industry bottlenecks and can be adapted elsewhere. Effective Training Time Definition Effective Training Time (ETT%) is defined as the percentage of E2E wall time spent on consuming new data. Since the end to end wall time depends on many factors such as model architecture, complexity, training data volume etc, it is hard to directly measure Effective Training Time(ETT%). Instead, focus on measuring idleness and failures, which can be represented as following formula: A visual view of the formula is shown below with three L1 sub-metrics: Time to Start : the period from when a job is allocated hardware to when it begins training the first batch of data. Time to Recover : the duration required for a training job to restart and resume productive training after a failure or interruption. Number of Failures : refers to the total count of infra-related interruptions or unsuccessful attempts that occur during the lifecycle of a training job.
