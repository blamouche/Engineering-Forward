# OpenAI Secure MCP Tunnel: Connecting Private MCP Servers Without Exposing Them
**Source**: https://developers.openai.com/blog/connect-private-mcp-servers-to-openai-products
**Date**: 2026-05-28
**Author**: OpenAI
**Keywords**: openai, mcp, secure-tunnel, private-servers, enterprise-security, model-context-protocol

## Elevator pitch
OpenAI's Secure MCP Tunnel lets enterprises connect private, on-premises MCP servers to ChatGPT, Codex, and other OpenAI products without opening inbound firewall ports or exposing servers to the public internet — using a customer-run tunnel client that initiates and controls the connection.

## Takeaways
- Secure MCP Tunnel places a small, inspectable open-source tunnel client next to the private MCP server, which then initiates and controls the outbound connection to OpenAI
- The private MCP server stays behind the customer's network boundary — no inbound firewall ports, no public listener, no expanded network perimeter
- The tunnel client authenticates to OpenAI's tunnel control plane, while the product side uses an OpenAI-hosted tunnel endpoint — keeping the security boundary explicit
- Enterprise authentication is preserved: the MCP server's address stays private and is used only from inside the customer environment
- The approach avoids the wrong defaults of moving the MCP server, expanding the network perimeter, or introducing another connectivity vendor
- Works with ChatGPT, Codex, the Responses API, and other supported OpenAI surfaces that need to call private MCP tools

## Synthesis
OpenAI's Secure MCP Tunnel solves a fundamental tension in enterprise MCP deployments: how to give AI products access to private, on-premises tools without exposing those tools to the public internet. The solution is architecturally elegant — instead of asking customers to move their MCP server, expand their network perimeter, or introduce a third-party connectivity vendor, OpenAI places a small, inspectable open-source tunnel client next to the private server.

The tunnel client initiates and controls the connection. It authenticates to OpenAI's tunnel control plane using outbound HTTPS, forwards MCP requests locally to the private server, and returns responses through the same tunnel. The private MCP server address is never exposed publicly — it stays inside the customer-controlled environment and is used only from within that environment. This keeps the security boundary explicit and auditable.

The design respects enterprise constraints at every layer. The MCP server remains private, on-premises, or behind existing access controls. The only network requirement is that the host running tunnel-client can make outbound HTTPS requests to OpenAI and reach the private MCP server. Enterprise authentication flows are preserved because the MCP address stays private. This is a practical answer to the question of how enterprises adopt MCP at scale — by making the connection path secure by default rather than requiring customers to compromise their network architecture. For organizations building internal tool ecosystems around MCP, Secure MCP Tunnel removes the last major barrier to connecting those tools to AI products.