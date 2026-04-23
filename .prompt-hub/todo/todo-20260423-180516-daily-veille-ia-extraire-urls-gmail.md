# Daily veille IA extraire URLs Gmail

## Objective
Exécuter la veille quotidienne Gmail label `0---veille-ia` et maintenir `LIST.md` propre et synchronisé.

## Plan
- [x] Lire le contexte prompt-hub requis.
- [ ] Vérifier/synchroniser l'état git du repo.
- [ ] Lire les emails Gmail `label:0---veille-ia` (et fallback historique si besoin).
- [ ] Extraire, normaliser, dédupliquer et filtrer les URLs AI/app-dev.
- [ ] Mettre à jour `LIST.md` et supprimer les URLs hors sujet.
- [ ] Mettre à la corbeille les emails traités.
- [ ] Mettre à jour version, releases, mémoire, puis commit+push.

## Notes
- Si le repo n'est pas clean, commiter/pusher toutes les modifs locales non synchronisées avant de toucher `LIST.md`.
- Conserver `LIST.md` en texte brut, une URL par ligne.
