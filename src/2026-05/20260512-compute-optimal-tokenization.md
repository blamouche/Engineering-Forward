# Compute Optimal Tokenization
**Source**: https://arxiviq.substack.com/p/compute-optimal-tokenization (Analysis) / https://arxiv.org/abs/2605.01188 (Paper)
**Date**: May 12, 2026 (ArXivIQ) / May 2, 2026 (arXiv submission)
**Author**: Tomasz Limisiewicz, Artidoro Pagnoni, Srini Iyer, Mike Lewis, Sachin Mehta, Alisa Liu, Margaret Li, Gargi Ghosh, Luke Zettlemoyer (FAIR / Meta AI)
**Keywords**: Tokenization, scaling laws, neural scaling, compression rate, BPE, Chinchilla, bytes per token, BLT, compute optimality

## Elevator pitch
Meta AI researchers systematically prove that the widely-used Chinchilla scaling law (20 tokens per parameter) is an artifact of specific tokenizers — the true invariant is that training data should scale with model parameters in bytes, not tokens, and the optimal compression rate actually decreases as compute budgets grow.

## Takeaways
- The Chinchilla scaling law's "20 tokens per parameter" heuristic is tied to specific BPE tokenizers with ~4.57 bytes/token — it's not a fundamental law
- By training 988 BLT (Byte Latent Transformer) models from 50M to 7B parameters with variable compression rates, the authors show model size should scale proportionally to data in bytes, not tokens
- The optimal compression rate is compute-dependent: larger compute budgets benefit from lower compression (fewer bytes per token)
- Findings generalize across both latent and subword tokenization, and across languages beyond English
- The paper provides a tokenizer-agnostic scaling framework that maximizes compute efficiency for multilingual and multimodal foundation models

## Synthesis
A team of researchers from Meta AI (FAIR) and the University of Washington, led by Tomasz Limisiewicz and including prominent figures like Luke Zettlemoyer, has published a paper that challenges one of the foundational assumptions of modern language model training. The work, titled "Compute Optimal Tokenization," reframes tokenization — typically treated as a fixed preprocessing step — as a dynamic variable that fundamentally shapes scaling behavior.

The paper's core insight is both simple and profound. The Chinchilla scaling law (Hoffmann et al., 2022), which established the widely-adopted heuristic of training with approximately 20 tokens per model parameter, was derived assuming a fixed tokenization scheme — specifically, the Byte-Pair Encoding (BPE) tokenizer that produces tokens averaging about 4.57 bytes each. By treating "tokens" as the unit of data measurement, the field has been optimizing for an artifact of the tokenizer rather than for the underlying information density. The authors demonstrate this by training 988 models using the Byte Latent Transformer (BLT) architecture, which allows them to control the compression rate — the average bytes of text per token — as an independent variable across models ranging from 50 million to 7 billion parameters.

The experimental results reveal a more fundamental scaling relationship: in compute-optimal configurations, model parameter counts scale proportionally to data size measured in bytes, not in tokens. This is a significant correction to prevailing wisdom. If you're counting tokens, you're measuring the wrong thing — the information content, measured in raw bytes, is what actually matters for optimal compute allocation. The ArXivIQ analysis by Grigory Sapunov captures the implication succinctly: "training data should scale proportionally to model parameters in bytes, not tokens."

Perhaps the most counterintuitive finding is that the optimal compression rate decreases as compute budgets increase. This means that for the largest training runs — the kind that produce GPT-4 and Gemini-class models — you actually want lower compression per token. In practice, this suggests that bigger models benefit from tokenizers that represent fewer bytes per token, providing finer-grained information representation. Current BPE tokenizers may be over-compressing for the scale at which frontier models are trained.

The findings generalize across tokenization paradigms (both latent tokenization via BLT and traditional subword tokenization) and across languages beyond English, giving the results broad applicability. For practitioners, the paper provides a practical framework: when planning a pre-training run, optimize the compression rate alongside model size and data volume as a joint optimization problem rather than accepting whatever the default tokenizer produces. The paper's companion code at co-tok.github.io suggests the authors intend this work to be operational, not merely theoretical.

The broader significance extends to the ongoing debate about tokenizer-free architectures. If tokenization choice materially affects scaling efficiency — and this paper demonstrates it does — then architectures that operate on raw bytes or learned latent representations may have a structural advantage over those tied to BPE or similar subword tokenizers. This work strengthens the case for the BLT architecture and similar byte-level approaches, while giving all model developers a new dimension to optimize in their pursuit of compute-efficient training.
