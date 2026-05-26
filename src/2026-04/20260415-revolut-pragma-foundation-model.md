# Inside Revolut's PRAGMA: The Foundation Model Trained on 40 Billion Banking Events
**Source**: https://linas.substack.com/p/revolut-pragma-foundation-model
**Date**: April 15, 2026
**Author**: Linas Beliūnas
**Keywords**: foundation model, banking, Revolut, PRAGMA, encoder, Transformer, credit scoring, fraud detection, Stripe, Mastercard, Visa, financial services, AI

## Elevator pitch
Revolut's PRAGMA is a family of encoder Transformer models pre-trained on 40 billion banking events from 25 million users across 111 countries, delivering massive improvements in credit scoring (+130% PR-AUC), fraud detection (+65% recall), and engagement prediction (+79% PR-AUC) by replacing siloed task-specific models with a single shared behavioral embedding backbone.

## Takeaways
- PRAGMA was trained on approximately 40 billion events and 207 billion tokens from real user banking data, making it the most ambitious consumer neobank foundation model to date.
- The architecture fuses multiple event sources (transactions, app navigation, trading, push notifications) into a single user-level embedding, unifying formerly siloed ML tasks.
- Performance gains over production baselines include +130.2% in Credit Scoring PR-AUC, +64.7% in Fraud Recall, and +79.4% in Communication Engagement PR-AUC.
- This marks a new competitive layer in financial services where behavioral representation quality matters more than individual model sophistication, joining Stripe PFM, Mastercard LTM, and Visa TransactionGPT.
- PRAGMA simultaneously degrades AML performance by 47%, highlighting the tension between task-agnostic embeddings and specialized compliance requirements.

## Synthesis
Revolut has published PRAGMA (arXiv: 2604.08649), a family of encoder-style Transformer foundation models that represents a fundamental bet on a specific theory of AI value creation in finance: that rich, longitudinal behavioral data from a Super App generates embeddings that are universally superior to hand-crafted, task-specific features, and that the competitive moat in AI has shifted from algorithms to proprietary event scale.

The training corpus is staggering in its scope — approximately 40 billion banking events spanning 207 billion tokens, drawn from roughly 25 million users across 111 countries. This is not synthetic data or public web text; it is real behavioral data encompassing transactions, app navigation patterns, trading activity, and push notification interactions, all fused into unified user-level embeddings through a three-encoder architecture.

The performance improvements over existing production baselines are dramatic: +130.2% lift in Credit Scoring PR-AUC, +64.7% improvement in Fraud Recall, and +79.4% gain in Communication Engagement PR-AUC. These numbers validate the core hypothesis that a single shared backbone, trained on broad behavioral data, can transfer learned representations across diverse financial tasks more effectively than purpose-built models trained on narrow feature sets.

However, the story is more nuanced than headline performance numbers suggest. PRAGMA also degrades anti-money laundering (AML) performance by 47%, revealing a critical limitation: task-agnostic embeddings trained on general behavioral patterns may dilute the specialized signals required for compliance-critical applications. This tension between broad representation and domain-specific precision will likely define the next phase of financial foundation model development.

PRAGMA enters a rapidly converging competitive landscape. Within the past twelve months, Stripe, Mastercard, Visa, and now Revolut have all published or announced foundation models for financial data. This convergence is not coincidental — it signals the emergence of a new competitive layer in financial services where the quality of behavioral representation increasingly determines who can underwrite credit, detect fraud, and personalize experiences most effectively. PRAGMA is arguably the most ambitious of these efforts, as the only model fusing multiple event sources at consumer scale and the only one built by a consumer neobank rather than a payments network.

The implications extend far beyond Revolut. For fintechs and neobanks considering their own foundation models, the minimum data scale threshold becomes a critical strategic question. For traditional banks, the organizational structure that separates credit, fraud, compliance, and product teams into silos may make the kind of unified behavioral training that PRAGMA represents structurally impossible — even if they possess comparable data. For startups, opportunities emerge in thin-file credit scoring, explainability tooling for foundation model decisions, and the regulatory compliance layer that will be necessary when these models enter production in regulated markets.
