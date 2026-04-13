# Todo — veille-ia-extraire-urls-gmail

- [x] Read required prompt-hub context (`lessons.md`, `memory.md`, `releases.md`) and repo instructions.
- [x] Check repo status and current `LIST.md` state.
- [x] Attempt Gmail search on label `0---veille-ia`.
- [x] Stop execution because Gmail access is blocked by `gog` OAuth `invalid_grant`.
- [x] Leave `LIST.md` unchanged and do not trash any email.
- [x] Log the failed scheduled run for traceability.

## Review
- Gmail extraction could not run because `gog gmail messages search 'label:0---veille-ia' --json --no-input` returned `oauth2: "invalid_grant" "Token has been expired or revoked."`
- Repo was already clean/synced when checked.
- `LIST.md` was empty before and after the run.
- No URL was added.
- No URL was removed.
- No email was trashed.
