# Adaption aims big with AutoScientist, an AI tool that helps models train themselves
**Source**: https://techcrunch.com/2026/05/13/adaption-aims-big-with-autoscientist-an-ai-tool-that-helps-models-train-themselves/
**Date**: May 13, 2026
**Author**: Russell Brandom
**Keywords**: AutoScientist, self-training, fine-tuning, AI neolab, adaptive data

## Elevator pitch
Adaption's AutoScientist automates AI fine-tuning by co-optimizing data and models, enabling frontier-level training outside of major AI labs.

## Takeaways
- AutoScientist co-optimizes both training data and model parameters simultaneously, learning the best way to acquire any target capability
- Adaption claims more than doubled win rates across different models in internal testing, though conventional benchmarks don't apply
- The tool is free for the first 30 days after launch, signaling confidence in user adoption
- CEO Sara Hooker (ex-Cohere VP of AI Research) positions this as a way to democratize frontier AI training beyond the major labs
- Builds on Adaption's existing Adaptive Data product, creating a pipeline where continuously improving datasets produce continuously improving models

## Synthesis
Adaption, a research-driven AI neolab founded by former Cohere VP of AI Research Sara Hooker, has unveiled AutoScientist, a tool designed to automate and accelerate the process of fine-tuning AI models for specific capabilities. The announcement, covered by TechCrunch's Russell Brandom on May 13, 2026, marks a significant step toward the long-anticipated goal of AI systems that can improve themselves more effectively than human-directed training alone.

The core innovation of AutoScientist lies in its approach to co-optimization. Unlike conventional fine-tuning, which typically involves manually curating datasets and then training models on them, AutoScientist simultaneously optimizes both the data and the model. This means the system learns not just what to learn, but how to learn it most effectively for any given capability. Hooker describes it as a system where "the whole stack should be completely adaptable" and optimizes on the fly for whatever task is at hand.

AutoScientist builds upon Adaption's earlier product, Adaptive Data, which focused on making it easier to build high-quality datasets that improve over time. AutoScientist closes the loop by taking those continuously improving datasets and translating them into continuously improving models. This creates a virtuous cycle where better data leads to better models, which in turn can help generate better data.

The company reports that AutoScientist has more than doubled win rates across different models in internal evaluations. However, these numbers are difficult to benchmark against industry standards because the system is designed for task-specific adaptation rather than general-purpose benchmarks like SWE-Bench or ARC-AGI. This highlights both the strength and the limitation of the approach: it excels at targeted capability improvement but doesn't necessarily translate to broad, generalized intelligence gains.

Adaption's broader mission is to democratize frontier AI training. Hooker explicitly frames AutoScientist as enabling "successful frontier AI trainings outside of these labs," challenging the concentration of cutting-edge model development within a handful of well-resourced organizations. The 30-day free launch period reflects an aggressive go-to-market strategy aimed at proving value quickly.

The context for this launch is a rapidly growing ecosystem of AI neolabs — research-focused startups backed by significant venture capital — that are betting against the pure scaling hypothesis. Rather than simply increasing model size and data volume, these labs are pursuing smarter, more efficient training methodologies. AutoScientist represents a concrete product manifestation of this philosophy: instead of scaling brute-force computation, it scales the intelligence of the training process itself.

If successful, AutoScientist could reshape the economics of AI development by lowering the barrier to creating specialized, high-performing models. In fields from scientific research to enterprise applications, the ability to rapidly fine-tune models for specific domains without requiring the resources of a major AI lab could accelerate innovation significantly. The key question remains whether the claimed performance improvements hold up in real-world deployments across diverse use cases.
