# Vibe coding : distinguons les usages, repensons les organisations
**Source**: https://www.journaldunet.com/developpeur/1550573-vibe-coding-distinguons-les-usages-repensons-les-organisations/
**Date**: May 26, 2026
**Author**: Mickael Peyrot, INSIGN
**Keywords**: vibe coding, AI-assisted development, Cursor, Claude Code, Codex, Lovable, prototyping, software engineering, organizational design, technical debt

## Elevator pitch
Vibe coding, popularized by Andrej Karpathy, has split into two distinct paradigms — technical vibe coding with AI-augmented IDEs and product vibe coding via no-code platforms — but without coherent organizational adaptation, both risk producing fragile prototypes rather than production-ready products.

## Takeaways
- Vibe coding splits into two modes: technical (Cursor, Claude Code, Codex) for developers retaining code visibility, and product (Lovable, Base44) for non-technical users building prototypes from prompts.
- Without a formalized design system, vibe-coded interfaces quickly become visually incoherent and time-consuming to iterate.
- The prototype-turned-product trap is the biggest risk: functional-appearing but fragile code with no architectural vision, creating costly maintenance debt.
- Refactoring remains essential even with AI — LLMs can assist with restructuring, but the discipline of pausing to address technical debt is still a human responsibility.
- Security is a blind spot: LLMs generate functional code, not secure code; vibe-coded apps with exposed tokens are increasingly being hacked.
- Organizational models must evolve: Doctolib has product owners pushing AI-generated code reviewed by lead developers, and tools like Figma integration, Google Stitch, and Claude Design bridge the design-code gap.

## Synthesis
Mickael Peyrot of INSIGN provides a nuanced analysis of the vibe coding phenomenon, moving beyond Karpathy's original viral definition to distinguish two fundamentally different use cases. Technical vibe coding — using AI-augmented IDEs like Cursor, Claude Code, or Codex — serves experienced developers who maintain full visibility over generated code and calibrate AI autonomy deliberately. Product vibe coding — via platforms like Lovable, Base44, or Bolt — targets founders and product owners who want to transform ideas into functional prototypes without traditional development cycles.

The article identifies four critical failure modes common to both approaches. First, design coherence: without a pre-existing design system and reusable component logic, iterating on screens through prompts alone becomes imprecise and produces visually inconsistent interfaces disconnected from brand identity. Second, the prototype-to-product trap: features accreted through successive, sometimes contradictory prompts produce code that appears functional but is architecturally fragile, difficult to maintain, and expensive to evolve. Third, the eternal refactoring gap: the intoxicating speed of vibe coding leads teams to skip necessary pauses for restructuring and optimization — even though LLMs can themselves assist with refactoring. Fourth, security negligence: LLMs prioritize functionality over security, and without expert review (AI-assisted or otherwise), apps ship with exposed tokens and vulnerable patterns that attackers increasingly exploit.

The tooling landscape is responding. AI-native companies are integrating with design tools (Figma), adding rapid prototyping capabilities (Google Stitch, Anthropic's Claude Design), and building dedicated security products. No-code platforms now expose generated source code for editing. But Peyrot argues the real challenge transcends tools: organizations designed around pre-AI workflows must fundamentally restructure. He cites Doctolib as an early adapter — product owners generate AI-assisted code that lead developers review and validate, compressing traditional role boundaries.

The article's core thesis is that vibe coding demands a rethinking of production models, role distribution, and team structure. The question is no longer purely technical — organizations face "massive decrochage" (massive drop-off) if they fail to evolve.
