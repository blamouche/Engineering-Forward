# Toto 2.0: Time series forecasting enters the scaling era
**Source**: https://www.datadoghq.com/blog/ai/toto-2/
**Date**: May 14, 2026
**Author**: Emaad Khwaja, Gerald Woo, Chris Lettieri, Ameet Talwalkar, David Asker (Datadog)
**Keywords**: time series forecasting, foundation models, Toto 2.0, Datadog, scaling laws, open-weights, observability

## Elevator pitch
Datadog releases Toto 2.0 — a family of open-weights time series forecasting models from 4M to 2.5B parameters — demonstrating that time series foundation models follow scaling laws: every size improves on the one below it with no sign of saturation.

## Takeaways
- Toto 2.0 spans 4M to 2.5B parameters with consistent improvement at every scale, suggesting time series forecasting benefits from the same scaling dynamics as language models
- Claims best-in-class performance on every benchmark tested, including BOOM (Datadog's observability benchmark) and standard academic benchmarks
- Open-weights release on Hugging Face makes the models accessible for research and commercial use
- Positions time series forecasting as entering a "scaling era" similar to what NLP experienced with GPT/BERT
- Practical implications for anomaly detection, capacity planning, and resource optimization at scale

## Synthesis
Toto 2.0 represents a significant milestone in applying the foundation model paradigm to time series forecasting. The core finding — that scaling laws apply to time series models just as they do to language models — could reshape how organizations approach forecasting infrastructure. Instead of training bespoke models per metric or system, a single scaled foundation model could provide state-of-the-art forecasts across diverse domains.

The 4M to 2.5B parameter range demonstrates a clear scaling trajectory without saturation, suggesting that even larger models could yield further improvements. This mirrors the early days of language model scaling, where each doubling of parameters reliably improved performance. For Datadog, whose business depends on helping customers detect anomalies and predict capacity needs, better forecasting directly impacts product value.

The open-weights release strategy is notable: it positions Datadog as a research leader in the observability space while ensuring the broader community can build on the work. Combined with Datadog's LLM observability products, Toto 2.0 suggests the company is making a strategic bet on AI-first observability — where foundation models handle not just text generation but the core analytical tasks that observability platforms have traditionally solved with statistical methods.
