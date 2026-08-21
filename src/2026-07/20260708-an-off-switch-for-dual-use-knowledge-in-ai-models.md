# An Off Switch for Dual-Use Knowledge in AI Models
**Source**: https://www.anthropic.com/research/off-switch-dual-use
**Date**: 2026-07-08
**Author**: Anthropic / AE Studio
**Keywords**: Anthropic, GRAM, dual-use knowledge, AI safety, modular pretraining, model editing, alignment

## Elevator pitch
Anthropic introduces GRAM (Gradient-Routed Auxiliary Modules), a technique that trains dual-use knowledge into removable compartments within a model, enabling a single training run to produce 16 different capability configurations.

## Takeaways
- GRAM adds extra neurons to every transformer layer, divided into modules for each dual-use category (e.g., virology, cybersecurity, nuclear physics), so that knowledge accumulates in specific compartments rather than diffusing across the network.
- When the model encounters dual-use data, only the corresponding module is allowed to learn—general-purpose weights are frozen—meaning deleting a module removes the capability almost as effectively as never having trained on that data.
- A single GRAM training run with four dual-use categories yields a model configurable 16 different ways (on/off for each category), replacing the need to train 16 separate filtered models.
- GRAM resists fine-tuning attacks about as well as data filtering, while unlearning techniques applied after training only suppress knowledge and can be easily restored with small amounts of malicious data.
- Tested across seven model sizes (50M to 5B parameters), GRAM matched data filtering at every size, and the gap between "module on" and "module off" grew wider as models got larger.

## Synthesis
Anthropic's latest alignment research tackles one of AI safety's hardest problems: how to limit access to dual-use knowledge without crippling general capabilities. Current safeguards—refusal training and input/output classifiers—don't change the knowledge stored in the model. A determined attacker can jailbreak past them. Previous work on pretraining data filtering produces one model with one fixed set of capabilities; if you need a model that can discuss virology for a vetted biosecurity lab and another that can't, you have to train two separate models.

GRAM offers a more elegant solution. By routing dual-use knowledge into dedicated, removable compartments during training, a single model can be configured for different deployment contexts. Delete the cybersecurity module and the capability goes with it; leave it in for trusted deployments. The technique works by adding auxiliary neurons to every transformer layer, grouped by dual-use category. When training encounters general text, all weights learn normally. When it encounters, say, virology text, only the virology module updates—the general weights stay frozen. This compartmentalization means knowledge doesn't diffuse throughout the network.

The experimental results are encouraging. On a realistic mix of web text, code, and scientific papers with four dual-use domains, removing a module reduced the corresponding capability about as effectively as never having trained on that data, without degrading general performance. The approach also resists fine-tuning attacks as well as data filtering, which is notable because post-hoc unlearning proved much more vulnerable—a small amount of malicious training data could restore the suppressed knowledge.

The caveats are important: GRAM hasn't been applied to any production Claude models, evaluations measure next-token prediction ability rather than real downstream task performance, and there's a deeper open problem around dual-use capabilities so entangled with general knowledge that no method can separate them cleanly. Still, as a research direction, GRAM represents a meaningful advance in the toolbox for building models that can be precisely configured for different safety contexts.