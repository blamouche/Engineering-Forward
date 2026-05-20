# model half-life
**Source**: https://aifoc.us/model-half-life/
**Date**: May 18, 2026
**Author**: Paul Kinlan
**Keywords**: model release cadence, AI labs, half-life, frontier models, release frequency, predictions

## Elevator pitch
Paul Kinlan empirically challenges the "model half-life" buzzword by analyzing release dates across 12 AI labs, showing that while model release frequency has increased, the claimed halving-time narrative doesn't hold up to the data.

## Takeaways
- Kinlan compiled a TSV dataset of every headline model release from late 2022 through May 2026 across all major US and Chinese frontier labs, split by model sub-series (Opus vs Sonnet, GPT vs o-series, etc.).
- The analysis uses median gap calculation over trailing three releases to predict next drops — a "naive heuristic" that tracks current cadence rather than long-run averages.
- The term "model half-life" is characterized as a buzzword: release frequency has ticked up but isn't halving every six months as the phrase implies.
- Prediction confidence is low for series with few data points (e.g., GPT OSS predicted for end of 2027 is speculative at best).
- The dataset is open-source and verifiable, compiled initially by Claude and being manually audited against vendor announcements, Hugging Face, and Wikipedia.
- The post provides a reproducible methodology for tracking AI release cadence over time, with plans to re-run the analysis periodically.

## Synthesis
Paul Kinlan's "model half-life" post is a refreshingly empirical counterweight to a phrase that has spread through AI discourse with little supporting evidence. The claim that model release cadence is halving — implying some exponential acceleration toward daily or hourly drops — sounds compelling but crumbles under Kinlan's spreadsheet-first approach.

The analysis tracks 12 major AI labs (6 US, 6 Chinese) from late 2022 through May 2026, splitting releases by sub-series to account for the fact that Claude Opus and Claude Sonnet follow different schedules. The methodology is deliberately simple: sort releases chronologically, compute gaps, take the median of the trailing three, and project forward. Kinlan is transparent about its limitations — single-drop series get no prediction, and the trailing-three approach means predictions reflect current pace rather than historical averages.

The conclusion is measured: releases have accelerated, but the "half-life" framing is misleading. The data shows an uptick, not a halving curve. Where the term captures something real is that models now ship months apart rather than years apart — but that's a one-time shift in industry cadence, not an ongoing exponential compression.

The open approach to the data is notable. The TSV was initially compiled by Claude (an AI assistant) but is being manually verified against vendor sources, with corrections accepted from the community. This hybrid human-AI verification workflow is itself a small case study in how AI tools can accelerate research without replacing judgment.

For anyone tracking the AI industry, Kinlan's dataset and methodology provide a useful baseline. The real insight may be less about when the next model drops and more about what "release" means when models are continuously improved and capabilities are rolled out incrementally rather than in discrete version bumps.
