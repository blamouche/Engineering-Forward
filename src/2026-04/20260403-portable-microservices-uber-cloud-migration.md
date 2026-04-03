# Portable Microservices Ready for the Cloud

**Source**: https://www.uber.com/blog/up-portable-microservices-ready-for-the-cloud
**Date**: Unknown
**Author**: Uber Engineering
**Keywords**: Uber, microservices, cloud migration, portability, Oracle, Google Cloud, µDeploy, infrastructure

## Elevator pitch
Uber migrated 4,500 stateless microservices to multi-cloud by building "portability"—services that can run in any zone automatically, enabling 100,000+ weekly deployments without manual placement management.

## Takeaways
- Uber's 4,500 stateless microservices are deployed 100,000+ times weekly by 4,000 engineers—a scale that makes manual placement management impossible
- "Portability" means a service can run in any zone within a region automatically—the key abstraction that made cloud migration feasible
- Previous µDeploy system containerized services but still required engineers to manually specify zones, creating bottlenecks for cloud migration
- In 2023, Uber partnered with Oracle and Google Cloud to reduce supply chain exposure after experiencing chip shortages affecting on-prem data centers
- Cloud migration required transforming thousands of services to be "automatically manageable" without human involvement in placement decisions

## Synthesis
Migrating 4,500 microservices to the cloud while keeping a global transportation business running is one of the more challenging infrastructure migrations in recent tech history. Uber's solution centers on a concept they call "portability"—and the engineering required to achieve it at scale reveals important lessons about infrastructure design.

The core insight is that service placement decisions shouldn't be made by individual service engineers. Before the portability system, engineers using µDeploy still had to specify which zone their service would run in. This worked when Uber ran entirely on-prem and the zone choices were familiar. But for cloud migration, it created an impossible coordination problem: thousands of engineers making thousands of placement decisions, each requiring cloud-specific knowledge they didn't have.

Portability inverts this: a portable service can run anywhere within a region, and the infrastructure system decides where based on capacity, latency, and operational requirements. Service engineers declare what their service needs; the infrastructure layer handles placement. This is the right abstraction—it separates concerns cleanly and enables the infrastructure team to make optimal placement decisions centrally.

The trigger for cloud migration was revealing: chip shortages and supply chain issues caused long lead times for on-prem hardware. The pandemic exposed the fragility of infrastructure strategies that depend on reliable hardware delivery. Oracle and Google Cloud partnerships diversified this exposure, but executing the migration required the portability abstraction to already be in place—you can't migrate 4,500 services manually.

The scale of Uber's deployment operation is worth appreciating. 100,000+ deployments per week across 4,500 services means roughly 14,000 deployments per day, many driven by autonomous systems rather than direct human action. At this scale, any manual step in the deployment process becomes a bottleneck. The portability work was, in part, about removing the last manual steps from the deployment critical path.

For engineering teams building microservice infrastructure: the lesson is to abstract placement decisions away from service engineers as early as possible. The services that are easiest to migrate are the ones that were designed to be placement-agnostic from the start. Design for portability before you need it, and the cloud migration becomes an infrastructure problem rather than a coordination problem spanning thousands of engineers.
