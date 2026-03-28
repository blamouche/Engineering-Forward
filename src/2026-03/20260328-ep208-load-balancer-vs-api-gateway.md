# EP208: Load Balancer vs API Gateway
**Source**: https://blog.bytebytego.com/p/ep208-load-balancer-vs-api-gateway
**Date**: March 28, 2026
**Author**: Unknown
**Keywords**: load balancer, api gateway, traffic distribution, rate limiting, authentication, observability

## Elevator pitch
A concise system design refresher that clarifies how load balancers distribute traffic while API gateways enforce policy and orchestration, and why mature architectures use both together.

## Takeaways
- Load balancers focus on distributing traffic, health checks, and failover at L4/L7.
- API gateways add policy controls like rate limiting, auth, and request/response transformations.
- Gateways can aggregate multiple backend services behind one client-facing API.
- Observability is a core gateway function, providing centralized logging and monitoring.
- The common pattern is gateway in front, load balancer behind, each doing its specialized job.

## Synthesis
ByteByteGo’s EP208 refresher draws a clean line between two components that often get lumped together: load balancers and API gateways. A load balancer is described as a focused traffic distribution layer. It accepts requests from clients and spreads them across backend instances to keep any single server from being overwhelmed. The piece highlights standard operational functions like health checks and failover, and notes that load balancers can work at both the transport layer (L4) and the application layer (L7), depending on how granular the routing needs to be.

An API gateway, by contrast, is framed as a control plane for inbound API traffic rather than a pure distribution layer. The gateway still receives HTTP requests from clients, but it enforces policy before anything hits the backend. Rate limiting protects services from abuse or runaway clients, authentication and authorization gate access, and observability features centralize logging and monitoring. The gateway can also transform requests and responses, reshaping payloads as they pass between external clients and internal services. Another emphasized capability is API aggregation, where the gateway can combine calls to multiple services so clients do not need to orchestrate complex workflows themselves.

The article’s practical conclusion is that these tools are complementary rather than competing. The gateway handles the “smart” front‑door responsibilities—policy, routing logic, and interface shaping—while the load balancer handles even distribution across the instances that ultimately serve a given API. In production microservice setups, this pairing yields clearer responsibilities and better scalability. The gateway protects and organizes traffic, and the load balancer ensures that the approved traffic is spread efficiently and resiliently across the infrastructure. The result is a cleaner separation of concerns and fewer architectural surprises when systems scale.
