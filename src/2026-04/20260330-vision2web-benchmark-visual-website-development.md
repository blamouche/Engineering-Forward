# Vision2Web: A Hierarchical Benchmark for Visual Website Development
**Source**: https://github.com/zai-org/Vision2Web
**Date**: March 30, 2026
**Author**: Zehai He, Wenyi Hong, Zhen Yang, Ziyang Pan, Mingdao Liu, Xiaotao Gu, Jie Tang
**Keywords**: benchmark, multimodal, web development, coding agents, visual evaluation, frontend, fullstack

## Elevator pitch
Vision2Web is a 193-task hierarchical benchmark evaluating multimodal coding agents on web development across three difficulty levels — static pages, interactive frontends, and full-stack systems — with 918 prototype images and 1,256 functional test cases.

## Takeaways
- Three progressive difficulty levels: static webpage (from mockups), interactive frontend (multi-page with navigation), full-stack website (backend logic)
- 193 tasks across 16 subcategories in 4 domains: E-Commerce, SaaS, Content, and Public Service
- Evaluation combines Visual Score (VLM-based) and Functional Score (GUI automation agents)
- 918 prototype images and 1,256 functional test cases for comprehensive coverage
- Supports implementation-agnostic evaluation across different coding agent frameworks

## Synthesis
Vision2Web addresses a gap in existing coding agent benchmarks: the inability to evaluate visual understanding as an input to code generation. Most coding benchmarks provide text-based specifications and evaluate text-based or executable outputs. Web development tasks typically start with visual mockups — design prototypes, screenshots of desired interfaces, wireframes — and require agents to translate visual specifications into working code.

The three-level difficulty progression reflects the actual complexity spectrum in web development. Level 1 (static webpages from mockups) tests the core visual-to-code translation capability: given an image of what a page should look like, generate HTML/CSS that produces the specified layout across device sizes. Level 2 adds navigation and multi-page interactions, testing whether agents can maintain consistency across pages and implement the functional behaviors that connect them. Level 3 adds backend logic, testing whether agents can bridge frontend interfaces with data persistence and server-side processing.

The combined evaluation approach — Visual Score from vision language models plus Functional Score from GUI automation testing — is well-suited to web development assessment. Functional correctness (does the form submission work?) and visual fidelity (does the page look like the mockup?) are both necessary for a quality web application; an agent that produces functionally correct but visually wrong code, or vice versa, has not solved the problem.

The 918 prototype images provide a meaningful visual evaluation corpus. For meaningful visual scoring, the evaluation needs sufficient diversity of layouts, color schemes, and component types to prevent overfitting to specific visual patterns. Covering four major domains (E-Commerce, SaaS, Content, Public Service) with 16 subcategories provides this diversity.

For research on multimodal coding agents, Vision2Web provides a standardized evaluation framework. For practitioners evaluating AI coding tools for web development use cases, the benchmark provides a systematic way to compare agent performance on representative tasks rather than relying on informal testing.
