# Better Experiments with LLM Evals — A Funnel, Not a Fork
**Source**: https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork
**Date**: 2026-05-18
**Author**: Matilda Ankargren, Mårten Schultzberg (Spotify)
**Keywords**: Spotify, LLM evals, experimentation, A/B testing, evaluation funnel, offline evaluation, guardrail metrics, calibration

## Elevator pitch
Spotify's experimentation team presents a framework where LLM evals and online A/B tests form a funnel rather than competing alternatives — evals verify implementation quality and filter candidates before experiments, while experiments validate real user impact, with a continuous calibration loop that makes both smarter over time.

## Takeaways
- Only 12% of Spotify's A/B tests ship a positive result; 64% produce valid learning (regressions caught, hypotheses refined)
- LLM evals can now assess dimensions like relevance, coherence, tone, and intent alignment at scale — previously only feasible with expensive human annotation
- Key distinction: evals verify (does the output conform to quality standards?), experiments validate (do real users respond as predicted?)
- Evals filter non-promising candidates before they consume experiment bandwidth, raising the hit rate of what reaches A/B tests
- 42% of launched experiments are rolled back at Spotify due to secondary metric regressions that no eval caught — proving offline evaluation alone is insufficient

## Synthesis
Spotify's data science team offers one of the most pragmatic frameworks yet for integrating LLM-based evaluation into production ML workflows. Drawing on their extensive experimentation culture and the theoretical work of Schultzberg and Ottens (2024), they argue that the relationship between LLM evals and A/B tests isn't competitive — it's sequential.

The core insight is that evals and experiments measure fundamentally different things. Evals verify implementation quality: did the change produce the intended output? Experiments validate business impact: did real users respond as predicted? The "funnel" model places evals before experiments, filtering out non-promising candidates and generating hypotheses about what to improve. Only after an eval passes does a change reach the experiment stage, where guardrail metrics protect against regressions in unmeasured dimensions.

The calibration challenge is the most valuable part of the framework. LLM judges are proxies — they substitute a score for an outcome — and that substitution requires validation. The authors describe a two-layer calibration problem: first, the eval score must track online outcomes (like any proxy metric), and second, the LLM judge's qualitative assessments must map to real user behavior. The calibration loop runs both directions: experiments validate whether the eval-preferred variant actually performed better, and gaps between eval scores and experiment outcomes become "diagnostic gold" that improves the next generation of judges.

The sobering data point — 42% of launched experiments are rolled back due to secondary metric regressions that no eval detected — underscores that evals are complements to, not replacements for, online experimentation. As AI systems become more complex, the combination of cheap, scalable evals for filtering and rigorous experiments for validation becomes the rational default for any organization shipping LLM-powered features.
