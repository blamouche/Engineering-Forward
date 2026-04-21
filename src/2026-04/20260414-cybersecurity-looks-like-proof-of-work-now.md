# Cybersecurity Looks Like Proof of Work Now

**Source**: https://www.dbreunig.com/2026/04/14/cybersecurity-is-proof-of-work-now.html
**Date**: April 14, 2026
**Author**: Daniel Breunig
**Keywords**: cybersecurity, proof of work, Mythos, exploit discovery, security economics

## Elevator pitch
Daniel Breunig argues that if frontier models keep finding exploits as long as defenders keep buying tokens, software hardening starts to look like a proof-of-work race where security goes to whoever can afford more compute.

## Takeaways
- AISI’s Mythos evaluation suggests frontier models can keep improving attack performance with larger token budgets.
- That creates a security economy where defenders may need to spend more on exploit discovery than attackers spend on exploitation.
- The argument strengthens the case for shared open-source hardening because pooled token budgets can improve common dependencies.
- Agentic development workflows may split into development, review, and a separate hardening phase driven primarily by budget.
- The article reframes secure software as expensive not because code is hard to write, but because exploit search may become a compute market.

## Synthesis
This article offers a sharp economic lens on AI-enabled security. Rather than focusing only on whether a frontier model can complete a sophisticated attack path, Daniel Breunig asks what the cost curve means if the model keeps improving as more tokens are spent. Using Anthropic’s Mythos and the UK AI Security Institute evaluation as the concrete case, he argues that security may increasingly resemble proof of work. In that world, success is not about having a clever insight once, but about sustaining enough compute and budget to keep searching until vulnerabilities appear or are exhausted.

That framing matters because it changes how we think about defense. Historically, organizations treated audits and pentests as periodic expert exercises. If exploit discovery becomes a token-budget problem, then hardening turns into an ongoing spend decision. Defenders need to invest enough in automated exploit search to outspend, or at least outlast, likely attackers. The relevant constraint shifts from scarce human security labor to capital allocation. That does not eliminate expertise, but it does mean the economics of secure software may increasingly be set by the market value of exploits and the price of model-powered search.

One of the article’s strongest ideas is its implication for open source. If major companies spend token budgets to harden widely shared dependencies, those libraries may become more secure than bespoke internal reimplementations. That directly pushes back on the emerging instinct to replace dependencies with agent-generated code just to reduce supply-chain exposure. Under a proof-of-work model, shared software can benefit from pooled defensive spend and broader scrutiny, even if attackers are also incentivized to target it. The argument is not that open source is automatically safer, but that collective hardening budgets can become a real moat.

Breunig also sketches a likely workflow shift for software teams: development, review, then hardening. The first phase stays guided by human judgment and product goals. The last phase becomes a budgeted computational assault against your own system before others do it first. That is a useful way to think about where agentic engineering may go next. Code generation keeps getting cheaper, but secure code may stay expensive because the cost of confidence is set by how much attack surface you can afford to probe.
