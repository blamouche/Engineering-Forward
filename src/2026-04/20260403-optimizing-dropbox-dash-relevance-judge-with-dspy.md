# How We Optimized Dash's Relevance Judge with DSPy

**Source**: https://dropbox.tech/machine-learning/optimizing-dropbox-dash-relevance-judge-with-dspy
**Date**: Unknown
**Author**: Dropbox Engineering
**Keywords**: DSPy, LLM, relevance judge, Dropbox Dash, prompt optimization, search, production ML

## Elevator pitch
Dropbox used DSPy to systematically optimize their LLM-as-a-judge relevance system, achieving better accuracy at lower cost by automating prompt adaptation across model changes instead of manual tuning.

## Takeaways
- Dropbox Dash's relevance judge scores query-document pairs on a 1-5 scale and is used across ranking, training data generation, and offline evaluation pipelines
- Manual prompt tuning hit quality plateaus and caused regressions every time the underlying model was swapped—a common and expensive problem in production LLM systems
- DSPy converts prompt optimization into a systematic, measurable optimization loop using Normalized Mean Squared Error (NMSE) against human rater agreement as the objective
- The system migrated from expensive proprietary models (o3) to open-weight models (gpt-oss-120b) while maintaining quality through DSPy-optimized prompts
- Output formatting reliability (valid JSON) was tracked as a hard constraint alongside accuracy, since unparseable outputs fail entire pipelines

## Synthesis
LLM-as-a-judge systems have become a critical component of modern AI-powered products: they evaluate search results, generate training labels, power offline evaluation pipelines, and rank candidates at scale. But building a reliable relevance judge in production is harder than it looks—and Dropbox's engineering blog post provides one of the most concrete accounts of what that actually entails.

The core problem Dropbox faced was prompt brittleness. Their initial relevance judge worked well with a powerful proprietary model, but quality plateaued during manual tuning and any model swap—even a minor prompt edit—risked unexpected regressions. As Dash scaled, they needed to judge orders of magnitude more query-document pairs than the expensive o3 model could economically handle. The solution required both a model migration and a systematic approach to prompt optimization.

DSPy (Declarative Self-improving Python) provides exactly this: a framework that treats prompt construction as an optimization problem with a measurable objective. Rather than manually crafting prompts and testing them, DSPy optimizes prompt templates against a defined metric. For Dropbox, the metric was Normalized Mean Squared Error between the LLM judge's 1-5 relevance scores and scores from human annotators performing the same task.

The human agreement measurement is subtle and worth unpacking. Humans evaluate query-document pairs and assign 1-5 relevance scores with explanations. NMSE captures the magnitude of disagreement: a judge that assigns 4 when humans assign 5 is penalized less than one that assigns 1. This scalar metric makes the optimization tractable and interpretable.

Dropbox also tracked structural reliability as a hard constraint: if the model returns broken JSON, the output is unusable and treated as completely wrong. This is not just a cosmetic concern—formatting failures at scale cause batches to fail, examples to be dropped, and evaluation metrics to become unreliable. Production relevance judges must be both accurate and structurally reliable.

The model migration path—from o3 to gpt-oss-120b—represents a significant cost reduction. Open-weight models that can be run on Dropbox's own infrastructure eliminate per-call API costs at scale. The challenge was that prompts optimized for o3 didn't transfer cleanly, requiring the optimization loop DSPy provides to adapt prompts to the new model's behavior.

The broader lesson for ML engineers: LLM-based judges should be treated as optimizable systems, not static prompt engineering exercises. Every model change is an opportunity for regression if prompts aren't re-adapted. Building an automated optimization pipeline around a clear human-agreement metric makes model migrations manageable and systematic rather than risky and manual.

For teams building similar systems: define your evaluation metric against human judgments early, invest in structured output validation, and treat prompt adaptation as a first-class engineering concern rather than ad-hoc manual tuning.
