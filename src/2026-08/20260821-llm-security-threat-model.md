# LLM Security Basics: The Full Threat Model
**Source**: https://blog.bytebytego.com/p/llm-security-basics-the-full-threat
**Date**: 2026-08-03
**Author**: ByteByteGo
**Keywords**: llm, security, threat-model, prompt-injection, owasp, agents

## Elevator pitch
A comprehensive mapping of LLM security threats organized as positions on a data pipeline rather than a flat list, revealing that the real damage concentrates wherever an agent holds private data, untrusted content, and an external channel simultaneously.

## Takeaways
- The root cause of most LLM vulnerabilities is that instructions and data arrive as a single token sequence with no marker separating commands from information — there is no equivalent of parameterized queries for natural language
- Indirect prompt injection (via retrieved content, emails, documents) is more dangerous than direct injection because it arrives during legitimate tasks and can bypass input filters, as demonstrated by the EchoLeak CVE-2025-32711 incident against Microsoft 365 Copilot
- The "lethal trifecta" defines where real damage occurs: an agent with access to private data, exposure to untrusted content, and an external channel — remove any one capability and the exposure drops significantly
- Model theft via API extraction (OpenAI layer recovery for $20) and training data extraction (ChatGPT verbatim training data recovery) are real but bounded — they're expensive, narrow, or already mitigated by providers
- Defense in depth is the only viable posture: no single filter holds, so organizations need input validation, retrieval hygiene, minimal tool permissions, output sanitization, monitoring, and human review for high-consequence actions

## Synthesis
ByteByteGo's threat model article is one of the clearest mappings of LLM security risks available. Rather than treating OWASP's Top 10 for LLMs as isolated items, it organizes them as positions on a data pipeline: input, retrieval, model, tools, output, and supply chain. This reframing reveals a mismatch in attention — the threats that generate the most concern (model theft, training-data extraction) are bounded and largely mitigated, while the threats that reach production (excessive agency, indirect injection, improper output handling) receive comparatively less investment.

The central insight is the "lethal trifecta": whenever an agent holds private data, processes untrusted content, and can send data externally, it can be directed by injected instructions to exfiltrate information. This pattern has already appeared in documented incidents: GitHub's MCP server was compromised via malicious issues to expose private repositories, GitLab's Duo leaked private repo contents through hidden instructions, and a Chevrolet dealership chatbot was manipulated into selling an SUV for $1.

The article also highlights a critical finding from a November 2025 study by OpenAI, Anthropic, and Google DeepMind that defeated twelve proposed defenses against prompt injection. The conclusion is that a single guardrail provides a false sense of security. The recommended approach borrows from Google DeepMind's CaMeL (treat the model as untrusted, use a separate privileged component) and Meta's Agents Rule of Two (an agent should satisfy at most two of three risky properties without human review). These are not complete solutions, but they represent the pragmatic state of the art for organizations deploying LLM-powered agents in production.