# Your AI Might be Lying to Your Boss
**Source**: https://williamoconnell.me/blog/post/ai-ide
**Date**: 2026-04-25
**Author**: Unknown
**Keywords**: ai, might, lying, boss

## Elevator pitch
This post is my personal opinion based on my testing and observations.

## Takeaways
- This post is my personal opinion based on my testing and observations.
- How much of your code is AI?
- I donât make heavy use any of these in my personal life, but I have gotten to try a handful of them through various…
- One thing thatâs very important to any enterprise rolling out a tool like this is metrics:
- Is this technology being used to paper over inefficiencies in our existing processes, obscuring underlying issues because using AI to quickly produce documents that…

## Synthesis
This post is my personal opinion based on my testing and observations. I'm pretty confident in my test methodology, but William O'Connell is human and can make mistakes, check important info, etc.

How much of your code is AI? That question would've been gibberish to me five years ago, but of course the last few years have seen an explosion of "AI-enhanced" IDEs and other software development tools. Software companies are spending huge sums of money to provide these tools to their staff, and rapidly cycling through them as the space continues to evolve.

I donât make heavy use any of these in my personal life, but I have gotten to try a handful of them through various employers. One such tool is Windsurf, a VSCode fork that most people know as the one they assume shut down after Google bought out their key leadership last year. It didn't though, at least not yet, and Iâd imagine its FedRAMP and HIPAA certifications will continue to make it appealing to certain types of enterprise customers for the foreseeable future. If youâve seen Cursor or GitHub Copilot, itâs basically the same, with some AI-powered autocomplete features and an "agent" chatbox called Cascade where you can ask your favorite LLM why a bug is happening, or get it to draft a class or function for you. In theory these types of agents can develop features and even whole applications on their own, but in my experience the results are pretty inconsistent, so I tend to stick to simpler requests.

One thing thatâs very important to any enterprise rolling out a tool like this is metrics:

Is this technology being used to paper over inefficiencies in our existing processes, obscuring underlying issues because using AI to quickly produce documents that wonât be read and code that wonât be run is easier than asking why those things are being done in the first place?

Admittedly I havenât heard that last one much, but the first two definitely get asked a lot. To help with this, Windsurf offers a dashboard of analytics at both the individual and team level. It includes things like the number of autocomplete suggestions accepted, the number of messages sent to Cascade, and which models are being used the most. It also includes a metric called "% new code written by Windsurf" (or sometimes "PCW"), which they seem quite proud of, since it gets top billing on the dashboard and they wrote a whole blog post explaining it.

The pitch is pretty simple: how much of the code did a developer write by hand, and how much did they generate with AI? When I first learned about this feature my guess would have been 10, maybe 20% AI, depending on the project and whether you include unit tests (LLMs are pretty good at those). So you can imagine my surprise when I opened the dashboard and saw this:

Now, itâs certainly possible to misjudge how often you use a particular tool. If the number had been 40%, or even 50%, I wouldnât have been that shocked. But 98%? That would mean Iâm generating forty-nine times as much code as Iâm writing manually. If that were true wouldnât I have run through my token budget by now? Shouldnât I either have been promoted for my godlike productivity, or fired because 49/50 of all developers are now redundant? Youâd think, but Windsurf says this result is pretty normal:
