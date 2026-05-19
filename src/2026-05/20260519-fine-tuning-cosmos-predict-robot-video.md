# Fine-Tuning NVIDIA Cosmos Predict 2.5 with LoRA/DoRA for Robot Video Generation

**Source:** https://huggingface.co/blog/nvidia/cosmos-fine-tuning-for-robot-video-generation
**Date:** 2026-05-18

## Summary

NVIDIA provides a practical guide for fine-tuning Cosmos Predict 2.5, a 2B-parameter world model, for robot video generation using parameter-efficient techniques (LoRA/DoRA). The approach addresses the expensive and slow process of collecting real-robot demonstration data by generating synthetic trajectories instead. Key technical details:

- LoRA adapters are injected into the DiT's attention projections (to_q, to_k, to_v, to_out.0) and feedforward layers
- DoRA can be swapped in for magnitude+direction decomposition of weight updates
- Uses rectified flow training with logit-normal timestep sampling
- Requires at minimum one 80GB GPU; 8× H100s recommended for faster iteration
- Training datasets: GR1-100 (92 robot manipulation videos) and PhysicalAI-Robotics-GR00T-Eval (50 test pairs)

This represents the growing convergence of world models and robotics, making robot policy training more accessible through synthetic data generation.

**Tags:** #robotics #world-models #nvidia #fine-tuning #synthetic-data #video-generation
