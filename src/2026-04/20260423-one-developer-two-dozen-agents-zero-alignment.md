# One Developer, Two Dozen Agents, Zero Alignment

**Source**: https://maggieappleton.com/zero-alignment
**Date**: April 23, 2026
**Author**: Maggie Appleton
**Keywords**: agents, software teams, coordination, GitHub Next, collaboration, developer tools

## Elevator pitch
Maggie Appleton argues that agentic development will fail if teams only scale individual output, because the real bottleneck is shared context and alignment before code gets generated.

## Takeaways
- The essay criticizes the fantasy that one developer with many agents can replace the coordination work of a team.
- As implementation gets cheaper, choosing the right work and aligning on it becomes more important and more fragile.
- Pull requests and issues are described as outdated primitives for a world of fast, parallel agent output.
- Appleton highlights how business context, politics, user insight, and product vision live outside the codebase.
- Her Ace prototype explores multiplayer prompting and shared cloud workspaces as a better surface for collaborative agent work.

## Synthesis
Maggie Appleton’s argument lands because it targets the weakest assumption in a lot of agent hype. The fantasy is simple: if one engineer can supervise a wall of coding agents, software output will scale linearly. Her critique is that software has never been bottlenecked only by typing speed. Teams fail because they build the wrong thing, duplicate work, collide in the same files, or discover too late that nobody agreed on the plan. Agents reduce implementation cost, which means those alignment failures get amplified rather than solved.

That is why her attack on the “single-player interface” matters. Many current tools are optimized for one operator delegating work privately, then pushing the result into a PR once the code already exists. But when agent output becomes cheap and abundant, the pull request is carrying too much weight. It becomes the place where planning, review, and coordination all collapse into one late-stage checkpoint. Appleton argues that this is the wrong primitive for the next phase of software development.

Her deeper point is that most of the important context for building software does not live in repositories. It lives in people’s heads and in organizational systems: goals, constraints, user pain, political ownership, and previous decisions. Agents cannot infer that reliably on their own. If the tooling does not make it easy for humans to surface that context early and continuously, teams will generate more code but not necessarily more value.

The Ace prototype she describes is one answer: multiplayer sessions, shared sandboxes, visible prompting history, and a common workspace where PMs, designers, and engineers can shape the work together while agents execute. Even if Ace itself is just a prototype, the framing feels right. The next generation of developer tools probably needs to optimize less for solo coding velocity and more for collective alignment around fast, agent-assisted execution.
