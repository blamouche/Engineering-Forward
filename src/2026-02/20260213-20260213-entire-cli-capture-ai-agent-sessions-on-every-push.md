# Entire CLI: capture AI agent sessions on every push
**Source**: https://github.com/entireio/cli
**Date**: Unknown
**Author**: Entire
**Keywords**: developer tooling, git hooks, agent transcripts, checkpoints, traceability

## Elevator pitch
Entire ajoute une couche “observabilité des agents” à Git: il capture transcripts + fichiers touchés à chaque push/commit, crée des checkpoints rewindables, et garde l’historique de code propre en stockant le contexte sur une branche dédiée.

## Takeaways
- S’intègre via hooks Git et suit les sessions Claude Code / Gemini CLI.
- Stocke la metadata (prompts/réponses, fichiers modifiés) sur `entire/checkpoints/v1` plutôt que polluer l’historique principal.
- Deux stratégies: manual-commit (par défaut) vs auto-commit (checkpoint après chaque réponse).
- Commandes clés: `status`, `rewind`, `resume`, `doctor`, `reset`.
- Positionnement: compréhension du “pourquoi”, audit/compliance, onboarding et recovery rapide quand un agent déraille.

## Synthesis
Le projet Entire part d’un problème pratique: quand du code est écrit avec des agents, ce qui manque souvent au futur lecteur, c’est le **contexte** (intention, contraintes, étapes, essais/erreurs). Git capture le “quoi” (diff) mais pas le “pourquoi”.

Entire propose de combler ce trou en branchant la capture au workflow Git: des hooks enregistrent les sessions d’agent et créent des checkpoints. L’idée de conserver le contexte sur une branche séparée est intéressante: on obtient une traçabilité riche sans transformer l’historique principal en suite de commits artificiels. La fonctionnalité `rewind` matérialise aussi une nécessité des workflows agentiques: revenir à un point stable rapidement, puis reprendre.

Le design explicite les compromis: auto-commit offre une granularité maximale mais peut être intrusif sur une branche active; manual-commit garde le contrôle humain. Enfin, au-delà de la productivité, l’outil se positionne sur des enjeux de qualité: auditabilité, compréhension, et réduction du coût de récupération — trois sujets qui deviennent critiques quand la production de changements s’accélère.
