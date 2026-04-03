# The Uber Engineering Tech Stack, Part I: The Foundation

**Source**: https://www.uber.com/blog/tech-stack-part-one-foundation
**Date**: 2016
**Author**: Uber Engineering
**Keywords**: Uber, tech stack, microservices, infrastructure, Schemaless, Cassandra, Riak, MySQL, platform

## Elevator pitch
Uber's 2016 engineering tech stack overview reveals a "tree" architecture philosophy—common trunk with diverse branches—supporting global real-time operations with no safe downtime and 300+ cities.

## Takeaways
- Uber prioritizes availability and scalability above all else because it has no "free" users—every user is transactional (rider, driver, eater, courier) and relies on the system in real time
- The tech stack follows a "tree" metaphor: a common platform trunk shared by all teams, with different tool choices blooming as branches for different use cases
- Storage uses a mix of Schemaless (built in-house on MySQL for long-term storage), Riak, and Cassandra—each chosen for specific access patterns
- Uber runs an all-active multi-datacenter model: no "backup" datacenter exists, and every city is assigned to a primary data center with a secondary in a different location
- The principle: use existing tools until needs exceed their capabilities, then build in-house—avoiding premature optimization while maintaining flexibility

## Synthesis
Uber's 2016 tech stack overview is a snapshot of how one of the most complex real-time distributed systems in the world was engineered at a specific moment in its development. The context matters: this is a company that had been operating for six years, recently migrated from a Python monolith to microservices, and was expanding aggressively across 300 cities globally.

The "no free users" observation defines everything about Uber's engineering philosophy. Companies with freemium models can take their infrastructure offline without immediately losing money. Uber cannot. When the system is down, riders can't get rides and drivers can't make money. This drives the relentless prioritization of availability—not as a best practice but as a business necessity.

The all-active multi-datacenter model reflects this priority. By assigning every city to a primary data center with automatic failover to a different geographic location, Uber ensures that no single data center failure can take down the entire service. The engineering cost of this architecture is substantial—every write must be replicated, every read must handle the possibility of slightly stale data, every service must be designed to survive its primary data center disappearing. But the alternative—downtime during a data center failure—is unacceptable.

The storage strategy illustrates pragmatic tool selection. Schemaless (a MySQL-based key-value store built in-house) handled long-term data storage where the structure was clear and immutable. Riak and Cassandra handled high-availability, low-latency demands where availability took priority over consistency. Multiple storage systems serving different access patterns is characteristic of large-scale systems—one-size-fits-all databases rarely survive real-world scale.

The "tree" metaphor for the tech stack is useful for thinking about platform architecture generally. The trunk is standardized: common deployment infrastructure, common observability, common service communication protocols, common security patterns. The branches diverge where teams have genuinely different needs—some teams use Go, some use Python, some have specialized data processing requirements. Standardizing the trunk while allowing branch diversity is how large engineering organizations achieve both consistency and flexibility.

The article was published in 2016 but reads as a case study in principles that remain relevant: design for availability first, choose tools based on access patterns rather than familiarity, build in-house only when existing tools fail, and maintain a common platform foundation that all teams share.
