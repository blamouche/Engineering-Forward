# Angela Jiang (Anthropic), Katelyn Lesse (Anthropic): "Anthropic veut amener Claude à un niveau de perpétuelle autonomie"
**Source**: https://www.journaldunet.com/intelligence-artificielle/1550545-anthropic-veut-amener-claude-a-un-niveau-de-perpetuelle-autonomie/
**Date**: May 25, 2026
**Author**: Benjamin Polge
**Keywords**: Anthropic, Claude, autonomie, agents, coding, Computer Use, Mythos, harness, AI engineering, Developer Tools

## Elevator pitch
Anthropic's product and engineering leads detail their strategy to make Claude perpetually autonomous — self-correcting, self-learning, and capable of working unsupervised for days — while leveraging improved model scaling and well-designed harnesses to unlock disproportionate performance gains.

## Takeaways
- Anthropic segments its products (Claude Code, Cowork, Desktop App) by user persona rather than building a unified tool, with each optimized for different use cases via distinct system prompts and tools.
- Claude Code Desktop differs from CLI by supporting remote agents in sandboxes, enabling asynchronous work off the local machine.
- The engineering team achieves rapid delivery by being "AI-pilled" — using their own tools extensively, running dozens to hundreds of concurrent agents, and investing heavily in testing and auto-verification loops.
- The roadmap targets perpetual autonomy, better context handling, improved Computer Use for complex enterprise UIs (Bloomberg terminals, EHR systems), and self-learning from errors.
- A well-built harness coupled with improved models now yields disproportionate performance gains — the dynamic has flipped from requiring massive harness investment for marginal returns.

## Synthesis
In an interview during Anthropic's Code with Claude developer conference in London, Angela Jiang (Head of Product, Claude Platform) and Katelyn Lesse (Head of Engineering, Claude Platform) laid out the company's bold roadmap toward perpetual AI autonomy. The core thesis: Claude should be able to code, self-correct, and operate without supervision for days.

The product segmentation strategy is deliberate. Rather than a single unified tool, Anthropic offers different "form factors" — Claude Code for engineers comfortable in terminals, Cowork for non-engineers, and a Desktop app that combines local execution with the ability to dispatch remote agents to sandboxes for asynchronous work. All share a common platform of tool APIs and harnesses, differentiated by system prompts tuned for each audience.

Lesse attributed their rapid delivery cadence to an engineering culture fully embracing AI-driven development. Teams range from beginners doing prompt-based debugging to engineers orchestrating hundreds of concurrent agents — with the most advanced practitioners having invested deeply in robust testing infrastructure and self-verification loops that enable genuine automation at scale.

Jiang outlined three frontier capabilities: infinite context handling, perpetual autonomy, and enhanced Computer Use targeting complex legacy UIs. Bloomberg terminals and EHR systems exemplify the kind of "obscure interfaces" where autonomy delivers outsized value. Additionally, Claude needs to learn from mistakes and self-improve at scale, potentially leveraging memory primitives for self-directed learning.

Perhaps the most technically significant insight concerns the evolving relationship between models and harnesses. Historically, extracting value from the software layer required disproportionate investment relative to model capabilities. Anthropic has observed that dynamic reversing — as models become more powerful, a moderately sized but well-constructed harness delivers dramatically higher performance gains. This suggests software engineering around models is becoming more capital-efficient, not less, as foundation models advance. Jiang confirmed that while more compute is "almost always" needed, significant progress can come from harness improvements alone.

On Mythos, Anthropic's powerful but contained generalist model, Jiang highlighted its best-ever METR benchmark endurance score and strong coding performance — capabilities that will eventually flow to enterprise offerings while maintaining appropriate safety constraints.
