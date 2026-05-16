# Our Response to the TanStack npm Supply Chain Attack
**Source**: https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/
**Date**: May 13, 2026
**Author**: OpenAI
**Keywords**: supply chain attack, npm, TanStack, Mini Shai-Hulud, code signing, macOS security, OpenSSL, incident response

## Elevator pitch
OpenAI discloses that two employee devices were compromised in the TanStack npm supply chain attack (Mini Shai-Hulud), prompting certificate rotation for all platforms and requiring macOS users to update apps by June 12, 2026.

## Takeaways
- The TanStack npm library was compromised as part of the Mini Shai-Hulud supply chain attack; two OpenAI employee devices were impacted before updated security controls were fully deployed.
- Only limited credential material was exfiltrated from internal source code repositories; no customer data, production systems, or intellectual property were compromised.
- Code-signing certificates for iOS, macOS, Windows, and Android were in the impacted repositories — all applications are being re-signed with new certificates.
- macOS users must update ChatGPT Desktop, Codex App, Codex CLI, and Atlas by June 12, 2026; after that date, older versions will be blocked by macOS security protections.
- The incident highlights the growing threat of ecosystem-level supply chain attacks targeting shared software dependencies rather than individual companies.

## Synthesis
OpenAI's disclosure about the TanStack npm supply chain compromise provides a detailed window into how modern software supply chain attacks unfold — and how even the most sophisticated organizations remain vulnerable to ecosystem-level threats.

The attack, part of a broader campaign dubbed "Mini Shai-Hulud," compromised the widely-used TanStack open-source library. Two OpenAI employee devices downloaded the malicious package before the company's phased rollout of updated security controls reached those machines. The malware's behavior — unauthorized access and credential-focused exfiltration — was consistent with publicly documented patterns. OpenAI moved quickly: isolated impacted systems and identities, revoked user sessions, rotated all impacted credentials, temporarily restricted code-deployment workflows, and engaged a third-party forensics firm.

The most consequential finding was that code-signing certificates for all major platforms — iOS, macOS, Windows, and Android — were stored in repositories accessible to the impacted employees. While only "limited credential material" was exfiltrated, the presence of signing certificates in those repos triggered a precautionary full certificate rotation.

For macOS users, this has tangible implications. By June 12, 2026, any app signed with the old certificate will be blocked by macOS security protections. Users must update ChatGPT Desktop, Codex App, Codex CLI, and Atlas through official channels. OpenAI has already blocked new notarizations with the impacted certificate, meaning any fraudulent app would lack notarization and be blocked by default — but the certificate revocation on June 12 adds a hard stop.

The incident reveals an uncomfortable truth about enterprise security postures: OpenAI had already accelerated security controls after the Axios developer tool compromise, including hardened CI/CD credentials, package manager configurations with minimumReleaseAge, and provenance validation for new packages. Yet the two impacted devices fell through the cracks of a phased rollout. This is not unique to OpenAI — it reflects the fundamental challenge of securing developer workstations in an ecosystem where every `npm install` carries risk.

The broader shift OpenAI describes is real and accelerating: attackers increasingly target shared software dependencies and development tooling rather than individual companies, exploiting the deeply interconnected nature of modern software supply chains. A vulnerability introduced upstream in a popular open-source library can propagate across thousands of organizations before anyone notices.

OpenAI's response — transparent disclosure, certificate rotation, platform coordination, and a measured revocation timeline to minimize user disruption — sets a reasonable standard for incident response. But the incident also serves as a warning that supply chain security controls need to be default-on, not opt-in, and that phased rollouts create dangerous windows of differential vulnerability.
