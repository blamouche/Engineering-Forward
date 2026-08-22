# Protecting Against AI Inference Theft at Scale
**Source**: https://vercel.com/blog/protecting-against-token-theft
**Date**: 2026-06-03
**Author**: Malte Ubl, Eric Dodds (Vercel)
**Keywords**: inference theft, BotID, AI security, token theft, rate limits, residential proxies, OpenAI-compatible adapter, Vercel, authentication

## Elevator pitch
AI inference is a million times more expensive than HTTP requests, making inference theft one of the highest-margin businesses an attacker can run—Vercel's response is per-request verification using BotID deep analysis, because rate limits and auth walls alone can't stop attackers who buy residential proxies by the thousand.

## Takeaways
- Inference theft is the unauthorized use of someone else's paid AI inference—operators pay per call, attackers pay nothing and resell tokens at a discount
- A single prompt to a frontier model can cost $2, making AI a million times more expensive than HTTP requests (~$2/million)—inference theft is one of the highest-margin businesses an attacker can run
- Attackers wrap custom AI endpoints in OpenAI-compatible adapters and fan calls through residential proxies, defeating IP rate limits and auth walls
- Verification must run on every AI request, not per session—per-session checks amortize the attacker's bypass cost across thousands of stolen calls
- Vercel's BotID deep analysis (powered by Kasada) detected and blocked 10,000+ bot requests in the first minutes of a real attack that spiked to 1,300 requests per minute

## Synthesis
Vercel's analysis of inference theft reveals a threat model that traditional web defenses can't handle. HTTP requests cost roughly $2 per million, but a single AI prompt to a frontier model can cost $2—making AI inference a million times more expensive per call. This economic asymmetry makes inference theft one of the highest-margin businesses an attacker can run: steal inference from a paid endpoint, resell the tokens at a discount, and pocket the difference with zero marginal cost.

The attack architecture is sophisticated. Attackers wrap a victim's custom AI endpoint in an OpenAI- or Anthropic-compatible adapter, making the stolen calls drop into any standard coding agent or SDK. They fan calls through residential proxies that obscure real client IPs, defeating per-IP rate limits. The adapter serves as the session boundary for the attacker's downstream users—they authenticate to the adapter, not to the victim's endpoint. By the time a call hits the victim's API, it has already crossed the boundary the defender was planning to protect.

A real attack on Vercel's own docs AI chat endpoint on April 12, 2026 illustrates the scale: traffic spiked to 1,300 requests per minute (ten times normal), translating to an inference cost run rate of over $10,000 per day. Across hundreds of thousands of bot requests over two days, standard per-IP rate limits had nothing useful to act on because the attacker used residential proxies.

The defense requires a fundamental shift: verification on every AI request, not per session. If a gate runs at session start, the attacker pays the bypass cost once and walks away with hundreds of thousands of stolen calls. Per-request gates force the ratio to one—defeating a check on every call isn't worth the cost. Vercel deploys BotID deep analysis, an invisible CAPTCHA powered by Kasada that uses client-side machine learning to distinguish humans from bots without a visible challenge. It detected and blocked more than 10,000 bot requests in the first minutes of the attack, and within 24 hours request volume was back to normal. Traditional image CAPTCHAs no longer work because the same AI models that make inference worth stealing can easily bypass them.