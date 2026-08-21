# Why DoorDash, Instacart, and Uber Eats Integrated LLMs Into Search Three Different Ways
**Source**: https://blog.bytebytego.com/p/why-doordash-instacart-and-uber-eats
**Date**: 2026-07-28
**Author**: ByteByteGo
**Keywords**: LLM search, DoorDash, Instacart, Uber Eats, food delivery, architecture, retrieval-augmented generation, semantic search, infrastructure

## Elevator pitch
Three major food delivery companies solved the same LLM-search integration problem in three fundamentally different architectures—revealing that existing infrastructure, not model choice, determines how deeply AI should reach into your production runtime.

## Takeaways
- The core problem is the same across all three: keyword search fails on synonyms, typos, shorthand, and natural-language intent like "something healthy for a rainy evening."
- DoorDash chose a "thin integration" approach where the LLM sits outside the runtime as a query-understanding layer, translating natural language into structured search parameters—minimizing latency and maintaining existing infrastructure.
- Instacart went deeper, embedding the LLM inside the search pipeline to reshape ranking and retrieval in real time—trading more latency and cost for richer understanding.
- Uber Eats took the deepest integration, giving the LLM direct access to the runtime so it can reason over catalog data, user context, and business rules simultaneously—maximizing understanding but adding the most complexity.
- The key insight is architectural: which approach fits depends not on which LLM you pick but on what infrastructure you already have in place, how much latency you can tolerate, and what level of intent resolution your product requires.

## Synthesis
ByteByteGo's deep dive into how DoorDash, Instacart, and Uber Eats each rebuilt their search systems around LLMs is one of the clearest architectural comparisons available for teams integrating AI into existing production systems. The article frames the decision as a single question: how deeply should the LLM reach into the runtime?

DoorDash's thin integration treats the LLM as a query-understanding preprocessor. Natural-language queries get translated into structured search parameters before they hit the existing search engine. This is the least invasive approach: low latency, minimal infrastructure change, and easy to roll back, but the LLM never sees actual catalog data or real-time inventory.

Instacart's middle-ground approach embeds the LLM within the search pipeline itself. The model participates in ranking and retrieval, which means it can consider richer signals—product attributes, user preferences, substitution logic—but it also adds latency at a critical path in the user experience.

Uber Eats went all-in, giving the LLM direct access to the runtime environment. The model reasons over the full catalog, user context, pricing, and business rules simultaneously. This delivers the richest understanding but requires the most engineering investment, the most compute, and the most careful latency management.

The article's most valuable contribution is not the specific implementations (which draw on published engineering blogs from each company) but the framework for thinking about the decision. The specific model each company chose was secondary to the infrastructure question. Teams evaluating LLM integration should start by auditing what they already have, then pick the depth that matches their latency budget and their product's tolerance for imperfect understanding.

For engineering leaders, this is a must-read architecture pattern comparison that maps directly onto any domain where search or intent resolution matters—not just food delivery.