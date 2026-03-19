# APM – Agent Package Manager
**Source**: https://github.com/microsoft/apm
**Date**: 2026-03-19
**Author**: Microsoft (danielmeppiel)
**Keywords**: agent package manager, APM, Microsoft, apm.yml, AGENTS.md, CLAUDE.md, MCP servers, transitive dependencies, agent configuration

## Elevator pitch
Microsoft's APM is package.json for AI agents—declare agent dependencies (instructions, skills, prompts, agents, hooks, plugins, MCP servers) in `apm.yml` and teammates get a fully configured agent environment in seconds with transitive dependency resolution.

## Takeaways
- Unified `apm.yml` manifest for all agent configuration: instructions, skills, prompts, agents, hooks, plugins, and MCP servers.
- Transitive dependency resolution similar to npm or pip—declaring one agent dependency automatically installs its dependencies.
- Compiles to multiple agent standard formats: AGENTS.md, CLAUDE.md, .cursor/rules/ for different AI coding tool ecosystems.
- Installation support across GitHub, GitLab, Bitbucket, Azure DevOps, and enterprise git platforms.
- Security scanning for hidden Unicode characters and compromised packages.
- v0.8.2 as of March 2026; 574 stars, 40 forks, 16 contributors.

## Synthesis
APM addresses the "it works on my machine" problem for AI agent configuration. When teams share codebases with AI coding tools, each developer typically sets up their own agent configuration independently—leading to inconsistent behavior, missing context, and time spent on configuration rather than work. APM externalizes this configuration into a version-controlled manifest that makes agent setup reproducible.

The npm/pip analogy is apt and points to where APM's value accrues. Package managers created the reproducible build infrastructure that made software dependency management tractable at scale. The same problem is emerging in AI agent configuration: as agent ecosystems develop composable skills, MCP servers, and specialized prompts, managing these dependencies manually creates the same fragmentation that npm solved for JavaScript. APM's transitive dependency resolution means declaring a high-level agent capability automatically installs everything needed to run it.

The multi-format compilation output (AGENTS.md, CLAUDE.md, .cursor/rules/) addresses ecosystem fragmentation where different AI coding tools use different configuration formats. Rather than maintaining parallel configuration files for each tool, APM maintains a single source of truth and generates the format each tool expects. This is the same abstraction layer that build tools like Webpack provide across browser JavaScript environments.

The security scanning for hidden Unicode characters addresses a real attack vector in the prompt injection era. Agent configuration files that contain invisible control characters or Unicode lookalikes can manipulate model behavior in ways that aren't visible in standard code review. Making this a first-class security feature rather than an afterthought reflects the security context of agent deployment in enterprise environments.
