# Generalization Results from Training on the APEX-Agents Dev Set

**Source**: https://www.mercor.com/blog/generalization-results-from-training-on-the-apex-agents-dev-set/
**Date**: Unknown
**Author**: Mercor
**Keywords**: APEX-Agents, post-training, generalization, AC-Small, GLM, tool use, professional reasoning, benchmarks

## Elevator pitch
Mercor's AC-Small model, post-trained on agentic professional task data, shows genuine capability generalization—not just benchmark overfitting—improving +5 to +8 points across held-out benchmarks in tool use, professional reasoning, and economically valuable work.

## Takeaways
- AC-Small (post-trained GLM-4.7) improved substantially on three held-out benchmarks: +5.7 points on APEX, +8.0 on Toolathalon, and +7.7pp on GDPVal—none of which were in the training set
- On GDPVal (human-judged professional work across 44 occupations), AC-Small ranks 5th globally, surpassing Claude Opus 4.5 while being significantly cheaper
- Training on law, consulting, and finance data surprisingly improved medicine performance—gains appear to come from learning professional process habits (preserving details, sanity-checking, revising) rather than domain knowledge
- Toolathalon gains (+8pp on 604-tool multi-step workflows) suggest the model learned generalizable tool-use patterns, not just APEX-Agents-specific strategies
- The pattern suggests that training on expert-level agentic task data teaches general professional reasoning habits that transfer across domains

## Synthesis
The most important question in model post-training is whether capability gains are real or just benchmark overfitting. It's easy to train a model that performs well on a benchmark it was optimized for; it's much harder to produce genuine capability improvements that transfer to novel tasks. Mercor's AC-Small results offer meaningful evidence that the latter is possible.

In a previous post, Mercor described post-training GLM-4.7 on the APEX-Agents dev set—a collection of agentic professional tasks spanning law, consulting, and corporate finance. That produced AC-Small, which rose from 17th to 4th on the APEX-Agents leaderboard. The obvious skeptical question: did the model just learn APEX-Agents-specific patterns, or did it actually improve?

The answer, supported by three held-out benchmarks, is that the improvement generalized substantially. On Toolathalon—which evaluates agents on multi-step workflows spanning 604 tools across 32 software applications—AC-Small improved 8 points over the base GLM-4.7. This benchmark tests generalizable tool-use capability across entirely different tools and workflows than the training set. The gain is real.

On APEX (non-agentic professional reasoning across management consulting, investment banking, law, and primary healthcare), AC-Small improved 5.7 points even without any tool access—just reasoning over provided documents. This is perhaps the most surprising result, since it shows that agentic training improved reasoning quality even in non-agentic contexts.

On GDPVal—the most comprehensive test, measuring professional work across 44 occupations as judged by subject-matter experts—AC-Small improved 7.7 percentage points and would rank 5th globally on OpenAI's official leaderboard, surpassing Claude Opus 4.5.

The medicine result is particularly illuminating. Despite training entirely on law, consulting, and finance data, AC-Small substantially improved on medical tasks. The researchers traced this to process improvements: the model learned to preserve sub-details, sanity-check intermediate outputs, and revise when checks fail. These habits transferred directly to medicine, where the base model was losing points by omitting clinically significant details.

This suggests the mechanism of generalization: training on high-quality expert task data doesn't primarily teach domain facts—it teaches professional work habits. How experts structure their thinking, verify their conclusions, and handle ambiguity are generalizable skills that transfer across domains.

The implication for model training: curating expert-level agentic task data across domains may be more valuable than raw scale, because it instills transferable reasoning habits rather than domain-specific pattern matching.
