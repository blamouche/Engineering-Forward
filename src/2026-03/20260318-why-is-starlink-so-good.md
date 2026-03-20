# Why is Starlink on planes so good?
**Source**: https://stardrift.ai/blog/why-is-starlink-so-good
**Date**: 2026-03-18
**Author**: Leila Clark
**Keywords**: Starlink, satellite internet, aviation connectivity, latency, throughput, LEO, SpaceX

## Elevator pitch
Starlink's low-Earth-orbit constellation delivers the first in-flight internet combining both great latency and great throughput, solving the fundamental tradeoff that plagued all previous aviation connectivity technologies.

## Takeaways
- Quality internet requires two metrics: low latency (request-response delay) and high throughput (data speed)
- Air-to-ground towers offered good latency but poor throughput and no oceanic coverage
- Geostationary satellites at 36,000 km altitude provide good throughput but ~500ms latency due to distance
- Starlink's ~10,000 LEO satellites are 50x closer than geostationary alternatives, proportionally reducing latency while preserving throughput
- Starlink satellites cost $1-2M to launch (100x cheaper than competitors) and SpaceX earns $8B of its $15B revenue from this segment

## Synthesis
In-flight internet has historically forced a hard tradeoff: you could have speed or responsiveness, but not both. Leila Clark's piece for Stardrift explains why Starlink finally resolves this dilemma by attacking the physics of the problem directly.

The first generation of aviation connectivity used air-to-ground (ATG) towers, a technology dating to around 2008. ATG delivered excellent latency—signals only need to travel a few kilometers to the nearest tower—but throughput was severely limited, ocean crossings were impossible, and the system could not cope with the data appetites of modern streaming services.

Geostationary (GEO) satellites attempted to fix the coverage problem by positioning themselves 36,000 km above Earth, creating a fixed point that any aircraft could see from anywhere on the planet. The throughput improved dramatically, but physics imposed an unavoidable penalty: with light traveling at roughly 300,000 km/s, even a one-way trip takes about 120ms. Round-trip latency of approximately 500ms made anything interactive—video calls, games, real-time web browsing—frustratingly sluggish.

Starlink sidesteps the GEO problem entirely. By deploying approximately 10,000 satellites in low Earth orbit, SpaceX created a constellation where any aircraft is always within 550-1,200 km of a satellite—roughly 50 times closer than geostationary alternatives. That geometric advantage directly translates into proportionally reduced latency while preserving throughput comparable to ground-based broadband.

The economics are equally novel. Each Starlink satellite costs $1-2 million to manufacture and launch, a figure approximately 100 times cheaper than traditional telecommunications satellites. Their five-year design life enables regular technology refresh without stranded capital. SpaceX has already reached profitability in this segment—$8 billion of $15 billion total revenue—demonstrating that accessible connectivity in remote and mobile environments is not just technically achievable but commercially sound. Clark's analysis frames Starlink not merely as an incremental improvement but as the first connectivity architecture genuinely adequate for the demands of modern digital work at altitude.
