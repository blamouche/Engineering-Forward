# Data for Agents: NVIDIA's Open Data Initiative for Agentic AI
**Source**: https://huggingface.co/blog/nvidia/open-data-for-agents
**Date**: 2026-07-08
**Author**: NVIDIA / HuggingFace
**Keywords**: NVIDIA, Nemotron, open data, synthetic data, AI agents, agentic AI, data curation, HuggingFace

## Elevator pitch
NVIDIA and HuggingFace release open datasets for training agentic AI, arguing that open weights alone aren't enough—reproducible, inspectable agent behavior requires open data, training recipes, and evaluation methods.

## Takeaways
- NVIDIA's open data initiative argues that for agents, open weights are only part of the story: reproducibility also depends on datasets, curation choices, training recipes, and evaluation methods.
- Synthetic data is the key scaling mechanism: Nemotron-CC used synthetics to enhance Common Crawl for pretraining, Nemotron-CC-MATH leverages synthetic math questions for reasoning, and Nemotron Pretraining spans general, code, math, and synthetic data across trillions of tokens.
- Agent behavior needs to be inspectable—if a model calls tools, executes workflows, and acts across systems, developers need to understand the data that shaped those behaviors.
- Nearly 145 papers at ICML cite Nemotron models and datasets, demonstrating that open data drives broader research progress.
- NVIDIA's VP Bryan Catanzaro emphasizes that "every company is built around a secret"—synthetic data gives teams a way to preserve useful signals without exposing underlying sources.

## Synthesis
NVIDIA and HuggingFace's "Data for Agents" blog post makes a fundamental argument: the AI ecosystem's focus on open model weights is necessary but insufficient for the agent era. If agents are going to call tools, execute workflows, retrieve information, and act across systems, then understanding the data that shaped those behaviors is just as important as understanding the model architecture.

The practical contribution is a series of open datasets under the Nemotron brand. Nemotron-CC enhances Common Crawl with synthetic data for pretraining. Nemotron-CC-MATH adds synthetic math questions to improve reasoning. Nemotron Pretraining is a broad collection spanning general, code, math, and synthetic data across trillions of tokens. Each addresses a different gap in the open data landscape.

The philosophical argument is perhaps more important than any individual dataset. When every model trains on the same narrow pool of data, the models start to feel the same. Synthetic data—carefully generated to preserve useful signals without exposing proprietary sources—offers a path to diversity without leakage. NVIDIA's Catanzaro frames this as both a practical and ecosystem concern: companies shouldn't casually expose their competitive secrets, but they can share synthetic representations that capture the essence without revealing the underlying data.

For the agent community specifically, the post argues that agent behavior must be inspectable. If a model decides to call a particular API or follow a particular workflow, developers need to trace that decision back to training data. Open data makes this possible in a way that proprietary data never can. The 145+ ICML papers citing Nemotron models and datasets suggest the research community is already finding this valuable.

The broader signal for engineering teams: as you build agents, pay attention to what data shaped their tool-use behavior. The open data movement is making it possible to build on transparent foundations rather than black boxes.