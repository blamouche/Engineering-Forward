# Engram: How DeepSeek Added a Second Brain to LLM

**Source**: https://rewire.it/blog/engram-how-deepseek-added-second-brain-to-llm/index.html

**Date**: January 13, 2026

**Author**: Tim Richardson

**Keywords**: DeepSeek, Engram, LLM architecture, memory systems, N-gram, transformer optimization, sparse parameters, MoE

## Elevator pitch

DeepSeek's Engram architecture adds a "second brain" to large language models by storing frequently occurring N-gram patterns in lookup tables for O(1) retrieval, freeing computational resources for more complex reasoning tasks.

## Takeaways

- Large language models waste enormous computational effort reconstructing patterns they've seen millions of times—Engram solves this by storing common N-grams in lookup tables
- The architecture uses four key mechanisms: tokenizer compression (23% vocabulary reduction), multi-head hashing, context-aware gating, and multi-branch integration for different N-gram orders
- Performance improvements span all benchmarks, with the most dramatic gains in long-context retrieval showing a 12.8-point improvement in multi-query tasks
- The "U-shaped scaling law" discovery suggests optimal performance when allocating 20-25% of sparse parameters to Engram memory, creating a new orthogonal axis of sparsity
- Deterministic N-gram IDs enable CPU offloading of 100B parameter embedding tables with less than 3% overhead, far exceeding attention-based memory systems

## Synthesis

Tim Richardson's technical deep-dive into DeepSeek's Engram architecture reveals a elegantly simple insight that could reshape how we think about large language model efficiency. The core observation is almost embarrassingly obvious once stated: LLMs spend vast computational resources repeatedly reconstructing the same patterns they've encountered millions of times during training. Instead of forcing the model to rediscover these patterns through expensive neural computation, why not simply store them in lookup tables?

Engram implements this concept through a sophisticated four-component architecture. First, tokenizer compression reduces vocabulary size by 23% by recognizing semantic redundancy among tokens, making the lookup tables more manageable in size. Second, multi-head hashing employs multiple independent hash functions to mitigate collisions, drawing clear parallels to how multi-head attention operates in standard transformers. Third, context-aware gating uses the hidden state as a dynamic query to determine when the model should trust memory lookups versus fall back on neural computation. Finally, multi-branch integration maintains separate processing branches for different N-gram orders—bigrams, trigrams, and beyond—combining them through learned convolutions.

The empirical results validate this architectural approach across every benchmark tested. Knowledge tasks saw improvements of 3-4 points on MMLU and CMMLU. Reasoning benchmarks improved by 3-5 points on BBH and DROP. Code and math tasks showed gains of 2-3 points across HumanEval, MATH, and GSM8K. But the most striking improvement appeared in long-context retrieval, where multi-query NIAH tasks improved by 12.8 points. This dramatic gain suggests that offloading pattern matching to memory frees up the attention mechanism to focus on what it does best: modeling long-range dependencies and complex relationships.

Perhaps the most significant contribution is the discovery of what the researchers call the "U-shaped scaling law." This finding indicates that optimal performance emerges when approximately 20-25% of sparse parameters are allocated to Engram memory, with the remainder going to Mixture-of-Experts computation. This represents a genuinely new dimension of model design—an orthogonal axis of sparsity that complements rather than competes with existing architectural innovations.

The practical implications for deployment are substantial. Because N-gram IDs are deterministic, they enable runtime prefetching that overlaps communication with computation. This allows CPU offloading of embedding tables with negligible overhead—less than 3% despite handling 100 billion parameters. Such efficiency dramatically exceeds what attention-based memory systems can achieve, opening new possibilities for running increasingly capable models on constrained hardware.

Engram represents the kind of architectural innovation that advances the field not through brute-force scaling but through smarter resource allocation—recognizing that different types of computation deserve different treatment.
