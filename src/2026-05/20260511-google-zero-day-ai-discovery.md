# Google Announces Its First-Ever Discovery of a Zero-Day Exploit Made With AI
**Source**: https://www.engadget.com/2170002/google-announces-its-first-ever-discovery-of-a-zero-day-exploit-made-with-ai/
**Date**: May 11, 2026
**Author**: Jackson Chen
**Keywords**: Google, zero-day, AI exploit, GTIG, cybersecurity, China, North Korea, Anthropic Project Glasswing, AI defense

## Elevator pitch
Google's Threat Intelligence Group publicly confirmed the first-ever detection of a zero-day exploit developed with AI, calling it "the tip of the iceberg" for AI-augmented cyberattacks.

## Takeaways
- The AI-developed zero-day was planned for a "mass exploitation event" but GTIG's proactive discovery prevented its use; the unnamed target company was notified and patched the vulnerability.
- GTIG Chief Analyst John Hultquist characterized the discovery as "a taste of what's to come" — the first tangible evidence that AI is being used to build weaponized exploits in the wild.
- Google has high confidence an AI model was involved despite believing its own Gemini wasn't used, based on structural characteristics of the exploit code.
- China and North Korea-nexus actors showed "significant interest" in AI-augmented vulnerability exploitation, alongside documented use in other attack phases.
- The discovery coincides with Anthropic's Project Glasswing initiative, which uses Claude Mythos Preview to find and defend against high-severity vulnerabilities — highlighting the AI-for-defense counter-narrative.

## Synthesis
Engadget's coverage of Google's GTIG report frames the discovery as a watershed moment: the first concrete evidence that AI-generated zero-day exploits have moved from theoretical risk to operational reality. The exploit was discovered before deployment — Google proactively identified the threat, notified the vendor, and the patch was applied — but the significance lies in what it portends.

The exploit itself targeted a two-factor authentication bypass in a popular open-source web administration tool. It was implemented as a Python script containing telltale signs of AI generation: educational docstrings, a hallucinated CVSS score, and textbook Pythonic formatting consistent with LLM training data. The vulnerability class — a high-level semantic logic flaw where a developer hardcoded a trust assumption — is precisely where frontier LLMs outperform traditional vulnerability scanners, which are optimized for memory corruption and input sanitization bugs rather than reading developer intent.

GTIG Chief Analyst John Hultquist's framing as "the tip of the iceberg" is deliberate. The report documents multiple threat actor clusters experimenting with AI across the attack lifecycle: persona-driven jailbreaking by Chinese actors, large-scale recursive CVE analysis by North Korean APT45, and the emergence of autonomous malware like PROMPTSPY that offloads operational decisions to AI models. Engadget connects this to a broader pattern of AI dual-use concerns, referencing studies on AI's negative cognitive effects and a lawsuit against OpenAI by the spouse of an FSU shooting victim.

Notably, the article positions Anthropic's Project Glasswing as the defensive counterpart — using Claude Mythos Preview to find and defend against the same class of vulnerabilities that attackers are now using AI to exploit. The implication is clear: AI cybersecurity is becoming a symmetric arms race, with both attackers and defenders wielding the same underlying technology.
