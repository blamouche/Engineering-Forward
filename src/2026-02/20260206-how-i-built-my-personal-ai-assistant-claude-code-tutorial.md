# How I Built My Personal AI Assistant (Claude Code Tutorial)
**Source**: https://open.substack.com/pub/michaelcrist/p/personal-ai-assistant?utm_source=share&utm_medium=android&r=fhb7r
**Date**: Unknown
**Author**: Michael Crist (Substack)
**Keywords**: personal assistant, Claude Code, productivity, GTD, filesystem, workflows

## Elevator pitch
Un guide très concret pour construire un assistant IA « local-first » avec Claude Code : une structure de fichiers (notes, tâches, mémoire) + quelques commandes (/start, /sync, /wrap-up) qui transforment l’IA en opérateur de ton système de travail.

## Takeaways
- Le vrai saut, ce n’est pas « mieux discuter avec une IA », c’est lui donner un accès direct à tes fichiers pour réduire la friction.
- Une architecture simple (Scratch Pad, Daily Notes, Meetings, Task Board, memory.md) suffit à créer de la continuité.
- Des commandes ritualisées cadrent les moments clés : début de journée, synchronisation, clôture.
- L’approche s’inscrit dans l’esprit GTD : sortir les boucles ouvertes de la tête, réduire l’admin.
- Le risque principal est la gouvernance : où tu lances l’outil (périmètre de fichiers) et comment tu supervises les changements.

## Synthesis
L’article raconte un problème familier : l’inflation des to-do lists et la maintenance permanente du système de tâches (tri, pruning, re‑priorisation) qui finit par devenir une anxiété de fond. L’auteur propose un pivot : utiliser Claude Code pour faire disparaître une partie de ce travail administratif en transformant l’IA en « opérateur » de ton environnement de fichiers.

Le point central est la notion d’« aperture » : dans une interface de chat, l’IA reste derrière une petite ouverture, et c’est l’utilisateur qui doit rassembler les documents, rappeler le contexte, et maintenir l’historique. Avec Claude Code, le modèle peut lire/écrire dans un dossier, suivre des liens entre fichiers, et exécuter des routines. L’auteur présente cette continuité comme l’équivalent d’un assistant qui range, synthétise, et met à jour, au lieu d’un interlocuteur qui répond.

La mise en œuvre est volontairement minimaliste : deux notes (Scratch Pad pour la capture brute, Task Board pour la liste structurée), deux dossiers (Daily Notes, Meetings), et un fichier de mémoire pour la continuité. Sur cette base, trois commandes servent de « rituels » et de contrats d’interface : /start (standup du matin, priorisation), /sync (triage en cours de journée : notes, réunions, tâches), /wrap-up (clôture : vérifier les éléments non traités et écrire ce qui compte dans la mémoire). Cette structuration est importante : elle borne les moments où l’IA agit et réduit le risque d’un agent qui « fait un peu de tout, tout le temps ».

Le texte insiste aussi, même si c’est en filigrane, sur la question du périmètre et de la supervision. L’auteur recommande implicitement de lancer l’outil dans un dossier contrôlé (pas dans un répertoire contenant des secrets) et de garder un œil sur les modifications. Autrement dit : l’efficacité vient d’un accès large, mais la sécurité vient d’une surface d’action bien définie.

Pour une équipe produit ou un individu, la leçon la plus réutilisable est la forme : une architecture simple + des points d’entrée explicites + un fichier de mémoire concis. C’est une recette pour passer d’un « chat » à un « système » et, surtout, pour rendre l’IA utile sur des tâches répétitives à faible valeur ajoutée (triage, synthèse, mise à jour) sans complexifier l’outillage.
