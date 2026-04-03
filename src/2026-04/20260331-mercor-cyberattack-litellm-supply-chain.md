# Mercor Hit by Cyberattack Tied to Compromise of Open Source LiteLLM
**Source**: https://techcrunch.com/2026/03/31/mercor-says-it-was-hit-by-cyberattack-tied-to-compromise-of-open-source-litellm-project/
**Date**: March 31, 2026
**Author**: Jagmeet Singh (TechCrunch)
**Keywords**: Mercor, LiteLLM, supply chain attack, cybersecurity, open source, extortion, Lapsus$

## Elevator pitch
Mercor confirmed a data breach traced to a compromise of the open-source LiteLLM proxy project, illustrating software supply chain risk for AI infrastructure that depends on third-party LLM routing libraries.

## Takeaways
- Mercor (AI recruiting startup) confirmed a breach tied to compromised LiteLLM open-source project
- LiteLLM is a popular proxy server for language models; widely used in AI application infrastructure
- Extortion-focused hacking group (linked to Lapsus$) claimed responsibility and threatened to release stolen data
- Attackers gained access through the LiteLLM supply chain rather than directly attacking Mercor's systems
- The breach illustrates AI-specific supply chain risk: LLM routing/proxy libraries are attack surface

## Synthesis
The Mercor breach via LiteLLM highlights a supply chain risk category specific to AI infrastructure. LiteLLM is a proxy server that routes requests to multiple LLM providers through a unified interface, allowing organizations to call OpenAI, Anthropic, and other providers without managing separate API integrations. It occupies a privileged position in AI application architectures: it sits between applications and LLM providers, handling API keys, routing logic, and request/response processing for all AI operations.

This privileged position makes LiteLLM an attractive supply chain attack target. A compromised LiteLLM instance has access to LLM API keys (potentially enabling unauthorized API usage), request and response data (potentially containing sensitive information processed by the AI application), and the application's LLM routing configuration. The attack surface is comparable to compromising an authentication library or an API gateway — the component's central role in the architecture means that compromising it affects everything downstream.

The Lapsus$ attribution (if accurate) fits the group's established pattern of targeting software supply chains and extorting companies rather than pursuing nation-state-style persistent access. The extortion model requires demonstrating data exfiltration credibly enough to motivate payment, which means attackers need to have collected something worth paying to suppress.

For engineering teams evaluating AI infrastructure dependencies, the LiteLLM compromise is a reminder that the expanded dependency surface of modern AI applications — which often include LLM routing, vector databases, embedding services, and AI-specific infrastructure — extends the attack surface beyond traditional software dependencies. Security review processes that were designed for web application dependencies need to extend to AI-specific infrastructure components.

The timing — concurrent with the Claude Code source map leak and the Axios npm trojan — suggests that AI infrastructure is experiencing increased attacker attention as the value of these systems becomes more apparent. Organizations building on open-source AI infrastructure components should apply the same supply chain security practices (dependency pinning, hash verification, vendor security review) that mature organizations apply to other critical dependencies.
