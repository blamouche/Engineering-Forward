# Fair Source Software in the AI Age
**Source**: https://blog.sentry.io/fair-source-software-in-the-ai-age/
**Date**: 2026-03-17
**Author**: Chad Whitacre, Gavin Zee
**Keywords**: fair source, licensing, AI, copyright, open source, Cloudflare, Next.js, code generation, LLM training

## Elevator pitch
Sentry's authors argue that Fair Source licensing remains viable against three AI-driven threats to software licensing: unauthorized training data use, rapid AI-assisted rewrites, and the absence of copyright protection for AI-generated code.

## Takeaways
- LLMs trained on public source code without license compliance raise unresolved "fair use" legal questions
- AI agents can quickly reimplement libraries under different licenses—Cloudflare rebuilt Next.js in a week using agentic coding
- The U.S. Supreme Court declined to extend copyright to AI-generated material, requiring "significant human element" for eligibility
- Fair Source licenses use non-compete clauses rather than copyright alone, providing protection that pure copyright-based licenses lack
- The competitive use restriction in Fair Source licenses addresses the rewrite threat by targeting use cases, not just copying

## Synthesis
The intersection of AI and software licensing is creating genuine legal uncertainty that every software company with a public codebase now faces. Sentry's Chad Whitacre and Gavin Zee identify three distinct AI-driven threats to traditional licensing models and argue that Fair Source licensing is structurally better positioned to survive them than alternatives.

The first threat is training without consent. Large language models are trained on vast public code repositories without necessarily complying with the license conditions of that code. The "fair use" doctrine might permit this in the United States, but the legal question remains genuinely unresolved. For permissive licenses that rely on copyright attribution requirements, AI training effectively makes those requirements unenforceable in practice.

The second threat is the easy rewrite. The Cloudflare example is instructive: using agentic coding tools, Cloudflare recreated Next.js—a substantial, mature JavaScript framework—in approximately one week and licensed the result under different terms. A similar exercise recently relicensed a Python library from LGPL to MIT. When the technical barrier to reimplementation collapses, licenses protecting against direct copying provide diminishing protection. The question becomes not "can you copy this?" but "can you reimplement this from scratch quickly enough to make copying irrelevant?"

The third threat undermines enforcement itself. The Supreme Court's refusal to extend copyright protection to AI-generated material means that code produced purely by AI cannot be copyrighted. Any license predicated on copyright exclusivity faces an erosion challenge as AI-generated contributions become difficult to distinguish from human-authored ones.

Fair Source's response to all three threats rests on a non-compete clause rather than pure copyright protection. The restriction is on competitive use—running a competing service using the licensed software—rather than on copying or redistribution. This target-the-use-case approach remains enforceable even when underlying copyright protections are circumvented, and it remains relevant even when a competitor reimplements functionality from scratch, because the restriction follows the competitive purpose rather than the specific code.
