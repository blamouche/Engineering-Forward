# The Open/Closed Problem in AI
**Source**: https://blog.mempko.com/the-open-closed-problem-in-ai/
**Date**: May 23, 2026
**Author**: Maxim Khailo
**Keywords**: open-loop learning, closed-loop learning, AI hardware, ASICs, GPU, inference, training, ML systems, agent memory

## Elevator pitch
The AI industry is hardening its hardware and learning paradigms around open-loop systems—static models trained offline—which quietly forecloses the more promising path of closed-loop learning where models update themselves continuously, just as biological neurons do.

## Takeaways
- The GPU/ASIC evolution mirrors a historical pattern: CPU (open) → fixed-pipeline GPU (closed) → programmable GPU (open) → specialized ASICs (closed again), and each closing phase kills creative experimentation.
- Today's LLMs use open-loop learning: they are trained offline via backpropagation and then deployed frozen, relying on external memory hacks (agents writing to markdown files) to simulate learning.
- Biological brains use closed-loop learning: a single neuron both computes and physically rewrites itself based on prediction errors, with no external training process.
- Inference-optimized ASICs physically bake in the open-loop assumption—read-only weights, separate compute and memory—making closed-loop learning fundamentally impossible on current hardware.
- The window to experiment with closed-loop learning is closing with every specialized chip that ships; what's needed is a new substrate (like an advanced FPGA) built for models that rewrite themselves in place.

## Synthesis
Maxim Khailo, writing after attending the ninth MLSys conference in Seattle, diagnoses what he calls the "Open/Closed Problem" in AI—a dual phenomenon spanning both hardware architecture and learning paradigms. His central claim is uncomfortable: the efficiency work the field is celebrating is not neutral progress but hardware hardening around a paradigm that may be fundamentally wrong.

Khailo draws a historical parallel with 3D graphics. In the 1990s, CPUs allowed wild creativity in rendering—voxels, unconventional pipelines, varied aesthetics. Fixed-function GPUs accelerated polygon rendering but killed that diversity until programmable shaders restored flexibility. CUDA then emerged from that programmability, enabling the neural network revolution. Today's trajectory repeats the pattern: ASICs optimized purely for inference are closing the system again, physically encoding assumptions that foreclose alternative approaches.

The technical argument is precise. An inference ASIC assumes frozen weights, so parameter memory is built to be read, not rewritten. Compute and memory sit in separate places because that's efficient when the model never changes. Everything is optimized for large batched matrix multiplications—the signature of serving a static model. But a closed-loop learning system needs the opposite: weights that change constantly, fine-grained updates, and fused memory-compute so parameters can rewrite themselves in place. Every generation of specialization concretizes the open-loop assumption deeper into silicon.

The second dimension of the problem concerns learning itself. Current AI is open-loop: models are trained via an external process (data gathering, loss function, gradient descent), then deployed frozen. They don't learn from experience. The agent paradigm—LLMs using tool calls to update external markdown files or databases—is Khailo describes as an inefficient hack that simulates learning without achieving it. Biological intelligence, by contrast, is closed-loop: the brain continuously predicts sensory inputs, compares predictions against reality, and updates its internal model when surprised. No external process is needed.

Khailo invokes Eric Kandel's Nobel Prize-winning work showing that memory and computation are fused in individual neurons—they physically rewrite themselves as they learn. The breakthrough, he argues, requires models that do the same: self-updating, no separate training run, memory and compute integrated at fine grain. This demands an experimental substrate—something like a large, fast FPGA purpose-built for the task. Yet nobody is building it because the entire industry is optimizing the existing paradigm.

The article's real provocation is its call to action: if you're working on open-loop efficiency, you're not working on the breakthrough—you're working on the thing that makes the breakthrough harder to find. With every ASIC that ships, the window for closed-loop experimentation narrows. Khailo's piece is a rallying cry for someone to build the substrate before the hardware path dependency becomes irreversible.
