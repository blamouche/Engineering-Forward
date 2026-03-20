# LLM Architecture Gallery
**Source**: https://sebastianraschka.com/llm-architecture-gallery/
**Date**: 2026-03-17
**Author**: Sebastian Raschka, PhD
**Keywords**: LLM architecture, transformer, MoE, attention, GPT, Qwen, DeepSeek, model comparison, reference

## Elevator pitch
Sebastian Raschka's LLM Architecture Gallery compiles architecture diagrams and technical specifications for 50+ large language models in one place, from 1.5B-parameter GPT-2 variants to trillion-parameter systems like Kimi K2.

## Takeaways
- 50+ model cards covering parameter counts, context windows, attention mechanisms, architecture types, licenses, and publication dates
- Spans the evolution from classic dense transformers to sparse MoE designs and emerging hybrid architectures
- Models range from GPT-2 XL (1.5B) to DeepSeek V3 (671B) and Kimi K2 (multi-trillion scale)
- Sourced from four Raschka articles on his Ahead of AI newsletter, with GitHub implementations available
- Physical poster versions available; regularly updated (last update March 17, 2026)

## Synthesis
Sebastian Raschka's LLM Architecture Gallery fills a genuine reference gap in the AI practitioner's toolkit. The landscape of large language model architectures has expanded rapidly, with dozens of significant models released in the past two years across different organizations, parameter scales, and architectural approaches. Keeping current with this landscape previously required reading dozens of technical reports and synthesizing their architectural details independently.

The gallery's value is in standardization. Each model card presents the same set of attributes—parameter counts, context window, decoder architecture type (dense, sparse MoE, or hybrid), attention mechanism variant (MHA, GQA, MLA), license, and publication date—enabling direct comparison across models that would otherwise require careful reading of individual technical reports to compare.

The architectural taxonomy the gallery reveals is itself informative. The shift from dense transformer architectures (where all parameters are active for every token) to sparse MoE designs (where only a fraction activate per token) is visible across the model timeline. More recent entries show hybrid approaches combining traditional attention with linear attention variants, reflecting ongoing experimentation with the attention mechanism's quadratic scaling properties.

The coverage of Chinese lab models—DeepSeek V3/V3.2, Qwen3 family, Kimi K2—alongside Western models provides a genuinely global picture that is sometimes underrepresented in English-language AI coverage. DeepSeek V3's 671B parameters and Kimi K2's multi-trillion scale represent architectural choices and training investments that influence the field regardless of their geographic origin.

For practitioners making model selection decisions, infrastructure sizing estimates, or architecture research decisions, the gallery provides reference material that reduces the time cost of comparative analysis. The GitHub link to LLMs-from-scratch implementations adds a pedagogical dimension—understanding architectures through implementation is often more durable than reading architecture diagrams alone.
