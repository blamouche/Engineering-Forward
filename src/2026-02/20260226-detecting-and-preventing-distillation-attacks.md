# Detecting and preventing distillation attacks
**Source**: https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks
**Date**: 2026-02-26
**Author**: Anthropic
**Keywords**: model security, distillation, API abuse, export controls, AI governance

## Elevator pitch
Anthropic reports large-scale campaigns by three AI labs to illicitly distill Claude via thousands of fraudulent accounts, argues this weakens safeguards and export controls, and outlines detection, access controls, and industry coordination as countermeasures.

## Takeaways
- Anthropic attributes industrial-scale distillation campaigns to DeepSeek, Moonshot, and MiniMax, totaling ~16M+ exchanges.
- Illicit distillation risks stripping safety guardrails and accelerating proliferation of dual-use capabilities.
- Distillation abuse intersects with export controls: it can make foreign progress look “organic” while actually depending on stolen capability.
- Attack patterns are behavioral: high-volume, repetitive prompt structures targeting high-value capabilities (tool use, coding, reasoning).
- Defenses span traffic fingerprinting, coordinated intelligence sharing, tightened verification, and model/product countermeasures.

## Synthesis
This post is a rare, concrete disclosure about competitive model “distillation” in the wild. Anthropic claims it identified and disrupted campaigns by three named labs—DeepSeek, Moonshot (Kimi), and MiniMax—attempting to extract Claude’s capabilities at scale. The reported mechanism is not a single clever exploit but a supply chain of fraud: thousands of fake accounts, proxy infrastructure (“hydra cluster” architectures), and coordinated traffic designed to evade detection while generating large training corpora.

Anthropic is careful to distinguish legitimate distillation (e.g., distilling your own frontier model into smaller, cheaper variants) from illicit distillation that violates access restrictions and terms of service. The company’s argument for why this matters goes beyond business competition: it frames the key harm as safety regression. If a competitor trains on Claude outputs without inheriting Claude’s safety systems, then capabilities can propagate while safeguards are lost—especially if the resulting models are open-sourced or integrated into sensitive government and surveillance systems.

A second theme is policy. Anthropic links distillation attacks to the debate over compute export controls: if foreign labs can “catch up” partly by siphoning outputs from US models, progress may be misinterpreted as evidence that export controls are ineffective. Anthropic argues the opposite: at-scale distillation still requires substantial infrastructure and advanced chips, and therefore reinforces the rationale for restricting access.

Operationally, the post provides a practitioner’s mental model for detection: look for patterns that differ from organic use—massive volume, narrow capability targeting (agentic reasoning, tool use, coding), and high repetition with structured prompt templates. Anthropic says it is responding with classifiers and behavioral fingerprinting, cross-industry intelligence sharing, tighter identity verification for commonly abused pathways (including educational accounts), and countermeasures that reduce the usefulness of outputs for distillation without harming legitimate customers.

Overall, the piece treats “model security” as a fast-moving adversarial domain, where technical defenses and governance need to be coordinated, not siloed.