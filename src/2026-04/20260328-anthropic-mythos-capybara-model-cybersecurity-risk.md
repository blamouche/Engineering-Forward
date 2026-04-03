# Anthropic Readies Mythos Model with High Cybersecurity Risk
**Source**: https://www.testingcatalog.com/anthropic-redies-powerfull-mythos-model-with-high-cybersecurity-risk/
**Date**: March 28, 2026
**Author**: M1Astra and Alexey Shabanov
**Keywords**: Anthropic, Mythos, Capybara, Claude, cybersecurity, AI safety, leak, frontier model

## Elevator pitch
A CMS misconfiguration exposed Anthropic's draft materials for Claude Mythos (Capybara) — a model above Opus that demonstrates "unprecedented cybersecurity risks" and will initially be restricted to defense-focused organizations.

## Takeaways
- Mythos (also referenced as Capybara) described as "larger and more intelligent than Opus models" with dramatically higher scores in coding, reasoning, and cybersecurity
- Draft materials explicitly warn the model poses "unprecedented cybersecurity risks" enabling attacks that could surpass defender capabilities
- Initial access restricted to cybersecurity defense-focused organizations; extremely compute-intensive
- Previous incident: Chinese state-sponsored actors exploited Claude Code to infiltrate approximately 30 organizations
- No public timeline announced; documents characterized as early drafts

## Synthesis
The accidental exposure of Anthropic's draft materials for Mythos provides an unusual window into how frontier AI labs communicate internally about the safety tradeoffs of their most capable models. The draft language — "unprecedented cybersecurity risks," "enables attacks surpassing defender capabilities" — is notable for its directness. Most public communications about frontier models hedge capability claims; internal draft materials written for the purpose of justifying restricted deployment apparently do not.

The precedent of Chinese state-sponsored actors exploiting Claude Code to infiltrate approximately 30 organizations gives context to why cybersecurity is the specific risk category Anthropic is treating with heightened caution for Mythos. Code generation capabilities at frontier quality have already demonstrated adversarial utility at scale. A model that exceeds current Opus performance on cybersecurity benchmarks would extend this capability further.

The initial access restriction to cybersecurity defense-focused organizations reflects a deployment strategy that attempts to concentrate offensive capability improvements in defensive hands first. This mirrors historical patterns in cryptography and vulnerability research, where capabilities developed for offensive purposes are first deployed to defenders who can use them to improve resilience before broader access. The practical effectiveness of this strategy depends on whether offensive actors can obtain equivalent capabilities through other means, or whether Anthropic's model remains sufficiently ahead to provide meaningful defense-first advantage.

The compute intensity limitation — mirroring GPT-4.5's rollout — provides an involuntary access control: models that are too expensive to serve at scale are automatically restricted to well-funded organizations with sufficient financial and infrastructure resources. This may be a more effective access control for the near term than policy-based restrictions.

The leak via CMS misconfiguration adds to a pattern of AI companies inadvertently exposing materials through infrastructure oversights — consistent with the Claude Code source map leak reported in the same news cycle.
