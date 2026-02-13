# “Engineers are becoming sorcerers” | The future of software development with OpenAI’s Sherwin Wu
**Source**: https://www.lennysnewsletter.com/p/engineers-are-becoming-sorcerers?post_id=186818429
**Date**: Unknown
**Author**: Lenny’s Podcast (show notes)
**Keywords**: Codex adoption, code review, managers, scaffolding, parallel agents

## Elevator pitch
Show notes d’un épisode avec Sherwin Wu (OpenAI API platform): presque tous les ingénieurs utilisent Codex, souvent avec 10–20 agents en parallèle, et l’organisation optimise désormais pour la spécification, la revue ultra-rapide, et la disparition progressive du “scaffolding”.

## Takeaways
- Sherwin Wu indique ~95% d’usage de Codex côté ingénierie API platform.
- Pattern de travail: “fleets” d’agents parallèles (10–20) plutôt qu’un seul.
- Réduction du temps de code review (mentionnée: 10–15 min → 2–3 min) via process/outillage.
- Impacts sur le management: rôle qui se déplace vers priorisation, feedback, design de systèmes.
- Idée clé: “models will eat your scaffolding for breakfast” (les abstractions temporaires deviennent obsolètes vite).

## Synthesis
Le contenu accessible ici est essentiellement une liste de points et de liens, mais il suffit à capter un signal: à l’intérieur d’OpenAI, l’usage des agents de code n’est pas une expérimentation marginale — c’est un mode de production standardisé.

Deux idées ressortent. D’abord, l’industrialisation du parallèle: au lieu d’un agent, des “flottes” de sous-agents spécialisés, ce qui transforme l’ingénierie en orchestration (décomposition, allocation, aggregation, validation). Ensuite, l’accélération des boucles de feedback, avec une code review beaucoup plus courte, ce qui suggère des pratiques de diff plus petits, des conventions d’acceptance criteria plus strictes, ou des outils de vérification plus intégrés.

Enfin, le slogan “models eat scaffolding” pointe un phénomène d’architecture: les couches de glue et d’outillage créées pour compenser les limites d’un modèle peuvent devenir rapidement inutiles quand le modèle progresse. Cela pousse à concevoir des systèmes qui acceptent le changement rapide (interfaces stables, tests, invariants) plutôt que des hacks durables.
