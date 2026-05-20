# Claw Chain: Critical OpenClaw Vulnerabilities (CVE-2026-44112, 44113, 44115, 44118) Enable Data Theft, Privilege Escalation, and Persistent Access
**Source**: https://www.rescana.com/post/claw-chain-critical-openclaw-vulnerabilities-cve-2026-44112-44113-44115-44118-enable-data-theft-privilege-escalation-and
**Date**: May 17, 2026
**Author**: Rescana
**Keywords**: OpenClaw, CVE, vulnerability, sandbox bypass, privilege escalation, TOCTOU, Claw Chain, cybersecurity, agent platform

## Elevator pitch
A coordinated set of four critical vulnerabilities in the OpenClaw agent platform—dubbed "Claw Chain"—can be chained by adversaries to achieve data theft, privilege escalation, and persistent unauthorized access, with confirmed exploitation in the wild.

## Takeaways
- Four CVEs (CVE-2026-44112, 44113, 44115, 44118) form an attack chain targeting OpenClaw's sandboxing, authentication, and command validation mechanisms
- Exploitation confirmed in the wild by multiple independent sources including The Hacker News and SentinelOne
- All OpenClaw versions prior to 2026.4.22 (released April 23, 2026) are affected — immediate upgrade is the primary remediation
- Attack chain mimics legitimate agent behavior, making detection by traditional security controls challenging
- No specific APT group has been formally attributed, but the sophistication suggests nation-state or highly skilled criminal actors

## Synthesis
The Rescana advisory details a coordinated set of four critical vulnerabilities in the OpenClaw agent platform, collectively referred to as the "Claw Chain." These flaws — CVE-2026-44112, CVE-2026-44113, CVE-2026-44115, and CVE-2026-44118 — target fundamental trust boundaries within OpenClaw's security architecture and can be chained to achieve full compromise of confidentiality, integrity, and availability.

CVE-2026-44112 is a time-of-check/time-of-use (TOCTOU) race condition in the OpenShell managed sandbox backend, enabling attackers to bypass sandbox restrictions and redirect file writes outside the intended mount root. This allows tampering with agent configuration files, planting persistent backdoors, and modifying system settings. CVE-2026-44113 is a similar TOCTOU race condition that enables reading files outside sandbox boundaries, facilitating credential exfiltration and lateral movement. CVE-2026-44115 exploits an incomplete allowlist of shell inputs, where embedding shell expansion tokens within heredoc bodies bypasses command filtering, enabling execution of unapproved commands. CVE-2026-44118 is an improper access control flaw in loopback client authentication — non-owner clients can impersonate owners by manipulating a client-controlled `senderIsOwner` flag, gaining control over gateway configuration, cron scheduling, and execution environments.

The exploitation chain typically begins with initial access via a malicious plugin, prompt injection, or compromised external input, granting code execution within the OpenShell sandbox. Attackers then leverage CVE-2026-44113 and CVE-2026-44115 to access credentials and sensitive files, followed by CVE-2026-44118 for privilege escalation to owner-level control, and finally CVE-2026-44112 to establish persistence. Each step mimics legitimate agent behavior, making detection by conventional security tools particularly difficult.

The advisory notes that multiple independent sources — including The Hacker News, Cyera, SentinelOne, Reddit, and LinkedIn — have confirmed active exploitation in the wild. Attackers have been observed chaining these flaws to move laterally within networks, escalate privileges, and maintain persistent access. While no public proof-of-concept exploit code has been released, detailed technical descriptions have been published by Cyera and SentinelOne, and sophisticated threat actors have already demonstrated weaponization capability. No specific APT group has been formally attributed, but the attack's complexity aligns with tactics typically observed in nation-state or highly skilled criminal operations.

All versions of OpenClaw released prior to April 23, 2026 (version 2026.4.22) are affected. The patched release addresses all four vulnerabilities through robust sandbox enforcement, corrected input validation logic, and an overhauled authentication mechanism — the MCP loopback runtime now issues distinct owner and non-owner bearer tokens, and the spoofable sender-owner header is no longer accepted. Beyond patching, the advisory recommends auditing agent logs for suspicious activity, enhancing runtime monitoring for anomalous behaviors, and implementing layered defenses with behavioral analytics, strict privilege separation, and continuous validation of agent actions.
