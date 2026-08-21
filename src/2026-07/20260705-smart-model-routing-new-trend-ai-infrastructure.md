# Smart Model Routing: The New Trend in AI Infrastructure
**Source**: https://newsletter.pragmaticengineer.com/p/the-pulse-a-new-trend-smart-model-routing
**Date**: 2026-07-02
**Author**: Gergely Orosz
**Keywords**: model routing, AI infrastructure, token costs, LLM routing, Factory Router, Not Diamond, OpenRouter, LiteLLM, intelligent routing

## Elevator pitch
A new category of "intelligent routing" tools is emerging to automatically select the right AI model for each task, addressing the 10-20x cost difference between cheap and frontier models.

## Takeaways
- Token prices vary 10-20x between cheap models and state-of-the-art ones, creating a strong economic incentive for intelligent model selection
- Several vendors have launched dedicated routing products: Factory Router (20-25% cost savings), Not Diamond (30% cost savings for coding, used by OpenRouter), Prism by Augment Code, Model Router by Morph, and Weave Router
- AI gateways with routing built in include OpenRouter (auto router using Not Diamond), Kilo Gateway, Requestly.ai, and LiteLLM (more manual but more control)
- Open source option: Envoy AI Gateway offers routing configuration focused more on availability than cost optimization
- Hosted open models are sufficient for approximately 60% of coding-related work by token spend, according to Factory AI CEO Matan Grinberg, and open model usage is strictly increasing
- Cursor's fixed-price "Auto" model and GitHub Copilot's Auto mode represent the product-embedded approach, but feedback on Copilot's auto mode has been mixed, and top models aren't available on all tiers

## Synthesis
Gergely Orosz identifies "intelligent routing" as a new and rapidly growing category in AI infrastructure. The core insight is simple but economically powerful: with token prices varying 10-20x between commodity models and frontier ones, there's a massive cost optimization opportunity in selecting the right model for each request rather than defaulting to the most capable option.

The article maps out the emerging ecosystem with impressive clarity. Dedicated routing vendors like Factory Router, Not Diamond, Prism, and Morph's Model Router each approach the problem differently—some focusing on coding tasks, others on general-purpose routing, still others on agentic workflows. The AI gateway layer adds another dimension: OpenRouter, Kilo Gateway, Requestly.ai, and LiteLLM all embed routing into the API gateway function, which is how most enterprises actually access LLMs in production.

The most significant data point comes from Factory AI's CEO: approximately 60% of coding-related token spend can be served by hosted open models. This aligns with the broader industry trend of open models (Llama, Mistral, DeepSeek) becoming increasingly competitive on quality while offering dramatically lower costs. If intelligent routing becomes table stakes—as Orosz argues it will—the implications are far-reaching: frontier model providers face pricing pressure, open model adoption accelerates, and a new layer of infrastructure emerges between applications and model providers.

The article also honestly notes the limitations. Envoy AI Gateway's routing focuses on availability rather than cost optimization. GitHub Copilot's Auto mode hasn't received enthusiastic feedback from developers. And the routing decisions themselves are only as good as the classification logic—misrouting a complex prompt to a cheap model could produce poor results that negate the cost savings.

The bottom line: intelligent routing is becoming infrastructure-grade technology, and organizations that aren't evaluating their model routing strategy are likely overpaying for AI inference by a significant margin.