# How Snapchat Serves a Billion Predictions Per Second
**Source**: https://blog.bytebytego.com/p/how-snapchat-serves-a-billion-predictions
**Date**: May 19, 2026
**Author**: ByteByteGo
**Keywords**: Snapchat, machine learning, ranking, recommendation systems, Bento, infrastructure, feature store, real-time inference

## Elevator pitch
Snapchat's Bento platform handles over a billion ML predictions per second across 477 million daily users by splitting model serving into retrieval and ranking stages, with a dedicated feature store processing 10 trillion events daily to prevent train-serve skew.

## Takeaways
- Bento is Snap's unified ML platform powering content recommendations, ad ranking, friend suggestions, and AR lens selection
- The architecture splits inference into retrieval (cheap models filtering millions to hundreds) and ranking (expensive models scoring final candidates)
- A key innovation is splitting compute graphs: dense matrix ops go to GPU while embedding lookups and feature parsing run on CPU
- Robusta, the feature platform, processes 10 trillion events/day and maintains consistency between offline training data and online serving data to prevent train-serve skew
- The system supports hundreds of ML experiments per month through a layered training architecture with shared frameworks and YAML configuration

## Synthesis
ByteByteGo's deep dive into Snapchat's ML infrastructure reveals how the social platform serves over a billion predictions per second to its 946 million monthly active users. At the core is Bento, a unified platform that powers four distinct ML-driven decisions: content recommendations in Discover and Spotlight feeds, ad auction ranking, friend suggestions, and AR lens selection. Each decision must complete within roughly 100 milliseconds while operating on a massive scale — a single user request expands into hundreds or thousands of individual model evaluations before returning a short ranked list to the user.

The architecture's fundamental insight is the two-stage split between retrieval and ranking. Cheap, lightweight models first filter the full corpus of millions of candidates down to a few hundred worth scoring, then expensive deep learning models score each surviving candidate in detail and produce the final order. This fanout pattern — one request expanding into thousands of internal evaluations — shapes every architectural decision in the platform. The compute is further optimized by splitting the trained model's graph: dense matrix multiplications run on GPU hardware while embedding lookups and feature parsing stay on CPU, avoiding the waste of running memory-bound and compute-bound operations on the same hardware.

The most consequential engineering challenge is maintaining consistency between the offline world where models train and the online world where they serve. Snap's Robusta feature platform, built on Apache Spark, processes 10 trillion events per day, computes aggregated features over sliding time windows, and writes results to both the analytical database used for training (Iceberg) and the low-latency key-value store used for serving. This synchronization prevents train-serve skew — the insidious class of bugs where models perform well in offline evaluation but fail in production because features are computed differently in each context. The training side enables rapid experimentation through a three-layer architecture: a shared Core framework on TensorFlow/Keras, individual model code, and YAML configuration, allowing hundreds of experiments per month with automated incremental retraining and deployment.
