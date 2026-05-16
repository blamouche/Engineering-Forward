# Introducing BigLaw Bench: A Framework for Evaluating LLMs on Complex Legal Tasks
**Source**: https://www.harvey.ai/research/biglaw-bench
**Date**: August 29, 2024
**Author**: Harvey Team
**Keywords**: BigLaw Bench, legal AI, LLM evaluation, Harvey, legal benchmarks, answer score, source score, legal reasoning, AI legal work product

## Elevator pitch
Harvey introduced BigLaw Bench, the first legal AI benchmark built from real billable time entries, showing its proprietary models produce 74% of a lawyer-quality work product while revealing that all models — including frontier LLMs — remain far from fully automating complex legal work.

## Takeaways
- BigLaw Bench tasks are derived from actual lawyer time entries covering litigation and transactional work (drafting, due diligence, case strategy, etc.) — a departure from multiple-choice benchmarks that fail to capture real billable work.
- Harvey's proprietary models scored 74% on answer quality vs. leading foundation models, with the gap most pronounced in source attribution — foundation models consistently hallucinated sources when asked to cite documents.
- The benchmark uses dual scoring: answer score (what % of lawyer-quality work the model completes) and source score (what % of correct statements are backed by verifiable citations) — independent metrics that reveal different failure modes.
- Performance was stronger on transactional tasks (more analytical) than litigation tasks (requiring ideation and argumentation), highlighting where foundation models underperform.
- The public benchmark and evaluation framework are available on GitHub, with plans to expand toward an industry-standard benchmark for measuring AI performance on the full range of legal knowledge work.

## Synthesis
Harvey's BigLaw Bench represents a methodological advance in legal AI evaluation. Rather than relying on bar exam questions or multiple-choice tests — the hallmarks of earlier legal benchmarks — BigLaw Bench constructs tasks from the time entries that define actual legal practice: drafting board consents, analyzing trial exhibits for contradictions, developing negotiation strategies, conducting due diligence. These are the activities lawyers bill for, and they require outputs far more nuanced than a correct answer choice.

The evaluation methodology is notably sophisticated. Harvey's legal research team (composed of BigLaw attorneys) developed bespoke rubrics for each task that establish objective criteria for effective completion while penalizing common LLM failure modes: incorrect tone or length, irrelevant material, toxicity, and hallucinations. The dual scoring system — separating content quality (answer score) from verifiability (source score) — reveals a critical insight: foundation models can produce reasonably good answers (getting users "more than halfway" to a final work product) but consistently fail at showing their work. When explicitly prompted to cite sources, ChatGPT and others hallucinated document text, page numbers, or both, leading to worse answer scores as the hallucinated citations contaminated the output.

Harvey's proprietary models' 74% answer score is simultaneously impressive and sobering — the outputs are more detailed and closer to final lawyer quality than any public model, yet still fall 26% short of complete lawyer-quality work. The performance gap between transactional tasks (stronger, more analytical) and litigation tasks (weaker, requiring ideation and argumentation) points to where current AI architectures hit fundamental limits. The public release on GitHub and collaboration with vals.ai signals Harvey's intent to establish BigLaw Bench as an industry standard, much as SWE-bench has become for software engineering. The roadmap toward benchmarking the full range of tasks lawyers perform — many of which remain "far beyond the reach of LLMs" — acknowledges that this is an early milestone, not an endpoint.
