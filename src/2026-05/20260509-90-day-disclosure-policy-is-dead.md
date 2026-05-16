# The 90 Day Disclosure Policy Is Dead
**Source**: https://blog.himanshuanand.com/2026/05/the-90-day-disclosure-policy-is-dead/
**Date**: May 9, 2026 (Updated May 9, 2026)
**Author**: Himanshu Anand
**Keywords**: vulnerability disclosure, LLM, security, zero-day, exploit development, Copy Fail, Dirty Frag, Linux kernel

## Elevator pitch
LLMs have compressed vulnerability discovery and exploit development timelines to near-zero, rendering the traditional 90-day responsible disclosure window obsolete and demanding immediate patching of all critical security issues.

## Takeaways
- LLM-assisted vulnerability hunters are converging on the same bugs simultaneously — Himanshu Anand was the 11th reporter of a critical bug in just six weeks, and triage teams report waves of duplicate reports within days of an LLM-assisted discovery.
- AI can turn a security patch diff into a working exploit in as little as 30 minutes, eliminating the "grace period" between patch publication and exploitation that defenders historically relied on.
- The Copy Fail (CVE-2026-31431) and Dirty Frag (CVE-2026-43284, CVE-2026-43500) Linux kernel vulnerabilities demonstrated the collapse: AI-assisted discovery, public PoCs within hours, nation-state weaponization within days, and in-the-wild exploitation confirmed within 24 hours.
- Embargo-based coordination is broken — Dirty Frag's embargo was broken within hours by an independent third party who found the same bug class, proving that sensitive vulnerability information can no longer be contained.
- The author's single ask: treat every critical security issue as P0 and fix it immediately — not in the next sprint, not after impact assessment, but now.

## Synthesis
Himanshu Anand, a security researcher, delivers a forceful post-mortem on the 90-day responsible disclosure model that has governed vulnerability reporting for over a decade. His thesis is unambiguous: LLMs have killed the foundational assumptions underlying coordinated disclosure, and the industry must adapt or continue bleeding.

Anand structures his argument around three real-world stories. The first is personal: in late April 2026, he reported a critical e-commerce vulnerability (no signature verification on server responses, enabling zero-cost purchases) only to learn he was the eleventh reporter. Triage teams confirmed this pattern — LLM-assisted hunters using different workflows independently converge on the same bugs within days. The uncomfortable math: if 11 people reported it, how many found it and didn't report? How many sold it? The 90-day window isn't protecting users; it's giving everyone who already has the bug a 90-day head start.

The second story is a hands-on experiment. After React published a security advisory with patch details, Anand turned the diff into a working denial-of-service exploit in 30 minutes using AI assistance. In the old world, this n-day exploitation took skilled reverse engineers days to weeks. That safety net — the gap between patch publication and widespread exploitation — no longer exists.

The third story is the most devastating. In late April and early May 2026, two back-to-back critical Linux kernel vulnerabilities demonstrated the complete collapse of the disclosure model. Copy Fail (CVE-2026-31431), discovered by Xint Code using AI-assisted workflow, was a 732-byte Python script granting root on every Linux distribution since 2017. Discovered in approximately one hour of AI-amplified research, it spawned public PoCs and Iranian nation-state weaponization within days.

Barely a week later, Dirty Frag (CVE-2026-43284, CVE-2026-43500) hit — same bug class, different attack path, and crucially effective even with Copy Fail mitigations applied. The researcher coordinated with linux-distros under a 5-day embargo, but an unrelated third party independently found and published exploit details within hours, breaking the embargo. At the moment of full public disclosure, zero distributions had a patch. Microsoft's Defender team confirmed in-the-wild exploitation within 24 hours: attackers gaining SSH access, deploying ELF binaries, escalating to root, modifying auth configs, and moving laterally.

Anand's conclusion is stark: not just the 90-day window, but monthly patch cycles and "wait for the advisory" postures are all dead. His prescription is equally uncompromising: P0 critical issues must be fixed immediately upon report receipt. For blue teams, he advocates integrating LLMs at four points: at code push (AI security review in CI), for automatic patch diff analysis, for continuous dependency scanning, and for pre-shipment patch testing with AI-generated regression tests and exploit attempts.

The piece is a compelling synthesis of recent events into a coherent call to action. It's also a document of a security industry at an inflection point, where the tools that empower defenders equally empower attackers, and the only viable response is speed.
