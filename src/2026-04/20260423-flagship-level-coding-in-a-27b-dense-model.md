# Flagship-Level Coding in a 27B Dense Model

**Source**: https://simonwillison.net/2026/Apr/22/qwen36-27b
**Date**: April 22, 2026
**Author**: Simon Willison
**Keywords**: Qwen3.6-27B, open weights, coding models, local AI, llama.cpp

## Elevator pitch
Simon Willison highlights Qwen’s claim that a 27B dense open model now reaches flagship-level coding quality, and shows that a quantized local version can already produce impressively complex SVG output on consumer hardware.

## Takeaways
- Qwen says Qwen3.6-27B beats its previous giant open MoE coding model on major benchmarks.
- The smaller dense model dramatically lowers deployment footprint compared with the prior 397B-class model.
- Simon tested a 16.8GB quantized version locally with llama.cpp and got strong visual coding results.
- The result reinforces how fast local open-weight coding models are improving.
- The practical story is not just benchmark quality but accessibility on ordinary hardware.

## Synthesis
Simon Willison’s post is short, but it points to a meaningful shift in the open-model landscape. Qwen’s claim is that a 27B dense coding model can now match or beat the previous open-source flagship in its own family, which was a much larger mixture-of-experts system. If that holds up broadly, the important story is not only higher quality. It is that high-end coding capability is becoming cheaper to store, easier to run, and far more practical to use locally.

Simon’s local test is what makes the note compelling. Rather than only quoting the benchmark claims, he ran a quantized 16.8GB GGUF build through llama.cpp and used a familiar creative coding prompt, generating an SVG of a pelican riding a bicycle. The result was good enough for him to call it outstanding for a local model of that size. That kind of anecdotal benchmark matters because it reflects the experience of real users who care about whether an open model is actually worth running on their own machines.

There is also a broader pattern here. Dense models are regaining interest because they are simpler to deploy and often more predictable operationally than huge MoE checkpoints. If vendors can keep pushing dense open models upward on coding quality, then the practical gap between frontier cloud models and local developer tools could keep narrowing for many tasks.

The deeper takeaway is about distribution of capability. Each time a strong coding model becomes smaller and easier to run, more experimentation moves to the edge. Independent developers, security-conscious teams, and offline workflows all benefit. Even if the absolute best coding agents still live in the cloud, posts like this suggest that the baseline for local coding assistance is rising surprisingly fast.
