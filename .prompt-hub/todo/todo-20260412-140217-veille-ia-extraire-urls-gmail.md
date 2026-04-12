# TODO - Daily veille IA extraire URLs Gmail

- Timestamp: 20260412-140217
- Task: Exécuter la séquence quotidienne veille IA (Gmail -> URLs -> LIST.md -> cleanup -> trash)

## Plan
- [x] Lire les consignes repo (`agents.md`, `.prompt-hub/lessons.md`, `.prompt-hub/memory.md`, `.prompt-hub/releases.md`)
- [x] Vérifier l'état Git du repo
- [x] Tenter l'accès Gmail via `gog`
- [x] Tenter un fallback via le navigateur connecté
- [x] Si bloqué, consigner l'échec, versionner, commit et push pour restaurer un état propre

## Progress
- `gog gmail messages search 'label:0---veille-ia' --max 100 --json --account b.lamouche@gmail.com` a échoué avec `oauth2: invalid_grant` (`Token has been expired or revoked`).
- Le fallback navigateur a aussi échoué: impossible d'attacher Chrome (`Could not find DevToolsActivePort`).
- Aucune lecture d'email possible, donc aucune extraction d'URL, aucun nettoyage de `LIST.md`, aucun email mis à la corbeille.

## Review
- Outcome: failed
- URLs added: 0
- URLs removed: 0
- Emails trashed: 0
- Blocking issue: `gog` nécessite une ré-auth Gmail; le navigateur utilisateur n'était pas attachable au moment du run.
