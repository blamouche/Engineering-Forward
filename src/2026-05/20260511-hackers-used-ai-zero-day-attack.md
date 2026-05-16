# Google: Hackers Used AI to Build Zero-Day Attack, Researchers Say
**Source**: https://www.bloomberg.com/news/articles/2026-05-11/hackers-used-ai-to-build-zero-day-attack-google-researchers-say
**Date**: May 11, 2026
**Author**: Bloomberg News
**Keywords**: AI, zero-day, cybersecurity, Google GTIG, threat actors, vulnerability exploitation, China, North Korea, APT, malware

## Elevator pitch
Google's Threat Intelligence Group (GTIG) confirmed the first-ever discovery of a zero-day exploit developed with AI assistance, planned for mass exploitation before Google's proactive counter-discovery prevented its use.

## Takeaways
- GTIG identified a criminal threat actor using an AI-generated zero-day that bypassed 2FA on a popular open-source web administration tool; the exploit script contained LLM-typical hallmarks like hallucinated CVSS scores and textbook Python formatting.
- China (PRC) and North Korea (DPRK) threat actors showed significant interest in AI-augmented vulnerability discovery, using persona-driven jailbreaking and specialized vulnerability repositories with 85,000+ real-world cases to prime models.
- AI-enabled malware families like PROMPTFLUX, HONESTCUE, and CANFAIL demonstrate a shift toward polymorphic, self-modifying malware that evades signature-based detection.
- Autonomous malware PROMPTSPY signals a move toward AI orchestrating attack operations dynamically, with models interpreting system states to generate commands in real-time.
- Google stresses AI is also a powerful defensive tool, citing projects like Big Sleep and CodeMender that use AI agents to find and automatically fix vulnerabilities.

## Synthesis
Google's Threat Intelligence Group (GTIG) released its May 2026 AI Threat Tracker report detailing a significant milestone in offensive cybersecurity: the first confirmed case of a threat actor using AI to discover and weaponize a zero-day vulnerability. The exploit targeted a 2FA bypass in a popular open-source web-based system administration tool and was discovered before deployment thanks to GTIG's proactive research. The vulnerability itself was notable — not a memory corruption or input sanitization flaw, but a high-level semantic logic error where a developer hardcoded a trust assumption. Frontier LLMs excel at identifying precisely this class of flaw, reading developer intent and surfacing dormant logic errors invisible to traditional fuzzers and static analysis tools.

The report paints a broader picture of AI's dual-use nature in cybersecurity. State-sponsored actors from China and North Korea are experimenting with sophisticated approaches: persona-driven jailbreaking (posing as senior security auditors), leveraging curated vulnerability databases like the "wooyun-legacy" GitHub project containing 85,000+ real-world cases, and using agentic tools like OpenClaw to refine AI-generated payloads in controlled environments. APT45 alone sent thousands of repetitive prompts recursively analyzing CVEs and validating PoC exploits.

On the malware front, GTIG documented a shift toward AI-enabled obfuscation and autonomy. Malware families PROMPTFLUX, HONESTCUE, CANFAIL, and LONGSTREAM incorporate dynamic code modification, just-in-time payload generation, and AI-generated decoy logic to evade detection. PROMPTSPY represents an emerging class of autonomous malware where AI models interpret system states and dynamically generate commands — essentially offloading operational decision-making to the model itself. Supply chain attacks targeting AI environments and dependencies have also emerged as an initial access vector, with actors like "TeamPCP" pivoting from compromised AI software to broader network environments for ransomware deployment.

Google's counter-narrative is clear: AI is equally powerful for defenders. Projects like Big Sleep (vulnerability discovery) and CodeMender (automatic vulnerability patching) demonstrate that the same technology can be deployed protectively. The report underscores a fundamental asymmetry — attackers only need to succeed once, while defenders must cover everything — making proactive AI-augmented defense increasingly essential.
