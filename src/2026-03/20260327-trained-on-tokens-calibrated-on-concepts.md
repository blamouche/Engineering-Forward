# Trained on Tokens, Calibrated on Concepts: The Emergence of Semantic Calibration in LLMs
**Source**: https://machinelearning.apple.com/research/trained-on-tokens
**Date**: Unknown
**Author**: Preetum Nakkiran, Arwen Bradley, Adam Goliński, Eugene Ndiaye, Michael Kirchhof, Sinead Williamson
**Keywords**: calibration, confidence, LLMs, uncertainty, semantic evaluation

## Elevator pitch
Apple researchers show that base LLMs can be semantically calibrated—meaning their confidence aligns with correctness at the level of meaning—while RL instruction‑tuning and chain‑of‑thought degrade that calibration.

## Takeaways
- The paper defines “B‑calibration,” a flexible calibration notion over semantic equivalence classes.
- Base LLMs can estimate confidence in meaning, not just next‑token probabilities.
- Semantic calibration emerges as a byproduct of next‑token prediction under local optimality.
- RL instruction‑tuning systematically harms semantic calibration.
- Chain‑of‑thought reasoning also breaks calibration in their experiments.

## Synthesis
This research note tackles a persistent gap in LLM evaluation: models can be well‑calibrated at the token level yet still provide confidence estimates that do not track the correctness of their answers’ meaning. The authors propose a sampling‑based measure of “semantic calibration,” then show that base LLMs (prior to instruction tuning) are surprisingly well‑calibrated under this definition in open‑domain question answering.

The key theoretical idea is a general framework called B‑calibration, where calibration is defined relative to equivalence classes of outputs—semantic classes rather than literal token strings. Using a recent link between calibration and local loss optimality, they argue that next‑token prediction can induce semantic calibration as a byproduct when the model can predict its own distribution over semantic answer classes. This yields a concrete prediction: base models should be calibrated on semantics when they can estimate those semantic distributions before generating a response.

Experiments validate three implications. First, base LLMs show semantic calibration across QA tasks, suggesting that confidence estimates can align with meaning‑level correctness even without explicit calibration training. Second, RL instruction‑tuning harms this property: after alignment‑style fine‑tuning, the models’ semantic calibration degrades. Third, chain‑of‑thought reasoning also breaks calibration, implying that reasoning traces—often used to boost accuracy—can distort confidence estimates at the semantic level.

The result reframes calibration as a property that can be lost through common post‑training techniques. It implies a trade‑off: instruction tuning and reasoning prompts may improve helpfulness or accuracy but can make confidence signals less reliable. For practitioners who rely on confidence for decision thresholds, retrieval fallbacks, or safety filters, the paper suggests caution: calibration should be measured explicitly after fine‑tuning, not assumed to carry over from base models.

Overall, the work provides a principled explanation for when semantic calibration emerges and when it fails. It also offers a pathway to designing training procedures that preserve meaning‑level calibration—an important step for building systems that can accurately communicate uncertainty to users.
