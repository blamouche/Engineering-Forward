# Open-Sourcing Harvey's Long Horizon Legal Agent Benchmark
**Source**: https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
**Date**: May 6, 2026
**Author**: Niko Grupen, Gabe Pereyra, Julio Pereyra (Harvey)
**Keywords**: legal AI, agent benchmark, Harvey, LAB, legal agent, long-horizon tasks, open-source, law firms, evaluation, practice areas

## Elevator pitch
Harvey open-sourced its Legal Agent Benchmark (LAB), a comprehensive evaluation framework with over 1,200 agent tasks across 24 legal practice areas, designed to measure how well AI agents can perform real-world, long-horizon legal work — from navigating client matters to producing review-ready deliverables.

## Takeaways
- LAB includes 1,250+ agent tasks across 24 legal practice areas, evaluated by 75,000+ expert-written rubric criteria, mirroring how work is assigned, performed, and reviewed at large law firms
- The benchmark uses a "client matter-centric" structure: agents receive loose instructions, must navigate a closed-universe file system of documents, and produce reviewable legal deliverables — not just answer questions
- Tasks are graded on an "all-pass" basis: every criterion must pass, reflecting how high-stakes legal work is reviewed in practice (a report missing one of ten risks is not 80% useful, it's materially incomplete)
- LAB is intentionally launched without a leaderboard to allow community input before publishing baseline scores, with results expected in the coming weeks
- The benchmark is designed to help law firms measure ROI on AI investments by identifying where agents can do all, some, or none of a task, enabling responsible deployment decisions

## Synthesis
Harvey's release of the Legal Agent Benchmark (LAB) marks a significant milestone in the evaluation of AI systems for professional legal work. Unlike previous legal benchmarks — such as LegalBench, CUAD, or Harvey's own BigLaw Bench — which focused on short-horizon reasoning tasks like reading a contract and answering specific questions, LAB is designed to test whether an agent can complete entire legal work assignments end-to-end.

The benchmark's architecture deliberately mirrors the workflow of a large law firm. Each task begins with a short instruction from a "partner" (averaging just fifty words), gives the agent access to a client matter containing relevant and irrelevant documents, and requires the agent to produce a reviewable work product. This structure tests capabilities that go far beyond legal knowledge: the agent must discover which files matter, build context across documents, synthesize information, and produce professional deliverables. One example task involves analyzing change-of-control provisions for a fictional $458 million M&A deal, requiring the agent to navigate a virtual data room with eight material contracts plus adjacent documents, then produce a deal-team memo with an executive summary, risk mapping, contract-by-contract analysis, severity ratings, and mitigation recommendations.

The evaluation methodology is equally rigorous. Each task is graded against expert-written rubrics that break down what partners and clients would scrutinize into atomic, binary pass/fail criteria. The change-of-control task alone has 57 criteria covering nine legal issues. Critically, Harvey enforces "all-pass grading" — a task is marked complete only if every criterion passes. This philosophy reflects real legal practice: a deal-team report that identifies eight of ten risks is not 80% useful; the missing issues could change deal economics or surface as problems after closing.

The 24 practice areas covered in this initial release span transactional, advisory, regulatory, and litigation work. While not exhaustive, they represent the types of tasks associates regularly encounter. Harvey plans to expand coverage to all BigLaw practice areas, in-house legal work, and adjacent professional services domains like asset management and banking.

The timing is strategic. Just as coding benchmarks like SWE-Bench Pro and Terminal-Bench 2.0 served as leading indicators of when coding agents became practically useful, LAB aims to provide the same legible index for legal work. Harvey explicitly positions the benchmark as a tool for law firms to understand where agents are capable, where they struggle, and how to deploy them responsibly. By open-sourcing LAB, Harvey invites model providers, startups, researchers, and law firms to run the benchmark, audit the rubrics, and contribute new task families. The absence of an initial leaderboard reflects a deliberate choice to work with the community before publishing results — an approach that prioritizes accuracy and fairness over immediate competitive positioning. As legal AI tools proliferate and law firms face increasing pressure to demonstrate ROI on technology investments, LAB provides a shared, transparent foundation for measuring progress.
