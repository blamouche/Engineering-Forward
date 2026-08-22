# The Mathematics of Multi-Tenancy
**Source**: https://www.bitsxpages.com/p/the-mathematics-of-multi-tenancy
**Date**: 2026-06-01
**Author**: Almog Gavra (bits & pages)
**Keywords**: multi-tenancy, S3, statistics, partitioning, workload-correlation, Pareto-distribution, heat-ratio, infrastructure, capacity-planning

## Elevator pitch
A statistical model for understanding multi-tenancy economics reveals why S3's multi-tenant architecture works perfectly (massive tenant count, uncorrelated workloads, Reed-Solomon file splitting) but why most companies can't replicate it — correlated workloads and size skew push the heat ratio past the breakeven threshold.

## Takeaways
- Multi-tenancy's economic benefit is measured by the heat ratio H = max(x)/avg(x) — the ratio of peak to average workload; the economics work when a vendor's H ≤ 2.0
- S3 works because: massive tenant count, foundational API serving diverse use cases (uncorrelated workloads), and Reed-Solomon coding making file splits the unit of tenancy
- Correlated workloads (ρ ≥ 0.25 shared component) corrode multi-tenant efficiency — no amount of tenants fixes this
- Pareto-distributed workloads (80:20 size skew) also push H near 2.0 even with zero correlation, requiring many more tenants to pool smaller ones
- Recall.ai's meeting-recording workload (correlated to meeting start times at top of the hour) is a real-world example where multi-tenancy doesn't flatten the curve

## Synthesis
Almog Gavra builds a statistical model to explain why multi-tenancy works so well for S3 but fails for most other systems. The investigation began with an X thread about an S3 customer whose bucket migration triggered a swarm of 503 errors, revealing that S3 prevents users from explicitly defining partitions — a decision that surprised the author as an infrastructure engineer who likes controlling partition placement.

The model's key output is the heat ratio H = max(x)/avg(x), measuring the gap between peak and average workload. For multi-tenancy to be economically viable, the vendor's H must be low enough (modeled as ≤ 2.0) that they can still take margin while charging less than self-hosting cost. An idealized simulation with uncorrelated, equally-sized workloads shows H converging to 1.0 as tenant count increases — the theoretical best case.

Three factors erode this ideal. First, workload correlation: if customers share time zones, seasonality, or usage patterns, the smoothing effect disappears regardless of tenant count. Even a 25% shared workload component pushes H near 2.0. Second, size skew: real workloads follow the Pareto Principle (20% of workloads account for 80% of volume), which doesn't raise H's floor the way correlation does but requires many more tenants before smaller ones pool together. Third, combining correlation with size skew creates the worst case.

S3 succeeds because three conditions map perfectly to the model's requirements: massive tenant count, a foundational API so basic it serves everything from warehouse analytics to vector databases (ensuring uncorrelated workloads), and Reed-Solomon error coding that splits objects across shards — making a file split, not even a full object, the unit of tenancy. This last point is crucial: even Pareto-distributed customers can't create hot spots because individual objects are spread across many shards.

The practical lesson is that infrastructure builders should deeply consider these dynamics before assuming multi-tenancy will drive down pricing. The author cites Recall.ai as a real-world example: their meeting-recording infrastructure has workloads correlated to meeting start times (top of the hour), so multi-tenancy doesn't flatten their aggregate curve and can even make the peak/average ratio more dramatic. Their solution is to push the problem to a lower layer by building on S3, which can multiplex their workload with many other different ones. The simulation code is available on GitHub.