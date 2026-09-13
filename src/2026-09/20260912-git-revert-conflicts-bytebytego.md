# EP225: Why Does Git Revert Cause Conflicts?
**Source**: https://blog.bytebytego.com/p/ep225-why-does-git-revert-cause-conflicts
**Date**: 2026-09-12
**Author**: ByteByteGo (Alex Xu)
**Keywords**: git revert, git conflicts, version control, Claude Code features, symmetric encryption, asymmetric encryption, load balancing, cache systems, system design

## Elevator pitch
ByteByteGo's EP225 newsletter covers why git revert can cause conflicts (and how to resolve them), 12 essential Claude Code features every engineer should know, symmetric vs. asymmetric encryption explained, seven key load balancer use cases, four ways cache systems can go wrong, and the launch of ByteByteGo Live cohort-based courses.

## Takeaways
- `git revert` creates a new commit that undoes an earlier commit rather than rewriting history — conflicts arise when later commits changed the same lines the reverted commit touched, and Git cannot know which version is correct
- 12 Claude Code features worth knowing: CLAUDE.md project memory, Permissions, Plan Mode, Checkpoints, Skills, Hooks, MCP, Plugins, Context management, Slash Commands, Compaction, and Subagents for parallel task execution
- Symmetric encryption uses one shared key (fast, good for bulk data) while asymmetric uses a key pair (slower, ideal for identity/auth/key exchange) — the common mistake is using asymmetric for large payloads
- Seven load balancer use cases: traffic distribution, SSL termination, session persistence, high availability, scalability, DDoS mitigation, and health monitoring
- Four cache failure modes: thunder herd (mass expiry), cache penetration (non-existent keys), cache breakdown (hot key expiry), and cache crash — each with distinct mitigation strategies like random expiry jitter, null caching, bloom filters, and circuit breakers
- ByteByteGo Live launches cohort-based courses with ~40% completion vs. ~4% for self-paced, featuring courses on Claude Code, production AI systems, AI evals, and more, taught by engineers from Meta, Google, AMD, and Salesforce

## Synthesis
This newsletter is a dense system-design refresher that moves from a specific Git mechanics question to broad infrastructure literacy. The git revert explanation is the clearest piece: it distinguishes revert (safe, additive) from reset (destructive, history-rewriting) and shows precisely why conflicts emerge — not because revert is broken, but because it applies an inverse diff onto a codebase that has since moved on. The resolution workflow (revert → conflict → manual fix → stage → continue) is standard but worth documenting because developers often encounter it under pressure during hotfix rollbacks.

The 12 Claude Code features section is a useful inventory of the current agentic coding toolkit. The progression from project memory (CLAUDE.md) through plan mode and checkpoints to subagents maps the maturation of AI coding tools from single-shot assistants to orchestrated multi-agent workflows. Skills and Hooks in particular represent the shift toward programmable agent behavior — developers are now writing infrastructure for their AI collaborators, not just prompts.

The encryption and load balancer sections are standard ByteByteGo fare — clear, visual, suited for interview prep or onboarding. The cache failure modes section is the most practically useful: the distinction between thunder herd (many keys expire simultaneously) and cache breakdown (a single hot key expires) is often confused, and the mitigation strategies (expiry jitter, no-expiry hot keys, bloom filters, circuit breakers) are directly applicable to production systems. The launch of ByteByteGo Live with cohort-based courses signals the broader industry trend toward live, instructor-led AI engineering education as the gap between self-paced learning and real-world proficiency widens.