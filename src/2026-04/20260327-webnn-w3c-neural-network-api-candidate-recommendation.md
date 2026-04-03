# Web Neural Network API — W3C Candidate Recommendation
**Source**: https://www.w3.org/TR/webnn/
**Date**: March 27, 2026
**Author**: W3C
**Keywords**: WebNN, W3C, neural network, browser ML, hardware acceleration, GPU, NPU, on-device inference, privacy

## Elevator pitch
The W3C Web Neural Network API reaches Candidate Recommendation status, defining a hardware-agnostic low-level API for neural network inference acceleration across GPU, CPU, and NPU from web applications.

## Takeaways
- Defines a low-level API for hardware-accelerated neural network inference, abstracting across GPU, CPU, and NPU
- Enables ML frameworks to build, compile, and execute computational graphs with hardware acceleration
- Supports computer vision, NLP, audio processing, and generative AI use cases directly from web browsers
- Privacy-preserving by design: keeps sensitive user data on-device rather than requiring cloud processing
- Candidate Recommendation status indicates the spec is stable and ready for implementation review

## Synthesis
The Web Neural Network API reaching Candidate Recommendation status is a milestone in the standardization of on-device machine learning in web browsers. Candidate Recommendation means the W3C Working Group considers the specification complete and stable, and is seeking implementation experience from browser vendors before advancing to full Recommendation status.

WebNN's position in the ML stack is specifically as a low-level hardware abstraction layer. Higher-level ML frameworks — TensorFlow.js, ONNX Runtime Web, Transformers.js — can use WebNN as their execution backend rather than implementing their own hardware-specific optimizations for each GPU and NPU architecture. This prevents duplication of effort: each framework that adopts WebNN automatically gains support for all hardware that WebNN supports, rather than each framework needing to separately implement GPU and NPU support.

The hardware scope — GPU, CPU, and NPU — reflects the current diversity of devices that run web browsers. Desktop browsers primarily have GPUs; mobile devices increasingly include dedicated Neural Processing Units; all devices have CPUs as a fallback. WebNN provides a unified interface that can route neural network operations to whatever hardware is available, enabling web applications to benefit from specialized hardware without building hardware-specific code paths.

The privacy-preserving framing is architecturally significant. Cloud-based ML inference requires sending user data to servers, which creates privacy exposure for sensitive use cases like medical image analysis, voice interactions, or document processing. WebNN enables inference to run entirely on the user's device, eliminating this exposure. As privacy regulations tighten and user sensitivity to data sharing increases, this property becomes increasingly valuable for applications that handle sensitive information.

For web developers, WebNN's stabilization signals that browser-based ML is becoming infrastructure rather than experimental technology. As major browsers implement the spec, the baseline ML capabilities available to web applications without cloud dependencies will expand.
