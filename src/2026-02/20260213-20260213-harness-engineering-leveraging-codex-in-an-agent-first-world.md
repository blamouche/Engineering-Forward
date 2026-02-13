# Harness engineering: leveraging Codex in an agent-first world
**Source**: https://openai.com/index/harness-engineering/
**Date**: Unknown
**Author**: OpenAI
**Keywords**: Codex, agent-first engineering, scaffolding, feedback loops, repo knowledge

## Elevator pitch
OpenAI raconte comment une petite équipe a livré un produit interne avec 0 ligne de code écrite “à la main” — et pourquoi, dans un monde d’agents, le job d’ingénieur devient surtout de concevoir des environnements, contraintes et boucles de feedback.

## Takeaways
- Produit construit en ~1/10 du temps, avec ~1M LOC agent-générées et ~1500 PRs, via Codex.
- Le goulot d’étranglement se déplace: moins “écrire du code”, plus **spécifier** et rendre le système “agent-legible”.
- La connaissance doit être dans le repo (AGENTS.md comme table des matières + docs structurées), pas dans des chats/Google Docs.
- Investir dans la legibility: UI/logs/metrics accessibles aux agents (CDP, snapshots, observabilité éphémère par worktree).
- Enforcer des invariants mécaniques (linters, tests structurels, “taste invariants”) plutôt que micromanager l’implémentation.

## Synthesis
Le texte décrit une expérience volontairement extrême: construire et opérer un produit sans code humain, pour découvrir ce qui change quand les agents écrivent tout (logiciel, tests, CI, docs, outillage). La conclusion centrale: le rôle de l’ingénieur se “rehausse” vers la conception de **scaffolding** et de boucles d’amélioration continue.

Le pattern d’apprentissage est depth-first: quand un agent échoue, la solution n’est pas “retry” mais “quelle capacité manque au système?” (outils, abstractions, contraintes, observabilité). Cela conduit à rendre l’application et son runtime lisibles par l’agent: bootable par worktree, pilotable via navigateur, logs/metrics/traces queryables, environnement isolé par tâche.

Un deuxième pilier est la gestion du contexte. OpenAI insiste sur l’idée de donner une **carte** plutôt qu’un manuel: un AGENTS.md court qui pointe vers une base de connaissances structurée (docs/, plans d’exécution versionnés, qualité/grades). Le repo devient le “system of record” pour l’agent; ce qui est hors repo est, pour l’agent, pratiquement inexistant.

Enfin, la cohérence à long terme nécessite de la mécanique: invariants d’architecture (couches, dépendances autorisées), préférences encodées en lints et messages d’erreur “didactiques”, et un processus de “garbage collection” (agents de doc-gardening, refactors réguliers). Le parallèle avec Rust est explicite: on ne prouve pas la correction business, mais on élimine des classes d’erreurs et on augmente la vitesse sans chaos.

En filigrane, c’est un guide de stratégie: si la ressource rare est l’attention humaine, il faut investir là où elle se multiplie — structures, tests, métriques, contraintes — pour que le flot de changements agentiques reste fiable.
