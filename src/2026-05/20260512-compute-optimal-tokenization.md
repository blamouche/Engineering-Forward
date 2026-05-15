# Compute Optimal Tokenization
**Source**: https://arxiviq.substack.com/p/compute-optimal-tokenization
**Date**: May 12, 2026
**Author**: Tomasz Limisiewicz, Artidoro Pagnoni, Srini Iyer, Mike Lewis, Sachin Mehta, Alisa Liu, Margaret Li, Gargi Ghosh, Luke Zettlemoyer (summarized by ArXivIQ / Grigory Sapunov)
**Keywords**: tokenization, neural scaling laws, Chinchilla, compute-optimal training, compression rate, BPE, multilingual models, information density

## Elevator pitch
New research systematically derives compression-aware neural scaling laws by training nearly 1,300 models, demonstrating that the widely accepted "20 tokens per parameter" Chinchilla heuristic is an artifact of specific subword tokenizers and proposing a tokenizer-agnostic scaling framework based on bytes rather than tokens.

## Takeaways
- The Chinchilla scaling law's "20 tokens per parameter" optimal ratio is not a fundamental property of neural network training but an artifact of the specific tokenizer used—changing the tokenizer changes the optimal ratio.
- By reframing scaling in terms of bytes (information content) rather than tokens (tokenizer output), the authors derive a tokenizer-agnostic scaling law that generalizes across languages, modalities, and tokenization schemes.
- The optimal compression rate (bytes per token) is compute-dependent: as FLOP budgets increase, the optimal compression rate actually decreases, meaning larger training runs benefit from less aggressive tokenization.
- Training nearly 1,300 models provided the statistical power to isolate tokenization as an independent variable in scaling behavior, exposing how BPE tokenizers inherently skew compute allocation.
- The findings have direct practical implications for training massively multilingual foundation models, where the same tokenizer may compress different languages differently, leading to suboptimal allocation of compute across languages.

## Synthesis
The paper summarized by ArXivIQ challenges one of the most deeply embedded assumptions in modern LLM training: the Chinchilla-derived heuristic that optimal training requires approximately 20 tokens per model parameter. The authors, a research team that includes prominent figures in NLP scaling research, argue that this ratio is not a law of nature but an artifact of the specific Byte-Pair Encoding (BPE) tokenizers used in the experiments that established it. By treating tokenization as a variable rather than a fixed preprocessing step, they reveal that the true invariant in scaling behavior is information content measured in bytes, not tokenizer output measured in tokens.

The scale of the experimental work is impressive: nearly 1,300 models were trained to systematically vary compression rates and observe the effects on compute efficiency. This data enables the derivation of what the authors call "compression-aware neural scaling laws"—a framework that predicts optimal compute allocation based on bytes of training data rather than token counts, making it robust across different tokenization strategies.

A particularly counterintuitive finding is that the optimal compression rate is compute-dependent. As training FLOP budgets increase, the optimal bytes-per-token ratio actually decreases—meaning that for very large training runs, you benefit from less aggressive compression. This inverts the intuition that bigger models need more aggressive tokenization to manage sequence lengths, suggesting instead that bigger models benefit from access to finer-grained information in the training data.

The practical stakes are significant. The entire field has been allocating hundreds of millions of dollars in compute based on scaling laws that implicitly assume a particular tokenizer. If the "20 tokens per parameter" rule is specific to certain BPE configurations, then many large training runs may have been systematically misallocating resources—either training on too little data (if the tokenizer compresses more than assumed) or too much (if it compresses less). The byte-based framework provides a path to more efficient compute allocation, particularly for multilingual models where tokenization compression rates vary dramatically across languages.

The paper's broader message is that preprocessing choices—often treated as implementation details—can have first-order effects on training dynamics and outcomes. Tokenization, long considered a solved problem, turns out to be a strategic variable that interacts with scaling behavior in ways that the field is only beginning to understand.
