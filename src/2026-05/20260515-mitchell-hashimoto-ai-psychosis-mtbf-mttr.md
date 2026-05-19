# Mitchell Hashimoto on AI Psychosis and the MTBF vs MTTR Reckoning

**Source:** Thread Reader App (Twitter/X thread by @mitchellh)
**Author:** Mitchell Hashimoto
**Date:** May 15, 2026
**URL:** https://threadreaderapp.com/thread/2055380239711457578.html

## Summary

Mitchell Hashimoto (HashiCorp co-founder) warns that entire companies are operating under "heavy AI psychosis" — an almost absolute "MTTR is all you need" mentality where shipping bugs is considered acceptable because AI agents will fix them quickly at scale. He draws a parallel to the cloud/infrastructure MTBF vs MTTR reckoning, where the industry learned that resilient systems can't be replaced entirely by fast recovery.

## Key Points

- **"AI psychosis":** Companies believe it's fine to ship bugs because agents will fix them quickly at scale that humans can't match
- **Infrastructure parallel:** The cloud/automation transition taught us that MTTR (mean-time-to-recovery) is great but you can't eliminate resilient systems entirely
- **The dismissal pattern:** When concerns are raised, responses are "it has full test coverage" or "bug reports are going down" — which don't paint the whole picture
- **Resilient catastrophe machines:** Systems can appear healthy by local metrics while globally becoming incomprehensible
- **Warning signs:** Bug reports going down while latent risk explodes; test coverage rising while semantic understanding falls; changes happening so fast nobody notices architecture decaying
- **Personal concern:** Hashimoto can't even bring this up to friends because the conversation gets dismissed immediately

## Why It Matters

A deeply respected infrastructure founder (HashiCorp) is sounding the alarm that the AI industry is repeating the same mistake the DevOps movement already solved — confusing speed of recovery with system resilience. The concern isn't anti-AI; it's that agentic development without resilient systems thinking produces fragile architectures that look healthy in metrics but are disasters waiting to happen.
