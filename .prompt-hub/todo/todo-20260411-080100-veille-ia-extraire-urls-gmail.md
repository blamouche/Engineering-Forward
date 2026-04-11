# Todo — 2026-04-11 08:01:00 — veille-ia-extraire-urls-gmail

## Objective
Exécuter la veille IA quotidienne : chercher les emails Gmail label `0---veille-ia`, extraire les URLs d'articles, mettre à jour `LIST.md`, retirer les URLs non pertinentes, puis mettre à la corbeille les emails traités.

## Plan
- [x] Lire les consignes du repo (`agents.md`, `.prompt-hub/lessons.md`, `.prompt-hub/memory.md`, `.prompt-hub/releases.md`).
- [x] Vérifier l'état Git du repo et le contenu actuel de `LIST.md`.
- [x] Chercher les messages Gmail avec le label `0---veille-ia`.
- [x] Si des emails sont trouvés, extraire/normaliser les URLs pertinentes, dédupliquer, mettre à jour `LIST.md`, puis supprimer les URLs hors IA/dev applicatif.
- [x] Mettre à la corbeille les emails traités si applicable.
- [x] Mettre à jour les journaux prompt-hub, version, releases, puis commit/push.

## Notes d'exécution
- `git status --short --branch` : repo déjà propre et synchronisé.
- `LIST.md` était vide au départ.
- `gog gmail messages search 'label:0---veille-ia' --max 50 --json --include-body --no-input` a retourné 0 message.
- Aucun email à traiter, donc aucune URL à ajouter/supprimer et aucun email à mettre à la corbeille.

## Review
- Run sans changement fonctionnel sur `LIST.md`.
- Le repo reste propre; seuls les fichiers de traçabilité prompt-hub sont mis à jour.
- Résultat : 0 URL ajoutée, 0 URL supprimée, 0 email traité/archivé à la corbeille.
