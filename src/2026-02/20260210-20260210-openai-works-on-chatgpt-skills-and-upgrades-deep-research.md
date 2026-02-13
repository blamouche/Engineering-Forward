# OpenAI works on ChatGPT Skills, upgrades Deep Research
**Source**: https://www.testingcatalog.com/openai-works-on-chatgpt-skills-upgrades-deep-research/
**Date**: 2026-02-10
**Author**: Unknown
**Keywords**: ChatGPT, Deep Research, skills, connectors, agent workflows

## Elevator pitch
ChatGPT Deep Research devient une expérience guidée et itérative (contraintes de sources, connecteurs, intervention en cours de run) pendant que des indices suggèrent l’arrivée d’une couche “Skills” installable/partageable.

## Takeaways
- Deep Research passe d’un mode “lancer et attendre” à une session pilotable (ajouter contraintes/requirements en cours).
- Possibilité de limiter la recherche à certains sites (scope control + reproductibilité).
- Connecteurs pour injecter du contexte depuis des apps/espaces de travail (quand le “missing piece” est interne).
- Backend Deep Research migrerait vers GPT‑5.2.
- Apparition d’un UI/popup laissant penser à une bibliothèque de “Skills” importables.

## Synthesis
L’article décrit une évolution produit cohérente: transformer une fonctionnalité de recherche longue en **workflow interactif**, plus proche d’un agent que d’un rapport généré en une fois. Le problème de fond est le même que sur tous les outils “research”: les premiers résultats changent la question. Sans possibilité d’intervenir, l’utilisateur recommence (coût/latence) ou accepte un rapport “trop large”.

Trois ajouts répondent directement à cette friction. (1) Le **pilotage en cours d’exécution**: on peut rediriger, ajouter des exigences, resserrer l’angle. (2) Le **contrôle de périmètre** via une liste de sites: utile quand on sait déjà quelles sources sont légitimes (ou quand on veut de la reproductibilité). (3) Les **connecteurs**: Deep Research devient plus intéressant quand il peut combiner web + contexte de travail (docs, emails, calendriers), au lieu d’un browsing “aveugle”.

Le billet relie aussi ces changements à la stratégie “agentic” d’OpenAI: plutôt que d’améliorer uniquement la qualité du texte, améliorer la boucle (outils + contexte + itération). La migration mentionnée vers GPT‑5.2 s’inscrit dans cette logique.

Enfin, la rumeur “Skills” est notable: si ChatGPT intègre des procédures installables/éditables, on passe d’un assistant qui improvise à un assistant qui **exécute un playbook** (standardisation d’équipes, partage interne, cohérence des résultats). C’est exactement le “middle layer” (entre prompt ad hoc et outil sur-mesure) qui manque souvent aux usages en entreprise.
