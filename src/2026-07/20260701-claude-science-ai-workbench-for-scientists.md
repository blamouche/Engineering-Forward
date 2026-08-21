# Claude Science: An AI Workbench for Scientists
**Source**: https://www.anthropic.com/news/claude-science-ai-workbench
**Date**: 2026-06-30
**Author**: Anthropic
**Keywords**: Anthropic, Claude Science, AI workbench, scientific research, life sciences, genomics, reproducibility

## Elevator pitch
Anthropic launched Claude Science, an integrated AI workbench for scientists that consolidates fragmented research tools into a single environment with 60+ curated skills, auditable artifacts, and native rendering of scientific outputs like 3D protein structures and genome browser tracks.

## Takeaways
- Claude Science is a standalone app that integrates common scientific tools (PubMed, Jupyter, R, HPC terminals) into a unified research environment with a generalist coordinating agent.
- It ships with 60+ curated skills and connectors pre-configured for genomics, single-cell analysis, proteomics, structural biology, and cheminformatics.
- A reviewer agent checks citations and calculations, flagging and correcting errors — addressing the reproducibility and hallucination concerns that have limited AI adoption in scientific workflows.
- Every output carries an auditable history of how it was made, making results reproducible; figures and manuscripts include the exact code and environment that produced them.
- Available in beta for Claude Pro, Max, Team, and Enterprise users; runs locally on macOS/Linux or remotely over SSH/HPC login nodes.

## Synthesis
Anthropic's Claude Science is the company's most ambitious push into vertical AI applications, targeting scientific researchers who have been underserved by general-purpose chatbots. The key insight is that scientists don't just need answers — they need auditable, reproducible workflows that integrate with their existing toolchain. By building a workbench rather than a chat interface, Anthropic is betting that the future of AI in science is not replacement but augmentation of the research process.

The product addresses three persistent problems in AI-assisted research: fragmented tools, lack of reproducibility, and hallucination risk. Scientists routinely switch between PubMed for literature, Jupyter for analysis, R for statistics, and cluster terminals for computation. Claude Science consolidates these into one environment where the coordinating agent can spin up specialist agents for domain-specific tasks. The reviewer agent that checks citations and calculations is particularly notable — it's an architectural admission that AI-generated science needs its own quality control layer.

The auditable artifact system is the most important design decision. Every figure, manuscript, and analysis comes with the exact code and environment that produced it. This is how scientific work should be done with AI: not black-box outputs, but transparent pipelines that can be inspected, modified, and rerun. It mirrors the Jupyter Notebook philosophy but extends it with an AI agent that can iteratively refine results based on feedback.

The competitive positioning is clear. While OpenAI pushes toward consumer superapps and Google embeds Gemini into productivity suites, Anthropic is carving out the professional vertical. Science is a natural first move: high-value users with complex workflows, strong reproducibility requirements, and willingness to pay for tools that demonstrably work. If Claude Science succeeds, the pattern — domain-specific workbench + coordinating agent + auditable artifacts — could extend to law, finance, and engineering.