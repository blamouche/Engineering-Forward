# Quantization from the ground up
**Source**: https://ngrok.com/blog/quantization
**Date**: March 25, 2026
**Author**: Sam Rose
**Keywords**: quantization, model compression, LLM performance, floating point, benchmarking

## Elevator pitch
A hands-on explanation of how quantization compresses LLMs, why it preserves most quality at 8- and 4-bit levels, and how to evaluate the trade-offs in accuracy and speed.

## Takeaways
- LLM size is dominated by parameters stored as floating point values; shrinking their precision yields big memory wins.
- Most model weights cluster near zero, which makes low-precision formats viable for many parameters.
- Quantization is lossy compression: symmetric and asymmetric schemes trade off error and overhead.
- Outliers break naive, whole-model quantization, so real systems quantize in small blocks.
- Benchmarking quantized models requires multiple lenses (perplexity, KL divergence, task scores, and real usage).

## Synthesis
Quantization is the practice of shrinking a model’s numeric precision to reduce memory and speed up inference. The post opens with the scale problem: modern LLMs contain billions to trillions of parameters, and storing those weights as 16- or 32-bit floats balloons RAM requirements far beyond what typical hardware can handle. Because most parameters are just numbers in memory, compressing them yields immediate gains. The author explains that floats trade off range and precision by allocating bits to sign, exponent, and significand. Lower-precision formats such as float16 or bfloat16 reduce memory by half while remaining broadly accurate because most model weights sit near zero and don’t need large ranges.

The core of the piece breaks down how quantization works as a lossy compression technique. Directly rounding high-precision floats to low-precision values is often disastrous, especially at 4-bit or 2-bit levels. Symmetric quantization improves on this by scaling weights into a tight integer range centered at zero, then dequantizing at runtime using a saved scale factor. This reduces error relative to naïve rounding while shrinking memory footprint. Asymmetric quantization goes further by shifting the range to match data distributions that aren’t centered on zero, improving accuracy again by reducing wasted representational space. The article shows these approaches with small examples that make the distortion concrete.

A critical practical detail is outliers. While most weights cluster near zero, a few large values can distort scaling and wreck accuracy if you quantize an entire model in one shot. Production systems avoid that by quantizing in blocks (often 32–256 parameters). Each block has its own scale (and zero point for asymmetric), which contains the impact of outliers but introduces overhead. Choosing block size is a trade‑off: smaller blocks improve fidelity but add more metadata.

The post also emphasizes that quantization impacts not only accuracy but behavior. It walks through evaluation approaches that capture different aspects: perplexity (confidence in the correct next token), KL divergence (distribution shifts across all token probabilities), and task benchmarks such as GPQA. The examples show minimal change for 8-bit symmetric quantization and modest degradation for 4-bit variants, while 2-bit quantization often collapses model usefulness. The author then layers in “real-world” checks—asking the model questions—and highlights that low-bit quantization can fail in ways that aren’t captured by a single metric.

Performance is the other side of the coin. Benchmarks using llama.cpp demonstrate that 8- and 4-bit quantization can roughly double token throughput versus bfloat16, on both consumer hardware and datacenter GPUs. The post closes with a practical stance: quantized models are far more capable than many assume, and the quality drop is not linear. For many use cases, 8- or 4-bit quantization yields substantial speed and memory benefits with acceptable accuracy loss. The right choice depends on the task, which is why the author encourages systematic evaluation rather than intuition alone.
