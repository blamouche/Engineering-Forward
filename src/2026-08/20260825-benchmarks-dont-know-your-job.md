# Benchmarks Don't Know Your Job
**Source**: https://every.to/context-window/benchmarks-don-t-know-your-job
**Date**: 2026-08-25
**Author**: Katie Parrott
**Keywords**: AI evaluation, benchmarks, KateBench, offline evals, model selection, internal evals

## Elevator pitch
Companies spending $100M a year on AI models often have no idea whether those models save employees time or produce trustworthy work, because public benchmarks measure general capability, not performance on the specific tasks a company needs—the gap requires building internal evals from real work.

## Takeaways
- Companies spending $100M/year on AI know what they pay and where models sit on leaderboards, but often don't know whether the models save employees time or produce work people trust without rechecking
- Public benchmarks can tell you one model is generally more capable than another, but can't tell you whether it caught the clause your lawyers care about, preserved your house style, or spared an employee another round of checking
- Every built KateBench: an AI copyeditor trained on ~30,000 edits by editor-in-chief Kate Lee, which suggests changes in Google Docs and tracks acceptance rates—but its 85-90% acceptance rate hides measurement problems: a 40-suggestion cap, non-deterministic output, and residual work editors still do after the tool completes
- The practical recommendation: choose one recurring job, write down five ways the current model gets it wrong with one gold-standard example each, and run models against those cases—that is the beginning of an eval, and it tells you more than another afternoon comparing leaderboards
- A six-agent solar crew built with Grok Bot connected a Raspberry Pi to an off-grid solar system, monitoring pack voltage and forecasting energy production to answer one question: is there enough power to run the dryer?

## Synthesis
AI has a measurement problem. Companies know how much they spend on models and how those models score on public benchmarks. What they often don't know is whether the models save employees time or produce work people can trust without rechecking. Mercor CEO Brendan Foody says he meets executives at companies in exactly this position: spending as much as $100 million a year running models without "offline evals"—a fixed set of real tasks used to test and compare models before they touch live work. Box CEO Aaron Levie echoed the point: "Enterprises will not be able to go just on vibes."

Public benchmarks can tell you one model is generally more capable than another. They can't tell you whether it caught the clause your lawyers care about, preserved your house style, or spared an employee another round of checking. A useful eval starts with the work your company already does: representative cases, failures employees know to look for, and a count of what humans still have to fix.

Every built KateBench to test this internally—an AI copyeditor trained on roughly 30,000 of editor-in-chief Kate Lee's past edits. It suggests changes in a Google Doc, then tracks which ones editors accept or reject. Across recent runs, editors accepted about 85 to 90 percent of its suggestions. But engineer Jannik Jung showed two reasons to distrust that number. The tool stopped after filing 40 suggestions, so on long essays it could find a good edit and throw it away before the editor saw it. The cap is now 80. KateBench also doesn't produce exactly the same edits every time, so its acceptance rate can rise or fall even when nothing has changed—meaning a new prompt might score higher once without being consistently better.

The practical prescription is concrete: choose one recurring job, like compiling a weekly report or producing a slide deck. Write down five ways the current model gets it wrong, with one example of each, and a gold-standard version. Run the models you are considering against those cases. That is the beginning of an eval, and it will tell you more about what to buy than another afternoon spent comparing leaderboards. The article also notes that diminishing returns on intelligence may be real for many tasks, but companies building evals that capture residual work—the work a human still has to do after the agent completes its task—may find that progress hasn't slowed, only that the measurements were missing it.