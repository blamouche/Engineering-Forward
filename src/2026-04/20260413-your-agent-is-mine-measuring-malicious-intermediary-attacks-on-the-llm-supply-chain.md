# Your Agent Is Mine: Measuring Malicious Intermediary Attacks on the LLM Supply Chain

**Source**: https://arxiv.org/abs/2604.08407
**Date**: April 13, 2026
**Author**: Yanju Chen et al.
**Keywords**: LLM security, supply chain, routers, secret exfiltration, arXiv

## Elevator pitch
This paper argues that third-party LLM routers are a major supply-chain risk because they can silently inject payloads or exfiltrate secrets, and the authors show the problem is not theoretical.

## Takeaways
- This paper argues that third-party LLM routers are a major supply-chain risk because they can silently inject payloads or exfiltrate secrets, and the authors show the problem is not theoretical.
- The paper studies a part of the LLM stack that is easy to ignore: API routers that sit between an agent framework and the upstream model provider. Because these routers see raw prompts, tool calls, and sometimes secrets in plaintext, they are in a position to inject malicious content or steal sensitive data without either endpoint noticing.
- What makes the work important is that the authors did not stop at theorizing. They report observing active malicious behavior in a subset of paid and free routers, including prompt injection, adaptive evasion, canary credential access, and even asset theft. They also use their own research proxy to evaluate client-side defenses such as fail-closed policy gates and append-only logging.
- The broader takeaway is brutal but useful: if your agent stack depends on opaque intermediaries, then model alignment is not your only trust boundary. The transport and routing layer can become the attack surface, and that means agent security needs integrity checks, logging, and explicit distrust of convenience routers by default.

## Synthesis

The paper studies a part of the LLM stack that is easy to ignore: API routers that sit between an agent framework and the upstream model provider. Because these routers see raw prompts, tool calls, and sometimes secrets in plaintext, they are in a position to inject malicious content or steal sensitive data without either endpoint noticing.

What makes the work important is that the authors did not stop at theorizing. They report observing active malicious behavior in a subset of paid and free routers, including prompt injection, adaptive evasion, canary credential access, and even asset theft. They also use their own research proxy to evaluate client-side defenses such as fail-closed policy gates and append-only logging.

The broader takeaway is brutal but useful: if your agent stack depends on opaque intermediaries, then model alignment is not your only trust boundary. The transport and routing layer can become the attack surface, and that means agent security needs integrity checks, logging, and explicit distrust of convenience routers by default.
