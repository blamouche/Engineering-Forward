# Todo - daily veille ia extraire urls gmail

## Context
- Requested by cron on 2026-04-23 20:01 Europe/Paris.
- Goal: search Gmail label `0---veille-ia`, extract article URLs, update `LIST.md` with clean sync/dedupe/filtering, trash processed emails, and report counts.

## Plan
- [x] Inspect repo state and restore a clean synced baseline if needed.
- [x] Search Gmail messages for the veille label and extract candidate URLs.
- [x] Filter to AI/app-dev relevant URLs, dedupe, and update `LIST.md`.
- [x] Remove off-topic URLs from `LIST.md`.
- [x] Trash processed emails.
- [x] Update prompt-hub trace files, commit, and push.

## Review
- Repo sync préalable effectué via commit/push des tâches locales non synchronisées.
- 1 URL pertinente ajoutée à `LIST.md`.
- 0 URL hors sujet supprimée de `LIST.md`.
- 1 email Gmail traité puis mis à la corbeille.
