# China's Zhipu Rolls Out AI Model Trained on Huawei Chips

**Source**: https://www.techinasia.com/news/chinas-zhipu-rolls-ai-model-trained-huawei-chips

**Date**: January 14, 2026

**Author**: Tech in Asia

**Keywords**: Zhipu AI, Huawei, Ascend chips, GLM-Image, China AI, US sanctions, image generation, open-source AI

## Elevator pitch

Chinese AI startup Zhipu has unveiled GLM-Image, the first state-of-the-art multimodal model trained entirely on domestic Huawei Ascend chips, marking a significant milestone in China's push for AI self-reliance amid US export restrictions.

## Takeaways

- GLM-Image is the first major AI model trained end-to-end on Huawei's Ascend Atlas 800T A2 hardware, demonstrating viable alternatives to Nvidia GPUs
- The model uses a hybrid architecture combining a 9-billion-parameter autoregressive model with a 7-billion-parameter diffusion decoder for instruction understanding and detail rendering
- GLM-Image achieved first place among open-source models on the CVTG-2K benchmark with a Word Accuracy score of 0.9116 for text placement in images
- The development was accelerated after the US Commerce Department added Zhipu to its entity list, cutting off access to Nvidia H100 and A100 GPUs
- Zhipu has open-sourced the model on GitHub, Hugging Face, and ModelScope, with API access priced at 0.1 yuan (~$0.014) per generated image

## Synthesis

Zhipu AI's announcement of GLM-Image represents a watershed moment in the ongoing technology competition between China and the United States. The image generation model, unveiled on January 14, 2026, is notable not primarily for its technical capabilities—though those are impressive—but for what it represents: proof that Chinese companies can train state-of-the-art AI models without access to American hardware.

The strategic context is essential for understanding this development. Last year, the US Commerce Department added Zhipu to its entity list, citing alleged ties to China's military. This designation effectively barred the company from purchasing Nvidia's most advanced GPUs, the H100 and A100 chips that have become the de facto standard for AI training worldwide. Rather than accepting diminished capabilities, Zhipu pivoted to collaboration with Huawei, whose Ascend chips have been positioning as domestic alternatives to American silicon.

GLM-Image's architecture reflects thoughtful engineering choices. The hybrid approach combines a 9-billion-parameter autoregressive model—responsible for understanding instructions and planning overall image composition—with a 7-billion-parameter diffusion decoder that handles fine detail rendering and accurate text placement. This division of labor allows each component to specialize in what it does best, resulting in a model that excels at generating images with precisely positioned text, a traditionally challenging task for image generation systems.

The benchmark results validate this approach. On CVTG-2K, which specifically measures text placement accuracy across multiple image locations, GLM-Image achieved a Word Accuracy score of 0.9116, claiming first place among open-source models. While benchmarks always warrant skepticism, this performance suggests Huawei's hardware can support competitive AI training, at least for models of this scale.

The market response has been dramatic. Zhipu's shares surged more than 17% following the announcement, building on an already remarkable 80% gain since the company became the first major Chinese AI startup to go public the previous week. Investors appear to be betting that Zhipu's demonstrated ability to work around US restrictions positions it favorably for long-term growth in China's expanding AI market.

Zhipu's decision to open-source the model weights—making them available on GitHub, Hugging Face, and ModelScope—serves multiple purposes. It allows independent verification of capabilities, builds goodwill in the developer community, and demonstrates confidence in the technical achievement. The API pricing at 0.1 yuan per image positions the service competitively for commercial adoption.

For the broader AI industry, GLM-Image signals that the era of Nvidia's unchallenged dominance in AI training may be entering a new phase. While Huawei's chips likely cannot yet match Nvidia's most advanced offerings in raw performance, this release demonstrates they have reached a threshold of practical viability that could reshape global AI development patterns.
