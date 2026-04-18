# Vibe Check: Opus 4.7 Stopped Reading Between the Lines

**Source**: https://every.to/vibe-check/opus-4-7
**Date**: April 17, 2026
**Author**: Katie Parrott
**Keywords**: every, vibe, check, opus, stopped, reading, between, lines

## Elevator pitch
Anthropic's latest Opus is more precise, more literal, and the best coding model we've tested on well-specified tasks—but it won't fill in the gaps for you anymore.

## Takeaways
- Anthropic’s latest Opus 4.7 model, released yesterday, is a sharper tool than its predecessor—but it also needs a sharper operator.
- It delivered the best results we’ve seen on our LFG coding benchmark, but it hedges or stalls when you don’t tell it exactly what you want.
- Every didn’t get advance access for this release, so we have been testing it for the last day on our most important use cases.
- The variable across our testing was specificity.
- With a detailed brief, 4.7 cleared our hardest coding benchmark and produced consulting prose that one of our testers called “better than reading my own.” With less direction, it waits for clearer instructions or guesses wrong.

## Synthesis
Anthropic’s latest Opus 4.7 model, released yesterday, is a sharper tool than its predecessor—but it also needs a sharper operator. It delivered the best results we’ve seen on our LFG coding benchmark, but it hedges or stalls when you don’t tell it exactly what you want. Every didn’t get advance access for this release, so we have been testing it for the last day on our most important use cases. The variable across our testing was specificity. With a detailed brief, 4.7 cleared our hardest coding benchmark and produced consulting prose that one of our testers called “better than reading my own.” With less direction, it waits for clearer instructions or guesses wrong. Anthropic researcher Alex Albert , who joined us on our testing livestream , confirmed that 4.6 had been doing a meaningful amount of prompt engineering on your behalf that 4.7 doesn’t, which means the burden is on the user to specify exactly what they want. The new model is listening for explicit permission now that its predecessor took for granted. So the prompts you’ve tuned on 4.6 for the last two months are likely to give you disappointing results at first. Alex walked us through the pattern Anthropic has taken with its models over the past year: Sonnet 3.7 (released in March 2025) was too eager, Opus 4 (May 2025) got dialed back, Opus 4.6 (February 2026) was doing too much, and now Opus 4.7 has been reined in again. That’s four re-tunings in about a year, and Alex told us it’s deliberate—a “perpetual back-and-forth,” as he called it.
