# Securing non

**Source**: https://blog.cloudflare.com/improved-developer-security/
**Date**: April 14, 2026
**Author**: Justin Hutchings Adam Bouhmad Rebecca Varley
**Keywords**: blog, securing

## Elevator pitch
Cloudflare is introducing scannable API tokens, enhanced OAuth visibility, and GA for resource-scoped permissions. These tools help developers implement a true least-privilege architecture while protecting against credential leakage

## Takeaways
- Securing non-human identities: automated revocation, OAuth, and scoped permissions 2026-04-14 Justin Hutchings Adam Bouhmad Rebecca Varley 8 min read This post is also available in íêµ­ì´ .
- Agents let you build software faster than ever, but securing your environment and the code you write â from both mistakes and malice â takes real effort.
- Open Web Application Security Project (OWASP) details a number of risks present in agentic AI systems, including the risk of credential leaks, user impersonation, and elevation of privilege.
- These risks can result in extreme damage to your environments including denial of service, data loss, or data leaks â which can do untold financial and reputational damage.Â This is an identity problem.
- In modern development, "identities" aren't just people â they are the agents, scripts, and third-party tools that act on your behalf.

## Synthesis
Securing non-human identities: automated revocation, OAuth, and scoped permissions 2026-04-14 Justin Hutchings Adam Bouhmad Rebecca Varley 8 min read This post is also available in íêµ­ì´ . Agents let you build software faster than ever, but securing your environment and the code you write â from both mistakes and malice â takes real effort. Open Web Application Security Project (OWASP) details a number of risks present in agentic AI systems, including the risk of credential leaks, user impersonation, and elevation of privilege. These risks can result in extreme damage to your environments including denial of service, data loss, or data leaks â which can do untold financial and reputational damage.Â This is an identity problem. In modern development, "identities" aren't just people â they are the agents, scripts, and third-party tools that act on your behalf. To secure these non-human identities, you need to manage their entire lifecycle: ensuring their credentials (tokens) aren't leaked, seeing which applications have access via OAuth, and narrowing their permissions using granular RBAC. Today, we are introducing updates to address these needs: scannable tokens to protect your credentials, OAuth visibility to manage your principals, and resource-scoped RBAC to fine-tune your policies. Understanding identity: Principals, Credentials, and Policies To secure the Internet in an era of autonomous agents , we have to rethink how we handle identity. Whether a request comes from a human developer or an AI agent, every interaction with an API relies on three core pillars: The Principal (The Traveler): This is the identity itself â the "who." It might be you logging in via OAuth, or a background agent using an API token to deploy code. The Credential (The Passport): This is the proof of that identity.
