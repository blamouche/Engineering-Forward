# Reinforcement Learning Course Materials — Paderborn University / University of Siegen
**Source**: https://github.com/upb-lea/reinforcement_learning_course_materials
**Date**: Unknown (ongoing, repository active)
**Author**: upb-lea (Paderborn University / University of Siegen)
**Keywords**: reinforcement-learning, open-education, course-materials, lecture-notes, python, pytorch, gymnasium

## Elevator pitch
A complete, open-source reinforcement learning course with lecture slides, video recordings, Python tutorial exercises, and solutions, covering everything from Markov decision processes to PPO, freely available under Creative Commons.

## Takeaways
- Full semester course: 14+ lecture topics from MDP fundamentals through dynamic programming, Monte Carlo, TD-learning, policy gradients, to TRPO/PPO, each with slides and YouTube video
- 12 tutorial exercises with templates and solutions, progressing from Python basics through solving classic RL problems (CartPole, Mountain Car, Lunar Lander) with increasingly sophisticated algorithms
- Licensed under Creative Commons Attribution 4.0 — freely usable for self-study or by lecturers to set up their own courses
- Based on Sutton & Barto's canonical textbook and David Silver's UCL course, with practical exercises using Gymnasium (maintained fork of OpenAI Gym)
- Originally hosted at Paderborn University, transferred to University of Siegen; actively maintained with open issues for community contributions

## Synthesis
This repository is one of the most comprehensive open educational resources for reinforcement learning available today. It's not just a collection of slides — it's a full-fledged university course, complete with recorded lectures, Jupyter notebook exercises with solutions, and a clear pedagogical arc that mirrors the structure of Sutton & Barto's seminal textbook.

The course is organized into two major parts: Part 1 covers RL in finite state and action spaces (tabular methods, dynamic programming, Monte Carlo, TD-learning, multi-step bootstrapping, planning with Dyna), while Part 2 moves to continuous spaces with function approximation, value-based control, policy gradients, deterministic policy gradients, and modern algorithms like TRPO and PPO. Each topic has lecture slides, a YouTube video, and a corresponding tutorial exercise.

The exercises are particularly well-designed for practical learning. They use Gymnasium environments and guide students from basic Python setup through increasingly complex problems: solving Markov chains by hand, implementing dynamic programming for a "beer-bachelor" problem, racing with Monte Carlo learning, driving with TD-learning, stabilizing an inverted pendulum with multi-step methods and Dyna, predicting electric drive behavior with supervised learning, mastering Mountain Car with function approximation and LSPI, and landing on the moon with REINFORCE, actor-critic, DDPG, and PPO.

What makes this resource stand out is its commitment to openness. Everything — slides, code, videos — is freely accessible and CC-BY licensed. The maintainers actively encourage contributions through GitHub issues and pull requests, and the materials are published on Zenodo with a DOI for academic citation. For anyone teaching or self-studying reinforcement learning, this is essentially a free, production-quality alternative to expensive online courses, built by domain experts at a research university.
