# Cram Less to Fit More: Training Data Pruning Improves Memorization of Facts

**Source**: https://machinelearning.apple.com/research/cram-less
**Date**: April 13, 2026
**Author**: Jiayuan Ye, Vitaly Feldman, Kunal Talwar
**Keywords**: training data pruning, memorization, factual accuracy, model capacity, Apple research, LLM training

## Elevator pitch
Apple shows that smaller models can memorize more factual knowledge when training data is pruned to reduce fact overload and flatten skew, suggesting that smarter data curation can beat brute-force scale on knowledge retention.

## Takeaways
- The paper argues that factual accuracy becomes suboptimal when the informational load of facts in the dataset exceeds model capacity, especially under skewed frequency distributions.
- Loss-based data selection can improve fact memorization by limiting redundant or capacity-wasting examples and flattening fact frequency.
- In Apple’s experiments, smarter curation let a GPT2-Small model match the fact memorization of a much larger model trained on the full dataset.

## Synthesis
Apple’s result is a nice reminder that more data is not always better data. The paper frames factual memorization as a capacity-allocation problem: if the training distribution stuffs in more high-entropy facts than a model can hold, especially under a skewed popularity curve, then the model will memorize poorly even before architecture becomes the bottleneck. In that setting, pruning is not waste. It is compression of the learning problem.

What makes the result strategically interesting is that it challenges a lazy scaling instinct. If a small model with better curation can match a much larger model on factual retention, then some capabilities may be much more data-engineering-limited than we assume. That opens a path where model builders improve knowledge quality not only through bigger runs or retrieval layers, but through much more selective dataset construction.

The broader implication is economic. Smarter pruning could let organizations get more value out of smaller models, which matters for on-device deployment, energy budgets, and privacy-sensitive settings where giant models are impractical. It is a good example of how the next tranche of gains may come from disciplined pipeline design rather than from raw parameter inflation.
