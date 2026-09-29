# How I AI: Jev for Beginners + I Left Claude for Months, Opus 5.5 Brought Me Back + Opus 5.5 vs. GPT-6 Sol Bench
**Source**: Lenny's Newsletter (lenny+how-i-ai@substack.com)
**Date**: 2026-09-28
**Author**: Lenny (Claire Vo)
**Keywords**: Jev, TypeSafe, decision model, Claude Opus 5.5, GPT-6 Sol, GPT-6 Astra, Fable 5, Codex, model review, blind test, SVG, frontend, agentic tasks, pricing, cross-model review

## Elevator pitch
Lenny's How I AI podcast covers three topics: Claire tests Jev (TypeSafe's decision model) for large-scale classification at 4 cents per million tokens, returns to Claude after months because Opus 5.5 fixed its personality problem, and blind-tests Opus 5.5 vs GPT-6 Sol across eight categories from writing to SVG illustration.

## Takeaways
- Jev is a decision model, not a language model — it returns predefined values like categories, scores, or probabilities instead of generating text, covering roughly 90% of what software workflows actually need at 4 cents per million input tokens with no output-token fee
- Claire used Jev to compare 1,700 ChatPRD pull requests across 17,000 pairs for 9 cents, learning that nearly 30% of engineering work went toward platform, security, and infrastructure
- Jev classified locally stored Claude Code and Codex sessions in minutes, revealing that engineering fell from nearly 100% of Claire's AI usage in January to less than 40% by September
- Jev paired with a frontier model is far more powerful: Jev classifies, clusters, filters, and routes large datasets, then only the most important groups go to GPT-6 Astra for deeper reasoning — processing 1,100 signals and 200,000 operations for about $4
- Claire built a voice app where Jev's decisions were so fast that the quote API became the slowest part of the workflow
- YouTube comment analysis is an immediate use case: Claire classified 4,500 comments by sentiment, identified 58 containing episode ideas, and built a keyword search scanning the full dataset in under a second
- Opus 5.5 is the first Claude model that no longer makes Claire's "blood boil" — its rambling, preachy, verbose personality was fixed, which no benchmark captures but which matters enormously for daily use
- Opus 5.5 is 40% cheaper than Opus 5 and noticeably faster, completing four complex tasks spanning inbox triage, backend development, research, and computer use including runs of up to 82 steps from a single prompt
- Opus 5.5 is the strongest frontend designer Claire has tested — its ChatPRD homepage redesign was bold and polished enough to ship, handling hierarchy, white space, and visual rhythm exceptionally well
- The best use of Opus 5.5 may be as an adversarial reviewer: Claire now has Codex and Opus review each other's work, a cross-model loop that catches issues either model might miss alone
- In the blind taste test, GPT-6 Astra "won Claire's heart," Opus 5.5 "won her week," and Sol delivered mixed results while remaining a favorite for everyday work — dash-heavy writing was an immediate warning sign for agent personality
- GPT-6 Sol costs roughly half as much as Opus 5.5, which changes how teams should route work; Claire also believes teams should optimise caching before obsessing over model choice

## Synthesis
The How I AI episode reveals three distinct shifts in how experienced practitioners are using AI models. First, Jev's decision model architecture represents a category break: instead of using a frontier LLM for everything, Claire routes classification, routing, and filtering tasks to a purpose-built model that costs orders of magnitude less. The 9-cent pull request analysis and the $4 product insights graph demonstrate that many workloads do not need language generation at all — they need decisions. The key insight is that pairing Jev with a frontier model creates a two-tier pipeline where the expensive model only sees the cases that matter, which is a fundamentally different architecture from "send everything to GPT-6."

Second, Opus 5.5's return to Claire's workflow is driven by ergonomics, not benchmarks. The fact that she abandoned Claude for months because of its personality — rambling, preachy, verbose — and returned only when Opus 5.5 fixed this, illustrates that model quality is multidimensional. No benchmark captures "I don't want to strangle this model," but it determines whether a model gets used at all. The cross-model review pattern, where Codex and Opus review each other's work, is a practical response to the fact that no single model is best at everything: instead of choosing, use both as adversarial checkers.

Third, the blind taste test reveals that price changes model routing. Learning that GPT-6 Sol costs roughly half of Opus 5.5 immediately changed how Claire thought about which model to use for which task. Combined with her observation that teams should optimise caching before model choice, this suggests the model market is maturing beyond "which model is best" toward "which model is cheapest for the quality level this task requires" — the same commoditisation trajectory that every computing layer eventually follows.