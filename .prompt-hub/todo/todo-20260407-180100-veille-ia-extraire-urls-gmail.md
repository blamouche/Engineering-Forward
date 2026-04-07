# Veille IA — 2026-04-07 18:01:00

## Objective
Exécuter la séquence quotidienne : extraire les URLs Gmail label `0---veille-ia`, mettre à jour `LIST.md` selon les règles `add-url`, retirer les URLs hors IA/dev applicatif, mettre à la corbeille les emails traités, puis journaliser/versionner.

## Plan
- [ ] Vérifier l’état du repo et le synchroniser proprement si nécessaire
- [ ] Chercher les emails Gmail `label:0---veille-ia` et extraire les URLs candidates
- [ ] Filtrer/normaliser/dédupliquer les URLs pertinentes IA/dev applicatif
- [ ] Mettre à jour `LIST.md` en respectant le workflow `add-url`
- [ ] Supprimer de `LIST.md` les URLs non pertinentes
- [ ] Mettre à la corbeille les emails traités
- [ ] Mettre à jour prompt-hub (memory/version/releases), commit + push

## Notes
- Si le repo n’est pas clean, commit/push toutes les modifs locales non synchronisées avant l’ajout d’URLs.
- Résumé attendu : nombre d’URLs ajoutées/supprimées + statut trash Gmail.
