# The 90 Day Disclosure Policy Is Dead
**Source**: https://blog.himanshuanand.com/2026/05/the-90-day-disclosure-policy-is-dead/
**Date**: May 9, 2026
**Author**: Himanshu Anand
**Keywords**: security, disclosure, LLM, vulnerability management, Linux, exploit

## Elevator pitch
LLMs have compressed both vulnerability discovery and exploit development timelines to near-zero, rendering the traditional 90-day responsible disclosure window obsolete and dangerous.

## Takeaways
- 11 independent researchers found the same critical bug in 6 weeks using LLM-assisted workflows — the old assumption of "you're the only finder" is dead
- Copy Fail (CVE-2026-31431) went from AI-assisted discovery to nation-state weaponization within days, affecting every Linux distro since 2017
- Dirty Frag (CVE-2026-43284) saw its embargo broken within hours by a third party who independently found the same bug class; in-the-wild exploitation confirmed within 24 hours
- AI can turn a patch diff into a working exploit in 30 minutes — the safety net between patch release and exploitation has vanished
- Monthly patch cycles and "wait for the advisory" postures are attack windows, not safety margins
- Every critical vulnerability must be treated as P0 and fixed immediately; defensive LLM integration at CI, patch analysis, and dependency scanning is no longer optional

## Synthesis
Himanshu Anand, a security researcher, argues that the 90-day responsible disclosure policy is fundamentally broken in the age of large language models. Through three vivid case studies, he demonstrates how AI has obliterated the temporal assumptions that underpinned vulnerability disclosure for over a decade.

The first story involves a critical e-commerce payment verification bug. Anand reported it to the vendor and was told he was the eleventh reporter in six weeks. Ten other researchers, using unrelated LLM-assisted workflows, had independently converged on the same vulnerability. This pattern has been observed across the industry — triage teams are seeing waves of duplicate reports within days of a new vulnerability class being discovered. The uncomfortable math: if ten people reported it, how many found it and chose not to report, or to sell it instead? The 90-day window, far from protecting users, gives bad actors a 90-day head start.

The second case study demonstrates the collapse of the post-patch safety window. After React published security fixes and a blog post explaining the changes, Anand experimented: feeding the patch diff into an LLM, he produced a working denial-of-service exploit in 30 minutes. In the old world, n-day exploitation took skilled reverse engineers days to weeks. That gap — the traditional grace period for administrators to update — has vanished. The moment a patch ships, the exploit exists.

The third and most devastating story covers the two weeks in late April to early May 2026 when the Linux kernel caught fire. Copy Fail (CVE-2026-31431), discovered by Theori's team using the Xint Code AI-assisted platform, was a deterministic privilege escalation affecting every Linux distribution since 2017 — exploitable with a 732-byte Python script. Within days, Iranian adversaries were weaponizing it against Ubuntu servers for DDoS infrastructure. Barely a week later, Dirty Frag (CVE-2026-43284) was published: same bug class, different attack path, working even with the Copy Fail mitigation applied. Its agreed-upon five-day embargo was broken within hours by an unrelated third party. Microsoft's Defender team confirmed in-the-wild exploitation within 24 hours. As of Anand's writing, one component still had no upstream patch.

Anand's prescription is uncompromising: every critical vulnerability must be treated as P0 and fixed immediately, not within 24 hours or the next sprint. For vendors, the clock starts when the report lands; for researchers, sitting on critical bugs is irresponsible when you're no longer the only finder; for vulnerability management teams, the maximum response time is hours. On the defensive side, he calls for LLM integration at every stage of the security pipeline: AI-assisted review at code push time, automated patch diff analysis for upstream dependencies, continuous AI-powered dependency scanning, and adversarial testing of patches before publication. The window between vulnerability existence and exploitation is shrinking to zero — defense must automate at the same speed as offense.
