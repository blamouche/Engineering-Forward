# The new engineering job is to make systems legible to agents

*When models write most of the code, the scarce resource becomes constraints, context, and verification.*

For most of software history, the center of gravity was obvious: a human reads requirements, writes code, then tries (often heroically) to make production match intent. The tools improved—IDEs, CI, cloud, frameworks—but the shape of the job stayed largely the same.

That shape is starting to break.

Not because code disappears, but because the bottleneck is moving. If you buy the premise that AI systems can now generate large volumes of “correct-looking” code quickly, then writing code stops being the limiting factor. The limiting factor becomes: **can the system reliably converge on the right change, in the right direction, without blowing up everything around it?**

This week’s reading pile is a neat cross-section of that transition: agent-first engineering inside OpenAI; the emergence of “skills” as a packaging layer for procedures; a browser architecture designed for agentic interaction; tools to capture agent transcripts as part of Git; warnings about autonomy and security; and even, oddly, the digitization of smell—a reminder that what matters is the representation layer that makes a messy world computable.

The pattern that ties it together is simple:

> As agents get more capable, engineering becomes the design of constraints and feedback loops that make their work dependable.

## 1) The bottleneck shifts: from typing to scaffolding

OpenAI’s “Harness engineering” write-up is blunt about the endgame they tested: a small team shipped an internal product with essentially *no* code written “by hand,” but with an enormous amount of code produced by Codex across many PRs. The interesting part isn’t the headline. It’s the conclusion: in an agent-first world, engineers spend more time designing the environment the agent operates in—tools, invariants, observability, guardrails—than on line-by-line implementation.

This resonates with the Lenny’s Podcast notes featuring Sherwin Wu: engineers running “fleets” of 10–20 parallel agents, with code review times collapsing. That’s a different job. When throughput is cheap, you optimize for **spec clarity, fast verification, and safe rollback**.

There’s a subtle but important corollary: scaffolding is temporary. Wu’s quoted line—“models will eat your scaffolding for breakfast”—isn’t a call to stop building tooling. It’s a reminder to build the *right kind* of tooling:

- Prefer **mechanical invariants** (linters, tests, architectural constraints) over brittle prompt glue.
- Prefer **repo-embedded knowledge** (documents that evolve with the codebase) over one-off chat context.
- Prefer **interfaces that survive model upgrades** over hacks that assume today’s limitations.

If you treat agents like interns, you’ll overfit your process to supervision and retries. If you treat them like a new compiler target, you’ll invest in what compilers need: explicit constraints, deterministic build steps, and debuggable artifacts.

## 2) Skills: the missing middle layer between prompts and tools

A lot of “agent failure” is not intelligence—it’s packaging.

The OpenAI “Skills in API” cookbook frames skills as a standardized bundle: instructions, scripts, assets, versioned and mountable into an execution environment. That’s important because it creates a crisp separation of concerns:

- **System prompt**: enduring behavior and boundaries.
- **Tools**: side effects and access (APIs, shell, filesystem).
- **Skills**: *procedures*—the reusable playbooks that connect intent to tool use.

This is the same point the finance/Claude Code article makes from a different angle: adoption fails when “AI” is treated as one-shot chat instead of a production system. The biggest accelerator is not turning analysts into programmers; it’s defining tasks with stable output formats, then reusing them.

Once you accept that, “skills” are inevitable. Enterprises don’t want ten different employees improvising ten different ways to do “earnings preview.” They want a procedure they can version, audit, and refine.

And once skills exist, the job shifts again: good engineers become *procedure designers*. The question becomes less “can the model do it?” and more “what is the smallest, safest, most reusable procedure that makes this task boring?”

## 3) Legibility is the new architecture: agents need a map, not a manual

A recurring theme across multiple sources is **legibility**.

OpenAI’s harness note argues that knowledge must live in the repo: a short AGENTS.md as a table of contents, with structured docs that an agent can traverse. Boris Tane’s “How I use Claude Code” is essentially a human process for manufacturing legibility: research → plan → annotation cycle → todo → implementation. The plan is a durable artifact that can be reviewed and corrected before any code changes happen.

Tools like Entire take this one step further: capture agent transcripts and touched files on every push, store them on a dedicated branch, and enable rewind/resume. That’s not “nice to have.” It’s recognition that with agents, you’ll generate more changes, faster—and you’ll need to recover from mistakes cheaply.

The deeper insight: **Git captures what changed, not why.**

When code is increasingly authored by a system that can’t be cross-examined later (“why did you do this?”), you need to make intent auditable. Capturing transcripts is one approach. Forcing a written plan is another. Encoding constraints in tests is the strongest option, because it is executable intent.

This also hints at a new engineering aesthetic: codebases will increasingly be designed as *training environments* for agents—systems where the right move is easy and the wrong move is hard.

## 4) The distributed systems problem doesn’t go away—it gets louder

Joe Hellerstein’s essay is the cold shower in the room.

If agents make it cheap to produce lots of code, they also make it cheap to produce lots of distributed-system footguns. The nastiest failures in production aren’t syntax errors; they’re retries, partial failure, ordering, idempotency, long-lived state, and “implicit contracts” between components that no one wrote down.

Hellerstein’s thesis is refreshing: don’t rely on heroic testing to catch every interleaving. Instead, change the *surface area* where code is expressed so whole classes of bugs are unrepresentable.

Frameworks and languages that make nondeterminism explicit (marking it, typing it, constraining it) are not academic luxuries in an agentic era. They’re practical: they reduce the number of places where an agent can accidentally smuggle in a false assumption.

In other words: when the producer of code is probabilistic, your runtime model should be more deterministic.

## 5) Agentic browsing is architecture, not a feature

The Atlas browser architecture piece looks like “browser nerd trivia,” but it’s actually a clue about where product design is heading.

Atlas reportedly isolates Chromium in a separate host process and uses an intermediate layer (OWL) with IPC bindings to a native UI. Beyond startup and performance, the important bit is the agent mode: composing coherent screenshots (including popups) and routing agent-generated events in a sandboxed way.

That’s a serious engineering claim: **agentic interaction changes the requirements of UI plumbing.**

If your product is going to be driven by a model, you have to design the sensory and action interfaces explicitly:

- What is the model “seeing” (screenshots, DOM, accessibility tree)?
- How do we ensure it sees a coherent state?
- What actions can it take, and through what pathways?
- How do we isolate sessions and storage so mistakes don’t persist?

We’re used to thinking of the browser as a user tool. In an agentic world, the browser becomes an execution substrate: a controlled reality where a model can act.

## 6) Autonomy increases the value—and the danger

The “Clawdbot and Moltbook” piece plays the skeptic: today’s highly autonomous assistants are still unreliable, and giving unreliable systems broad tool access is a security and safety nightmare. Prompt injection, social engineering, exfiltration, “YOLO mode” misfires—these aren’t edge cases. They’re the first-order risk.

This skepticism is healthy. It also aligns with the way OpenAI’s skill documentation hints at risk: powerful procedures plus network access needs allowlists and careful data separation.

The synthesis here isn’t “don’t build agents.” It’s:

- Build agents **inside constraints**.
- Make risky pathways explicit and gated.
- Treat the internet as hostile input.
- Prefer workflows where the agent produces *proposals* (plans, diffs, reports) and humans or automated checks decide what merges.

Autonomy is not a binary. It’s a dial—and you should be able to turn it up and down per task.

## 7) The macro constraint: compute is the bill you can’t hand-wave

It’s easy to read all of this as a pure tooling shift. But the Journal du Net piece is a reminder that agentic systems are also a capital story: enormous capex on datacenters and GPUs, with uncertain payback timing.

If the industry is betting hundreds of billions on compute, you can expect two things:

1) Teams will continue to push for workflows that turn compute into business outcomes (agentic automation, deep research, copilots that do real work).
2) There will be pressure to make those workflows efficient and controllable—because the bill arrives regardless of the demo.

The “Something big is happening” essay captures the emotional side of this: a power user’s sense that we crossed a threshold, and that the public perception lags behind frontier capabilities.

You can disagree with timelines and rhetoric. But the underlying dynamic is hard to ignore: more capability → more usage → more spend → more incentive to productize and standardize.

## 8) A surprising metaphor: digitizing smell shows what “making the world legible” looks like

“Scent, In Silico” feels like it belongs to a different newsletter—until you notice the rhyme.

Smell is messy: subjective, high-dimensional, poorly captured by language. The breakthrough described isn’t a new perfume. It’s a representation—the Principal Odor Map—where molecules are embedded into a continuous space where proximity corresponds to perceptual similarity.

That is the same pattern we’re seeing in software engineering:

- Take a chaotic domain (a codebase, a UI, a research question, a distributed system).
- Build a representation and an interface that makes the domain navigable.
- Add verification loops so outputs are checkable.

Agents don’t just need intelligence. They need *maps*. The map is what lets them operate without hallucinating a world that isn’t there.

## Where this leaves us: agentic engineering as constraint design

Simon Willison’s note about GLM‑5 is mostly a signal flare: open weights are arriving at absurd scale, and the term “agentic engineering” is becoming a banner for the emerging craft.

Here’s my take on what the craft actually is:

1) **Design procedures** (skills) that turn recurring work into playbooks.
2) **Make knowledge durable** (repo docs, plans, transcripts).
3) **Engineer for verification** (tests, invariants, typed constraints, explicit nondeterminism).
4) **Invest in observability and rollback** (checkpoints, rewind, small diffs).
5) **Control autonomy** (gated actions, safe browsing substrates, hostile-input assumptions).

If we get this right, the near-term result won’t be “the end of engineers.” It will be more software, built faster, with humans spending more time on judgment and less on keystrokes.

If we get it wrong, we’ll ship increasingly complex systems whose creators can’t explain them, can’t audit their provenance, and can’t contain their failure modes.

The punchline is not that engineers become sorcerers.

It’s that engineering becomes a kind of **civic planning for code**: you don’t control every car, but you design roads, traffic lights, zoning, and inspections so the city doesn’t collapse under its own motion.

In an agent-first world, your agents will drive.

Your job is to build the city.

---

## Sources
1. [How Claude Code Is Transforming Finance—Without Turning You Into a Coder](https://every.to/p/how-claude-code-is-transforming-finance-without-turning-you-into-a-coder)
2. [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
3. [Skills in OpenAI API](https://developers.openai.com/cookbook/examples/skills_in_api/)
4. [Aletheia: a math research agent (Superhuman Reasoning)](https://github.com/google-deepmind/superhuman/blob/main/aletheia/Aletheia.pdf)
5. [Clawdbot and Moltbook are a False Alarm – For Now](https://secondthoughts.ai/p/clawdbot-and-moltbook)
6. [Scent, In Silico](https://press.asimov.com/articles/scent)
7. [Coding Agents Meet Distributed Reality](https://jhellerstein.github.io/blog/codegen-reality/)
8. [How I Use Claude Code](https://boristane.com/blog/how-i-use-claude-code/)
9. [Something Big Is Happening](https://shumer.dev/something-big-is-happening)
10. [Intelligence artificielle : la face sombre des folles dépenses des big tech](https://www.journaldunet.com/intelligence-artificielle/1547929-intelligence-artificielle-la-face-sombre-des-folles-depenses-des-big-tech/)
11. [Entire CLI: capture AI agent sessions on every push](https://github.com/entireio/cli)
12. [“Engineers are becoming sorcerers” | The future of software development with OpenAI’s Sherwin Wu](https://www.lennysnewsletter.com/p/engineers-are-becoming-sorcerers?post_id=186818429)
13. [The Architecture Behind Atlas: OpenAI’s New ChatGPT-based Browser](https://blog.bytebytego.com/p/the-architecture-behind-atlas-openais)
14. [GLM-5: From Vibe Coding to Agentic Engineering](https://simonwillison.net/2026/Feb/11/glm-5/)
15. [OpenAI works on ChatGPT Skills, upgrades Deep Research](https://www.testingcatalog.com/openai-works-on-chatgpt-skills-upgrades-deep-research/)
