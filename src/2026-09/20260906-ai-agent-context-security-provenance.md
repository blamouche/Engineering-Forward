# AI Agent Context Security Needs Provenance, Not Just Prompt Injection Defense
**Source**: https://sunglasses.dev/blog/ai-agent-context-security-provenance-authorization
**Date**: 2026-08-31
**Author**: Sunglasses
**Keywords**: AI agent security, context provenance, prompt injection, retrieval poisoning, authorization, trust boundaries, agent workflow security, RAG security

## Elevator pitch
Sunglasses identifies a class of AI agent security failures where relevant context is treated as authority rather than evidence, and proposes provenance tracking — source, lineage, trust, and authorization — as the fix for three failure modes that span workflow security, retrieval poisoning, and protocol boundaries.

## Takeaways
- The core insight is that context (files, snippets, prior chat) helps an agent understand a task but should not automatically grant it the authority to decide what is true or allowed
- Three failure modes are identified: sibling files steering code repairs (cross-file dependency poisoning), copied evidence being counted as independent sources (evidence aggregation manipulation), and conversational trust being mistaken for permission (trust escalation)
- The fix is provenance: track source identity, lineage (what changed it), trust level, and authorization status for every context record before the agent acts
- Sunglasses 0.4.5 ships two detection patterns (GLS-RP-567 and GLS-RP-585) from this research, inside a 39-pattern release
- The research tested three narrow mechanisms with inert fixtures — no hostile code was executed, no credentials used, no external actions taken — making the findings reproducible and safe to verify

## Synthesis
Sunglasses' research on AI agent context security addresses a subtle but dangerous class of vulnerabilities that sits at the intersection of workflow security, retrieval poisoning, and protocol boundaries. The central argument is that the AI agent ecosystem has been so focused on prompt injection — adversarial text that overrides an agent's instructions — that it has missed a quieter and equally dangerous failure mode: treating relevant context as if it carried authority.

The first mechanism, cross-file dependency retrieval context poisoning, targets coding agents that retrieve related files to guide repairs. A sibling file can be relevant to a repair while still containing hostile instructions. The test used an inert hostile fixture that pointed a repair worker at a specific file and claimed an authorization check was missing, then a retrieved "validation" file containing instructions that could steer the patch decision. The trust boundary runs from an attacker-controlled sibling file through the repair context assembly to an autonomous patch decision.

The second mechanism involves evidence aggregation. When an agent retrieves multiple snippets that appear to be independent witnesses but actually share a single origin (copied through a summary and a rendered excerpt), it may count them as three independent sources confirming a claim. The Sunglasses scan blocks this by grouping evidence by its real origin before aggregation, preventing one source from masquerading as multiple.

The third mechanism involves conversational trust being mistaken for permission. Repeated claims of harmless intent in a chat session can start to look like authorization to the agent, even though no actual permission was granted. The fix requires a fresh permission check before any private data access or protected action, regardless of how much conversational context suggests the action is safe.

The proposed solution across all three mechanisms is provenance: every context record must carry its source identity, what changed it (lineage), its trust level, and what it is authorized to decide. If lineage or permission is missing, the agent should stop. This is a more principled approach than trying to detect and filter individual injection attempts, because it addresses the root cause — the absence of a trust model — rather than the symptoms.