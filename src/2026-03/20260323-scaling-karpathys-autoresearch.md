# Scaling Karpathy’s Autoresearch
**Source**: https://blog.skypilot.co/scaling-autoresearch/
**Date**: March 23, 2026
**Author**: Unknown
**Keywords**: autoresearch, SkyPilot, Claude Code, GPUs, parallel experiments

## Elevator pitch
SkyPilot shows how giving Karpathy’s autoresearch agent a 16‑GPU cluster radically ускорates experiment throughput and improves model quality faster than sequential runs.

## Takeaways
- Parallel GPU clusters let the agent run factorial experiment grids instead of sequential trials.
- A 16‑GPU setup ran ~910 experiments in ~8 hours, achieving a 2.87% val_bpb improvement.
- The agent learned to exploit heterogeneous GPUs (H100 for screening, H200 for validation).
- Scaling changed the search strategy, surfacing interaction effects faster.
- SkyPilot’s YAML workflow enabled automated provisioning and pipelining across clusters.

## Synthesis
This SkyPilot post describes what happens when an autonomous research agent is given serious compute resources. Using Andrej Karpathy’s autoresearch project—which iteratively edits a training script, runs a fixed‑budget training run, and keeps changes that improve validation loss—the team scaled the workflow from one GPU to a 16‑GPU cluster. The result was a dramatic increase in throughput and a different style of search behavior.

In the baseline setup, the agent is limited by sequential experiments: one edit, one training run, one evaluation at a time. This creates a greedy hill‑climbing loop where each experiment is dependent on the previous one. By contrast, with 16 GPUs the agent can execute factorial grids of experiments in parallel. This unlocks interaction effects that would take hours or days to uncover sequentially, because multiple parameters can be tested in the same wave.

The reported run used SkyPilot to provision clusters across Kubernetes, with YAML definitions specifying GPU type, dependencies, and run commands. The agent ran roughly 910 experiments in eight hours, achieving a 2.87% improvement in validation bits per byte (val_bpb). It also learned to exploit heterogeneous hardware by screening ideas on cheaper H100 GPUs and validating winners on H200s, effectively optimizing both speed and cost. This emergent strategy shows that agents can adapt their workflows when they have visibility into available resources.

The post details the phases of the search: initial hyperparameter sweeps, architecture scaling (where model width dominated other knobs), fine‑tuning, optimizer tweaks, and diminishing‑returns exploration. The biggest gains came from parallel testing of model widths, which would have been prohibitively slow in a single‑GPU setting. The takeaway is not just more experiments per hour, but faster identification of the highest‑impact changes.

SkyPilot’s role is to abstract the cloud infrastructure: the agent uses the SkyPilot skill and YAML definitions to spin up clusters, submit jobs, and fetch logs. This suggests a new pattern for autonomous research—agents that can manage their own compute fleets, iterate rapidly, and optimize experiments without human intervention at the infrastructure layer.

Overall, the case study argues that compute parallelism fundamentally changes the behavior of autonomous research agents. With enough GPUs, agents shift from sequential trial‑and‑error to parallel hypothesis testing, revealing interactions and accelerating progress. The implication is that infrastructure—not just model capability—will determine how far these systems can push research workflows.
