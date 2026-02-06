# How I Built My Personal AI Assistant (Claude Code Tutorial)
**Source**: https://michaelcrist.substack.com/p/personal-ai-assistant
**Date**: Unknown
**Author**: Michael Crist
**Keywords**: Claude Code, personal assistant, productivity, Obsidian, workflows, commands

## Elevator pitch
Un tutoriel pragmatique pour construire un “assistant personnel” basé sur Claude Code et des fichiers locaux (type Obsidian), en s’appuyant sur une structure simple (notes quotidiennes + mémoire) et trois commandes (/start, /sync, /wrap-up) afin de réduire le coût mental de la gestion de tâches.

## Takeaways
- Le cœur du système: des notes en fichiers + un agent capable de lire/écrire dedans (le « passage du keyhole à la pièce entière »).
- Une séparation utile: capture brute (scratchpad) vs journal quotidien (log) vs mémoire “curated” pour la continuité.
- Des commandes comme “raccourcis de prompt” (fichiers dans un dossier dédié) pour rendre le workflow reproductible.
- L’objectif n’est pas d’optimiser la todo-list, mais de supprimer l’overhead (tri, pruning, re-copie) qui crée de l’anxiété.
- Beaucoup de valeur vient de la recherche/relance contextuelle: retrouver l’info dans des notes/meetings passés au lieu de “scroller et chercher”.

## Synthesis
L’article part d’un constat très réaliste: la productivité se noie souvent dans l’administration de la productivité. En multipliant les listes, les vues (“Today/This Week/Waiting/Done…”) et les rituels de nettoyage, on finit par optimiser la gestion du backlog plutôt que l’exécution réelle. L’auteur raconte comment l’“inbox zéro” appliquée à des todo-lists devient une anxiété de fond.

Son déclic vient d’un usage “agentic” de Claude Code: plutôt que d’interagir via une petite interface de chat, l’agent dispose d’un accès direct au système de fichiers où vivent les notes. Cette bascule est présentée comme un changement d’interface cognitive: l’utilisateur n’est plus le seul curateur qui doit rassembler manuellement les bons documents; l’agent peut parcourir, relier, résumer et produire des mises à jour de manière autonome.

Le setup proposé est volontairement minimaliste: deux dossiers (notes quotidiennes et meetings), deux notes (scratch pad pour la capture et task board), plus un fichier mémoire maintenu au fil du temps. À cela s’ajoutent trois commandes.

- /start: début de journée, revue des priorités, surfacing des items vieillissants, prise en compte du contexte mémorisé.
- /sync: pendant la journée, ingestion de la capture brute, mise à jour des tâches, traitement des transcriptions de meeting.
- /wrap-up: fin de journée, vérification qu’il ne reste pas de “non traités”, consolidation et écriture dans la mémoire.

Ce qui ressort, c’est une architecture de workflow qui s’apparente à un mini-système GTD “agentisé”: la capture est frictionless, le traitement est délégué, et la continuité est garantie par une mémoire explicitement maintenue. Le tutoriel insiste aussi sur une vertu opérationnelle: ces commandes sont des fichiers (dans un dossier de commandes), donc versionnables, ajustables, et faciles à faire évoluer.

Enfin, au-delà de Claude, le pattern est transférable: si l’on veut des assistants utiles, il faut leur donner des primitives stables (fichiers, structure, conventions) et des routines explicites. Les gains viennent moins d’un prompt miracle que d’un système répété quotidiennement, où l’agent fait surtout le “travail invisible”: retrouver, résumer, ranger, et rappeler.
