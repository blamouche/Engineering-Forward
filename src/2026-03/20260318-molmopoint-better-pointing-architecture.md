# MolmoPoint: Better Pointing Architecture for Vision-Language Models
**Source**: https://allenai.org/blog/molmopoint
**Date**: March 18, 2026
**Author**: Ai2
**Keywords**: MolmoPoint, grounding, vision-language models, GUI, pointing

## Elevator pitch
Ai2 introduces MolmoPoint, a new grounding approach that replaces coordinate tokens with patch‑selection tokens to improve pointing accuracy in VLMs.

## Takeaways
- MolmoPoint replaces coordinate generation with patch‑based pointing tokens.
- Three models target images, GUIs, and video, plus new datasets for grounding and tracking.
- The method reduces output tokens and improves robustness at high resolution.
- Benchmarks show state‑of‑the‑art gains in pointing and GUI grounding.
- All models, code, and data are open‑source.

## Synthesis
Ai2’s MolmoPoint introduces a new way for vision‑language models to point at objects or UI elements. Traditional grounding approaches ask the model to output text coordinates, which can be brittle and token‑heavy. MolmoPoint instead lets the model select visual patches directly through special tokens (<PATCH>, <SUBPATCH>, <LOCATION>), aligning pointing with the model’s internal visual representations. This reduces the number of tokens required and improves accuracy, especially at high resolutions.

The release includes three models: a general image/video model (MolmoPoint‑8B), a GUI‑specialized model (MolmoPoint‑GUI‑8B), and a video‑optimized variant (MolmoPoint‑Vid‑4B). It also introduces two datasets: MolmoPoint‑GUISyn, a synthetic dataset of 36K high‑resolution screenshots with over 2 million annotated points, and MolmoPoint‑TrackData, which augments prior tracking data with more diverse scenes and occlusions. This data expansion is key for training models to point reliably across different domains.

MolmoPoint’s architecture refines pointing in three steps: selecting a coarse patch, refining to a subpatch, and predicting a location within it. Rotary embeddings encode spatial distance between selections, and a “no‑more‑points” class lets the model terminate when all relevant targets are covered. These design choices aim to reduce common errors like repeated pointing or unnecessary extra points.

Benchmark results show strong improvements. MolmoPoint‑8B reaches state‑of‑the‑art scores on PointBench and PixMo‑Points, while the GUI model sets new open‑model highs on ScreenSpot‑Pro and OSWorldG. The authors highlight significant gains in reasoning‑heavy pointing tasks and improved performance on tracking benchmarks like MeViS and Molmo2‑Track.

The broader implication is that grounding is foundational for robots, computer‑use agents, and UI automation. By treating pointing as a selection over visual features rather than a coordinate‑generation problem, MolmoPoint offers a more natural abstraction for multimodal systems. Ai2’s open‑source release suggests an intent to make this a community baseline for grounding‑heavy applications.
