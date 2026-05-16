# Reinforcement Learning Course Materials
**Source**: https://github.com/upb-lea/reinforcement_learning_course_materials
**Date**: May 16, 2026
**Author**: University of Paderborn / University of Siegen (LEA group)
**Keywords**: reinforcement learning, open education, lecture notes, MDP, policy gradient, deep RL, course materials

## Elevator pitch
A comprehensive open-source reinforcement learning course with lecture notes, tutorial tasks with solutions, and online videos, covering everything from Markov decision processes to contemporary algorithms like PPO and TRPO.

## Takeaways
- Complete university-level RL curriculum: 14+ lecture modules with slides in PDF format and accompanying YouTube video lectures.
- Covers the full RL spectrum: from fundamentals (MDPs, dynamic programming, Monte Carlo, TD-learning) to modern deep RL (policy gradients, DDPG, TRPO, PPO).
- Practical Python exercises built on Python 3.12 with templates and full solutions provided for self-learners and instructors.
- Licensed under Creative Commons Attribution 4.0, enabling both self-study and course setup by other lecturers.
- Originally from Paderborn University, now maintained at University of Siegen with active CI/CD for PDF builds.

## Synthesis
This repository represents one of the most complete open educational resources for reinforcement learning available today. Originally developed at Paderborn University and now maintained by the University of Siegen's LEA (Learning and Embedded Automation) group, it provides a full semester's worth of RL curriculum under a Creative Commons license.

The course follows a logical progression that mirrors the historical development of RL. It begins with foundational concepts — introduction to RL, Markov decision processes, and dynamic programming — before advancing through model-free methods (Monte Carlo and temporal-difference learning). The curriculum then bridges to modern deep RL with function approximation, value-based control, and policy gradient methods. The final modules cover contemporary algorithms like Trust Region Policy Optimization (TRPO) and Proximal Policy Optimization (PPO), ending with research outlooks.

Each lecture module includes a pre-rendered PDF slide deck (hosted via GitHub Pages) and a YouTube video lecture, making the material accessible for both self-study and formal education. The exercise component is equally thorough: Python-based tutorials with Jupyter-style templates provide hands-on practice with scientific Python for RL, and complete solutions are provided for each exercise.

The technical infrastructure is well-organized with automated PDF builds via GitHub Actions, a Zenodo DOI for citation, and clear requirements management via pip. The course has clear institutional backing — the LEA group at the University of Siegen maintains and continues to update the materials.

What makes this resource particularly valuable is its dual-use design. Self-learners can work through lectures and exercises independently, while lecturers can fork and adapt the entire curriculum for their own courses. The open license removes barriers to both uses.

The course fills an important gap in AI education. While there are excellent RL textbooks (Sutton & Barto) and online courses (David Silver's), this repository uniquely combines structured lecture slides, video content, and graded Python exercises in a single, version-controlled package that can be integrated into university curricula or self-study paths with minimal friction.
