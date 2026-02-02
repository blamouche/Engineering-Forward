# What's important now - When the Interface Left the App

*AI isn’t just writing code; it’s taking the customer relationship—and forcing every product to become an API.*

Claire Vo gave an autonomous agent full access to her computer for a day. Within hours it had done something both mundane and unsettling: it broke her family calendar. Not in a cinematic “AI goes rogue” way—more like the kind of quiet, plausible mistake that ruins a week. In the same experiment, the agent also joined her podcast workflow, drafted outreach emails, and produced better market research than most interns. The contrast is the point. We are entering a phase where systems can do real work inside our accounts, but they still don’t reliably understand the social and operational boundaries those accounts represent.

At the same moment, a different kind of boundary is dissolving: the one between “using software” and “talking to software.” Anthropic’s MCP Apps let major SaaS products render inside Claude. Users don’t open Asana or Figma; they ask, and a chat window becomes the surface area of the product. The interface—the thing software companies spent a decade polishing into muscle memory—starts to move somewhere else.

Put those together and a pattern emerges. AI is not merely a feature. It’s a new layer that sits between people and the tools they use. That layer is becoming the default interface, the default coordinator, and—if we’re not careful—the default owner of trust.

## From “writing” to “directing”

The fastest way to understand what’s happening is to watch how high-output builders are working right now. Peter Steinberger’s line—“I ship code I don’t read”—sounds irresponsible until you hear the rest of the method. The craft hasn’t disappeared; it has relocated.

In Steinberger’s workflow, implementation is delegated to agents, but direction is not. Planning expands. Architecture becomes the primary human responsibility. Verification becomes non-negotiable. He describes systems where agents operate in closed loops: they compile, lint, run, and prove their work against a concrete harness. That’s the difference between “AI helped me” and “AI shipped this.” The former is a writing assistant. The latter is a teammate—one that must be managed like a teammate.

This reframes code review. If agents produce the code, the most leverage often sits upstream: in the prompt, in the constraints, in the acceptance criteria. Steinberger treats pull requests as “prompt requests,” a phrase that will sound obvious a year from now. The review surface shifts from “did you format this correctly?” to “did we define the right behavior, and did we force the system to validate it?”

What makes this change durable is not novelty. It’s economics. When a developer can queue five or ten agent tasks in parallel, the opportunity cost of meticulous line-by-line review explodes. Teams either build strong verification loops—or they drown in plausible output.

## The interface stops being your moat

For most SaaS companies, the interface wasn’t just UX. It was the product. The UI bundled data, logic, and relationship into a single place where users developed habits and switching costs. Linas Beliunas’ argument about MCP Apps is stark: if an AI platform becomes the interface, the app becomes a backend.

That isn’t a metaphor. If Asana “renders” inside Claude, the user experiences Anthropic’s interaction model while Asana supplies the underlying data and actions. The user’s day is spent in one conversational shell that can move across tools instantly. In that world, the old moat—familiarity with a particular UI—erodes fast.

So why would incumbents participate? Because the alternative is worse: invisibility. In an agentic workflow, anything the agent can’t reach might as well not exist. If your product can’t be invoked, inspected, and operated by the layer where work now happens, you become a tab someone used to keep open.

The strategic consequence is uncomfortable. The customer relationship—the day-to-day interaction surface—shifts to whoever owns the assistant layer. SaaS vendors are pushed into competing on what remains when the UI is externalized: data quality, domain logic, integrations, reliability, and pricing. The winners may be the products that behave best as APIs, not the ones that look best on a dashboard.

If you’ve spent years investing in polish, onboarding, and workflows, “become an API” sounds like surrender. But it can also be liberation: less time building yet another interface for yet another niche, more time making the underlying capabilities sharp enough that any interface can use them.

## Always-on assistants need a body

If chat becomes the interface for knowledge work, the next question is where that interface lives. Demis Hassabis’ comments at Davos point toward the obvious physical answer: glasses. Google’s partnerships (including Warby Parker and Samsung) aim at prototypes in summer 2026, with a “universal digital assistant” as the killer application.

But glasses only work if the assistant works everywhere: in motion, in noisy environments, with low latency, and with enough privacy that people trust it around their lives. Hassabis flags trust as a product constraint, not an ethics sidebar. An ad-supported assistant has an intrinsic credibility problem: users need to believe the system is optimizing for them, not for whoever pays the most.

That trust problem rhymes with Claire Vo’s calendar mishap. When an agent acts under your identity, tiny errors are not “bugs.” They are reputational damage. A universal assistant can’t be merely capable; it must be legible, constrained, and predictable.

The technical direction that makes this plausible is happening in parallel: on-device LLMs are moving from demos to production. Meta’s research team describes how billion-parameter models now run on flagship phones, not because mobile chips suddenly became data-center GPUs, but because the stack adapted. Quantization (especially 4-bit), architectural choices for small models, and inference optimizations like speculative decoding shift the bottleneck from “can we run it?” to “what do we keep local, and what do we send to the cloud?”

On-device models change more than latency. They change the privacy posture and the unit economics. If the first pass of interpretation—what you asked, what you meant, what you’re looking at through a camera—can happen locally, the assistant can be fast, offline-tolerant, and less invasive. The cloud remains the place for deep reasoning and giant context. But the edge becomes the place where the assistant feels immediate and personal.

If you’re trying to build an assistant that people will wear on their face, “personal” is not a marketing adjective. It is the baseline.

## The boom, the timeline, and the missing pieces

Marc Andreessen offers the investor’s macro lens: AI is arriving at a moment of demographic decline and productivity stagnation, making it a tool economies will reach for out of necessity. His optimism is essentially an argument about absorption capacity. He expects AI to amplify workers rather than eliminate work wholesale, and he urges people to become non-fungible—building “E-shaped” careers that combine multiple skills and distinctive expertise.

That’s a useful counterweight to the more breathless “everything will be automated” narratives. But it’s also incomplete without the research reality Hassabis points to. Even if progress continues—DeepMind’s internal confidence suggests it will—AGI (in the scientific sense) is still blocked on hard problems: continual learning from experience, robust memory, and efficient context. Those aren’t UX tweaks. They are missing mechanisms.

This matters because the next few years won’t be a clean, linear transition from “tools” to “agents” to “AGI.” It will be messy. We’ll see systems that are shockingly competent at narrow operational workflows and embarrassingly unreliable at the kinds of human boundary judgments that make those workflows safe.

In that world, the practical question for teams is not “when will AGI arrive?” It’s “what can we safely delegate today?”

## Where teams should place their bets

The six pieces in this week’s corpus land on one shared conclusion: delegation is becoming the default mode—delegation of coding, delegation of UI, delegation of research, delegation of daily tasks. The winners won’t be the teams with the cleverest demos. They’ll be the teams that build disciplined interfaces between humans and machines.

That starts with verification. If you want to ship code you don’t read, you must make “closed loop” a core requirement: tests that actually assert behavior, linters that catch the footguns, and environments agents can run without endangering the rest of your system. The simplest version is a local harness; the mature version is an agent runtime with scoped permissions and observable actions.

It also requires product strategy changes. If the interface is migrating to assistants, your product must become callable. Your primitives need to be composable. You need to think like a platform even if you sell a “simple” app. And you need to decide which parts of the relationship you are willing to outsource to a third-party assistant layer—and which parts are existential to keep.

Finally, it demands a new stance on trust. We learned the wrong lesson from “move fast and break things.” When the thing that breaks is someone’s calendar, inbox, or identity, the blast radius is personal. The assistant layer will win on reliability, transparency, and incentives. Hassabis is right to flag advertising as a trust tax; Claire Vo’s story shows why users will notice that tax immediately.

The interface is leaving the app. That doesn’t mean software is dying. It means the center of gravity is shifting to the layers we used to treat as wrappers: the agent, the API, the execution loop, the device. If you build those layers well, the new interface becomes a distribution channel. If you don’t, it becomes a gatekeeper.

---

## Sources

1. [I Gave Clawdbot Full Access to My Computer. It Broke My Family Calendar and Joined My Podcast.](https://www.lennysnewsletter.com/p/today-on-how-i-ai-i-gave-clawdbot)
2. [The Creator of Clawd: "I Ship Code I Don't Read"](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)
3. [Google DeepMind CEO Demis Hassabis on AI's Next Breakthroughs, What Counts As AGI, And Google's AI Glasses Bet](https://www.bigtechnology.com/p/google-deepmind-ceo-demis-hassabis-946)
4. [AI Just Killed the User Interface](https://linas.substack.com/p/aikilledui)
5. [Marc Andreessen: The Real AI Boom Hasn't Even Started Yet](https://www.lennysnewsletter.com/p/marc-andreessen-the-real-ai-boom)
6. [On-Device LLMs: State of the Union, 2026](https://v-chandra.github.io/on-device-llms/)
