# EP205: CPU vs GPU vs TPU
**Source**: https://blog.bytebytego.com/p/ep205-cpu-vs-gpu-vs-tpu
**Date**: Unknown
**Author**: Unknown
**Keywords**: CPU, GPU, TPU, hardware architecture, parallelism, accelerators

## Elevator pitch
A clear architectural comparison of CPUs, GPUs, and TPUs that explains why each excels at different workloads and how to choose the right compute for modern systems.

## Takeaways
- CPUs optimize for low‑latency, control‑heavy tasks with complex branching and system calls.
- GPUs trade single‑thread speed for massive data‑parallel throughput across thousands of cores.
- TPUs specialize further with systolic arrays and compiler‑controlled dataflow for dense matrix math.
- Performance differences come from architecture, memory hierarchies, and instruction execution models.
- Workload shape (branching vs. regular math) should drive accelerator selection.

## Synthesis
This ByteByteGo refresher frames the CPU–GPU–TPU debate as an architectural matching problem rather than a simple performance race. The CPU is presented as the general‑purpose workhorse: it is optimized for low latency, complex control flow, and rapid switching between different instructions. That makes it the default choice for operating systems, databases, and applications that need to handle lots of branching logic, system calls, interrupts, and unpredictable execution paths. The key takeaway is not that CPUs are “slow,” but that they are built for flexibility and responsiveness on a wide variety of tasks.

GPUs, by contrast, excel when the work can be parallelized across large datasets with the same instruction applied repeatedly. The article highlights the architectural shift: instead of a few powerful cores, GPUs pack thousands of simpler cores designed to execute in lockstep (SIMD/SIMT‑style). This makes them ideal for workloads like matrix multiplication, image processing, and neural network training, where the same operation is performed across many elements. The trade‑off is that GPUs are less efficient when the workload is irregular, branch‑heavy, or small enough that parallelism cannot be fully exploited.

TPUs push specialization even further. They are built around systolic arrays that move data through a grid of multiply‑accumulate units in a predictable, high‑throughput pipeline. By coupling that hardware with compiler‑controlled dataflow and on‑chip buffers for weights and activations, TPUs minimize data movement and maximize throughput for dense tensor operations. The synthesis emphasizes that TPUs are not “better GPUs,” but domain‑specific accelerators optimized for deep learning workloads that fit their dataflow constraints.

A recurring theme is that performance depends on matching workload shape to hardware design. CPUs handle control and branching; GPUs handle embarrassingly parallel math; TPUs handle highly structured tensor pipelines. Architectural choices determine the memory hierarchy, the scheduling model, and the instruction execution style, which in turn dictates why the same code can run quickly on a GPU and slowly on a CPU. The practical implication is that system designers should choose compute based on workload characteristics rather than brand or raw specs.

Finally, the article invites a systems‑level perspective: modern systems increasingly use heterogeneous compute, mapping different stages of a pipeline to different hardware. The lesson is not to pick one chip to rule them all, but to build architectures that route the right computation to the right accelerator, balancing cost, latency, and throughput. For AI engineers and system architects, the CPU–GPU–TPU comparison becomes a decision framework: identify the dominant operations, assess data parallelism and branching, and choose the hardware that aligns with those constraints.