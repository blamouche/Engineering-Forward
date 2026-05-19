# How Snapchat Serves a Billion Predictions Per Second

**Source:** [ByteByteGo](https://blog.bytebytego.com/p/how-snapchat-serves-a-billion-predictions)
**Date:** 2026-05-19
**Author:** ByteByteGo

## Summary

A deep dive into Bento, Snap's unified ML platform that serves over 1 billion predictions per second to 474M daily active users. The architecture handles ranking workloads for content recommendations, ads, friend suggestions, and AR lenses under 100ms latency budgets.

## Key Takeaways

- **Asymmetric workload**: one user request fans out to hundreds/thousands of (user, candidate) scoring pairs, then collapses to a ranked list
- **Training half**: layered code structure (Core framework → user model code → YAML config) enables hundreds of experiments/day; GPU/CPU compute graph split at export
- **Feature store (Robusta)**: processes 10T events/day; 800TB online store serving 1TB/s reads; keeps offline (Iceberg) and online stores in sync
- **Two fanout strategies**: (1) collocate document features on inference instances, (2) dedicated Retrieval service with ANN search for larger corpora
- **Serialization was the bottleneck**: raw-byte feature transfer + custom Protobuf → 2x lower latency, 10x cheaper data plane
- **Continuous feedback loop**: every prediction logged → training data → incremental retraining → auto-deploy → monitoring for train/serve skew
- **K8s-inspired deployment control plane**: desired vs actual state reconciliation

## Key Numbers

- 946M MAU, 474M DAU
- 1B+ predictions/second
- 1TB/s feature reads
- 10T events/day
- 800TB online feature store
- 20x model size growth, 40x training data growth over 2 years

## Tags

ML infrastructure, recommendation systems, Snapchat, feature store, inference optimization, ranking, Bento

---

*Generated from: https://blog.bytebytego.com/p/how-snapchat-serves-a-billion-predictions*
