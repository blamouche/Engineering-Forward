# Streaming vs Batch: Two Philosophies of Data Processing
**Source**: https://blog.bytebytego.com/p/streaming-vs-batch-two-philosophies
**Date**: 2026-07-09
**Author**: ByteByteGo
**Keywords**: streaming, batch processing, data engineering, watermarks, lambda architecture, kappa architecture, exactly-once processing

## Elevator pitch
The fundamental question in data processing—when is data complete enough to compute on?—splits the field into two philosophies, and understanding both is essential for building reliable data systems.

## Takeaways
- Batch processing waits for completeness: it collects data up to a natural boundary and then computes over the whole set at once, prioritizing correctness over speed.
- Streaming prioritizes speed over completeness: it produces answers from data that is still arriving, requiring estimates of when "enough" data has arrived and handling cases where those estimates are wrong.
- On the batch side, strategies include full loads, incremental loads, and large-window aggregation, with micro-batch sitting in between as a compromise.
- On the streaming side, the territory covers tumbling, sliding, and session windows; watermarks and late data handling; lambda and kappa architectures; and the often-misunderstood meaning of exactly-once processing.
- The trade-off between completeness and latency is the key consideration: every system that processes data eventually has to answer the question of when data is "complete enough."

## Synthesis
ByteByteGo's technical deep dive frames data processing as fundamentally about one question: when is data complete enough to be moved to the compute stage? The answer determines whether you're in the batch or streaming camp, and the article systematically walks through both.

For batch processing, completeness is the default. A program adding up a day's sales needs all of today's sales to have arrived. Files have ends, so batch works naturally with file-based data. The strategies here are well-established: full loads that replace the entire dataset, incremental loads that only add new or changed records, and large-window aggregation that mimics streaming by using time windows measured in hours or days.

Streaming takes the opposite bet. Data arrives continuously and never stops, so there's no clean boundary. Instead, streaming systems use windows—tumbling (fixed-size, non-overlapping), sliding (fixed-size, overlapping), and session (activity-based, variable-size)—to create artificial boundaries. Watermarks provide the mechanism for tracking how far through the data stream a system has progressed, and late data handling deals with the inevitable reality that data arrives after its window has closed.

The lambda and kappa architectures represent the two philosophical endpoints. Lambda keeps both a batch layer (for correctness) and a speed layer (for latency), merging results at serving time. Kappa argues that you can do everything with streaming if you handle it correctly, using replay to recompute when needed. The article explains that exactly-once processing, often cited as a key differentiator, is more nuanced than it appears—it depends heavily on what "exactly once" means at different system boundaries and whether end-to-end exactly-once is actually achievable or even desirable.

For engineering teams, the practical takeaway is that this isn't an either/or choice. Most production systems use a blend: streaming for latency-sensitive paths and batch for correctness-critical paths, with micro-batch filling the gap in between.