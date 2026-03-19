# Thinking to Recall: How Reasoning Unlocks Parametric Knowledge in LLMs
**Source**: https://arxiv.org/abs/2603.09906
**Date**: 2026-03-10
**Author**: Zorik Gekhman, Roee Aharoni, Eran Ofek, Mor Geva, Roi Reichart, Jonathan Herzig
**Keywords**: reasoning, knowledge recall, LLMs, hallucination, factual priming, computational buffer, chain-of-thought, parametric knowledge

## Elevator pitch
Reasoning processes help language models retrieve factual knowledge even for simple single-hop questions—through two mechanisms: using generated tokens as a computational buffer for hidden computations, and creating semantic pathways that prime related facts.

## Takeaways
- Two mechanisms by which reasoning aids knowledge recall: computational buffer effect (generated tokens used for hidden computation regardless of semantic content) and factual priming (topically connected generation creates semantic pathways to target facts).
- Reasoning helps even for simple, single-hop questions that seemingly don't require complex logical steps—suggesting reasoning processes have broad positive effects on knowledge retrieval beyond complex multi-step reasoning.
- Critical trade-off: when models generate incorrect intermediate facts during reasoning, they become significantly more likely to produce hallucinated final answers.
- Practical implication: selecting reasoning paths that maintain factual accuracy improves overall model performance on knowledge recall tasks.

## Synthesis
This paper addresses a question that chain-of-thought prompting research has raised but not fully answered: why does generating reasoning steps help even for questions that don't logically require step-by-step reasoning? The two mechanisms identified—computational buffer and factual priming—provide mechanistic explanations for an empirically observed phenomenon.

The computational buffer effect is the more counterintuitive finding. It suggests that the act of generating tokens, regardless of their semantic content, provides the model with additional computational capacity for retrieving information. This is consistent with theoretical arguments about transformer computation: more forward passes through the network layers provide more opportunities for the right circuits to activate. The implication is that even nonsensical filler text in a chain-of-thought might provide computational benefit—a finding with practical implications for how chain-of-thought prompting should be evaluated.

The factual priming mechanism is more intuitive but still important. When a model generates text that is topically related to the target answer, it activates semantic neighborhoods in its representation space that include the target fact. This is analogous to how human memory works: thinking about related concepts increases the accessibility of associated memories. For LLMs, this suggests that prompting strategies that naturally contextualize questions within their topic area—rather than asking bare questions—may improve knowledge retrieval systematically.

The hallucination risk is the most practically significant finding. If incorrect intermediate facts increase the probability of hallucinated final answers, then chain-of-thought prompting creates a new failure mode: the model generates plausible-sounding but incorrect reasoning, which then propagates into an incorrect answer that the model presents with the false confidence of a reasoned conclusion. This is potentially more dangerous than direct hallucination, because the reasoning chain provides spurious justification that can fool both the model and the human reader.
