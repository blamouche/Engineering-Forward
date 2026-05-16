# Our response to the TanStack npm supply chain attack
**Source**: https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/
**Date**: May 13, 2026
**Author**: OpenAI
**Keywords**: supply chain attack, TanStack, npm, Mini Shai-Hulud, macOS, certificate rotation, cybersecurity

## Elevator pitch
OpenAI discloses a supply chain attack via the compromised TanStack npm library that affected two employee devices and led to a precautionary code-signing certificate rotation requiring all macOS users to update their OpenAI apps by June 12, 2026.

## Takeaways
- The attack was part of the broader "Mini Shai-Hulud" software supply chain campaign that compromised the widely-used TanStack open-source library on May 11, 2026
- Two employee corporate devices were impacted, with limited credential exfiltration from internal source code repositories — but no user data, production systems, or intellectual property were compromised
- OpenAI is rotating macOS, iOS, Windows, and Android code-signing certificates as a precaution; macOS users must update all OpenAI apps by June 12, 2026 or they will stop functioning
- The incident occurred during a phased deployment of enhanced security controls (CI/CD hardening, package provenance validation) that hadn't yet reached the two affected devices
- This attack reflects a broader shift where attackers increasingly target shared software dependencies and developer tooling across the ecosystem

## Synthesis
On May 13, 2026, OpenAI published a detailed incident report on a supply chain attack originating from the compromise of TanStack, a popular open-source npm library. The attack was part of a wider campaign dubbed "Mini Shai-Hulud" by security researchers. The breach reached two corporate employee devices at OpenAI, leading to unauthorized access and credential-focused exfiltration from a limited subset of internal source code repositories accessible to those employees.

OpenAI moved quickly to contain the incident: isolating impacted systems, revoking user sessions, rotating credentials across all affected repositories, and temporarily restricting code-deployment workflows. A third-party digital forensics firm was engaged to support the investigation. Critically, the company found no evidence that user data, production systems, or OpenAI's intellectual property were compromised, and no signs of follow-on access or credential misuse by the threat actor.

Because the impacted repositories included code-signing certificates for OpenAI's desktop and mobile applications, the company is rotating all signing certificates. For macOS users, this carries a hard deadline: by June 12, 2026, the old certificate will be fully revoked, and apps signed with it will be blocked by macOS security protections. Users must update to the latest versions of ChatGPT Desktop, Codex App, Codex CLI, and Atlas through official channels. Windows and iOS users do not need to take manual action.

The incident reveals both progress and gaps in OpenAI's security posture. Following a prior supply chain incident involving Axios, the company had accelerated deployment of enhanced controls — including minimumReleaseAge package manager configurations and software to validate package provenance. However, the phased nature of this rollout meant the two affected devices hadn't yet received the updated configurations that would have blocked the malicious package.

This event underscores a fundamental shift in the threat landscape. Modern software development depends on an interconnected ecosystem of open-source libraries, package managers, and CI/CD infrastructure. Attackers have recognized that compromising a single upstream dependency can propagate widely and quickly across organizations. OpenAI's transparent disclosure — including detailed technical findings, remediation steps, and a commitment to further investment in supply chain integrity controls — represents the kind of industry response needed as these attacks become more sophisticated and frequent.
