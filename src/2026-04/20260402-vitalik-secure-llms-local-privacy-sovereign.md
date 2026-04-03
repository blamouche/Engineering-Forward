# My Self-Sovereign / Local / Private / Secure LLM Setup, April 2026
**Source**: https://vitalik.eth.limo/general/2026/04/02/secure_llms.html
**Date**: April 2, 2026
**Author**: Vitalik Buterin
**Keywords**: local LLM, privacy, security, self-sovereign AI, NixOS, llama-server, Apple Silicon, Qwen, AMD Ryzen AI

## Elevator pitch
Vitalik Buterin documents a privacy-first local LLM infrastructure using NixOS, llama-server, and Qwen3.5:35B, warning against OpenClaw agent security vulnerabilities and normalizing the feeding of personal data to cloud AI.

## Takeaways
- Three hardware options evaluated: NVIDIA 5090 laptop (90 tokens/s), AMD Ryzen AI Max Pro (51 tokens/s), DGX Spark (60 tokens/s) — 50+ tokens/s is the acceptable threshold
- Software stack: NixOS for reproducibility, llama-server (preferred over Ollama), ComfyUI for image/video
- Warns: OpenClaw agents can modify critical settings without confirmation; genuine security vulnerabilities in mainstream AI agent frameworks
- Core philosophy: privacy, security, and self-sovereignty as non-negotiable; rejects normalization of "feeding your entire life to cloud-based AI"
- Catalogs genuine threats: jailbreaks, data exfiltration, potential backdoors in open-weight models

## Synthesis
Buterin's local LLM setup documentation is notable for its author and for the seriousness with which it treats the security and privacy implications of AI assistant deployment. The piece comes from someone with significant technical expertise and strong views on self-sovereignty, and it represents a coherent alternative to the cloud-first AI assistant model that most users accept without much examination.

The hardware analysis is practically grounded. The 50+ tokens/second threshold is Buterin's observed minimum for acceptable interaction quality — below this, generation speed becomes perceptible as a limitation on interaction flow. All three hardware options he evaluates exceed this threshold, validating that current consumer and prosumer hardware is sufficient for capable local inference without cloud dependency. The AMD Ryzen AI Max Pro at 51 tokens/second is the most accessible option, suggesting that high-performance local inference is no longer exclusively available to hardware enthusiasts with NVIDIA GPUs.

The NixOS preference reflects a concern about reproducibility and predictability that is consistent with the security-first approach. NixOS's declarative system configuration means that the AI inference environment can be specified precisely and reproduced reliably — a property important for security auditing and for confidence that the environment behaves as expected. Ollama's convenience abstractions apparently create enough opacity that Buterin prefers the lower-level llama-server for confidence about what the system is actually doing.

The warning about OpenClaw agents modifying critical settings without confirmation is a concrete security concern. Agent frameworks that can execute system modifications without confirmation flows create an attack surface where manipulated prompts can cause agents to take damaging actions. This is a recognized risk in agentic AI design, but Buterin's documentation of it as a reason to avoid certain tools reflects appropriate wariness.

The broader philosophical point — rejecting the normalization of feeding personal data to cloud AI — positions this not as an extreme position but as a reasonable response to genuine risks. For individuals and organizations handling sensitive information, the architecture of processing that information locally rather than through cloud APIs is worth the additional operational complexity.
