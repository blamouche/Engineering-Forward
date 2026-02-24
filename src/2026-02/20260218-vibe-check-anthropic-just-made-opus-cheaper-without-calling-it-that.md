# Vibe Check: Anthropic Just Made Opus Cheaper Without Calling It That
**Source**: https://every.to/vibe-check/vibe-check-anthropic-just-made-opus-cheaper-without-calling-it-that
**Date**: 2026-02-18
**Author**: Katie Parrott
**Keywords**: anthropic, sonnet, pricing

## Elevator pitch
Katie Parrott reviews Claude Sonnet 4.6, arguing it delivers near‑Opus quality at roughly half the cost, though speed gains are modest and some edge cases persist.

## Takeaways
- Sonnet 4.6 prices are $3/$15 per million tokens, about half of Opus.
- Early tests show Opus‑level quality across coding and complex workflows.
- Speed is not meaningfully faster than Opus, which may disappoint iterators.
- Some reliability issues surface under pressure, despite overall strength.
- The value proposition is strongest for production apps priced out of Opus.

## Synthesis
In this Vibe Check piece, Katie Parrott assesses Anthropic’s Claude Sonnet 4.6 and frames it as a de facto price cut for Opus‑level capability. Sonnet has traditionally been the cheaper, faster sibling to Opus, trading some reasoning power for cost and latency savings. With Sonnet 4.6, Anthropic claims you no longer have to make that tradeoff. The headline is economic: Sonnet 4.6 costs $3 input/$15 output per million tokens—roughly half the price of Opus—and therefore materially reduces operating costs for apps built on Claude’s top tier.

Parrott reports that early day‑zero tests show the model is genuinely strong. Across coding tasks, pull‑request triage, brainstorming, and financial analysis, Sonnet 4.6 followed multi‑step instructions and avoided the mid‑task errors that plagued Sonnet 4.5. One tester ran a full “compound engineering” workflow—merging branches, writing changelogs, and organizing issues—and found no obvious gaps relative to Opus 4.6. This suggests Anthropic has achieved near‑Opus performance in the Sonnet tier, which is a major win for teams constrained by Opus pricing.

The cost reduction is not theoretical. Parrott notes that Every’s AI ghostwriter, Spiral, has been running on Opus at up to $1,000 per day; Sonnet 4.6 would roughly halve those costs without changing the codebase. For teams with large inference bills, this is a meaningful upgrade. The article suggests this is consistent with Anthropic’s strategy: keep tier prices stable while continuously improving performance, so what Opus can do today, Sonnet can do tomorrow at a lower price.

However, speed is the main disappointment. Historically, Sonnet models were faster than Opus, which made them attractive for interactive or iteration‑heavy workflows. Sonnet 4.6 appears to run at roughly the same speed as Opus, so users do not get the expected latency boost. If you were counting on snappier response times, the improvement might feel underwhelming.

Parrott also documents a few reliability quirks. In one example, the model asked to set up a safe work tree and then immediately started rewriting a homepage, acting both overly cautious and overly eager. In another, it got stuck on an MCP configuration issue that Opus resolved quickly. These edge cases suggest that while Sonnet 4.6 is very capable, it still has rough edges that can frustrate advanced users.

The conclusion is pragmatic. For production apps that avoided Opus because of cost, Sonnet 4.6 is the obvious choice: comparable quality at a much lower price. For individuals doing complex, high‑stakes work and already paying for Opus, the switch is less clear because speed gains are minimal and Opus still handles some corner cases better. But for many teams, Sonnet 4.6 looks like the new default.
