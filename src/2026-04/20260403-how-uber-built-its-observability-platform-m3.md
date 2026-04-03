# How Uber Built Its Observability Platform

**Source**: https://newsletter.pragmaticengineer.com/p/how-uber-built-its-observability-platform
**Date**: Unknown
**Author**: Gergely Orosz (Pragmatic Engineer)
**Keywords**: Uber, M3, observability, metrics, Chronosphere, Cassandra, time-series, monitoring

## Elevator pitch
Uber built M3—processing 600 million data points per second at peak—from scratch after two successive observability platforms failed to scale, driven by 10x annual data volume growth and split-brain issues with Cassandra.

## Takeaways
- Uber built M3 from scratch after their initial Graphite/Carbon/Whisper stack couldn't scale (not horizontally scalable, no replicas, capacity additions required taking offline for a week)
- A second-generation Cassandra-based stack worked temporarily but suffered split-brain issues when using Cassandra as a time-series database—the wrong tool for the job
- At peak, M3 processed 600 million data points per second, likely still one of the largest observability platforms in the world
- The team grew 10x year-on-year in data volume—fast enough that even the replacement systems needed to be replaced before they were fully mature
- Martin Mao, who led M3 engineering, later co-founded Chronosphere to bring efficient observability to other organizations facing similar scale challenges

## Synthesis
Building observability infrastructure for a system growing 10x per year is one of the hardest engineering problems in infrastructure. You're building for a scale you've never operated at, with requirements that change faster than the build cycle. Uber did this three times before getting to M3.

The progression is instructive. The original Graphite/Carbon/Whisper stack—the industry-standard observability setup circa 2015—had fundamental architectural limitations: not horizontally scalable, no replication, capacity additions required taking the system offline. For a company growing at Uber's rate, this was a slow-motion disaster. Martin Mao spent his first oncall week just deleting data to free up space.

The first replacement, built on Cassandra and ElasticSearch, worked well enough to survive Uber's second-largest peak load event (Halloween 2015) without an outage. But 10x growth isn't survivable with a system that scales by adding nodes indefinitely. At 700 Cassandra nodes, the team was already pushing the technology past its design limits. Worse, using Cassandra as a time-series database—which it wasn't designed for—introduced split-brain issues during the frequent networking failures Uber experienced at its data centers.

The fundamental problem with split-brain is that it corrupts your observability data at exactly the moment you most need it reliable. If your metrics platform fails during a network incident, you lose visibility precisely when you need it most. M3 was designed from the ground up to avoid this failure mode with a purpose-built time-series storage engine.

The resulting system was remarkable at scale: 600 million data points per second, processing metrics from infrastructure, microservices, and real-time business metrics (rides per second, payments processed). The open-source release of M3 allowed other organizations facing similar challenges to benefit from Uber's work.

The broader lesson is about tooling choices at scale. Cassandra as a key-value store is excellent; Cassandra as a time-series database is a square peg in a round hole. This kind of misalignment between tool design and use case is survivable at small scale but becomes catastrophic at large scale. Rigorous tool selection—using technology for what it was designed for—pays compounding dividends as systems grow.

Martin Mao took these lessons and founded Chronosphere to help other organizations avoid building M3 from scratch. The pattern is becoming common in infrastructure: engineers at hyperscalers build internal systems that no commercial product can match, realize the market gap they've identified, and start companies to fill it.
