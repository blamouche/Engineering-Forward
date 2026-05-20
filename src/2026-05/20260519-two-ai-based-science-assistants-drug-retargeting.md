# Two AI-Based Science Assistants Succeed with Drug-Retargeting Tasks
**Source**: https://arstechnica.com/science/2026/05/two-ai-based-science-assistants-succeed-with-drug-retargeting-tasks/
**Date**: May 19, 2026
**Author**: John Timmer
**Keywords**: ai, science, drug-discovery, biology, llm, google, futurehouse, literature-review, hypothesis-generation

## Elevator pitch
Two independently developed AI systems — Google's Co-Scientist and FutureHouse's Robin — demonstrate the ability to generate testable drug-repurposing hypotheses by synthesizing vast amounts of scientific literature, with Robin going further by automating data analysis from biological assays.

## Takeaways
- Both systems address the same core problem: the explosion of scientific publications has made it impossible for human researchers to stay on top of their field, let alone find relevant insights across disciplines
- Google's Co-Scientist uses a "tournament" system where hypotheses compete, with a Reflection agent evaluating and an Evolution agent improving survivors — keeping human scientists in the loop throughout
- FutureHouse's Robin processed 551 papers in 30 minutes versus an estimated 540 hours for a human, using specialized tools (Crow, Falcon) for literature summarization
- Robin uniquely includes Finch, a tool that automates evaluation of data from standard assays like flow cytometry and RNA-seq — closing the loop from hypothesis to experimental validation
- Swapping Robin's custom literature tools for a general-purpose LLM (OpenAI's o4-mini) caused hallucinated references to jump from 0% to 45%

## Synthesis
Two papers published simultaneously in Nature describe AI systems designed not to replace scientists, but to tackle a problem that has become intractable for human researchers alone: the overwhelming volume of scientific literature. With the proliferation of online journals, no single researcher can comprehensively track their field, and cross-disciplinary connections — the kind that often lead to breakthroughs — are even harder to make.

Google's Co-Scientist, built on Gemini, takes a research goal from human scientists and launches a literature search to form hypotheses. These compete in a tournament structure, evaluated by a Reflection agent with access to external search tools. Surviving ideas are refined by an Evolution agent and re-entered into competition. Throughout, human scientists remain in the loop — their judgment directs the system, and expert panels prioritize which drug candidates to test. When applied to acute myeloid leukemia, the system identified drugs effective against subsets of cancer cell lines, consistent with the biological reality that different mutations create different vulnerabilities.

FutureHouse's Robin takes a complementary approach with a critical difference. Its specialized literature tools — Crow for concise summaries and Falcon for deep paper analysis — allow it to process 551 papers in half an hour. But the key innovation is Finch, which automates the analysis of experimental data from standard biological assays. This means Robin can form a hypothesis, suggest experiments, and then evaluate the resulting data — creating a more complete scientific workflow. When applied to macular degeneration, Robin identified a novel hypothesis involving cellular debris clearance and a drug that appeared to boost that mechanism.

Both systems benefit enormously from domain-specific tooling. When FutureHouse swapped its custom literature tools for a general-purpose model, hallucinated references skyrocketed from zero to 45%. The success of both approaches in drug repurposing — an area where existing drugs have known safety profiles and the hypothesis format is relatively concrete — demonstrates real value while also highlighting that more open-ended scientific questions remain beyond current capabilities. As John Timmer notes, the real contribution may be preventing the tragedy of insights that sit undiscovered in the literature for a decade because no human ever put them together.
