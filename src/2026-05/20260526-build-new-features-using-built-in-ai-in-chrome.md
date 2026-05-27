# Build new features using built-in AI in Chrome
**Source**: https://developer.chrome.com/blog/build-new-features-using-built-in-ai-in-chrome-io2026
**Date**: May 26, 2026
**Author**: Thomas Steiner
**Keywords**: built-in AI, Chrome, on-device AI, Summarizer API, Prompt API, Writer API, Rewriter API, Translator API, Gemini Nano, web platform

## Elevator pitch
Chrome's built-in AI APIs bring on-device language models directly to the browser, enabling developers to build AI-powered web features that are cost-efficient, privacy-preserving, and work offline — no cloud inference required.

## Takeaways
- Chrome's built-in AI runs models directly on users' devices, eliminating cloud inference costs and keeping sensitive data local.
- Five major APIs are now available: Summarizer, Prompt (with structured JSON output), Writer, Rewriter, and Translator — all accessible from JavaScript.
- The Prompt API supports multimodal input for image analysis, enabling automatic alt-text generation and captioning.
- Hybrid inference strategies (with polyfills and Firebase AI Logic) allow graceful cloud fallback on unsupported devices.
- Real-world adoption is growing: Drupal uses the Summarizer API for SEO, Yahoo! Japan uses the Prompt API for comment moderation, and Trip.com uses AI for flight booking overviews.

## Synthesis

Thomas Steiner's Google I/O 2026 talk presents Chrome's built-in AI as a fundamental shift in how web applications can integrate intelligence. Rather than routing every AI request to cloud servers, Chrome now exposes on-device language model APIs directly to JavaScript, unlocking a new class of applications that are cheaper, more private, and functional offline.

The talk frames this through a concrete use case: "trAIlblazers," a travel blog platform where AI assists content creators at every step — generating headlines, suggesting tags, moderating comments, writing alt-text for images, expanding bullet points into paragraphs, and translating content into multiple languages. This isn't speculative; a starter template built with Build Awesome (formerly Eleventy) is already available on GitHub with all these features implemented.

The technical architecture is noteworthy for its pragmatism. Chrome's built-in AI APIs are designed as progressive enhancements: the Summarizer, Writer, Rewriter, and Translator APIs handle common text tasks, while the Prompt API serves as the general-purpose interface with structured output support via JSON Schema. For multimodal use cases like image analysis, the Prompt API accepts pixel data, enabling features like automatic alt-text generation directly in the browser. The system also supports streaming responses, allowing real-time UI updates as the model generates output.

Steiner makes a compelling case for the economics of on-device AI: no cloud inference costs, hardware acceleration that can rival or beat cloud speeds, and offline functionality once models are downloaded. The privacy argument is equally strong — sensitive content never leaves the user's device, which matters for applications like comment moderation or personal writing assistance.

For the real world, hybrid inference strategies bridge the gap between ideal and reality. On devices that don't support built-in AI (particularly mobile devices), developers can use polyfills and Firebase AI Logic to fall back to cloud inference while staying native on desktop. This "best of both worlds" approach acknowledges that on-device AI deployment is uneven while pushing the web platform forward.

The partner adoption section is brief but telling: Drupal, Yahoo! Japan, and Trip.com are already shipping features built on these APIs, suggesting that built-in AI has moved beyond experimental status into production readiness. Combined with TypeScript support via `@types/dom-chromium-ai` and comprehensive documentation, the developer experience appears deliberately polished — Google clearly wants this to be a real platform capability, not a toy.

What's most significant about this initiative is how it changes the mental model for web developers. Instead of AI being something you call out to, it becomes something you have locally, like localStorage or the Canvas API. The implications for web application architecture are substantial: offline-first AI features, zero-latency inference, and a shift in cost modeling where adding AI to a feature doesn't automatically mean a cloud bill. If browser vendors continue investing in on-device models, the line between native apps and web apps will blur even further, with the browser becoming an increasingly capable AI runtime.
