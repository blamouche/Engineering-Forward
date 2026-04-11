# Todo — veille-ia-extraire-urls-gmail

- [x] Lire `.prompt-hub/lessons.md`
- [x] Lire `.prompt-hub/memory.md`
- [x] Lire `.prompt-hub/releases.md`
- [x] Vérifier l’état du repo et le remettre propre/synchronisé si nécessaire
- [x] Chercher les emails Gmail `label:0---veille-ia` *(échec OAuth `invalid_grant`)*
- [ ] Extraire les URLs d’articles AI/app-dev *(bloqué : Gmail inaccessible)*
- [ ] Mettre à jour `LIST.md` avec déduplication et nettoyage des URLs non pertinentes *(bloqué : aucune URL extraite)*
- [ ] Mettre à la corbeille les emails traités *(bloqué : Gmail inaccessible)*
- [x] Mettre à jour les logs prompt-hub (memory/version/releases)
- [x] Commit + push

## Review
- Run bloqué par `gog` Gmail : `invalid_grant` (`Token has been expired or revoked`).
- Aucun email lu, aucune URL ajoutée, aucune URL supprimée, aucun email mis à la corbeille.
- Le repo a été nettoyé en commitant/poussant les logs de ce run pour revenir à un état synchronisé.
