# Task: substack-post-recents

- Created: 2026-04-19 16:34:00 Europe/Paris
- Agent: substack-post-recents
- Objective: Create the recents Substack post from the 15 most recent README articles, copy it to substack/latest.md, then commit and push all required prompt-hub updates.

## Plan
- [x] Sync repo and inspect current status
- [x] Collect the 15 most recent article files from README and review them
- [x] Draft the Substack article and save it to substack/YYYYMMDD-post-<slug>.md
- [x] Copy the article to substack/latest.md
- [x] Update prompt-hub files, commit, and push

## Notes
- Assumption: use current date 20260419 for the Substack filename because the agent instruction for recents does not pin an article date.
- To keep the repo safe, unrelated local changes were stashed before the pull/rebase step.

## Review
- Drafted `substack/20260419-post-the-real-ai-race-is-moving-behind-the-interface.md` and copied it to `substack/latest.md`.
- Article theme: the real AI race is shifting from chat interfaces to operational infrastructure, agent-executable systems, and compute constraints.
- Completed: version bump and prompt-hub log updates prepared, commit/push executed, then the pre-existing local stash was restored.
