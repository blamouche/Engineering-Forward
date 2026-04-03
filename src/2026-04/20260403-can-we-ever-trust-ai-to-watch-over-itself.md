# Can We Ever Trust AI to Watch Over Itself?

**Source**: https://www.transformernews.ai/p/ai-alignment-researchers-want-to-superintelligence
**Date**: Unknown
**Author**: Transformer News
**Keywords**: AI alignment, superintelligence, safety, automated alignment, Anthropic, OpenAI, Superalignment, Jan Leike

## Elevator pitch
As AI systems become capable enough to contribute to their own development, alignment researchers face the uncomfortable reality that they may need to delegate AI safety work to AI itself—with all the risks that entails.

## Takeaways
- AI safety research accounts for a small fraction of total AI research, and as models improve faster than human researchers can keep pace, the field may have to automate alignment research using AI itself
- OpenAI's Superalignment team (now disbanded) explicitly targeted building a human-level automated alignment researcher; Anthropic's Jan Leike leads similar work there
- Frontier models from Anthropic, OpenAI, and Google have already contributed to their own development in limited ways—this trend is expected to accelerate
- The core dilemma: humans can't reliably supervise AI systems much smarter than themselves, but delegating AI safety to AI requires trusting systems whose alignment is precisely what's in question
- Leike argues that a model that's "as good as us at alignment research and that we trust more than ourselves" may be achievable before full superintelligence, creating a potential window for safe handoff

## Synthesis
The AI safety field faces an uncomfortable recursive problem: as AI systems become more capable, they increasingly contribute to their own development. The researchers tasked with keeping those systems aligned are in a race against the capability curve—and many worry they're falling behind.

The numbers frame the scale of the challenge. When OpenAI published GPT-1, roughly 100 full-time researchers were working seriously on AI safety. By 2025, that number had grown sixfold to around 600. But total AI research headcount grew much faster, meaning safety research accounts for an ever-smaller fraction of the overall field. More resources are going toward making AI faster, smarter, and cheaper than toward understanding how to keep it controllable.

This matters because the nature of the control problem changes as systems become more capable. Current frontier models can use computers autonomously, write code, run experiments, and plot results. OpenAI and Anthropic are already using LLMs to interpret aspects of their own training. As agentic AI systems take over more of the work of making models smarter, human researchers become progressively less able to audit what's happening.

The logical endpoint—and the uncomfortable conclusion that AI safety researchers have largely reached—is that aligning AI may eventually require delegating alignment work to AI itself. OpenAI's now-disbanded Superalignment team explicitly pursued this: their stated goal was building "a roughly human-level automated alignment researcher." Anthropic's Jan Leike, who now leads that company's Alignment Science team, continues pursuing similar goals.

Leike's framing provides a useful distinction. He's not arguing for immediate AI superintelligence doing alignment work—he's targeting the more achievable intermediate goal of a model "as good as us at alignment research, and that we trust more than ourselves to do this research well." If this intermediate goal is achievable before full superintelligence, it could create a window where a trusted AI alignment researcher can help solve the harder problem of aligning much more powerful systems.

But the circularity is real and difficult. To delegate alignment work to an AI, you need to trust that AI's alignment. Establishing that trust requires alignment work that may itself require AI assistance. The field hasn't resolved this loop—it's acknowledging it.

Ryan Greenblatt of Redwood Research captures the stakes: without automating alignment research, humanity risks getting "left in the dust" as AI capability outpaces human ability to supervise it. This isn't a comfortable place to be—but it may describe where we actually are.

For engineering teams building AI systems today, the practical implication is simpler: build with the assumption that human oversight will eventually be insufficient, design safety properties that are robust rather than reliant on human review, and invest in automated testing and evaluation of model behavior.
