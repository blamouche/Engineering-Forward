# AI Agents Can Think. Now They Can Pay.
**Source**: ByteByteGo (bytebytego@substack.com)
**Date**: 2026-09-28
**Author**: ByteByteGo
**Keywords**: Machine Payments Protocol, MPP, Stripe, Tempo, AI agents, HTTP 402, micropayments, sessions, IOU, delegated keys, spending caps, internet payments, IETF

## Elevator pitch
ByteByteGo deep-dives the Machine Payments Protocol (MPP), co-authored by Stripe and Tempo, which gives AI agents a native way to pay for services via HTTP headers — covering the Challenge-Credential-Receipt flow, session-based micropayments, spending guardrails, and the commercial implications of removing human signup flows.

## Takeaways
- MPP (Machine Payments Protocol) was co-authored by Stripe and Tempo, launched March 18, 2026, with the core specification submitted to the IETF standards track — the same body that maintains HTTP
- The protocol uses three core objects: Challenge (server asks for payment), Credential (client sends proof), and Receipt (server confirms delivery) — all placed in HTTP headers (WWW-Authenticate: Payment, Authorization: Payment, Payment-Receipt)
- When an agent requests a service, the server returns HTTP 402 Payment Required with payment details; the agent checks the terms, authorises payment via a delegated key with a spending cap, and retries with proof — no account creation or API keys needed
- Session-based payments solve the micropayment problem: agents open a session with a deposit, then pay each request with a signed IOU; when the session ends, the server claims the total in one real transaction, dividing a single processing fee across thousands of requests
- Spending guardrails include delegated keys with per-period caps, fixed expiry, permitted-recipient lists, and separate keys per deployment — so a runaway agent cannot spend beyond its limit
- MPP removes the signup flow entirely: the seller only gets a public key, not a company name or email — payment is no longer a form of identification, which breaks traditional abuse control, dispute management, and sales funnels
- Identity and disputes are being built as separate layers rather than attached to the payment flow, using specifications backed by Visa and Cloudflare for agent signing
- As of August 2026, about 30,000 transactions are MPP transactions — small, but comparable to the early days of the Apple App Store where first-year revenue said little about the platform's eventual scale
- Michael Blau demonstrated agents paying per article from publications like ByteByteGo using Drip and a Tempo wallet, without subscriptions — writers get paid behind the scenes even for a single cent

## Synthesis
MPP represents a fundamental rethinking of internet commerce: it removes the human from the payment loop and replaces the signup flow — which served as identity verification, abuse control, and sales pipeline — with a cryptographic proof of payment that carries no identity. The Challenge-Credential-Receipt flow is elegantly minimal because it has to be: agents cannot fill forms, recognise checkout buttons, or make the judgement calls that humans use to navigate heterogeneous payment pages. By placing terms in standardised HTTP headers, MPP creates a universal interface that any agent can parse and any service can serve, without prior knowledge of each other.

The session mechanism is the key innovation that makes micropayments viable. The fundamental problem with per-request payment is that processing fees are flat — a cent-sized transaction costs more than a cent to settle. By accumulating signed IOUs within a session and settling once at the end, MPP drives per-request cost to nearly zero while keeping latency at the milliseconds needed for a signature check. This makes real-time agent workflows economically feasible: an agent making thousands of search queries, lookups, and API calls within a single task can pay pennies per request without each transaction being individually settled.

The commercial implications are profound and underexplored. Removing the signup flow means losing the entire customer acquisition pipeline: no landing page visits, no free-tier conversions, no sales calls, no customer records. The seller gets a public key and a payment — nothing more. This forces a rethinking of abuse control (you cannot ban an account that does not exist), dispute resolution (there is nobody to contact after the transaction), and revenue models (advertising-funded content faces a paid-access alternative where machines pay per request). The guardrails — delegated keys with spending caps, immutable logs out of the agent's reach, and advisory-only directories — are necessary but insufficient: the real risk is that a protocol designed for machines paying machines creates an economy where the human is structurally absent from every transaction.