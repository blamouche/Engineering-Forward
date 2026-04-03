# TimesFM: Time Series Foundation Model by Google Research
**Source**: https://github.com/google-research/timesfm
**Date**: March 19, 2026
**Author**: Google Research
**Keywords**: time series, forecasting, foundation model, pretrained, quantile forecasting, PyTorch, JAX, open-source

## Elevator pitch
TimesFM is Google Research's open-source pretrained foundation model for time-series forecasting, supporting context lengths up to 16k tokens, continuous quantile forecasting, and 1,000-step horizons with both PyTorch and JAX backends.

## Takeaways
- 200M parameter pretrained model (reduced from previous 500M) optimized for efficiency
- Supports context lengths up to 16,000 tokens for long-horizon forecasting
- Provides continuous quantile forecasting up to 1,000-step horizons with uncertainty estimates
- Compatible with both PyTorch and JAX/Flax backends for flexible deployment
- Apache 2.0 licensed; archived versions available for backward compatibility

## Synthesis
TimesFM represents Google Research's application of the foundation model paradigm to time-series forecasting, a domain that has traditionally required domain-specific models trained on data from each individual use case. The premise is analogous to what large language models did for text: instead of training a separate model for each forecasting task, a single pretrained model can be applied across diverse temporal patterns with minimal task-specific adaptation.

The 200M parameter footprint of version 2.5, down from the previous 500M, reflects a deliberate efficiency optimization. For production forecasting systems where inference is called frequently — often over many time series simultaneously — model size directly affects deployment cost. The parameter reduction without capability regression indicates architectural improvements rather than simple compression.

The 16,000-token context length is significant for forecasting applications. Long-horizon forecasting requires the model to incorporate extended historical patterns — seasonal cycles, multi-year trends, and structural breaks — that shorter context windows cannot capture. For business forecasting, quarterly seasonality requires at least 4× the seasonal period in context; annual seasonality requires even more. The 16k context enables these patterns to be captured directly rather than requiring engineered features.

Continuous quantile forecasting is a practical improvement over point forecasts or discrete confidence intervals. Rather than predicting a single value or a fixed set of percentiles, continuous quantile prediction allows users to query any desired probability level at inference time. For risk-sensitive applications — inventory planning, demand forecasting, financial modeling — the ability to query P99 rather than being limited to pre-specified quantiles is operationally valuable.

The dual PyTorch/JAX backend support addresses a real deployment consideration: teams already invested in PyTorch ecosystem can use the model directly without framework switching, while Google's internal infrastructure (predominantly JAX-based) is equally supported. For organizations already using JAX through other Google ML tools, the consistency reduces operational overhead.
