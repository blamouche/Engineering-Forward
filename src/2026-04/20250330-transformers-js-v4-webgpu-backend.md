# Transformers.js v4.0.0: New WebGPU Backend and Standalone Tokenizers
**Source**: https://github.com/huggingface/transformers.js/releases/tag/4.0.0
**Date**: March 30, 2025
**Author**: HuggingFace
**Keywords**: Transformers.js, WebGPU, browser ML, ONNX Runtime, tokenizers, Node.js, Bun, Deno, esbuild

## Elevator pitch
Transformers.js v4 introduces a rewritten WebGPU backend in C++ with ONNX Runtime achieving 4x speedups for embedding models, extends WebGPU support beyond browsers to Node/Bun/Deno, and releases a standalone 8.8kB tokenizers library.

## Takeaways
- New WebGPU runtime written in C++ with ONNX Runtime team, enabling WebGPU-accelerated models in Node, Bun, and Deno (not just browsers)
- ~4x speedup for BERT-based embedding models; supports larger models exceeding 8B parameters (~60 tokens/second on M4 Pro Max for a 20B model)
- Standalone @huggingface/tokenizers library at 8.8kB gzipped with zero dependencies
- ModelRegistry API for inspecting pipeline assets, checking cache status, and detecting available quantization types before loading
- Build system switched from Webpack to esbuild: build times from 2s to 200ms; main export 53% smaller

## Synthesis
Transformers.js v4 marks a significant maturation of browser-based and edge ML inference. The most consequential change is the WebGPU backend rewrite in C++ in collaboration with the ONNX Runtime team. Previous JavaScript-based inference backends left substantial performance on the table because JavaScript cannot fully exploit GPU hardware. The C++ implementation through ONNX Runtime closes much of this gap, delivering the 4x speedup for embedding models and enabling larger model classes that were previously impractical in browser or Node environments.

The extension of WebGPU support beyond browsers to Node, Bun, and Deno is strategically important. Previously, WebGPU-accelerated inference was tied to the browser runtime. The v4 expansion means server-side Node.js applications, edge runtimes like Deno Deploy, and Bun-based services can leverage WebGPU acceleration without deploying to GPU-equipped cloud instances. For inference workloads that fit within WebGPU's capabilities, this opens a cost-efficient serving path through commodity edge compute.

The standalone tokenizers library deserves recognition as an independent contribution. At 8.8kB gzipped with zero dependencies, it provides cross-platform tokenization that can be embedded in any JavaScript application without pulling in the full inference library. Tokenization is frequently needed independent of inference — for preprocessing, analytics, or rate limiting based on token counts — and a minimal implementation reduces the overhead of adding this capability.

The build system migration from Webpack to esbuild reflects the broader JavaScript ecosystem trend toward faster tooling. The 10x reduction in build time (2 seconds to 200ms) and 53% reduction in the main export size are meaningful for developer experience and deployment efficiency respectively. Smaller bundles reduce initial load times for browser applications and network transfer costs for edge deployments.

The ModelRegistry API addresses a gap in production deployment workflows: the ability to inspect model assets and check cache status before loading prevents the common pattern of a model attempting to load, discovering it's not cached, and making an unexpected network request in production.
