# How NVIDIA Builds Open Data for AI
**Source**: https://huggingface.co/blog/nvidia/open-data-for-ai
**Date**: 2026-03-10
**Author**: Will Jennings, Yev Meyer, Leanna Chraghchian, Rebecca Kao, Jane Polak Scowcroft, Annie Surla
**Keywords**: NVIDIA, open data, datasets, Nemotron, robotics, AI training, pre-training, RAG, open source AI, Hugging Face

## Elevator pitch
NVIDIA has released 2+ petabytes across 180+ datasets and 650+ open models, framing open data as shared infrastructure that addresses the data bottleneck constraining AI development across industries.

## Takeaways
- The data bottleneck is a primary constraint on AI adoption: organizations spend millions and 1+ years on data collection, annotation, and validation before training can begin.
- NVIDIA's open releases include 500K+ robotics trajectories (15TB), 1,700 hours of autonomous vehicle sensor data from 25 countries, 41M+ synthetic personas, and 455K protein structures for drug discovery.
- Nemotron-ClimbMix (400B tokens) optimizes pre-training data composition, achieving a 33% H100 speedup and the largest improvement on the Time-to-GPT-2 leaderboard.
- Real-world impact: CrowdStrike improved NL→CQL accuracy from 50.7% to 90.4% with 2M personas; NTT Data improved legal QA accuracy from 15.3% to 79.3%.
- NVIDIA's "extreme co-design" approach crosses data strategists, AI researchers, infrastructure engineers, and policy experts to build datasets that work in practice rather than just in benchmarks.

## Synthesis
NVIDIA's open data strategy makes sense as competitive infrastructure play: releasing datasets and training recipes builds ecosystem dependency on NVIDIA's hardware stack. Every team that trains on ClimbMix, fine-tunes with Nemotron Personas, or benchmarks with SPEED-Bench is doing so on NVIDIA GPUs. Open data creates gravitational pull toward the hardware without requiring proprietary data lock-in.

The data bottleneck framing is accurate and underappreciated. The public discourse about AI progress focuses heavily on model architecture and compute; data quality and availability constrain practical deployment in ways that benchmarks don't capture. A model that performs well on standard benchmarks can fail dramatically when applied to a domain—legal documents, medical imaging, industrial sensor data—where training-appropriate data is scarce or expensive to annotate.

The domain-specific releases reflect where this bottleneck is most acute. Robotics trajectory data is genuinely scarce because collection requires physical robots operating in real environments. Protein structures require specialized knowledge to validate. Autonomous vehicle sensor data requires expensive multi-sensor rigs in diverse geographic conditions. By releasing in these high-friction domains, NVIDIA creates more leverage than releasing general-purpose text datasets that organizations could build themselves.

The Nemotron-ClimbMix compute efficiency result is particularly notable. A 33% H100 speedup from pre-training data composition optimization means that data engineering and hardware utilization are deeply coupled—optimizing the data directly optimizes the hardware economics. This makes NVIDIA's data research a direct extension of its hardware business in a way that goes beyond traditional ecosystem building.
