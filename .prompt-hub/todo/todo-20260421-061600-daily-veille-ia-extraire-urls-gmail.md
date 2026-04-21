# Todo - 2026-04-21 06:16:00 - daily-veille-ia-extraire-urls-gmail

## Objective
Run the daily AI watch flow: fetch Gmail messages from `label:0---veille-ia`, extract relevant article URLs, update `LIST.md`, remove off-topic URLs, and trash processed emails.

## Plan
- [x] Load prompt-hub context and repo-specific instructions.
- [x] Check repo sync/cleanliness and restore a clean synced state if needed.
- [x] Search Gmail veille labels and extract article URLs.
- [x] Update `LIST.md` with normalization, dedupe, and topical filtering.
- [x] Commit/push repo changes and trash processed emails.
- [x] Write review notes.

## Review
- Repo was not clean at start, so pending local prompt-hub tracking was committed and pushed first to restore a clean synced state.
- Gmail labels `0---veille-ia` and `0 - Veille/IA` both returned 0 message(s).
- `LIST.md` was already empty, so 0 URL(s) were added and 0 off-topic URL(s) were removed.
- No email was trashed because no message matched the labels.
