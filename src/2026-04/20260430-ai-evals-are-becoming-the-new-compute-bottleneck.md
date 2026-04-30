# AI evals are becoming the new compute bottleneck

**Source**: https://huggingface.co/blog/evaleval/eval-costs-bottleneck
**Date**: April 30, 2026
**Author**: Unknown
**Keywords**: huggingface, evals, becoming, compute, bottleneck

## Elevator pitch
A Blog post by EvalEval Coalition on Hugging Face.

## Takeaways
- Back to Articles AI evals are becoming the new compute bottleneck Team Article Published April 29, 2026 Upvote 11 +5 Avijit Ghosh evijit Follow evaleval Yifan Mai yifanmai Follow evaleval Georgia Channing cgeorgiaw Follow evaleval Leshem Choshen borgr Follow evaleval Summary.
- AI evaluation has crossed a cost threshold that changes who can do it.
- The Holistic Agent Leaderboard (HAL) recently spent about $40,000 to run 21,730 agent rollouts across 9 models and 9 benchmarks.
- A single GAIA run on a frontier model can cost $2,829 before caching.
- Exgentic 's $22,000 sweep across agent configurations found a 33× cost spread on identical tasks, isolating scaffold choice as a first-order cost driver, and UK-AISI recently scaled agentic steps into the millions to study inference-time compute.

## Synthesis
Back to Articles AI evals are becoming the new compute bottleneck Team Article Published April 29, 2026 Upvote 11 +5 Avijit Ghosh evijit Follow evaleval Yifan Mai yifanmai Follow evaleval Georgia Channing cgeorgiaw Follow evaleval Leshem Choshen borgr Follow evaleval Summary. AI evaluation has crossed a cost threshold that changes who can do it. The Holistic Agent Leaderboard (HAL) recently spent about $40,000 to run 21,730 agent rollouts across 9 models and 9 benchmarks. A single GAIA run on a frontier model can cost $2,829 before caching. Exgentic 's $22,000 sweep across agent configurations found a 33× cost spread on identical tasks, isolating scaffold choice as a first-order cost driver, and UK-AISI recently scaled agentic steps into the millions to study inference-time compute. In scientific ML, The Well costs about 960 H100-hours to evaluate one new architecture and 3,840 H100-hours for a full four-baseline sweep. While compression techniques have been proposed for static benchmarks, new agent benchmarks are noisy, scaffold-sensitive, and only partly compressible. Training-in-the-loop benchmarks are expensive by construction, and when you try to add reliability to these evals, repeated runs further multiply the cost. Making static LLM benchmarks cheaper The cost problem started before agents. When Stanford's CRFM released HELM in 2022, the paper's own per-model accounting showed API costs ranging from $85 for OpenAI's code-cushman-001 to $10,926 for AI21's J1-Jumbo (178B), and 540 to 4,200 GPU-hours for the open models, with BLOOM (176B) and OPT (175B) at the top end.
