# Todo - daily-veille-ia-extraire-urls-gmail

## Objective
Traiter les emails Gmail label `0---veille-ia`, extraire les URLs d'articles pertinentes IA/dev applicatif, mettre a jour `LIST.md`, supprimer les URLs hors sujet et mettre a la corbeille les emails traites.

## Plan
- [x] Lire le contexte prompt-hub requis (`lessons.md`, `memory.md`, `releases.md`).
- [x] Verifier les regles du repo et l'etat git.
- [x] Remettre le repo dans un etat clean/synchronise si necessaire.
- [x] Lire les emails Gmail du label `0---veille-ia` et extraire les URLs candidates.
- [x] Mettre a jour `LIST.md` avec dedupe et filtrage IA/dev applicatif.
- [x] Mettre a jour la tracabilite prompt-hub (`memory.md`, `version.md`, `releases.md`, review ci-dessous).
- [x] Commit + push les changements.
- [x] Mettre a la corbeille les emails traites.

## Review
- Gmail label `0---veille-ia` returned 0 message(s).
- `LIST.md` was already empty, so 0 URL(s) were added and 0 URL(s) were removed.
- 0 email(s) were moved to trash.
- Repo was cleaned, synced, then final prompt-hub tracking was committed and pushed.
