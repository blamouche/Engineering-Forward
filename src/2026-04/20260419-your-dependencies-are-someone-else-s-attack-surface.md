# Your Dependencies Are Someone Else's Attack Surface

**Source**: https://quodeq.ai/blog/supply-chain-attack-surface/
**Date**: April 2026
**Author**: Victor Purcallas Marchesi
**Keywords**: quodeq, your, dependencies, someone, else, attack, surface

## Elevator pitch
Supply chain attacks have escalated sharply in fifteen months. Shai-Hulud, Axios, TeamPCP, and what you can do about it

## Takeaways
- ← All posts April 2026 By Victor Purcallas Marchesi Your Dependencies Are Someone Else's Attack Surface Someone spent two years writing helpful patches for a compression library.
- The kind of contributor every open-source project dreams of.
- It runs on every major Linux distribution, every server you have ever used to deploy anything.
- The contributor called himself Jia Tan, and the patches contained a backdoor that would have given an attacker remote access to virtually any Linux machine on the planet.
- A Microsoft engineer named Andres Freund noticed that SSH logins were taking half a second longer than they should.

## Synthesis
← All posts April 2026 By Victor Purcallas Marchesi Your Dependencies Are Someone Else's Attack Surface Someone spent two years writing helpful patches for a compression library. The kind of contributor every open-source project dreams of. It runs on every major Linux distribution, every server you have ever used to deploy anything. The contributor called himself Jia Tan, and the patches contained a backdoor that would have given an attacker remote access to virtually any Linux machine on the planet. A Microsoft engineer named Andres Freund noticed that SSH logins were taking half a second longer than they should. What happened in the last twelve months In September 2025, a self-replicating worm called Shai-Hulud compromised over 500 npm packages. It started with phishing: developers received emails that looked like npm asking them to update their MFA settings. Once it had a developer's credentials, it automatically injected malicious code into every other package that person maintained, then used those packages to harvest more credentials. Shai-Hulud 2.0 hit over 25,000 GitHub repositories across 350 user accounts. It installed persistent backdoors via GitHub Actions runners, recycled stolen credentials across victims to build a botnet-like network, and included a dead man's switch designed to delete user data if anyone tried to contain it.
