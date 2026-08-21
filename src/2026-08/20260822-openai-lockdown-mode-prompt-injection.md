# OpenAI Adds Lockdown Mode to Counter Prompt Injection
**Source**: https://tldrnewsletter.com (TLDR AI, 2026-06-08)
**Date**: 2026-06-08
**Author**: TLDR AI
**Keywords**: openai, prompt-injection, security, lockdown-mode, agent-security, adversarial-input

## Elevator pitch
OpenAI introduced Lockdown Mode to reduce exposure to prompt injection attacks from webpages and external content by disabling live browsing, web image retrieval, deep research, and agent mode while keeping cached content and image generation available.

## Takeaways
- Lockdown Mode disables live browsing, web image retrieval, deep research, and agent mode — the primary vectors for prompt injection from external content
- Some cached content and image-generation functionality remain available, balancing security with usability
- The feature targets the attack surface where malicious web content can inject instructions into an LLM's context, causing it to execute unintended actions
- Represents a recognition that agent capabilities (browsing, tool use) create security risks that require user-controllable mitigations
- Part of a broader industry trend toward giving users granular control over agent attack surfaces, trading capability for safety

## Synthesis
OpenAI's Lockdown Mode is a direct response to one of the most significant security challenges in LLM deployment: prompt injection. When an AI agent browses the web, retrieves images, or processes external content, that content becomes part of the model's context. Malicious actors can embed instructions in webpages, images, or documents that the model interprets as commands — causing the agent to perform unintended actions, exfiltrate data, or bypass safety guardrails.

Lockdown Mode addresses this by disabling the primary vectors for external content injection. Live browsing is turned off, meaning the agent cannot visit webpages that might contain malicious prompts. Web image retrieval is disabled, preventing injection through steganographic or text-in-image attacks. Deep research and agent mode — which involve multi-step autonomous actions that amplify the impact of a successful injection — are also disabled. The feature keeps cached content and image generation available, which are lower-risk because cached content has already been processed and image generation produces output rather than consuming external input.

This represents a broader industry recognition that agent capabilities and security are in tension. Every capability that makes an agent more useful — browsing, tool use, autonomous action — also creates an attack surface. Lockdown Mode gives users a dial to trade capability for safety, which is a pragmatic approach: not all use cases require autonomous web browsing, and for sensitive workflows the reduced capability is worth the security gain.

The feature is part of a maturing approach to AI security where mitigations are user-controllable rather than globally imposed. Different use cases have different risk profiles, and giving users the ability to restrict their agent's attack surface is more flexible than a one-size-fits-all security policy.