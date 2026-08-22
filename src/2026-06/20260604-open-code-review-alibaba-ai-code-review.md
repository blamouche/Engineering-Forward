# Open Code Review: Alibaba's AI-Powered Code Review CLI
**Source**: https://github.com/alibaba/open-code-review
**Date**: 2026-05-18
**Author**: Alibaba Group
**Keywords**: code-review, ai, cli, open-source, llm, agent, alibaba, developer-tools, ci-cd

## Elevator pitch
Open Code Review is an open-source CLI tool from Alibaba that combines deterministic engineering pipelines with an LLM agent to produce structured, line-level code review comments — battle-tested at Alibaba's scale with tens of thousands of developers and millions of identified defects.

## Takeaways
- Hybrid architecture: deterministic pipelines handle rule-based checks (NPE, thread-safety, XSS, SQL injection) while an LLM agent with tool-use capabilities handles contextual analysis and generates structured review comments
- Originated as Alibaba's internal AI code review assistant, serving tens of thousands of developers and identifying millions of code defects over two years before open-sourcing
- Supports multiple LLM providers (OpenAI and Anthropic compatible) with configurable model endpoints, plus a Delegation Mode where the coding agent itself performs the review
- Integrates with Claude Code, Codex, Cursor, and OpenCode via plugins, with CI/CD support for GitHub Actions, GitLab CI, and Gerrit
- Built on a real-world benchmark (AACR-Bench) constructed from 50 popular open-source repositories, 200 real pull requests, and 10 programming languages, cross-validated by 80+ senior engineers
- 21,000+ GitHub stars and 1,500+ forks within months of open-sourcing, with 145 contributors and 109 releases as of August 2026

## Synthesis
Open Code Review (OCR) is Alibaba's open-source AI-powered code review CLI tool, incubated from the company's internal AI code review assistant that has served tens of thousands of developers and identified millions of code defects over the past two years. The project was open-sourced in May 2026 and has rapidly gained traction, accumulating over 21,000 GitHub stars.

The tool's core philosophy is combining deterministic engineering with an LLM agent, letting each handle what it does best. Deterministic pipelines handle rule-based checks for common defect patterns including null pointer exceptions, thread-safety issues, XSS, and SQL injection across multiple programming languages. The LLM agent, equipped with tool-use capabilities, reads Git diffs, inspects full file contents, searches codebases for context, and generates structured review comments with line-level precision.

A key differentiator is Delegation Mode, which allows AI coding agents like Claude Code or Codex to perform the review themselves using their own LLM, with OCR handling file selection and rule resolution. This eliminates the need for a separate OCR API key and leverages the coding agent's existing context. The tool also supports traditional CLI usage where OCR runs reviews using its own configured LLM provider.

The project includes AACR-Bench, a real-world code review benchmark built from 50 popular open-source repositories, 200 real pull requests, and 10 programming languages, with 1,505 annotated ground-truth issues cross-validated by 80+ senior engineers. The benchmark measures F1 score, precision, recall, average review time, and token consumption — providing a standardized evaluation framework for AI code review tools.

Integration support is extensive: plugins for Claude Code, Codex, Cursor, and OpenCode allow seamless integration into existing AI coding workflows. CI/CD integration covers GitHub Actions, GitLab CI, GitFlic CI, and Gerrit. The tool is installed via npm and provides commands for workspace review, branch range review, single commit review, and full-file scanning.