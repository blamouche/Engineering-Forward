# Universal Commerce Protocol (UCP)

**Source**: https://ucp.dev/

**Date**: Unknown

**Author**: Google, Shopify, Etsy, Wayfair, Target, and Walmart (collaborative development)

**Keywords**: Agentic commerce, checkout, identity linking, order management, OAuth 2.0, payment protocols, interoperability, open standard

## Elevator pitch

UCP is an open protocol that creates a universal language for platforms, AI agents, and businesses to conduct commerce transactions without requiring custom integrations for each merchant.

## Takeaways

- UCP provides standardized building blocks (Checkout, Identity Linking, Order Management) that enable any agent or platform to interact with any merchant
- Major industry players including Google, Shopify, Target, Walmart, Etsy, and Wayfair have collaborated to develop this open standard
- The protocol addresses the fragmented commerce landscape that causes cart abandonment and poor user experiences across chat, visual, and voice interfaces
- Security and merchant control are prioritized through OAuth 2.0 authentication and merchants remaining the Merchant of Record for all transactions
- The open-source design encourages community-driven development and extensibility beyond the initial core capabilities

## Synthesis

The Universal Commerce Protocol (UCP) represents a significant collaborative effort by major commerce players to standardize how AI agents, platforms, and businesses interact during commercial transactions. At its core, UCP aims to solve a fundamental problem in the emerging agentic commerce landscape: the lack of interoperability between different systems that leads to fragmented shopping experiences and abandoned carts.

The protocol introduces itself as "the common language for platforms, agents and businesses," establishing a set of standardized building blocks that enable ecosystem-wide interoperability without the need for custom integrations. This approach mirrors how HTTP standardized web communication, potentially doing the same for commerce in an AI-driven world.

UCP launches with three core capabilities. First, Checkout manages complex cart logic, dynamic pricing, and tax calculations across different businesses, providing a unified way to handle the purchase flow regardless of the merchant. Second, Identity Linking uses OAuth 2.0 to establish secure relationships between agents and merchants, ensuring that authentication and authorization follow proven security standards. Third, Order Management tracks purchases from confirmation through delivery, with real-time webhook updates keeping all parties informed of status changes.

The technical foundation of UCP is built on REST and JSON-RPC transports, with support for complementary protocols including the Agent Payments Protocol (AP2), Agent2Agent (A2A), and Model Context Protocol (MCP). This layered approach allows UCP to integrate with existing agent communication standards while focusing specifically on the commerce layer.

What makes UCP particularly noteworthy is the coalition behind it. Google, Shopify, Etsy, Wayfair, Target, and Walmart have joined forces to develop this standard, representing a rare alignment of both technology platforms and major retailers. This broad industry backing suggests the protocol has strong potential for widespread adoption.

The design principles emphasize scalability, merchant-centricity, and openness. Merchants retain full control as the Merchant of Record, meaning they maintain their relationship with customers and handle their own compliance requirements. The open-source nature invites community contributions and extensions beyond the initial feature set.

UCP addresses the reality that commerce is increasingly happening through conversational interfaces, voice assistants, and AI agents rather than traditional web storefronts. By providing a standardized protocol, it enables these new modalities to access merchant capabilities consistently, regardless of the underlying platform or agent technology. This could accelerate the adoption of agentic commerce by removing the integration burden that currently limits which merchants can participate in these emerging channels.
