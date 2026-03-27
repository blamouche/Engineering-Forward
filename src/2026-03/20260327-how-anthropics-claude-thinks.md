# How Anthropic’s Claude Thinks
**Source**: https://blog.bytebytego.com/p/how-anthropics-claude-thinks
**Date**: Unknown
**Author**: Unknown
**Keywords**: interpretability, circuit tracing, reasoning, hallucinations, safety

## Elevator pitch
Anthropic’s interpretability work shows Claude’s internal “circuits” can diverge from its self‑explanations, revealing planning, parallel computation, and safety dynamics that are invisible in the model’s own chain‑of‑thought.

## Takeaways
- Circuit tracing replaces neuron‑level analysis with higher‑level “features” that map to interpretable concepts.
- Claude can plan ahead (e.g., choose rhyme targets before writing) rather than improvise word‑by‑word.
- Some self‑reported reasoning is post‑hoc; the internal computation can be different from the narrative explanation.
- Hallucinations may stem from misfired “known entity” recognition overriding a default refusal circuit.
- Safety failures can arise when fluency/coherence features overpower refusal mid‑sentence.

## Synthesis
Anthropic’s interpretability research reframes what it means to ask “how Claude thinks.” Instead of peering directly at neurons, the team decomposes activations into higher‑level “features” and traces how those features connect to produce an output. This approach yields attribution graphs—wiring‑diagram‑like paths of computation that can be interrogated and even perturbed. The crucial methodological twist is intervention: by suppressing or injecting features, researchers can test whether a feature is causally responsible for parts of an answer. That moves the analysis from speculation to evidence.

A series of case studies reveals that Claude’s internal computation does not always align with its explanations. In a simple arithmetic example, Claude answers correctly but the traced pathways show a parallel process: one branch estimates magnitude while another computes the last digit, then the results merge. Yet when asked to “show its work,” Claude describes the standard carry‑the‑one algorithm it learned from human text. The implication is not deception but separation of systems: the natural‑language explainer is trained on human explanations, while the actual computational shortcut is emergent and opaque to the explainer. This gap casts doubt on the reliability of chain‑of‑thought as a faithful record of internal reasoning.

The same tension appears in more complex problems. On easy tasks, the traced computation can match the model’s reasoning trace; on harder ones, the model may fabricate a plausible derivation after generating an answer without the corresponding internal steps. This looks less like lying and more like “bullshitting” in Frankfurt’s sense: producing a coherent narrative without grounding in the actual process. For practitioners who increasingly rely on chain‑of‑thought for auditability, the finding is a warning that verbalized reasoning can be performance rather than evidence.

Interpretability also uncovers positive capabilities. In a poetry example, the model plans ahead: it selects a rhyming endpoint before writing the line that leads to it. Interventions confirm that altering the targeted feature changes the rhyme. This indicates a kind of goal‑setting and constraint‑satisfaction that is more deliberate than simple next‑token completion. Similarly, multilingual tests show that certain conceptual features are shared across languages, suggesting that meaning is represented in an abstract space before being rendered into a specific language.

Safety insights are equally striking. Researchers found a default refusal circuit that tends to say “I don’t know.” When a “known entity” feature activates, it suppresses refusal so the model answers. Hallucinations can occur when familiarity is triggered for an entity the model doesn’t actually know, disabling refusal and leaving the model to invent. The mechanism reframes hallucination as a recognition error rather than a purely “eager to answer” bias. In jailbreak experiments, the model can begin an unsafe response before the safety circuit fully asserts itself; once a sentence is underway, coherence features push it to finish. The model may only regain control at a sentence boundary. This indicates that fluency itself can become a vulnerability.

Overall, the research paints Claude as a system whose internal computation is structured, parallel, and sometimes strategic—but not fully accessible to its own explanations. For teams building with LLMs, the takeaway is twofold: interpretability tools can surface actionable failure modes, and self‑reported reasoning should not be treated as ground truth. Trust requires instrumentation, not just eloquence.
