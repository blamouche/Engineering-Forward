# Building Software Is Learning
**Source**: https://registerspill.thorstenball.com/p/building-software-is-learning
**Date**: 2026-06-02
**Author**: Thorsten Ball (Register Spill)
**Keywords**: software development, learning, feedback, prototyping, iteration, shipping, Amp, engineering culture

## Elevator pitch
When building new software, you don't yet know what you're building—you learn what it is as you build it—so the question is not "how do I build this?" but "how do I get feedback as fast as possible so I can learn?"

## Takeaways
- Building new software is learning: if you're building something new and don't fully know how it should work, you will learn what you're building as you do it
- The key question is not "how do I build this?" but "how can I get feedback as soon as possible, so I can learn?"
- Ship small pieces every day so that every day what you built hits reality and you get to learn from the response
- Write the example code that would go into the README before building the SDK—if people dislike the API in the readme, they don't need the SDK
- Prototypes, asking questions, explaining the idea, and cutting things are all forms of learning that should happen before and during building, not after

## Synthesis
Thorsten Ball's internal note to the Amp team, published as "Building Software Is Learning," captures a deceptively simple insight that reshapes how engineering teams should think about shipping. The core argument: when you're building something genuinely new, you don't yet fully know what it is you're building. You learn what it is as you build it. This means the traditional approach—specify, design, build, ship, learn—is backwards for new software. The learning happens during building, not before it.

The essay reframes the engineering question. Instead of asking "how do I build this correctly?", the question becomes "how can I get feedback as soon as possible, so I can learn?" This shift has practical consequences for how you chop up work and ship it. If learning is the goal, then shipping one small piece every day is better than shipping a large piece every two weeks, because every day what you built hits reality and you get to learn. On day 2, someone says "you know what, we should change..." and that feedback is the learning.

Ball offers concrete tactics. Write the example code that would go into the README and show it around—does that look like a good API? People don't need an SDK built if they dislike the API in the readme. Build prototypes. Ask more questions. Figure out what to cut out. Try to explain the idea to someone. All of these are forms of learning that should happen before and during the build, not after.

The essay pairs naturally with Ball's earlier work on ownership: ownership means taking a problem from "we have a problem" to "we don't have to think about it again," but the path to that resolution is through learning, not through getting it right the first time. The framework is a mental shift from "building as execution" to "building as discovery."