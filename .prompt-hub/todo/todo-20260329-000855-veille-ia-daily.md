# Todo 20260329-000855 - veille-ia-daily

## Objective
- Run daily veille IA pipeline: fetch Gmail label 0---veille-ia, extract article URLs, update LIST.md per add-url rules, prune non-AI/app-dev URLs, and trash processed emails.

## Plan
1. Ensure repo is clean; if not, commit+push all pending changes to restore clean state.
2. Fetch Gmail messages with label 0---veille-ia, extract article URLs, and dedupe.
3. Run add-url workflow to append URLs to LIST.md, then remove non-AI/app-dev URLs.
4. Trash processed Gmail messages.
5. Update prompt-hub logs/version/releases and summarize.

## Progress
- [ ] Validate clean repo / commit pending work if needed.
- [ ] Fetch Gmail messages + extract URLs.
- [ ] Update LIST.md via add-url + prune non-AI/app-dev URLs.
- [ ] Trash processed emails.
- [ ] Update prompt-hub memory/version/releases + finalize summary.

## Review
- Status: pending
- Notes:
- Plan auto-approved for cron execution.
