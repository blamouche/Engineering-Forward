# Todo - daily veille ia extraire urls gmail

- [x] Load prompt-hub context (lessons, memory, releases, agents)
- [x] Inspect repo state
- [x] Search Gmail label `0---veille-ia`
- [x] Normalize/filter URLs and update `LIST.md`
- [x] Trash processed emails
- [x] Update prompt-hub logs/version/release notes, commit and push

## Notes
- Cron run started around 2026-04-23 06:07 Europe/Paris.
- If the repo is not clean, commit+push all pending local changes before applying add-url sync.

## Review
- Extracted 2 relevant Sifted URLs and added them to `LIST.md` after dedupe.
- Removed 0 off-topic URLs because the queue was empty before the run.
- Trashed 1 processed Gmail message.
