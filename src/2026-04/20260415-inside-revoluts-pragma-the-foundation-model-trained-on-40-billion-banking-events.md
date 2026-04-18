# Inside Revolut's PRAGMA: The Foundation Model Trained on 40 Billion Banking Events
**Source**: https://linas.substack.com/p/revolut-pragma-foundation-model
**Date**: April 15, 2026
**Author**: Linas Beliūnas
**Keywords**: FinTech, Foundation Models, Credit Scoring, AI in Finance, Revolut, Fraud Detection, AI Risk

## Elevator pitch
Revolut's PRAGMA foundation model represents a structural shift in fintech competition, where proprietary behavioral data and unified architectures now matter more than algorithm sophistication.

## Takeaways
- Behavioral data represents the new competitive moat in fintech, shifting focus from algorithm sophistication to longitudinal event scale and embedding quality
- Unified architecture approach achieves dramatic performance gains across multiple downstream tasks while maintaining a single shared backbone
- Regulatory and task-specific limitations prevent universal performance improvements; AML applications show 47% degradation, indicating specialized architectures remain necessary
- Organizational structure matters significantly; traditional banks face structural disadvantages competing with neobanks due to data silos and governance complexity
- Commercial ecosystem opportunities exist in explainability, compliance tooling, and vertical-specific fine-tuning rather than building competing foundation models from scratch

## Synthesis
Revolut has released PRAGMA, an encoder-style Transformer foundation model trained on approximately 40 billion banking events from 25 million users across 111 countries. This represents a paradigm shift from task-specific models with hand-crafted features toward a unified architecture that transfers learned representations across multiple financial use cases.

The model demonstrates striking performance improvements: a 130% lift in credit scoring PR-AUC, 64.7% improvement in fraud detection recall, and 79.4% gains in communication engagement metrics compared to existing production systems. However, these numerical victories mask a deeper competitive story about how financial services companies view artificial intelligence as a strategic asset.

PRAGMA's three-encoder architecture integrates multiple event streams—transactions, application navigation patterns, trading activity, and notification engagement—into coherent user-level embeddings. This fusion approach distinguishes it from competitors. Stripe, Mastercard, and Visa have all announced or published similar foundation models within the past year, signaling an industry-wide recognition that behavioral data representation now constitutes a fundamental competitive moat.

The convergence of these initiatives from payments networks and neobanks marks the emergence of a new competitive layer in financial services. Rather than competing primarily on algorithmic sophistication, firms now compete on data richness and longitudinal behavioral signals. This represents a structural advantage for companies with diverse transaction ecosystems and extended user interaction histories.

Despite impressive headline metrics, important limitations surface in the research. The model shows a 47% performance degradation in anti-money laundering applications, suggesting that unified embeddings optimized for consumer-friendly tasks may compromise performance in compliance-critical functions. This tradeoff indicates that foundation models won't eliminate the need for specialized architectures in regulated domains.

Regulatory constraints pose another practical barrier. Several jurisdictions may restrict deployment of PRAGMA's highest-performing applications despite technical capabilities, potentially limiting commercial value in Revolut's most profitable markets. Traditional banks face structural disadvantages in replicating this approach, primarily because organizational silos, legacy infrastructure, and governance complexity impede the data integration that foundation models require.

For emerging fintech companies and neobanks, the minimum viable scale for building proprietary foundation models remains undefined, though 25 million users across significant geographies appears sufficient. This creates barriers for smaller competitors while favoring established players with substantial user bases. Commercial opportunities emerge for startups addressing specific gaps: thin-file credit scoring using transfer learning, explainability tooling for regulatory compliance, and specialized fine-tuning frameworks for vertical applications.
