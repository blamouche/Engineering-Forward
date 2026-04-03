# Rewriting Uber Engineering: The Opportunities Microservices Provide

**Source**: https://www.uber.com/blog/building-tincup-microservice-implementation
**Date**: Unknown
**Author**: Uber Engineering
**Keywords**: microservices, Uber, Tincup, MVCS, SOA, currency service, RFC, architecture

## Elevator pitch
Uber's implementation of Tincup—their currency and exchange rate microservice—illustrates the RFC-driven process and architectural patterns they established as they migrated hundreds of services from a monolith to microservices.

## Takeaways
- Uber requires RFC (Request for Comments) submissions before any new microservice to prevent duplicate efforts and surface collaboration opportunities across a rapidly growing organization
- The Tincup currency service exemplifies Uber's MVCS architecture pattern: Model-View-Controller-Service, separating persistence logic from application logic for easier layer replacement
- Currency and exchange rate data required a globally replicated datastore (UDR) rather than simple PostgreSQL, because all data centers need access for Uber's all-active architecture
- With hundreds of microservices in multiple languages, Uber invested heavily in standardized tooling and frameworks to streamline service development
- The RFC process serves dual purposes: quality improvement through review and de-duplication of parallel efforts

## Synthesis
Uber's move from monolith to microservices is one of the more thoroughly documented engineering transformations in tech history. The Tincup blog post provides a concrete, ground-level view of how that transition happened in practice—not just the high-level architecture, but the specific patterns, protocols, and process decisions that made it manageable.

The RFC process is the organizational innovation worth highlighting. In a rapidly growing engineering organization, teams inevitably build things that overlap with what other teams are already building—or are about to build. By requiring engineers to submit a high-level proposal before starting a new service, Uber created a structured review mechanism that served two distinct purposes: improving quality through expert review, and surfacing duplication or collaboration opportunities.

This isn't bureaucracy for its own sake. When you have hundreds of microservices and thousands of engineers, the cost of building duplicate services is enormous. An RFC that catches a duplicate before implementation begins saves months of engineering time. The discipline also forces the proposing team to think clearly about the service's purpose, architecture, and dependencies before writing code—a useful quality check on its own.

The MVCS pattern (Model-View-Controller-Service) represents Uber's hard-won learning about persistence layer coupling. They'd already migrated several datasets' persistence layers and found each migration expensive because application logic was coupled to storage details. By creating an explicit service layer where application logic lives, they separated concerns in a way that allows the persistence layer to evolve or be replaced without touching business logic. This is a classic software design principle applied at organizational scale.

The currency service is a good example of why global infrastructure matters for global businesses. Currency and exchange rates need to be accessible from every data center. Standard PostgreSQL with incremental IDs doesn't support global replication cleanly. UDR—Uber's globally replicated scalable datastore—was the right tool for this requirement, even if it added complexity.

The broader pattern: Uber's microservices transformation wasn't just a technical decision. It required RFC processes, new data stores, new language frameworks, new operational tooling, and new organizational structures. The technical architecture and the organizational architecture had to evolve together. Teams building microservices today face the same challenge—the technology is the easier part.
