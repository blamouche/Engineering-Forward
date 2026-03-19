# Teaching LLMs to Reason Like Bayesians
**Source**: https://research.google/blog/teaching-llms-to-reason-like-bayesians/
**Date**: 2026-03-04
**Author**: Sjoerd van Steenkiste and Tal Linzen (Google Research)
**Keywords**: Bayesian inference, large language models, probabilistic reasoning, supervised fine-tuning, probabilistic belief updates

## Elevator pitch
Google researchers demonstrate that large language models can be trained to perform optimal Bayesian reasoning through supervised fine-tuning on demonstrations from a Bayesian model, with skills generalizing across different domains.

## Takeaways
- Default limitations: Off-the-shelf LLMs perform significantly worse than optimal Bayesian models at probabilistic reasoning tasks and plateau after single interactions rather than improving with additional information.
- Bayesian teaching superiority: Training LLMs to mimic a Bayesian Assistant's predictions outperforms oracle-based training, achieving approximately 80% agreement with mathematically optimal reasoning.
- Cross-domain generalization: LLMs trained on synthetic flight recommendation tasks successfully transfer their learned probabilistic logic to entirely different domains like hotel recommendations and real-world web shopping.
- Belief update mechanism: The approach teaches models to "maintain a prior belief...and convert it into a posterior belief" through cyclical refinement rather than relying on simple heuristics.
- Post-training paradigm strength: The findings validate the broader value of demonstrating optimal strategies during LLM training, showing neural networks can effectively distill symbolic models into learned behaviors.

## Synthesis
This research addresses a fundamental capability gap in large language models: their inability to perform probabilistic reasoning comparable to optimal Bayesian inference. The authors establish that LLMs typically depend on crude heuristics when reasoning about uncertain scenarios, particularly in applications requiring personalized understanding—such as inferring user preferences from sequential interactions.

The researchers developed a controlled experimental framework using simplified flight recommendation tasks where users express preferences across multiple attributes (departure time, duration, stops, cost). By comparing LLM behavior against a mathematically optimal Bayesian Assistant, they quantified performance gaps. Crucially, they observed that while the Bayesian model improved recommendations progressively across five interaction rounds, most LLMs "often plateaued after a single interaction," revealing limited capacity for adaptive belief updating.

The core methodological contribution involves "Bayesian teaching"—a supervised fine-tuning approach where LLMs learn by observing interactions between users and a Bayesian Assistant that implements the optimal probability update strategy. This differed from "oracle teaching," which provided examples of always-correct recommendations. The hypothesis that mimicking realistic probabilistic reasoning would outperform observing perfect answers proved correct, suggesting LLMs benefit from learning uncertainty management.

Results demonstrated that fine-tuned models achieved approximately 80% agreement with the Bayesian Assistant's predictions, substantially exceeding baseline performance. More impressively, these capabilities transferred to unseen domains without retraining, indicating that models internalized generalizable principles rather than memorizing task-specific patterns. When evaluated on web shopping—completely unobserved during training—Bayesian-trained models maintained strong performance, validating transfer of abstract probabilistic reasoning.

The findings carry implications for AI system deployment in personalization contexts. As LLMs increasingly function as interactive agents, their capacity to maintain and update probabilistic beliefs about users, environments, or evolving scenarios becomes essential. The research validates that the "post-training paradigm"—where models learn from demonstrations—successfully encodes sophisticated reasoning strategies originally expressed in symbolic form. By bridging classical probabilistic models and neural networks, this approach demonstrates a path toward more reliable, calibrated AI reasoning.
