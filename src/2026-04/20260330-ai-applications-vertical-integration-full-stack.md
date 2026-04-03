# AI Applications and Vertical Integration
**Source**: https://www.tanayj.com/p/ai-applications-and-vertical-integration
**Date**: March 30, 2026
**Author**: Tanay Jaipuria (Partner at Wing)
**Keywords**: AI applications, vertical integration, full-stack AI, model development, outcome-based services, Cursor, Intercom

## Elevator pitch
AI application companies are pursuing vertical integration in one of two directions: downward into model development (capturing training data advantages) or upward into services (selling outcomes rather than software).

## Takeaways
- Three-layer AI stack: model (bottom), application/agent (middle), human/service layer (top)
- Path 1 (Full-Stack Down): companies like Cursor and Intercom develop proprietary models using their unique user interaction traces
- Path 2 (Full-Stack Up): companies deliver outcomes across legal, insurance, accounting, combining software, AI, and human expertise
- Cursor's Composer 2 uses continued pretraining plus RL on long-horizon coding tasks; Intercom's Fin Apex handles all English chat and email
- Data flywheel advantage: proprietary user traces enable fine-tuned models that outperform larger generic alternatives at lower cost

## Synthesis
Jaipuria's framework identifies the strategic logic driving a pattern visible across AI application companies: sustained competitive advantage in an environment where base models are commoditizing requires integration beyond the application layer. Single-layer businesses — those that provide only the application/agent layer between a foundation model and end users — face the same differentiation problem that API-wrapper businesses always have, with the additional risk that foundation model providers can eliminate their market by improving their own products.

The Full-Stack Down path addresses this through data and model ownership. Cursor's development of Composer 2 through continued pretraining and reinforcement learning on long-horizon coding tasks illustrates the flywheel: an application deployed at scale generates proprietary training data from user interactions that no competitor can replicate. This data trains a model that outperforms generic alternatives on the specific tasks the application handles, which in turn improves the application, attracting more users and generating more training data. Intercom's Fin Apex — reportedly handling all English-language chat and email interactions — represents the same flywheel applied to customer service.

The Full-Stack Up path is strategically distinct. Rather than competing on model quality, these companies compete on outcome delivery. A legal services company that sells contract review outcomes (not contract review software) can charge on value delivered, absorbs the risk of model performance, and differentiates through the combination of software, AI, and human expertise that ensures outcomes. This model is more defensible against commoditization because the value is in the integrated workflow, not the AI component alone.

The evolutionary path Jaipuria describes — service-layer companies eventually integrating downward into model development — suggests these two integration directions may ultimately converge. Companies that own the full stack from model to outcome delivery would have the strongest competitive position, though the operational complexity of running that full stack is substantial. The pattern suggests that the AI application market is stratifying between businesses committed to deep vertical integration and those that remain dependent on commodity foundation models.
