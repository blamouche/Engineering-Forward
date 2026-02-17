# EP202: MCP vs RAG vs AI Agents
**Source**: https://blog.bytebytego.com/p/ep202-mcp-vs-rag-vs-ai-agents
**Date**: Unknown
**Author**: ByteByteGo
**Keywords**: MCP, RAG, AI agents, routing, skills, system design

## Elevator pitch
MCP, RAG et agents ne sont pas des “alternatives” : MCP standardise l’accès aux outils, RAG injecte de la connaissance fraîche/privée, et les agents orchestrent des boucles action‑réflexion; combinés, ils décrivent une pile complète pour passer d’un LLM qui répond à un système qui agit.

## Takeaways
- MCP (Model Context Protocol) = couche d’intégration: découverte/invocation d’outils et retours structurés.
- RAG = couche “runtime knowledge”: récupérer des docs et les fournir au modèle pour réduire l’hallucination sans retraining.
- Agents = couche d’exécution: planifier, appeler des outils, itérer, déléguer, mémoriser.
- Le “système GPT‑5” est décrit comme un router + plusieurs modes (instant/thinking/auto/pro) avec safeguards en parallèle.
- “Skills” = playbooks chargés à la demande pour éviter les prompts monolithiques et stabiliser le comportement.

## Synthesis
Le post cherche surtout à clarifier des termes qui se mélangent dans les discussions. Il place MCP, RAG et agents à des niveaux différents.

MCP est présenté comme un protocole d’interface entre un modèle et des systèmes externes (bases de données, filesystem, GitHub, Slack, APIs internes). L’objectif n’est pas de décider “quoi faire”, mais d’éviter que chaque application réinvente de la glue code différente: on standardise la façon d’exposer un outil, de le découvrir et de récupérer des résultats structurés.

RAG adresse un autre problème: la connaissance du modèle au moment de répondre. Plutôt que de retrainer, on récupère des documents pertinents (privés, récents, internes) et on les injecte dans le contexte. Le bénéfice attendu est la réduction des hallucinations et l’accès à des informations non présentes dans les poids. La limite clé est qu’un pipeline RAG n’agit pas sur le monde: il améliore la qualité de la réponse, pas l’exécution.

Les agents, eux, sont définis par une boucle: observer → raisonner → décider → agir → répéter. Un agent peut appeler des outils (souvent via MCP), s’appuyer sur RAG pour se “grounder”, stocker de la mémoire et éventuellement déléguer. On passe alors d’un LLM “one‑shot” à un système qui accomplit une tâche.

Le post ajoute un schéma (vulgarisation) sur le routage des requêtes dans un système type GPT‑5: des modes orientés latence (instant), raisonnement (thinking), routage automatique (auto) et un mode qui augmente la qualité via plusieurs tentatives + sélection (pro). L’idée générale est que la “plateforme” n’est pas un seul modèle mais une combinaison de modèles et de garde‑fous.

Enfin, il introduit une approche “skills” pour agents: au lieu d’un prompt énorme qui dégrade la performance, on maintient un catalogue de procédures courtes, chargées à la demande selon la tâche. Cela réduit la taille de contexte, améliore la cohérence, et rapproche le design d’un système modulaire plutôt qu’un unique prompt fragile.
