# Unlocking the Codex harness: how we built the App Server
**Source**: https://openai.com/index/unlocking-the-codex-harness/
**Date**: Unknown
**Author**: Unknown
**Keywords**: Codex, agents, app server, JSON-RPC, architecture, IDE integration, protocol

## Elevator pitch
OpenAI décrit l’App Server de Codex: un process long-vivant et un protocole JSON-RPC bidirectionnel (sur stdio) qui expose le “harness” agentique de Codex à différents clients (TUI, IDE, desktop, web), en standardisant la persistance, les événements, et les boucles d’approbation.

## Takeaways
- Motivation: réutiliser le même agent loop (harness) sur plusieurs surfaces (TUI, VS Code, desktop) sans ré-implémenter.
- Choix clé: abandon MCP pour cette couche, au profit d’un protocole JSON-RPC mieux adapté aux sémantiques d’UI/streaming.
- Primitives de conversation: Item (avec lifecycle), Turn, Thread (persisté, reconnectable).
- Architecture: process App Server qui héberge des “core threads” et traduit les événements bas niveau en notifications stables côté client.
- Positionnement: App Server comme méthode d’intégration “full-fidelity” vs alternatives (MCP server, CLI one-shot, libs).

## Synthesis
Le post raconte une histoire familière dans les produits agents: au départ, un outil existe sur une surface (ici un TUI/CLI), puis on veut l’amener ailleurs (IDE, desktop, web) sans dupliquer la logique agentique. La difficulté n’est pas seulement d’envoyer une requête et de recevoir une réponse: une boucle agent implique exploration, streaming de progression, exécution d’outils, production d’artefacts (diffs), et parfois des demandes d’approbation qui suspendent l’exécution.

L’App Server est la réponse d’OpenAI à ce problème d’architecture. Il s’agit d’un protocole JSON-RPC (sur stdio, en JSONL) et d’un process long-vivant qui héberge Codex “core” et gère la persistance des conversations. L’idée est que les clients deviennent des “renderers” et contrôleurs, pendant que le serveur conserve l’état et orchestre la boucle agent.

Un point notable est l’accent mis sur des primitives simples mais robustes: Item, Turn, Thread. Un Item a un lifecycle explicite (started → delta(s) → completed) ce qui permet de rendre une UI progressive et streaming sans ambiguïtés. Un Turn encapsule l’unité de travail déclenchée par l’utilisateur et peut contenir de nombreux items (tool calls, approvals, messages). Un Thread est le conteneur durable, ce qui rend possible la reconnexion et une timeline cohérente.

Côté exécution, le serveur agit comme couche de traduction: il reçoit des requêtes client, les transforme en opérations sur le runtime core, écoute le stream d’événements internes, puis renvoie un set réduit de notifications “UI-ready” stable dans le temps. Ce découplage est essentiel pour permettre de faire évoluer l’implémentation interne sans casser les intégrations.

Le post décrit aussi des patterns d’intégration: clients locaux qui embarquent un binaire App Server, web runtime qui lance le serveur dans un container et stream les événements au navigateur, et une refonte envisagée du TUI pour qu’il devienne un client comme les autres.

Au final, l’App Server est présenté comme un choix de plateforme: si l’on veut un agent “multi-surface” cohérent, il faut une API qui transporte l’expérience agent (événements, streaming, approbations, artefacts) et pas seulement du texte. C’est aussi une façon de rendre l’écosystème intégrable par des partenaires tout en gardant compatibilité et évolutivité.
