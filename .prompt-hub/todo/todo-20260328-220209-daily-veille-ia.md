# Task: daily veille IA (cron)

## Plan
1. Confirm repo clean state; if not, commit/push all local changes.
2. Pull Gmail messages with label:0---veille-ia and extract/normalize article URLs.
3. Filter to AI/app-dev links; update LIST.md with dedupe per add-url rules.
4. Remove non-AI/app-dev URLs from LIST.md.
5. Commit/push with prompt-hub version/release updates, then trash processed Gmail messages.

## Status
- [x] Completed

## Notes
- Cron run requested; proceeding without interactive check-in.
- Gmail label returned 0 messages; no LIST.md changes.

## Review
- No URLs added or removed; no emails trashed (none found).
