# Todo - Daily veille IA extraire URLs Gmail

## Context
- Trigger: cron `Daily veille IA Extraire urls de gmail`
- Objective: search Gmail label `0---veille-ia`, extract article URLs, update `LIST.md` with clean sync/dedupe, remove off-topic URLs, trash processed emails, and report counts.

## Plan
- [x] Read prompt-hub context and repo instructions
- [x] Check git state and restore a clean synced repo if needed
- [x] Search Gmail label and extract candidate URLs
- [x] Update `LIST.md` with normalization, dedupe, and scope filtering
- [x] Update prompt-hub logs/versioning, commit, and push
- [x] Trash processed Gmail emails
- [x] Add review notes

## Notes
- Assume scope includes AI, AI infrastructure, AI product/app development, and broader application engineering content.

## Review
- Repo cleaned first with a dedicated sync commit to satisfy the add-url precondition.
- Gmail label returned 1 message.
- Extracted 22 raw URLs from the newsletter body, resolved redirects, and kept only 1 new in-scope article URL not already covered in the repo: `https://linas.substack.com/p/agenticsingularity`.
- Skipped previously covered URLs and finance-only/off-topic links.
- Added URL to `LIST.md` and trashed the processed email `19da780215cf9744`.
