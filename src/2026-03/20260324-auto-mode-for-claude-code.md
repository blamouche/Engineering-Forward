# Auto mode for Claude Code
**Source**: https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/
**Date**: March 24, 2026
**Author**: Simon Willison
**Keywords**: Claude Code, permissions, safety, prompt injection, tooling

## Elevator pitch
Simon Willison reviews Claude Code’s new auto‑mode permissions, highlighting its classifier‑based safeguards while questioning AI‑driven defenses against prompt injection.

## Takeaways
- Auto mode lets Claude decide permissions on the user’s behalf with a safety classifier.
- The classifier runs on Claude Sonnet 4.6, independent of the main model.
- Default rules include explicit allow/deny lists for local operations, installs, and destructive git actions.
- Willison argues AI‑based guardrails remain non‑deterministic and imperfect.
- He prefers deterministic sandboxing over prompt‑based protections.

## Synthesis
Simon Willison’s post examines Claude Code’s new “auto mode,” a permissions setting that removes frequent approval prompts by delegating permission decisions to a classifier model. The core promise is convenience: Claude can proceed without constant user confirmation, while safeguards check each action before execution. According to the documentation, those safeguards are implemented by a separate model (Claude Sonnet 4.6) that evaluates intent and blocks actions that exceed scope or target untrusted infrastructure.

Willison digs into the default rule set by running the `claude auto-mode defaults` command and inspecting the JSON output. The allow list covers items like local file operations within the project scope, read‑only operations, and dependency installs that are already declared in manifest files. Importantly, the rules treat the repository the session started in as the trusted scope; moves outside that scope (like wandering into system directories) are considered escalation. The soft‑deny list includes force pushes, direct pushes to default branches, and executing code fetched from external sources, reflecting a bias toward preserving review gates and mitigating supply‑chain risk.

The post’s main critique is that AI‑based prompt‑injection defenses are inherently non‑deterministic. While the system’s classifier may block many risky actions, it can still allow dangerous operations when user intent is ambiguous or the environment context is incomplete. Willison notes that allowing `pip install -r requirements.txt` is not sufficient to prevent dependency poisoning—untrusted packages can still be pulled in if the requirements file is compromised or unpinned. He cites a recent real‑world incident as an example of that risk.

Willison’s conclusion is pragmatic: auto mode is an interesting step toward reducing permission friction, but he does not consider it a full solution for agent safety. His preferred mitigation is deterministic sandboxing that restricts file access and network connections by default. In his view, such sandboxing provides stronger guarantees than AI‑driven classifiers, which can fail in unpredictable ways.

Overall, the post provides a clear overview of how auto mode works, surfaces its default rules, and frames the feature within a broader safety conversation. It highlights the tension between usability (fewer prompts) and security (strong, deterministic boundaries), and it argues that the best approach likely combines guardrails with robust sandbox isolation rather than relying solely on AI‑based intent checks.
