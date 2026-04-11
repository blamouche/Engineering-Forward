# Task: Daily veille IA extraire URLs Gmail

## Objective
Exécuter la séquence quotidienne:
1. Chercher les emails Gmail label `0---veille-ia`
2. Extraire les URLs d'articles
3. Ajouter les URLs dans `LIST.md` via le workflow `add-url` (sync propre, dedupe, commit+push)
4. Supprimer de `LIST.md` les URLs non liées à l'IA ou au développement applicatif
5. Mettre à la corbeille les emails traités

## Plan
- [x] Charger le contexte prompt-hub requis
- [x] Créer ce task log
- [x] Vérifier l'état du repo et restaurer un état clean/synced si nécessaire
- [x] Extraire les URLs pertinentes depuis Gmail
- [x] Mettre à jour `LIST.md` avec déduplication et filtrage
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour mémoire/version/releases, commit et push

## Notes
- Timestamp cron: 2026-04-11 04:01 Europe/Paris

## Review
- Gmail label `0---veille-ia` a retourné 0 message.
- Repo déjà clean/synced avant le run; seul le nouveau task log a été créé.
- `LIST.md` inchangé: 0 URL ajoutée, 0 URL supprimée.
- 0 email mis à la corbeille.
- Run journalisé dans prompt-hub avec bump de version/release prévu.
