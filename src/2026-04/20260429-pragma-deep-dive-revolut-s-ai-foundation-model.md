# PRAGMA Deep Dive: Revolut's AI Foundation Model

**Source**: https://linas.substack.com/p/revolut-pragma-foundation-model
**Date**: April 29, 2026
**Author**: Linas Beliūnas
**Keywords**: revolut, foundation-models, fintech, fraud, credit-scoring

## Elevator pitch
Revolut's PRAGMA model shows how large-scale behavioral event data is becoming a strategic asset in finance, with one shared backbone outperforming siloed models across multiple banking tasks.

## Takeaways
- PRAGMA is trained on banking event sequences from roughly 25 million users across 111 countries.
- The model replaces many task-specific systems with a shared representation used across credit, fraud, engagement, and other tasks.
- Reported gains are large for several tasks, but the article notes performance tradeoffs such as weaker AML outcomes.
- The broader pattern includes similar moves by Stripe, Visa, and Mastercard toward financial foundation models.
- The real moat may come from proprietary event scale and organizational ability to operationalize it, not novel architectures alone.

## Synthesis
This deep dive treats Revolut's PRAGMA model as evidence that finance is entering a foundation-model phase centered on behavioral data. According to the summary, PRAGMA is trained on tens of billions of banking events and hundreds of billions of tokens from a user base spanning more than a hundred countries. Rather than maintaining separate pipelines and hand-built features for each downstream use case, Revolut uses a shared encoder architecture to generate representations that can transfer across credit scoring, fraud detection, user engagement, and other financial tasks. The headline improvements are substantial in some areas, but the article is careful not to present the model as universally better. It notes meaningful tradeoffs, such as weaker anti-money-laundering performance, which suggests that financial foundation models will still need careful task-level evaluation and governance. The larger strategic argument is that the real advantage may lie less in algorithmic novelty than in access to rich longitudinal event streams at scale. Stripe, Visa, Mastercard, and now Revolut are all converging on this thesis, which implies a new competitive layer in financial services. The firms best positioned may be those with enough proprietary behavioral data, product breadth, and regulatory capacity to turn shared representations into production decisions across the stack.
