# Todo — veille IA extraire URLs Gmail

- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier l'état du repo et `LIST.md`
- [x] Chercher les emails Gmail `label:0---veille-ia` *(échec: `gog` -> `invalid_grant`)*
- [ ] Extraire les URLs d'articles IA/dev *(bloqué par l'auth Gmail)*
- [ ] Mettre à jour `LIST.md` via le workflow add-url (sync/dedupe/commit/push) *(non exécuté)*
- [ ] Supprimer les URLs non IA/dev restantes dans `LIST.md` *(non exécuté)*
- [ ] Mettre à la corbeille les emails traités *(non exécuté)*
- [x] Mettre à jour prompt-hub (`memory`, `version`, `releases`) et finaliser

## Review
- Exécution bloquée: `gog gmail messages search 'label:0---veille-ia' --max 100 --json --no-input` renvoie `oauth2: "invalid_grant" "Token has been expired or revoked."`.
- Repo déjà propre côté contenu métier: `LIST.md` est vide, aucun URL ajouté/supprimé, aucun email traité.
