# How Snapchat Serves a Billion Predictions Per Second
**Source**: https://blog.bytebytego.com/p/how-snapchat-serves-a-billion-predictions
**Date**: May 19, 2026
**Author**: ByteByteGo
**Keywords**: Snapchat, ML infrastructure, ranking systems, Bento, Robusta, feature store, inference optimization, recommendation systems

## Elevator pitch
Snapchat's ML platform "Bento" serves over a billion predictions per second across 477 million daily users by splitting recommendation workloads into a two-stage retrieval-ranking pipeline and collocating document features on inference instances to eliminate network fanout.

## Takeaways
- Snapchat processes ranking across four domains simultaneously: content feeds, ad auctions, friend suggestions, and AR lenses — each with different latency requirements and cost-of-error profiles
- The Bento platform splits into training (Kubeflow + TensorFlow/Keras, with YAML-configurable experiments enabling hundreds of daily iterations) and serving (where the real engineering complexity lives)
- Snap's feature platform "Robusta" processes 10 trillion events/day on Apache Spark, maintaining an 800TB online feature store serving 1TB/sec of reads, with Iceberg for offline training data
- The key architectural innovation: collocating document features directly on inference engine instances eliminates network fanout entirely — costly in memory but justified at Snap's scale
- GPU/CPU compute graph splitting (dense math on GPU, embeddings on CPU) avoids wasting scarce GPU memory on lookup tables while keeping latency within budget

## Synthesis
ByteByteGo's deep dive into Snap's ML infrastructure reveals how Snapchat's recommendation system operates at genuinely staggering scale: 946 million monthly active users, 474 million daily active users, one billion predictions per second, and 10 trillion events per day flowing through feature pipelines. The article examines the Bento platform, which powers all of Snap's ranking decisions — from content recommendations and ad auctions to friend suggestions and AR lens surfacing.

The architecture's core insight is the asymmetric nature of ranking workloads. A single user request fans out into thousands of (user, candidate) pairs that each need model scoring, creating a computational expansion that shapes every architectural decision. Bento handles this through a two-stage pipeline: cheap retrieval models filter millions of candidates to hundreds, then expensive ranking models score those candidates carefully.

The serving infrastructure is where the most interesting engineering lives. Snap's approach to the feature fanout problem is unusual: rather than fetching document features over the network for every candidate, they collocate the full document feature corpus on each inference instance's local memory. One user feature lookup triggers the request; the inference engine reads document features from local memory. At smaller scales this would be wasteful, but at Snap's scale the latency reduction justifies the memory cost. For corpora too large to fit locally, a separate Retrieval service handles ANN search, inverted index lookups, and forward index lookups in a single pass.

The feature platform "Robusta" addresses the fundamental train/serve skew problem — the central operational concern of every mature ML team. It processes 10 trillion daily events on Apache Spark, computes aggregated features over sliding time windows, and writes to both an offline Iceberg store and a fast online key-value store, ensuring both stores stay in sync.

Training is structured as three layers (Core framework, user model code, YAML configuration), enabling hundreds of experiments per day. The model export step splits compute graphs for different hardware: dense matrix multiplication on GPU, embedding lookups and feature parsing on CPU — avoiding resource waste patterns.

The article underscores that at this scale, ML isn't a feature — it's the product itself, and the infrastructure to support it must handle latency, scale, freshness, and iteration pressure simultaneously, despite these pulling in opposing directions.
