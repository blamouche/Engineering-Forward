# How I Use Claude Code
**Source**: https://boristane.com/blog/how-i-use-claude-code/
**Date**: Unknown
**Author**: Boris Tane
**Keywords**: Claude Code, planning, workflow, research, annotation cycle

## Elevator pitch
Un workflow “agentic” discipliné: séparer strictement **research → plan → annotations → todo → implémentation**, et ne jamais laisser l’agent coder avant validation d’un plan écrit.

## Takeaways
- Le piège: lancer l’agent directement en implémentation → hypothèses fausses → dette de correction.
- Phase research: lecture profonde du code + rapport écrit persistant (surface de review).
- Phase planning: un `plan.md` versionnable et éditable, plutôt que le plan mode intégré.
- “Annotation cycle”: l’humain annote le plan dans le document; l’agent met à jour sans coder.
- Implémentation ensuite “mécanique”: checklist todo, itération courte et corrections terses.

## Synthesis
L’auteur décrit une méthode de travail qui ressemble à un process d’ingénierie classique, mais optimisé pour un agent de code. La règle d’or est de découpler pensée et frappe clavier: tant que le plan n’est pas validé, l’agent ne touche pas au code.

Le pipeline commence par une phase de research explicite: demander à l’agent de lire en profondeur une zone du repo et d’écrire un rapport (`research.md`). Ce document sert à vérifier la compréhension et à corriger les malentendus avant qu’ils ne contaminent la suite. Ensuite vient le plan (`plan.md`), écrit comme artefact de spécification: approche, chemins de fichiers, snippets, trade-offs.

La partie distinctive est l’“annotation cycle”: l’humain relit le plan dans son éditeur, ajoute des notes inline (contraintes, corrections, préférences, knowledge context), puis renvoie l’agent sur le document avec un garde-fou explicite “don’t implement yet”. Après 1 à 6 itérations, le plan devient une spec alignée sur le codebase et les priorités.

Enfin, on demande une todo list granularisée et on bascule en implémentation, avec une instruction standard: exécuter tout le plan, marquer les tâches complétées, éviter les fioritures, typecheck en continu. En exécution, les retours deviennent brefs (“wider”, “move this to admin app”) car le plan porte déjà l’intention.

Le message de fond: les agents ne remplacent pas l’architecture et le jugement — ils automatisent la partie mécanique. Le plan écrit est le contrat qui rend l’autonomie utile au lieu de chaotique.
