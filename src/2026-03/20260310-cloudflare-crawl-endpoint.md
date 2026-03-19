# Crawl entire websites with a single API call using Browser Rendering
**Source**: https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/
**Date**: 2026-03-10
**Author**: Cloudflare
**Keywords**: Cloudflare, web crawling, Browser Rendering, RAG, training data, robots.txt, crawl API, WebAssembly, headless browser

## Elevator pitch
Cloudflare's new /crawl endpoint enables single-call website crawling with a headless browser, respecting robots.txt by default and returning content in HTML, Markdown, or JSON—designed for RAG pipelines and training data collection.

## Takeaways
- Asynchronous processing: submit a URL, receive a job ID, poll for results as pages are discovered and rendered.
- Compliance-focused: the crawl endpoint functions as a signed agent that respects robots.txt and AI Crawl Control by default—not designed to bypass protections.
- Multiple output formats: HTML, Markdown, and JSON powered by Workers AI for different downstream use cases.
- Incremental crawling: `modifiedSince` and `maxAge` parameters reduce redundant processing for repeated crawls of the same domain.
- Static mode option: bypasses browser rendering for faster retrieval of server-rendered HTML.
- Limitations: cannot bypass bot detection or CAPTCHAs; self-identifies as a bot.
- Available on Workers Free and Paid plans, currently in open beta.

## Synthesis
Cloudflare's /crawl endpoint turns an expensive, complex operation—rendering an entire website in a headless browser—into a managed service. Previously, teams building RAG pipelines or training datasets had to operate their own crawling infrastructure: managing headless Chrome instances, handling JavaScript-heavy sites, implementing polite crawling behavior, and dealing with the operational complexity of distributed crawling at scale. This API abstracts all of that.

The compliance-first design is the feature most likely to matter for enterprise adoption. Organizations building AI training datasets or knowledge bases need to demonstrate they've respected publisher restrictions. A tool that respects robots.txt and AI Crawl Control by default, and self-identifies as a bot, creates a cleaner compliance story than custom crawlers that require teams to implement these behaviors themselves.

The incremental crawling parameters address a practical issue with long-running RAG systems: content changes, and keeping the knowledge base current requires re-crawling, but re-crawling entire domains is expensive. `modifiedSince` allows targeting only recently changed content, dramatically reducing the cost of keeping large-scale indexed content current.

The positioning of this alongside Cloudflare's Workers AI stack is strategic: teams that host their RAG infrastructure on Cloudflare can now run the entire pipeline—crawl, embed, query, generate—within Cloudflare's network, reducing latency and egress costs. This is the same bundling strategy that made S3 + Lambda + API Gateway a natural fit, applied to AI infrastructure.
