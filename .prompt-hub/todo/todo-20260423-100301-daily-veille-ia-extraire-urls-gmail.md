# Todo - daily veille ia extraire urls gmail

## Context
- Scheduled cron run on 2026-04-23 10:03 Europe/Paris.
- Goal: extract article URLs from Gmail label `0---veille-ia`, update `LIST.md` via add-url workflow, remove off-topic URLs, trash processed emails, and keep prompt-hub traceability/versioning up to date.

## Plan
- [x] Check repo cleanliness and sync requirements
- [x] Fetch Gmail messages from veille IA labels and extract candidate URLs
- [x] Filter to AI / app-dev URLs, dedupe, and update `LIST.md`
- [x] Trash processed emails
- [x] Update prompt-hub memory/version/releases and commit/push

## Review
- Gmail labels `0---veille-ia` and `0 - Veille/IA` both returned 0 message.
- `LIST.md` remained unchanged and already empty.
- No emails were trashed.
