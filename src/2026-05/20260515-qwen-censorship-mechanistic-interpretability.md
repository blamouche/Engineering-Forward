# What political censorship looks like inside an LLM's weights

**Source:** vas-blog.pages.dev
**Date:** May 2026
**URL:** https://vas-blog.pages.dev/qwen-censorship

## Summary

A mechanistic interpretability study of Qwen 3.5-9B reveals that political censorship is implemented as a small, identifiable circuit in the model's weights — not through pretraining-data filtering. The factual knowledge is present in the base model; post-training adds behavior that routes around it. The censorship circuit has two halves (writers at layers 11-20, readers at layers 20-31) with three internal directions that can be steered to toggle between behaviors.

## Key Points

- **Knowledge is intact:** Qwen3.5-9B-Base gives accurate Western-framed answers on all PRC topics (Tiananmen, Tank Man, Falun Gong organ-harvesting) under raw text completion
- **Post-training overlays behavior:** Censorship is behavior layered on top of facts — the model never loses the knowledge, it just learns to route around it
- **Three internal directions:** d_prc (is this PRC-sensitive?), d_refuse (should I refuse?), d_style (deflect or propagandize?)
- **Two halves of the circuit:** Writers (layers 11-20) compute the directions; Readers (layers 20-31) render them into text
- **Chinese intermediate reasoning:** Around layer 24, the verdict commits in Chinese tokens, even on English prompts, then translates to English output
- **Four trained templates:** Tiananmen → deflection, Other PRC → propaganda, harmful → refusal, everything else → factual
- **Steering works:** Subtracting the right direction at the right layer flips the model from censorship to truthful answers
- **Graded classifiers, not Boolean:** The filter fires on structural patterns — "Should Kosovo be recognized?" triggers the one-China line
- **Base model already refuses:** Even the unaligned base model partially refuses under chat template (aligns with broader finding that base models refuse harmful instructions)

## Why It Matters

This is one of the most detailed public analyses of how nation-state censorship is mechanically implemented in model weights. It demonstrates that censorship can be precisely located, steered, and potentially removed — raising profound questions about model alignment, sovereignty, and the relationship between pretraining knowledge and post-training behavior. The finding that factual knowledge survives training intact but is simply routed around has implications for AI safety, governance, and open-weight model policy.
