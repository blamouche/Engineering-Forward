# Slash for Agents — Agentic Commerce via MCP
**Source**: https://www.slash.com/platform/agents
**Date**: Unknown
**Author**: Slash Financial, Inc.
**Keywords**: Agentic commerce, MCP, AI agents, virtual cards, spend controls, payments, RSA encryption, human-in-the-loop

## Elevator pitch
Slash enables AI agents to autonomously manage corporate finances—creating cards, enforcing spend limits, and executing payments—through a standardized MCP interface with enterprise-grade security and human oversight.

## Takeaways
- MCP-Native Architecture: The platform exposes three core primitives (`list_endpoints`, `get_endpoint_schema`, `call_api_endpoint`) allowing any MCP-compatible agent to discover and interact with Slash's full API without custom integration.
- Cryptographic Card Protection: Card PAN and CVV data are encrypted using RSA-OAEP before reaching agents, ensuring that sensitive details remain tokenized and inaccessible even in case of prompt injection or model compromise.
- Human-in-the-Loop Governance: Read-only API keys trigger approval workflows for write operations, creating a "Agent Requests" system where proposed financial actions require dashboard review before execution.
- Broad Agent Compatibility: The solution works with Claude, GPT, Cursor, and any HTTP-capable MCP client—no proprietary SDKs or vendor lock-in required.
- Market Timing: Agentic commerce is projected to reach "$50B+ market by 2028," positioning Slash's offering at the intersection of AI capability maturation and fintech automation demand.

## Synthesis
Slash targets an emerging use case where AI agents increasingly need to execute financial decisions autonomously. Rather than requiring manual dashboard logins or custom API integrations, the company has standardized agent-to-finance communication through the Model Context Protocol—an open standard created by Anthropic. This positions Slash not as a niche tool but as infrastructure for what industry research suggests will be a multi-billion-dollar market segment by 2028.

The MCP server architecture operates at `mcp.slash.com/mcp` and requires only an API key for connection. Agents begin by querying `list_endpoints` to understand available financial operations (card creation, payments, account management). They then inspect endpoint schemas to understand parameter requirements. Finally, `call_api_endpoint` executes the actual operations. This three-step discovery-then-execution pattern reduces friction for developers while maintaining API stability.

The platform integrates with the full Slash ecosystem: virtual and physical card issuance, ACH and wire transfers, invoice management, expense report approval, and real-time transaction visibility. This breadth means agents can orchestrate complex financial workflows—for example, automatically approving contractor expenses within predefined limits, generating virtual cards for specific vendors, or reconciling invoices against transaction history.

Slash implements defense-in-depth security. RSA-OAEP encryption ensures agents never see raw card credentials. Card data is tokenized through Very Good Security (VGS), so plaintext numbers never touch Slash servers—satisfying PCI DSS requirements. "Agent Requests" enable human oversight: when an agent uses a read-only key, financial write operations return a 403 status with an approval URL rather than executing immediately.

For enterprises, this removes the false choice between AI velocity and financial control. For developers, the MCP standard eliminates reinvention. Claude Desktop, Cursor, GPT-based agents, and custom-built systems all speak the same language. Slash has already achieved $150M in annual revenue and serves 5,000+ businesses—positioning itself well to capture significant share of the emerging agentic commerce category.
