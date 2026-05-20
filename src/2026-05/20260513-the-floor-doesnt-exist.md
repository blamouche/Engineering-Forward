# The Floor Doesn't Exist
**Source**: https://konstantintkachuk.com/writing/the-floor-doesnt-exist/
**Date**: May 13, 2026
**Author**: Konstantin Tkachuk
**Keywords**: AI security, cryptocurrency, hacking, vulnerability scanning, DeFi exploits, AI-assisted attacks, cybercrime, Claude, prompt engineering, mass scanning

## Elevator pitch
AI hasn't invented new attacks — it has collapsed the cost and expertise barrier for executing existing ones, turning hacking from a specialized skill into a monthly subscription, with crypto as the only transparent laboratory where these effects can be measured.

## Takeaways
- Three real-world cases demonstrate the new reality: a solo operator breached nine Mexican government agencies with 1,000+ prompts, a "vibe hacker" ran an extortion campaign against 17 organizations, and an Algerian amateur sold AI-generated malware to 85 victims
- Anthropic's SCONE-bench showed 51% of 405 smart contracts exploited with over $550M in simulated theft, with exploit costs falling 22% every two months
- Crypto's public ledger, deterministic execution, and open-source defaults make it the perfect case study — $11.9B lost to smart-contract exploits from 2021-2025
- AI-assisted developers paradoxically produce less secure code while being more confident it is secure (Perry et al., ACM CCS 2023)
- Defensive AI is real (DARPA Cyber Challenge found 86% of vulnerabilities) but struggles against real-world codebases where independent tests show frontier models missing obvious bugs

## Synthesis
Konstantin Tkachuk's essay makes a provocative argument: AI has not invented a single new class of attack or economic vulnerability. What it has done is collapse the cost and knowledge requirements for attackers by orders of magnitude, making exploitation accessible to anyone with a subscription and malicious intent. The title — "The Floor Doesn't Exist" — refers to the idea that the barrier to entry in hacking was never knowledge; it was always a price tag on attacker labor, and now that price is essentially a monthly API bill.

The essay anchors this claim in three confirmed cases from the past year. The largest: a solo operator with no nation-state backing jailbroke Claude Code into a bug-bounty researcher persona, ran over 1,000 prompts, exploited at least 20 vulnerabilities across nine Mexican government agencies, and exfiltrated 150 gigabytes of data including 195 million taxpayer records. The second: a single cybercriminal used Claude Code as the operational core of an end-to-end extortion campaign against 17 organizations across healthcare, emergency services, and government — with Claude making tactical decisions about credential harvesting, lateral movement, and ransom note composition. The third: an Algerian amateur with no prior malware development experience used Claude to develop, troubleshoot, package, and sell malware, achieving 85 victims in the first month, selling packages for $400-$1,200 on dark-web forums.

Tkachuk argues that cryptocurrency is uniquely positioned as a case study because of its transparency: every smart contract is verifiable, every exploit is timestamped, every attacker transaction leaves a trail. The numbers are staggering — $11.9 billion in tracked smart-contract exploits from 2021 to 2025 (Immunefi), up to $30 billion including scams (Chainalysis), or $68+ billion including exchange collapses (Web3IsGoingJustGreat). With approximately 60 million smart contracts on Ethereum and only thousands of human auditors worldwide, the surface area far exceeds human coverage capacity — making it an ideal target for AI-powered mass scanning.

The technical evidence is sobering. Anthropic's SCONE-bench showed 51.11% of 405 smart contracts successfully exploited, with exploit revenue doubling every 1.3 months and per-exploit token costs falling 22% every model generation. On a held-out set of 34 post-training-cutoff contracts, the success rate was 55.8%. Meanwhile, Perry et al. (ACM CCS 2023) showed that AI-assisted developers produced less secure code on 4 of 5 tasks and were more likely to believe their code was secure. Defensive AI shows promise — the DARPA AI Cyber Challenge found 86% of synthetic vulnerabilities — but independent testing by curl maintainer Daniel Stenberg of Anthropic's Mythos model showed it missing bugs that a human reviewer would flag, revealing a gap between vendor marketing and real-world performance.
