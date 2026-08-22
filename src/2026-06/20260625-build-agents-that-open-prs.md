# Stop Building Chatbots. Build Agents That Open PRs.
**Source**: https://zackproser.com/blog/build-agents-that-open-prs
**Date**: 2026-06-24
**Author**: Zachary Proser
**Keywords**: AI agents, pull requests, reviewable artifacts, chatbots, agent engineering, CI gates, software workflow

## Elevator pitch
The unit of useful agent work is a reviewable artifact — a PR, a draft, a diff — not a chat reply, because a chat reply evaporates while a PR sits in a queue with your name on it until you decide.

## Takeaways
- A chat reply evaporates — you read it, scroll past, and ten minutes later it's gone; a pull request sits in GitHub with your name on it until you deal with it, has a diff, has status checks, and either passes the gate or doesn't
- The unit of useful agent work is a reviewable artifact (PR, draft, diff) not a chat reply — if the output is a chat paragraph, you still have the job; if it's a PR with passing checks, you have a decision to make
- A gate (CI, tests, linter, validation script) is load-bearing: the agent must satisfy checks before its output reaches a human, which is what lets you trust the queue
- Reject should be the default: nothing the agent produces should ship without an explicit yes from someone who owns the outcome — the agent runs the bellows, the human keeps the quench
- The pattern generalizes: "ask the docs" bot → PR against docs repo with proposed paragraph; "summarize incident" bot → drafted postmortem for review; "fix config" bot → one-line diff with failing test linked

## Synthesis
Zachary Proser's manifesto for building agents that open PRs rather than chatbots is one of the most practical and well-argued pieces on agent engineering architecture published this year. His central thesis is deceptively simple: the unit of useful agent work is a reviewable artifact — a PR, a draft, a diff — not a chat reply. The difference is that a chat reply evaporates (you read it, nod, scroll, and ten minutes later it's gone) while a PR sits in a queue with your name on it until you decide.

The analysis of why chat replies are a dead end is precise. The common chatbot flow — ask, think, stream prose, copy the part you wanted, paste it somewhere, fix the three things it got wrong — means the agent did real work and then handed it to you in the one format that guarantees you have to do the work again. The chat reply has no home: it doesn't live in the system where the work lives, can't be checked by CI, can't be diffed against what was there before, can't be approved by a second person. You are the storage layer, the validation layer, and the merge button, doing all three by hand from memory.

The worked example — Proser's own blog bot — is the article's strongest evidence. When he `@`-mentions the agent in Slack with an opinionated post idea, it doesn't reply with 1,700 words of markdown. It opens a pull request against his portfolio repo. Between the Slack message and the PR, the agent runs a pipeline: reset repo, survey recent posts to calibrate voice, draft the page, scan for banned phrases, generate and upload images, boot the site locally, render the post, generate the OG image, and run `verify-blog-post.sh` — which exits nonzero if any check fails, preventing the PR from being opened. The gate is load-bearing.

The `verify-blog-post.sh` script checks falsifiable things: files exist, CDN images return 200, internal links resolve, no banned phrases, OG image is live. If any fail, the agent does not open the PR. This is the key insight: the agent is built so it cannot hand the author a draft that fails the checks they know how to automate. It can still hand them a draft that passes every check and is wrong in a way no script catches — which is exactly why the PR exists, so a human reads it before it ships.

The "spark, bellows, and quench" metaphor is powerful. The agent runs the bellows (the mechanical middle, the rough draft, the scaffolding). The human keeps the quench (hitting merge, putting their name on it, standing behind it). A chat reply collapses all three into one ambiguous blob. A PR keeps the boundary crisp: the machine opens it, you close it. The failures move from "silently absorbed by the human" to "visible, gated, and reversible." A clean reject should cost ten seconds; if it costs ten minutes, the gate is too weak.