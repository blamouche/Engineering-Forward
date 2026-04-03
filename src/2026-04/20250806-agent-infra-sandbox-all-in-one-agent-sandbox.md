# AIO Sandbox: All-in-One Sandbox Environment for AI Agents
**Source**: https://github.com/agent-infra/sandbox
**Date**: August 6, 2025
**Author**: agent-infra
**Keywords**: AI agents, sandbox, Docker, browser automation, shell, MCP, VSCode Server, Jupyter, security isolation

## Elevator pitch
AIO Sandbox is a single Docker container that provides AI agents with a complete, isolated execution environment including browser, shell, filesystem, VSCode Server, Jupyter, and MCP support.

## Takeaways
- Single Docker container bundles browser, terminal, file system, VSCode Server, Jupyter, and MCP capabilities for AI agents
- Deployed with a single docker run command, minimal setup required
- Available as Python package (agent-sandbox) and npm package (@agent-infra/sandbox)
- Supports both self-hosted deployment and managed API access
- Published research paper (arxiv.org/pdf/2509.02544) documenting the sandbox architecture

## Synthesis
The AIO Sandbox addresses a fundamental challenge in AI agent deployment: agents that can interact with web browsers, execute shell commands, read and write files, and run code need a secure, isolated environment to do so safely. Without sandboxing, an agent with these capabilities poses serious security risks — both from the agent's own potential errors and from adversarial inputs that might exploit its capabilities.

The all-in-one approach is the key design decision. Rather than requiring teams to compose separate containerized services for browser automation (typically Playwright or Selenium), shell execution, file access, and IDE integration, AIO Sandbox packages all of these into a single container with a unified interface. This dramatically simplifies the infrastructure required to run capable AI agents: a single `docker run` command brings up a complete execution environment.

The inclusion of MCP (Model Context Protocol) support is particularly relevant in the current ecosystem. MCP has emerged as a standard protocol for AI models to interact with external tools and data sources. By building MCP support directly into the sandbox, AIO Sandbox positions itself as compatible with the growing ecosystem of MCP-enabled AI tools, rather than requiring custom integration work.

VSCode Server inclusion deserves attention: this is not just a code editor, but a development environment with extension support, terminal access, and language server integration. For AI agents tasked with software development work, having a proper IDE environment rather than just a shell means access to the same tooling that human developers use — syntax highlighting, intellisense, debugging — which may improve code quality.

The research paper documentation is a sign of maturity: the team has thought systematically about the architecture and its tradeoffs, and has published their approach for peer review. For teams evaluating sandboxing solutions, a published paper provides a level of design documentation that most open-source projects lack.

The primary constraint is the `--security-opt seccomp=unconfined` flag required for the Docker run command, which disables the default seccomp security profile. This is necessary for some of the sandbox's capabilities but represents a security tradeoff that teams should evaluate against their threat model before deploying in sensitive environments.
