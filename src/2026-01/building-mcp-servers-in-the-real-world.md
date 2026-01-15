# Building MCP servers in the real world

**Source**: https://newsletter.pragmaticengineer.com/p/mcp-deepdive

**Date**: December 9, 2025

**Author**: Gergely Orosz and Elin Nilsson

**Keywords**: MCP, Model Context Protocol, AI agents, Claude Code, Cursor Agent, internal tools, data access, agent architecture

## Elevator pitch

Most Model Context Protocol (MCP) adoption happens invisibly inside companies where internal teams use it to democratize access to data warehouses and complex systems for non-technical stakeholders, not in public marketplaces as commonly assumed.

## Takeaways

- Only about 10 heavily-used public MCP servers exist from major developer-facing companies, while most production MCP usage occurs internally within organizations
- The median MCP user is a non-technical business stakeholder accessing company data warehouses through MCP servers, not developers building public tools
- Practical MCP implementations span development workflows (GitHub, JIRA), debugging (Sentry), testing (Playwright), design-to-code (Figma), documentation access, and legacy system integration
- Security concerns remain unresolved, making internal deployment behind corporate firewalls more prudent than public-facing servers
- Successful MCPs prioritize agent capabilities over human-friendly interfaces, avoiding features like confirmation prompts that break agent functionality

## Synthesis

Gergely Orosz and Elin Nilsson's article challenges the prevailing narrative around Model Context Protocol adoption by revealing a significant disconnect between public perception and actual usage patterns. While discussions of MCP often focus on public server marketplaces and developer tools, the authors present evidence that most meaningful MCP adoption occurs behind corporate firewalls, serving internal business needs rather than external developer audiences.

The article's most striking revelation comes from Jeremiah Lowin, CEO of Prefect, who explains that the "more builders than users" framing fundamentally misunderstands how MCP is being deployed. Approximately ten heavily-used public MCP servers exist from major developer-facing companies, while the vast majority of MCP implementations remain invisible because they operate within trusted corporate boundaries. This pattern emerges not from lack of interest but from MCP's primary value proposition: democratizing access to internal systems and data.

Counter to expectations that developers would drive MCP adoption, the median user profile is someone seeking to access "company's own data warehouse through an MCP server." Internal data and platform teams have recognized MCP as a mechanism to grant non-technical stakeholders—product managers, business analysts, executives—access to complex systems without requiring technical expertise. This represents a fundamental shift in how organizations think about tool access: rather than building specialized interfaces for each stakeholder group, they can expose systems through MCP and let AI agents handle the translation between user intent and system capabilities.

The practical use cases documented span an impressive range of domains. Development workflow integration enables agents to create pull requests and implement features by connecting to GitHub and JIRA. Debugging becomes more efficient through Sentry integration, allowing agents to analyze stack traces and suggest fixes automatically. Testing workflows benefit from Playwright and Puppeteer MCPs that automate browser interactions. Design-to-code transformations become practical through Figma MCPs—Razorpay reports achieving 75% accuracy on first-generation code from designs. Documentation access through Context7 and AWS MCPs reduces AI hallucinations by providing current reference material. Perhaps most intriguingly, custom MCPs bridge integration gaps with complex legacy systems like Siemens Polarion ALM, enabling modernization without wholesale replacement.

Security considerations remain a critical unresolved challenge. The protocol still faces open questions around authentication, authorization, and data protection, making internal deployment significantly more prudent than public-facing servers. This security limitation reinforces why most production MCPs operate behind corporate firewalls—organizations can manage risk within trusted boundaries while still capturing substantial value from agent-enabled access to internal systems.

The article highlights important design principles that emerge from real-world implementation. Successful MCPs prioritize agent capabilities over human-friendly interfaces, which represents a departure from traditional API design. Features like "elicitation" (confirmation prompts) that make sense for human interaction can break functionality when MCP clients don't support them. This forces developers to simplify designs and focus on what agents need: clear schemas, unambiguous endpoints, and predictable behavior rather than conversational flexibility.

This agent-centric design philosophy reflects a broader shift in how we think about system interfaces. Traditional APIs assume human developers will read documentation, understand context, and write code to orchestrate complex workflows. MCP-connected agents handle much of this orchestration automatically, but they require different affordances: structured responses over flexibility, explicit schemas over implicit conventions, and deterministic behavior over contextual adaptation.

The disconnect between public perception and actual usage patterns has significant implications for how we evaluate MCP's success. Counting public servers or GitHub stars dramatically understates adoption because it misses the primary deployment pattern: internal tools accessed through corporate infrastructure. This is somewhat analogous to how much enterprise software adoption occurs behind firewalls and doesn't appear in public metrics—the lack of visible activity doesn't indicate lack of value or adoption.

The authors document that MCPs are becoming infrastructure rather than end-user products. By enabling non-developers to access internal systems and allowing agents to handle complex workflows, MCPs change how teams operate fundamentally. Product managers can prototype features by having agents access data warehouses and generate mockups. Business analysts can query complex systems through natural language rather than learning SQL or custom query languages. Developers reduce context-switching by having agents handle routine integrations rather than manually copying information between systems.

Best practices for MCP development remain emergent. The field lacks standardized approaches to security, error handling, versioning, and other concerns that typically stabilize as technologies mature. However, the article suggests starting small and locally appears optimal for initial development—building internal MCPs for specific teams before expanding scope or considering public deployment.

The technology demonstrates concrete value across roles and use cases. Whether reducing context-switching for developers, enabling PMs to prototype features, or granting executives direct access to business intelligence systems, MCPs address real productivity gaps. The key insight is that this value accrues primarily within organizations rather than through public tooling—MCP's killer app may be internal system democratization rather than external developer tools.

This perspective reframes how we should evaluate protocol success. Rather than asking "how many public MCP servers exist?" the more meaningful question becomes "how many organizations have deployed internal MCPs to democratize system access?" The latter is far harder to measure but captures the protocol's actual impact more accurately. As MCP matures and security concerns resolve, this internal-first adoption pattern may persist as the dominant use case rather than an interim phase before public deployment becomes standard.
