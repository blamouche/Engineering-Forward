# A Functional Taxonomy of World Models
**Source**: https://www.a16z.news/p/a-functional-taxonomy-of-world-models
**Date**: 2026-06-03
**Author**: Fei-Fei Li (World Labs)
**Keywords**: world-models, spatial-intelligence, robotics, reinforcement-learning, pomdp, renderers, simulators, planners, ai-taxonomy

## Elevator pitch
Fei-Fei Li and the World Labs team publish a taxonomy that cuts through the overloaded term "world model" by identifying three functional components — renderers, simulators, and planners — connected by the classic agent loop from reinforcement learning, providing precision to a concept claimed by computer vision, robotics, RL, and generative AI alike.

## Takeaways
- "World model" is one of the most important and most overloaded terms in AI, with computer vision, robotics, reinforcement learning, and generative AI each claiming to build world models but meaning fundamentally different things
- The taxonomy identifies three functional components: renderers (produce observations), simulators (predict how state changes), and planners (decide actions), connected by the POMDP agent loop
- Language models learn the statistical structure of text; world models learn the statistical structure of space and time — how light falls on surfaces, how objects respond to force, how physics governs motion
- The classic POMDP (partially observable Markov decision process) framework from RL textbooks provides the loop beneath the taxonomy: agents take actions, actions affect world state, agents receive observations, observations inform new actions
- A video model producing physically impossible flames, a language model improvising a game, and a physics engine faithfully simulating combustion all go by the name "world model" — the taxonomy distinguishes them
- The framework aims to bring precision at exactly the moment the field needs it, as investment in spatial intelligence and world models accelerates

## Synthesis
Fei-Fei Li and the World Labs team published "A Functional Taxonomy of World Models" on June 3, 2026, going a level deeper than their earlier essay on spatial intelligence as AI's next frontier. The piece addresses a fundamental terminological problem: "world model" has become one of the most important and most overloaded terms in AI, with fields as diverse as computer vision, robotics, reinforcement learning, and generative AI all claiming to build world models while meaning fundamentally different things.

The opening premise is that the world is not made of words. Language models have given machines extraordinary command of concepts, vocabulary, and reasoning, but the physical world — virtual or real — runs on a different substrate of space and time. Where language models learn the statistical structure of text, world models learn the statistical structure of space and time: how light falls on a surface, how a garden looks from an angle no camera has captured, how objects respond to force and follow the laws of physics.

The taxonomy cuts through this confusion by starting with a diagram older than the technology in question. Reinforcement learning textbooks, including the canonical Sutton and Barto, have used a version of the same picture for decades: the partially observable Markov decision process (POMDP). In this framework, an agent (person, robot, or software system) takes actions that affect the state of the world. The agent never sees the state directly — what reaches it are observations: photons on a retina, readings from sensors, pixels in a video frame. New observations inform new actions, and the loop continues.

Within this loop, the taxonomy identifies three functional components. Renderers produce observations — the visible output of a world state, like a graphics engine rendering a scene. Simulators predict how state changes — modeling the dynamics of the world as actions are taken, like a physics engine computing the trajectory of objects. Planners decide actions — using the simulated futures to choose what to do next, like an RL policy selecting the action that maximizes expected reward. These components are not independent layers but parts of a connected loop.

The practical value of this taxonomy is in distinguishing things that are currently conflated. A video model that produces gorgeous but physically impossible flames is a renderer without a simulator. A language model improvising a playable game is a simulator without a renderer. A physics engine faithfully simulating combustion is a simulator without a planner. Only when all three components are present and connected in the loop does a system qualify as a complete world model in the POMDP sense. This precision matters because the field is investing heavily in spatial intelligence, and understanding which functional pieces are being built determines whether the resulting system can actually support agentic behavior in physical or virtual worlds.