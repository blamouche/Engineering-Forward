# GitHub - amazon-science/expert

**Source**: https://github.com/amazon-science/expert-upcycling
**Date**: April 24, 2026
**Author**: amazon-science
**Keywords**: github, amazon, science, expert

## Elevator pitch
Contribute to amazon-science/expert-upcycling development by creating an account on GitHub

## Takeaways
- This repository was archived by the owner on Apr 23, 2026.
- amazon-science / expert-upcycling Public archive Notifications You must be signed in to change notification settings Fork 0 Star 4 main Branches Tags Go to file Code Open more actions menu Folders and files Name Name Last commit message Last commit date Latest commit History 3 Commits 3 Commits assets assets configs configs expert_upcycling expert_upcycling scripts scripts tests tests .gitignore .gitignore CODE_OF_CONDUCT.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTING.md LICENSE LICENSE NOTICE NOTICE README.md README.md pyproject.toml pyproject.toml View all files Repository files navigation Expert Upcycling Capacity expansion for Mixture-of-Experts models during continued pre-training.
- Dwivedi et al., "Expert Upcycling: Shifting the Compute-Efficient Frontier of Mixture-of-Experts" (preprint).
- Scaling laws show that MoE quality improves predictably with total expert count at fixed active computation, but training large MoEs from scratch is expensive — memory, gradients, and all-to-all communication all scale with total parameters.
- Expert upcycling sidesteps this by starting training with a smaller E-expert model and expanding to mE experts mid-training via the upcycling operator: Expert replication — each expert is duplicated (high-utility experts receive more copies via gradient-based importance scores).

## Synthesis
This repository was archived by the owner on Apr 23, 2026. amazon-science / expert-upcycling Public archive Notifications You must be signed in to change notification settings Fork 0 Star 4 main Branches Tags Go to file Code Open more actions menu Folders and files Name Name Last commit message Last commit date Latest commit History 3 Commits 3 Commits assets assets configs configs expert_upcycling expert_upcycling scripts scripts tests tests .gitignore .gitignore CODE_OF_CONDUCT.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTING.md LICENSE LICENSE NOTICE NOTICE README.md README.md pyproject.toml pyproject.toml View all files Repository files navigation Expert Upcycling Capacity expansion for Mixture-of-Experts models during continued pre-training. Dwivedi et al., "Expert Upcycling: Shifting the Compute-Efficient Frontier of Mixture-of-Experts" (preprint). Scaling laws show that MoE quality improves predictably with total expert count at fixed active computation, but training large MoEs from scratch is expensive — memory, gradients, and all-to-all communication all scale with total parameters. Expert upcycling sidesteps this by starting training with a smaller E-expert model and expanding to mE experts mid-training via the upcycling operator: Expert replication — each expert is duplicated (high-utility experts receive more copies via gradient-based importance scores). Router extension — router weights are copied to new slots with small bias perturbations to seed routing diversity. Continued pre-training (CPT) — stochastic gradient diversity and loss-free load balancing break symmetry among duplicates, driving specialization. Top-K routing is held fixed throughout, so per-token inference cost is unchanged. Figure 1: Overview of the expert upcycling procedure. Key results on a 7B→13B total parameter (1B active) interleaved MoE, pre-trained on 380B tokens: The upcycled model (32→64 experts) matches the fixed-size 64-expert baseline across 11 downstream benchmarks (56.4 vs.
