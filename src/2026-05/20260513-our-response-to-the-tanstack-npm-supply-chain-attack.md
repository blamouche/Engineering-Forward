# Our response to the TanStack npm supply chain attack
**Source**: https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/
**Date**: May 13, 2026
**Author**: OpenAI
**Keywords**: supply chain attack, TanStack, npm, Mini Shai-Hulud, code signing, macOS, certificate rotation, open source security, CI/CD, software supply chain

## Elevator pitch
OpenAI discloses that two employee devices were compromised in the TanStack npm supply chain attack (Mini Shai-Hulud), resulting in limited credential exfiltration from internal source repositories that included code-signing certificates, prompting a macOS certificate rotation requiring all users to update their OpenAI apps by June 12, 2026.

## Takeaways
- The TanStack npm compromise was part of a broader "Mini Shai-Hulud" supply chain attack; two OpenAI employee devices were impacted, leading to unauthorized access and credential exfiltration from a limited subset of internal repositories.
- OpenAI confirmed no user data, production systems, or intellectual property were compromised, and no malicious software was signed with OpenAI's certificates.
- macOS users must update ChatGPT Desktop, Codex App, Codex CLI, and Atlas by June 12, 2026, when the old certificate is fully revoked; iOS and Windows users need not take action.
- This incident occurred during a phased security rollout—the two affected devices lacked updated configurations that would have blocked the malicious package.
- The broader lesson: attackers increasingly target shared software dependencies and CI/CD infrastructure rather than individual companies, requiring ecosystem-level defenses.

## Synthesis
OpenAI's disclosure of its involvement in the TanStack npm supply chain attack provides a rare window into how a leading AI company handles—and learns from—a significant security incident. The attack, identified as part of the broader "Mini Shai-Hulud" campaign, compromised a widely-used open-source JavaScript library, and two OpenAI employee devices in the corporate environment were caught in the blast radius.

The timeline and response are instructive. Upon detecting malicious activity on May 11, 2026, OpenAI isolated affected systems and identities, revoked user sessions, rotated all credentials across impacted repositories, temporarily restricted code-deployment workflows, and engaged a third-party digital forensics firm. The investigation confirmed that credential material was successfully exfiltrated from a limited subset of internal source code repositories, but that no customer data, production systems, or intellectual property were compromised. Critically, no follow-on access or credential misuse by the threat actor was detected.

The most significant operational consequence for users concerns code-signing certificates. The impacted repositories contained signing certificates for OpenAI's macOS, iOS, and Windows applications. As a precaution, OpenAI is rotating all code-signing certificates, which creates a hard deadline for macOS users: by June 12, 2026, all OpenAI desktop applications must be updated to versions signed with the new certificate. After revocation, macOS security protections will block new downloads and first-time launches of apps signed with the old certificate. The grace period (roughly one month from announcement) balances user risk against disruption, and OpenAI notes it will accelerate the timeline if malicious activity is detected during the window.

Perhaps the most candid part of the disclosure is the admission that this incident occurred during a phased security rollout. After a previous Axios developer tool compromise, OpenAI had accelerated deployment of specific controls—CI/CD credential hardening, package manager configurations with minimumReleaseAge, and provenance validation for new packages. The two affected devices had not yet received these updated configurations, highlighting the operational challenge of securing every endpoint in a large organization against rapidly evolving supply-chain threats.

The strategic takeaway extends beyond OpenAI. The company frames the incident as symptomatic of a broader shift where attackers target shared software dependencies and development tooling rather than individual organizations. In this ecosystem, a vulnerability introduced upstream—in a package manager, an open-source library, or CI/CD infrastructure—can propagate widely and quickly. OpenAI's response includes continued investment in controls that validate the integrity and provenance of third-party components, a posture that other organizations building on the same open-source foundations would do well to emulate.
