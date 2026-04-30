# stripe/link-cli: Let your agents spend on your behalf. Your payment credentials are never exposed. You approve every purchase.

**Source**: https://github.com/stripe/link-cli
**Date**: April 30, 2026
**Author**: Stripe
**Keywords**: payments, agents, cli, mcp, commerce

## Elevator pitch
Stripe's Link CLI gives agents one-time payment credentials and human approval flows, aiming to let software buy things without exposing a user's real card details.

## Takeaways
- Link CLI connects an agent to a Link wallet and returns one-time payment credentials instead of persistent card details.
- Approval remains human-controlled through push notifications or email, which keeps the agent inside a bounded spending loop.
- The tool can also act as an MCP server so local agent environments can call payments through a standard interface.
- Stripe supports both virtual-card checkout flows and shared payment tokens for merchants using the Machine Payments Protocol.
- The product suggests payments infrastructure is being redesigned for agent-mediated commerce, not just human checkout.

## Synthesis
Stripe's link-cli is a concrete attempt to make autonomous purchasing safe enough for practical agent use. The core idea is simple: an agent should be able to complete a purchase, but it should never hold a user's permanent payment credentials. Instead, the CLI connects to a Link wallet, lets the user approve a spend request, and returns a short-lived credential that can be used for a specific merchant and transaction context. Stripe layers this with support for human approvals, structured JSON outputs, and MCP integration so the tool can fit directly into modern agent environments. It also supports both traditional browser-style checkout using virtual cards and a newer machine-to-machine flow using shared payment tokens and the Machine Payments Protocol. That makes the project more than a developer convenience. It is part of a broader effort to build a payments control plane for agents, where approval, identity, credential issuance, and transaction limits are all first-class primitives. The practical significance is that commerce for agents needs different infrastructure from commerce for people: tighter scopes, explicit approvals, programmable credentials, and auditable machine-readable interfaces. Stripe appears to be building that layer before agent shopping becomes mainstream.
