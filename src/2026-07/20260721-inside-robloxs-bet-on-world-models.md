# Inside Roblox's Bet on World Models
**Source**: https://blog.bytebytego.com/p/inside-robloxs-bet-on-world-models
**Date**: 2026-07-21
**Author**: ByteByteGo (Anupam Singh, SVP Engineering at Roblox)
**Keywords**: world models, Roblox, game engine, hybrid architecture, photorealism, edge computing, real-time systems

## Elevator pitch
Roblox is combining a deterministic game engine with a video world model (Super Upsampler) to deliver photorealistic multiplayer games at scale — a hybrid architecture where each technology handles what it's best at.

## Takeaways
- A pure video world model lacks persistent state, consistent rules, and reliable input handling — it generates beautiful frames but cannot run a game, since turning the camera away and back may produce a different world
- A pure game engine struggles with photorealism — achieving realistic rendering requires enormous compute and artistic resources that are out of reach for small creators
- Roblox's hybrid splits work: the game engine (data model, physics, rules) keeps the world consistent and fair; the Super Upsampler generates photorealistic visuals from low-res rendered frames, running on edge GPUs
- The four open problems are latency, consistency, multiplayer, and creator control — Roblox addresses latency via self-forcing (model generates its own training data), consistency via multi-scale supervision, multiplayer via the engine as single source of truth
- Roblox owns its compute infrastructure (24+ edge data centers, own GPUs) and plans for sudden capacity surges via weekly "Taco Tuesday" resilience testing

## Synthesis
Roblox's approach to photorealistic gaming is a pragmatic engineering compromise between two technologies that each solve only half the problem. Video world models can generate stunning visuals but lack the deterministic systems — persistent state, consistent rules, real-time physics synchronization — that make a game playable. Game engines provide those systems but require enormous artistic and computational investment to achieve photorealism, putting it out of reach for most creators.

The solution, called Roblox Reality, has three components: the game engine maintains a structured data model of every object and its properties, running simulation and physics with exact repeatability; the Roblox Cloud handles coordination; and the Super Upsampler takes the engine's low-resolution rendered frames and generates photorealistic output. This means a creator doesn't need a powerful machine — the heavy rendering happens on shared edge GPUs, and visual quality becomes independent of the creator's budget or the player's device.

The engineering challenges are significant. For latency, the team uses a technique called self-forcing, where the model generates its own training data during inference to maintain temporal coherence, combined with a "game cartridge" harness from the Lucid AI acquisition that bridges deterministic game logic with the video model. For consistency across frames, they use multi-scale supervision so local and global features remain coherent. For multiplayer, the engine remains the single source of truth — the world model only paints what the engine says exists, so all players see the same consistent world.

The piece also highlights Roblox's operational advantages: 20 years of building the data model, ownership of compute infrastructure, and a culture where executives share on-call rotations with engineers. The company runs weekly capacity-reduction exercises ("Taco Tuesday") to find system limits before users do. The initial quality target is 2K at 60fps, with 4K as a longer-term goal. If successful, this architecture could let a two-person studio build something as visually rich as a large studio's work, fundamentally changing who can create photorealistic experiences.