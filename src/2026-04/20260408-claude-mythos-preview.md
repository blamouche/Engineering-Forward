# Claude Mythos Preview

**Source**: https://red.anthropic.com/2026/mythos-preview
**Date**: April 7, 2026
**Author**: Anthropic Frontier Red Team
**Keywords**: mythos preview, exploit generation, zero-day, cyber capability, autonomous vulnerability research

## Elevator pitch
Anthropic’s red-team write-up argues that Mythos Preview represents a real step change in autonomous cyber capability, including zero-day discovery and exploit construction across major operating systems and browsers.

## Takeaways
- Anthropic claims Mythos Preview can both find subtle vulnerabilities and often exploit them autonomously.
- The team says the model has saturated many prior cyber benchmarks, forcing a shift toward real-world evaluation.
- Examples include deep bugs in mature codebases and multi-stage exploit chains.
- The write-up stresses that these abilities emerged from general coding and reasoning gains, not narrow cyber tuning.
- The report is essentially an argument for restricted deployment plus urgent defensive preparation.

## Synthesis
Compared with the higher-level Glasswing announcement, this post is where Anthropic tries to earn the scary claim. The notable thing is not just bug finding, but the combination of real code reading, exploit synthesis, and enough autonomy to complete long vulnerability workflows with minimal human steering. If accurate, that shifts the conversation from “LLMs help security researchers” to “frontier models are becoming independent cyber operators in constrained environments.” For engineering orgs, the practical implication is that secure development and patch management may soon need to assume both defenders and attackers can cheaply automate parts of offensive research. That would make exploit windows shorter and the value of continuous code scanning much higher.
