# The Product-Minded Engineer

**Source**: https://newsletter.pragmaticengineer.com/p/the-product-minded-engineer

**Date**: January 20, 2026

**Author**: Gergely Orosz, Drew Hoskins

**Keywords**: product engineering, error handling, diagnostics, API design, developer experience, software craftsmanship

## Elevator pitch

Drew Hoskins argues that product-minded engineers distinguish themselves by treating error messages as first-class UI, applying the same thoughtfulness to diagnostics that they bring to feature development.

## Takeaways

- Diagnostics frequently constitute the primary interaction point for users in complex systems, making error message design a critical product skill
- Engineers should categorize errors into five types (System, User's Invalid Argument, Precondition, Developer's Invalid Argument, and Assertion) to tailor messages appropriately
- Effective errors suggest solutions or alternatives rather than merely stating what went wrong
- Catching errors early through static validation, testing fakes, or confirmations reduces user frustration and protects systems
- The rising demand for product engineers correlates with AI handling more code generation, requiring engineers to specify what systems should build

## Synthesis

Gergely Orosz interviews Drew Hoskins about his new O'Reilly book on becoming a product-minded engineer, with an exclusive excerpt focused on error design. Hoskins brings over two decades of experience from Microsoft, Facebook, Oculus, and Stripe, and currently works as a Staff Product Manager at Temporal. His career trajectory from platform infrastructure through API design to product leadership gives him a unique perspective on how engineers can develop product intuition.

The central argument of the excerpt is that diagnostics—error messages and warnings—represent an overlooked but critical aspect of product development. Hoskins contends that well-crafted error messages often constitute the primary interaction users have with complex systems. When a system fails, the error message becomes the entire user experience at that moment. Treating it as an afterthought means abandoning users precisely when they need guidance most.

Hoskins presents a framework for categorizing errors into five types: System errors (infrastructure failures), User's Invalid Argument (incorrect input from end users), Precondition errors (missing requirements), Developer's Invalid Argument (API misuse by calling code), and Assertion errors (impossible states indicating bugs). Each category demands different messaging strategies because each serves a different audience with different needs. A user encountering a validation error needs different information than a developer debugging an API integration.

The principle of actionable messaging runs throughout the excerpt. Rather than merely stating what went wrong, effective errors should suggest solutions or alternatives. Using a fictional messaging platform called Channelz as a running example, Hoskins demonstrates how error messages can guide users toward resolution instead of leaving them stranded.

Hoskins emphasizes raising errors at interface boundaries—the points where system-level understanding meets user-intent knowledge. By combining technical context with awareness of what users are trying to accomplish, engineers can craft messages that are both accurate and helpful. This typically happens at API or UI boundaries through upfront validation or error repackaging.

The concept of "shifting left" appears as a practical strategy: catching errors early through static validation, testing fakes, or confirmations reduces user frustration and protects systems from processing invalid inputs. This proactive approach aligns with product thinking by preventing problems rather than merely handling them gracefully.

Orosz notes that the demand for product-minded engineers is rising alongside AI capabilities in code generation. As AI tools handle more implementation work, engineers increasingly need to specify what systems should build rather than just executing predetermined solutions. This shift makes product intuition more valuable than ever. Hoskins cites John Carmack as an exemplary product-minded engineer who combined deep technical expertise with relentless pursuit of user-facing goals, suggesting that this combination defines the most effective engineering careers.
