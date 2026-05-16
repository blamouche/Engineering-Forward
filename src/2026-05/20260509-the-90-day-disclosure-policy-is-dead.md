# The 90 Day Disclosure Policy Is Dead
**Source**: https://blog.himanshuanand.com/2026/05/the-90-day-disclosure-policy-is-dead/
**Date**: May 9, 2026
**Author**: Himanshu Anand
**Keywords**: vulnerability disclosure, LLM, security, exploit development, Linux kernel, Copy Fail, Dirty Frag

## Elevator pitch
The traditional 90-day vulnerability disclosure window is obsolete: LLMs have compressed both bug discovery and exploit development to near-zero timelines, making the old model a liability rather than a protection.

## Takeaways
- LLM-assisted bug hunting has led to 10+ independent researchers finding the same critical vulnerability within 6 weeks — the "lone finder" assumption is dead.
- AI can now turn a public patch diff into a working exploit in 30 minutes, eliminating the traditional days-to-weeks safety gap for patching.
- The Linux kernel suffered two back-to-back critical vulnerabilities (Copy Fail and Dirty Frag) in April-May 2026, both with AI-accelerated discovery and public exploits within hours.
- Dirty Frag's embargo was broken within hours by an independent third party — coordinated disclosure is failing when multiple actors discover the same bug class simultaneously.
- The author's recommendation: treat every critical security issue as P0 and patch immediately, not on a scheduled maintenance window.

## Synthesis
Himanshu Anand delivers a stark post-mortem on the 90-day responsible disclosure model through three concrete stories that collectively prove the old framework is unsustainable. His central thesis: LLMs have democratized both vulnerability discovery and exploit development simultaneously, creating a situation where the traditional grace period between discovery, patch, and deployment no longer exists.

The first story is almost comical in its implications. Anand reported a critical e-commerce bug (no signature verification on payment responses) only to be told he was the 11th reporter in six weeks. The same LLM tools that helped honest researchers find the bug are available to anyone — including those who won't report it. The 90-day window, rather than protecting users, gives silent exploit holders a 90-day head start.

The second story is equally damning: after reading React's public security patch blog post, Anand used AI to turn the patch diff into a working DoS exploit in 30 minutes. The skill of reverse-engineering patches used to be a niche expertise requiring days or weeks. Now the LLM does the heavy lifting while the human merely steers. The moment a patch ships, the exploit effectively exists.

The third story is the centerpiece: the Linux kernel's catastrophic April-May 2026. Copy Fail (CVE-2026-31431) — found via AI-assisted workflow in about an hour — gave unprivileged users root on every Linux distribution since 2017 with a 732-byte Python script. Iranian threat actors weaponized it within days. Then Dirty Frag (CVE-2026-43284) hit a week later, bypassing Copy Fail mitigations entirely. The embargo was broken within hours by an unrelated third party. Zero distributions had patches available when the full PoC dropped.

Anand's conclusion is unambiguous: the industry must shift to immediate P0 response for all critical vulnerabilities. The coordination mechanisms, the disclosure timelines, the patching cadences — all were designed for a pre-LLM world that no longer exists. The security community's social contract with vendors has expired, and nobody seems to have noticed.
