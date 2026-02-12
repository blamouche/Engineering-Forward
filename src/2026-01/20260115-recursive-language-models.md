# Recursive Language Models

**Source**: https://alexzhang13.github.io/blog/2025/rlm/

**Date**: October 15, 2025

**Author**: Alex L. Zhang (with Omar Khattab)

**Keywords**: language models, recursive inference, context scaling, programmatic context, long-context processing

## Elevator pitch

Language models can dramatically improve their performance on long-context tasks by recursively calling themselves through Python REPL environments, treating prompts as variables rather than consuming entire contexts at once.

## Takeaways

- Traditional long-context approaches suffer from "context rot" where performance degrades as context windows increase, even when models theoretically fit the data
- RLMs treat the prompt as a Python variable in a REPL environment, allowing programmatic interaction with unbounded input lengths
- RLM(GPT-5-mini) outperformed GPT-5 by over 33% on 132k-token contexts while maintaining comparable costs
- The system spontaneously develops emergent strategies like peeking, grepping, partition-map operations, and summarization
- This represents a shift from problem-centric decomposition (agents) to context-centric decomposition where the LM determines optimal handling strategies

## Synthesis

Alex L. Zhang and Omar Khattab from MIT CSAIL introduce Recursive Language Models (RLMs), a novel inference strategy that fundamentally reimagines how language models handle long contexts. Rather than processing entire contexts directly as traditional approaches do, RLMs decompose complex problems by recursively calling themselves or other language models through Python REPL environments. The key innovation lies in treating the prompt as a Python variable that can be processed programmatically, enabling dynamic interaction with unbounded input lengths.

The motivation for this approach stems from a critical limitation of existing long-context models: "context rot." Even when models theoretically have sufficient token capacity, their performance degrades as context windows increase. This phenomenon affects even state-of-the-art models, suggesting that simply expanding context windows is not a sustainable solution. The RLM framework addresses this by giving models the agency to determine dynamically which portions of context to examine, rather than forcing them to consume everything at once.

The empirical results are compelling. On the OOLONG benchmark, RLM(GPT-5-mini) outperformed the larger GPT-5 model by over 33% when processing 132k-token contexts, while maintaining comparable costs. This performance advantage persisted even at 263k tokens, though with some degradation. Perhaps even more impressive, on the BrowseComp-Plus document retrieval task, RLM(GPT-5) maintained perfect performance while handling 1,000 documents totaling approximately 10 million tokens, demonstrating cost-effective scaling compared to both retrieval baselines and truncation approaches.

What makes RLMs particularly fascinating is the emergence of sophisticated interaction patterns that the system develops spontaneously. The authors identified four primary strategies: peeking (initial context inspection to identify structure), grepping (regex-based filtering to narrow search spaces), partition-map operations (chunking contexts and running parallel recursive queries), and summarization (condensing subsets for outer-model decision-making). These strategies were not explicitly programmed but emerged from the model's ability to manipulate context programmatically.

The authors acknowledge several limitations in their current implementation. The system lacks optimization for speed, asynchronous processing, and prefix caching. Runtime and cost guarantees remain uncontrolled, requiring systems-level optimization before production deployment. However, these are engineering challenges rather than fundamental limitations of the approach.

The broader significance of RLMs extends beyond technical performance improvements. The authors position this work as representing "the next milestone in general-purpose inference-time scaling" and a fundamental paradigm shift in how we think about language model inference. Traditional agent frameworks focus on problem-centric decomposition—breaking down tasks into subtasks. RLMs introduce context-centric decomposition, where the model itself determines optimal strategies for handling large contexts.

This approach opens new possibilities for scaling language model capabilities at inference time. Rather than relying solely on larger models or longer context windows, RLMs demonstrate that strategic, programmatic interaction with context can yield superior results. The recursive nature of the system allows for arbitrary depth of analysis, limited only by practical considerations of time and cost rather than architectural constraints.

The work also raises intriguing questions about the nature of intelligence and problem-solving. By giving models the tools to manipulate their own inputs programmatically, the researchers have created a system that exhibits more sophisticated reasoning patterns than direct inference alone. The emergence of strategies like grepping and partition-map operations suggests that language models, when given appropriate tools and frameworks, can develop surprisingly sophisticated problem-solving approaches autonomously.
