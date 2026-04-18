# Migrate a Legacy Codebase with Sandbox Agents

**Source**: https://developers.openai.com/cookbook/examples/agents_sdk/sandboxed-code-migration/sandboxed_code_migration_agent
**Date**: April 19, 2026
**Author**: Unknown
**Keywords**: developers, migrate, legacy, codebase, with, sandbox, agents

## Elevator pitch
Code modernization never really ends. Outdated dependencies, security risks, compliance pressure, and legacy patterns keep accumulating acro.

## Takeaways
- Copy Page More page actions Copy Page More page actions Apr 7, 2026 Migrate a Legacy Codebase with Sandbox Agents KK Konstantine Kahadze (OpenAI) View on GitHub Download raw Code modernization never really ends.
- Outdated dependencies, security risks, compliance pressure, and legacy patterns keep accumulating across large codebases, and one massive migration PR is hard to review and risky to merge.
- A code-migration agent should work in a controlled environment, one scoped task at a time: inspect the relevant repo, edit files, run checks, and return a patch.
- This cookbook uses the Agents SDK with the harness outside the sandbox: orchestration stays in the trusted host process, while shell commands and file edits run in isolated execution environments.
- This separation lets the host harness use secrets, tools, and external services while giving the sandbox only the files and commands needed for the task.

## Synthesis
Copy Page More page actions Copy Page More page actions Apr 7, 2026 Migrate a Legacy Codebase with Sandbox Agents KK Konstantine Kahadze (OpenAI) View on GitHub Download raw Code modernization never really ends. Outdated dependencies, security risks, compliance pressure, and legacy patterns keep accumulating across large codebases, and one massive migration PR is hard to review and risky to merge. A code-migration agent should work in a controlled environment, one scoped task at a time: inspect the relevant repo, edit files, run checks, and return a patch. This cookbook uses the Agents SDK with the harness outside the sandbox: orchestration stays in the trusted host process, while shell commands and file edits run in isolated execution environments. This separation lets the host harness use secrets, tools, and external services while giving the sandbox only the files and commands needed for the task. By the end of this cookbook, you’ll be able to: Keep the agent harness outside the execution environment that runs shell commands and file edits Segment a modernization job into task-sized repo shards Validate each shard with tests, checks, artifacts, and an audit log Swap sandbox providers without rewriting the agent The example is a two-service code migration. Each service runs in its own sandbox and returns its own patch bundle, the same shape you could use to open separate pull requests for review and CI. In each sandbox, the agent migrates an OpenAI client wrapper from Chat Completions to the Responses API . Along the way it runs tests, patches the app and tests, runs a compile check, reruns tests, and returns a typed migration report with a patch. We’ll run the sandbox with Docker locally.
