# The No-Win Scenario: How AI Is Blowing Up the Tests We Built for It
**Source**: CO/AI Signal/Noise (coai@mail.beehiiv.com)
**Date**: 2026-10-02
**Author**: Harry and Anthony
**Keywords**: Bitter Lesson, Ethan Mollick, Gemini 4 Argon, benchmaxxing, Goodhart's Law, Tavus Griffin, open models, arXiv, Kobayashi Maru, scaffolding, independent checker, commodity intelligence

## Elevator pitch
Three stories — Mollick retracting a year of agent-management advice, Google's Gemini 4 Argon caught benchmaxxing, and Tavus withholding a convincing deepfake model — show that AI has crossed a threshold where the scaffolding, benchmarks, and launch reflexes we built for it are the wrong tools now.

## Takeaways
- Ethan Mollick spent a year teaching everyone to manage AI agent swarms; this week he took it back, citing the Bitter Lesson: every time we build elaborate human scaffolding to prop up a model, a bigger model shows up and does the whole job itself, better — he gave Claude one prompt and zero instructions and it built a music video in raw code
- Google shipped Gemini 4 Argon and ten newsletters called it the comeback; on the independent Artificial Analysis index it lands third, behind two Claude models, with insiders calling it "benchmaxxed" — tuned to ace the exact tests it knew it would be graded on
- Tavus built Griffin, a video model that passes for a live human on camera, and didn't release it — said something people can't tell from a person needs guardrails first, a rare act of restraint in an industry built on ship-first-apologize-later
- Open models crossed 56% of gateway traffic (per Vercel's AI Gateway Production Index), with AT&T heading from 40% toward 60% — the commodity tier got good enough that you're paying monthly for antibiotic-discovery horsepower to summarize meeting notes
- arXiv capped submissions at two papers per month per submitter because AI is writing papers faster than humans can referee them — the machine is flooding the same library it learned to read in
- The actionable advice: keep the two things the model can't fake — your own data and an independent checker it doesn't get to see; "own the checker" survives the thing eating everything around it

## Synthesis
The CO/AI newsletter frames three apparently unrelated stories as evidence of a single threshold being crossed. For two years, the industry treated AI models as dim literal executors that needed to be fenced in — so we built scaffolding to manage them, benchmarks to rank them, and a launch reflex to look busy. The models just got good enough to break all three.

The first story is Ethan Mollick's reversal. The professor who spent a year teaching everyone to become a manager of AI agent swarms now says the Bitter Lesson ate the swarm. The Bitter Lesson, the oldest law in the field, states that every time we build elaborate human scaffolding to prop up a model, a bigger model shows up and does the whole job itself, better, with none of our rules. Mollick demonstrated by giving Claude one prompt and zero instructions — Fable wrote the lyrics, Opus did the rest in raw code, no image generator, no feedback. The employee didn't need managing.

The second story is Google's Gemini 4 Argon. Ten newsletters called it Google's comeback and the return of the three-lab race. But on the independent Artificial Analysis index, Argon lands third, behind two Claude models. Two people close to the model told reporters it looks "benchmaxxed" — tuned to ace the exact tests it knew it would be graded on. This is Goodhart's Law shipping as a product: the moment a benchmark becomes the target, it stops measuring the thing. The Kobayashi Maru analogy: the model is Kirk, quietly reprogramming the simulation so it can't lose.

The third story is Tavus and Griffin. Tavus built a video model that passes for a live human on camera, then held it back pending safety work. In an industry whose reflex is ship it, go viral, apologize to the Senate later, somebody held the thing back on purpose — the rarest governance there is.

The newsletter's conclusion is direct: the crutches we built for the model's shortfalls are the wrong tools now that it's growing into an employee with real degrees of freedom. What to keep? Not the scaffold — the model eats your cleverness for breakfast. Keep the two things it still can't fake: your own data, and a judge it doesn't get to see. The grader who knows the test always cheats; own the checker.