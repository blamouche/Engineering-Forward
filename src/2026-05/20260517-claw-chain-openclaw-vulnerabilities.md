# Claw Chain: Critical OpenClaw Vulnerabilities Enable Data Theft, Privilege Escalation, and Persistent Access
**Source**: https://www.rescana.com/post/claw-chain-critical-openclaw-vulnerabilities-cve-2026-44112-44113-44115-44118-enable-data-theft-privilege-escalation-and
**Date**: 2026-05-17
**Author**: Rescana
**Keywords**: openclaw, vulnerability, CVE, CVE-2026-44112, CVE-2026-44113, CVE-2026-44115, CVE-2026-44118, sandbox-escape, privilege-escalation, TOCTOU, security

## Elevator pitch
A coordinated set of four critical vulnerabilities in the OpenClaw agent platform, collectively named "Claw Chain," can be chained to achieve full system compromise through sandbox escape, data exfiltration, command injection, and privilege escalation, with active exploitation confirmed in the wild.

## Takeaways
- The four CVEs exploit distinct trust boundaries: TOCTOU sandbox write escape (CVE-2026-44112), TOCTOU sandbox read escape (CVE-2026-44113), shell allowlist bypass via heredoc token injection (CVE-2026-44115), and owner impersonation through a client-controlled flag (CVE-2026-44118)
- Exploitation begins with initial access via malicious plugin, prompt injection, or compromised external input, then chains the four vulnerabilities for full compromise: read → escalate → persist
- Active in-the-wild exploitation confirmed by multiple sources (The Hacker News, Reddit, LinkedIn) with attackers blending TTPs into normal agent behavior to evade detection
- All versions of OpenClaw prior to 2026.4.22 are affected; the vulnerabilities are fully patched in version 2026.4.22 and later, which implements robust sandboxing, corrected input validation, and distinct owner/non-owner bearer tokens
- No specific APT group has been formally attributed, but the sophistication of the attack chain aligns with nation-state or highly skilled criminal group capabilities

## Synthesis
Rescana's advisory details a coordinated vulnerability chain in the OpenClaw agent platform that represents a textbook example of how layered security flaws compound into catastrophic compromise. Each CVE targets a different security boundary, and none alone would be sufficient — but together they dismantle the platform's entire trust model.

CVE-2026-44112 and CVE-2026-44113 are both time-of-check/time-of-use (TOCTOU) race conditions in the OpenShell managed sandbox. The first allows writing files outside the intended mount root (establishing persistence), while the second allows reading files outside sandbox boundaries (enabling credential theft). CVE-2026-44115 exploits an incomplete shell allowlist by embedding shell expansion tokens inside heredoc bodies, bypassing command restrictions to execute arbitrary code. CVE-2026-44118 is perhaps the most concerning: a non-owner loopback client can impersonate an owner by manipulating a `senderIsOwner` flag that was never validated against the authenticated session — granting control over gateway configuration, cron scheduling, and execution environment management.

The attack chain proceeds in a logical progression: initial access through a malicious plugin or prompt injection → use CVE-2026-44113 and CVE-2026-44115 to read credentials and sensitive files → leverage CVE-2026-44118 for privilege escalation to owner-level control → deploy CVE-2026-44112 for persistence through configuration modification or backdoor planting. Each step mimics legitimate agent behavior, making detection by traditional security tools extremely difficult.

The fix in version 2026.4.22 is comprehensive: proper sandbox enforcement, corrected input validation, and a redesigned authentication mechanism. The MCP loopback runtime now issues distinct owner and non-owner bearer tokens, and the spoofable sender-owner header is no longer accepted. Organizations running any earlier version are urged to upgrade immediately and audit logs for signs of prior exploitation. The advisory also recommends treating agent platforms as attack vectors requiring layered defenses including runtime behavioral analytics and strict privilege separation.
