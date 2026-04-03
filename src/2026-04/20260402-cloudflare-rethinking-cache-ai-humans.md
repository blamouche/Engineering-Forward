# Why Cloudflare is Rethinking Cache for the AI Era
**Source**: https://blog.cloudflare.com/rethinking-cache-ai-humans/
**Date**: April 2, 2026
**Author**: Avani Wildani and Suleman Ahmad (Cloudflare)
**Keywords**: CDN, cache, AI crawlers, bot traffic, cache replacement, AI infrastructure, web performance

## Elevator pitch
AI bot traffic (10 billion weekly requests, 32% of Cloudflare's network) exhibits 70-100% unique URL ratios that defeat traditional LRU caching, requiring AI-aware cache replacement algorithms and separate AI/human cache tiers.

## Takeaways
- 32% of all Cloudflare network traffic is automated; AI crawlers show 70-100% unique URL ratios vs. human traffic patterns
- AI crawlers access long-tail and loosely related content unlike human focus on popular pages
- Wikipedia saw 50% surge in multimedia bandwidth; Read the Docs and Fedora faced service instability from crawlers
- LRU cache replacement fails for AI traffic; Cloudflare is exploring SIEVE, S3FIFO, and ML-based algorithms
- Separate cache tiers for AI vs. human traffic, routing based on latency tolerance and task type

## Synthesis
Cloudflare's cache rethinking analysis reveals an infrastructure consequence of AI adoption that is not widely appreciated: AI crawlers are not just more traffic, they are qualitatively different traffic that existing caching infrastructure was not designed to serve.

Traditional content delivery networks are optimized for human access patterns. Humans exhibit strong content popularity skew — a small fraction of URLs receive the vast majority of traffic, making LRU (Least Recently Used) caching highly effective. When a popular article is requested by a thousand users in an hour, it gets cached on the first request and served from cache for the remaining 999. Cache hit rates of 80-90% are achievable for human traffic with standard LRU policies.

AI crawler patterns are fundamentally different. A language model indexing web content for retrieval or training systematically explores the full URL space, including long-tail content that humans rarely access. The 70-100% unique URL ratio observed means that for every 10 crawler requests, between 7 and 10 are for content that has not been cached from a previous request. LRU caching provides near-zero benefit for this access pattern because cached entries are not reused before they are evicted.

The practical impact on origin servers is severe. Cache hit rates that approach zero under AI traffic mean proportionally more requests hit origin servers, which are not provisioned for this traffic volume. Wikipedia's 50% multimedia bandwidth surge demonstrates the scale: AI systems training on web content can generate traffic that dwarfs the human baseline on specific content types.

The proposed solutions reflect the structural nature of the problem. SIEVE and S3FIFO are cache replacement algorithms designed to handle access patterns with lower hit rate potential more efficiently than LRU. ML-based algorithms that predict which content will be accessed again — effectively modeling AI crawler behavior as a distinct traffic class — offer the potential to adapt dynamically to observed patterns. The separate cache tier approach is the most direct: route AI traffic to infrastructure designed for its access pattern rather than forcing it through infrastructure optimized for human behavior.

For organizations operating web infrastructure, the implication is that AI crawler traffic requires dedicated capacity planning rather than being absorbed into headroom above human baseline projections.
