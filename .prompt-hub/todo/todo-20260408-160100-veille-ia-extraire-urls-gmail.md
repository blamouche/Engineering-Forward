# Todo 20260408-160100 veille-ia-extraire-urls-gmail

- [x] Read prompt-hub context (`lessons.md`, `memory.md`, `releases.md`).
- [x] Inspect repo state and restore clean synced state if needed.
- [x] Search Gmail label `0---veille-ia` and extract article URLs.
- [x] Update `LIST.md` with normalized/deduped relevant URLs; remove non-AI/app-dev entries.
- [x] Trash processed Gmail messages.
- [x] Update prompt-hub tracking (`memory.md`, `version.md`, `releases.md`) and commit/push.

## Review
- Repo cleanup commit done first to satisfy the clean-tree add-url rule.
- Extracted 16 relevant AI/app-dev URLs from TLDR AI and Unwind AI newsletters.
- `LIST.md` was empty before the run, so net change is +16 URLs and 0 removals.
- Trashed both processed Gmail messages after queue update.
