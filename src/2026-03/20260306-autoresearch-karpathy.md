# autoresearch: AI agents running research on single-GPU nanochat training automatically
**Source**: https://github.com/karpathy/autoresearch
**Date**: 2026-03-06
**Author**: Andrej Karpathy
**Keywords**: AI agents, autonomous research, LLM training, neural networks, single-GPU, optimization

## Elevator pitch
An experimental framework enabling AI agents to autonomously conduct machine learning research by iteratively modifying training code, executing 5-minute experiments, and progressively optimizing model performance without human intervention.

## Takeaways
- Agent-Driven Iteration: Rather than humans manually tweaking code, AI agents autonomously modify `train.py`, run experiments within a fixed time budget, and accept or reject changes based on validation metrics.
- Standardized Evaluation: All experiments use validation bits-per-byte (val_bpb) as the metric, enabling fair comparison across different architectural changes and hyperparameter configurations.
- Human-Configurable Direction: Researchers guide agent behavior through `program.md`, a Markdown instruction file that serves as the "research org code" defining experiment strategy.
- Constrained Simplicity: The framework deliberately limits scope to one GPU, one editable file, and one metric, prioritizing clarity and comparative fairness over distributed complexity.
- Platform Adaptability: While optimized for NVIDIA GPUs, the design principles support adaptation to smaller compute platforms through configurable hyperparameters.

## Synthesis
The autoresearch project reimagines research methodology by positioning AI agents as autonomous experimenters. Rather than framing this as replacing human researchers, Karpathy presents it as automating the iterative hypothesis-testing cycle that currently consumes significant research time.

The core innovation is the five-minute training budget, which creates a consistent experimental unit. This constraint ensures researchers can generate ~100 experiments overnight and fairly compare results regardless of architectural modifications. Unlike traditional research where different model sizes or batch configurations produce incomparable results, this framework normalizes the computational budget.

The three-file structure reflects deliberate constraint philosophy. `prepare.py` remains untouched, establishing unchanging baselines. `train.py` becomes the experimental sandbox where agents modify everything from model architecture to optimizer selection. `program.md` functions as meta-instructions, allowing humans to steer research direction without touching implementation details. This separation enables interpretable agent behavior—any improvement comes from modifications to a single, reviewable file.

Using bits-per-byte rather than loss values addresses a fundamental comparison problem in machine learning. When agents alter vocabulary size or other architectural components, standard loss metrics become incomparable. Bits-per-byte normalizes across these variations, creating objective progress measurement.

The framework acknowledges hardware heterogeneity through documented hyperparameter guidance for smaller platforms. Rather than forcing all users onto identical hardware, the design suggests adjusting DEPTH, MAX_SEQ_LEN, and TOTAL_BATCH_SIZE based on available compute—keeping the methodology sound while accommodating resource constraints.

The `program.md` file represents an interesting abstraction—encoding research methodology as interpretable instructions rather than hardcoded algorithms. This suggests the possibility of optimizing not just models, but the research process itself through agent iteration.

The project deliberately maintains minimalism despite obvious extensions (distributed training, multiple agents, complex logging). This constraint serves pedagogical purposes while making the system sufficiently focused that AI agents can meaningfully explore the possibility space. For the ML research community, autoresearch represents a compelling vision: treating the iterative experiment loop as an engineering problem solvable through careful system design, rather than an irreducibly human intellectual activity.
