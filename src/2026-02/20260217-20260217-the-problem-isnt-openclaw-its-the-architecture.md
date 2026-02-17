# the problem isn’t OpenClaw. it’s the architecture.
**Source**: https://www.vulnu.com/p/the-problem-isnt-openclaw-its-the-architecture
**Date**: Unknown
**Author**: Unknown
**Keywords**: agent security, prompt injection, plugin marketplaces, least privilege, sandboxing

## Elevator pitch
Les incidents de skills malveillants autour d’OpenClaw illustrent surtout une vérité plus large : dès qu’un agent peut ingérer du contenu non fiable, accéder à des données privées et agir/communiquer, la sécurité ne peut plus reposer sur des “prompts‑policies” mais sur une architecture de confinement, de moindre privilège et d’audit.

## Takeaways
- OpenClaw est présenté comme un “canari” : le même scénario se reproduira pour tout écosystème agent+tools+marketplace.
- “Prompts are not policies” : les instructions ne sont pas des frontières de sécurité; l’injection de prompt est un risque opérationnel.
- La “lethal trifecta” (accès données privées + ingestion contenu non fiable + capacité de communication) définit une zone de danger.
- Les agents changent le mode d’échec: d’une réponse fausse à une action fausse (commandes, fichiers, infra, CI, SQL…).
- Les contre‑mesures clés: sandboxing réel, scoping des credentials, restriction/allowlist des outils, logs d’actions, et gestion des skills comme des dépendances.

## Synthesis
L’auteur prend les polémiques récentes autour d’OpenClaw (et notamment la circulation de “skills” potentiellement malveillants) comme point de départ, mais refuse la conclusion facile “OpenClaw est le problème”. Pour lui, l’incident révèle surtout un nouveau type de surface d’attaque qui apparaît dès qu’on combine trois ingrédients: des agents autonomes capables d’utiliser des outils, un mécanisme d’installation simple de plugins/skills, et des utilisateurs qui veulent que “ça marche” sans lire dans le détail — exactement le terrain que les attaquants préfèrent.

Le cœur du message est une mise en garde contre une confusion fréquente: écrire un bon system prompt et l’appeler “guardrails”. Un prompt peut orienter le comportement, mais ne constitue pas une barrière de sécurité. Lorsque l’agent lit du contenu non fiable (web, emails, tickets, docs), l’injection de prompt devient un risque concret: un texte adversarial peut pousser l’agent à contourner l’intention initiale. Dans ce contexte, l’auteur reprend la notion de “lethal trifecta” (accès à des données privées, ingestion de contenu non fiable, capacité de communiquer vers l’extérieur) comme un cadre simple pour décider si un agent est dangereux.

La thèse s’élargit ensuite: l’accès aux outils amplifie fortement le “blast radius”. Une hallucination dans un chatbot est surtout un problème de qualité; une hallucination dans un agent peut produire une action destructrice. Les exemples donnés (shell commands, changements Terraform, requêtes SQL, étapes CI) montrent comment une simple sortie textuelle peut devenir une injection indirecte si elle est réutilisée sans validation (improper output handling). L’auteur rapproche ces risques des catégories OWASP (prompt injection, supply chain, excessive agency), en soulignant que les marketplaces de skills ressemblent à des registres de packages — avec les mêmes risques de dépendances compromises.

La conclusion propose un modèle d’exploitation “adulte” des agents: les traiter comme de l’infrastructure de production, pas comme une app de productivité. Concrètement: exécuter dans un environnement réellement confiné (VM, container restreint, compte OS séparé), distribuer des credentials à privilèges minimaux et à durée limitée, restreindre les outils via des contrôles techniques (allowlists/approbations), instrumenter et auditer les actions (pas seulement la conversation), et appliquer à l’écosystème de skills une discipline “dépendances” (revue, curation, provenance). L’idée n’est pas d’arrêter la vague des agents, mais de s’assurer qu’elle arrive avec des frontières de sécurité adaptées à leur pouvoir d’exécution.
