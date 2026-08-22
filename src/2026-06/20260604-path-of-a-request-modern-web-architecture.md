# The Path of a Request: A Tour of Modern Web Architecture
**Source**: https://blog.bytebytego.com/p/the-path-of-a-request-a-tour-of-modern
**Date**: 2026-06-04
**Author**: ByteByteGo (Alex Xu)
**Keywords**: web-architecture, system-design, dns, cdn, load-balancing, caching, database, latency, scalability

## Elevator pitch
ByteByteGo traces the journey of a web request through roughly ten distinct systems — from DNS resolution through CDN, load balancing, caching, and database — showing how each layer forms a funnel that absorbs traffic before passing the rest along, with latency spent at every hop.

## Takeaways
- A web page loads in under a second, but in that second a single user request may pass through roughly ten distinct systems on its way to and from the database
- Each layer in the modern web stack absorbs as much traffic as it can before passing the rest along, forming a funnel with most traffic handled long before it reaches the bottom
- The journey starts before the request has fully left the browser, with latency spent at every hop
- DNS is the first stop: resolving the domain name to an IP address, with TTL and caching strategies that determine how quickly changes propagate
- Understanding what each layer does and what trade-off it makes leads to a better grasp of each component of a modern web stack
- The article asks two questions at each stop: what is this layer doing, and what trade-off is it making?

## Synthesis
ByteByteGo's "The Path of a Request" article takes a fundamentally different approach to explaining modern web architecture: rather than describing each component in isolation, it follows the journey of a single web request one hop at a time, from the moment it leaves the browser to the moment it reaches the database and back.

The core insight is that a web page loads in under a second, but in that second, a single user request may pass through roughly ten distinct systems. The page feels fast because of how those systems are arranged. Each layer absorbs as much traffic as it can before passing the rest along. Taken together, the layers form a funnel, with most traffic handled long before it reaches the bottom. This funnel design is what makes modern web applications performant at scale — a DNS cache absorbs repeated lookups, a CDN serves static content without touching the origin, a load balancer distributes traffic across multiple servers, and a cache layer serves hot data without hitting the database.

At each stop in the journey, the article asks two questions: what is this layer doing, and what trade-off is it making? This framing is valuable because every layer in the stack represents a trade-off between consistency, availability, latency, cost, and complexity. DNS trading propagation delay for reduced lookup latency. CDN trading cache freshness for reduced origin load. Load balancers trading session affinity for even distribution. Caches trading data consistency for read speed. Each trade-off is a deliberate engineering choice, not an accident.

The journey starts before the request has fully left the browser, and latency is spent at every hop. This end-to-end perspective is what makes the article distinctive — most system design resources describe components individually, but the path of a request through the stack reveals how they interact, where bottlenecks accumulate, and why the arrangement of layers matters as much as the layers themselves. For engineers building or scaling web applications, understanding this funnel — and the specific trade-off at each layer — is essential for diagnosing performance issues and making informed architectural decisions.