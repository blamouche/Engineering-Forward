# OlmoEarth v1.1: A more efficient family of Earth observation models
**Source**: https://huggingface.co/blog/allenai/olmoearth-v1-1
**Date**: May 19, 2026
**Author**: Allen AI (Ai2)
**Keywords**: OlmoEarth, remote sensing, Earth observation, satellite imagery, transformer efficiency, AI2, climate AI

## Elevator pitch
AI2 releases OlmoEarth v1.1, a family of Earth observation models that reduces compute costs by up to 3x compared to v1 while maintaining performance, achieved by redesigning how satellite imagery is tokenized for transformer processing.

## Takeaways
- Compute costs scale quadratically with token sequence length in transformers, making tokenization design the key lever for efficiency in remote sensing models.
- OlmoEarth v1.1 merges multi-resolution Sentinel-2 band tokens into a single token — reducing token count by 3x — without performance loss thanks to modified pretraining.
- Naively merging resolution tokens caused a 10 percentage point drop on m-eurosat kNN; overcoming this required changes to the pretraining regimen detailed in the paper.
- The model family comes in Base, Tiny, and Nano sizes, allowing users to match compute budgets; v1.1 runs up to 3x cheaper at every size.
- Trained on the same dataset as v1 to isolate methodological improvements, the release doubles as a scientific contribution for studying pretraining design choices in remote sensing.
- Real-world deployments span mangrove tracking, forest loss classification, and country-scale crop-type mapping, with efficiency gains directly expanding the platform's partner capacity.

## Synthesis
AI2's OlmoEarth v1.1 is a study in applied efficiency. Rather than scaling up model size or data, the team attacked the cost problem at the architectural level: token sequence length. In transformer-based models, compute scales quadratically with sequence length, so reducing tokens is disproportionately valuable. The insight was that Sentinel-2 satellite imagery produces 3 resolution-dependent tokens per timestep per patch (10m, 20m, 60m) — merging these into a single token would cut token count by two-thirds, but naively doing so degraded performance by 10 points on a standard benchmark.

The solution required rethinking pretraining, not just inference. By modifying the pretraining regimen to preserve cross-band relationships that the model previously learned from separated tokens, the team achieved efficiency parity — same performance, 3x fewer tokens, 3x lower compute. The methodological transparency is notable: training on the same dataset as v1 isolates the effect of tokenization changes, making this both a product release and a reproducible scientific contribution.

The practical implications are significant for climate and environmental applications. OlmoEarth is used to track mangrove change, classify forest loss drivers, and produce crop-type maps at country scale. Compute is the dominant cost across the full lifecycle (data export, preprocessing, inference, post-processing), so a 3x efficiency gain directly translates to more partners served, larger areas mapped, and more frequent updates — all on the same infrastructure budget.

This release exemplifies a broader trend in AI: the most impactful improvements aren't always bigger models, but smarter architectures that make existing capabilities more accessible and sustainable. For the Earth observation community specifically, cheaper inference means democratized access to planetary-scale monitoring.
