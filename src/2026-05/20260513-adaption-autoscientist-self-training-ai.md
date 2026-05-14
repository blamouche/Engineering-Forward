# Adaption aims big with AutoScientist, an AI tool that helps models train themselves
**Source**: https://techcrunch.com/2026/05/13/adaption-aims-big-with-autoscientist-an-ai-tool-that-helps-models-train-themselves
**Date**: May 13, 2026
**Author**: Russell Brandom
**Keywords**: Adaption, AutoScientist, self-training, fine-tuning, AI research, Sara Hooker, automated machine learning, neolabs

## Elevator pitch
Adaption, founded by ex-Cohere VP Sara Hooker, launched AutoScientist — a tool that co-optimizes both data and models to automate fine-tuning, potentially enabling successful frontier AI training beyond the largest labs.

## Takeaways
- AutoScientist automates conventional fine-tuning by co-optimizing both training data and the model simultaneously
- Adaption claims the system has more than doubled win rates across different models, though standard benchmarks don't apply due to the task-specific nature
- The tool builds on Adaption's existing "Adaptive Data" product, creating a loop where improving datasets yield continuously improving models
- CEO Sara Hooker sees this as enabling frontier AI training outside the dominant labs, similar to how code generation unlocked diverse applications
- AutoScientist is free for the first 30 days after release, signaling Adaption's confidence in user adoption

## Synthesis
On May 13, 2026, Adaption — a research-focused AI lab founded by former Cohere VP of AI Research Sara Hooker — introduced AutoScientist, a tool designed to automate and accelerate the process of training AI models for specific capabilities. The launch represents a significant milestone in the pursuit of self-improving AI systems, an idea long anticipated by researchers but only now becoming practical through dedicated commercial products.

The core innovation of AutoScientist is what Hooker describes as "co-optimization" — the system simultaneously optimizes both the training dataset and the model parameters, learning the most effective way to acquire any given capability. This departs from the traditional fine-tuning pipeline where datasets are curated manually by human engineers before being fed into a static training process. Instead, AutoScientist treats the data and the model as two sides of the same optimization problem, dynamically adjusting both as it iterates toward better performance.

AutoScientist builds on Adaption's existing "Adaptive Data" product, which helps organizations construct high-quality datasets that improve over time. The new tool closes the loop: Adaptive Data produces increasingly better datasets, and AutoScientist converts those improved datasets into improved models. Hooker's vision is a "completely adaptable" stack that optimizes on the fly for whatever task is at hand, reducing the dependency on large-scale pretraining runs that only the wealthiest labs can afford.

The performance claims are striking — Adaption reports more than doubled win rates across different models tested. However, these numbers are difficult to contextualize because AutoScientist is optimized for task-specific adaptation rather than general benchmarks like SWE-Bench or ARC-AGI. The tool's value proposition is not "a better general-purpose model" but rather "a dramatically better specialized model for your specific use case."

Strategically, AutoScientist positions Adaption in the emerging "neolab" category — startups that don't just build applications on top of existing models but push the frontier of AI research itself, competing with the likes of Anthropic and OpenAI on fundamental capabilities. Hooker frames the tool as a democratizing force: "It suggests we can finally allow for successful frontier AI trainings outside of these labs." By making the tool free for 30 days, Adaption is betting that once users experience automated self-improvement, they'll integrate it into their core workflows — potentially reshaping who can participate in cutting-edge AI development.
