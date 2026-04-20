# Daily veille IA extraire URLs Gmail

- Timestamp: 2026-04-20 04:02:15 Europe/Paris
- Goal: traiter les emails Gmail du label `0---veille-ia`, extraire les URLs d'articles, mettre a jour `LIST.md`, filtrer le hors-sujet, puis mettre a la corbeille les emails traites.

## Plan
- [x] Lire les consignes repo (`agents.md`, `.prompt-hub/lessons.md`, `.prompt-hub/memory.md`, `.prompt-hub/releases.md`)
- [x] Verifier l'etat git et restaurer un etat propre/synchronise si necessaire
- [x] Lire les emails Gmail cibles et extraire les URLs candidates
- [x] Mettre a jour `LIST.md` avec dedupe + filtre IA/dev
- [x] Mettre a jour les traces prompt-hub (memory/version/releases)
- [x] Commit + push les changements necessaires
- [x] Mettre a la corbeille les emails traites

## Review
- Gmail `label:0---veille-ia` a retourne 0 message.
- `LIST.md` n'a pas change, donc 0 URL ajoutee et 0 URL supprimee.
- Aucun email a mettre a la corbeille.
- Le repo n'etait pas clean a cause de ce nouveau todo uniquement, donc les traces prompt-hub ont ete commit/push pour revenir a un etat propre.
