# The Agent Stack Is Becoming the Product

*As software shifts from writing code to orchestrating work, the winners won’t be the cleverest models—they’ll be the teams that can run agents safely, cheaply, and without losing accountability.*

For a decade, “software” has meant a familiar thing: you open an IDE, you write code, you ship features. The tools got nicer—better autocomplete, better CI, better observability—but the workflow stayed legible. Humans made the decisions. Code was the artifact.

Now that legibility is breaking.

Across the last wave of writing on agentic development, a coherent picture is emerging: the primary unit of progress is no longer a pull request. It’s a loop. A spec becomes a task. A task becomes an agent run. The agent runs tools. Tools touch real systems. The system produces feedback. The agent tries again.

The result is not “AI helps you code.” It’s that the *agent stack*—how you delegate, verify, recover, and pay for work—becomes the product.

That shift is already showing up in places you might not expect: Apple putting agent primitives into Xcode; open-source labs optimizing models for multi-turn tool use; practitioners reverse-engineering how agent telemetry works; and even investors repricing “software” based on the story they believe about how software will get built.

This isn’t a hype cycle. It’s a workflow change. And workflow changes are the ones that actually stick.

## 1) The vocabulary reset: vibe coding vs. agentic engineering

Addy Osmani’s argument is simple and overdue: we need better words. “Vibe coding” started as a useful label for a real behavior—prompt, accept output, run, paste errors back in, repeat—*without reading the diffs*. It’s fun, fast, and appropriate in narrow contexts: hackathon demos, one-off scripts, personal prototypes.

But the term has become a suitcase. It now gets used to describe disciplined engineering where AI is merely the implementation engine under human supervision. That conflation matters, because it blurs what’s actually risky.

Osmani proposes a cleaner split: vibe coding is YOLO. **Agentic engineering** is professional development where you delegate implementation to agents but keep the grown-up responsibilities: specs, review, tests, documentation, ownership.

In agentic engineering, the human is not a prompt DJ. The human is an architect and a reviewer. That job isn’t smaller. It’s different.

And here’s the uncomfortable kicker: this workflow rewards fundamentals. Senior engineers can get a 2–5× boost while maintaining quality because they can review quickly, reason about edge cases, and know what “good” looks like. Juniors can accidentally ship systems they can’t debug.

If you want the agent era to be safe, you don’t just need better models. You need better engineering habits.

## 2) The IDE’s new job: orchestration, not typing

When Apple adds an agent SDK to Xcode, it’s not because Apple suddenly cares about chat. It’s because the IDE is becoming the control plane.

The interesting part of “Xcode supports the Claude Agent SDK” isn’t branding. It’s the implied primitives: subagents, background tasks, and visual verification in Previews. That’s an admission that an IDE can’t just be a text editor with a compiler bolted on. It has to help you *manage delegation*.

Delegation introduces new failure modes:

- An agent can change the right file for the wrong reason.
- A test suite can pass while the product breaks in an untested corner.
- A “helpful” refactor can silently rewrite a contract you rely on.

To ship software in this world, you need tools that make agent actions reviewable and auditable, not just faster.

This is also why the humble act of “visual verification” matters. If an agent can run and iterate, then humans need high-signal checkpoints: preview diffs, snapshots, UI regression artifacts. Not vibes.

## 3) The hidden economics: the agent cost curve is about *call count*

One of the most useful pieces of analysis in this batch is the claim that agent loops can become “expensively quadratic.” But the real insight isn’t that tokens grow.

It’s that *calls multiply*.

A single coding task can become a chain of micro-requests:

- plan
- search
- patch
- run tests
- interpret failure
- patch again
- re-run
- summarize

Even if each call is cheap, the product of (tokens × calls) becomes the bill.

The uncomfortable twist: as context grows, **cache reads** can dominate. The thing that feels like “reuse” can become the thing you pay for most.

So if you’re building agentic workflows, your biggest lever isn’t just “use a cheaper model.” It’s **reduce the number of turns**.

That means:

- tighter task scoping
- stronger tests so loops converge faster
- better tool outputs so the agent doesn’t thrash
- better memory hygiene so you don’t drag a novel into every call

This is where engineering discipline becomes cost discipline.

## 4) Training is moving from “write code” to “survive the environment”

The Qwen3-Coder-Next post makes an explicit bet: the path to better coding agents is not just bigger parameters, but **scaling agentic training signals**.

That framing matters. Traditional code models optimized completion. Agentic models optimize trajectories. They’re trained on verifiable tasks in executable environments, learning from feedback and failure recovery.

You can see the same story echoed in benchmark talk: SWE-Bench (Verified and Pro) isn’t about producing a nice-looking snippet. It’s about making a real repo pass.

If you’ve ever watched an agent loop fail, you know why this matters. The core skill is not writing a function. It’s continuing to function after the first attempt doesn’t work.

In other words: resilience, tool use, and error recovery become first-class capabilities.

## 5) Observability becomes a feature: what /insights reveals

The reverse-engineered walkthrough of Claude Code’s `/insights` command is a reminder that agent systems generate a new kind of telemetry.

If your developers are delegating meaningful work, you can’t just observe CPU and latency. You need to observe:

- what tasks the agent attempted
- where it got stuck
- which tools it used
- how many turns it burned
- what patterns recur

That’s not just “analytics.” It’s operational safety.

Agent observability is how you prevent a workflow from quietly turning into a money leak—or worse, a security incident.

And that leads to the most important point in the entire batch.

## 6) Transparency isn’t accountability

“AI at work: beyond algorithmic transparency” argues that transparency is an attractive decoy. We can demand disclosures—what model was used, what data was referenced, what the system did—but that doesn’t automatically create accountability.

In the agent era, accountability shifts. The critical question is not “was the AI transparent?” It’s:

- **who delegated judgment?**
- **what guardrails were in place?**
- **what incentives punish honest disclosure?**

If an organization uses agents to accelerate work, it also creates new ways to offload responsibility. The danger isn’t an AI making a mistake. The danger is a human deciding that the AI is the one who should answer for it.

That’s why agentic engineering has to be paired with explicit ownership. Delegation without responsibility is how you get institutionalized blame-shifting.

## 7) The story can move markets before the code moves users

The WSJ take—AI won’t kill software, but it can kill the *growth story*—is a useful reminder that narratives bite before fundamentals do.

If investors believe AI will commoditize software creation, they may reprice companies long before revenue changes. That affects hiring, M&A currency, and the willingness to fund “software as a growth category.”

Even if the story is partially wrong, the second-order effects are real.

This matters for builders because “AI strategy” isn’t only a technical decision. It becomes part of how you justify your moat.

## Where this goes next

If you squint, the pattern is consistent:

- The IDE is becoming an orchestration layer.
- Models are being trained to survive tool feedback, not just complete code.
- Cost is increasingly driven by turn count and context bloat.
- Observability becomes a safety feature.
- Transparency won’t save you from accountability gaps.

If you want a practical definition of the next era of software, here’s one:

**Software is becoming the art of delegated work.**

Your team’s advantage won’t be “who has the best model.” Models will converge. Your advantage will be:

- who can write specs that agents can execute
- who can build tests that agents can’t game
- who can review fast without rubber-stamping
- who can keep the loop cheap
- who can keep responsibility human

That’s not vibe coding.

That’s a new discipline.

---

## Sources
1. [Agentic Engineering](https://addyosmani.com/blog/agentic-engineering/?utm_source=tldrnewsletter)
2. [Qwen3-Coder-Next: Pushing Small Hybrid Models on Agentic Coding](https://qwen.ai/blog?id=qwen3-coder-next&utm_source=tldrai)
3. [Anthropic Performance Team Take-Home for Dummies](https://www.ikot.blog/anthropic-take-home-for-dummies)
4. [AI Won’t Kill the Software Business, Just Its Growth Story](https://www.wsj.com/tech/ai/ai-wont-kill-the-software-business-just-its-growth-story-05673e07?st=4rDCyV&reflink=desktopwebshare_permalink&mod=tldr&utm_source=tldrnewsletter)
5. [Expensively Quadratic: the LLM Agent Cost Curve](https://blog.exe.dev/expensively-quadratic?utm_source=tldrai)
6. [The AI That Called Its Human](https://www.fintechbrainfood.com/p/the-ai-that-called-its-human?utm_source=tldrai)
7. [NanoClaw: a small, container-isolated Claude assistant](https://github.com/gavrielc/nanoclaw?utm_source=www.theunwindai.com&utm_medium=newsletter&utm_campaign=clawdbot-in-just-500-lines-of-code&_bhlid=ee1649147d4a6aa7be0dafb677e397d95ebacbb8)
8. [Deep Dive: How Claude Code's /insights Command Works](https://www.zolkos.com/2026/02/04/deep-dive-how-claude-codes-insights-command-works.html?utm_source=tldrai)
9. [The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+](https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment-blog-3?utm_source=tldrai)
10. [Apple’s Xcode now supports the Claude Agent SDK](https://www.anthropic.com/news/apple-xcode-claude-agent-sdk?utm_source=tldrai)
11. [AI at work: beyond algorithmic transparency](https://patricecochin.substack.com/p/ai-at-work-beyond-algorithmic-transparency?publication_id=4666503&post_id=186850631&isFreemail=true&r=fhb7r&triedRedirect=true&utm_source=substack&utm_medium=email)
12. [New Data: OpenAI's Lead Is Contracting as AI Competition Intensifies](https://www.bigtechnology.com/p/new-data-openais-lead-is-contracting)
13. [We Trained an AI on a Board Game. It Became a Better Customer Support Agent.](https://every.to/playtesting/we-trained-an-ai-on-a-board-game-it-became-a-better-customer-support-agent-299b5938-09dd-4881-803f-aea21f0d461f)
14. [OpenAI Codex: AI Coding Partner](https://openai.com/fr-FR/codex/)
15. [Anthropic Is About to Drop Sonnet 5 During Super Bowl Week](https://www.testingcatalog.com/anthropic-is-about-to-drop-sonnet-5-during-super-bowl-week/)
