# The Next Big Programming Language Is English
**Source**: https://every.to/chain-of-thought/i-spent-24-hours-with-github-copilot-workspaces
**Date**: May 2, 2024
**Author**: Dan Shipper
**Keywords**: GitHub Copilot Workspace, agentic coding, natural language programming, developer workflow

## Elevator pitch
A field report from 24 hours with GitHub Copilot Workspace, arguing that agent‑style tools turn English into the new programming interface.

## Takeaways
- Copilot Workspace reframes coding as describing outcomes in natural language.
- The tool builds a plan and specification before writing code, enabling structured delegation.
- Success depends on providing clear context, constraints, and desired behavior.
- Agentic workflows excel on defined tasks but still require human supervision.
- The trend points toward programming as conversation plus verification.

## Synthesis
This essay documents a hands‑on experiment with GitHub Copilot Workspace (CW), a preview product that turns natural language tasks into full coding workflows. Dan Shipper compares Copilot’s traditional autocomplete to Workspace’s agent‑like approach: the user describes the outcome, the tool maps the codebase, proposes a plan, and then implements changes under supervision. The experience suggests a shift toward “English as the programming language,” where the human’s role is to articulate intent and evaluate results rather than write every line.

Shipper tests CW on a real but manageable task: replacing an ugly placeholder logo in an internal tool. The task is intentionally small but nuanced—common in real codebases and easy to procrastinate on—making it a good barometer for agentic programming. The key difference from a standard chat‑based LLM is CW’s structured flow. It begins by building a specification: a plain‑language description of what the code should look like after the change. This effectively acts as acceptance criteria. Next, CW produces a plan that details the edits it intends to make across files, bringing the agent’s reasoning into a reviewable form before execution.

The essay highlights that success with CW depends on precision in the task description. When prompts include specifics—file names, exact placement, visual constraints—the model performs better. This mirrors a broader trend in agentic development: the more explicit the intent and constraints, the more reliable the output. CW’s workflow also underscores that “planning” is now an explicit step in AI‑assisted coding, allowing humans to validate logic before code is changed.

While the experiment is optimistic, it’s not a claim of full automation. Shipper notes that the agent still needs human oversight: reviewing the plan, validating diffs, and checking for unintended side effects. It’s capable, but not autonomous enough to skip review. The value is speed and cognitive relief—offloading tedious tasks and scaffolding work—but the responsibility for correctness remains with the human developer.

The essay situates CW among other agentic tools like Devin and Claude Code, suggesting a near‑term future where developers ask for features in natural language, approve a plan, and then watch the agent implement. This workflow compresses the feedback loop for common tasks and reduces the friction of context switching. It also hints at a new skill: the ability to express technical intent clearly and to evaluate plans rather than just code.

Overall, the piece argues that the biggest change is not the quality of generated code, but the interface itself. Programming is becoming a conversational activity supported by planning, specification, and delegation. CW is a concrete example of how this shift will reshape daily engineering work, moving developers closer to a role of product and system reasoning while AI handles the execution details.
