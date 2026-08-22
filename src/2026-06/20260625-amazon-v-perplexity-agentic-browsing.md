# Notes on Amazon v. Perplexity: Agentic Browsing and the Open Web
**Source**: https://educatedguesswork.org/posts/notes-amazon-perplexity/
**Date**: 2026-06-24
**Author**: ekr (Eric Rescorla)
**Keywords**: agentic browsing, prompt injection, Amazon, Perplexity, Comet browser, web security, open web

## Elevator pitch
Amazon's lawsuit against Perplexity's Comet browser surfaces a fundamental tension between agentic browsing and the open Web: sites want to control how they're accessed, but the Web's architecture gives users the right to choose their own client.

## Takeaways
- Amazon is suing Perplexity because Comet identifies itself as Chrome rather than as an AI agent, violating Amazon's Conditions of Use and creating security risks
- Agentic browsers add an AI harness that can interact with sites using the user's own browsing context — passwords, cookies, and local data — making the agent effectively the user
- The core security concern is prompt injection: malicious content on a website can hijack the AI agent to steal data or perform unauthorized actions
- The fundamental tension is between site control (sites wanting to dictate how they're accessed) and user agency (users having the right to choose their own client software)
- The open Web's architecture — where the site renders on the client — means users can always download software that renders sites however they prefer, making site-side restrictions unenforceable in the long run

## Synthesis
Eric Rescorla's analysis of Amazon v. Perplexity is one of the most technically grounded examinations of agentic browsing published to date. The lawsuit centers on Perplexity's Comet browser, which Amazon alleges was configured to identify itself as Google Chrome rather than as an AI agent, violating Amazon's Conditions of Use and creating security risks for customers.

The technical explanation of agentic browsers is clear and accessible. An agentic browser adds an AI harness — typically with a chat interface — that connects to the browser engine via a tool-calling interface. The agent can view and interact with sites using the same mechanisms a human user would. Crucially, if the agent shares the user's browsing context (passwords, cookies, local storage), it effectively becomes the user for all practical purposes. This is necessary for the agent to perform transactions on behalf of the user, but it also concentrates enormous trust in the agent.

The security analysis focuses on prompt injection as the new threat vector. When an AI model processes untrusted input — like the content of a web page — an attacker can craft content that causes the model to deviate from the user's actual instructions. In an agentic browsing context, this could mean a malicious website causing the agent to take actions the user never intended, such as making purchases, changing account settings, or revealing sensitive data. The model doesn't distinguish between the user's prompt and the data it's processing — both are concatenated into a single input stream.

Rescorla frames the deeper conflict as one between site control and user agency. Sites have always tried to control how users interact with their content — through terms of service, technical measures, and legal threats. But the open Web's fundamental architecture — where the site renders on the client — means users ultimately have the ability to download a client that renders the site however they prefer. Agentic browsing is just another browser feature that lets users engage with the Web on their terms.

The implication is that Amazon's legal strategy, while technically grounded in terms-of-service violations, is fighting against the structural reality of the open Web. The increased user agency of agentic browsing is what distinguishes the Web from downloadable apps, and sites that try to prevent it are in the same position as those who historically tried to prevent ad blocking, scraping, or alternative clients. The resolution will likely require new technical standards for agent identification rather than legal enforcement against specific browser implementations.