# How Snapchat Serves a Billion Predictions Per Second
**Source**: https://blog.bytebytego.com/p/how-snapchat-serves-a-billion-predictions
**Date**: May 19, 2026
**Author**: ByteByteGo (Alex Xu)
**Keywords**: Snapchat, ML infrastructure, Bento, ranking systems, feature store, recommendation engines, inference optimization, train-serve skew, Robusta, real-time ML

## Elevator pitch
Snapchat's ML platform Bento serves over a billion predictions per second across 474 million daily users by exploiting the asymmetric nature of ranking workloads — one user request fans out into thousands of model evaluations — and optimizing every layer from the GPU/CPU compute split to serialization overhead, achieving 2x latency reductions and 10x cheaper data plane costs.

## Takeaways
- Snap's Bento platform handles four ML-driven decisions per session (content ranking, ad selection, friend suggestions, AR lenses), all within ~100ms latency budgets at massive scale: 946M MAUs, 474M DAUs.
- The core architectural insight is that ranking requests are asymmetric — one user request expands into hundreds/thousands of (user, candidate) model evaluations, which drives nearly every design decision in Bento.
- Bento splits model training into a layered structure (Core framework, user code, YAML config) enabling hundreds of experiments per day, with model export that separates dense GPU compute from CPU-bound embedding lookups.
- The feature store (Robusta, built on Apache Spark) processes 10 trillion events/day and must keep offline (Iceberg) and online (key-value store) features perfectly synchronized to avoid train-serve skew.
- The most impactful optimization was mundane: redesigning serialization and data transfer as raw bytes (with custom Protobuf optimizations) cut inference latency 2x and data plane costs 10x — proving that at scale, the "boring machinery" often dominates cost more than the model itself.

## Synthesis
ByteByteGo's deep dive into Snapchat's Bento ML platform reveals how extreme-scale recommendation systems are architected when every millisecond matters. The article, based on publicly shared details from Snap's engineering team, paints a comprehensive picture of a platform that processes over a billion predictions per second across 474 million daily active users.

The foundational observation is that ranking workloads have an inherently asymmetric shape. Unlike typical web requests (one-to-one), a ranking request fans out one-to-many: a single user opening the app triggers hundreds or thousands of (user, candidate) model evaluations before collapsing back to a short ranked list. This asymmetry creates four competing pressures — latency, scale, freshness, and iteration — that Bento must reconcile simultaneously.

The platform is organized into two halves. The training half follows a four-stage workflow (data generation, training, evaluation, export) orchestrated by Kubeflow, with a clever three-layer code structure (Core framework, user model code, YAML configuration) that allows ML engineers to run hundreds of experiments daily. The model export step is particularly notable: it splits the compute graph so dense matrix operations run on GPUs while embedding lookups and feature parsing stay on CPUs, matching the unusual computational shape of recommendation models.

The serving half is where the hardest engineering lives. The feature platform Robusta processes 10 trillion events per day, maintaining separate offline (Apache Iceberg) and online (key-value store) feature stores that must remain perfectly synchronized — any divergence causes train-serve skew, where models perform well offline but fail in production. To handle the fanout problem at the feature layer, Bento employs two strategies: for manageable corpora, document features are collocated directly on inference instances (eliminating network fanout entirely); for larger corpora, a dedicated Retrieval service performs ANN search, inverted index lookups, and forward index lookups in a single pass.

The most striking finding is where optimization effort paid off most. Bento's engineers discovered that a large fraction of inference latency came from serialization/deserialization of feature data — the "boring machinery" of the system — rather than from model computation. Redesigning inference APIs to transfer features as raw bytes (with custom Protobuf optimizations) yielded 2x lower latency and 10x cheaper data plane costs. This lesson is profound: at scale, the infrastructure plumbing often dominates costs more than the ML models themselves.

Around all of this runs a continuous feedback loop. Every prediction and user action is logged, flowing back into training data. Incremental training produces new model versions that deploy automatically via a Kubernetes-inspired reconciliation control plane. Two monitoring systems watch for feature drift and compute offline-vs-online prediction comparisons to catch skew. Over a recent two-year period, ranking model size grew 20x and training data grew 40x, absorbed by the platform in normal operation — the mark of a system designed for scale from first principles.
