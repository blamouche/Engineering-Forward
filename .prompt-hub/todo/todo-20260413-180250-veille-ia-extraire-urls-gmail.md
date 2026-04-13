# Todo — veille IA extraire URLs Gmail

## Objective
Exécuter la séquence quotidienne :
1. Chercher les emails Gmail label `0---veille-ia`
2. Extraire les URLs d'articles
3. Mettre à jour `LIST.md` via le workflow `add-url` (sync propre, déduplication, commit+push)
4. Supprimer de `LIST.md` les URLs hors IA / dev applicatif
5. Mettre à la corbeille les emails traités

## Plan
- [x] Charger le contexte prompt-hub obligatoire
- [x] Créer ce fichier de tâche
- [ ] Vérifier / restaurer un état git propre et synchronisé
- [ ] Lire Gmail label `0---veille-ia`
- [ ] Extraire, normaliser et filtrer les URLs pertinentes
- [ ] Mettre à jour `LIST.md`, vérifier, commit+push
- [ ] Mettre à la corbeille les emails traités
- [ ] Mettre à jour memory/version/releases et clôturer

## Review
- Pending
