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
- [x] Vérifier / restaurer un état git propre et synchronisé
- [x] Lire Gmail label `0---veille-ia`
- [x] Extraire, normaliser et filtrer les URLs pertinentes
- [x] Mettre à jour `LIST.md`, vérifier, commit+push
- [x] Mettre à la corbeille les emails traités
- [x] Mettre à jour memory/version/releases et clôturer

## Review
- Done: 4 emails, 12 URLs ajoutées, 1 URLs supprimées.
