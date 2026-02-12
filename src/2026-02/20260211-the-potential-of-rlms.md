# The Potential of RLMs
**Source**: https://www.dbreunig.com/2026/02/09/the-potential-of-rlms.html?utm_source=tldrai
**Date**: 2026-02-09
**Author**: David Breunig
**Keywords**: long context, context rot, RLM, REPL, agents, DSPy

## Elevator pitch
Recursive Language Models (RLMs) mitigate long-context failure (“context rot”) by moving massive context into a programmable REPL, letting the model *compute over* the data, sample what it needs into tokens, and spawn sub-calls—turning context management into a coding problem.

## Takeaways
- Context rot is quality degradation beyond soft limits, not just a hard context capacity issue.
- RLMs keep two context pools: programmatic (in REPL variables) and tokenized (in model window).
- The model uses the REPL to explore/filter/chunk, and calls a sub-LLM function for help.
- Works on extremely large corpora (hundreds of MB / millions of tokens) but can be slower.
- Traces of RLM runs can reveal repeatable strategies—potentially “discovering” new agent designs.

## Synthesis
The post is a strong reminder that “more context” is not automatically better. Many agent failures emerge from context rot: as transcripts and retrieved documents accumulate, the model continues answering confidently while its accuracy quietly decays. RLMs propose a different posture: stop stuffing everything into tokens, and instead store the bulk of information in a deterministic computational substrate (a REPL) that the model can query.

The mechanism is elegant. Treat the long context like a dataset. Let the model write code to inspect it (counts, filters, sampling, clustering), printing only the slices required for the next reasoning step. When it needs additional judgment, it can spawn sub-LLM calls and store results. This converts an attention-management problem into an iterative analysis loop—something frontier models have become much better at due to heavy post-training on coding and verifiable reasoning.

Two implications matter for agent builders. First, the “hybrid” architecture (probabilistic reasoning + deterministic code) becomes a general recipe for reliability. Second, the traces are gold: by watching how a model explores and converges within an iteration budget, you can extract repeatable patterns (e.g., how it situates itself, how it validates hypotheses). Those patterns can be packaged into purpose-built agents or pipelines that are faster and more reliable than a generic exploratory loop.

The limitations are also clear: latency and the need for strong models. But as with chain-of-thought, RLMs may represent a simple test-time trick that later becomes a first-class capability once models and harnesses are tuned for it.
