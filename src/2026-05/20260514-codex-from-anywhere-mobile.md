# Work with Codex from Anywhere — Codex Comes to Mobile

**Source:** [OpenAI Blog](https://openai.com/index/work-with-codex-from-anywhere) — May 14, 2026

## TL;DR
Codex is now available in the ChatGPT mobile app (iOS + Android preview, all plans). Connect to any machine running Codex (laptop, Mac mini, remote environment) and work across threads, review outputs, approve commands, change models from your phone. Also: Remote SSH GA, Hooks GA, programmatic access tokens, and HIPAA-compliant support for Enterprise.

## Key Points

### Mobile Experience
- Full Codex client in ChatGPT mobile app — not just remote control
- Connect to any machine running Codex via secure relay layer
- Live state sync: screenshots, terminal output, diffs, test results, approvals
- Files, credentials, permissions stay on the machine where Codex operates

### Use Cases for Mobile Codex
- **Start investigating a bug** while waiting for coffee — follow along with screenshots/diffs
- **Reach a decision point during commute** — review tradeoffs, choose a path, work continues
- **Prepare for customer conversations** — synthesize updates, flag open questions, generate briefing
- **Send new ideas while fresh** — start a thread that takes shape before you return to desk

### Enterprise Updates
- **Remote SSH** (GA): connect Codex directly to remote environments via SSH config; detected automatically
- **Hooks** (GA): scan prompts for secrets, run validators, log conversations, create memories, customize behavior
- **Programmatic access tokens**: scoped credentials from ChatGPT workspace settings for CI/CD, automations
- **HIPAA-compliant** Codex in local environments for ChatGPT Enterprise

### Scale
- 4M+ people use Codex weekly
- Same secure relay infra connects phone ↔ desktop ↔ remote environments

## Relevance to Engineering-Forward
Mobile agent access is a key unlock for the "always-on agent" paradigm. Remote SSH + Hooks GA signals that enterprise agent infrastructure is maturing rapidly. The relay architecture (secure, no direct exposure) is worth studying for any agent platform.
