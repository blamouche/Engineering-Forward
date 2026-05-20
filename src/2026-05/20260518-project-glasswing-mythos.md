# Project Glasswing: What Mythos Showed Us
**Source**: https://blog.cloudflare.com/cyber-frontier-models/
**Date**: May 18, 2026
**Author**: Grant Bourzikas (Cloudflare)
**Keywords**: Mythos Preview, Anthropic, vulnerability research, cybersecurity, LLM, exploit chain, Project Glasswing, Cloudflare, AI security

## Elevator pitch
Cloudflare tested Anthropic's Mythos Preview on over 50 of their own repositories and found it represents a genuine step-change in AI-powered vulnerability research — capable of chaining exploits and generating working proofs, but requiring careful harness architecture rather than naive agent deployment to achieve meaningful coverage.

## Takeaways
- Mythos Preview can construct multi-step exploit chains (e.g., use-after-free to ROP chain) and generate working proof-of-concept code by compiling and iterating against results — capabilities no previous model demonstrated end-to-end
- Organic model refusals exist but are inconsistent: semantically equivalent tasks produce opposite outcomes depending on framing, making them unreliable as safety boundaries without additional safeguards
- Signal-to-noise remains the dominant operational challenge: models over-report with "possibly/potentially/could in theory" hedging, but Mythos Preview's PoC-generation capability dramatically reduces triage cost — a finding with a PoC is actionable
- Pointing a generic coding agent at a repository doesn't work for vulnerability research — it requires narrow, parallel hypotheses with adversarial review, not single-stream exploration
- Cloudflare's harness architecture uses narrow-scoped parallel agents, adversarial review (two agents in deliberate disagreement), chain-splitting across agents, and deduplication — a fundamentally different interaction model than chat or coding agents

## Synthesis
Cloudflare's security team provides one of the most detailed public evaluations of Anthropic's Mythos Preview, a security-focused model made available through Project Glasswing. The post is candid about both the model's capabilities and limitations, making it valuable for understanding what "cyber frontier models" actually look like in practice.

The step-change is real: Mythos Preview's ability to chain multiple low-severity bugs into a working exploit — writing code, compiling it, running it, and iterating on failures — moves AI vulnerability research from "finding interesting bugs" to "proving exploitability." Previous frontier models could identify bugs and write thoughtful descriptions but consistently failed at stitching primitives together. Mythos Preview closes the gap between identification and proof.

However, the operational challenges remain significant. The model exhibits emergent guardrails that sometimes cause it to refuse legitimate security research, and these refusals are inconsistent — the same task framed differently produces different outcomes. This makes organic refusals unreliable as a safety layer, reinforcing the need for additional safeguards in generally available models.

The most practically valuable section covers harness architecture. Cloudflare learned that naive approaches — pointing a coding agent at a repository — fail for vulnerability research because of fundamentally incompatible interaction shapes. Coding agents are tuned for focused single-stream work; vulnerability research requires narrow, parallel hypotheses across thousands of surface points.

Cloudflare's solution: a harness that scopes agents narrowly (specific vulnerability class, specific function, specific trust boundary), adds adversarial review (a second agent with different prompt/model that only critiques, never proposes), splits reasoning chains across agents (separating "is this buggy?" from "is this reachable?"), and runs tightly scoped parallel tasks with deduplication. This architecture is described as something "that isn't a chat interface anymore" — a recognition that scaling AI vulnerability research requires fundamentally different interaction models than consumer AI products provide.

The post is also notable for what it doesn't say: no specifics about vulnerabilities found, which is appropriate for ongoing security work. But the methodological insights make it a must-read for any organization considering AI-assisted security testing.
