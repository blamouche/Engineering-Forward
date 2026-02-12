# Unlocking the Codex harness: how we built the App Server
**Source**: https://openai.com/index/unlocking-the-codex-harness/
**Date**: Unknown
**Author**: OpenAI
**Keywords**: agents, Codex, architecture, JSON-RPC, protocol design, IDE integrations

## Elevator pitch
OpenAI détaille l’App Server de Codex : un runtime/protocole (JSON‑RPC bidirectionnel sur stdio) qui expose le « harness » agentique (threads/turns/items, outils, persistance) pour permettre à des clients variés (TUI, VS Code, desktop, web) de réutiliser le même loop.

## Takeaways
- Besoin initial : réutiliser le même agent loop entre le TUI (CLI) et des surfaces IDE (VS Code) sans tout réécrire.
- Choix de design : JSON-RPC bidirectionnel + notifications de streaming plutôt qu’un simple request/response.
- Trois primitives de conversation : Thread (durable), Turn (unité de travail), Item (événements typés avec lifecycle started/delta/completed).
- App Server comme process long‑vivant qui héberge des « core threads » et gère persistance, config/auth, exécution d’outils/extensions.
- Objectif plateforme : stabilité/backward compatibility pour partenaires (JetBrains, Xcode) et produits internes.

## Synthesis
Ce billet explique comment OpenAI a « productisé » l’expérience Codex en séparant le loop agentique (le harness) de ses interfaces. Le point de départ est pragmatique : Codex CLI (TUI) existait déjà, mais lorsqu’il a fallu construire une extension VS Code et d’autres surfaces, ré-implémenter le loop à chaque fois devenait coûteux et incohérent. L’App Server apparaît alors comme une couche standard : un protocole + un process qui encapsulent la logique d’agent, la persistance, l’exécution d’outils et l’état d’auth/config.

La contribution la plus intéressante est la formalisation des primitives d’interaction. Plutôt que de modéliser l’agent comme un « appel modèle → réponse », OpenAI découpe l’expérience en items (unités atomiques typées : message agent, exécution d’outil, diff, demande d’approbation…), regroupés en turns (une requête utilisateur qui déclenche une séquence d’items), eux‑mêmes stockés dans des threads durables (une conversation persistante, archivable, forkable). Chaque item suit un cycle de vie (started → deltas optionnels → completed), ce qui rend le streaming et le rendu UI plus robustes.

Côté transport, JSON‑RPC sur stdio (JSONL) est un choix orienté intégrateurs : c’est simple à binder dans beaucoup de langages et adapté à un modèle « client lance un binaire server et échange via pipes ». La bidirectionnalité est clé, car un agent n’est pas autonome sans interaction : demandes d’approbation, besoin d’inputs, pauses/reprises. Le billet décrit aussi comment l’App Server transforme des événements internes bas niveau en notifications « UI‑ready », réduisant la complexité côté clients.

Enfin, le texte met en lumière un enjeu produit : la stabilité. Une fois que des partenaires et plusieurs produits dépendent d’un runtime agentique, l’API devient un contrat de long terme. L’App Server est conçu pour évoluer sans casser les clients, ce qui permet de pousser des améliorations (ex. compaction, nouveaux paramètres) sans attendre des releases synchronisées de toutes les interfaces.

Pour quiconque construit une plateforme d’agents, la leçon est claire : l’architecture doit capturer la réalité d’un agent loop (streaming, outils, approvals, persistance) et fournir des primitives stables que plusieurs UI peuvent consommer. En pratique, cela ressemble plus à un protocole événementiel qu’à une simple API de complétion.
